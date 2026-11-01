# ⚡ Volume 0.3: Universal Motor Driving Topologies & Control Architectures
*The definitive guide to pairing salvaged motors with the proper silicon drivers, power supplies, and microcontroller code.*

---

## 1. Topologies Overview & Selection Matrix

```
+------------------------------------------------------------------------------------------------+
| Motor Type          | Drive Topology              | Controller IC / Module      | Control Signal|
| ---------------------------------------------------------------------------------------------- |
| Brushed DC (< 2A)   | Dual BJT/MOSFET H-Bridge    | L298N / DRV8833             | PWM + 2 DIR   |
| Brushed DC (10-43A) | High-Current Half-Bridge x2 | BTS7960 Dual Module         | 2 PWM + Enable|
| Bipolar Stepper     | Chopper Constant-Current    | A4988 / TMC2209 / TB6600    | STEP + DIR    |
| Unipolar Stepper    | Low-Side Darlington Array   | ULN2003                     | 4-Phase Logic |
| Sensorless BLDC     | 6-Step Inverter (Back-EMF)  | Hobby RC ESC (30A–100A)     | 50Hz Servo PWM|
| Sensored BLDC / FOC | Field Oriented Control      | ODrive / VESC / SimpleFOC   | CAN / UART /RC|
| High-Voltage PMDC   | SCR Half-Wave / Full-Wave   | KB Electronics KBIC-120/240 | 5k Pot / 0-10V|
| AC Universal Motor  | TRIAC Phase-Angle (Closed)  | TDA1085 / U2008B Board      | Pot + Tacho In|
+------------------------------------------------------------------------------------------------+
```

---

## 2. High-Power Brushed DC Control: The BTS7960 43A Driver

For salvaged windshield wiper motors, cordless drill assemblies, power seat screws, and window regulators, standard hobby motor shields (like the antique L298N) will burn out under high-current stall conditions. The **BTS7960 43A H-Bridge module** is the scrapper's gold standard.

```
BTS7960 Module Hookup to Arduino / ESP32:
+-------------------------------------------------------------+
| BTS7960 Pin | Connects To                                   |
| ----------- | --------------------------------------------- |
| VCC         | +5V Logic from Microcontroller                |
| GND         | Ground (Common with Motor PSU Ground)         |
| R_EN + L_EN | +5V (Jumpered together to enable both sides)  |
| RPWM        | Arduino D9 (PWM pin for Forward Speed)        |
| LPWM        | Arduino D10 (PWM pin for Reverse Speed)       |
| B+ / B-     | High-Current 12V/24V Battery or Bench PSU     |
| M+ / M-     | Motor Terminals                                |
+-------------------------------------------------------------+
```

### Arduino Control Code for Heavy DC Motors:
```cpp
// BTS7960 Bi-directional Speed Control
const int RPWM_PIN = 9;  // Forward PWM
const int LPWM_PIN = 10; // Reverse PWM

void setup() {
  pinMode(RPWM_PIN, OUTPUT);
  pinMode(LPWM_PIN, OUTPUT);
}

void driveMotor(int speed) {
  // speed: -255 (Full Reverse) to +255 (Full Forward)
  if (speed > 0) {
    analogWrite(RPWM_PIN, constrain(speed, 0, 255));
    analogWrite(LPWM_PIN, 0);
  } else if (speed < 0) {
    analogWrite(RPWM_PIN, 0);
    analogWrite(LPWM_PIN, constrain(abs(speed), 0, 255));
  } else {
    analogWrite(RPWM_PIN, 0);
    analogWrite(LPWM_PIN, 0); // Active braking
  }
}

void loop() {
  driveMotor(200);   // Forward at ~80% power
  delay(3000);
  driveMotor(0);     // Stop
  delay(1000);
  driveMotor(-200);  // Reverse at ~80% power
  delay(3000);
  driveMotor(0);
  delay(2000);
}
```

---

## 3. Precision Stepper Motor Control: Setting $V_{ref}$ on A4988 / TMC2209

When driving stepper motors salvaged from scanners, printers, and optical drives, **you must calibrate the current-limiting potentiometer on the driver module before applying power**, or the motor windings will overheat and melt.

```
Current Limit Formula for A4988:
  I_max = V_ref / (8 * R_sense)
  
  Rearranging to find target V_ref:
  V_ref = I_max * 8 * R_sense
```
*Note: Typical A4988 boards have $R_{sense} = 0.05\,\Omega$ (marked R050) or $0.1\,\Omega$ (marked R100).*

### Calibration Steps:
1. Power the driver logic with +5V and GND (keep the high-voltage motor supply disconnected).
2. Attach the negative multimeter probe to ground.
3. Touch the positive multimeter probe (using a ceramic screwdriver or crocodile clip on the metal adjustment trimpot) to the metal screw of the trimpot.
4. Slowly rotate the trimpot until the multimeter reads the calculated $V_{ref}$ (typically **0.4V to 0.7V** for small salvaged printer steppers to achieve ~500mA–800mA current limits).

---

## 4. Brushless DC (BLDC) Control: Sensorless ESC vs. Sensored FOC

```
                   [ BLDC Control Spectrum ]
                              |
      +-----------------------+-----------------------+
      |                                               |
  Sensorless RC ESC                                Sensored FOC
  (Hobbywing, SimonK, BLHeli)                     (ODrive, VESC, SimpleFOC)
  - Uses Back-EMF zero-crossing                   - Uses 3 Hall sensors or encoder
  - High RPM applications (fans, turbines)        - Full rated torque from 0 RPM
  - Jitters/stalls at startup                     - Precise angle holding & robotics
```

### Sensorless ESC Driving via Microcontroller:
Sensorless electronic speed controllers treat motor drive signals identically to a standard hobby RC servo:
- **Frequency**: 50 Hz (20 ms period).
- **Pulse Width**:
  - `1.0 ms`: Full Stop / Throttle Zero
  - `1.5 ms`: Half Throttle (or Neutral on bidirectional car ESCs)
  - `2.0 ms`: Full Throttle

```cpp
#include <Servo.h>
Servo esc;

void setup() {
  esc.attach(9); // Connect to ESC signal wire
  
  // Arming sequence for RC ESCs:
  esc.writeMicroseconds(1000); // Send zero throttle
  delay(2000);                 // Wait for initialization beeps
}

void loop() {
  esc.writeMicroseconds(1300); // Spin up to ~30% RPM
  delay(5000);
  esc.writeMicroseconds(1600); // Accelerate to ~60% RPM
  delay(5000);
}
```

---

## 5. High-Voltage PMDC Treadmill Motor Control

Salvaged treadmill motors operate at **90V to 180V DC**. Driving them safely requires dedicated high-voltage rectifying drives.

```
KBIC / KBMM SCR Drive Wiring Topology:
+-------------------------------------------------------------------------+
| AC Mains (120V/240V) ---> [ KBIC L1 & L2 Inputs ]                       |
|                                 |                                       |
|                                 v                                       |
|                  [ Plug-in Horsepower Resistor ]                        |
|                                 |                                       |
|                                 v                                       |
| Motor Armature A+ / A- <--- [ Rectified DC Output ]                     |
|                                 |                                       |
| Speed Control Potentiometer <-- [ P1, P2, P3 Terminals ]                |
+-------------------------------------------------------------------------+
```

### Why KBIC Beats Cheap Digital PWM:
- **Armature Feedback (IR Compensation)**: The KBIC drive continuously senses the back-EMF voltage produced by the treadmill motor. When you push a heavy steel rod into a lathe chuck or press a knife blade into a belt grinder, the motor slows slightly; the drive instantly compensates by increasing firing angle to maintain **rock-solid spindle speed under load**.
- **Adjustable Current Limit (CL)**: Prevents throwing your household circuit breaker or snapping cutting tools if a mechanical jam occurs.

---

## 6. AC Universal Motor Control with Closed-Loop TDA1085

Salvaged washing machine universal motors spin at 12,000 RPM [TYPICAL]. A simple wall-dimmer TRIAC circuit will stall completely under mechanical load.

```
Closed-Loop TDA1085 Architecture:
  [Speed Potentiometer] ------------------+
                                          |
  [TDA1085 Processor Chip] ===(Phase Pulse)===> [Heavy BTA41 TRIAC] ===> [Universal Motor]
           ^                                                                   |
           |                                                                   v
           +=================(Real-time RPM Feedback)================ [Rear Tacho Coil]
```

- **The Function**: The chip compares the requested speed with the actual pulse frequency from the motor's rear tacho-generator.
- **The Result**: You can set the motor to turn at an ultra-slow 200 RPM [TYPICAL], and when you grab the shaft with a gloved hand, the chip feeds maximum current to preserve exact rotation without stalling.

---

## 7. Dual-Wound Solenoid "Pull-and-Hold" PWM Economics

Electromechanical solenoids (harvested from pinball machine flippers, automotive starter relays, door chimes, and diesel fuel cutoff valves) obey fundamental electromagnetic air-gap physics:

```
            Magnetic Pull Force vs. Plunger Position:
            Force
              ^
              |         *  <=== Air Gap Closed (x ≈ 0): Minimal Hold Current Needed!
              |        *
              |       *
              |      *
              |    *
              |  *      <=== Plunger Extended (Large x): Massive Inrush Pull Needed!
              +-----------------------------> Air Gap Distance (x)
```

### A. The Inverse-Square Air Gap Law
The magnetic attractive force generated by an iron core solenoid is roughly governed by:
$$F \approx \frac{(N \cdot I)^2 \cdot \mu_0 \cdot A}{2 \cdot x^2}$$ [CALCULATED]
Where:
- $N \cdot I$ = Ampere-turns (Coil current $\times$ wire turns)
- $x$ = Air gap distance between the plunger and internal stop

When the plunger is fully extended ($x = 15\text{ mm}$), the magnetic air gap has enormous magnetic reluctance. To generate enough initial snap force to pull the mechanism in, the coil must draw heavy current (e.g., $15\text{A}$ at $24\text{V} = 360\text{ Watts}$). 
However, once the plunger seats against the internal iron pole face ($x \approx 0$), the magnetic reluctance drops to near zero. A tiny fraction of that current (e.g., $0.5\text{A} = 12\text{ Watts}$) will hold the plunger seated with identical mechanical holding force!

### B. The Overheating Trap vs. The Overdrive-and-Hold Exploit
If you power a high-pull solenoid continuously at full voltage, its thin copper windings overheat, melt the enamel insulation, and burn out in under 2 minutes.

By utilizing an N-channel logic-level MOSFET (e.g., IRLB8721 or IRFZ44N) driven by an Arduino or 555 timer:
1. **The Overdrive Snap Phase (0 to 40 ms)**: Apply **100% duty cycle at 24V–36V DC [TYPICAL]** to a standard 12V solenoid for exactly **30 to 40 milliseconds**. This generates an explosive, high-acceleration mechanical punch (300% rated force) to overcome static friction and inertia.
2. **The PWM Hold Phase (40 ms to $\infty$)**: Immediately throttle the PWM signal down to **15% to 20% duty cycle** at 20 kHz. 
3. **The Result**: The coil consumes less than $1/5\text{th}$ of its rated thermal wattage, running cool to the touch indefinitely while maintaining maximum holding clamp force.

```cpp
// High-Speed Overdrive Pull-and-Hold Driver
const int SOLENOID_PIN = 3; // PWM Output to Gate of N-Channel MOSFET

void fireSolenoid() {
  analogWrite(SOLENOID_PIN, 255); // 100% Duty Cycle: Maximum Magnetic Pull!
  delay(35);                      // Hold full voltage for 35 ms to seat plunger
  analogWrite(SOLENOID_PIN, 45);  // Throttle to ~18% PWM: Cold, Indefinite Hold
}

void releaseSolenoid() {
  analogWrite(SOLENOID_PIN, 0);   // De-energize coil: Spring returns plunger
}
```

*Note: Always install an ultra-fast high-current Schottky freewheeling diode (e.g., MBR20100CT) directly across the solenoid coil terminals to clamp the colossal inductive flyback spike when the MOSFET switches off!*
