# Project 06: Single Traffic Signal with Pedestrian Request

**Platform:** Arduino Nano or Uno

**Difficulty:** Beginner

**Estimated session:** 60 minutes

**Group:** 2–3 students; shared inventory rotates between activities.

**Revised:** 14 October 2026

## What students build

One red/yellow/green traffic signal stays green until a pedestrian requests a crossing. A non-blocking state machine keeps checking the button during each phase; requests during a crossing are served by that crossing, while a new request during the return-to-green phase waits for the minimum green time. This is a model of one road crossing, not a four-way junction.

## Materials and preparation

Use the items in the [revised procurement plan](../School_Electronics_Club_Procurement_Plan_LKR_50000.md). The club needs a computer and the correct USB **data** cable for programming. Disconnect power before changing wiring. These are classroom prototypes; hardware acceptance checks below still need to be performed.

| Item from revised inventory | Quantity needed for this build |
| :-- | :-- |
| Nano and USB-C data cable | 1 |
| full breadboard and jumpers | 1 |
| red/yellow/green LED | 1 each |
| 1kΩ through-hole resistors | 4 |
| passive piezo disc | 1 |
| push button | 1 |


## Complete wiring and power

Buttons connect between their GPIO and GND and use `INPUT_PULLUP`: released is HIGH, pressed is LOW. Use opposite switched terminals, not the two legs already connected internally. No external pull-down resistor is required.

Use a **passive piezo disc**, not the DC continuous alarm: GPIO → 1kΩ resistor → piezo lead; other lead → GND. The resistor limits drive current and the sound may be quiet. Solder flexible leads to the disc with adult supervision; never substitute a magnetic buzzer or speaker without a suitable driver.

| Component | Connection |
| :-- | :-- |
| Green LED | D8 → 1kΩ → anode; cathode → GND |
| Yellow LED | D9 → 1kΩ → anode; cathode → GND |
| Red LED | D10 → 1kΩ → anode; cathode → GND |
| Piezo | D11 via 1kΩ; other lead GND |
| Request button | D2 to GND |

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
Button request;
byte phase = 0;
bool pending = false;
unsigned long phaseSince = 0;
void setPhase(byte p) {
  phase = p; phaseSince = millis();
  digitalWrite(8, p == 0); digitalWrite(9, p == 1); digitalWrite(10, p >= 2);
  noTone(11);
}
void setup() {
  for (byte p = 8; p <= 11; p++) pinMode(p, OUTPUT);
  request.begin(2); setPhase(0);
}
void loop() {
  bool press = request.update();
  if (press && (phase == 0 || phase == 1)) pending = true;
  unsigned long elapsed = millis() - phaseSince;
  if (phase == 0 && pending && elapsed >= 3000) setPhase(1);
  else if (phase == 1 && elapsed >= 2500) { pending = false; setPhase(2); }
  else if (phase == 2 && elapsed >= 1000) setPhase(3);
  else if (phase == 3) {
    if ((elapsed / 300) % 2 == 0) tone(11, 750); else noTone(11);
    if (elapsed >= 6000) setPhase(0);
  }
}
```

## Build, test and acceptance checks

1. Power over USB and verify only green is initially lit.
2. Press the button: after at least three seconds of green, yellow lasts 2.5s, red clearance 1s and the red walking interval 6s with beeps.
3. Verify green and red never appear together; hold the button and confirm it does not generate endless requests.
4. Repeat a new press during each phase and inspect the behaviour described above.

## Extension

Add explicit pedestrian walk/stop LEDs. A true intersection needs separate road groups and an all-red phase.

## Verification status

The wiring and code have been revised to address the feasibility review. Software checks and their limits are recorded in [VALIDATION.md](../VALIDATION.md). Physical testing of the exact purchased parts is still required before a student session.
