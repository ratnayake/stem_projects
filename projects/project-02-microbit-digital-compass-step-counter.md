# Project 02: Digital Compass & Experimental Step Counter

**Platform:** micro:bit V2

**Difficulty:** Beginner/intermediate

**Estimated session:** 60 minutes

**Group:** 2–3 students; shared inventory rotates between activities.

**Revised:** 14 October 2026

## What students build

A calibrated compass shares the board with an experimental acceleration peak counter. The counter uses upper/lower thresholds and a minimum interval, and needs calibration for the chosen mounting position. It is not an exact pedometer. A selects compass, B selects live step count; A+B resets the count.

## Materials and preparation

Use the items in the [revised procurement plan](../School_Electronics_Club_Procurement_Plan_LKR_50000.md). The club needs a computer and the correct USB **data** cable for programming. Disconnect power before changing wiring. These are classroom prototypes; hardware acceptance checks below still need to be performed.

| Item from revised inventory | Quantity needed for this build |
| :-- | :-- |
| micro:bit V2 | 1 |
| micro-USB data cable | 1 |
| 2×AAA holder and AAA cells | 1 holder + 2 cells |
| rubber band/strap | reused craft material |


## Complete wiring and power

No external electronics. Mount the board firmly on the body with a secure strap. Keep it away from motor magnets and steel desks when calibrating or using the compass.

## Complete source code

Use the **Python editor in [MakeCode for micro:bit](https://makecode.microbit.org)**, not MicroPython. Select V2 hardware when testing microphone/speaker behaviour.

```python
steps = 0
mode = 0
armed = True
last_step = 0
HIGH_PEAK = 1300
LOW_REARM = 1100
MIN_INTERVAL = 300
input.calibrate_compass()

def compass_mode():
    global mode
    mode = 0
input.on_button_pressed(Button.A, compass_mode)

def steps_mode():
    global mode
    mode = 1
input.on_button_pressed(Button.B, steps_mode)

def reset_steps():
    global steps
    steps = 0
input.on_button_pressed(Button.AB, reset_steps)

def sample_steps():
    global steps, armed, last_step
    strength = input.acceleration(Dimension.STRENGTH)
    now = input.running_time()
    if strength < LOW_REARM:
        armed = True
    if armed and strength > HIGH_PEAK and now - last_step >= MIN_INTERVAL:
        steps += 1
        last_step = now
        armed = False
    basic.pause(30)
basic.forever(sample_steps)

def display_mode():
    if mode == 0:
        heading = input.compass_heading()
        if heading < 45 or heading >= 315:
            basic.show_string("N")
        elif heading < 135:
            basic.show_string("E")
        elif heading < 225:
            basic.show_string("S")
        else:
            basic.show_string("W")
    else:
        basic.show_number(steps)
    basic.pause(200)
basic.forever(display_mode)
```

## Build, test and acceptance checks

1. Fill the calibration display by tilting the board when prompted. Rotate away from magnetic objects and check the four directions.
2. Reset with A+B, press B and manually count 20 slow steps; repeat with 20 normal and 20 fast steps. Record the counter error for each.
3. Adjust HIGH_PEAK, LOW_REARM and MIN_INTERVAL for the mounting position. At rest the count should remain stable.
4. Confirm sampling continues while numbers scroll. Mode changes take effect after the current display finishes.

## Extension

Record raw acceleration against time and develop a better step detector; measured errors should accompany any distance estimate.

## Verification status

The wiring and code have been revised to address the feasibility review. Software checks and their limits are recorded in [VALIDATION.md](../VALIDATION.md). Physical testing of the exact purchased parts is still required before a student session.
