# Project 03: Classroom Relative Noise Monitor

**Platform:** micro:bit V2

**Difficulty:** Beginner

**Estimated session:** 45–60 minutes

**Group:** 2–3 students; shared inventory rotates between activities.

**Revised:** 14 October 2026

## What students build

The onboard microphone reports a relative level from 0–255, not decibels. Quiet shows a happy face, moderate noise a bar graph, and a threshold crossing a warning cross. The warning is silent to avoid self-triggering. A lowers the threshold, B raises it, and A+B temporarily displays the violation count.

## Materials and preparation

Use the items in the [revised procurement plan](../School_Electronics_Club_Procurement_Plan_LKR_50000.md). The club needs a computer and the correct USB **data** cable for programming. Disconnect power before changing wiring. These are classroom prototypes; hardware acceptance checks below still need to be performed.

| Item from revised inventory | Quantity needed for this build |
| :-- | :-- |
| micro:bit V2 | 1 |
| micro-USB data cable | 1 |
| 2×AAA holder and AAA cells | optional portable supply from inventory |
| cardboard stand | reused material |


## Complete wiring and power

No external wiring. Mount it on a cardboard stand without covering the microphone or hot-gluing the board itself.

## Complete source code

Use the **Python editor in [MakeCode for micro:bit](https://makecode.microbit.org)**, not MicroPython. Select V2 hardware when testing microphone/speaker behaviour.

```python
threshold = 150
violations = 0
armed = True
warning_until = 0
count_until = 0

def more_sensitive():
    global threshold
    threshold = max(60, threshold - 10)
input.on_button_pressed(Button.A, more_sensitive)

def less_sensitive():
    global threshold
    threshold = min(240, threshold + 10)
input.on_button_pressed(Button.B, less_sensitive)

def show_count():
    global count_until
    count_until = input.running_time() + 3000
input.on_button_pressed(Button.AB, show_count)

def monitor():
    global armed, violations, warning_until
    now = input.running_time()
    level = input.sound_level()
    if level < threshold - 20 and now >= warning_until:
        armed = True
    if armed and level >= threshold:
        violations += 1
        armed = False
        warning_until = now + 2000
    if now < count_until:
        basic.show_number(violations)
    elif now < warning_until:
        basic.show_icon(IconNames.NO)
    elif level < 60:
        basic.show_icon(IconNames.HAPPY)
    else:
        led.plot_bar_graph(level, 255)
    basic.pause(50)
basic.forever(monitor)
```

## Build, test and acceptance checks

1. Flash to a V2 board and compare quiet, normal speech and controlled claps. Avoid shouting close to ears.
2. Use A/B to select a useful classroom threshold. A sustained loud sound should produce one violation until sound falls below the rearm threshold.
3. Check the cross remains visible for two seconds and the bar graph does not overwrite it.
4. A+B shows the count for about three seconds. Counting/sampling pauses while this count scrolls; it is a classroom indicator, not a continuous calibrated recorder.

## Reference notes

[Official MakeCode sound-level documentation](https://makecode.microbit.org/reference/input/sound-level) defines the relative range.

## Extension

Send a radio notification to another board on each violation.

## Verification status

The wiring and code have been revised to address the feasibility review. Software checks and their limits are recorded in [VALIDATION.md](../VALIDATION.md). Physical testing of the exact purchased parts is still required before a student session.
