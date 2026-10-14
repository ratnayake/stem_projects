# Project 18: Bluetooth Smartphone RC Car with Command Timeout

**Platform:** Arduino Uno

**Difficulty:** Advanced

**Estimated session:** 90–120 minutes

**Group:** 2–3 students; shared inventory rotates between activities.

**Revised:** 14 October 2026

## What students build

An Android Bluetooth Classic/SPP controller sends F/B/L/R/S characters. Valid motion commands must repeat at least every 100ms; after 400ms without a valid command the car stops. SoftwareSerial keeps HC-06 traffic off the USB upload pins. Unknown commands stop the motors; CR/LF framing is ignored.

## Materials and preparation

Use the items in the [revised procurement plan](../School_Electronics_Club_Procurement_Plan_LKR_50000.md). The club needs a computer and the correct USB **data** cable for programming. Disconnect power before changing wiring. These are classroom prototypes; hardware acceptance checks below still need to be performed.

| Item from revised inventory | Quantity needed for this build |
| :-- | :-- |
| robot kit: chassis, motors, Uno/cable, L298N, 4×AA holder | 1 |
| HC-06 carrier module with 5V VCC regulator | 1 |
| 1kΩ resistors | 3 |
| AA cells | 4 |
| 5V/2A USB power bank and USB power breakout | 1 each |
| 100nF motor capacitors | 2 |
| motor switch, 2A fuse/holder, power wire and signal jumpers | shared |
| Android Bluetooth Classic/SPP phone | school-provided |


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

Use the listed enclosed **USB power bank with two fixed-5V outputs and at least 2A total continuous rating**. One output powers the Uno through its USB socket/cable; the second powers L298N logic through the USB-A 5V/GND screw-terminal cable. Verify the bank stays on at idle. Do not use a USB-PD higher-voltage trigger, connect the four-AA pack to Uno Vin, or join the peripheral 5V terminal to the Uno 5V pin. Join all grounds. For bench testing, use computer USB for Uno and the separate 5V/2A adapter/DC socket for driver logic; never attach both peripheral sources at once.

For this build the peripheral 5V supplies L298N logic only; detach the sonar and servo from project 17. An HC-06 **carrier** with onboard VCC regulator may use board 5V; a bare 3.3V module needs a different regulated supply and is not the specified purchase.

| HC-06 connection | Destination |
| :-- | :-- |
| VCC / GND | Uno 5V / common GND |
| TXD | Uno D2 (SoftwareSerial RX) |
| RXD | Divider node N below |

```
Uno D3 (TX) -- 1kΩ -- N -- 1kΩ -- 1kΩ -- GND
                       |
                    HC-06 RXD
```

N receives about 3.33V from a 5V TX signal. The two lower 1kΩ resistors are in series (2kΩ total). Uno D0/D1 stay unconnected to HC-06, avoiding upload contention. Do not connect Uno TX directly to HC-06 RXD.

## Complete source code

Paste this entire sketch into Arduino IDE. Select **Arduino Uno** for the Uno or **Arduino Nano / ATmega328P** for a classic Nano; some CH340 Nano clones require the old bootloader setting. Use Arduino AVR Boards 1.8.6. SoftwareSerial is included in that core; install any additional libraries specified for this project below.

```cpp
#include <Arduino.h>
#include <SoftwareSerial.h>
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
SoftwareSerial bluetooth(2,3); // Board RX, TX
unsigned long lastCommand=0;
bool moving=false;
const int SPEED=140;
void setup() {
  beginMotors(); bluetooth.begin(9600); Serial.begin(9600);
  Serial.println("Repeat F/B/L/R/S every <=100ms. Timeout 400ms.");
}
void loop() {
  while(bluetooth.available()) {
    char c=bluetooth.read();
    if(c=='\r' || c=='\n') continue;
    bool valid=true;
    switch(c) {
      case 'F': motor(SPEED,SPEED); moving=true; break;
      case 'B': motor(-SPEED,-SPEED); moving=true; break;
      case 'L': motor(-SPEED,SPEED); moving=true; break;
      case 'R': motor(SPEED,-SPEED); moving=true; break;
      case 'S': stopCar(); moving=false; break;
      default: stopCar(); moving=false; valid=false; break;
    }
    if(valid) lastCommand=millis();
  }
  if(moving && millis()-lastCommand>=400) {stopCar(); moving=false;}
}
```

## Build, test and acceptance checks

1. Complete project 16 first. Verify the divider and VCC regulator, upload with wheels raised and pair the phone to HC-06 (the supplied firmware may use PIN 1234 or 0000).
2. Use an Android app supporting **Bluetooth Classic SPP** and custom single-character button messages. Configure repeated commands ≤100ms and S on release; not every RC app uses this protocol. A generic serial terminal can send a command for a short test pulse.
3. Check F/B/L/R/S and an unknown character. Without repetition, one motion command must stop after about 400ms.
4. Disconnect Bluetooth while sending forward repeatedly; confirm automatic stop. Test power-bank idle and motor voltage before slow supervised floor use.

## Extension

Add a speed command only after defining and testing its protocol and preserving the timeout.

## Verification status

The wiring and code have been revised to address the feasibility review. Software checks and their limits are recorded in [VALIDATION.md](../VALIDATION.md). Physical testing of the exact purchased parts is still required before a student session.
