# 🛹 Volume 4.1: Mobility Electromechanics & Power Tools
*Reprogramming hoverboard STM32 controllers, hacking 30-pole BLDC hub motors, drill planetary gearboxes, and 125k RPM vacuum turbines.*

---

## 1. Hoverboard Hub Motors & Controller Hacking

```
Hoverboard Hardware Architecture:
+--------------------------------------------------------------+
| [36V 4.4Ah 18650 Battery Pack]                               |
|                     |                                        |
|                     v                                        |
|  [Mainboard: STM32F103 MCU + Dual 3-Phase Inverter MOSFETs]  |
|          |                                   |               |
|          v                                   v               |
|  [Left 350W Hub Motor]              [Right 350W Hub Motor]   |
|  (30 Neodymium Poles)               (30 Neodymium Poles)     |
+--------------------------------------------------------------+
```

### Why Hoverboard Scrap is a Maker Goldmine:
Hoverboards offer an unbeatable price-to-performance ratio. A scrap hoverboard yields:
- **Two 350-Watt Brushless Hub Motors**: Built directly into solid rubber or pneumatic wheels, packing 30 sintered neodymium magnets and 3 built-in Hall-effect sensors.
- **A Complete Dual-Motor Inverter Controller**: Driven by an **ARM Cortex-M (STM32F103 or GD32F103)** microcontroller connected to 12 high-power MOSFETs capable of switching 15A to 20A per phase at 36V–42V.
- **A 36V 10S2P Lithium-Ion Battery Pack**: 20 high-drain 18650 cells with integrated Battery Management System (BMS).

---

### The Open-Source Controller Hack (`hoverboard-firmware-hack`):
You do not need to discard the motherboard or buy expensive aftermarket motor drivers!

```
ST-Link Programming Header on Mainboard:
  [GND]   ---> ST-Link GND
  [SWDIO] ---> ST-Link SWDIO
  [SWCLK] ---> ST-Link SWCLK
  [3.3V]  ---> ST-Link 3.3V (Only when main battery is disconnected!)
```

1. **Flashing Procedure**:
   - Solder a 4-pin header to the programming pads labeled `GND`, `DIO`, `CLK`, and `3.3V` on the hoverboard mainboard.
   - Connect an inexpensive **ST-Link V2 programmer** ($4 online) to your PC.
   - Clone the open-source **`hoverboard-firmware-hack`** repository (available on GitHub).
   - In `config.h`, choose your preferred control input method:
     - `CONTROL_UART`: Control speed and steering via serial commands from an Arduino, Raspberry Pi, or ESP32.
     - `CONTROL_PPM`: Plug directly into a standard RC hobby drone or car receiver.
     - `CONTROL_ADC`: Wire directly to two analog thumb throttles or potentiometers.
   - Flash the firmware using OpenOCD or STM32CubeProgrammer.
2. **The Result**: You now have a complete, professional-grade dual-channel 700W motor drive platform with regenerative braking and Field-Oriented Control (FOC) for $0 in driver costs.

---

### Creative Engineering Projects:

```
Electric Powered Yard Cart / Wheelbarrow:
  +-------------------------------------------------------------+
  | [Dual Hoverboard Hub Motors as Front Wheels]                |
  |         |                                                   |
  | [Reprogrammed Mainboard mounted under steel tray]           |
  |         |                                                   |
  | [Thumb Throttle & Reverse Switch on Left/Right Handles]     |
  |                                                             |
  | ====> Hauls 350 lbs of gravel up a 25° incline effortlessly!|
  +-------------------------------------------------------------+
```

#### A. Autonomous Heavy Rover / AGV (Outdoor Robot Platform)
- Mount the two hoverboard wheels to a rectangular aluminum or plywood chassis with two rear caster wheels.
- Send simple ASCII serial velocity commands from a Raspberry Pi running ROS (Robot Operating System) or an Arduino:
  ```
  Speed: 150, Steer: -50\n
  ```
- Easily carries 100+ lbs of payload over grass, rocks, and dirt roads.

#### B. ODrive-Powered Robotic Arm & Quadruped Leg Joints
- Remove the rubber tire from a hoverboard hub motor to expose the bare aluminum rim.
- Attach an off-axis magnetic rotary encoder (such as the **AS5600** or **AMT102**).
- Connect to an **ODrive motor controller**: The hub motor transforms into a direct-drive, zero-backlash robotic actuator capable of holding position down to 0.01° with massive holding torque.

---

## 2. Cordless Drills: Modular Powertrains for Combat Robotics

```
Drill Planetary Transmission:
  [Mabuchi 550 DC Motor] ---> (Sun Gear 1) ===> [Planetary Stage 1 (6:1)]
                                                        |
                                                        v
                              [Planetary Stage 2 (6:1)] ===> High-Torque 1/2" Spindle
                              *(Total Reduction: 36:1)*
```

### The Combat Robotics Rite of Passage:
For decades, combat robot builders in the 12 lb (Hobbyweight) and 30 lb (Featherweight) classes built drivetrains from cheap cordless drills (Harbor Freight, Black & Decker, Ryobi).
- **Why**: A complete drill provides a high-torque 550-size motor, a hardened steel 2-stage or 3-stage planetary gearbox, an output bearing, and a keyless chuck all in one compact cylindrical assembly.

#### Locking the Clutch (Mandatory for High Load):
The adjustable torque collar on a drill will slip under aggressive acceleration or wheel impacts.
1. Unscrew the front chuck (remember: chuck retention screws inside the jaw are **reverse-threaded / left-hand thread**).
2. Remove the plastic clam-shell and unscrew the gearbox ring collar.
3. Extract the small steel clutch ball bearings and springs.
4. Fill the ball pockets with high-strength structural epoxy (J-B Weld) or insert solid steel roll-pins, then re-tighten the collar. The transmission is now locked solid into 100% direct-drive mode.

---

## 3. Digital Brushless Vacuum Turbines (Dyson Type)
Modern bagless cordless stick vacuums utilize custom brushless switched-reluctance or high-frequency PMSM motors.
- **Insane Velocity**: Spins at **100,000 to 125,000 RPM [TYPICAL]**.
- **Impeller**: Precision CNC-machined aerodynamic mixed-flow impeller.

### Repurposing Exploits:
- **Instant Desktop Thermoforming Vacuum Former**: Standard shop vacuums have slow air evacuation rates. A digital vacuum motor creates instantaneous, intense negative pressure—drawing heated plastic sheets down over intricate 3D-printed patterns before the plastic can cool.
- **Micro Wind Tunnel**: Testing aerodynamic drag on miniature airfoils and model rockets.

---

## 4. Electric Scooters (Ninebot / Xiaomi): Narrow Hubs & Traction

Commercial rental and consumer electric commuter scooters (Ninebot ES2/ES4/Max, Xiaomi M365) are discarded in large quantities due to dead battery management systems (BMS) or cracked neck stems:

```
+--------------------------------------------------------------------------+
| Scrap E-Scooter Powertrain Components:                                  |
|                                                                          |
| [ 8.5" or 10" Narrow Pneumatic Tire BLDC Hub ] (36V 350W-500W, Hollow)   |
| [ 36V 15A Field-Oriented Brushless Controller ]                          |
| [ Hall Effect Thumb Lever Throttle ] (0.8V to 4.2V Analog Output)       |
+--------------------------------------------------------------------------+
```

### A. The Narrow Pneumatic Hub Motor
- **Specs**: 36V DC [TYPICAL] nominal, 250W–350W continuous (up to 700W peak), narrow wheel profile ($45\text{ mm}$ width) with an 8.5" or 10" inflatable pneumatic tire.
- **Advantage Over Hoverboards**: Hoverboard hub motors are wide ($6.5\text{ to }8.0\text{ inches}$) with solid, unforgiving rubber tires that transmit harsh road vibration. Scooter hubs feature standard bicycle-style pneumatic tires that absorb shocks, fit into narrow fabricated steel swingarms, and feature integrated disc or drum brake mounts.
- **Axle Geometry**: Dual-flat machined $12\text{ mm}$ solid steel axle with internal phase and Hall sensor wire routing.

### B. Repurposing Exploits:
1. **Motorized Heavy Shop Cart / Wheelbarrow**: Mount a single scooter front hub into a pivot fork on a heavy welding cart or yard wheelbarrow. Run off a 36V power tool battery pack (e.g., two 18V tool batteries in series) and control speed with the salvaged thumb throttle to move 400 lb loads effortlessly up ramps.
2. **Band Saw Variable-Speed Drive**: Couple the smooth pneumatic tire directly against the driven wheel of an old wood/metal bandsaw. By adjusting the scooter controller throttle, you achieve infinitely variable blade speed for cutting steel, brass, or aluminum without changing belt pulley steps.
3. **Heavy Linear Gantry Traction Drive**: Press the rubber tire against the underside of a long I-beam or square-tube rail on a heavy gantry crane or rolling gate for high-traction, non-slip friction propulsion.

---

## 5. Robot Vacuum Cleaners (Roomba / Roborock): 360° LDS LiDAR Turrets

While Volume 5.1 outlines building a custom 2D LiDAR using a supermarket barcode polygon mirror, discarded robotic vacuum cleaners (Neato Botvac, Roborock, Xiaomi, Dreame) provide complete, factory-calibrated **360° Laser Distance Sensor (LDS) turrets** for next to nothing:

```
                [ Rotating Optical Turret ]
           (Laser Emitter + CMOS Line-Array Sensor)
       =================================================
             [ Wireless Inductive Transformer / Slip Ring ]
       -------------------------------------------------
             [ 5V DC Drive Motor + O-Ring Belt Transmission ]
                                   |
                                   v
             [ 115200 Baud UART Serial Data Stream: Angle, Dist ]
```

### A. Internal Architecture & Data Transmission
- **Optical Engine**: An infrared laser diode and a CMOS linear camera sensor mounted on a rotating carousel spinning at **5 Hz to 10 Hz (300 to 600 RPM [TYPICAL])**.
- **Power & Data Interface**: The rotating turret is powered via a contactless high-frequency inductive transformer or miniature gold-wire slip ring.
- **Electrical Interface**: Only 4 connections are required:
  1. `Motor VCC` (+5V DC to spin the drive motor via PWM speed control).
  2. `Logic VCC` (+3.3V or +5V DC to power the optical core).
  3. `GND` (Common ground).
  4. `UART TX` (3.3V TTL serial data output transmitting at **115200 baud**).

### B. Standard Serial Packet Format
The turret continuously broadcasts raw binary packets containing:
- Packet Header byte (`0xFA` or `0x55`).
- Current rotational angle index ($0^\circ\text{ to }360^\circ$ in fractional increments).
- Target distance in millimeters ($150\text{ mm}$ minimum to $6,000\text{ mm}$ maximum range).
- Signal confidence / optical quality byte.
- Checksum validation byte.

### C. Repurposing Exploits:
- **Plug-and-Play ROS2 / SLAM Navigation for AGVs**: Wire the UART TX directly to the hardware serial port of an ESP32 or Raspberry Pi. Using standard open-source ROS/ROS2 driver packages (e.g., `xv_11_laser_driver` or `rplidar_ros`), the sensor provides full real-time Simultaneous Localization and Mapping (SLAM) and obstacle avoidance on autonomous mobile rovers, completely eliminating the labor of optical calibration and mirror balancing.


---

## 6. Electric Scooter Rental Fleet Salvage & Controller Decryption

```
Rental E-Scooter Architecture & Bypassing Encryption:
  +-------------------------------------------------------------+
  | [Rental Head Stem: Cellular IoT Modem & GPS Tracker]        |
  |   (Sends Encrypted Proprietary Handshake via UART to ESC)   |
  |                              |                              |
  |                    ====[CUT & DISCARD!]===>                 |
  |                              |                              |
  | [Main Inverter ESC: STM32 / GD32 MCU + 6 High-Power FETs]   |
  |                              |                              |
  |         +--------------------+--------------------+         |
  |         | 3 Thick Phase Wires| 5 Hall Sensor Wires|         |
  |         v                    v                    v         |
  | [36V 350W-500W Narrow Pneumatic Hub Motor with Drum Brake]  |
  +-------------------------------------------------------------+
```

### The Rental Lockout Trap
Municipal police auctions, scrap yards, and metal recyclers regularly accumulate hundreds of commercial commuter electric scooters (Ninebot Max G30, Xiaomi Pro 2, Segway Commercial).
- Many makers discard the entire electronic powertrain because the scooter refuses to power on or sounds an alarm buzzer when moved.
- **The Mechanism**: The main motor controller (ESC) in the deck listens for an encrypted serial ping packet from the handlebar cellular IoT tracking module. Without this periodic heartbeat, the controller remains in a locked sleep state.

### The 3 Options for Full Motor Exploitation:
1. **The Flashed Open-Source Firmware Option (Free)**:
   - For Ninebot G30 / Xiaomi M365 ESCs, open-source community firmware projects (e.g., *ScooterHacking Utility / SHFW*) overwrite the protected bootloader via an ST-Link programmer or Bluetooth.
   - Disables all IoT handshakes, unlocks **Field-Oriented Control (FOC)**, raises phase current limits to 30A, and enables linear analog throttle inputs.
2. **The \$15 Generic E-Bike Controller Swap (Fastest)**:
   - Discard the proprietary motherboard entirely.
   - Connect the hub motor's 3 thick wires (Phase $U, V, W$) and 5 thin Hall sensor wires ($5\text{V}, \text{GND}, H_a, H_b, H_c$) to a generic 36V/48V 350W sensorless/sensored brushless e-bike ESC.
   - Wire a standard 3-wire Hall thumb throttle ($+5\text{V}, \text{GND}, 0.8\text{–}4.2\text{V}$ signal) to achieve instantaneous variable speed with forward and reverse functionality.
3. **High-Performance Robotics Drive via VESC / ODrive**:
   - Running the hub motor on a VESC (Vedder ESC) allows closed-loop torque, velocity, and position control over CAN-bus, turning the scooter wheel into a high-precision autonomous gantry traction drive.

---

## 7. 10S/13S BMS Locked-State Triage & Cell Recovery

```
10S Lithium Pack Recovery Workflow:
  [Dead 36V E-Scooter Battery Pack (Reads 0.0V at Output XT60)]
                              │
                              ▼
  (Carefully Cut Heat-Shrink Wrap Along Seam with Plastic Tool)
                              │
                              ▼
  [Probe Main Positive and Main Negative Nickel Busbars DIRECTLY]
       ├── Reading < 15.0V? ──► DANGER: Cells Deeply Discharged (<1.5V/cell).
       │                        Copper dendrites formed. Discard to battery recycling!
       │
       └── Reading 30.0V - 36.0V? ──► CELLS ARE IN EXCELLENT HEALTH!
                                      Internal BMS tripped into protective lock.
                                      │
                                      ▼
             (Desolder Proprietary BMS & Wire Generic 10S Balance Board)
                                      │
                                      ▼
         =====> Recovers a $200 High-Drain 36V 10Ah Lithium Battery Pack!
```

- **Cell Grade**: Rental scooter packs contain top-tier industrial high-drain cells: **Samsung 25R / 30Q, LG Chem MJ1 / HG2, or Panasonic 18650PF** rated for 15A to 20A continuous discharge.
- **The BMS Fault**: When a scooter sits idle in a warehouse for months, the BMS logic drains a few micro-amps until the overall pack drops below the lower cutoff threshold ($30.0\text{V}$ nominal for 10S). The proprietary firmware permanently disables the output MOSFETs.
- **Triage SOP**:
  1. Measure total pack voltage directly on the raw battery busbars before the BMS board. If the voltage is between **$30\text{V}$ and $36\text{V}$**, the cells are in pristine condition.
  2. Measure each individual parallel group (Groups 1 through 10) with a digital multimeter. Verify that all group voltages match within **$\pm 0.05\text{V}$**.
  3. Desolder or snip the thin balance ribbon wires leading to the dead proprietary BMS.
  4. Solder a \$12 generic 10S 30A Lithium BMS board with balance charging leads. The pack is fully restored to 100% capacity for powering off-grid solar generators, high-power workshop lighting, or electric go-karts.

---

## 8. Regenerative Braking Energy Absorption & Shunt Dump Resistors

```
Regenerative Energy Shunt Dump Circuit:
  [ Spinning Hub Motor Driving Large Inertial Load ]
                         │
                         ▼ (Emergency Stop Command)
  [ Inverter Switches into Dynamic Regen Braking: Pumps 30A Back EMF! ]
                         │
                         ▼
  [ DC Bus Voltage Spikes: 36V ──> 42V ──> 58V! ]
                         │
                         ▼
  [ Voltage Comparator / Zener Sense Circuit Triggers IRFB4110 MOSFET ]
                         │
                         ▼
  [ Diverts Surge Current into 2.0 Ohm 200W Aluminum Wirewound Resistor ]
                         │
                         ▼
  =====> Dynamic Magnetic Braking Halts 500 lb Load in 1.2 Seconds
         Without Blowing Out Inverter MOSFETs!
```

- **The Inertial Hazard**: When using high-torque hub motors on heavy moving loads (automated material carts, shop cranes, or bandsaw drives), commanding an abrupt stop forces the motor to act as a powerful 3-phase alternator.
- **The Overvoltage Surge**: If the battery pack is already fully charged (or if powered by an AC-to-DC power supply that cannot absorb reverse current), the generated back-EMF spikes the DC bus voltage above **60V**, instantly puncturing the gate oxide of the inverter MOSFETs and destroying the driver.
- **The Solution**: Wire a high-power **braking chopper circuit** across the DC bus:
  - Use a high-current N-channel MOSFET (e.g., IRFB4110) controlled by a comparator set to trigger at **$43.0\text{V}$**.
  - Route the excess electrical energy into a chassis-mounted **$2.0\,\Omega$, 200W aluminum-housed wirewound power resistor** (or a 12V 55W automotive halogen bulb).
  - The kinetic energy of the moving cart is converted cleanly into thermal heat, delivering ferocious, controllable electromagnetic deceleration without wearing mechanical brake pads.
