# Project 13: Touchless Cardboard Dustbin Model

**Platform:** Arduino Nano or Uno

**Difficulty:** Intermediate

**Estimated session:** 75–90 minutes

**Group:** 2–3 students; shared inventory rotates between activities.

**Revised:** 14 October 2026

## What students build

A lightweight cardboard lid opens for a hand closer than 20cm. It closes gradually only after four seconds of valid clear readings. A nearby hand or invalid echo during closure reopens it. This is a supervised model, not a hygienic or certified anti-pinch product.

## Materials and preparation

Use the items in the [revised procurement plan](../School_Electronics_Club_Procurement_Plan_LKR_50000.md). The club needs a computer and the correct USB **data** cable for programming. Disconnect power before changing wiring. These are classroom prototypes; hardware acceptance checks below still need to be performed.

| Item from revised inventory | Quantity needed for this build |
| :-- | :-- |
| Nano and USB-C data cable | 1 |
| HC-SR04 | 1 |
| SG90 with horn | 1 |
| 5V/2A adapter and DC socket | 1 |
| 470µF capacitor ≥10V | 1 |
| full breadboard/jumpers | 1 |
| glue gun, matching 11mm glue sticks, cardboard hinge/link | shared |


## Complete wiring and power

Power the board through its USB socket. Power the SG90 red lead from the separate **regulated 5V/2A adapter** through its matching DC screw-terminal socket; brown goes to adapter negative. Join adapter negative to board GND. Only the servo signal connects to the listed GPIO. Do not join adapter +5V to the board's USB-derived 5V rail, micro:bit 3V, or Vin. Add a 470µF capacitor (rated at least 10V) across the servo supply near the servo, positive to +5V and negative to GND. Use short power wires and a lightweight, freely moving model. Check voltage and polarity before attaching the servo. If the board resets or the servo stalls, disconnect and correct supply/wiring/linkage before continuing.

HC-SR04 VCC → board 5V; GND → board GND. These guides use 5V Uno/Nano boards. Never carry the 5V ECHO signal directly into a micro:bit. Each measurement has a timeout and readings outside 2–400cm are invalid; invalid does not mean “clear.” Wait at least 60ms between triggers on the same module; two-module builds alternate triggers at least 60ms apart to reduce crosstalk. Test your actual module against a flat target.

TRIG D9; ECHO D10; servo signal D5. Mount the sonar on the **stationary front wall**, aimed at the approach area. Keep the lid light and linkage loose; confirm its path is clear. The sonar does not cover every possible pinch point.

## Complete source code

Install **Servo 1.2.2 by Arduino** from Library Manager.

Paste this entire sketch into Arduino IDE. Select **Arduino Uno** for the Uno or **Arduino Nano / ATmega328P** for a classic Nano; some CH340 Nano clones require the old bootloader setting. Use Arduino AVR Boards 1.8.6. SoftwareSerial is included in that core; install any additional libraries specified for this project below.

```cpp
#include <Arduino.h>
#include <Servo.h>
float distanceCM(byte trig, byte echo) {
  digitalWrite(trig, LOW); delayMicroseconds(2);
  digitalWrite(trig, HIGH); delayMicroseconds(10); digitalWrite(trig, LOW);
  unsigned long us = pulseIn(echo, HIGH, 25000UL);
  float cm = us * 0.0343f / 2.0f;
  return (us == 0 || cm < 2 || cm > 400) ? -1.0f : cm;
}
Servo lid;
const int CLOSED=10, OPEN=90;
int angle=CLOSED;
byte state=0; // 0 closed, 1 opening, 2 open, 3 closing
bool clear=false;
unsigned long lastPing=0, lastMove=0, clearSince=0;
void setup() {
  Serial.begin(9600); pinMode(9,OUTPUT); pinMode(10,INPUT);
  lid.attach(5); lid.write(CLOSED);
}
void loop() {
  unsigned long now=millis();
  if (now-lastPing>=75) {
    lastPing=now; float d=distanceCM(9,10);
    bool wasClear=clear; clear=d>=25;
    if (!clear || !wasClear) clearSince=now;
    if (d>0 && d<20 && state==0) state=1;
    if (!clear && state==3) state=1; // Invalid echo also cancels closure.
    if (d<0) Serial.println("Invalid echo: closure inhibited");
  }
  if (state==2 && clear && now-clearSince>=4000) state=3;
  if (now-lastMove>=20) {
    lastMove=now;
    if (state==1) { angle=min(OPEN,angle+2); lid.write(angle); if(angle==OPEN) {state=2; clearSince=now;} }
    else if (state==3) { angle=max(CLOSED,angle-2); lid.write(angle); if(angle==CLOSED) state=0; }
  }
}
```

## Build, test and acceptance checks

1. Verify 5V power and common ground. Test the unloaded servo before attaching the cardboard lid.
2. Place a flat reference surface within sonar range beyond the 25cm clear threshold. A valid clear echo is needed to close; an empty beam may time out and keep the model open.
3. Wave a hand at 10–15cm, remove it and check the four-second clear delay. Return the hand while closing: it should reopen.
4. Disconnect ECHO with power off, then restart/test: invalid echoes must inhibit closure. Keep fingers out of the linkage throughout.

## Extension

Add a second downward-facing sensor for a bin-full indication, with spaced alternating pings.

## Verification status

The wiring and code have been revised to address the feasibility review. Software checks and their limits are recorded in [VALIDATION.md](../VALIDATION.md). Physical testing of the exact purchased parts is still required before a student session.
