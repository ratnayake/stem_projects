# Project 15: Secret Knock Detector with Model Servo Latch

**Platform:** Arduino Uno

**Difficulty:** Advanced

**Estimated session:** 90–120 minutes

**Group:** 2–3 students; shared inventory rotates between activities.

**Revised:** 14 October 2026

## What students build

A **bare passive piezo disc** senses taps on a cardboard panel. Five knocks produce four time intervals, normalized against the first. The pattern [100,50,50,100] must match within 20% of each target ratio. Successful recognition moves a light model latch for four seconds. This is a learning exercise, not a secure door lock.

## Materials and preparation

Use the items in the [revised procurement plan](../School_Electronics_Club_Procurement_Plan_LKR_50000.md). The club needs a computer and the correct USB **data** cable for programming. Disconnect power before changing wiring. These are classroom prototypes; hardware acceptance checks below still need to be performed.

| Item from revised inventory | Quantity needed for this build |
| :-- | :-- |
| Uno and USB data cable | 1 |
| bare 35mm passive piezo disc | 1 |
| 1MΩ through-hole resistor | 1 |
| 10kΩ series resistor | 1 |
| BAT85 Schottky diodes | 2 |
| SG90 with horn | 1 |
| 5V/2A adapter and DC socket | 1 |
| 470µF capacitor ≥10V | 1 |
| red and green LEDs | 1 each |
| 1kΩ resistors | 2 |
| breadboard/jumpers and cardboard panel | shared |


## Complete wiring and power

Power the board through its USB socket. Power the SG90 red lead from the separate **regulated 5V/2A adapter** through its matching DC screw-terminal socket; brown goes to adapter negative. Join adapter negative to board GND. Only the servo signal connects to the listed GPIO. Do not join adapter +5V to the board's USB-derived 5V rail, micro:bit 3V, or Vin. Add a 470µF capacitor (rated at least 10V) across the servo supply near the servo, positive to +5V and negative to GND. Use short power wires and a lightweight, freely moving model. Check voltage and polarity before attaching the servo. If the board resets or the servo stalls, disconnect and correct supply/wiring/linkage before continuing.

Use the bare piezo, **not** the DC active alarm. Wire the input protection before connecting A0:

| Part | Connection |
| :-- | :-- |
| Piezo brass/negative lead | GND |
| Piezo ceramic/positive lead | Sensor node S |
| 1MΩ resistor | S to GND, across the piezo |
| 10kΩ series resistor | S to A0 |
| Lower BAT85 | Anode GND, cathode/banded end A0 |
| Upper BAT85 | Anode A0, cathode/banded end board 5V |
| Servo signal | D9 |
| Green/red LED | D4/D5, each via 1kΩ to anode; cathodes GND |

The bleed resistor and series resistor perform different jobs; neither can be replaced by two 10kΩ resistors. Clamps limit excursions at A0; powered testing is required because piezo pulses can inject current into an unpowered rail. Use gentle taps, never hard strikes. Mount the disc without cracking the ceramic and solder flexible leads with supervision. The diode polarity must be checked before sensor connection.

## Complete source code

Install **Servo 1.2.2 by Arduino** from Library Manager.

Paste this entire sketch into Arduino IDE. Select **Arduino Uno** for the Uno or **Arduino Nano / ATmega328P** for a classic Nano; some CH340 Nano clones require the old bootloader setting. Use Arduino AVR Boards 1.8.6. SoftwareSerial is included in that core; install any additional libraries specified for this project below.

```cpp
#include <Arduino.h>
#include <Servo.h>
Servo latch;
const int THRESHOLD=60;
const int ratios[4]={100,50,50,100};
unsigned long intervals[4],lastKnock=0;
byte knocks=0;
bool rearmed=true;
void resetPattern() { knocks=0; rearmed=false; lastKnock=millis(); }
void evaluate() {
  bool match=intervals[0]>0;
  for(byte i=0;i<4 && match;i++) {
    float normalized=100.0f*intervals[i]/intervals[0];
    if(fabs(normalized-ratios[i])>ratios[i]*0.20f) match=false;
  }
  Serial.println(match ? "Pattern accepted" : "Pattern rejected");
  if(match) {
    digitalWrite(5,LOW); digitalWrite(4,HIGH); latch.write(90); delay(4000);
    latch.write(15); digitalWrite(4,LOW); digitalWrite(5,HIGH);
  }
  resetPattern();
}
void setup() {
  Serial.begin(9600); pinMode(4,OUTPUT); pinMode(5,OUTPUT);
  digitalWrite(5,HIGH); latch.attach(9); latch.write(15);
  delay(1000); lastKnock=millis();
}
void loop() {
  int value=analogRead(A0); unsigned long now=millis();
  if(value<THRESHOLD/2) rearmed=true;
  if(knocks>0 && now-lastKnock>2000) { Serial.println("Pattern timeout"); resetPattern(); }
  if(rearmed && value>THRESHOLD && now-lastKnock>=120) {
    rearmed=false;
    if(knocks>0) intervals[knocks-1]=now-lastKnock;
    lastKnock=now; knocks++;
    Serial.print("Knock "); Serial.println(knocks);
    if(knocks==5) evaluate();
  }
}
```

## Build, test and acceptance checks

1. Inspect clamp diode bands, 1MΩ bleed, 10kΩ series resistance and external servo power. Initially leave the model latch off.
2. Observe gentle taps in Serial Monitor and tune THRESHOLD so a tap registers once and silence does not.
3. Try intervals approximately 600,300,300,600ms, then a proportional slower rhythm; both should match if inside the two-second interval limit. A different rhythm should fail.
4. Stop halfway for more than two seconds and confirm reset. Attach only a lightweight latch and test without stressing the SG90.

## Reference notes

[Arduino knock example](https://docs.arduino.cc/built-in-examples/sensors/Knock?setlang=it) uses a piezo element with a 1MΩ parallel resistor; this build also includes series resistance and external clamps.

## Extension

Add a supervised teach button to store a different rhythm; do not use this as an access-control product.

## Verification status

The wiring and code have been revised to address the feasibility review. Software checks and their limits are recorded in [VALIDATION.md](../VALIDATION.md). Physical testing of the exact purchased parts is still required before a student session.
