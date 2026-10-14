# Project 16: Dual Motor Speed & Direction Controller

**Platform:** Arduino Uno

**Difficulty:** Intermediate

**Estimated session:** 60–75 minutes

**Group:** 2–3 students; shared inventory rotates between activities.

**Revised:** 14 October 2026

## What students build

The full robot kit provides two TT motors and an L298N. The sketch ramps forward, stops, turns and reverses with wheels raised. The stop function disables the bridges and coasts; it is not an emergency brake.

## Materials and preparation

Use the items in the [revised procurement plan](../School_Electronics_Club_Procurement_Plan_LKR_50000.md). The club needs a computer and the correct USB **data** cable for programming. Disconnect power before changing wiring. These are classroom prototypes; hardware acceptance checks below still need to be performed.

| Item from revised inventory | Quantity needed for this build |
| :-- | :-- |
| full robot kit: Uno/cable, L298N, motor pair/chassis, 4×AA holder | 1 |
| AA alkaline cells | 4 |
| 5V/2A adapter and DC socket | 1 |
| 100nF ceramic capacitors | 2 |
| motor switch, 2A fuse/holder, 22AWG wire | shared power kit |
| jumpers for logic signals | 6 plus grounds |


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

Power the Uno through computer USB; supply L298N logic separately from the regulated 5V/2A adapter/DC socket, joining grounds only. The AA pack supplies only the motor Vs terminal.

## Complete source code

Paste this entire sketch into Arduino IDE. Select **Arduino Uno** for the Uno or **Arduino Nano / ATmega328P** for a classic Nano; some CH340 Nano clones require the old bootloader setting. Use Arduino AVR Boards 1.8.6. SoftwareSerial is included in that core; install any additional libraries specified for this project below.

```cpp
#include <Arduino.h>
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
void setup() { Serial.begin(9600); beginMotors(); delay(2000); }
void loop() {
  Serial.println("Forward ramp");
  for(int speed=80;speed<=240;speed+=20) { motor(speed,speed); delay(200); }
  delay(1000); stopCar(); delay(1000);
  Serial.println("Right turn"); motor(150,-150); delay(600); stopCar(); delay(1000);
  Serial.println("Reverse"); motor(-150,-150); delay(1000); stopCar(); delay(2000);
}
```

## Build, test and acceptance checks

1. Remove all three specified jumpers, check grounds and test 5V logic voltage before inserting AA cells. Lift the wheels and confirm startup leaves them stopped.
2. Apply motor power and verify forward/reverse directions. Swap one motor pair at its output terminal if its wheel direction is reversed, with all power disconnected.
3. Measure AA pack and motor voltages under load; check for failed starts, excessive heating and wiring movement.
4. Complete this test before combining the driver with sensors or Bluetooth. Power down immediately if a motor stalls.

## Reference notes

[ST L298 datasheet](https://www.st.com/resource/zh/datasheet/l298.pdf) specifies substantial bridge voltage drop. [Arduino power guidance](https://support.arduino.cc/hc/en-us/articles/360018922259-What-power-supply-can-I-use-with-my-Arduino-board) explains board supply requirements.

## Extension

Compare measured speed against PWM duty cycle without increasing the motor voltage beyond its rating.

## Verification status

The wiring and code have been revised to address the feasibility review. Software checks and their limits are recorded in [VALIDATION.md](../VALIDATION.md). Physical testing of the exact purchased parts is still required before a student session.
