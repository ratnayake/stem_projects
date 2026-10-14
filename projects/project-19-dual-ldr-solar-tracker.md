# Project 19: Dual-LDR Light-Following Tracker Model

**Platform:** Arduino Nano or Uno

**Difficulty:** Intermediate/advanced

**Estimated session:** 75–90 minutes

**Group:** 2–3 students; shared inventory rotates between activities.

**Revised:** 14 October 2026

## What students build

Two bare LDR dividers compare light on each side of a cardboard shadow vane. A servo moves a lightweight platform to reduce the difference. This is a light-following tracker model; no solar panel is included and no energy-generation gain is claimed.

## Materials and preparation

Use the items in the [revised procurement plan](../School_Electronics_Club_Procurement_Plan_LKR_50000.md). The club needs a computer and the correct USB **data** cable for programming. Disconnect power before changing wiring. These are classroom prototypes; hardware acceptance checks below still need to be performed.

| Item from revised inventory | Quantity needed for this build |
| :-- | :-- |
| Nano and USB-C data cable | 1 |
| matched bare GL12528 LDRs | 2 |
| 10kΩ resistors | 2 |
| SG90 and horn | 1 |
| 5V/2A adapter and DC socket | 1 |
| 470µF capacitor ≥10V | 1 |
| breadboard/jumpers, vane/platform, glue gun/11mm sticks | shared |


## Complete wiring and power

Power the board through its USB socket. Power the SG90 red lead from the separate **regulated 5V/2A adapter** through its matching DC screw-terminal socket; brown goes to adapter negative. Join adapter negative to board GND. Only the servo signal connects to the listed GPIO. Do not join adapter +5V to the board's USB-derived 5V rail, micro:bit 3V, or Vin. Add a 470µF capacitor (rated at least 10V) across the servo supply near the servo, positive to +5V and negative to GND. Use short power wires and a lightweight, freely moving model. Check voltage and polarity before attaching the servo. If the board resets or the servo stalls, disconnect and correct supply/wiring/linkage before continuing.

Wire each LDR divider identically: board 5V → LDR → measurement node → 10kΩ → GND. Left node goes to A0; right node goes to A1. Brighter light gives a higher reading. The servo signal goes to D9. Bare LDRs have two leads and no separate AO/DO pins. Mount them on the moving light platform with enough slack in the wires and a shadow vane between them.

## Complete source code

Install **Servo 1.2.2 by Arduino** from Library Manager.

Paste this entire sketch into Arduino IDE. Select **Arduino Uno** for the Uno or **Arduino Nano / ATmega328P** for a classic Nano; some CH340 Nano clones require the old bootloader setting. Use Arduino AVR Boards 1.8.6. SoftwareSerial is included in that core; install any additional libraries specified for this project below.

```cpp
#include <Arduino.h>
#include <Servo.h>
Servo tracker;
int angle=90;
const int DIRECTION=1; // Change to -1 if motion increases the measured imbalance.
const int RIGHT_OFFSET=0; // Calibrate under equal lighting.
const int TOLERANCE=40;
void setup() {Serial.begin(9600); tracker.attach(9); tracker.write(angle); delay(500);}
void loop() {
  long left=0,right=0;
  for(byte i=0;i<4;i++) {left+=analogRead(A0); right+=analogRead(A1); delay(5);}
  int l=left/4, r=right/4+RIGHT_OFFSET, error=l-r;
  Serial.print(l); Serial.print(','); Serial.print(r); Serial.print(','); Serial.println(error);
  if(l>80 || r>80) {
    if(error>TOLERANCE) angle-=2*DIRECTION;
    else if(error<-TOLERANCE) angle+=2*DIRECTION;
    angle=constrain(angle,20,160); tracker.write(angle);
  }
  delay(80);
}
```

## Build, test and acceptance checks

1. Verify external servo power; test both divider voltages before connecting A0/A1. Cover each LDR and confirm its value falls.
2. With equal light on both, set RIGHT_OFFSET to average(left − right) and choose a tolerance above the remaining noise.
3. Place a light on one side. Check that servo movement reduces the error; if it grows, change DIRECTION to -1 or swap sensor sides.
4. Move the light slowly between sides and verify tracking within 20–160°. Darkness should hold position, and hard stops must not stall the servo.

## Extension

A photovoltaic experiment requires a separately budgeted small panel and measured energy comparison against a fixed mount.

## Verification status

The wiring and code have been revised to address the feasibility review. Software checks and their limits are recorded in [VALIDATION.md](../VALIDATION.md). Physical testing of the exact purchased parts is still required before a student session.
