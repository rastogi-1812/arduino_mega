# Arduino GIGA R1 WiFi — Comprehensive AI Knowledgebase

> **SKU:** ABX00063  
> **Product Page:** <https://docs.arduino.cc/hardware/giga-r1-wifi/>  
> **User Manual / Cheat Sheet:** <https://docs.arduino.cc/tutorials/giga-r1-wifi/cheat-sheet>  
> **Datasheet PDF:** ABX00063-datasheet.pdf  
> **MCU Datasheet:** STM32H747XI (DS12930)

---

## 1. Board Overview

The Arduino GIGA R1 WiFi is a high-performance development board in the **Arduino Mega form factor**. It combines the dual-core STM32H747XI microcontroller (same as the Portenta H7) with Wi-Fi/Bluetooth connectivity, 76 GPIOs, audio I/O, camera and display connectors, USB host capability, and extensive memory — all accessible through standard pin headers.

### Target Applications

- 3D Printing controller
- Audio / Signal Processing
- Data Acquisition Devices
- Robotics
- Machine Learning at the edge
- IoT (via Arduino Cloud)
- Motor Control

---

## 2. Microcontroller — STM32H747XIH6

| Parameter | Value |
|---|---|
| **Manufacturer** | STMicroelectronics |
| **Core** | Dual-core: Arm Cortex-M7 + Arm Cortex-M4 |
| **Cortex-M7 Clock** | Up to **480 MHz** |
| **Cortex-M4 Clock** | Up to **240 MHz** |
| **FPU** | M7: double-precision; M4: single-precision |
| **DSP** | Full set of DSP instructions on both cores |
| **MPU** | Memory Protection Unit on both cores |
| **Architecture** | 32-bit ARMv7E-M |
| **Internal Flash** | 2 MB (dual-bank) |
| **Internal SRAM** | 1 MB total (192 KB TCM RAM + up to 864 KB user SRAM + 4 KB backup SRAM) |
| **Operating Voltage** | 1.62 V to 3.6 V |
| **Temperature Range** | -40 °C to +85 °C |
| **RTOS** | Mbed OS (Arduino Mbed OS GIGA Board Package) |

### Dual-Core Operation

- The M7 and M4 cores can be programmed **independently**.
- Communication between cores uses **Remote Procedure Call (RPC)**.
- You can run **Arduino compiled code** on one core and **MicroPython** on the other simultaneously.
- Both cores share the same flash and SRAM but have separate NVIC instances (up to 150 maskable interrupt channels each).

### Memory Map (Internal to STM32H747XI)

| Region | Size | Notes |
|---|---|---|
| ITCM RAM | 64 KB | Tightly-coupled to M7, instruction execution |
| DTCM RAM | 128 KB | Tightly-coupled to M7, data |
| AXI SRAM | 512 KB | Accessible by all bus masters |
| SRAM1 | 128 KB | D2 domain |
| SRAM2 | 128 KB | D2 domain |
| SRAM3 | 32 KB | D2 domain |
| SRAM4 | 64 KB | D3 domain |
| Backup SRAM | 4 KB | Battery-backed |
| Flash | 2 × 1 MB banks | Dual-bank configuration |

### Power Domains

The STM32H747XI organizes peripherals into three power domains:

- **D1 Domain** — Cortex-M7 core, AXI SRAM, LTDC, DMA2D, MDMA, JPEG codec, FMC, QUADSPI, Flash
- **D2 Domain** — Cortex-M4 core, DMA1/DMA2, most communication peripherals (UART, SPI, I2C, USB, Ethernet, SDMMC, CAN), SRAM1-3
- **D3 Domain** — BDMA, LPUART, LPTIM, I2C4, SPI6, SRAM4, RTC, RCC

### Low-Power Modes

| Mode | Description |
|---|---|
| CSleep | CPU clock stopped |
| CStop | CPU subsystem clock stopped |
| DStop | Domain bus matrix clock stopped |
| Stop | System clock stopped |
| DStandby | Domain powered down |
| Standby | System powered down |

### Clock Sources

| Source | Frequency |
|---|---|
| HSI (internal) | 64 MHz |
| HSI48 (internal) | 48 MHz |
| CSI (internal) | 4 MHz |
| LSI (internal) | 32 kHz |
| HSE (external) | 4–48 MHz (crystal) or 4–50 MHz (ext. source) |
| LSE (external) | 32.768 kHz |
| PLLs | 3 PLLs (1 system, 2 kernel) |

---

## 3. Board Memory Architecture

| Component | Part Number | Size | Interface | Notes |
|---|---|---|---|---|
| Internal Flash | (on STM32H747XI) | 2 MB | — | Program storage |
| Internal SRAM | (on STM32H747XI) | 1 MB | — | Working RAM |
| External NOR Flash | AT25SF128A-MHB-T (U8) | 16 MB | Quad-SPI | File storage, FATFS/littleFS supported |
| External SDRAM | AS4C4M16SA (U3) | 8 MB | SDRAM bus @ 166 MHz | Large data buffers |

### Using SDRAM in Arduino Code

```cpp
#include "SDRAM.h"

void setup() {
  SDRAM.begin();
}

// Allocate 7 MB from SDRAM
uint8_t* myArray = (uint8_t*)SDRAM.malloc(7 * 1024 * 1024);

// Write data
for (int i = 0; i < 128; i++) {
  myArray[i] = i;
}

// Free when done
SDRAM.free(myArray);
```

### Using QSPI Flash as USB Storage

1. Upload `WiFiFirmwareUpdater` example (File > Examples > STM32H747_System)
2. Upload `QSPIFormat` example to partition the flash
3. Upload `AccessFlashAsUSBDisk` example (File > Examples > USB Mass Storage)
4. Flash storage persists across sketch uploads

---

## 4. Wireless Connectivity

### Radio Module

| Parameter | Value |
|---|---|
| **Module** | Murata LBEE5KL1DX-883 (U5) |
| **Chipset** | Cypress CYW4343W |
| **Wi-Fi Standard** | IEEE 802.11 b/g/n |
| **Max Transfer Rate** | 65 Mbps |
| **Wi-Fi Modes** | AP, STA, simultaneous AP/STA |
| **Bluetooth** | Classic + BLE |
| **BLE Version** | 5.X (Cordio stack) / 4.2 (Arduino stack) |
| **Antenna** | External (Micro UFL connector, J14) — antenna included |
| **Arduino Library** | `WiFi` (included in board package) |

### Wi-Fi Code Example

```cpp
#include <WiFi.h>

char ssid[] = "MyNetwork";
char pass[] = "MyPassword";

void setup() {
  Serial.begin(9600);
  while (WiFi.status() != WL_CONNECTED) {
    WiFi.begin(ssid, pass);
    delay(10000);
  }
  Serial.print("IP: ");
  Serial.println(WiFi.localIP());
}
```

### Bluetooth Low Energy

Use the `ArduinoBLE` library:

```cpp
#include <ArduinoBLE.h>
```

---

## 5. Pin Configuration & GPIO

### Quick Reference

| Category | Count | Details |
|---|---|---|
| Total Digital I/O | 76 | D0–D75 accessible via headers |
| Analog Input | 12 | A0–A11 (16-bit ADC resolution) |
| PWM Output | 13 | D2–D13 (12 pins via `analogWrite`) |
| DAC Output | 2 | A12/DAC0, A13/DAC1 (up to 12-bit) |
| Logic Level | 3.3V | **Do NOT apply 5V to GPIO pins** |
| DC Current per I/O | 8 mA | Maximum sink/source per pin |

### Complete Pin Map

| Pin | Function | Description |
|---|---|---|
| D0 | RX0 | UART0 Receive |
| D1 | TX0 | UART0 Transmit |
| D2 | PWM | PWM, Digital I/O |
| D3 | PWM | PWM, Digital I/O |
| D4 | PWM | PWM, Digital I/O |
| D5 | PWM | PWM, Digital I/O |
| D6 | PWM | PWM, Digital I/O |
| D7 | PWM | PWM, Digital I/O (defaults to ~1.65V output — set LOW explicitly) |
| D8 | PWM/SCL2 | PWM, Digital I/O, I2C bus 2 clock |
| D9 | PWM/SDA2 | PWM, Digital I/O, I2C bus 2 data |
| D10 | PWM/CS | PWM, Digital I/O, SPI5 chip select |
| D11 | PWM/COPI | PWM, Digital I/O, SPI5 controller out |
| D12 | PWM/CIPO | PWM, Digital I/O, SPI5 controller in |
| D13 | PWM/SCK | PWM, Digital I/O, SPI5 clock |
| D14 | TX3 | UART3 Transmit |
| D15 | RX3 | UART3 Receive |
| D16 | TX2 | UART2 Transmit |
| D17 | RX2 | UART2 Receive |
| D18 | TX1 | UART1 Transmit |
| D19 | RX1 | UART1 Receive |
| D20 | SDA | I2C bus 0 data |
| D21 | SCL | I2C bus 0 clock |
| D22–D75 | GPIO | General-purpose digital I/O |
| A0 / D76 | Analog In | ADC / GPIO / OPAMP1_VOUT / COMP1_INM |
| A1 / D77 | Analog In | ADC / GPIO / OPAMP1_VINM |
| A2 / D78 | Analog In | ADC / GPIO / OPAMP1_VINP / COMP1_INP |
| A3 / D79 | Analog In | ADC / GPIO / COMP1_INM |
| A4 / D80 | Analog In | ADC / GPIO |
| A5 / D81 | Analog In | ADC / GPIO |
| A6 / D82 | Analog In | ADC / GPIO / COMP1_INM |
| A7 / D83 | Analog In | ADC / GPIO / Audio jack microphone input |
| A8 | Analog In | Analog input only (not usable as GPIO) |
| A9 | Analog In | Analog input only (not usable as GPIO) |
| A10 | Analog In | Analog input only (not usable as GPIO) |
| A11 | Analog In | Analog input only (not usable as GPIO) |
| A12 / D84 | DAC0 | Analog output / Audio jack left channel |
| A13 / D85 | DAC1 | Analog output / Audio jack right channel |
| D86 | RGB Red | Onboard RGB LED (not GPIO) |
| D87 | RGB Green | Onboard RGB LED (not GPIO) |
| D88 | RGB Blue | Onboard RGB LED (not GPIO) |
| D89 | SPI1 CIPO | SPI header connector |
| D90 | SPI1 COPI | SPI header connector |
| D91 | SPI1 SCK | SPI header connector |
| D92 | USB Host Enable | USB-A connector (not GPIO) |
| D93 | CANRX | CAN bus receive |
| D94 | CANTX | CAN bus transmit |

### Special Pins

| Pin | Function | Description |
|---|---|---|
| OFF | Power control | Connect to GND to power off the board |
| VRTC | RTC battery | Connect coin cell for RTC persistence |
| IOREF | Logic reference | Connected to 3.3V |
| AREF | Analog reference | Reference voltage for analog inputs |
| BOOT0 (PC_13) | DFU Mode | Hold during power-on for bootloader; readable as `digitalRead(PC_13)` |

### D7 Pin Note

D7 defaults to outputting ~1.65V. To disable:

```cpp
pinMode(7, OUTPUT);
digitalWrite(7, LOW);
```

### LED_BUILTIN Note

The `LED_BUILTIN` logic is **inverted** compared to Arduino UNO:
- `HIGH` → LED **off**
- `LOW` → LED **on**

---

## 6. Communication Interfaces

### 6.1 UART / Serial

The GIGA R1 has **5 serial ports** (1 USB + 4 hardware UART):

| Port | TX Pin | RX Pin | Arduino Object |
|---|---|---|---|
| USB Serial | — | — | `Serial` |
| UART 0 | D1 | D0 | `Serial1` |
| UART 1 | D18 | D19 | `Serial2` |
| UART 2 | D16 | D17 | `Serial3` |
| UART 3 | D14 | D15 | `Serial4` |

```cpp
Serial.begin(9600);   // USB
Serial1.begin(9600);  // UART0 on D0/D1
Serial2.begin(9600);  // UART1 on D18/D19
Serial3.begin(9600);  // UART2 on D16/D17
Serial4.begin(9600);  // UART3 on D14/D15
```

### 6.2 I2C

Three I2C buses:

| Bus | SDA | SCL | Arduino Object | Pull-ups |
|---|---|---|---|---|
| I2C 0 | D20 | D21 | `Wire` | Internal |
| I2C 1 | (camera conn.) | (camera conn.) | `Wire1` | Internal |
| I2C 2 | D9 | D8 | `Wire2` | **External required** |

```cpp
#include <Wire.h>

Wire.begin();   // I2C 0
Wire1.begin();  // I2C 1
Wire2.begin();  // I2C 2 (needs external pull-ups)

Wire.beginTransmission(0x68);
Wire.write(byte(0x00));
Wire.write(val);
Wire.endTransmission();
```

### 6.3 SPI

Two SPI buses:

| Bus | CIPO | COPI | SCK | CS | Arduino Object | Notes |
|---|---|---|---|---|---|---|
| SPI1 (header) | D89 | D90 | D91 | Any GPIO | `SPI` | 5V on header! Check device compatibility |
| SPI5 (pins) | D12 | D11 | D13 | D10 | `SPI1` | 3.3V logic |

> **Note:** In schematics, `SPI` = SPI1 hardware and `SPI1` = SPI5 hardware. The Arduino code objects are `SPI` and `SPI1`.

```cpp
#include <SPI.h>

SPI.begin();   // SPI1 (header)
SPI1.begin();  // SPI5 (pins D10-D13)

digitalWrite(CS_PIN, LOW);
SPI.transfer(0x00);
digitalWrite(CS_PIN, HIGH);
```

### 6.4 CAN Bus

| Pin | Function |
|---|---|
| D93 / CANRX | CAN receive |
| D94 / CANTX | CAN transmit |

> **An external CAN transceiver is required.** Connect VCC→3.3V, GND→GND, CANTX→CANTX, CANRX→CANRX.

```cpp
#include "CAN.h"

mbed::CAN can1(PB_5, PB_13);

void setup() {
  Serial.begin(115200);
  can1.frequency(1000000);
}

// Send
void send() {
  uint8_t counter = 0;
  if (can1.write(mbed::CANMessage(1337, &counter, 1))) {
    counter++;
  }
}

// Receive
void receive() {
  mbed::CANMessage msg;
  if (can1.read(msg)) {
    Serial.println(msg.data[0]);
  }
}
```

---

## 7. Analog Features

### 7.1 ADC (Analog-to-Digital Converter)

| Parameter | Value |
|---|---|
| ADC Count (MCU) | 3 (ADC1, ADC2, ADC3) |
| Resolution | Configurable: 8, 10, 12, 14, or **16-bit** |
| GIGA Default Read Resolution | 16-bit |
| Reference Voltage | 3.3V |
| Channels on GIGA headers | A0–A11 (12 channels) |
| Non-GPIO analog pins | A8, A9, A10, A11 |
| Sampling Rate | Up to 3.6 Msps per ADC |

```cpp
int value = analogRead(A0);  // 16-bit resolution by default
```

#### Advanced ADC (AdvancedAnalogRedux library)

```cpp
#include "AdvancedADC.h"

AdvancedADC adc1(A7);

void setup() {
  Serial.begin(9600);
  if (!adc1.begin(AN_RESOLUTION_16, 16000, 32, 64)) {
    Serial.println("Failed to start analog acquisition!");
    while (1);
  }
}

void loop() {
  if (adc1.available()) {
    SampleBuffer buf = adc1.read();
    Serial.println(buf[0]);
    buf.release();
  }
}
```

### 7.2 DAC (Digital-to-Analog Converter)

| Parameter | Value |
|---|---|
| DAC Channels | 2 (DAC0/A12, DAC1/A13) |
| Resolution | Up to 12-bit |
| Default Write Resolution | 8-bit (0–255) |
| Max Sample Rate | 10 Msps |
| Output Mode | Buffered (low impedance) and Sample-and-Hold |
| Audio Jack Connection | DAC0 → Left, DAC1 → Right |

```cpp
analogWrite(A12, 128);           // 8-bit default
analogWriteResolution(12);       // Switch to 12-bit
analogWrite(A12, 2048);          // Mid-scale at 12-bit
```

#### Advanced DAC (AdvancedAnalogRedux library)

```cpp
#include "AdvancedDAC.h"

AdvancedDAC dac1(A12);

void setup() {
  if (!dac1.begin(AN_RESOLUTION_12, 8000, 32, 64)) {
    Serial.println("Failed to start DAC!");
    while (1);
  }
}

void loop() {
  if (dac1.available()) {
    SampleBuffer buf = dac1.dequeue();
    for (int i = 0; i < buf.size(); i++) {
      buf.data()[i] = (i % 2 == 0) ? 0 : 0xfff;
    }
    dac1.write(buf);
  }
}
```

### 7.3 OPAMP (Internal)

| Pin | OPAMP Function | COMP Function |
|---|---|---|
| A0 | OPAMP1_VOUT | COMP1_INM |
| A1 | OPAMP1_VINM & VINM0 | — |
| A2 | OPAMP1_VINP | COMP1_INP |
| A3 | — | COMP1_INM |
| A6 | — | COMP1_INM |

The STM32H7 provides 2 internal OPAMPs with PGA capability (gains: 2, 4, 8, 16 non-inverting; -1, -3, -7, -15 inverting) and 2 comparators.

---

## 8. USB Features

### 8.1 USB-C (J12) — Device/Programming Port

| Feature | Details |
|---|---|
| Connector | USB-C |
| Role | Device / Programming / HID |
| SuperSpeed Pins | Not populated (USB 2.0 only) |
| ESD Protection | TVS diode array (D2) |
| Functions | Sketch upload, Serial communication, HID (keyboard/mouse emulation) |

### 8.2 USB-A (J2) — Host Port

| Feature | Details |
|---|---|
| Connector | USB 2.0 Type-A |
| Role | Host only |
| ESD Protection | TVS diode array (D4) |
| Functions | USB keyboard input, USB mass storage read/write |

### USB HID Example

The GIGA R1 can emulate keyboard and mouse via USB-C.

### USB Host Keyboard Example

Read keyboard input from a USB keyboard connected to the USB-A port.

### USB Mass Storage

Read/write files on a USB flash drive connected to the USB-A port. Useful for data logging.

---

## 9. Audio

### Audio Jack (J15) — 3.5mm

| Connection | Pin | Direction |
|---|---|---|
| Left Channel | DAC0 / A12 | Output |
| Right Channel | DAC1 / A13 | Output |
| Microphone | A7 | Input |

### Important Notes

- **No onboard amplifier** — driving high-impedance speakers directly without an external amplifier may damage the board.
- Microphone input without an external preamp may be weak.
- DAC supports up to **12-bit** resolution and **10 Msps**.
- Use the `AdvancedAnalogRedux` library for advanced audio.

---

## 10. Display & Camera Interfaces

### 10.1 MIPI DSI Display Interface

The STM32H747XI has a built-in **2-lane MIPI DSI** display controller with:

- **LCD-TFT controller (LTDC)** supporting up to **1024×768** resolution
- **2D graphics accelerator** (Chrom-ART / DMA2D)
- **JPEG hardware codec** (encoder/decoder)
- 2 display layers with blending
- Up to 8 input color formats per layer

#### DSI Connector Pins

| Category | Pins |
|---|---|
| Dedicated DSI (not GPIO) | D1N, D1P, CKN, CKP, D0N, D0P |
| GPIO-capable | D68, D69, D70, D71, D72, D73, D74, D75 |
| Power | 3.3V, 5V, GND, VIN |

Compatible with the **Arduino GIGA Display Shield** which supports **LVGL** and **GFX** frameworks.

### 10.2 Camera Interface (DCMI)

| Parameter | Value |
|---|---|
| Connector | 20-pin Arducam compatible (J5/J6) |
| Interface | 8–14 bit parallel DCMI |
| Max Data Rate | 140 MB/s @ 80 MHz pixel clock |
| Formats | Monochrome, Raw Bayer, YCbCr 4:2:2, RGB 565, JPEG |
| Modes | Continuous, Snapshot (single frame) |

See [GIGA R1 Camera Guide](https://docs.arduino.cc/tutorials/giga-r1-wifi/giga-camera).

---

## 11. Power

### Power Supply Options

| Method | Voltage Range | Connector/Pin |
|---|---|---|
| USB-C | 5V | J12 |
| USB-A | 5V | J2 |
| VIN pin | 6–24V (max 32V absolute) | VIN header pin |

### Power Tree

```
VIN (6-24V) → MP2269GD-Z (U7) buck converter → 5V rail
                                                    ↓
5V rail ← USB 5V (J2 or J12)           MP2322GQH (U6) buck converter → 3.3V rail
```

### Operating Conditions

| Symbol | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| VIN | Input voltage (VIN pad) | 6 | 7.0 | 32 | V |
| VUSB | Input voltage (USB) | 4.8 | 5.0 | 5.5 | V |
| VIH | Input high-level voltage | 0.7×VDD | — | VDD | V |
| VIL | Input low-level voltage | 0 | — | 0.3×VDD | V |
| TOP | Operating temperature | -40 | 25 | 85 | °C |

### Board Logic Level

**3.3V** — All I/O pins operate at 3.3V. Do NOT apply 5V to GPIO pins. VDD = 3.3V.

### OFF Pin

Connecting the OFF pin to GND disables the 3.3V regulator (U6), powering down the board completely. Useful for power switches.

### VRTC Pin

Connect a coin-cell battery to the VRTC pin to keep the RTC running while the board is powered off.

---

## 12. Timers (STM32H747XI)

| Timer Type | Timers | Resolution | Channels | Complementary Output | Max Clock |
|---|---|---|---|---|---|
| High-Resolution | HRTIM1 | 16-bit | 10 outputs | Yes | 480 MHz |
| Advanced Control | TIM1, TIM8 | 16-bit | 4 each | Yes | 240 MHz |
| General Purpose | TIM2, TIM5 | 32-bit | 4 each | No | 240 MHz |
| General Purpose | TIM3, TIM4 | 16-bit | 4 each | No | 240 MHz |
| General Purpose | TIM12 | 16-bit | 2 | No | 240 MHz |
| General Purpose | TIM13, TIM14 | 16-bit | 1 each | No | 240 MHz |
| General Purpose | TIM15 | 16-bit | 2 | 1 | 240 MHz |
| General Purpose | TIM16, TIM17 | 16-bit | 1 each | 1 each | 240 MHz |
| Basic | TIM6, TIM7 | 16-bit | 0 | No | 240 MHz |
| Low-Power | LPTIM1–5 | 16-bit | 0 | No | 240 MHz |

### Watchdogs

- **IWDG1** — Independent watchdog (D1 domain)
- **IWDG2** — Independent watchdog (D2 domain)
- **WWDG1** — Window watchdog (D1 domain)
- **WWDG2** — Window watchdog (D2 domain)
- **SysTick** — System tick timer

---

## 13. DMA Controllers

| DMA | Location | Features |
|---|---|---|
| MDMA | D1 domain | 16 channels, linked-list, high-speed memory-to-memory |
| DMA1 | D2 domain | Dual-port with FIFO and request router |
| DMA2 | D2 domain | Dual-port with FIFO and request router |
| BDMA | D3 domain | Basic DMA with request router |
| DMA2D (Chrom-ART) | D1 domain | 2D graphics accelerator for blitting and pixel format conversion |

---

## 14. Additional MCU Peripherals

| Peripheral | Count/Details |
|---|---|
| ADC | 3× 16-bit (up to 3.6 Msps each) |
| DAC | 2× 12-bit |
| Comparators | 2 (COMP1, COMP2) — ultra-low power, rail-to-rail |
| OPAMPs | 2 (OPAMP1, OPAMP2) — PGA mode, 7.3 MHz GBW |
| DFSDM | 1 (4 filters, 8 channels) — Sigma-Delta/PDM microphone support |
| Temperature Sensor | Internal, connected to ADC3_IN18, -40 to +125°C |
| RNG | True random number generator (32-bit) |
| CRC | Programmable polynomial CRC calculation unit |
| JPEG Codec | Hardware JPEG encoder/decoder |
| FMC | Flexible Memory Controller (SRAM, NOR, NAND, SDRAM) |
| QUADSPI | Quad-SPI memory interface, up to 256 MB mapped |
| Crypto | ATECC608A-MAHDA-T secure element (U4) on GIGA board |

---

## 15. Interrupts

All 76 GPIO pins on the GIGA R1 support interrupts.

```cpp
attachInterrupt(digitalPinToInterrupt(pin), ISR_function, mode);
```

| Mode | Trigger |
|---|---|
| `LOW` | Pin is low |
| `CHANGE` | Pin changes value |
| `RISING` | Low → High transition |
| `FALLING` | High → Low transition |

The STM32H747XI EXTI controller handles up to 89 event/interrupt lines (28 configurable + 61 direct).

---

## 16. RTC (Real-Time Clock)

### Manual RTC Setup

```cpp
#include "mbed.h"
#include <mbed_mktime.h>

void setup() {
  Serial.begin(9600);
  tm t;
  t.tm_sec = 0;
  t.tm_min = 30;
  t.tm_hour = 14;
  t.tm_mday = 13;
  t.tm_mon = 3;       // 0-indexed (0 = Jan)
  t.tm_year = 126;    // Years since 1900
  set_time(mktime(&t));
}

void loop() {
  char buffer[32];
  tm t;
  _rtc_localtime(time(NULL), &t, RTC_4_YEAR_LEAP_YEAR_SUPPORT);
  strftime(buffer, 32, "%Y-%m-%d %H:%M:%S", &t);
  Serial.println(buffer);
  delay(1000);
}
```

### NTP Time Sync

Use `WiFiUdp` to query `pool.ntp.org` and call `set_time(epoch)`.

---

## 17. JTAG Debugging

The GIGA R1 features a **2×5 pin JTAG** connector for advanced debugging using tools like OpenOCD or J-Link.

---

## 18. Secure Element

| Parameter | Value |
|---|---|
| Chip | ATECC608A-MAHDA-T (U4) |
| Function | Hardware crypto, secure key storage |
| Use Case | Arduino Cloud authentication, TLS, IoT security |

---

## 19. Board Topology & Key Components

| Reference | Component | Description |
|---|---|---|
| U1 | STM32H747XIH6 | Dual-core microcontroller |
| U3 | AS4C4M16SA | 8 MB SDRAM |
| U4 | ATECC608A-MAHDA-T | Secure element |
| U5 | LBEE5KL1DX-883 | Wi-Fi/Bluetooth module (Murata 1DX) |
| U6 | MP2322GQH | 3.3V buck converter |
| U7 | MP2269GD-Z | 5V buck converter |
| U8 | AT25SF128A-MHB-T | 16 MB QSPI NOR Flash |
| J2 | USB 2.0 Type-A | USB Host connector |
| J12 | CX90B-16P USB-C | Programming/Device connector |
| J14 | Micro UFL | Antenna connector |
| J15 | 3.5mm jack | Audio in/out |
| J5/J6 | Camera connector | 20-pin Arducam compatible |
| PB1 | Reset button | Hardware reset |
| PB2 | BOOT0 button | DFU mode |
| DL1 | Power LED | Indicates power |
| DL2 | SMLP34RGB2W3 | RGB LED (common anode) |

---

## 20. Software & Development Environment

### Board Package

- **Name:** Arduino Mbed OS GIGA Board Package
- **Platform:** Mbed OS
- **IDE Support:** Arduino IDE 1.8.x, Arduino IDE 2.x, Arduino Cloud Editor
- **Install:** Board Manager → search "GIGA" → install

### Supported Languages

- **Arduino C/C++** (primary)
- **MicroPython** (supported, installable in minutes)

### Key Libraries

| Library | Purpose |
|---|---|
| `WiFi` | Wi-Fi connectivity (included in core) |
| `ArduinoBLE` | Bluetooth Low Energy |
| `Wire` | I2C communication |
| `SPI` | SPI communication |
| `SDRAM` | Access 8 MB external SDRAM |
| `AdvancedAnalogRedux` | Advanced ADC/DAC features |
| `AdvancedADC` | High-performance ADC |
| `AdvancedDAC` | High-performance DAC |
| `CAN` | CAN bus (mbed CAN) |
| `USBHost` | USB host keyboard/mass storage |
| `USBHID` | USB HID (keyboard/mouse emulation) |
| `Camera` | Arducam camera interface |

### MbedOS Crash Behavior

When MbedOS crashes (e.g., memory overflow), the board does **not** auto-reset. Instead:
- The **red LED** blinks in a pattern of 4 fast + 4 slow blinks.
- Press reset button once to restart the sketch.
- Double-tap reset to enter bootloader mode for reprogramming.

### Board Recovery

Double-tap the reset button right after power-up to enter **bootloader mode** (DFU), allowing USB reprogramming even if a sketch has locked the processor.

### BOOT0 Button

- Hold during power-on → DFU mode (Device Firmware Update) for reflashing bootloader
- Readable in sketch: `digitalRead(PC_13)`

---

## 21. MCU Communication Peripherals (STM32H747XI — Full List)

| Peripheral | Count | Details |
|---|---|---|
| USART | 4 | Full-featured serial (USART1, 2, 3, 6) |
| UART | 4 | (UART4, 5, 7, 8) |
| LPUART | 1 | Low-power UART |
| SPI | 6 | (SPI1–SPI6) |
| I2S | 3 | Half-duplex audio interface |
| SAI | 4 | Serial Audio Interface |
| I2C | 4 | (I2C1–I2C4) |
| SDMMC | 2 | SD/MMC card interface |
| USB OTG FS | 1 | Full-speed USB |
| USB OTG HS | 1 | High-speed USB (with ULPI) |
| FDCAN | 1 | Flexible data-rate CAN |
| TT-FDCAN | 1 | Time-triggered FDCAN |
| Ethernet | 1 | MAC with MII/RMII |
| SPDIF-RX | 1 | S/PDIF audio receiver |
| SWPMI | 1 | Single Wire Protocol Master |
| MDIO | — | Management Data I/O slave |
| HDMI-CEC | 1 | HDMI consumer electronics control |

---

## 22. Ethernet

The GIGA R1 does not have an onboard Ethernet PHY, but the STM32H747XI includes an Ethernet MAC. The **Arduino Ethernet Shield Rev2** is compatible with the GIGA R1 for adding Ethernet connectivity.

---

## 23. Certifications

- FCC (DSS, DTS)
- CE (RED)
- IC (Innovation, Science and Economic Development Canada)
- RCM (Australia)
- UKCA (United Kingdom)
- MIC (Japan)
- RoHS 2 & 3 compliant
- REACH compliant

### Antenna Specifications (ISED)

| Parameter | Value |
|---|---|
| Manufacturer | Molex |
| Model | 206994-0100 |
| Type | FPC Antenna |
| Gain | 3.60 dBi |
| Frequency | 2.4 GHz, 40 channels |

---

## 24. Mechanical

- **Form Factor:** Arduino Mega compatible
- **Board Dimensions:** See full pinout PDF (ABX00063-full-pinout.pdf)
- **Mounting Holes:** Standard Mega pattern
- **Weight:** Not specified in datasheet

---

## 25. Useful Links

| Resource | URL |
|---|---|
| Product Page | https://docs.arduino.cc/hardware/giga-r1-wifi/ |
| User Manual | https://docs.arduino.cc/tutorials/giga-r1-wifi/cheat-sheet |
| Getting Started | https://docs.arduino.cc/tutorials/giga-r1-wifi/giga-getting-started |
| Audio Guide | https://docs.arduino.cc/tutorials/giga-r1-wifi/giga-audio |
| Dual Core Guide | https://docs.arduino.cc/tutorials/giga-r1-wifi/giga-dual-core |
| Camera Guide | https://docs.arduino.cc/tutorials/giga-r1-wifi/giga-camera |
| USB Guide | https://docs.arduino.cc/tutorials/giga-r1-wifi/giga-usb |
| MicroPython | https://docs.arduino.cc/micropython/basics/board-installation |
| Datasheet PDF | https://docs.arduino.cc/resources/datasheets/ABX00063-datasheet.pdf |
| Pinout PDF | https://docs.arduino.cc/resources/pinouts/ABX00063-full-pinout.pdf |
| Schematics PDF | https://docs.arduino.cc/resources/schematics/ABX00063-schematics.pdf |
| STM32H747XI Datasheet | https://docs.arduino.cc/resources/datasheets/stm32h747xi.pdf |
| Arduino Cloud | https://create.arduino.cc/iot/ |
| Forum | https://forum.arduino.cc/c/hardware/giga-r1/182 |
| Online Store | https://store.arduino.cc/giga-r1-wifi |

---

*Generated from ABX00063-datasheet.pdf, ABX00063-full-pinout.pdf, stm32h747xi.pdf (DS12930), and the official Arduino documentation.*
