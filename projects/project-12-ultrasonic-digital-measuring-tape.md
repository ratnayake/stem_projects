# Project 12: Ultrasonic Distance Meter with LCD

**Platform:** Arduino Uno

**Difficulty:** Intermediate

**Estimated session:** 60–75 minutes

**Group:** 2–3 students; shared inventory rotates between activities.

**Revised:** 14 October 2026

## What students build

A button captures five spaced sonar readings; the median of at least three valid samples is displayed in cm and inches. A timeout is never converted to a valid distance. This is an approximate acoustic distance meter, not a precision measuring tape.

## Materials and preparation

Use the items in the [revised procurement plan](../School_Electronics_Club_Procurement_Plan_LKR_50000.md). The club needs a computer and the correct USB **data** cable for programming. Disconnect power before changing wiring. These are classroom prototypes; hardware acceptance checks below still need to be performed.

| Item from revised inventory | Quantity needed for this build |
| :-- | :-- |
| Uno and USB data cable | 1 |
| HC-SR04 | 1 |
| LCD and I2C backpack | 1 each |
| button | 1 |
| breadboard/jumpers | 1 |
| soldering tools | shared LCD assembly |


## Complete wiring and power

Solder the backpack's 16-pin header to the LCD if supplied separately. Use **hd44780 1.3.2 by Bill Perry**, class `hd44780_I2Cexp`, from Arduino Library Manager; it detects supported backpack pin mappings and addresses. Run its `I2CexpDiag` example first. LCD VCC → 5V, GND → GND, SDA → A4, SCL → A5 on Uno/classic Nano. Adjust the backpack contrast trimmer. A failed `lcd.begin(16, 2)` halts the sketch; check wiring and diagnosis before retrying.

HC-SR04 VCC → board 5V; GND → board GND. These guides use 5V Uno/Nano boards. Never carry the 5V ECHO signal directly into a micro:bit. Each measurement has a timeout and readings outside 2–400cm are invalid; invalid does not mean “clear.” Wait at least 60ms between triggers on the same module; two-module builds alternate triggers at least 60ms apart to reduce crosstalk. Test your actual module against a flat target.

Buttons connect between their GPIO and GND and use `INPUT_PULLUP`: released is HIGH, pressed is LOW. Use opposite switched terminals, not the two legs already connected internally. No external pull-down resistor is required.

TRIG D9; ECHO D10; measurement button D2 to GND. Power the board by USB; the listed USB power bank permits portable use through the board USB socket.

## Complete source code

Paste this entire sketch into Arduino IDE. Select **Arduino Uno** for the Uno or **Arduino Nano / ATmega328P** for a classic Nano; some CH340 Nano clones require the old bootloader setting. Use Arduino AVR Boards 1.8.6. SoftwareSerial is included in that core; install any additional libraries specified for this project below.

```cpp
#include <Arduino.h>
#include <Wire.h>
#include <hd44780.h>
#include <hd44780ioClass/hd44780_I2Cexp.h>
hd44780_I2Cexp lcd;
struct Button {
  byte pin;
  bool raw = HIGH, stable = HIGH;
  unsigned long changed = 0;
  void begin(byte p) { pin = p; pinMode(pin, INPUT_PULLUP);
    raw = stable = digitalRead(pin); changed = millis(); }
  bool update() {
    bool r = digitalRead(pin);
    if (r != raw) { raw = r; changed = millis(); }
    if (millis() - changed >= 25 && stable != raw) {
      stable = raw; return stable == LOW;
    }
    return false;
  }
  bool down() { return stable == LOW; }
};
float distanceCM(byte trig, byte echo) {
  digitalWrite(trig, LOW); delayMicroseconds(2);
  digitalWrite(trig, HIGH); delayMicroseconds(10); digitalWrite(trig, LOW);
  unsigned long us = pulseIn(echo, HIGH, 25000UL);
  float cm = us * 0.0343f / 2.0f;
  return (us == 0 || cm < 2 || cm > 400) ? -1.0f : cm;
}
Button measure;
float medianDistance() {
  float values[5]; byte count=0;
  for (byte i=0;i<5;i++) {
    float d=distanceCM(9,10); if (d>0) values[count++]=d;
    delay(70);
  }
  if (count<3) return -1;
  for (byte i=1;i<count;i++) for (byte j=i;j>0 && values[j]<values[j-1];j--) {
    float tmp=values[j]; values[j]=values[j-1]; values[j-1]=tmp;
  }
  return count%2 ? values[count/2] : (values[count/2-1]+values[count/2])/2;
}
void setup() {
  Serial.begin(9600); measure.begin(2); pinMode(9,OUTPUT); pinMode(10,INPUT);
  if (lcd.begin(16,2)) { Serial.println("LCD init failed"); while(true) delay(1000); }
  lcd.backlight(); lcd.print("Press to measure");
}
void loop() {
  if (measure.update()) {
    lcd.clear(); lcd.print("Measuring..."); float cm=medianDistance(); lcd.clear();
    if (cm<0) { lcd.print("Out of range"); lcd.setCursor(0,1); lcd.print("Check target"); }
    else {
      lcd.print(cm,1); lcd.print(" cm");
      lcd.setCursor(0,1); lcd.print(cm/2.54f,1); lcd.print(" in");
    }
  }
}
```

## Build, test and acceptance checks

1. Install hd44780 by Bill Perry and complete I2CexpDiag. Use a flat book as a target at 10, 30, 60 and 100cm from the transducer face.
2. Measure each distance and record error against a ruler; avoid claiming millimetre accuracy.
3. Remove the target or aim beyond range: display must show Out of range, not 400cm.
4. Hold the button: only one measurement should occur until release and a new press. Keep other sonar projects inactive nearby during testing.

## Extension

Add an enclosure offset measured from the sensor face; document its calibration.

## Verification status

The wiring and code have been revised to address the feasibility review. Software checks and their limits are recorded in [VALIDATION.md](../VALIDATION.md). Physical testing of the exact purchased parts is still required before a student session.
