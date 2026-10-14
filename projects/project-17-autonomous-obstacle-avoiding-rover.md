# Project 17: Obstacle-Avoiding Classroom Rover

**Platform:** Arduino Uno

**Difficulty:** Advanced

**Estimated session:** 120–150 minutes

**Group:** 2–3 students; shared inventory rotates between activities.

**Revised:** 14 October 2026

## What students build

After completing the motor bench test, mount sonar on a servo. The rover drives slowly on valid clear readings, stops for an obstacle, scans right and left, and makes a timed turn toward a valid clear direction. A missing echo stops the rover; an empty room with no reflecting targets may therefore keep it stopped. Reverse is deliberately omitted because this build has no rear sensor.

## Materials and preparation

Use the items in the [revised procurement plan](../School_Electronics_Club_Procurement_Plan_LKR_50000.md). The club needs a computer and the correct USB **data** cable for programming. Disconnect power before changing wiring. These are classroom prototypes; hardware acceptance checks below still need to be performed.

| Item from revised inventory | Quantity needed for this build |
| :-- | :-- |
| robot kit: chassis, motors, Uno/cable, L298N, HC-SR04, SG90, 4×AA holder | 1 |
| AA cells | 4 |
| 5V/2A USB power bank and USB power breakout | 1 each |
| 470µF capacitor ≥10V | 1 |
| 100nF motor capacitors | 2 |
| motor switch, 2A fuse/holder, power wire | shared |
| jumpers, servo horn/mount, glue gun/11mm sticks | shared |


## Complete wiring and power

Use the full robot kit's L298N, motors, chassis and **4×AA holder**; verify that the delivered holder really is four-cell before purchase. Fit four matched alkaline AA cells (nominal 6V) for motor power. The L298N loses voltage, so this is a modest-speed model; the available torque must be tested. Do not replace the pack with a PP3 9V battery, connect motors to GPIO, or use the breadboard regulator for motor power.

**Remove ENA and ENB jumpers** before wiring PWM, and **remove the separate 5V-EN/regulator-enable jumper** to disable the module's onboard regulator. Supply its labelled 5V logic terminal from the external regulated 5V source. On modules with different routing, confirm the board diagram before connecting power. Never join its regulator output to another 5V source.

| L298N/module terminal | Connection |
| :-- | :-- |
| Motor supply, often labelled +12V/Vs | Four-AA positive through switch and inline 2A fuse |
| GND | Four-AA negative, external 5V negative and board GND |
| Logic +5V | External regulated 5V; 5V-EN jumper removed |
| ENA / ENB | Board D5 / D6; both enable jumpers removed |
| IN1 / IN2 / IN3 / IN4 | D7 / D8 / D9 / D10 |
| OUT1 / OUT2 | Left motor |
| OUT3 / OUT4 | Right motor |
| 100nF ceramic capacitors | One across each motor's terminals |

Use insulated stranded power wire (about 22AWG), screw terminals and secure strain relief for motor current, not thin jumper leads or breadboard rails. The fuse protects wiring against a short; it does not make stalled motors safe. Verify motors are rated 3–6V, driver flyback diodes are fitted, and the motor case/driver does not overheat. If the four-AA/L298N combination cannot start reliably under the intended load, stop and use a separately quoted lower-loss driver rather than raising voltage blindly. The revised budget includes initial cells and spares, not recurring annual replacements.

For an untethered rover use the listed enclosed **USB power bank, fixed 5V output and at least 2A total continuous rating**, with two outputs: one powers the Uno through its USB socket/cable; the other powers L298N logic and the SG90 rail through a USB-A power breakout/screw-terminal cable. Add a 470µF ≥10V capacitor near the servo. Verify the power bank stays on at idle and holds 5V during servo motion. Do not use a USB-PD higher-voltage trigger, connect either pack to Uno Vin, or join this 5V rail to the Uno 5V pin. Join grounds as shown. For bench testing, the board can use computer USB and a separate 5V/2A adapter can provide the peripheral rail; do not connect both peripheral sources at once.

HC-SR04 VCC → board 5V; GND → board GND. These guides use 5V Uno/Nano boards. Never carry the 5V ECHO signal directly into a micro:bit. Each measurement has a timeout and readings outside 2–400cm are invalid; invalid does not mean “clear.” Wait at least 60ms between triggers on the same module; two-module builds alternate triggers at least 60ms apart to reduce crosstalk. Test your actual module against a flat target.

HC-SR04 TRIG D12, ECHO D13, VCC board 5V and GND common. Servo signal D11, red external peripheral 5V, brown common ground. Keep D5/D6 for motor PWM: the Uno Servo library uses Timer1 and disables PWM on D9/D10, which are used only as digital direction pins here. Attach the sensor securely on a balanced lightweight mount.

## Complete source code

Install **Servo 1.2.2 by Arduino** from Library Manager.

Paste this entire sketch into Arduino IDE. Select **Arduino Uno** for the Uno or **Arduino Nano / ATmega328P** for a classic Nano; some CH340 Nano clones require the old bootloader setting. Use Arduino AVR Boards 1.8.6. SoftwareSerial is included in that core; install any additional libraries specified for this project below.

```cpp
#include <Arduino.h>
#include <Servo.h>
const byte ENA=5, ENB=6, IN1=7, IN2=8, IN3=9, IN4=10;
void motor(int left, int right) {
  // Disable bridges before changing direction.
  analogWrite(ENA,0); analogWrite(ENB,0);
  digitalWrite(IN1,left>0); digitalWrite(IN2,left<0);
  digitalWrite(IN3,right>0); digitalWrite(IN4,right<0);
  analogWrite(ENA,constrain(abs(left),0,255));
  analogWrite(ENB,constrain(abs(right),0,255));
}
void stopCar() { motor(0,0); } // Enable LOW: coast; this is not active braking.
void beginMotors() {
  for(byte p=5;p<=10;p++) { digitalWrite(p,LOW); pinMode(p,OUTPUT); }
  stopCar();
}
float distanceCM(byte trig, byte echo) {
  digitalWrite(trig, LOW); delayMicroseconds(2);
  digitalWrite(trig, HIGH); delayMicroseconds(10); digitalWrite(trig, LOW);
  unsigned long us = pulseIn(echo, HIGH, 25000UL);
  float cm = us * 0.0343f / 2.0f;
  return (us == 0 || cm < 2 || cm > 400) ? -1.0f : cm;
}
Servo head;
const int SPEED=130;
float look(int angle) { head.write(angle); delay(450); return distanceCM(12,13); }
void setup() {
  Serial.begin(9600); beginMotors(); pinMode(12,OUTPUT); pinMode(13,INPUT);
  head.attach(11); head.write(90); delay(2000);
}
void loop() {
  float ahead=distanceCM(12,13);
  if(ahead<0) { stopCar(); Serial.println("Echo invalid: stopped"); delay(150); return; }
  if(ahead>30) { motor(SPEED,SPEED); delay(75); return; }
  stopCar(); delay(150);
  float right=look(30), left=look(150);
  head.write(90); delay(450);
  if(right>30 && (left<0 || right>=left)) motor(SPEED,-SPEED);
  else if(left>30) motor(-SPEED,SPEED);
  else { stopCar(); Serial.println("No valid clear route"); delay(150); return; }
  delay(350); stopCar(); delay(100);
  // The next loop remeasures before allowing forward movement.
}
```

## Build, test and acceptance checks

1. Complete project 16 with wheels lifted. Check sensor distance against a ruler, then check servo angles without driving.
2. Power from the USB bank and AA pack; sweep the servo and check for resets or power-bank shutdown.
3. On the floor at low speed, approach broad flat cardboard obstacles. Tune SPEED, the 30cm threshold and 350ms turn duration for the actual chassis. Keep the swept wheel path clear.
4. Cause an invalid echo and verify wheels stop, including after a turn. Test a dead end: the rover should wait rather than make a blind reverse. Use only a supervised floor course, away from stairs.

## Extension

Add separately tested rear sensing before implementing reverse manoeuvres; add sample filtering after observing actual sensor noise.

## Verification status

The wiring and code have been revised to address the feasibility review. Software checks and their limits are recorded in [VALIDATION.md](../VALIDATION.md). Physical testing of the exact purchased parts is still required before a student session.
