# School Electronics & Innovation Club: Revised LKR 50,000 Plan

**Revised:** 14 October 2026

**Budget cap:** LKR 50,000 including an allowance for delivery

**Use:** 20 rotating classroom activities for 15–25 students in three teams

**Primary supplier:** Duino.lk; correctly specified estimate-only items may require a second supplier.

## Purchase outcome and price confidence

The revised plan allocates **LKR 46,060 to parts, tools, power and initial consumables**, **LKR 1,500 to delivery**, and **LKR 2,440 to contingency**. All 20 activities are retained with corrected wiring, code and scope. This is a **planning budget, not a supplier quotation or a guarantee of current stock**. Obtain the selected-variant quote and confirm specifications before purchase; use contingency for price changes and delivery, not to silently omit necessary parts.

The core inventory is **two micro:bits, one Uno from the full robot kit and two Nanos**. The extra Uno, O/L starter kit and edge breakout have been removed; their required small parts, storage and connectors are itemized below. Two insulated crocodile-to-male leads provide the micro:bit P0/GND connection. We purchase the full robot kit once and count its included electronics once.

Price basis in each row:

- **S — supplier listing retrieved during this revision.** Listing/variant and stock still need reconfirmation; cached pages are not quotes.
- **P — previous-plan price retained as a provisional allowance.** It has not been independently reverified in this revision.
- **E — estimated procurement allowance.** The exact SKU, availability and price need a quotation. A link, where provided, identifies the intended product, not a verified price.

For a computer-readable copy of every row and reserve, see [procurement-bom.json](procurement-bom.json). Quantity is the purchase quantity; project guides state the quantity used per build.

## Itemized bill of materials

### A. Controllers, kit and programming connections — LKR 21,870

| ID | Item and supplier reference | Qty | Unit allowance (LKR) | Subtotal (LKR) | Basis | Required specification / note |
| :-- | :-- | --: | --: | --: | :--: | :-- |
| A01 | [micro:bit V2 board](https://www.duino.lk/product/microbit-v2-board/) | 2 | 6,250 | 12,500 | S | MB1037-1; board-only |
| A02 | Insulated crocodile-to-male leads for micro:bit P0/GND rings | 2 | 100 | 200 | E | Replaces edge breakout; cover unused 3V ring to prevent accidental 5V contact |
| A03 | [Full obstacle-avoidance robot kit, WITHOUT optional 18650 accessories](https://www.duino.lk/product/duino-obstacle-avoidance-smart-robot-car-kit/) | 1 | 5,990 | 5,990 | S | Duino-Kit-05 base variant; see included-parts list below; confirm four-AA holder |
| A05 | [Classic 5V ATmega328P Nano, USB Type-C](https://www.duino.lk/product/arduino-compatible-nano-v3-0/) | 2 | 990 | 1,980 | S | MB1006-A; confirm fitted headers; USB-C cables separately budgeted |
| A06 | 2×AAA micro:bit holder, correctly polarized PH2.0 connector | 2 | 200 | 400 | E | Order holder-only, not a micro:bit Go bundle |
| A07 | USB-A to micro-USB DATA cable | 2 | 200 | 400 | E | For both micro:bits |
| A08 | USB-A to Type-C DATA cable | 2 | 200 | 400 | E | For both Nanos; Uno cables included above/in kit |

### B. Workshop tools and storage — LKR 8,770

| ID | Item and supplier reference | Qty | Unit allowance (LKR) | Subtotal (LKR) | Basis | Required specification / note |
| :-- | :-- | --: | --: | --: | :--: | :-- |
| B01 | [220–240V adjustable 60W soldering iron 908](https://www.duino.lk/product/908-adjustable-soldering-60w/) | 1 | 1,390 | 1,390 | S | TS0186; stand purchased separately; confirm local voltage/plug |
| B02 | Metal soldering stand with sponge/brass tip cleaner | 1 | 400 | 400 | E | Quote the stated specification. |
| B03 | Manual solder sucker | 1 | 400 | 400 | E | Replaces heated desoldering pump |
| B04 | Electronics rosin-core solder wire, 20g starter spool | 1 | 450 | 450 | E | Quote electronics-grade flux-core alloy and handling requirements; replenish in later terms |
| B05 | [SD-A6 60W glue gun](https://www.duino.lk/product/60w-glue-gun-nozzle-sd-a6/) | 1 | 1,390 | 1,390 | S | TS0169-A; supplier specifies 11mm sticks |
| B06 | Glue sticks matching 11mm ±0.3mm inlet | 10 | 50 | 500 | E | Do not buy the previous 7mm or nominal 10mm refills |
| B07 | [Wire stripper/cutter suitable for 22AWG](https://www.duino.lk/product/wire-stripper-crimper-cutter-pliers/) | 1 | 860 | 860 | P | Quote the stated specification. |
| B08 | [DT-830D multimeter with leads](https://www.duino.lk/product/digital-multimeter-dt-830d/) | 2 | 890 | 1,780 | P | Low-voltage workshop use; confirm batteries included or use power allowance |
| B09 | Eye protection | 2 | 350 | 700 | E | Two students at the supervised soldering bench at a time |
| B10 | Heat-resistant soldering mat | 1 | 300 | 300 | E | Quote the stated specification. |
| B11 | Small screwdriver and craft-hand-tool set | 1 | 300 | 300 | E | School provides scissors/ruler as well |
| B12 | Compartmented parts organizer | 1 | 300 | 300 | E | Separate organizer replaces the starter-kit container |

### C. Wiring, connections and model consumables — LKR 3,880

| ID | Item and supplier reference | Qty | Unit allowance (LKR) | Subtotal (LKR) | Basis | Required specification / note |
| :-- | :-- | --: | --: | --: | :--: | :-- |
| C01 | [830-point full-size breadboard](https://www.duino.lk/product/breadboard-830-tie-point-16-5x5-5x0-85-cm/) | 4 | 265 | 1,060 | P | Quote the stated specification. |
| C02 | [Male–male jumpers, 40-piece pack](https://www.duino.lk/product/jumper-wire-male-to-male-20cm-40pcs/) | 2 | 190 | 380 | P | Quote the stated specification. |
| C03 | [Male–female jumpers, 40-piece pack](https://www.duino.lk/product/jumper-wire-male-to-female-20cm-40pcs/) | 2 | 180 | 360 | P | Quote the stated specification. |
| C04 | [Female–female jumpers, 40-piece pack](https://www.duino.lk/product/jumper-wire-female-to-female-20cm-40pcs/) | 1 | 180 | 180 | P | Quote the stated specification. |
| C05 | Insulated stranded 22AWG hookup wire, red/black plus signal wire lot | 1 | 400 | 400 | E | Motor supply wire and flexible soldered piezo leads; quote sufficient length |
| C06 | Heat-shrink/insulating tape lot | 1 | 300 | 300 | E | Quote the stated specification. |
| C07 | Small insulated alligator/probe leads | 2 | 100 | 200 | E | Consumed by project 20 |
| C08 | Small project enclosure | 1 | 200 | 200 | E | Consumed by project 20; not the shared organizer |
| C09 | 2.1×5.5mm female DC socket to screw terminals | 2 | 100 | 200 | E | Matched to the 5V adapters; verify centre-positive polarity |
| C10 | USB-A 5V/GND power cable/breakout to screw terminals | 1 | 300 | 300 | E | For power bank peripheral rail; no PD voltage trigger |
| C11 | Low-voltage on/off switches | 2 | 50 | 100 | E | One motor switch rated ≥2A DC; one tester switch |
| C12 | Inline 2A fuse, insulated holder and spare fuse | 1 | 200 | 200 | E | For four-AA motor branch |

### D. Sensors, displays and communication — LKR 3,980

| ID | Item and supplier reference | Qty | Unit allowance (LKR) | Subtotal (LKR) | Basis | Required specification / note |
| :-- | :-- | --: | --: | --: | :--: | :-- |
| D01 | [Additional HC-SR04 sonar](https://www.duino.lk/product/ultrasonic-distance-measuring-transducer/) | 2 | 275 | 550 | P | Plus one in robot kit: total three |
| D02 | [Additional SG90 servos with horns/screws](https://www.duino.lk/product/servo-motor-sg90-9g/) | 2 | 350 | 700 | P | Plus one in robot kit: total three; ordinary positional type |
| D03 | [16×2 blue-backlight LCD](https://www.duino.lk/product/lcd-16x02-display-blue/) | 1 | 380 | 380 | P | Quote the stated specification. |
| D04 | [PCF8574-compatible I2C LCD backpack with 16-pin header](https://www.duino.lk/product/iici2c-twi-spi-serial-interface-module-for-1602-1604-2004lcd/) | 1 | 210 | 210 | P | Solder assembly required; hd44780 library |
| D05 | [DHT11 module](https://www.duino.lk/product/dht11-temperature-and-humidity-sensor-module/) | 1 | 230 | 230 | P | Verify pin order/data pull-up |
| D06 | [Bare GL12528 12mm LDR](https://www.duino.lk/product/gl12528-12mm-light-sensitive-resistor-ldr/) | 2 | 110 | 220 | S | SEN1524-1; replaces ambiguous digital sensor modules |
| D07 | [5V relay MODULE with onboard driver and known trigger polarity](https://www.duino.lk/product/relay-board-module-5v-1-channel/) | 1 | 220 | 220 | P | Only low-voltage demonstration loads |
| D08 | [Bare passive 35mm piezo disc](https://www.duino.lk/product/piezo-ceramic-copper-buzzer-35mm/) | 2 | 200 | 400 | E | Product identity found, live price unavailable; no oscillator; reusable tone/knock parts |
| D09 | [Active continuous-sound DC 3–24V alarm buzzer](https://www.duino.lk/product/dc-3-24v-electronic-buzzer/) | 1 | 290 | 290 | S | Only project 20; not direct Arduino GPIO or knock sensor |
| D10 | [HC-06 carrier, Bluetooth Classic SPP, 5V VCC regulator](https://www.duino.lk/product/hc-06-bluetooth-rf-transceiver-module-slave/) | 1 | 780 | 780 | P | RX logic needs resistor divider |

### E. LEDs, passives and buttons — LKR 1,530

| ID | Item and supplier reference | Qty | Unit allowance (LKR) | Subtotal (LKR) | Basis | Required specification / note |
| :-- | :-- | --: | --: | --: | :--: | :-- |
| E01 | Red through-hole LEDs (3mm or 5mm) | 10 | 35 | 350 | E | Explicit colour/quantity; not an unverified assortment link |
| E02 | Yellow through-hole LEDs (3mm or 5mm) | 4 | 35 | 140 | E | Quote the stated specification. |
| E03 | Green through-hole LEDs (3mm or 5mm) | 6 | 35 | 210 | E | Quote the stated specification. |
| E04 | 1kΩ 1/4W through-hole resistors | 30 | 5 | 150 | E | LED current limiting, piezo drive, HC-06 divider and project 20 |
| E05 | 10kΩ 1/4W through-hole resistors | 10 | 5 | 50 | E | LDR dividers, DHT pull-up and knock series protection |
| E06 | 1MΩ 1/4W through-hole resistor | 2 | 10 | 20 | E | Piezo bleed resistor; one spare |
| E07 | BAT85 through-hole Schottky diode | 4 | 30 | 120 | E | Two knock-input clamps plus spares; verify part/polarity |
| E08 | 470µF electrolytic capacitor, ≥10V | 3 | 50 | 150 | E | Servo supply reservoir; observe polarity |
| E09 | 100nF ceramic capacitor | 4 | 10 | 40 | E | Motor suppression; two plus spares |
| E10 | [Breadboard-compatible momentary push button](https://www.duino.lk/product/tactile-push-button-switch-4pins-12x12x7-3mm/) | 10 | 30 | 300 | P | Use opposite switched legs; check physical fit |

### F. Power supplies and initial batteries — LKR 6,030

| ID | Item and supplier reference | Qty | Unit allowance (LKR) | Subtotal (LKR) | Basis | Required specification / note |
| :-- | :-- | --: | --: | --: | :--: | :-- |
| F01 | [Regulated 5V/2A enclosed adapter, UK 3-pin, centre-positive 2.1×5.5mm](https://www.duino.lk/product/5v-2a-3pin-ac-dc-smps-power-adaptor/) | 2 | 690 | 1,380 | S | PS3539-A; powers peripheral rails, not Uno Vin/barrel |
| F02 | Enclosed USB power bank with two fixed-5V outputs, ≥2A total rating | 1 | 2,500 | 2,500 | E | Quote reputable bank/idle behaviour; USB chargers and cable for charging included in this allowance |
| F03 | AAA alkaline cells | 4 | 100 | 400 | E | Two per micro:bit; initial set |
| F04 | AA alkaline cells | 8 | 100 | 800 | E | Four for robot motor pack, four spares; not rechargeable in this plan |
| F05 | 9V alkaline PP3 batteries | 3 | 300 | 900 | E | One tester battery and two multimeter batteries if needed; not motor power |
| F06 | [9V snap clips](https://www.duino.lk/product/9v-battery-snap-on-connector-clip/) | 2 | 25 | 50 | P | Tester clip plus spare; not board power |

## Budget balance

| Allocation | LKR |
| :-- | --: |
| A. Controllers, kit and programming connections | 21,870 |
| B. Workshop tools and storage | 8,770 |
| C. Wiring, connections and model consumables | 3,880 |
| D. Sensors, displays and communication | 3,980 |
| E. LEDs, passives and buttons | 1,530 |
| F. Power supplies and initial batteries | 6,030 |
| Hardware, tools and initial consumables — 57 purchase rows | **46,060** |
| Delivery allowance — quote needed for all suppliers combined | **1,500** |
| Contingency — unspent until required | **2,440** |
| Total allocation | **50,000** |

The old plan's category totals were inconsistent with its rows. These totals are calculated from the revised rows. This is an initial procurement budget: AA/AAA replacement cells, solder replenishment and future additions need later funding.

## Robot kit contents: included once

A03 is the **base full robot kit without optional 18650 batteries/charger**. The retrieved listing prices its variants at LKR 5,990–7,890. The base list includes chassis/hardware, two 3–6V geared motors, two wheels, caster, encoder discs, AA battery box, one L298N, one HC-SR04 and bracket, one SG90, one Uno and its cable, one 400-point breadboard, 20 male–male and 10 male–female jumpers. Do not additionally buy these included electronics. Confirm the exact base variant and a **four-cell AA holder** in the quotation; ask for a suitable four-AA holder within contingency if the delivered box differs. [Full robot-kit listing](https://www.duino.lk/product/duino-obstacle-avoidance-smart-robot-car-kit/).

Inventory after the planned order:

| Resource | Available total | Sharing constraint |
| :-- | :-- | :-- |
| micro:bit V2 | 2 | Project 01 uses both |
| Uno / classic Nanos | 1 / 2 | Three Arduino builds possible; Uno-labelled activities rotate on the single Uno |
| Motors/chassis and L298N | One pair/chassis and one driver | Projects 16–18 share the same car |
| HC-SR04 | 3 | Project 14 uses two; project 17 uses one |
| SG90 | 3 | One from kit plus two additional; models rotate |
| LCD and backpack / DHT11 | 1 pair / 1 | Projects 11 and 12 share the LCD |
| Bare LDRs | 2 | Project 19 uses both; project 07 must wait |
| Passive piezos / active alarm | 2 / 1 | Passive discs rotate; active alarm is reserved for project 20 |
| Full breadboards / kit breadboard | 4 / 1 | No mini boards assumed necessary |
| Bench peripheral 5V supplies | 2 adapters | One servo per adapter for the baseline model builds |
| Mobile electronics supply / motor supply | 1 USB bank / 1 four-AA holder | Shared rover; batteries explicitly budgeted |

Project 20 permanently consumes one green LED, one 1kΩ resistor, one active alarm, one snap, its probe leads/switch/enclosure and some wire/solder. The remaining inventory supports the other lessons. No other electronics are permanently committed in the baseline plan.

## Wiring and purchase decisions that apply across guides

- **Servo power:** board USB supply plus a separate regulated 5V peripheral supply, common ground, and a reservoir capacitor. Do not join separate +5V regulator outputs. micro:bit receives no external 5V at its edge rings. [Official micro:bit servo guidance](https://support.microbit.org/support/solutions/articles/19000101864-using-a-servo-with-the-micro-bit).
- **Mobile robot power:** four alkaline AA cells supply only L298N motor Vs. The enclosed fixed-5V USB bank powers Uno through USB and separately supplies L298N logic/servo. Remove L298N ENA/ENB jumpers and its regulator-enable jumper before supplying external 5V logic. Never supply Uno Vin from a four-AA pack or use a PP3 9V battery for drive motors. [Arduino power guidance](https://support.arduino.cc/hc/en-us/articles/360018922259-What-power-supply-can-I-use-with-my-Arduino-board).
- **LDR sensing:** bare GL12528 components plus individual 10kΩ dividers give an unambiguous analog signal. Do not substitute the old digital-only comparator module. [Bare LDR listing](https://www.duino.lk/product/gl12528-12mm-light-sensitive-resistor-ldr/).
- **Audio versus knock sensing:** passive discs handle `tone()` and the protected knock input. The active continuous alarm belongs only in the standalone 9V continuity indicator. Keep its draw off Arduino GPIO. [Passive-disc identity](https://www.duino.lk/product/piezo-ceramic-copper-buzzer-35mm/), [active-alarm listing](https://www.duino.lk/product/dc-3-24v-electronic-buzzer/).
- **Passives and colours:** specify through-hole resistor values individually, plus red/yellow/green LEDs individually. Do not reuse the old SMD resistor or red-only LED assortment links.
- **Glue fit:** the SD-A6 supplier description specifies 11mm sticks (±0.3mm). Refills are quoted by that diameter; nozzle aperture is not glue-stick diameter. [Glue-gun specification](https://www.duino.lk/product/60w-glue-gun-nozzle-sd-a6/).
- **LCD software:** guides 11/12 use `hd44780` by Bill Perry (`hd44780_I2Cexp`) with its diagnosis example and automatic compatible-backpack detection. The DHT guide specifies Adafruit DHT and Unified Sensor libraries. See [VALIDATION.md](VALIDATION.md) for checked versions and limits.

The two adapter listings specify 5V/2A and a centre-positive 2.1×5.5mm connector; C09 sockets must match. [Adapter listing](https://www.duino.lk/product/5v-2a-3pin-ac-dc-smps-power-adaptor/). Power supplies stay enclosed; students only work on their low-voltage outputs.

## Catalog of revised activities

| # | Guide | Platform | Difficulty |
| :-- | :-- | :-- | :-- |
| 01 | [Two-Way Pocket Radio Messenger](projects/project-01-microbit-radio-chat.md) | micro:bit V2 | Beginner |
| 02 | [Digital Compass & Experimental Step Counter](projects/project-02-microbit-digital-compass-step-counter.md) | micro:bit V2 | Beginner/intermediate |
| 03 | [Classroom Relative Noise Monitor](projects/project-03-microbit-sound-level-meter-noise-cop.md) | micro:bit V2 | Beginner |
| 04 | [Tilt-Controlled Grid Maze with Audio](projects/project-04-microbit-tilt-maze-game.md) | micro:bit V2 | Intermediate |
| 05 | [Servo Dial for Approximate Board Temperature](projects/project-05-microbit-servo-robotic-gauge.md) | micro:bit V2 + SG90 | Intermediate |
| 06 | [Single Traffic Signal with Pedestrian Request](projects/project-06-traffic-light-controller.md) | Arduino Nano or Uno | Beginner |
| 07 | [Automatic Dusk-to-Dawn Model Lamp](projects/project-07-smart-street-light-ldr.md) | Arduino Uno | Beginner |
| 08 | [Two-Player Reaction Speed Tester](projects/project-08-digital-stopwatch-reaction-timer.md) | Arduino Uno | Beginner/intermediate |
| 09 | [Audio-Visual Morse Code Keyer & Decoder](projects/project-09-morse-code-trainer.md) | Arduino Nano or Uno | Intermediate |
| 10 | [Ultrasonic Change-Detection Alarm](projects/project-10-intruder-security-alarm.md) | Arduino Nano or Uno | Intermediate |
| 11 | [Indoor Weather Station with I2C LCD](projects/project-11-indoor-weather-station-lcd.md) | Arduino Uno | Intermediate |
| 12 | [Ultrasonic Distance Meter with LCD](projects/project-12-ultrasonic-digital-measuring-tape.md) | Arduino Uno | Intermediate |
| 13 | [Touchless Cardboard Dustbin Model](projects/project-13-touchless-smart-dustbin.md) | Arduino Nano or Uno | Intermediate |
| 14 | [Two-Sensor Model Parking Barrier](projects/project-14-automatic-parking-barrier-gate.md) | Arduino Uno | Intermediate |
| 15 | [Secret Knock Detector with Model Servo Latch](projects/project-15-secret-knock-detector.md) | Arduino Uno | Advanced |
| 16 | [Dual Motor Speed & Direction Controller](projects/project-16-dual-motor-speed-controller.md) | Arduino Uno | Intermediate |
| 17 | [Obstacle-Avoiding Classroom Rover](projects/project-17-autonomous-obstacle-avoiding-rover.md) | Arduino Uno | Advanced |
| 18 | [Bluetooth Smartphone RC Car with Command Timeout](projects/project-18-bluetooth-smartphone-rc-car.md) | Arduino Uno | Advanced |
| 19 | [Dual-LDR Light-Following Tracker Model](projects/project-19-dual-ldr-solar-tracker.md) | Arduino Nano or Uno | Intermediate/advanced |
| 20 | [Soldering Workshop: LED & Buzzer Cable Tester](projects/project-20-workshop-continuity-tester-soldering-bench.md) | Low-voltage workshop circuit | Intermediate |

## Three-team sessions and resources supplied by the school

Treat the catalog as **20 sequential activities with reused parts**, not 20 simultaneous finished devices. Start with micro:bit 01/03/04, then LED/button activities, displays, servo models, motor bench tests and rover integration. Test each new subsystem separately before combining it.

An example concurrent session is team 1 on project 01 (both micro:bits), team 2 on project 06 or 09 (one Nano), and team 3 on project 16 (kit Uno and motors). A later session can pair micro:bit 04 with the Uno weather station and a Nano light tracker. Stagger soldering work because the iron/stand and two goggles are shared.

The school must supply at least three suitable computers for concurrent programming, permitted software/Internet access, safe wall sockets, a supervised ventilated workspace, scissors/rulers, reusable cardboard/straps and a compatible Android Bluetooth Classic/SPP phone for project 18. These existing facilities are **not bought by the LKR 50,000 plan**. Power-bank charging equipment is included in its estimated allowance and must be itemized in its quote. No solar panel, real door lock, fan, water pump or mains load is required by the baseline projects.

## Ordering and acceptance

1. Request a line-by-line quotation with the quantities, exact variants and specifications above. Reconfirm every S/P price; obtain exact prices for E rows, including shipping from any second supplier. Do not use the previous ambiguous SKU links.
2. Confirm the robot kit's contents, USB data cables, fitted Nano headers, passive piezo identity, BAT85 parts, capacitor ratings, adapter connector/polarity and fixed-5V bank outputs. Keep omitted optional robot battery accessories out of the order.
3. Sum the actual delivered quote. Parts plus all shipping must remain at or below LKR 50,000; contingency can absorb at most LKR 2,440 beyond the stated parts and shipping allowances. If the quote exceeds that, revise quantities or seek equivalent correctly specified parts before purchase. Do not remove input protection or required power supplies to balance the budget.
4. Inspect deliveries, measure low-voltage rails and test sensors/motors before using the guides. Never modify an enclosed mains adapter. Soldering/glue work needs adult supervision, eye protection and ventilation. Relay and continuity activities remain on disconnected low-voltage circuits as specified.
5. Run each guide's physical acceptance checks. Software validation does not establish the exact supplier parts will operate reliably together.

The [original feasibility review](PROJECT_FEASIBILITY_REVIEW.md) is retained as a historical audit of the previous documents; its quoted old quantities and prices are not the revised shopping list.
