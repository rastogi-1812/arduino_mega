#!/usr/bin/env python3
"""
Parse STM32H747xx CMSIS device header and emit a structured JSON register catalog.
Extracts:
  1. Peripheral register typedefs (register name, offset, description)
  2. Peripheral base addresses and instance pointers
  3. Bitfield #defines (position, mask, description) grouped by peripheral register
"""
import re, json, sys
from collections import OrderedDict

HEADER = "stm32h747xx.h"

with open(HEADER, "r", encoding="utf-8", errors="replace") as f:
    raw = f.read()

# ────────────────────────────────────────────────────────
# 1. Parse typedef structs → register maps
# ────────────────────────────────────────────────────────
# Match: typedef struct { ... } PERIPH_TypeDef;
struct_re = re.compile(
    r'typedef\s+struct\s*\{(.*?)\}\s*(\w+TypeDef)\s*;',
    re.DOTALL
)
# Match individual register lines inside structs (with comments)
reg_line_re = re.compile(
    r'(?:__IO|__I|__O)\s+uint32_t\s+'
    r'(\w+(?:\[\d+\])?)\s*;'
    r'\s*/\*!?<?\s*(.*?)\s*\*/',
    re.DOTALL
)
# Match individual register lines WITHOUT comments (e.g. ETH_TypeDef)
reg_line_bare_re = re.compile(
    r'(?:__IO|__I|__O)\s+uint32_t\s+(\w+(?:\[\d+\])?)\s*;'
)
# Also match reserved / padding lines
reserved_re = re.compile(
    r'uint32_t\s+(RESERVED\w*(?:\[\d+\])?)\s*;'
    r'\s*/\*!?\s*(.*?)\s*\*/',
    re.DOTALL
)
offset_re = re.compile(r'(?:Address\s+)?offset\s*:\s*(0x[0-9A-Fa-f]+)|(?:^|\s)([0-9A-Fa-f]{3,4})h(?:\s|$)', re.I)
array_re = re.compile(r'(\w+)\[(\d+)\]')

typedefs = {}
for m in struct_re.finditer(raw):
    body, name = m.group(1), m.group(2)
    regs = []
    # First try to extract register fields with comments
    for rm in reg_line_re.finditer(body):
        rname = rm.group(1).strip()
        desc = re.sub(r'\s+', ' ', rm.group(2).strip())
        off_m = offset_re.search(desc)
        offset_str = None
        if off_m:
            if off_m.group(1):
                offset_str = off_m.group(1)
            elif off_m.group(2):
                offset_str = "0x" + off_m.group(2)
        regs.append({"name": rname, "offset": offset_str, "description": desc})
    # Fallback: if no commented fields found, try bare fields (e.g. ETH)
    if not regs:
        for rm in reg_line_bare_re.finditer(body):
            rname = rm.group(1).strip()
            if rname.startswith("RESERVED"):
                continue
            regs.append({"name": rname, "offset": None, "description": ""})
    if regs:
        typedefs[name] = regs

# ────────────────────────────────────────────────────────
# 2. Parse base-address #defines
# ────────────────────────────────────────────────────────
base_re = re.compile(
    r'#define\s+(\w+(?:_BASE|_PERIPH_BASE))\s+\(([^)]+)\)\s*(?:/\*!?\s*(.*?)\s*\*/)?'
)
# Also match bare-symbol aliases:  #define D2_APB1PERIPH_BASE  PERIPH_BASE
base_bare_re = re.compile(
    r'#define\s+(\w+(?:_BASE|_PERIPH_BASE))\s+(\w+(?:_BASE|_PERIPH_BASE))\s*(?:/\*!?\s*(.*?)\s*\*/)?'
)
base_addrs = {}
for m in base_re.finditer(raw):
    name, expr, desc = m.group(1), m.group(2).strip(), (m.group(3) or "").strip()
    base_addrs[name] = {"expression": expr, "description": desc}
for m in base_bare_re.finditer(raw):
    name, expr, desc = m.group(1), m.group(2).strip(), (m.group(3) or "").strip()
    if name not in base_addrs:
        base_addrs[name] = {"expression": expr, "description": desc}

# Resolve simple numeric bases
def try_resolve(expr, depth=0):
    if depth > 12:
        return None
    expr = expr.strip()
    # pure hex: 0x40040000UL
    hm = re.fullmatch(r'(0x[0-9a-fA-F]+)\s*U?L?', expr)
    if hm:
        return int(hm.group(1), 16)
    # A + 0xNNNUL  or  A + 0xNNN
    pm = re.fullmatch(r'(\w+)\s*\+\s*(0x[0-9a-fA-F]+)\s*U?L?', expr)
    if pm:
        parent = try_resolve(base_addrs.get(pm.group(1), {}).get("expression", ""), depth+1)
        if parent is not None:
            return parent + int(pm.group(2), 16)
    # Just a symbol (may need further resolution)
    if expr in base_addrs:
        return try_resolve(base_addrs[expr].get("expression", ""), depth+1)
    return None

resolved_bases = {}
for name, info in base_addrs.items():
    val = try_resolve(info["expression"])
    if val is not None:
        resolved_bases[name] = f"0x{val:08X}"

# ────────────────────────────────────────────────────────
# 3. Parse instance #defines  → map symbol to TypeDef + base
# ────────────────────────────────────────────────────────
instance_re = re.compile(
    r'#define\s+(\w+)\s+\(\((\w+TypeDef)\s*\*\)\s*(\w+)\s*\)'
)
instances = {}
for m in instance_re.finditer(raw):
    sym, td, base_name = m.group(1), m.group(2), m.group(3)
    addr = resolved_bases.get(base_name)
    instances[sym] = {"typedef": td, "base_define": base_name, "base_address": addr}

# ────────────────────────────────────────────────────────
# 4. Parse bitfield #defines
# ────────────────────────────────────────────────────────
# Match: #define ADC_ISR_ADRDY_Pos  (0U)
pos_re = re.compile(r'#define\s+(\w+)_Pos\s+\((\d+)U?\)')
# Match: #define ADC_ISR_ADRDY_Msk  (0x1UL << ADC_ISR_ADRDY_Pos)  /*!< 0x00000001 */
msk_re = re.compile(
    r'#define\s+(\w+)_Msk\s+\((0x[0-9a-fA-F]+)U?L?\s*<<\s*\w+\)\s*'
    r'(?:/\*!?\s*(0x[0-9a-fA-F]+)\s*\*/)?'
)
# Match: #define ADC_ISR_ADRDY   ADC_ISR_ADRDY_Msk   /*!< description */
val_re = re.compile(
    r'#define\s+(\w+)\s+\1_Msk\s+'
    r'(?:/\*!?<?\s*(.*?)\s*\*/)?'
)
# Collect positions
positions = {}
for m in pos_re.finditer(raw):
    positions[m.group(1)] = int(m.group(2))

masks_raw = {}
for m in msk_re.finditer(raw):
    name = m.group(1)
    masks_raw[name] = m.group(3) or None  # resolved mask hex from comment

descs = {}
for m in val_re.finditer(raw):
    name, desc = m.group(1), (m.group(2) or "").strip()
    descs[name] = desc

# Group bitfields by peripheral_register prefix
# e.g. ADC_ISR_ADRDY → peripheral=ADC, register=ISR, field=ADRDY
# For multi-underscore peripherals (USB_OTG, FMC_Bank1E, etc.) we need longest-prefix matching.

# Collect all known peripheral prefixes from typedefs, sorted longest-first for greedy match
_all_prefixes = set()
for td_name in typedefs:
    prefix = td_name
    for suffix in ("_ClockCalibrationUnit_TypeDef", "_GlobalTypeDef", "_TypeDef", "TypeDef"):
        if prefix.endswith(suffix):
            prefix = prefix[:-len(suffix)]
            break
    _all_prefixes.add(prefix)
_sorted_prefixes = sorted(_all_prefixes, key=lambda x: -len(x))

bitfields_by_periph = {}
for name, pos in positions.items():
    # Try longest-prefix match against known peripheral names
    matched_prefix = None
    remainder = None
    for pfx in _sorted_prefixes:
        if name.startswith(pfx + "_"):
            matched_prefix = pfx
            remainder = name[len(pfx)+1:]
            break
    if not matched_prefix:
        # Fallback: simple split
        parts = name.split('_', 2)
        if len(parts) < 3:
            continue
        matched_prefix = parts[0]
        remainder = '_'.join(parts[1:])

    reg_parts = remainder.rsplit('_', 1)
    if len(reg_parts) == 2:
        regname, fieldname = reg_parts
    else:
        regname, fieldname = remainder, remainder
    mask = masks_raw.get(name)
    desc = descs.get(name, "")
    entry = {"field": fieldname, "pos": pos, "description": desc}
    if mask:
        entry["mask"] = mask
    bitfields_by_periph.setdefault(matched_prefix, {}).setdefault(regname, []).append(entry)

# ────────────────────────────────────────────────────────
# 5. Assemble final JSON
# ────────────────────────────────────────────────────────
# Build peripheral catalog keyed by instance name
peripherals_out = {}
for sym, info in sorted(instances.items()):
    td = info["typedef"]
    reg_list = typedefs.get(td)
    entry = {
        "instance": sym,
        "typedef": td,
        "base_address": info.get("base_address"),
    }
    if reg_list:
        entry["registers"] = reg_list
    peripherals_out[sym] = entry

# Attach bitfields to the catalog
# Map typedef prefix → bitfield prefix  (e.g. ADC_TypeDef → ADC, I2C_TypeDef → I2C)
td_prefix_map = {}
for td_name in typedefs:
    # Strip known suffixes in order of specificity
    prefix = td_name
    for suffix in ("_ClockCalibrationUnit_TypeDef", "_GlobalTypeDef", "_TypeDef", "TypeDef"):
        if prefix.endswith(suffix):
            prefix = prefix[:-len(suffix)]
            break
    td_prefix_map[td_name] = prefix

for sym, entry in peripherals_out.items():
    td = entry["typedef"]
    prefix = td_prefix_map.get(td)
    if prefix and prefix in bitfields_by_periph:
        entry["bitfields"] = bitfields_by_periph[prefix]

# Also emit standalone bitfield groups not tied to an instance
standalone_bitfield_periphs = set(bitfields_by_periph.keys()) - set(td_prefix_map.values())

output = {
    "_meta": {
        "description": "Auto-generated peripheral register and bitfield catalog for STM32H747XIH6 (Arduino GIGA R1 WiFi)",
        "source": "stm32h747xx.h CMSIS device header (STMicroelectronics cmsis_device_h7)",
        "generated_for": "Driver implementation — provides full register maps, offsets, and bitfield definitions",
        "companion_to": "arduino_giga_r1_wifi_knowledgebase.json"
    },
    "memory_base_addresses": {k: v for k, v in sorted(resolved_bases.items()) if not k.startswith("DMAMUX") or "Channel" not in k},
    "peripheral_instances": peripherals_out,
}

# Add standalone bitfields (like FLASH, EXTI, etc. that may have extra defines)
if standalone_bitfield_periphs:
    extra = {}
    for p in sorted(standalone_bitfield_periphs):
        extra[p] = bitfields_by_periph[p]
    output["additional_bitfields"] = extra

with open("arduino_giga_r1_wifi_registers.json", "w") as f:
    json.dump(output, f, indent=2, default=str)

# Stats
n_periphs = len(peripherals_out)
n_regs = sum(len(e.get("registers",[])) for e in peripherals_out.values())
n_bf = sum(sum(len(fields) for fields in regs.values()) for regs in bitfields_by_periph.values())
print(f"Done. {n_periphs} peripheral instances, {n_regs} register entries, {n_bf} bitfield entries.")
