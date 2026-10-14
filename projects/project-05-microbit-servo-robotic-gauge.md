# Project 05: Servo Dial for Approximate Board Temperature

**Platform:** micro:bit V2 + SG90

**Difficulty:** Intermediate

**Estimated session:** 60–75 minutes

**Group:** 2–3 students; shared inventory rotates between activities.

**Revised:** 14 October 2026

## What students build

The onboard processor temperature reading moves a cardboard pointer. It teaches scaling and servo positioning. It is an approximate board-temperature gauge, not a calibrated ambient thermometer.

## Materials and preparation

Use the items in the [revised procurement plan](../School_Electronics_Club_Procurement_Plan_LKR_50000.md). The club needs a computer and the correct USB **data** cable for programming. Disconnect power before changing wiring. These are classroom prototypes; hardware acceptance checks below still need to be performed.

| Item from revised inventory | Quantity needed for this build |
| :-- | :-- |
| micro:bit V2 and data cable | 1 |
| insulated crocodile-to-male leads for P0/GND | 2 |
| SG90 with horn/screw | 1 |
| regulated 5V/2A adapter and DC socket | 1 |
| 470µF capacitor ≥10V | 1 |
| breadboard/jumpers and light cardboard pointer | shared |


## Complete wiring and power

Power the board through its USB socket. Power the SG90 red lead from the separate **regulated 5V/2A adapter** through its matching DC screw-terminal socket; brown goes to adapter negative. Join adapter negative to board GND. Only the servo signal connects to the listed GPIO. Do not join adapter +5V to the board's USB-derived 5V rail, micro:bit 3V, or Vin. Add a 470µF capacitor (rated at least 10V) across the servo supply near the servo, positive to +5V and negative to GND. Use short power wires and a lightweight, freely moving model. Check voltage and polarity before attaching the servo. If the board resets or the servo stalls, disconnect and correct supply/wiring/linkage before continuing.

| Connection | Destination |
| :-- | :-- |
| Servo signal orange/yellow | micro:bit P0 ring through insulated lead |
| Servo red | External regulated +5V |
| Servo brown | External negative and micro:bit GND ring through insulated lead |

Connect only the large P0 and GND rings through insulated leads. Cover the unused 3V ring and prevent clips from touching adjacent rings. Do not clip servo power to the micro:bit. If a particular SG90 does not accept 3V logic, obtain a compatible servo or a suitable signal buffer before proceeding.

## Complete source code

Use the **Python editor in [MakeCode for micro:bit](https://makecode.microbit.org)**, not MicroPython. Select V2 hardware when testing microphone/speaker behaviour.

```python
def gauge():
    temp = input.temperature()
    angle = min(160, max(20, (temp - 15) * 140 / 30 + 20))
    pins.servo_write_pin(AnalogPin.P0, angle)
    basic.show_number(temp)
    basic.pause(1000)
basic.forever(gauge)
```

## Build, test and acceptance checks

1. Verify external +5V and common ground with a multimeter before connecting the board.
2. Run with no pointer attached; confirm smooth motion and no board resets.
3. Fit a balanced lightweight pointer with power disconnected; mark a 15–45°C scale over the commanded 20–160° travel.
4. Warm the back gently with a finger and compare changes, without treating the result as ambient accuracy.

## Reference notes

[Official micro:bit servo guidance](https://support.microbit.org/support/solutions/articles/19000101864-using-a-servo-with-the-micro-bit) recommends separate servo power and common ground.

## Extension

Use onboard relative light level instead; keep the same external servo supply.

## Verification status

The wiring and code have been revised to address the feasibility review. Software checks and their limits are recorded in [VALIDATION.md](../VALIDATION.md). Physical testing of the exact purchased parts is still required before a student session.
