# Project 09: Audio-Visual Morse Code Keyer & Decoder

**Platform:** Arduino Nano or Uno

**Difficulty:** Intermediate

**Estimated session:** 60 minutes

**Group:** 2–3 students; shared inventory rotates between activities.

**Revised:** 14 October 2026

## What students build

A debounced button keys a passive piezo and LED. Short/long presses build a bounded Morse sequence, decoded after 800ms of released silence. The trainer supports letters A–Z and a continuous SOS sequence; it is a timing exercise, not an acoustic decoder.

## Materials and preparation

Use the items in the [revised procurement plan](../School_Electronics_Club_Procurement_Plan_LKR_50000.md). The club needs a computer and the correct USB **data** cable for programming. Disconnect power before changing wiring. These are classroom prototypes; hardware acceptance checks below still need to be performed.

| Item from revised inventory | Quantity needed for this build |
| :-- | :-- |
| Nano and USB-C data cable | 1 |
| breadboard/jumpers | 1 |
| button | 1 |
| red or yellow LED | 1 |
| 1kΩ resistors | 2 |
| passive piezo disc | 1 |


## Complete wiring and power

Buttons connect between their GPIO and GND and use `INPUT_PULLUP`: released is HIGH, pressed is LOW. Use opposite switched terminals, not the two legs already connected internally. No external pull-down resistor is required.

Use a **passive piezo disc**, not the DC continuous alarm: GPIO → 1kΩ resistor → piezo lead; other lead → GND. The resistor limits drive current and the sound may be quiet. Solder flexible leads to the disc with adult supervision; never substitute a magnetic buzzer or speaker without a suitable driver.

Button D2 to GND; LED D13 → 1kΩ → anode, cathode GND; piezo D8 → 1kΩ → disc, other lead GND.

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
Button key;
const char* table[26] = {".-","-...","-.-.","-..",".","..-.","--.","....","..",
".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
char sequence[10] = "";
byte length = 0;
bool wasDown = false, overflow = false;
unsigned long pressAt = 0, releasedAt = 0;
void decode() {
  char letter = '?';
  if (!overflow) {
    for (byte i=0; i<26; i++) if (strcmp(sequence,table[i])==0) letter='A'+i;
    if (strcmp(sequence,"...---...")==0) letter='!';
  }
  Serial.print(sequence); Serial.print(" -> ");
  if (overflow) Serial.println("Too many symbols"); else Serial.println(letter);
  length=0; sequence[0]='\0'; overflow=false;
}
void setup() {
  key.begin(2); pinMode(13,OUTPUT); pinMode(8,OUTPUT); Serial.begin(9600);
  Serial.println("Short <250ms dot; long dash; 800ms silence ends a letter.");
}
void loop() {
  key.update(); bool down=key.down(); unsigned long now=millis();
  if (down && !wasDown) { pressAt=now; tone(8,750); digitalWrite(13,HIGH); }
  if (!down && wasDown) {
    noTone(8); digitalWrite(13,LOW); releasedAt=now;
    unsigned long duration=now-pressAt;
    if (duration>=40) {
      if (length<9) { sequence[length++]=duration<250 ? '.' : '-'; sequence[length]='\0'; }
      else overflow=true;
    }
  }
  wasDown=down;
  if (!down && length>0 && now-releasedAt>=800) decode();
}
```

## Build, test and acceptance checks

1. Upload and open Serial Monitor at 9600. Key E (dot), T (dash), A (dot-dash) and HELLO.
2. Send SOS as three separately paused letters, or nine continuous symbols for the special ! output.
3. Hold the key for a dash and verify switch bounce does not split it. Send more than nine symbols without a letter pause: the buffer must report overflow safely.

## Extension

Implement text-to-Morse using the same passive piezo.

## Verification status

The wiring and code have been revised to address the feasibility review. Software checks and their limits are recorded in [VALIDATION.md](../VALIDATION.md). Physical testing of the exact purchased parts is still required before a student session.
