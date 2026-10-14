# Project 14: Two-Sensor Model Parking Barrier

**Platform:** Arduino Uno

**Difficulty:** Intermediate

**Estimated session:** 75–90 minutes

**Group:** 2–3 students; shared inventory rotates between activities.

**Revised:** 14 October 2026

## What students build

One sonar detects an approaching model vehicle; a second monitors the model barrier zone against a fixed reference surface. The arm opens on approach and closes only after both zones give valid clear readings for 2.5 seconds. Invalid or occupied readings during closure reopen it. This demonstrates clearance interlocking with limited sonar coverage, not a real vehicle barrier.

## Materials and preparation

Use the items in the [revised procurement plan](../School_Electronics_Club_Procurement_Plan_LKR_50000.md). The club needs a computer and the correct USB **data** cable for programming. Disconnect power before changing wiring. These are classroom prototypes; hardware acceptance checks below still need to be performed.

| Item from revised inventory | Quantity needed for this build |
| :-- | :-- |
| Uno and USB data cable | 1 |
| HC-SR04 sensors | 2 |
| SG90 with horn | 1 |
| 5V/2A adapter and DC socket | 1 |
| 470µF capacitor ≥10V | 1 |
| red and green LEDs | 1 each |
| 1kΩ resistors | 2 |
| full breadboard/jumpers | 1 |
| glue gun, 11mm sticks, light cardboard arm | shared |


## Complete wiring and power

Power the board through its USB socket. Power the SG90 red lead from the separate **regulated 5V/2A adapter** through its matching DC screw-terminal socket; brown goes to adapter negative. Join adapter negative to board GND. Only the servo signal connects to the listed GPIO. Do not join adapter +5V to the board's USB-derived 5V rail, micro:bit 3V, or Vin. Add a 470µF capacitor (rated at least 10V) across the servo supply near the servo, positive to +5V and negative to GND. Use short power wires and a lightweight, freely moving model. Check voltage and polarity before attaching the servo. If the board resets or the servo stalls, disconnect and correct supply/wiring/linkage before continuing.

HC-SR04 VCC → board 5V; GND → board GND. These guides use 5V Uno/Nano boards. Never carry the 5V ECHO signal directly into a micro:bit. Each measurement has a timeout and readings outside 2–400cm are invalid; invalid does not mean “clear.” Wait at least 60ms between triggers on the same module; two-module builds alternate triggers at least 60ms apart to reduce crosstalk. Test your actual module against a flat target.

| Device | Connection |
| :-- | :-- |
| Approach sonar TRIG/ECHO | D9/D10 |
| Barrier-zone sonar TRIG/ECHO | D11/D12 |
| Both sonar VCC/GND | Board 5V/GND |
| Servo signal | D6 |
| Red LED | D4 → 1kΩ → anode; cathode GND |
| Green LED | D5 → 1kΩ → anode; cathode GND |

Aim each sonar at a stable surface about 40–100cm away in its clear state. Position the clearance sensor so the cardboard vehicle interrupts that path under the arm. Separate their beams and trigger them alternately. No echo is a fault, not proof of clearance.

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
Servo gate;
const int DOWN=15, UP=95;
float approach=-1, zone=-1;
byte state=0, nextSensor=0; // closed, opening, open, closing
int angle=DOWN;
bool wasClear=false;
unsigned long lastPing=0,lastMove=0,clearSince=0;
void setup() {
  pinMode(9,OUTPUT); pinMode(10,INPUT); pinMode(11,OUTPUT); pinMode(12,INPUT);
  pinMode(4,OUTPUT); pinMode(5,OUTPUT);
  gate.attach(6); gate.write(DOWN); Serial.begin(9600);
}
void loop() {
  unsigned long now=millis();
  if (now-lastPing>=70) {
    lastPing=now;
    if(nextSensor==0) approach=distanceCM(9,10); else zone=distanceCM(11,12);
    nextSensor=1-nextSensor;
    bool clear=approach>20 && zone>20;
    if (!clear || !wasClear) clearSince=now;
    wasClear=clear;
    if(state==0 && approach>0 && approach<12) state=1;
    if(state==3 && !clear) state=1;
    if(state==2 && clear && now-clearSince>=2500) state=3;
    if(approach<0 || zone<0) Serial.println("Sensor fault: closure inhibited");
  }
  if(now-lastMove>=20) {
    lastMove=now;
    if(state==1) {angle=min(UP,angle+2); gate.write(angle); if(angle==UP) {state=2; clearSince=now;} }
    else if(state==3) {angle=max(DOWN,angle-2); gate.write(angle); if(angle==DOWN) state=0; }
  }
  digitalWrite(4,state!=2); digitalWrite(5,state==2);
}
```

## Build, test and acceptance checks

1. Check external power, common grounds and sensor layout with the arm detached.
2. Move a cardboard vehicle within 12cm of approach sonar: the arm should rise. Hold it in the barrier sensor path: the arm should remain up.
3. Clear both paths to their reference surfaces and check the 2.5s delay before gradual closure.
4. Interrupt either path or cause a missing echo while closing: the arm should reopen. Test crosstalk and blind spots with the model; keep fingers away from the linkage.

## Extension

Use direction-aware entry/exit sensing before attempting occupancy counting; one approach trigger cannot reliably count parking slots.

## Verification status

The wiring and code have been revised to address the feasibility review. Software checks and their limits are recorded in [VALIDATION.md](../VALIDATION.md). Physical testing of the exact purchased parts is still required before a student session.
