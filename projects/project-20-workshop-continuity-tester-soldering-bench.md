# Project 20: Soldering Workshop: LED & Buzzer Cable Tester

**Platform:** Low-voltage workshop circuit

**Difficulty:** Intermediate

**Estimated session:** 90 minutes

**Group:** 2–3 students; shared inventory rotates between activities.

**Revised:** 14 October 2026

## What students build

Build a battery-powered continuity indicator for disconnected loose cables. A conducting path completes parallel LED and active-buzzer branches. The tester does not measure resistance or certify a path below 1Ω. This project permanently consumes its LED, resistor, alarm buzzer, snap clip and probe materials.

## Materials and preparation

Use the items in the [revised procurement plan](../School_Electronics_Club_Procurement_Plan_LKR_50000.md). The club needs a computer and the correct USB **data** cable for programming. Disconnect power before changing wiring. These are classroom prototypes; hardware acceptance checks below still need to be performed.

| Item from revised inventory | Quantity needed for this build |
| :-- | :-- |
| adjustable soldering iron, stand/cleaner, manual solder sucker | shared |
| solder wire, wire stripper, multimeter, eye protection | shared |
| green LED | 1 |
| 1kΩ through-hole resistor | 1 |
| 3–24V active continuous alarm buzzer | 1 |
| 9V PP3 battery | 1 |
| 9V snap clip | 1 |
| insulated probe/alligator leads | 2 |
| on/off switch | 1 |
| small enclosure, insulation/heat-shrink and hookup wire | workshop consumables |


## Complete wiring and power

This standalone circuit has no microcontroller. Use **1kΩ**, not 220Ω: at approximately 9V and a 2V LED it gives about 7mA and 0.049W in the resistor. A 1/4W through-hole resistor is adequate. The active DC alarm is intentionally different from the passive discs used in the Arduino tone and knock projects.

```
9V (+) -- switch -- Probe A -- [unpowered cable] -- Probe B --+-- 1kΩ -- LED anode
                                                           |           LED cathode -- 9V (-)
                                                           +-- active buzzer (+)
                                                               active buzzer (-) -- 9V (-)
```

Use only on loose, **disconnected and unpowered** cables. If buying the linked C07 clip pair, first solder flexible C05 hookup wires to the two clips, insulate the joints and add strain relief to make the probe leads. The probes apply battery voltage and are not suitable for testing connected semiconductor circuits, USB electronics, mains wiring or powered equipment. Keep the battery unplugged during assembly.

## Build, test and acceptance checks

1. At a supervised ventilated bench, put on eye protection, use a heat-resistant mat, and rest the iron only in its stand. Select a temperature suitable for the purchased solder; start around 330–350°C and adjust for the joint. Wash hands after soldering.
2. Breadboard the tester first with a 1kΩ resistor and briefly touch probes together: LED and active buzzer should operate. Disconnect the battery.
3. Strip and tin the hookup wires. Solder the switch/probe path and the two parallel branches, checking LED polarity and avoiding solder bridges. Use the manual sucker for rework.
4. Use the multimeter resistance mode to check joints before powering; compare with shorted test leads rather than expecting exactly zero. Check that the two branches do not short the battery.
5. Insulate every exposed joint, provide strain relief and mount in a small enclosure. Adult supervision is required for drilling or cutting. Connect the battery and verify a healthy cable, a broken cable and the off switch.
6. Label the enclosure: “UNPOWERED LOOSE CABLES ONLY — 9V TEST VOLTAGE.” Store with the switch off.

## Extension

Use the multimeter to compare resistance measurements with this simple audible/visual conducting-path test.

## Verification status

The wiring and code have been revised to address the feasibility review. Software checks and their limits are recorded in [VALIDATION.md](../VALIDATION.md). Physical testing of the exact purchased parts is still required before a student session.
