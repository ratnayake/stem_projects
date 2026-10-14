# Project 07: Automatic Dusk-to-Dawn Model Lamp

**Platform:** Arduino Uno

**Difficulty:** Beginner

**Estimated session:** 60 minutes

**Group:** 2–3 students; shared inventory rotates between activities.

**Revised:** 14 October 2026

## What students build

A bare LDR and 10kΩ resistor form an analog voltage divider. Dark readings are lower for the specified wiring. Hysteresis switches a low-voltage LED lamp through a relay and avoids rapid switching near dusk.

## Materials and preparation

Use the items in the [revised procurement plan](../School_Electronics_Club_Procurement_Plan_LKR_50000.md). The club needs a computer and the correct USB **data** cable for programming. Disconnect power before changing wiring. These are classroom prototypes; hardware acceptance checks below still need to be performed.

| Item from revised inventory | Quantity needed for this build |
| :-- | :-- |
| Uno and USB data cable | 1 |
| bare GL12528 LDR | 1 |
| 10kΩ resistor | 1 |
| 1kΩ resistor | 1 |
| yellow LED | 1 |
| 5V relay module with onboard driver | 1 |
| breadboard and jumpers | 1 |


## Complete wiring and power

Power Uno via USB. Use the module's onboard driver, not a bare relay coil. This demonstration switches only the listed 5V LED; do not connect mains loads. Check the supplied relay's active-low/active-high input before attaching the LED load. An optocoupler does not automatically isolate supplies when grounds are shared.

| Connection | Destination |
| :-- | :-- |
| LDR leg 1 | Uno 5V |
| LDR leg 2 | A0 and one end of 10kΩ |
| Other end of 10kΩ | GND |
| Relay VCC/GND/IN | 5V/GND/D7 |
| Relay COM | Uno 5V |
| Relay NO | 1kΩ → yellow LED anode |
| Yellow LED cathode | GND |
| Relay NC | Unconnected |

If the relay module requires a separate supply, use one listed adapter and a common ground without joining the two +5V rails; confirm the module's trigger compatibility.

## Complete source code

Paste this entire sketch into Arduino IDE. Select **Arduino Uno** for the Uno or **Arduino Nano / ATmega328P** for a classic Nano; some CH340 Nano clones require the old bootloader setting. Use Arduino AVR Boards 1.8.6. SoftwareSerial is included in that core; install any additional libraries specified for this project below.

```cpp
#include <Arduino.h>
const byte RELAY = 7;
const bool ACTIVE_LOW = true; // Confirm on the supplied module.
const int DARK_THRESHOLD = 350, LIGHT_THRESHOLD = 500;
bool on = false;
void setLamp(bool value) {
  on = value;
  digitalWrite(RELAY, ACTIVE_LOW ? (on ? LOW : HIGH) : (on ? HIGH : LOW));
}
void setup() {
  digitalWrite(RELAY, ACTIVE_LOW ? HIGH : LOW); // Set OFF before enabling output.
  pinMode(RELAY, OUTPUT); setLamp(false);
  Serial.begin(9600);
}
void loop() {
  int light = analogRead(A0);
  Serial.println(light);
  if (!on && light < DARK_THRESHOLD) setLamp(true);
  else if (on && light > LIGHT_THRESHOLD) setLamp(false);
  delay(200);
}
```

## Build, test and acceptance checks

1. With the LED load disconnected, check which output level releases the relay and set ACTIVE_LOW accordingly.
2. Print A0 in bright light and with the LDR covered; dark should read lower. Set thresholds between those readings with a useful deadband.
3. Connect the model LED; covering the LDR should light it, uncovering should turn it off.
4. Slowly change the light near the thresholds and confirm no relay chatter.

## Extension

Log time spent on. For LED dimming, use a suitable transistor/MOSFET circuit with PWM; a mechanical relay cannot provide brightness control.

## Verification status

The wiring and code have been revised to address the feasibility review. Software checks and their limits are recorded in [VALIDATION.md](../VALIDATION.md). Physical testing of the exact purchased parts is still required before a student session.
