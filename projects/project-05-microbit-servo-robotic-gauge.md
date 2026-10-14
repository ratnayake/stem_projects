# Project 05: Servo-Driven Analog Dial Gauge

**Track:** BBC Micro:bit Interactive Computing & Physical Mechatronics  
**Difficulty Level:** Intermediate (Grades 7–10)  
**Estimated Time:** 60 Minutes  
**Target Group:** 2 Students  

---

## 1. Project Overview
In physical computing, bridging software to physical mechanical motion is a milestone skill. In this project, students connect an SG90 micro-servo motor to the BBC Micro:bit V2 via the Micro:bit Breakout Board. Students build a physical analog pointer gauge (like a car speedometer or thermal dial) with cardboard and the glue gun. The pointer needle physically rotates to show temperature or light levels!

```mermaid
flowchart LR
    Sensor["Micro:bit Internal Temp / Light Sensor"] --> Process["Map Sensor Range to Servo Angle (0° to 180°)"]
    Process --> PWM["Generate 50Hz PWM Signal on Pin 0"]
    PWM --> Breakout["Breakout Extension Board"]
    Breakout --> Servo["SG90 Servo Motor Shaft"]
    Servo --> Needle["Physical Pointer Needle Moves on Paper Dial"]
```

---

## 2. Learning Objectives (STEM Concepts)
- **Mechatronics:** Pulse Width Modulation (PWM) duty cycle control, mechanical gear reduction, servo position calibration.
- **Data Scaling:** Mathematical linear interpolation (`map` function from 0–100% sensor value to 0–180 degrees).
- **Physical Prototyping:** Structural assembly, needle balance, dial face calibration.

---

## 3. Bill of Materials
| Item | Quantity | Source / Link |
| :--- | :---: | :--- |
| BBC Micro:bit V2 Board | 1 | [Duino.lk Micro:bit V2](https://www.duino.lk/product/microbit-v2-board/) |
| Micro:bit Extension Breakout Board | 1 | [Duino.lk Breakout Board](https://www.duino.lk/product/microbit-v2-extension-board-breakout-board/) |
| SG90 9g Micro Servo Motor | 1 | [Duino.lk SG90 Servo](https://www.duino.lk/product/servo-motor-sg90-9g/) |
| 5V/3.3V Breadboard Power Supply Module | 1 | [Duino.lk Power Module](https://www.duino.lk/product/5v-3-3v-breadboard-dedicated-power-module/) |
| 9V Battery Snap Connector Clip | 1 | [Duino.lk 9V Snap](https://www.duino.lk/product/9v-battery-snap-on-connector-clip/) |
| Male to Female Jumper Wires | 3 | [Duino.lk Jumper Wires](https://www.duino.lk/product/jumper-wire-male-to-female-20cm-40pcs/) |
| 60W Hot Melt Glue Gun & Cardboard | 1 | [Duino.lk Glue Gun](https://www.duino.lk/product/60w-glue-gun-nozzle-sd-a6/) |

---

## 4. Hardware Wiring & Pinout Table

> [!IMPORTANT]
> Servos draw inductive peak current when sweeping. While a single SG90 can be tested via the Micro:bit 3V supply, powering the servo rail via the Breadboard Power Module prevents board resets.

| SG90 Servo Lead Color | Connection Destination | Signal Function |
| :--- | :--- | :--- |
| **Brown** | Breakout Board **GND** (or Breadboard GND) | Ground Return |
| **Red** | Breakout Board **5V / 3.3V** (or Breadboard 5V) | DC Power Supply |
| **Orange / Yellow** | Breakout Board Pin **P0** | 50Hz PWM Servo Control |

---

## 5. Source Code (MakeCode Python)

```python
# Project 05: Servo-Driven Analog Dial Gauge
# Mode: Reads temperature and moves the physical pointer needle to match

def on_forever():
    # Read ambient temperature in degrees Celsius (typically 20°C - 40°C in Sri Lanka)
    temp = input.temperature()
    
    # Map temperature range (15°C to 45°C) to servo angle (0° to 180°)
    # Linear formula: angle = (temp - 15) * (180 / 30)
    target_angle = pins.map(temp, 15, 45, 0, 180)
    target_angle = Math.constrain(target_angle, 0, 180)
    
    # Write servo angle to Pin P0
    pins.servo_write_pin(AnalogPin.P0, target_angle)
    
    # Display reading on the matrix
    basic.show_number(temp)
    basic.pause(1000)

basic.forever(on_forever)
```

---

## 6. Physical Construction & Testing
1. Draw a semi-circle dial on white cardstock numbered from 15°C to 45°C in increments of 5 degrees.
2. Hot-glue the SG90 servo motor securely to the back of the cardstock dial with the output spline protruding through the center hole.
3. Power the Micro:bit and flash the code.
4. Press a plastic servo horn with a red pointer needle onto the shaft so it points exactly at 30°C when the room temperature is 30°C.
5. Place a warm finger or gently breathe on the back of the Micro:bit: observe the needle physically swing clockwise toward higher temperatures!

---

## 7. Innovation Challenges
1. **Light Meter Dial:** Swap `input.temperature()` for `input.light_level()` to build an analog photographic light meter.
2. **Audio-Level Speedometer:** Couple the gauge to the built-in microphone to create a physical "DJ Volume Meter".
