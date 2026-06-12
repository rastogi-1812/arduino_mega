# ABX00063-full-pinout

> Converted from `ABX00063-full-pinout.pdf`

| Property | Value |
| --- | --- |
| Source file | `ABX00063-full-pinout.pdf` |
| Pages | 9 |
| Creator | Adobe InDesign 18.4 (Macintosh) |
| Producer | Adobe PDF Library 17.0 |
| CreationDate | Wed Jul 12 18:01:15 2023 IST |

---

## Page 1

```text
                                                                                                                            PWR            3V3
                                                                                                                                                      Without an external antenna
                                                                                                                       Micro UFL Connector            connected to the Micro UFL
                                          Micro                                                                                     Micro             the WiFi does NOT work
                 It can be used
                                       PC13/BOOT0       BOOT0_BUTTON                                                   RESET_BUTTON NREST
                as USER button
                                            Micro               RGB LED
                                            PI12       D86      RED
                                            PJ13       D87     GREEN
                                            PE3        D88      BLUE

                            Short this with GND to                                                                                  Micro        I2C             SPI           USART
                                                                    OFF
                          turn oﬀ the entire board                                                                     D101/SCL1    PB6          I2C4_SCL
                                                                    GND                                                                                                                                            TOP VIEW
                                                                                                                       D102/SDA1    PH12         I2C4_SDA
                         VRTC pin can be connected              VRTC
                        to a coin cell that can keep                                                                      AREF      AREF
                                                                                                                                                                                               Micro   5V                                            5V         Micro
                        turned on the H7 RTC Timer                                                                        GND
                 VRTC pin CANNOT power the board                     NC                                                                                                                        PJ12     D22                                      D23            PG13
                                                                                                                          ~D13       PH6                       SPI5_SCK
                                                                IOREF                                                                                                                          PG12     D24                                      D25             PJ0
                                                                                                                          ~D12      PJ11                      SPI5_CIPO
                                                    RESET       RESET                                                                                                                          PJ14     D26                                      D27             PJ1
                                                                                                                          ~D11      PJ10                      SPI5_COPI
                                                                3V3                                                                                                                            PJ15     D28                                      D29             PJ2
                                                                                                                          ~D10       PK1                       SPI5_NSS
                                                                5V                                                                                                                              PK3     D30                                      D31             PJ3
                                                                                                                          ~D9        PB9         I2C1_SDA
                                                                    GND                                                                                                                         PK4     D32                                      D33             PJ4
                                                                                         STM32H747XIH6                    ~D8        PB8         I2C1_SCL
                                                                    GND                                                                                                                         PK5     D34                                      D35             PJ5
                                                                VIN                                                       ~D7        PB4                                                        PK6     D36                                      D37             PJ6

   OPAMP          Analog              CAN           Micro                                                                 ~D6       PD13                                                        PJ7     D38                                      D39            PI14
OPAMP1_OUT     ADC1_INP4                            PC4        A0        D76                                              ~D5        PA7                                                        PE6     D40                                      D41             PK7
OPAMP1_IN-     ADC1_INP8                             PC5       A1        D77                                              ~D4        PJ8                                                       PI15     D42                                      D43            PI10
OPAMP1_IN+     ADC1_INP9                             PB0       A2        D78                                              ~D3        PA2                                                       PG10     D44                                      D45            PI13
               ADC1_INP5                             PB1       A3        D79                                              ~D2        PA3                                                       PH15     D46                                      D47             PB2
              ADC1_INP13                             PC3       A4        D80                                            D1/TX0       PA9                                      USART1_TX         PK0     D48                                      D49             PE4
              ADC1_INP12                             PC2       A5        D81                                            D0/RX0       PB7                                      USART1_RX        PI11     D50                                      D51             PE5
              ADC1_INP10                             PC0       A6        D82                                                                                                                    PK2     D52                                      D53             PG7
              ADC1_INP16                             PA0       A7        D83                                            D14/TX3     PG14                                      USART6_TX                 GND                                      GND
                                                                                                                        D15/RX3      PC7                                      USART6_RX
               ADC3_INP0                            PC2_C           A8                                                  D16/TX2     PH13                                      USART4_TX
               ADC3_INP1                            PC3_C           A9                                                  D17/RX2      PI9                                      USART4_RX
               ADC2_INP1                            PA1_C           A10                                                 D18/TX1      PD5                                      USART2_TX
               ADC2_INP0                            PA0_C           A11                                                 D19/RX1      PD6                                      USART2_RX
               DAC1_OUT1                             PA4      DAC0       D84                                            D20/SDA     PB11         I2C2_SDA
               DAC1_OUT2                             PA5      DAC1       D85                                            D21/SCL      PH4         I2C2_SCL
                                  FDCAN2_RX          PB5     CAN RX D93
                                  FDCAN2_TX         PB13     CAN TX D94




           WARNING Pins A8, A9, A10 and A11 are
           ONLY analog pins, no GPIO peripherals

                                                                                         TOP VIEW




Legend:                                                                                                                                                                       MAXIMUM Total output current
                                                                                                                                                                              sourced or sunked by sum of all
   Power               Power Input                           GPIO Digital External        I2C             Default         LED                                                 I/Os and control pins is 140 mA

                                                                                                                                                                              MAXIMUM Output current sourced
                        Power Output                         Analog External              SPI             Default         RGB LED                                             or sunked by any I/O and
                                                                                                                                                                              control pin is 20 mA              SKU code: ABX00063
   Ground                                                    Main Part                    UART/USART      Default         Other                                                                                 Full Pinout - Page 1 of 9
                                                                                                                                                                              CIPO/COPI have previously been    Last update: 12 Jul, 2023
                                                                                                                                                                              referred to as MISO/MOSI
                                                             Secondary Part               Other SERIAL Communication
                                                                                                                                                                                                                                       This work is licensed under
                                                                                                                                                                                                                                       the Creative Commons
                                                             Internal Component           Analog          Default                                                                                                                      Attribution-ShareAlike 4.0
                                                                                                                                                                                                                                       International License. To view a
                                                                                                                                                                                                                                       copy of this license, visit http://
                                                                                                                                                                                                                                       creativecommons.org/licenses/
                                                             Other Pins (Reset, System    PWM/Timer                                                                                                                                    by-sa/4.0/ or send a letter to
                                                                                                                                                                                                                                       Creative Commons, PO Box 1866,
                                                             Control, Debugging)                                                                                                                                                       Mountain View, CA 94042, USA.
```

## Page 2

```text
                        USB                              FS_USB-C                                                                                                                     TOP VIEW
                                                       VBUS_USB0
               USB-OTG-FS_DP                PA12              DP
               USB-OTG-FS_DM                PA11              DM                                                                                                  D101/SCL1                                         D102/SDA1

                                            D1
                                                                                                                                  I2C4_SCL is shared with                                                                          I2C4_SDA is shared with
               VBUS_USB0                                      +5V                                                                 SCL1 pin of the headers                                                                          SDA1 pin of the headers

                                                                                                                                                                                                 1   J6
                                                                                                                                            Camera                                                                                        Camera
                        USB                               HS_USB-A                                                              I2C        (Arducam)    Micro      3V3                                                 GND       Micro   (Arducam)           I2C
                                                       VBUS_USB1                                                             I2C4_SCL                   PB6       D101/SCL1                                         D102/SDA1    PH12                     I2C4_SDA
               USB-OTG-HS_DP                PB15              DP                                                                             VSYNC          PI5      D54                                               D55        PH8         HREF
                                                                                                               1
               USB-OTG-HS_DM                PB14              DM                                                                             PCLK           PA6      D56                                               D57        PJ9         XCLK
                                                                                                                                             DOUT7          PI7      D58                                               D59        PI6     DOUT6
                        U 9 P o we r S wi tch
                                                                                                                                             DOUT5          PI4      D60                                               D61       PH14     DOUT4
               +5V                                   VBUS_USB1
                                                                                                                                             DOUT3      PG11         D62                                               D63       PH11     DOUT2
                               PA15
                                                                                                                                             DOUT1      PH10         D64                                               D65        PH9     DOUT0
                      Current limit ~ 500 mA
                                                                                                                                           POWER_EN         PA1     D66                                                D67        PD4         PWDN
                      It is not possible to power the board
                      thro ugh the USB-A Connector
                                                                                                                                                                                                                        Pins D66 and D67
                                                                                                                                        J6 Is compatible with Arducam
                                                                                                                                                                                                                        are duplicated pins
                                                 Micro    Jack Audio
                              D85    DAC1        PA5         LEFT
                              D84    DAC0        PA4          RIGHT
                              D83      A7        PA0           MIC

      SPI       Micro         SPI
   SPI1_CIPO    PG9           D89         1
                            5V            2               5   3     1
                                                                                                                                            DSI PINS have only display
    SPI1_SCK    PB3           D91         3                                                                                               feature, NO GPIO, NO Analog
   SPI1_COPI    PD7           D90         4                                                1
                                                                                                           1
                                                                                                                                                       Micro                          1   J5                                      Micro
                NRST        RESET         5               6   4     2
                                                                                                                                                     DSI_D1_N        D1N                                               D1P      DSI_D1_P
                              GND         6
                                                                                                                                                                     GND                                               GND
                             JTAG                                                                                                                    DSI_CK_N        CKN                                               CKP      DSI_CK_P
             Micro         3V3            1
                                                                                                                                                                     GND                                               GND
          PA13 SWDIO          SWD         2
                                                                                                                                                     DSI_D0_N        D0N                                               D0P      DSI_D0_P
                              GND         3               9    7    5   3   1                                      1                                                 GND                                               GND
          PA14 SWCLK          SCK         4
                                                                                                                                                       PC6           D68                                               D69         PI0
                              GND         5
                                                                                                                                                       PI1           D70                                               D71         PI2              DFSDM
                               NC         6
                                                                                                                                                       PI3           D72                                               D73         PC1          DFSDM1_DATIN0
                               NC         7
                                                          10 8      6   4   2                                                                          PB12          D74                                               D75         PD3           DFSDM1_CKOUT
                               NC         8
                                                                                                                                                                    5V                                                 GND
                              GND         9
                                                                                                                                                                   3V3                                                  VIN
             NRST           RESET        10




                                                                                               TOP VIEW




Legend:                                                                                                                                                                       MAXIMUM Total output current
                                                                                                                                                                              sourced or sunked by sum of all
  Power              Power Input                               GPIO Digital External           I2C             Default      LED                                               I/Os and control pins is 140 mA

                                                                                                                                                                              MAXIMUM Output current sourced
                      Power Output                             Analog External                 SPI             Default      RGB LED                                           or sunked by any I/O and
                                                                                                                                                                              control pin is 20 mA              SKU code: ABX00063
  Ground                                                       Main Part                       UART/USART      Default      Other                                                                               Full Pinout - Page 2 of 9
                                                                                                                                                                              CIPO/COPI have previously been    Last update: 12 Jul, 2023
                                                                                                                                                                              referred to as MISO/MOSI
                                                               Secondary Part                  Other SERIAL Communication
                                                                                                                                                                                                                                         This work is licensed under
                                                                                                                                                                                                                                         the Creative Commons
                                                               Internal Component              Analog          Default                                                                                                                   Attribution-ShareAlike 4.0
                                                                                                                                                                                                                                         International License. To view a
                                                                                                                                                                                                                                         copy of this license, visit http://
                                                                                                                                                                                                                                         creativecommons.org/licenses/
                                                               Other Pins (Reset, System       PWM/Timer                                                                                                                                 by-sa/4.0/ or send a letter to
                                                                                                                                                                                                                                         Creative Commons, PO Box 1866,
                                                               Control, Debugging)                                                                                                                                                       Mountain View, CA 94042, USA.
```

## Page 3

```text
                                                                                                                                                                   BOTTOM VIEW




                                                                                                                                                                                                       Pins D66 and D67
                                                                                                                                                                                                       are duplicated pins


                                                                                                                             Camera                                                  J6                                   Camera
                                                                                                                            (Arducam)    Micro                                                                  Micro    (Arducam)
                                                                                                                            POWER_EN     PA1       D66                                                D67       PD4        PWDN

                                                                                                                             DOUT1       PH10       D64                                               D65        PH9      DOUT0
                                                                            1                                                DOUT3       PG11       D62                                               D63       PH11      DOUT2
           Connectors J5 and J6 are pass through
                                                                                                                             DOUT5        PI4       D60                                               D61       PH14      DOUT4
           pins and can be connected also on the
           other side of the board, from the bottom                                                                          DOUT7        PI7       D58                                               D59        PI6      DOUT6
                                                                                                                              PCLK        PA6       D56                                               D57        PJ9         XCLK

                                                                                                                   I2C       VSYNC        PI5       D54                                               D55        PH8         HREF            I2C
                                                                                                                I2C4_SCL                  PB6    D101/SCL1                                         D102/SDA1    PH12                      I2C4_SDA
                                                                                                                                                  3V3                                                 GND
                                                                                                                                                                                 1

                                                                                                                            DO NOT connect the camera                                                  I2C4_SCL and I2C4_SDA are shared with
                                                                                                                                 from the bottom side                                                  SCL1 and SDA1 pins of the headers




                                                                                                                             DSI PINS have only display
                                                                                                                           feature, NO GPIO, NO Analog

                                                                                                                                                                          J5
                                                                                                                                                  3V3                                                  VIN

                                                                                                                                        Micro      5V                                                 GND        Micro                   DFSDM
                                                                                                                                        PB12        D74                                               D75         PD3            DFSDM1_CKOUT
                                                                                                                                        PI3         D72                                               D73         PC1           DFSDM1_DATIN0
                                                                                                                                        PI1         D70                                               D71         PI2
                                                                                                                                        PC6         D68                                               D69         PI0
                                                                        1
                                                                                                                                                    GND                                               GND
                                                                                                                                     DSI_D0_N       D0N                                               D0P      DSI_D0_P
                                                                                                                                                    GND                                               GND
                                                                                                                                     DSI_CK_N       CKN                                               CKP      DSI_CK_P
                                                                                                                                                    GND                                               GND
                                                                                                                                     DSI_D1_N       D1N                                               D1P      DSI_D1_P
                                                                                                                                                                      1




                                                                                BOTTOM VIEW




Legend:                                                                                                                                                      MAXIMUM Total output current
                                                                                                                                                             sourced or sunked by sum of all
  Power         Power Input                     GPIO Digital External             I2C             Default      LED                                           I/Os and control pins is 140 mA

                                                                                                                                                             MAXIMUM Output current sourced
                 Power Output                   Analog External                   SPI             Default      RGB LED                                       or sunked by any I/O and
                                                                                                                                                             control pin is 20 mA              SKU code: ABX00063
  Ground                                        Main Part                         UART/USART      Default      Other                                                                           Full Pinout - Page 3 of 9
                                                                                                                                                             CIPO/COPI have previously been    Last update: 12 Jul, 2023
                                                                                                                                                             referred to as MISO/MOSI
                                                Secondary Part                    Other SERIAL Communication
                                                                                                                                                                                                                         This work is licensed under
                                                                                                                                                                                                                         the Creative Commons
                                                Internal Component                Analog          Default                                                                                                                Attribution-ShareAlike 4.0
                                                                                                                                                                                                                         International License. To view a
                                                                                                                                                                                                                         copy of this license, visit http://
                                                                                                                                                                                                                         creativecommons.org/licenses/
                                                Other Pins (Reset, System         PWM/Timer                                                                                                                              by-sa/4.0/ or send a letter to
                                                                                                                                                                                                                         Creative Commons, PO Box 1866,
                                                Control, Debugging)                                                                                                                                                      Mountain View, CA 94042, USA.
```

## Page 4

```text
                              WARNING!


               Advan ced Section
The following information is for advanced use only and
 m a y n o t b e o f fi c i a l l y s u p p o r t e d b y A r d u i n o s o f t w a r e
```

## Page 5

```text
                                                                                                                                     ADC/DAC
                                                                                                                            ADC12_INN18/ADC12_INP19                        Micro     Jack Audio
                                                                                                                                   /DAC1_OUT2              D85   DAC1      PA5          LEFT
                                                                                                                             ADC12_INP18/DAC1_OUT1         D84   DAC0      PA4        RIGHT
                                                                                                                                  ADC1_INP16               D83    A7       PA0          MIC




                                                                                                                                                                                             OFF
                                                                                                                                                                                             GND
                                                                                                                                                   VRTC pin can be connected             VRTC
                                                                                                                                                  to a coin cell that can keep
                                                                                                                                                  turned on the H7 RTC Timer
                                                                                                                                           VRTC pin CANNOT power the board                    NC
                                                                                                                                                                                          IOREF
                                                                                                                                                                             RESET        RESET
                                                                                                                                                                                         3V3
                                                                                                                                                                                          5V
                                                                                                                                                                                             GND
                                                                                                                                                                                             GND
                                                                                                                                                                                         VIN
                                                                                                                                                                FDCAN
           SYS (Clock)      LPTIM          HRTIM                    Timer                     OPAMP          COMPARATOR             ADC/DAC                   (can bust)     Micro
                         (Low Power   (High Resolution                                     OPAMP1_VOUT       COMP1_INM            ADC12_INP_4                                PC4        A0        D76
                            Timer)         Timer)
                                                                                        OPAMP1_VINM, VINM0                   ADC12_INN4/ADC12_INP8                            PC5       A1        D77
                                                         TIM1_CH2N/TIM3_CH3/TIM8_CH2N      OPAMP1_VINP       COMP1_INP       ADC12_INP5/ADC12_INP9                            PB0       A2        D78
                                                         TIM1_CH3N/TIM3_CH4/TIM8_CH3N                        COMP1_INM             ADC12_INP5                                 PB1       A3        D79
           SYS_TRGIO                                                                                                        ADC12_INN12/ADC12_INP13                           PC3       A4        D80
                                                                                                                           ADC123_INN11/ADC123_INP12                          PC2       A5        D81
                                                                                                             COMP1_INM            ADC123_INP10                                PC0       A6        D82
           SYS_WKUP0                                     TIM2_CH1/TIM2_ETR/TIM5_CH1/                                               ADC1_INP16                                 PA0       A7        D83
                                                             TIM8_ETR/TIM15_BKIN

                                                                                                                              ADC3_INN1/ADC3_INP0                            PC2_C           A8
                                                                                                                                   ADC3_INP1                                 PC3_C           A9
                                                                                                                                   ADC12_INP1                                PA1_C           A10
                                                                                                                             ADC12_INN1/ADC12_INP0                           PA0_C           A11
                                                                   TIM5_ETR                                                  ADC12_INP18/DAC1_OUT1                            PA4      DAC0       D84
                                                         TIM2_CH1/TIM2_ETR/TIM8_CH1N                                      ADC12_INN18, INP19/DAC1_OUT2                        PA5      DAC1       D85
                                       HRTIM_EEV7            TIM17_BKIN/TIM3_CH2                                                                              FDCAN2_RX       PB5     CAN RX D93
           SYS_WKUP5     LPTIM2_OUT                               TIM1_CH1N                                                                                   FDCAN2_TX       PB13    CAN TX D94




                                                                                                                                                                                                                                     TOP VIEW




Legend:                                                                                                                                                                                            MAXIMUM Total output current
                                                                                                                                                                                                   sourced or sunked by sum of all
  Power      Power Input                    GPIO Digital External                        I2C                  Default                LED                                                           I/Os and control pins is 140 mA

                                                                                                                                                                                                   MAXIMUM Output current sourced
              Power Output                  Analog External                              SPI                  Default                RGB LED                                                       or sunked by any I/O and
                                                                                                                                                                                                   control pin is 20 mA                 SKU code: ABX00063
  Ground                                    Main Part                                    UART/USART           Default                Other                                                                                              Full Pinout - Page 5 of 9
                                                                                                                                                                                                   CIPO/COPI have previously been       Last update: 12 Jul, 2023
                                                                                                                                                                                                   referred to as MISO/MOSI
                                            Secondary Part                               Other SERIAL Communication
                                                                                                                                                                                                                                                               This work is licensed under
                                                                                                                                                                                                                                                               the Creative Commons
                                            Internal Component                           Analog               Default                                                                                                                                          Attribution-ShareAlike 4.0
                                                                                                                                                                                                                                                               International License. To view a
                                                                                                                                                                                                                                                               copy of this license, visit http://
                                                                                                                                                                                                                                                               creativecommons.org/licenses/
                                            Other Pins (Reset, System                    PWM/Timer                                                                                                                                                             by-sa/4.0/ or send a letter to
                                                                                                                                                                                                                                                               Creative Commons, PO Box 1866,
                                            Control, Debugging)                                                                                                                                                                                                Mountain View, CA 94042, USA.
```

## Page 6

```text
                                                                                                                                                                                      HRTIM            LPTIM
                                                                                                                              UART/                                              (High Resolution   (Low Power
                                                                          Micro               I2C                  SPI        USART                     Timer                         Timer)           Timer)    SYS (Clock)
                                                          D101/SCL1       PB6          I2C1_SCL/I2C4_SCL                                         TIM16_CH1N/TIM4_CH1               HRTIM_EEV8
                                                          D102/SDA1       PH12             I2C4_SDA                                                    TIM5_CH3
                                                            AREF          AREF
                                                            GND
                                                            ~D13          PH6                                   SPI5_SCK
                                                            ~D12          PJ11                                  SPI5_CIPO                         TIM1_CH2/TIM8_CH2N
                                                            ~D11          PJ10                                  SPI5_COPI                        TIM1_CH2N/TIM8_CH2/
                                                            ~D10          PK1                                   SPI5_NSS                          TIM1_CH1/TIM8_CH3N
                                                            ~D9           PB9     I2C1_SDA/I2C4_SDA/I2C4_SMBA                                     TIM17_CH1/TIM4_CH4
                                                            ~D8           PB8          I2C1_SCL/I2C4_SCL                                          TIM16_CH1/TIM4_CH3

                                                            ~D7           PB4
                                                            ~D6           PD13                                                                         TIM4_CH2                                     LPTIM1_OUT
                                                            ~D5           PA7                                                           TIM14_CH1/TIM1_CH1N/TIM3_CH2/TIM8_CH1N
                                                            ~D4           PJ8                                                                     TIM1_CH3N/TIM8_CH1
                                                            ~D3           PA2                                                                TIM2_CH3/TIM5_CH3/TIM15_CH1                            LPTIM4_OUT   SYS_WKUP1
                                                            ~D2           PA3                                                                 TIM2_CH4/TIM5_CH4/TIM5_CH4                            LPTIM5_OUT
                                                           D1/TX0         PA9                                               USART1_TX                  TIM1_CH2                   HRTIM_CHC1
                                                           D0/RX0         PB7                                               USART1_RX            TIM17_CH1N/TIM4_CH2              HRTIM_EEV9


                                                          D14/TX3         PG14                                              USART6_TX                                                               LPTIM1_ETR
                                                          D15/RX3         PC7                                               USART6_RX             TIM3_CH2/TIM8_CH2               HRTIM_CHA2
                                                          D16/TX2         PH13                                              USART4_TX                 TIM8_CH1N
                                                          D17/RX2         PI9                                               USART4_RX
                                                          D18/TX1         PD5                                               USART2_TX                                             HRTIM_EEV4
                                                          D19/RX1         PD6                                               USART2_RX
                                                          D20/SDA         PB11             I2C2_SDA                                                    TIM2_CH4                   HRTIM_SCIN        LPTIM2_ETR
                                                          D21/SCL         PH4              I2C2_SCL




                          TOP VIEW




Legend:                                                                                                                                                      MAXIMUM Total output current
                                                                                                                                                             sourced or sunked by sum of all
  Power    Power Input        GPIO Digital External                 I2C                    Default                LED                                        I/Os and control pins is 140 mA

                                                                                                                                                             MAXIMUM Output current sourced
           Power Output       Analog External                       SPI                    Default                RGB LED                                    or sunked by any I/O and
                                                                                                                                                             control pin is 20 mA                       SKU code: ABX00063
  Ground                      Main Part                             UART/USART             Default                Other                                                                                 Full Pinout - Page 6 of 9
                                                                                                                                                             CIPO/COPI have previously been             Last update: 12 Jul, 2023
                                                                                                                                                             referred to as MISO/MOSI
                              Secondary Part                        Other SERIAL Communication
                                                                                                                                                                                                                               This work is licensed under
                                                                                                                                                                                                                               the Creative Commons
                              Internal Component                    Analog                 Default                                                                                                                             Attribution-ShareAlike 4.0
                                                                                                                                                                                                                               International License. To view a
                                                                                                                                                                                                                               copy of this license, visit http://
                                                                                                                                                                                                                               creativecommons.org/licenses/
                              Other Pins (Reset, System             PWM/Timer                                                                                                                                                  by-sa/4.0/ or send a letter to
                                                                                                                                                                                                                               Creative Commons, PO Box 1866,
                              Control, Debugging)                                                                                                                                                                              Mountain View, CA 94042, USA.
```

## Page 7

```text
                                                                                                                   Conﬁgured to be used
                                                                                                                   with LTDC Display at 24bit




                                                                                                                       TOP VIEW
                              LPTIM        HRTIM                                                                                                                                    HRTIM          LPTIM
                           (Low Power (High Resolution                                                                                                                         (High Resolution (Low Power
           LTDC (Video)       Timer)       Timer)                        Timer                    Micro   5V                                         5V   Micro     Timer           Timer)         Timer)    LTDC (Video)              SAI (Audio - interface)
             LTDC_B0                                                                              PJ12    D22                                       D23   PG13                  HRTIM_EEV10 LPTIM1_OUT         LTDC_R0
            LTDC_B1       LPTIM1_IN1    HRTIM_EEV5                                                PG12    D24                                       D25   PJ0                                                 LTDC_R1
            LTDC_B2                                                                               PJ14    D26                                       D27   PJ1                                                 LTDC_R2
            LTDC_B3                                                                               PJ15    D28                                       D29   PJ2                                                 LTDC_R3
            LTDC_B4                                                                               PK3     D30                                       D31   PJ3                                                 LTDC_R4
            LTDC_B5                                                                               PK4     D32                                       D33   PJ4                                                 LTDC_R5
            LTDC_B6                                                                               PK5     D34                                       D35   PJ5                                                 LTDC_R6
            LTDC_B7                                                                               PK6     D36                                       D37   PJ6      TIM8_CH2                                   LTDC_R7
            LTDC_G0                                                    TIM8_CH2N                  PJ7     D38                                       D39   PI14                                                LTDC_CLK
            LTDC_G1                                      TIM15_CH2/TIM1_BKIN2/TIM1_BKIN2-COMP12   PE6     D40                                       D41   PK7                                                 LTDC_DE
            LTDC_G2                                                                               PI15    D42                                       D43   PI10                                               LTDC_HSYNC
            LTDC_G3                     HRTIM_FLT5                                                PG10    D44                                       D45   PI13                                               LTDC_VSYNC
            LTDC_G4                                                    TIM8_CH3N                  PH15    D46                                       D47   PB2                                                                SAI1_D1/SAI1_SD-A/SAI4_D1/SAI4_SD-A/
            LTDC_G5                                                TIM1_CH1N/TIM8_CH3             PK0     D48                                       D49   PE4     TIM15_CH1N                                                  SAI1_D2/SAI1_FS-A/SAI4_D2/SAI4_FS-A
            LTDC_G6                                                                               PI11    D50                                       D51   PE5     TIM15_CH1                                                 SAI1_CK2/SAI1_SCK-A/SAI4_CK2/SAI4_SCK-A
            LTDC_G7                                           TIM1_BKIN/TIM1_BKIN-COMP12/         PK2     D52                                       D53   PG7                   HRTIM_CHE2                                                 SAI1_MCLK-A
                                                               TIM8_BKIN/TIM8_BKIN-COMP12
                                                                                                          GND                                       GND




Legend:                                                                                                                                                                                   MAXIMUM Total output current
                                                                                                                                                                                          sourced or sunked by sum of all
  Power             Power Input                 GPIO Digital External                       I2C                 Default                   LED                                             I/Os and control pins is 140 mA

                                                                                                                                                                                          MAXIMUM Output current sourced
                      Power Output              Analog External                             SPI                 Default                   RGB LED                                         or sunked by any I/O and
                                                                                                                                                                                          control pin is 20 mA                  SKU code: ABX00063
  Ground                                        Main Part                                   UART/USART          Default                   Other                                                                                 Full Pinout - Page 7 of 9
                                                                                                                                                                                          CIPO/COPI have previously been        Last update: 12 Jul, 2023
                                                                                                                                                                                          referred to as MISO/MOSI
                                                Secondary Part                              Other SERIAL Communication
                                                                                                                                                                                                                                                         This work is licensed under
                                                                                                                                                                                                                                                         the Creative Commons
                                                Internal Component                          Analog              Default                                                                                                                                  Attribution-ShareAlike 4.0
                                                                                                                                                                                                                                                         International License. To view a
                                                                                                                                                                                                                                                         copy of this license, visit http://
                                                                                                                                                                                                                                                         creativecommons.org/licenses/
                                                Other Pins (Reset, System                   PWM/Timer                                                                                                                                                    by-sa/4.0/ or send a letter to
                                                                                                                                                                                                                                                         Creative Commons, PO Box 1866,
                                                Control, Debugging)                                                                                                                                                                                      Mountain View, CA 94042, USA.
```

## Page 8

```text
                                                                                                                                              TOP VIEW




                                                                                                                                                                 I2C4_SCL and I2C4_SDA are shared with
                                                                                                                                                                 SCL1 and SDA1 pins of the headers

     LPTIM          HRTIM                                                                                                                                J6                                                                                HRTIM
  (Low Power   (High Resolution                                            Camera                                                                                                                   Camera                            (High Resolution
     Timer)         Timer)                        Timer                   (Arducam)          I2C               Micro       3V3                                   GND        Micro         I2C      (Arducam)           Timer               Timer)
                 HRTIM_EEV8                TIM16_CH1N/TIM4_CH1                        I2C1_SCL/I2C4_SCL        PB6        D101/SCL1                           D102/SDA1      PH12      I2C4_SDA                      TIM5_CH3
                                                TIM8_CH1                   VSYNC                                PI5           D54                                D55         PH8                     HREF            TIM5_ETR
                                  TIM13_CH1/TIM1_BKIN/TIM1_BKIN-COMP12/     PCLK                                PA6           D56                                D57         PJ9                     XCLK      TIM1_CH3/TIM8_CH1N
                                   TIM3_CH1/TIM8_BKIN/TIM8_BKIN-COMP12
                                                                                                                                                                 D59         PI6                     DOUT6           TIM8_CH2
                                                TIM8_CH3                   DOUT7                                PI7           D58                                                                    DOUT4
                                                                                                                                                                 D61         PH14                                   TIM8_CH2N
                                       TIM8_BKIN/TIM8_BKIN-COMP12          DOUT5                                PI4           D60                                                                    DOUT2
                                                                                                                                                                 D63         PH11                                    TIM5_CH2
  LPTIM2_OUT    HRTIM_EEV4                                                 DOUT3                                PG11          D62                                                                    DOUT0
                                                                                                                                                                 D65         PH9
                                                TIM5_CH1                   DOUT1                                PH10          D64
                                                                                                                                                                 D67         PD4                     PWDN                              HRTIM_FLT3
  LPTIM2_OUT                          TIM2_CH2/TIM5_CH2/TIM15_CH1N        POWER_EN                              PA1          D66


                                                                                                                                                                 Pins D66 and D67
                                                                                                  J6 is compatible with Arducam
                                                                                                                                                                 are duplicated pins




                                                                                                       DSI PINS have only display
                                                                                                     feature, NO GPIO, NO Analog


                                                                                                               Micro                             J5                         Micro
                                                                                                             DSI_D1_N         D1N                                D1P      DSI_D1_P
                                                                                                                              GND                                GND
                                                                                                             DSI_CK_N         CKN                                CKP      DSI_CK_P
                                                                                                                              GND                                GND
                    HRTIM                                                                                    DSI_D0_N         D0N                                D0P      DSI_D0_P
               (High Resolution
                    Timer)                        Timer                                      I2S                              GND                                GND                      I2S                          Timer
                 HRTIM_CHA1                 TIM3_CH1/TIM8_CH1                             I2S2_MCK              PC6           D68                                D69         PI0        I2S2_WS                      TIM5_CH4
                                      TIM8_BKIN2/TIM8_BKIN2-COMP12                         I2S2_CK              PI1           D70                                D71         PI2       I2S2_SDI                      TIM8_CH4              DFSDM
                                                TIM8_ETR                                  I2S2_SDO              PI3           D72                                D73         PC1                                                       DFSDM1_DATIN0
                                       TIM1_BKIN/TIM1_BKIN-COMP12                                               PB12          D74                                D75         PD3                                                        DFSDM1_CKOUT
                                                                                                                            5V                                   GND
                                                                                                                           3V3                                    VIN




Legend:                                                                                                                                                           MAXIMUM Total output current
                                                                                                                                                                  sourced or sunked by sum of all
   Power             Power Input                 GPIO Digital External                      I2C                       Default         LED                         I/Os and control pins is 140 mA

                                                                                                                                                                  MAXIMUM Output current sourced
                      Power Output               Analog External                            SPI                       Default         RGB LED                     or sunked by any I/O and
                                                                                                                                                                  control pin is 20 mA                         SKU code: ABX00063
   Ground                                        Main Part                                  UART/USART                Default         Other                                                                    Full Pinout - Page 8 of 9
                                                                                                                                                                  CIPO/COPI have previously been               Last update: 12 Jul, 2023
                                                                                                                                                                  referred to as MISO/MOSI
                                                 Secondary Part                             Other SERIAL Communication
                                                                                                                                                                                                                                      This work is licensed under
                                                                                                                                                                                                                                      the Creative Commons
                                                 Internal Component                         Analog                    Default                                                                                                         Attribution-ShareAlike 4.0
                                                                                                                                                                                                                                      International License. To view a
                                                                                                                                                                                                                                      copy of this license, visit http://
                                                                                                                                                                                                                                      creativecommons.org/licenses/
                                                 Other Pins (Reset, System                  PWM/Timer                                                                                                                                 by-sa/4.0/ or send a letter to
                                                                                                                                                                                                                                      Creative Commons, PO Box 1866,
                                                 Control, Debugging)                                                                                                                                                                  Mountain View, CA 94042, USA.
```

## Page 9

```text
                                                                                                                            U.FL-R-SMT-1
                                  FMC (Flexible
                                Memory Controller)   Micro     SDRAM
                                    FMC_A0           PF0       FMC_A0                                                       LBEE5KL1DX     Micro      UART         SDMMC (SPI)
                                       FMC_A1        PF1       FMC_A1                                                           RX         PF7      UART7_TX

                                       FMC_A2        PF2       FMC_A2                                                           TX         PA8      UART7_RX

                                       FMC_A3        PF3       FMC_A3                                                           RTS        PF9     UART7_CTS

                                       FMC_A4        PF4       FMC_A4                                                           CTS        PF8     UART7_RTS

                                       FMC_A5        PF5       FMC_A5                                                           D0         PC8                     SDMMC1_D0

                                       FMC_A6        PF12      FMC_A6                                                           D1         PC9                     SDMMC1_D1

                                       FMC_A7        PF13      FMC_A7                                                           D2         PC10                    SDMMC1_D2

                                       FMC_A8        PF14      FMC_A8                                                           D3         PC11                    SDMMC1_D3

                                       FMC_A9        PF15      FMC_A9                                                           CLK        PC12                    SDMMC1_CK

                                      FMC_A10        PG0      FMC_A10                                                           CMD        PD2                     SDMMC1_CMD

                                      FMC_A11        PG1      FMC_A11                                                       WL_WAKE_H      PI8

                                      FMC_A12        PG2      FMC_A12                                                         WL_ON        PB10

                                      FMC_BA0        PG4      FMC_BA0                                                       BT_WAKE_D      PH7

                                      FMC_BA1        PG5      FMC_BA1                                                       BT_WAKE_H      PG3

                                   FMC_SDCLK         PG8     FMC_SDCLK                                                        BT_ON        PA10

                                                     PH2     FMC_SDCKE0                                                       LPO_IN

                                   FMC_SDNWE         PH5     FMC_SDNWE                                                          ANT

                                   FMC_SDNCAS        PG15    FMC_SDNCAS                                                       CRYPTO       Micro      I2C
                                   FMC_SDNRAS        PF11    FMC_SDNRAS                                                        SDA         PH12    I2C4_SDA
                                   FMC_SDNCS         PH3     FMC_SDNCS                                                          SCL        PB6     I2C4_SCL
                                      FMC_DQMH       PE1      FMC_DQMH                                                         FLASH       Micro       Quad-SPI
                                      FMC_DQML       PE0      FMC_DQML                                                        SI/IO0       PD11    QUADSPI_BK1_IO0
                                      FMC_D15        PD10     FMC_DQ15                                                        SO/IO1       PD12    QUADSPI_BK1-IO2
                                      FMC_D14        PD9      FMC_DQ14                                                        WP/IO2       PE2     QUADSPI_BK2-IO1
                                                     PD8      FMC_DQ13                                                       HOLD/IO3      PF6     QUADSPI_BK1_IO3
                                      FMC_D12        PE15     FMC_DQ12                                                          CS         PG6     QUADSPI_BK1_NCS
                                      FMC_D11        PE14     FMC_DQ11                                                          SCK        PF10      QUADSPI_CLK
                                      FMC_D10        PE13     FMC_DQ10
                                       FMC_D9        PE12     FMC_DQ9
                                       FMC_D8        PE11     FMC_DQ8
                                       FMC_D7        PE10     FMC_DQ7
                                       FMC_D6        PE9      FMC_DQ6
                                                     PE8      FMC_DQ5
                                                     PE7      FMC_DQ4
                                       FMC_D3        PD0      FMC_DQ3
                                       FMC_D2        PD1      FMC_DQ2
                                       FMC_D1        PD15     FMC_DQ1
                                       FMC_D0        PD14     FMC_DQ0                                  TOP VIEW




Legend:                                                                                                                                  MAXIMUM Total output current
                                                                                                                                         sourced or sunked by sum of all
  Power    Power Input    GPIO Digital External                           I2C             Default                 LED                    I/Os and control pins is 140 mA

                                                                                                                                         MAXIMUM Output current sourced
           Power Output   Analog External                                 SPI             Default                 RGB LED                or sunked by any I/O and
                                                                                                                                         control pin is 20 mA                    SKU code: ABX00063
  Ground                  Main Part                                       UART/USART      Default                 Other                                                          Full Pinout - Page 9 of 9
                                                                                                                                         CIPO/COPI have previously been          Last update: 12 Jul, 2023
                                                                                                                                         referred to as MISO/MOSI
                          Secondary Part                                  Other SERIAL Communication
                                                                                                                                                                                                        This work is licensed under
                                                                                                                                                                                                        the Creative Commons
                          Internal Component                              Analog          Default                                                                                                       Attribution-ShareAlike 4.0
                                                                                                                                                                                                        International License. To view a
                                                                                                                                                                                                        copy of this license, visit http://
                                                                                                                                                                                                        creativecommons.org/licenses/
                          Other Pins (Reset, System                       PWM/Timer                                                                                                                     by-sa/4.0/ or send a letter to
                                                                                                                                                                                                        Creative Commons, PO Box 1866,
                          Control, Debugging)                                                                                                                                                           Mountain View, CA 94042, USA.
```
