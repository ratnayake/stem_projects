# Project 08: Two-Player Reaction Speed Tester

**Platform:** Arduino Uno

**Difficulty:** Beginner/intermediate

**Estimated session:** 60–75 minutes

**Group:** 2–3 students; shared inventory rotates between activities.

**Revised:** 14 October 2026

## What students build

Two buttons start a five-light reaction game. Both must be released before the sequence starts. Every countdown stage checks for false starts. Once the LEDs extinguish, millisecond reaction times are recorded; unpressed players time out after three seconds and equal readings are reported as a tie.

## Materials and preparation

Use the items in the [revised procurement plan](../School_Electronics_Club_Procurement_Plan_LKR_50000.md). The club needs a computer and the correct USB **data** cable for programming. Disconnect power before changing wiring. These are classroom prototypes; hardware acceptance checks below still need to be performed.

| Item from revised inventory | Quantity needed for this build |
| :-- | :-- |
| Uno and USB data cable | 1 |
| breadboard/jumpers | 1 |
| red LEDs | 5 |
| 1kΩ resistors | 6 |
| push buttons | 2 |
| passive piezo disc | 1 |


## Complete wiring and power

Buttons connect between their GPIO and GND and use `INPUT_PULLUP`: released is HIGH, pressed is LOW. Use opposite switched terminals, not the two legs already connected internally. No external pull-down resistor is required.

Use a **passive piezo disc**, not the DC continuous alarm: GPIO → 1kΩ resistor → piezo lead; other lead → GND. The resistor limits drive current and the sound may be quiet. Solder flexible leads to the disc with adult supervision; never substitute a magnetic buzzer or speaker without a suitable driver.

| Component | Wiring |
| :-- | :-- |
| Five red LEDs | D3–D7, each via its own 1kΩ to anode; cathodes GND |
| Player 1 button | D2 to GND |
| Player 2 button | D8 to GND |
| Piezo | D9 via 1kΩ; other lead GND |

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
Button p1, p2;
const byte leds[5] = {3,4,5,6,7};
byte state = 0, lit = 0;
unsigned long since = 0, suspense = 0, raceStart = 0;
unsigned long t1 = 0, t2 = 0;
bool got1 = false, got2 = false;
void lightsOff() { for (byte p : leds) digitalWrite(p, LOW); }
void finish() {
  if (got1) { Serial.print("P1: "); Serial.print(t1); Serial.println(" ms"); }
  else Serial.println("P1: timeout");
  if (got2) { Serial.print("P2: "); Serial.print(t2); Serial.println(" ms"); }
  else Serial.println("P2: timeout");
  if (!got1 && !got2) Serial.println("No winner");
  else if (got1 && got2 && t1 == t2) Serial.println("Tie at millisecond resolution");
  else Serial.println(got1 && (!got2 || t1 < t2) ? "P1 wins" : "P2 wins");
  state = 5; since = millis();
}
void setup() {
  Serial.begin(9600); p1.begin(2); p2.begin(8);
  for (byte p : leds) pinMode(p, OUTPUT);
  pinMode(9, OUTPUT); lightsOff();
  randomSeed(analogRead(A0));
  Serial.println("Press either button to start; then release both.");
}
void loop() {
  bool hit1 = p1.update(), hit2 = p2.update();
  unsigned long now = millis();
  if (state == 0 && (hit1 || hit2)) state = 1;
  else if (state == 1 && !p1.down() && !p2.down()) {
    state = 2; lit = 0; since = now;
    Serial.println("\nStarting light sequence...");
  } else if (state == 2 || state == 3) {
    // Raw press stops the sequence too, including a press not yet debounced.
    if (digitalRead(2) == LOW || digitalRead(8) == LOW) {
      Serial.println("False start: race cancelled."); lightsOff(); tone(9,150,400);
      state = 5; since = now; return;
    }
    if (state == 2 && now - since >= 1000) {
      digitalWrite(leds[lit], HIGH); tone(9,440,100); lit++; since = now;
      if (lit == 5) { state = 3; suspense = random(1000,3501); }
    } else if (state == 3 && now - since >= suspense) {
      lightsOff(); raceStart = millis(); got1 = got2 = false;
      tone(9,880,100); state = 4;
    }
  } else if (state == 4) {
    // Times include the 25ms debounce window; use the same filter for both players.
    if (hit1 && !got1) { t1 = now - raceStart; got1 = true; }
    if (hit2 && !got2) { t2 = now - raceStart; got2 = true; }
    if ((got1 && got2) || now - raceStart >= 3000) finish();
  } else if (state == 5 && now - since >= 2000 && !p1.down() && !p2.down()) {
    state = 0; Serial.println("Press either button for another race.");
  }
}
```

## Build, test and acceptance checks

1. Upload and open Serial Monitor at 9600 baud. Press to start and release both buttons.
2. Press during each of the five lights and during suspense: every early attempt must cancel the race.
3. Run with two presses after lights-out, one player absent, and both absent; verify timeout messages and winners.
4. Hold a button at start and at the end: the next race must wait for release. Timing includes filtering and is not a laboratory measurement.

## Extension

Show results on the club LCD; keep the existing false-start and timeout behaviour.

## Verification status

The wiring and code have been revised to address the feasibility review. Software checks and their limits are recorded in [VALIDATION.md](../VALIDATION.md). Physical testing of the exact purchased parts is still required before a student session.
