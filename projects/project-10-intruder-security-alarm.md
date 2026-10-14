# Project 10: Ultrasonic Change-Detection Alarm

**Platform:** Arduino Nano or Uno

**Difficulty:** Intermediate

**Estimated session:** 60–75 minutes

**Group:** 2–3 students; shared inventory rotates between activities.

**Revised:** 14 October 2026

## What students build

A sonar faces a fixed flat reference target. Ten valid samples establish a baseline; an object at least 20cm closer triggers a latched alarm. Missing/invalid echoes cause a distinct latched sensor fault rather than an armed indication. A button disarms/resets; pressing it again requests recalibration.

## Materials and preparation

Use the items in the [revised procurement plan](../School_Electronics_Club_Procurement_Plan_LKR_50000.md). The club needs a computer and the correct USB **data** cable for programming. Disconnect power before changing wiring. These are classroom prototypes; hardware acceptance checks below still need to be performed.

| Item from revised inventory | Quantity needed for this build |
| :-- | :-- |
| Nano and USB-C data cable | 1 |
| HC-SR04 | 1 |
| red and green LEDs | 1 each |
| 1kΩ resistors | 3 |
| passive piezo disc | 1 |
| button | 1 |
| breadboard/jumpers | 1 |


## Complete wiring and power

HC-SR04 VCC → board 5V; GND → board GND. These guides use 5V Uno/Nano boards. Never carry the 5V ECHO signal directly into a micro:bit. Each measurement has a timeout and readings outside 2–400cm are invalid; invalid does not mean “clear.” Wait at least 60ms between triggers on the same module; two-module builds alternate triggers at least 60ms apart to reduce crosstalk. Test your actual module against a flat target.

Buttons connect between their GPIO and GND and use `INPUT_PULLUP`: released is HIGH, pressed is LOW. Use opposite switched terminals, not the two legs already connected internally. No external pull-down resistor is required.

Use a **passive piezo disc**, not the DC continuous alarm: GPIO → 1kΩ resistor → piezo lead; other lead → GND. The resistor limits drive current and the sound may be quiet. Solder flexible leads to the disc with adult supervision; never substitute a magnetic buzzer or speaker without a suitable driver.

TRIG D9; ECHO D10; green LED D4 and red LED D5 each through 1kΩ, cathodes GND; piezo D6 through 1kΩ; reset/arm button D2 to GND. Board power is USB.

## Complete source code

Paste this entire sketch into Arduino IDE. Select **Arduino Uno** for the Uno or **Arduino Nano / ATmega328P** for a classic Nano; some CH340 Nano clones require the old bootloader setting. Use Arduino AVR Boards 1.8.6. SoftwareSerial is included in that core; install any additional libraries specified for this project below.

```cpp
#include <Arduino.h>
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
Button arm;
byte mode=0, count=0, attempts=0; // 0 disarmed, 1 calibrating, 2 armed, 3 alarm, 4 fault
float total=0, baseline=0;
unsigned long lastSample=0;
void calibrate() { count=attempts=0; total=0; mode=1; Serial.println("Calibrating..."); }
void setup() {
  Serial.begin(9600); arm.begin(2);
  pinMode(9,OUTPUT); pinMode(10,INPUT);
  pinMode(4,OUTPUT); pinMode(5,OUTPUT); pinMode(6,OUTPUT);
  Serial.println("Place a reference target; press button to arm.");
}
void loop() {
  if (arm.update()) {
    if (mode==0) calibrate(); else { mode=0; noTone(6); Serial.println("Disarmed/reset"); }
  }
  unsigned long now=millis();
  if ((mode==1 || mode==2) && now-lastSample>=75) {
    lastSample=now; float d=distanceCM(9,10);
    if (mode==1) {
      attempts++;
      if (d>0) { total+=d; count++; }
      if (count==10) { baseline=total/count; mode=2; Serial.print("Baseline cm: "); Serial.println(baseline); }
      else if (attempts>=20) { mode=4; Serial.println("Calibration failed: sensor fault"); }
    } else if (d<0) { mode=4; Serial.println("Sensor fault: echo invalid"); }
    else if (baseline-d>20) { mode=3; Serial.println("Closer object detected"); }
  }
  digitalWrite(4,mode==2);
  digitalWrite(5,(mode==3 || mode==4) && (now/250)%2==0);
  if (mode==3) tone(6,(now/300)%2 ? 800:1200);
  else if (mode==4 && (now/500)%2==0) tone(6,300);
  else noTone(6);
}
```

## Build, test and acceptance checks

1. Put a broad flat target 60–100cm away and press arm. Green lights only after ten valid readings.
2. Insert an object more than 20cm nearer: red and alternating tones latch. Press to disarm.
3. Disconnect the echo wire with power off, restart and attempt calibration: it must report fault, never armed. Restore the circuit and repeat.
4. While armed, remove the reference target: invalid echoes must indicate a fault. This is a demonstration, not a security product.

## Extension

Add an LCD showing baseline, current reading and explicit armed/fault states.

## Verification status

The wiring and code have been revised to address the feasibility review. Software checks and their limits are recorded in [VALIDATION.md](../VALIDATION.md). Physical testing of the exact purchased parts is still required before a student session.
