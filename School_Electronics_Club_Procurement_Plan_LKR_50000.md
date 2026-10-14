# School Electronics & Innovation Club: Revised LKR 50,000 Plan

**Revised:** 14 October 2026

**Budget cap:** LKR 50,000 including an allowance for delivery

**Use:** 20 rotating classroom activities for 15–25 students in three teams

**Primary supplier:** Duino.lk; correctly specified estimate-only items may require a second supplier.

## Purchase outcome and price confidence

The revised plan allocates **LKR 46,060 to parts, tools, power and initial consumables**, **LKR 1,500 to delivery**, and **LKR 2,440 to contingency**. All 20 activities are retained with corrected wiring, code and scope. **Added purchase links expose prices above several allowances; the linked retail basket has not been repriced and is not confirmed within this budget.** This is a **planning budget, not a supplier quotation or a guarantee of current stock**. Obtain the selected-variant quote and confirm specifications before purchase; use contingency for price changes and delivery, not to silently omit necessary parts.

The core inventory is **two micro:bits, one Uno from the full robot kit and two Nanos**. The extra Uno, O/L starter kit and edge breakout have been removed; their required small parts, storage and connectors are itemized below. Two insulated crocodile-to-male leads provide the micro:bit P0/GND connection. We purchase the full robot kit once and count its included electronics once.

Price basis in each row:

- **S — supplier listing retrieved during this revision.** Listing/variant and stock still need reconfirmation; cached pages are not quotes.
- **P — previous-plan price retained as a provisional allowance.** It has not been independently reverified in this revision.
- **E — estimated procurement allowance.** The exact SKU, availability and price need a quotation. A link, where provided, identifies the intended product, not a verified price.

For a computer-readable copy of every row and reserve, see [procurement-bom.json](procurement-bom.json). Quantity is the planned number of individual parts or component lots. Follow each row's pack/assembly notes for the quantity to add to a supplier cart; project guides state the quantity used per build.

## Itemized bill of materials

### A. Controllers, kit and programming connections — LKR 21,870

| ID | Item and supplier reference | Qty | Unit allowance (LKR) | Subtotal (LKR) | Basis | Required specification / note |
| :-- | :-- | --: | --: | --: | :--: | :-- |
| A01 | [micro:bit V2 board](https://www.duino.lk/product/microbit-v2-board/) | 2 | 6,250 | 12,500 | S | MB1037-1; board-only |
| A02 | [Insulated crocodile-to-male leads for micro:bit P0/GND rings](https://tronic.lk/product/crocodile-clip-small-2pcs-red-and-black) — assemble from components | 2 | 100 | 200 | E | Replaces edge breakout; cover unused 3V ring to prevent accidental 5V contact TA0033 is a two-clip pack, not finished male-ended leads: buy one pack and solder two existing male jumper wires to the clips; insulate joints and check continuity. |
| A03 | [Full obstacle-avoidance robot kit, WITHOUT optional 18650 accessories](https://www.duino.lk/product/duino-obstacle-avoidance-smart-robot-car-kit/) | 1 | 5,990 | 5,990 | S | Duino-Kit-05 base variant; see included-parts list below; confirm four-AA holder |
| A05 | [Classic 5V ATmega328P Nano, USB Type-C](https://www.duino.lk/product/arduino-compatible-nano-v3-0/) | 2 | 990 | 1,980 | S | MB1006-A; confirm fitted headers; USB-C cables separately budgeted |
| A06 | [2×AAA micro:bit holder, correctly polarized PH2.0 connector](https://tronic.lk/product/battery-holder-case-2xaaa-3v-ph2-0-for-microbit-microbi) | 2 | 200 | 400 | E | Order holder-only, not a micro:bit Go bundle Tronic BA0216: holder-only, PH2.0, listed LKR 160 each; confirm polarity. |
| A07 | [USB-A to micro-USB DATA cable](https://tronic.lk/product/usb-to-microusb-data-cable-30cm) | 2 | 200 | 400 | E | For both micro:bits Tronic TA1422: USB data cable, listed LKR 100 each. |
| A08 | [USB-A to Type-C DATA cable](https://tronic.lk/product/celebrat-cb-24-usb-data-cable-usb-a-to-type-c-fast-char) | 2 | 200 | 400 | E | For both Nanos; Uno cables included above/in kit Tronic TA1678 explicitly supports data; listed LKR 700 each, above the LKR 200 allowance. |

### B. Workshop tools and storage — LKR 8,770

| ID | Item and supplier reference | Qty | Unit allowance (LKR) | Subtotal (LKR) | Basis | Required specification / note |
| :-- | :-- | --: | --: | --: | :--: | :-- |
| B01 | [220–240V adjustable 60W soldering iron 908](https://www.duino.lk/product/908-adjustable-soldering-60w/) | 1 | 1,390 | 1,390 | S | TS0186; stand purchased separately; confirm local voltage/plug |
| B02 | [Metal soldering stand with sponge/brass tip cleaner](https://tronic.lk/product/soldering-iron-stand-square) + [Sponge/cleaner category — request ACS4352-A](https://www.duino.lk/product-category/related-accessories/soldering-accessories/) — assemble from components | 1 | 400 | 400 | E | Tronic TA0048 stand, listed LKR 300; confirm cleaning sponge included, otherwise add a cleaner from the linked supplier category (request ACS4352-A) within a revised quote. |
| B03 | [Manual solder sucker](https://tronic.lk/product/l138-desoldering-pump-sucker) | 1 | 400 | 400 | E | Replaces heated desoldering pump Tronic TA0039 manual pump, listed LKR 200. |
| B04 | [Electronics rosin-core solder wire, 20g starter spool](https://transasia.lk/product/relife-rl-440-0-3mm-soldering-wire-alloy-20-80-20g/) | 1 | 450 | 450 | E | Quote electronics-grade flux-core alloy and handling requirements; replenish in later terms Trans Asia RL-440: 20g, listed LKR 375; verify rosin/flux core and alloy suitability. A higher-tin electronics solder is preferable if quoted within budget. |
| B05 | [SD-A6 60W glue gun](https://www.duino.lk/product/60w-glue-gun-nozzle-sd-a6/) | 1 | 1,390 | 1,390 | S | TS0169-A; supplier specifies 11mm sticks |
| B06 | [Glue sticks matching 11mm ±0.3mm inlet](https://alphatronic.lk/product/glue-stick-11mm/) | 10 | 50 | 500 | E | Do not buy the previous 7mm or nominal 10mm refills Alphatronic 11mm sticks, listed LKR 60 each, above the LKR 50 allowance; buy 10 and verify diameter tolerance with the gun. |
| B07 | [Wire stripper/cutter suitable for 22AWG](https://www.duino.lk/product/wire-stripper-crimper-cutter-pliers/) | 1 | 860 | 860 | P | Quote the stated specification. |
| B08 | [DT-830D multimeter with leads](https://www.duino.lk/product/digital-multimeter-dt-830d/) | 2 | 890 | 1,780 | P | Low-voltage workshop use; confirm batteries included or use power allowance |
| B09 | [Eye protection](https://elecshop.lk/product/ingco-safety-goggles-hsg02-in-sri-lanka-lowest-price/) | 2 | 350 | 700 | E | Two students at the supervised soldering bench at a time Elecshop Ingco HSG02 goggles, listed LKR 650 each, above the LKR 350 allowance; check student fit. |
| B10 | [Heat-resistant soldering mat](https://tronic.lk/product/solder-mat-heat-resistant-repair-station-28x20x0-5cm) | 1 | 300 | 300 | E | Tronic TA0328 soldering mat, listed LKR 1,100, above the LKR 300 allowance; not a thin heatsink thermal pad. |
| B11 | [Small screwdriver and craft-hand-tool set](https://tronic.lk/product/precision-screwdriver-tool-set-32-in-1-6011-a) | 1 | 300 | 300 | E | School provides scissors/ruler as well Tronic TA1255 precision screwdriver set, listed LKR 350, above the LKR 300 allowance; school supplies scissors and ruler. |
| B12 | [Compartmented parts organizer](https://tronic.lk/product/component-box-6-way) | 1 | 300 | 300 | E | Separate organizer replaces the starter-kit container Tronic EN0013 six-compartment box, listed LKR 300; use labelled small bags to separate additional resistor values. |

### C. Wiring, connections and model consumables — LKR 3,880

| ID | Item and supplier reference | Qty | Unit allowance (LKR) | Subtotal (LKR) | Basis | Required specification / note |
| :-- | :-- | --: | --: | --: | :--: | :-- |
| C01 | [830-point full-size breadboard](https://www.duino.lk/product/breadboard-830-tie-point-16-5x5-5x0-85-cm/) | 4 | 265 | 1,060 | P | Quote the stated specification. |
| C02 | [Male–male jumpers, 40-piece pack](https://www.duino.lk/product/jumper-wire-male-to-male-20cm-40pcs/) | 2 | 190 | 380 | P | Quote the stated specification. |
| C03 | [Male–female jumpers, 40-piece pack](https://www.duino.lk/product/jumper-wire-male-to-female-20cm-40pcs/) | 2 | 180 | 360 | P | Quote the stated specification. |
| C04 | [Female–female jumpers, 40-piece pack](https://www.duino.lk/product/jumper-wire-female-to-female-20cm-40pcs/) | 1 | 180 | 180 | P | Quote the stated specification. |
| C05 | [Insulated stranded 22AWG hookup wire, red/black plus signal wire lot](https://www.daraz.lk/products/10-colors-16-18-20-22-24-26-28-30-gauge-silicone-electrical-wire-10-ft-each-color-22-awg-stranded-tinned-copper-hookup-wire-kit-i616561192.html) — marketplace; verify seller/delivery | 1 | 400 | 400 | E | Motor supply wire and flexible soldered piezo leads; quote sufficient length Daraz.lk wire-kit listing: select 22AWG STRANDED copper and sufficient red/black length. Confirm seller location, delivery, variant and price; imported packs may exceed the allowance. Ask a local electronics supplier for a cut-length quote as an alternative. |
| C06 | [Heat-shrink/insulating tape lot](https://www.duino.lk/product/heat-shrink-sleeve-heat-shrink-tube/) | 1 | 300 | 300 | E | Duino heat-shrink tubing is sold by length and diameter; select sizes that fit the joints and insulation. The allowance is for a small mixed-size lot, not one unspecified tube. |
| C07 | [Small insulated alligator/probe leads](https://tronic.lk/product/crocodile-clip-small-2pcs-red-and-black) — assemble from components | 2 | 100 | 200 | E | Consumed by project 20 Tronic TA0033 is one red/black clip PAIR, listed LKR 30 per pack; make two probe leads using C05 wire, insulate and add strain relief. This is a separate pair from A02. |
| C08 | [Small project enclosure](https://www.duino.lk/product/158x900x47mm-plastic-abs-project-box-enclosure/) | 1 | 200 | 200 | E | Consumed by project 20; not the shared organizer Duino ACS4146: 158×90×47mm ABS box; listed LKR 890, above the LKR 200 allowance. Confirm space for the 9V battery, alarm and switch before drilling. |
| C09 | [2.1×5.5mm female DC socket to screw terminals](https://tronic.lk/product/dc-jack-barrel-connector-female-power-terminal-5-5x2-1m) | 2 | 100 | 200 | E | Matched to the 5V adapters; verify centre-positive polarity Tronic CN0034 female 5.5×2.1mm screw-terminal socket, listed LKR 30 each; verify centre-positive polarity. |
| C10 | [USB-A 5V/GND power cable/breakout to screw terminals](https://www.duino.lk/product/usb-to-dc-5-5mm-cable-usb-2-0-a/) + [Additional CN0034 socket](https://tronic.lk/product/dc-jack-barrel-connector-female-power-terminal-5-5x2-1m) — assemble from components | 1 | 300 | 300 | E | For power bank peripheral rail; no PD voltage trigger Use Duino CW0764 USB-A to 5.5×2.1mm 5V cable (listed LKR 240) PLUS one additional CN0034 screw-terminal socket (listed LKR 30): about LKR 270 before shipping. This third socket belongs to this assembly; do not subtract it from the two C09 sockets. Confirm cable current rating for servo peaks; no 9V/12V boost converter. |
| C11 | [Low-voltage on/off switches](https://www.duino.lk/product/on-off-2pin-g130-boat-rocker-switch/) | 2 | 50 | 100 | E | One motor switch rated ≥2A DC; one tester switch Duino two-terminal ON/OFF switch is listed LKR 40; confirm at least 2A DC rating for the motor branch. The advertised AC rating alone does not establish its DC rating. |
| C12 | [Inline 2A fuse, insulated holder and spare fuse](https://www.daraz.lk/products/globaltrendz5-pcs-screw-type-20-awg-wire-5-x-20mm-inline-fuse-holder-home-protection-inline-fuse-holder-copper-wire-components-5a-220v-520-i551090595.html) + [2A 5×20mm fuse pack (select 2A)](https://www.duino.lk/product/2a-250vac-glass-fuse-5x20mm-10pcs/) — marketplace assembly; verify seller/delivery | 1 | 200 | 200 | E | For four-AA motor branch Daraz.lk 5×20mm inline-holder listing is a five-pack: confirm delivery/origin and price. Fit a separately linked 2A 5×20mm fuse, NOT a supplied 5A fuse. Buy one matching 2A fuse pack for the installed fuse and spare; combined purchase may exceed the LKR 200 allowance. |

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
| E01 | [Red through-hole LEDs (3mm or 5mm)](https://tronic.lk/product/led-5mm-red-clear-pack-approx-10pcs) | 10 | 35 | 350 | E | Explicit colour/quantity; not an unverified assortment link Tronic LQ0007: buy ONE approximately 10-LED red clear pack, not 10 packs; listed LKR 50 per pack. Confirm actual count. |
| E02 | [Yellow through-hole LEDs (3mm or 5mm)](https://tronic.lk/product/led-5mm-yellow-diffused-pack-approx-10pcs) | 4 | 35 | 140 | E | Tronic LQ0004: buy ONE approximately 10-LED yellow pack for the four required LEDs; listed LKR 50 per pack. |
| E03 | [Green through-hole LEDs (3mm or 5mm)](https://tronic.lk/product/led-5mm-green-diffused-pack-approx-10pcs) | 6 | 35 | 210 | E | Tronic LQ0002: buy ONE approximately 10-LED green pack for the six required LEDs; listed LKR 50 per pack. |
| E04 | [1kΩ 1/4W through-hole resistors](https://tronic.lk/product/1k-14w-resistor-pack-carbon-film-tht-5-approx-40pcs) | 30 | 5 | 150 | E | LED current limiting, piezo drive, HC-06 divider and project 20 Tronic RP0035: buy ONE approximately 40-resistor pack for the 30 required parts; listed LKR 50 per pack; through-hole 1/4W. |
| E05 | [10kΩ 1/4W through-hole resistors](https://tronic.lk/product/10k-14w-resistor-pack-carbon-film-tht-5-approx-40pcs) | 10 | 5 | 50 | E | LDR dividers, DHT pull-up and knock series protection Tronic RP0047: buy ONE approximately 40-resistor pack for the 10 required parts; listed LKR 50 per pack; through-hole 1/4W. |
| E06 | [1MΩ 1/4W through-hole resistor](https://tronic.lk/product/1m-14w-resistor-pack-carbon-film-tht-5-approx-40pcs) | 2 | 10 | 20 | E | Piezo bleed resistor; one spare Tronic RP0071: buy ONE approximately 40-resistor pack for the two required parts; listed LKR 50 per pack, above this row's LKR 20 allowance; fixed resistor, not a preset. |
| E07 | [BAT85 through-hole Schottky diode](https://www.daraz.lk/products/50pcs-bat85-do35-schottky-diode-i189031201.html) — marketplace; verify seller/delivery | 4 | 30 | 120 | E | Two knock-input clamps plus spares; verify part/polarity Daraz.lk BAT85 DO-35 listing is a 50-pack for four required diodes. Search listing found; checkout page/price/stock could not be verified. Confirm seller, lead time and exact BAT85 part before ordering; request a local small-quantity quote as an alternative. |
| E08 | [470µF electrolytic capacitor, ≥10V](https://tronic.lk/product/original-samwha-470uf-16v-electrolytic-capacitor-tht) | 3 | 50 | 150 | E | Servo supply reservoir; observe polarity Tronic CA0223: 470µF 16V through-hole capacitor, listed LKR 30 each; buy three and observe polarity. |
| E09 | [100nF ceramic capacitor](https://tronic.lk/product/100nf-50v-ceramic-capacitor-tht) | 4 | 10 | 40 | E | Motor suppression; two plus spares Tronic CA0002: 100nF 50V through-hole ceramic capacitor, listed LKR 2 each; buy four, not an SMD capacitor. |
| E10 | [Breadboard-compatible momentary push button](https://www.duino.lk/product/tactile-push-button-switch-4pins-12x12x7-3mm/) | 10 | 30 | 300 | P | Use opposite switched legs; check physical fit |

### F. Power supplies and initial batteries — LKR 6,030

| ID | Item and supplier reference | Qty | Unit allowance (LKR) | Subtotal (LKR) | Basis | Required specification / note |
| :-- | :-- | --: | --: | --: | :--: | :-- |
| F01 | [Regulated 5V/2A enclosed adapter, UK 3-pin, centre-positive 2.1×5.5mm](https://www.duino.lk/product/5v-2a-3pin-ac-dc-smps-power-adaptor/) | 2 | 690 | 1,380 | S | PS3539-A; powers peripheral rails, not Uno Vin/barrel |
| F02 | [Enclosed USB power bank with two fixed-5V outputs, ≥2A total rating](https://lifemobile.lk/product/aspor-a323-10000mah-powerbank/) | 1 | 2,500 | 2,500 | E | Quote reputable bank/idle behaviour; USB chargers and cable for charging included in this allowance Life Mobile Aspor A323: two USB outputs specified 5V/2A; listed LKR 3,988, above the LKR 2,500 allowance. Confirm simultaneous total output, idle shutoff, charging cable and charger; those accessories are not established as included. |
| F03 | [AAA alkaline cells](https://tronic.lk/product/1-5v-aaa-battery-alkaline-2pcs-good-quality) | 4 | 100 | 400 | E | Two per micro:bit; initial set Tronic BA0061: buy TWO two-cell packs for four AAA cells; listed LKR 530 per pair, above the row's LKR 400 total allowance. Select 1.5V alkaline, not 1.2V rechargeable. |
| F04 | [AA alkaline cells](https://tronic.lk/product/1-5v-aa-battery-alkaline-2pcs-good-quality) | 8 | 100 | 800 | E | Four for robot motor pack, four spares; not rechargeable in this plan Tronic BA0066: buy FOUR two-cell packs for eight AA cells; listed LKR 530 per pair, above the row's LKR 800 total allowance. Select 1.5V alkaline. |
| F05 | [9V alkaline PP3 batteries](https://tronic.lk/product/kodak-9v-max-super-alkaline-battery-6lr61-original) | 3 | 300 | 900 | E | One tester battery and two multimeter batteries if needed; not motor power Tronic BA0206: 9V 6LR61 alkaline PP3, listed LKR 850 each, above the LKR 300 allowance. Buy three only if both multimeters need separate batteries; never use these for drive motors. |
| F06 | [9V snap clips](https://www.duino.lk/product/9v-battery-snap-on-connector-clip/) | 2 | 25 | 50 | P | Tester clip plus spare; not board power |

## Sri Lankan purchase links and order quantities

Every BOM row now has a Sri Lankan retailer or Daraz.lk marketplace link. Direct product links are used where a matching listing was found. Assembly rows link the components rather than claiming they are ready-made leads. Marketplace listings may ship from overseas; confirm the seller's location, delivery date, stock and final price before relying on them for a school session. Existing supplier links retain their earlier verification status.

**The numeric columns still show the previous planning allowances, not newly verified checkout prices.** A purchase link does not validate the price. Several linked items cost more than their allowance: USB-C cables, goggles, the soldering mat, enclosure, power bank and alkaline batteries. Notes give the observed listing price where available. **The linked retail basket is not yet confirmed within LKR 50,000**; obtain a new combined quote and recalculate the budget before ordering. Do not treat the displayed contingency as sufficient for all those price differences.

For LED/resistor/battery packs, the Qty column describes the number of parts needed, not the number of packs to add to the cart; the notes state the pack order. For example, 30 individual 1kΩ resistors require one approximately 40-piece pack. Assembly rows include separate component purchases in their notes.

- **A02/C07:** each needs its own red/black crocodile-clip pair. Solder existing jumper wires to the A02 pair for the micro:bit leads; use hookup wire for C07 probes. Insulate and test the assemblies before connecting power.
- **B02:** confirm the stand includes its sponge/cleaner; quote a cleaner if it does not.
- **C10:** buy the linked 5V USB-to-DC cable and an additional matching female screw-terminal socket. The two C09 sockets remain for the two bench adapters. Confirm current rating; never substitute a boosted 9V/12V USB cable.
- **C11:** confirm the switch's DC current rating, even when its product page advertises a higher AC rating.
- **C12/E07:** the exact inline-holder and BAT85 listings found are marketplace multipacks. Their checkout availability and landed price need confirmation; request local small-quantity equivalents if delivery or cost is unsuitable. The fuse holder uses a separately linked 2A 5×20mm fuse, not an included 5A fuse.
- **F02:** confirm the bank's simultaneous output rating and low-load behaviour. Its charger/cable are not established as included; quote them separately if absent. A compatible school-owned charger can be used only after confirming availability and suitability.

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
