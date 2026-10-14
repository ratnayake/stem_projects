# Project 11: Indoor Weather Station with 16x2 I2C LCD

**Track:** Sensor Measurement & Display Systems  
**Difficulty Level:** Intermediate (Grades 7–10)  
**Estimated Time:** 60 Minutes  
**Target Group:** 2 Students  

---

## 1. Project Overview
In this project, students build an automated climate station for the classroom or school science lab. Using the DHT11 digital capacitive humidity and thermistor sensor, an Arduino Uno polls environmental conditions every 2 seconds. The telemetry data (temperature in °C and relative humidity in %) is formatted and displayed on a crystal-clear 16x2 character LCD via the I2C serial communications bus.

```mermaid
flowchart LR
    Air["Classroom Atmosphere"] --> DHT["DHT11 Sensor (Single-Wire Bus)"]
    DHT --> Uno["Arduino Uno (Processing)"]
    Uno --> I2C["I2C Serial Bus (SDA / SCL)"]
    I2C --> Backpack["PCF8574 I2C Backpack Adapter"]
    Backpack --> LCD["16x2 Liquid Crystal Display"]
```

---

## 2. Learning Objectives (STEM Concepts)
- **Meteorology & Thermodynamics:** Temperature gradients, relative humidity (percentage of water vapor saturation in air), dew point calculations.
- **Serial Bus Protocols:** The Inter-Integrated Circuit ($I^2C$) protocol, two-wire communication (SDA and SCL), hex addressing (`0x27` or `0x3F`).
- **Liquid Crystal Technology:** 5x8 dot matrix character fonts, contrast potentiometer adjustment, screen refresh caching.

---

## 3. Bill of Materials
| Item | Quantity | Source / Link |
| :--- | :---: | :--- |
| Arduino Compatible Uno R3 | 1 | [Duino.lk Uno R3](https://www.duino.lk/product/arduino-compatible-r3-atmega328p-ch340g/) |
| DHT11 Temperature & Humidity Sensor | 1 | [Duino.lk DHT11](https://www.duino.lk/product/dht11-temperature-and-humidity-sensor-module/) |
| LCD 16x2 Character Display (Blue) | 1 | [Duino.lk LCD 16x2](https://www.duino.lk/product/lcd-16x02-display-blue/) |
| I2C Serial Interface Adapter for 1602 LCD | 1 | [Duino.lk I2C Adapter](https://www.duino.lk/product/iici2c-twi-spi-serial-interface-module-for-1602-1604-2004lcd/) |
| Breadboard 830 Tie Point | 1 | [Duino.lk Breadboard 830](https://www.duino.lk/product/breadboard-830-tie-point-16-5x5-5x0-85-cm/) |
| Male to Female Jumper Wires | 8 | [Duino.lk Jumper Wires](https://www.duino.lk/product/jumper-wire-male-to-female-20cm-40pcs/) |

---

## 4. Hardware Wiring & Pinout Table

### I2C LCD Adapter Connections
| I2C Adapter Pin | Arduino Uno Pin | Function |
| :--- | :--- | :--- |
| **GND** | GND | Ground |
| **VCC** | 5V | Power |
| **SDA** | **A4** (or dedicated SDA header) | Serial Data Line |
| **SCL** | **A5** (or dedicated SCL header) | Serial Clock Line |

### DHT11 Sensor Connections
| DHT11 Sensor Pin | Arduino Uno Pin | Function |
| :--- | :--- | :--- |
| **+ (VCC)** | 5V | Power |
| **- (GND)** | GND | Ground |
| **OUT / S (Signal)** | Pin **D2** | Bi-directional Single-Wire Data |

---

## 5. Arduino C++ Source Code

> [!NOTE]
> Install the **LiquidCrystal_I2C** and **DHT sensor library** via the Arduino IDE Library Manager before uploading.

```cpp
/*
 * Project 11: Indoor Weather Station with 16x2 I2C LCD
 * Club: School Electronics & Innovation Club
 */

#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);
// Standard I2C address is usually 0x27 (or 0x3F) for 16x2 displays
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  Serial.begin(9600);
  dht.begin();
  
  lcd.init();
  lcd.backlight();
  
  // Startup Welcome Screen
  lcd.setCursor(0, 0);
  lcd.print("INNOVATION CLUB");
  lcd.setCursor(0, 1);
  lcd.print("WEATHER STATION");
  delay(2000);
  lcd.clear();
}

void loop() {
  // Read humidity and temperature (takes ~250 milliseconds)
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  // Check if read failed
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor!");
    lcd.setCursor(0, 0);
    lcd.print("Sensor Error!   ");
    delay(2000);
    return;
  }

  // Format and print to Serial Monitor
  Serial.print("Temp: "); Serial.print(temperature); Serial.print(" *C  | ");
  Serial.print("Humidity: "); Serial.print(humidity); Serial.println(" %");

  // Format Line 1 on LCD
  lcd.setCursor(0, 0);
  lcd.print("Temp: ");
  lcd.print(temperature, 1); // 1 decimal place
  lcd.print((char)223);      // Degree symbol
  lcd.print("C   ");

  // Format Line 2 on LCD
  lcd.setCursor(0, 1);
  lcd.print("Humidity: ");
  lcd.print((int)humidity);
  lcd.print("%   ");

  delay(2000); // Wait 2 seconds between measurements
}
```

---

## 6. Testing & Calibration Tips
- **LCD screen is blue but showing only black rectangles?** Turn the small blue trimmer potentiometer on the back of the I2C backpack with a small screwdriver until the white letters appear crisp and high-contrast!
- **Display says "Sensor Error!"?** Verify DHT11 signal pin is firmly seated in Pin D2.

---

## 7. Innovation Challenges
1. **Heat Index Comfort Meter:** Compute the OSHA Heat Index formula and display a warning tag (`"COMFORT: OK"` vs `"HEAT ALERT: HIGH"`).
2. **Relay Fan Automation:** Connect the [5V Relay Module](https://www.duino.lk/product/relay-board-module-5v-1-channel/) so an electric cooling fan kicks on automatically when room temperature exceeds 31°C!
