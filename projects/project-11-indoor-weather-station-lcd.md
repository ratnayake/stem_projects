# Project 11: Indoor Weather Station with I2C LCD

**Platform:** Arduino Uno

**Difficulty:** Intermediate

**Estimated session:** 60–75 minutes

**Group:** 2–3 students; shared inventory rotates between activities.

**Revised:** 14 October 2026

## What students build

A DHT11 reports classroom temperature and humidity every two seconds. The 16×2 LCD displays the values or a sensor error. DHT11 is suitable for trends; displaying decimal places would not improve its accuracy.

## Materials and preparation

Use the items in the [revised procurement plan](../School_Electronics_Club_Procurement_Plan_LKR_50000.md). The club needs a computer and the correct USB **data** cable for programming. Disconnect power before changing wiring. These are classroom prototypes; hardware acceptance checks below still need to be performed.

| Item from revised inventory | Quantity needed for this build |
| :-- | :-- |
| Uno and USB data cable | 1 |
| DHT11 module | 1 |
| 16×2 LCD and I2C backpack | 1 each |
| breadboard/jumpers | 1 |
| 10kΩ data pull-up | 1 if absent from module |
| soldering tools | shared assembly |


## Complete wiring and power

Solder the backpack's 16-pin header to the LCD if supplied separately. Use **hd44780 1.3.2 by Bill Perry**, class `hd44780_I2Cexp`, from Arduino Library Manager; it detects supported backpack pin mappings and addresses. Run its `I2CexpDiag` example first. LCD VCC → 5V, GND → GND, SDA → A4, SCL → A5 on Uno/classic Nano. Adjust the backpack contrast trimmer. A failed `lcd.begin(16, 2)` halts the sketch; check wiring and diagnosis before retrying.

DHT11 VCC → 5V, GND → GND, DATA → D2. Verify pin labels, not just wire colour. If the module has no data pull-up, add 10kΩ between DATA and 5V. Power Uno through USB.

## Complete source code

Paste this entire sketch into Arduino IDE. Select **Arduino Uno** for the Uno or **Arduino Nano / ATmega328P** for a classic Nano; some CH340 Nano clones require the old bootloader setting. Use Arduino AVR Boards 1.8.6. SoftwareSerial is included in that core; install any additional libraries specified for this project below.

```cpp
#include <Arduino.h>
#include <Wire.h>
#include <hd44780.h>
#include <hd44780ioClass/hd44780_I2Cexp.h>
hd44780_I2Cexp lcd;
#include <DHT.h>
DHT dht(2,DHT11);
void setup() {
  Serial.begin(9600); dht.begin();
  int status=lcd.begin(16,2);
  if (status) { Serial.println("LCD init failed; run I2CexpDiag."); while(true) delay(1000); }
  lcd.backlight(); lcd.print("WEATHER STATION"); delay(2000);
}
void loop() {
  float h=dht.readHumidity(), t=dht.readTemperature();
  lcd.clear();
  if (isnan(h) || isnan(t)) { lcd.print("Sensor error"); Serial.println("DHT read failed"); }
  else {
    lcd.print("Temp: "); lcd.print(t,0); lcd.write((byte)223); lcd.print("C");
    lcd.setCursor(0,1); lcd.print("Humidity: "); lcd.print(h,0); lcd.print("%");
    Serial.print(t); Serial.print(" C, "); Serial.print(h); Serial.println(" %RH");
  }
  delay(2000);
}
```

## Build, test and acceptance checks

1. Solder and inspect the backpack, run I2CexpDiag and adjust contrast. Install hd44780, **DHT sensor library 1.4.6 by Adafruit**, and **Adafruit Unified Sensor 1.1.15** in Library Manager.
2. Upload the complete sketch and check readings against a reference thermometer/hygrometer if available.
3. Disconnect DHT DATA with power off and restart; the LCD must show Sensor error.
4. Restore wiring and check readings recover; do not use this prototype for health or heat-safety decisions.

## Extension

Log trends to Serial Plotter; any fan extension requires a separately budgeted low-voltage fan and supply.

## Verification status

The wiring and code have been revised to address the feasibility review. Software checks and their limits are recorded in [VALIDATION.md](../VALIDATION.md). Physical testing of the exact purchased parts is still required before a student session.
