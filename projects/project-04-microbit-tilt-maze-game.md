# Project 04: Tilt-Controlled Grid Maze with Audio

**Platform:** micro:bit V2

**Difficulty:** Intermediate

**Estimated session:** 60 minutes

**Group:** 2–3 students; shared inventory rotates between activities.

**Revised:** 14 October 2026

## What students build

Tilt moves the bright player one grid cell per update. Reach the blinking goal while avoiding the dim hazard. This is discrete grid movement, not a momentum simulation. A displays the score between levels.

## Materials and preparation

Use the items in the [revised procurement plan](../School_Electronics_Club_Procurement_Plan_LKR_50000.md). The club needs a computer and the correct USB **data** cable for programming. Disconnect power before changing wiring. These are classroom prototypes; hardware acceptance checks below still need to be performed.

| Item from revised inventory | Quantity needed for this build |
| :-- | :-- |
| micro:bit V2 | 1 |
| micro-USB data cable | 1 |
| 2×AAA holder and AAA cells | optional portable supply |


## Complete wiring and power

No external wiring. Hold the board flat and test which physical tilt direction corresponds to each axis.

## Complete source code

Use the **Python editor in [MakeCode for micro:bit](https://makecode.microbit.org)**, not MicroPython. Select V2 hardware when testing microphone/speaker behaviour.

```python
player_x = 0
player_y = 0
goal_x = 4
goal_y = 4
hazard_x = 2
hazard_y = 2
score = 0

def new_level():
    global player_x, player_y, goal_x, goal_y, hazard_x, hazard_y
    player_x = 0
    player_y = 0
    goal_x = randint(2, 4)
    goal_y = randint(2, 4)
    hazard_x = randint(1, 3)
    hazard_y = randint(1, 3)
    while hazard_x == goal_x and hazard_y == goal_y:
        hazard_x = randint(1, 3)
        hazard_y = randint(1, 3)
new_level()

def show_score():
    basic.show_number(score)
input.on_button_pressed(Button.A, show_score)

def game():
    global player_x, player_y, score
    ax = input.acceleration(Dimension.X)
    ay = input.acceleration(Dimension.Y)
    # Move one axis per update so diagonal jumps cannot skip a hazard.
    if abs(ax) >= abs(ay) and abs(ax) > 250:
        player_x = min(4, max(0, player_x + (1 if ax > 0 else -1)))
    elif abs(ay) > 250:
        player_y = min(4, max(0, player_y + (1 if ay > 0 else -1)))
    if player_x == hazard_x and player_y == hazard_y:
        music.play_tone(131, 150)
        basic.show_icon(IconNames.SKULL)
        basic.pause(500)
        score = 0
        new_level()
    elif player_x == goal_x and player_y == goal_y:
        score += 1
        music.play_tone(880, 150)
        basic.show_icon(IconNames.YES)
        basic.pause(500)
        new_level()
    basic.clear_screen()
    if (input.running_time() // 350) % 2 == 0:
        led.plot_brightness(goal_x, goal_y, 120)
    led.plot_brightness(hazard_x, hazard_y, 35)
    led.plot_brightness(player_x, player_y, 255)
    basic.pause(180)
basic.forever(game)
```

## Build, test and acceptance checks

1. Flash and test all four tilt directions. Invert the relevant axis sign if your desired controls differ.
2. Confirm the player stays inside the 5×5 grid, the goal blinks, and collision resets the score.
3. Reach several goals and press A to view the score. The game display may replace the score after the scroll finishes.

## Extension

Add a countdown timer and show the score in a dedicated paused game state.

## Verification status

The wiring and code have been revised to address the feasibility review. Software checks and their limits are recorded in [VALIDATION.md](../VALIDATION.md). Physical testing of the exact purchased parts is still required before a student session.
