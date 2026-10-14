# Verification record

Revised guides and procurement documents: 14 October 2026.

The automated checks in [tools/validate_projects.py](tools/validate_projects.py) verify BOM row arithmetic, budget allocation, matching procurement copies, all 20 guide files, local links and the syntax of five MakeCode Python blocks. Run the document checks with:

```bash
python3 tools/validate_projects.py
```

The 57 purchase rows total **LKR 46,060**. Delivery allowance **LKR 1,500** and contingency **LKR 2,440** bring the allocation to **LKR 50,000**. All category totals match their rows. Price labels distinguish retrieved listings, previous-plan allowances and estimates; software checks do not establish supplier prices, stock or quote availability.

All **14 Arduino sketches (projects 06–19)** compiled successfully for both `arduino:avr:uno` and `arduino:avr:nano:cpu=atmega328`: **28 successful target builds**. Each complete C++ block was extracted directly from its guide; there were no replacement mocks in the target builds. Project 20 has no software. Tested tools/libraries:

| Component | Version |
| :-- | :-- |
| Arduino CLI | 1.5.2-rc.1 |
| Arduino AVR Boards | 1.8.6 |
| Servo by Arduino | 1.2.2 |
| hd44780 by Bill Perry | 1.3.2 |
| DHT sensor library by Adafruit | 1.4.6 |
| Adafruit Unified Sensor | 1.1.15 |
| SoftwareSerial / Wire | Included in Arduino AVR Boards 1.8.6 |

Compiler tools and libraries were installed in an isolated `/tmp/electronics-arduino` directory. To reproduce with an existing CLI installation containing those dependencies:

```bash
python3 tools/validate_projects.py --arduino-cli arduino-cli
```

For an isolated installation, add `--arduino-config /path/to/config.yaml`. The YAML can set `directories.data`, `directories.downloads`, `directories.user` and `build_cache.path` to writable directories. The script writes extracted sketches to a temporary directory and does not upload anything.

Additional host simulations passed using the **actual guide C++ blocks** and fake GPIO, sonar echoes, serial input and clock functions:

| Project | Checked behaviour |
| :-- | :-- |
| 08 | Held start button prevents countdown; early press cancels; absent reactions show two timeouts and no winner |
| 12 | Five echo timeouts produce an invalid result; a valid 30cm target gives a corresponding distance |
| 13 | Valid hand detection opens the lid; clear readings initiate closure; missing echo during closure reopens and inhibits closure |
| 14 | Occupied barrier remains open; valid clear paths initiate closure; lost clearance echo reopens and inhibits closure |
| 18 | Startup stop; stop after 400ms without a command; repeated commands sustain motion; unknown command and S stop; CR/LF framing is ignored |

Reproduce these simulations with Python 3 and a host `g++` compiler:

```bash
python3 tools/simulate_arduino.py
```

These host tests check software decisions, not physical servo timing, motor torque, electrical compatibility, UART signal timing or sensor coverage. They do not emulate AVR interrupts or prove real-time behaviour on a board.

All **five MakeCode Python examples (projects 01–05)** pass Python syntax parsing. **They have not been compiled by MakeCode, flashed to micro:bits or checked for MakeCode type/API compatibility in this workspace.** Use the Python editor at [MakeCode for micro:bit](https://makecode.microbit.org) and complete each guide's device checks. MakeCode Python and MicroPython are different environments.

No physical build or upload was performed. Each guide contains acceptance checks for the exact delivered parts, including supply polarity/current, servo motion, valid/no-echo handling and the Bluetooth timeout. Supplier quotes and those physical checks remain prerequisites for purchasing and classroom use respectively.
