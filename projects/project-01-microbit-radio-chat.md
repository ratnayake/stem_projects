# Project 01: Two-Way Pocket Radio Messenger

**Platform:** micro:bit V2

**Difficulty:** Beginner

**Estimated session:** 45–60 minutes

**Group:** 2–3 students; shared inventory rotates between activities.

**Revised:** 14 October 2026

## What students build

Two V2 boards exchange short preset text messages and a happy-face emoji using the built-in radio. Button A selects text, B sends an emoji, and A+B sends the selected text. Radio groups separate classroom activities but provide no confidentiality; range depends on the room.

## Materials and preparation

Use the items in the [revised procurement plan](../School_Electronics_Club_Procurement_Plan_LKR_50000.md). The club needs a computer and the correct USB **data** cable for programming. Disconnect power before changing wiring. These are classroom prototypes; hardware acceptance checks below still need to be performed.

| Item from revised inventory | Quantity needed for this build |
| :-- | :-- |
| micro:bit V2 | 2 |
| micro-USB data cables | 2 |
| 2×AAA micro:bit battery holders | 2 |
| AAA alkaline cells | 4 |


## Complete wiring and power

No external circuit. Flash both boards over USB, then use their two-AAA holders for portable operation. Check holder connector polarity; never use a 9V battery. USB power is also suitable.

## Complete source code

Use the **Python editor in [MakeCode for micro:bit](https://makecode.microbit.org)**, not MicroPython. Select V2 hardware when testing microphone/speaker behaviour.

```python
radio.set_group(7)
radio.set_transmit_power(7)
messages = ["HELLO", "YES", "NO", "HELP", "GAME ON"]
selected = 0

def receive_text(message):
    basic.show_string(message)
radio.on_received_string(receive_text)

def receive_value(name, value):
    if name == "EMOJI" and value == 1:
        basic.show_icon(IconNames.HAPPY)
        basic.pause(800)
radio.on_received_value(receive_value)

def select_text():
    global selected
    selected = (selected + 1) % len(messages)
    basic.show_string(messages[selected])
input.on_button_pressed(Button.A, select_text)

def send_emoji():
    radio.send_value("EMOJI", 1)
    basic.show_icon(IconNames.HAPPY)
input.on_button_pressed(Button.B, send_emoji)

def send_text():
    radio.send_string(messages[selected])
    basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.AB, send_text)

basic.show_icon(IconNames.HEART)
```

## Build, test and acceptance checks

1. Open MakeCode for micro:bit, choose Python, paste this code and download it to both V2 boards. This is MakeCode Python, not MicroPython.
2. Send text and emoji in both directions. Check A/B/A+B agree with the controls above.
3. Change one radio group: it should stop receiving the other group. Restore group 7.
4. Measure the achievable classroom range and record missed messages; do not claim guaranteed range.

## Extension

Add a received-message acknowledgement and retry timeout; radio groups are not encryption.

## Verification status

The wiring and code have been revised to address the feasibility review. Software checks and their limits are recorded in [VALIDATION.md](../VALIDATION.md). Physical testing of the exact purchased parts is still required before a student session.
