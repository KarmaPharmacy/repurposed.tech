# ⚡ Volume 13.3: Electrical Sanity & Power Architecture
*Inrush current mathematics, battery buffering, flyback diode selection, wire gauge sizing, and star grounding.*

---

## 1. The Inrush Current Trap: Why Your Power Supply Shuts Down

A maker hooks a salvaged 12V windshield wiper motor or cordless drill motor to a commercial "12V 10-Amp" desktop switching power supply. The moment the switch is flipped, the power supply's LED blinks, the motor twitches, and the unit immediately shuts down into "hiccup protection mode."

```
Calculating Instantaneous Inrush Current:
  When a motor is stationary (0 RPM), it generates ZERO Back-EMF.
  
  Inrush Current Formula:
    I_inrush = V_supply / R_armature
    
  Example:
    Wiper Motor Armature Resistance R = 0.45 Ohms.
    At 12V DC [TYPICAL]:
    I_inrush = 12V / 0.45 Ohms = 26.6 AMPS!
```

- Although the motor only draws **3 to 4 Amps while running**, it demands **26+ Amps for the first 50 milliseconds** to overcome physical rotor inertia.
- Switching power supplies detect any draw exceeding their 10A current-limit trip point as a dead short circuit and shut down instantly.

---

### The Unwritten Field Fix: The Battery Buffer Topology

```
Battery-Buffered High-Current Power Station:
+-------------------------------------------------------------+
| [12V 10A Switching Power Supply / Wall Charger]             |
|                             |                               |
|          (Supplies 13.8V Float Trickle Charge)              |
|                             |                               |
|                             v                               |
| +=========================================================+ |
| | [Small 12V 7Ah SLA Battery OR 4S LiFePO4 Pack]          | |
| +=========================================================+ |
|                             |                               |
|          (Absorbs 30A - 60A Instantaneous Inrush Spikes!)   |
|                             |                               |
|                             v                               |
| [BTS7960 Motor Driver] ===> [Heavy Salvaged 12V DC [TYPICAL] Motor]   |
+-------------------------------------------------------------+
```

1. Wire a small, inexpensive 12V 7Ah Sealed Lead-Acid (SLA) alarm battery or a 4S LiFePO4 battery pack in **parallel** across your 12V power supply's output terminals.
2. The power supply maintains a constant 13.8V float charge on the battery.
3. When the motor starts or hits a momentary stall load, the chemical battery discharges **30 to 50 Amps instantly** without breaking a sweat, while the power supply recharges the battery between motor cycles.
4. Your power supply will never trip again.

---

## 2. Low-Voltage Wire Gauge Sizing (Voltage Drop Physics)

At 120V AC [TYPICAL] mains, a 2.0 Volt drop over a thin wire is negligible (1.6% loss).
At **12V DC [TYPICAL]**, a 2.0 Volt drop drops operating voltage to 10.0V—a catastrophic **16.7% loss of voltage and a 31% loss of motor power** ($P = V^2 / R$).

```
12V DC [TYPICAL] Wire Sizing Matrix (Target: Less than 3% Voltage Drop over 10 ft):
+-------------------------------------------------------------------------+
| Continuous Current  | Minimum Recommended Wire Gauge  | Typical Application|
| ------------------- | ------------------------------- | ------------------ |
| **0 to 5 Amps**     | 18 AWG                          | Steppers, sensors  |
| **5 to 15 Amps**    | 14 AWG                          | Window regulators  |
| **15 to 30 Amps**   | 10 AWG (Silicone high-strand)   | Wiper motors, drills|
| **30 to 60 Amps**   | 6 AWG or 4 AWG                  | Hoverboard hubs    |
| **60 to 120 Amps**  | 2 AWG or 0 AWG (Welding cable)  | Starter, EPS column|
+-------------------------------------------------------------------------+
```

---

## 3. Flyback Clamping Diodes: Saving Your MOSFETs

Electric motor windings are massive electrical inductors.
When your microcontroller turns off a MOSFET during PWM speed control, the collapsing magnetic field in the motor windings generates an instantaneous reverse voltage spike:
$$V_{\text{spike}} = -L \frac{di}{dt}$$ [CALCULATED]
- This inductive kickback easily reaches **150V to 400V in fractions of a microsecond**, exceeding the breakdown voltage of your driver's MOSFETs and blowing them instantly.

```
Flyback Diode Selection Trap:
  [1N4001 / 1N4007 Standard Diodes]:
    - Reverse Recovery Time: t_rr > 2,000 nanoseconds.
    - FATAL FLAW: At 20 kHz PWM, the diode is too slow to catch the spike!
    
  [Schottky Barrier Diodes (MBR20100CT / SR5100)]:
    - Reverse Recovery Time: t_rr < 30 nanoseconds.
    - Catches ultra-fast inductive transients instantly and runs cool.
```

- **The Rule**: Always wire a high-speed **Schottky diode** (or RC snubber network) directly across the motor's power terminals (Cathode to positive, Anode to negative) when designing custom discrete MOSFET switches.

---

## 4. Star Grounding & Logic Isolation

```
Ground Bounce Reset Phenomenon:
  [Motor High-Current Ground (20A Draw)] ---> (Thin Common Wire) ---> [Arduino GND]
                                                     |
                                        (Generates 0.8V Ground Bounce!)
                                                     |
                         ====> ARDUINO CRASHES & FREEZES REPEATEDLY!
```

### The Star Ground Rule:
High-current motor return currents must never flow through the same physical wire or copper trace as delicate 5V/3.3V microcontroller logic signals.
- **The Protocol**: Designate a single **Solid Copper Star Ground Stud** directly at the negative terminal of your power supply or battery.
- Run dedicated, isolated heavy-gauge ground wires from the motor driver directly back to the star stud.
- Run a separate, dedicated ground wire from the microcontroller to the star stud.
- Noise and ground bounce from motor brush arcing can no longer interfere with microcontroller logic.

---

## 5. The "Dim-Bulb Tester": Current-Limited Mains Bring-Up

Every hardware hacker's workshop must have a **Dim-Bulb Tester** permanently mounted above the electrical test bench. Connecting a newly rewound microwave transformer, an unlabelled treadmill motor controller, or a salvaged switching power supply directly to a 120V/240V wall socket is a recipe for tripped household breakers, vaporized PCB traces, and exploding silicon.

```
       120V AC [TYPICAL] Mains (Hot) o---[ 60W-100W Tungsten Bulb ]---+
                                                            |
                                                            v  (Protected Hot)
                                                   [ Test Outlet / Motor Load ]
                                                            ^
                                                            |  (Direct Neutral)
       120V AC [TYPICAL] Mains (Neutral) o----------------------------+
```

### A. The Non-Linear Tungsten Resistance Principle
A standard incandescent lightbulb filament is made of pure tungsten, which has a positive temperature coefficient of resistance ($\text{PTC}$):
- **Cold Filament**: When no current flows, cold tungsten has very low resistance ($\approx 10\ \Omega$ to $15\ \Omega$).
- **Hot Filament**: When forced to carry current, the filament instantly heats white-hot to $2,500^\circ\text{C}$, causing its electrical resistance to jump by a factor of 10 to over **$140\ \Omega$**.

### B. Diagnostic Triage from Bulb Behavior:
Plug your mystery salvaged device into the test outlet and observe the lamp:

1. **Condition A: Dead Short-Circuit (Blown Bridge Rectifier / Shorted Primary)**:
   - *Bulb Reaction*: Illuminates instantly to **100% full, blinding brightness**.
   - *Why It Saves You*: The tungsten filament absorbs the entire 120V mains voltage drop, strictly limiting current to:
     $$I_{\text{max}} = \frac{100\text{ W}}{120\text{ V}} \approx 0.83\text{ Amperes}$$ [CALCULATED]
     Your shop circuit breaker does not trip, zero sparks fly, and your workbench stays safe.
2. **Condition B: Healthy Power Supply / Healthy Motor**:
   - *Bulb Reaction*: Flashes brightly for a fraction of a second (as large DC-link filter capacitors draw initial inrush), then **dims down to a faint orange filament glow or goes completely dark**.
   - *Meaning*: The power supply has successfully stabilized, capacitors are charged, and standby current is minimal. You may now safely bypass the bulb and run on direct mains.
3. **Condition C: Partial Short / Shorted Motor Winding Turns**:
   - *Bulb Reaction*: Glows steadily at **half brightness** while motor hums or chatters.
   - *Action*: Power off immediately—the transformer or motor has shorted turns that are generating excessive eddy losses.

---

## 6. Industrial Definite Purpose Contactors & Master E-Stop Latching

When building high-energy shop tools (2x72 belt grinders, metal lathes, 5 HP alternator power drives), toggle switches or plastic rocker switches are dangerous. If power flickers or the tool jams, a toggle switch leaves the machine energized, leading to severe injury when power returns.

```
  120V/240V L1 ---[ E-Stop Mushroom (NC) ]---[ Start Button (NO) ]---+---( Contactor Coil )--- L2
                                                   |                |
                                                   +--[ Aux NO ]----+
                                                   (Self-Latching Hold)
```

- **Definite Purpose Contactor**: Use a salvaged **40A double-pole HVAC contactor**. It features massive silver-alloy contacts that will not weld under motor start surges, flanked by internal arc chutes.
- **The Self-Latching Interlock**:
  1. Pressing the momentary green **Start Button (NO)** energizes the 120V/240V coil.
  2. The contactor snaps shut, pulling in an auxiliary normally-open (NO) contact wired in parallel with the Start button.
  3. Releasing the Start button leaves the coil energized through its own auxiliary contact (**self-latched**).
  4. Slapping the large red **Emergency-Stop Mushroom Button (NC)** breaks the control circuit, instantly dropping the contactor and isolating the motor.
  5. **Anti-Restart Protection**: If grid mains power fails for 50 milliseconds, the contactor snaps open and drops the latch. When grid power comes back on, the motor remains completely dead until a human physically presses Start again.
