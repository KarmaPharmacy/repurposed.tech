# 🔍 Volume 0.2: Motor Identification & Benchtop Diagnostics
*A systematic field guide to reverse-engineering mystery motors salvaged from unknown scrap.*

---

## 1. The Scrapper's Wire-Count Diagnostic Tree

When pulling a motor from an unlabelled housing, the wire count exiting the motor frame is your first and most reliable diagnostic indicator.

```
                          [ COUNT EXTRACTED WIRES ]
                                      |
         +----------------------------+----------------------------+
         |                            |                            |
      2 WIRES                      3 WIRES                      4 WIRES
         |                            |                            |
  [Brushed DC or AC]           [3-Phase BLDC,               [Bipolar Stepper or
  - Commutator / Brushes?       AC Cap-Run Induction,        Independent Dual Coil]
  - Permanent Magnet = DC       or Split-Phase AC]          - 2 distinct isolated
  - Field Windings = Universal                              circuits with equal Ω
         |                            |                            |
         +----------------------------+----------------------------+
         |                                                         |
      5 WIRES                                                   6 WIRES
         |                                                         |
  [Unipolar Stepper]                                        [Unipolar Stepper with
  - 1 Common Wire                                            Two Center Taps or
  - 4 Coil Leads (Equal Ω to Common)                         Split Bipolar Coils]
         |                                                         |
         +---------------------------------------------------------+
         |
      8+ WIRES
         |
  [BLDC with Hall Sensors: 3 Heavy Phases + 5 Thin Signal Wires]
  OR [8-Wire Universal Stepper: 4 Independent Coils]
```

---


### Bench Triage Protocol for `[UNKNOWN]` Donor Motors

When salvaging a bare motor with missing placards, cut harnesses, or unknown windings:
1. **Initial State Assessment (`[UNKNOWN]`)**:
   - Do NOT apply mains or DC bus voltage.
   - Mark motor status: `[UNKNOWN]` pinout, `[UNKNOWN]` operating voltage, `[UNKNOWN]` insulation integrity.
2. **Phase Topology & Resistance Mapping (`[VERIFIED]`)**:
   - Use a 4-wire Kelvin digital micro-ohmmeter to measure terminal-to-terminal resistance across all wire pairs.
   - For 3-phase BLDC/PMSM: All three phase-to-phase pairs ($U-V, V-W, W-U$) must match within $\le 2.0\%$ `[TYPICAL]`.
   - Any reading $> 5.0\%$ variance indicates shorted turns or inter-layer winding breakdown (`REJECT`).
3. **Dielectric Insulation Breakdown Test (`[VERIFIED]`)**:
   - Apply $500\,\text{V}$ DC from an insulation resistance tester (Megohmmeter) between each phase lead and the grounded stator lamination stack.
   - Minimum acceptable resistance: $> 10.0\,\text{M}\Omega$ `[VERIFIED]`.
   - Readings $< 1.0\,\text{M}\Omega$ indicate moisture ingress, carbonized varnish, or dielectric puncture (`UNSAFE FOR MAINS`).
4. **Dyno Chuck-Spin Test for Velocity Constant $K_v$ (`[CALCULATED]`)**:
   - Chuck motor into a known-speed drill press at $1,200\,\text{RPM}$ `[TYPICAL]`.
   - Measure line-to-line AC peak voltage ($V_{\text{pk}}$) on an oscilloscope.
   - Calculate: $K_v = \frac{\text{RPM}}{V_{\text{pk}}}$ `[CALCULATED]`.

---

## 2. In-Depth Diagnostics by Motor Category

### A. Two-Wire Motors: Brushed DC vs. Universal AC/DC vs. Shaded-Pole AC

```
          Commutator & Brush Identification:
          
             [ Carbon Brush ] ----> [ + ]
                    |
                    v
             [/// COMMUTATOR ///] === (Rotating Armature)
                    ^
                    |
             [ Carbon Brush ] ----> [ - ]
```

1. **Permanent Magnet Brushed DC (PMDC)**:
   - *Physical Clues*: Strong magnetic resistance (cogging) when spinning the shaft by hand. Two access caps for carbon brushes on opposite sides of the rear bell.
   - *Multimeter Test*: Measures low resistance (typically 0.5 Ω to 20 Ω across terminals).
   - *Back-EMF Test*: Connect your multimeter set to **DC Volts** across the two wires. Spin the shaft sharply with your fingers. The meter will read a positive or negative DC voltage spike depending on spin direction.
   - *Reversibility*: Swap positive and negative voltage leads to reverse rotation direction instantly.
   - *Found In*: Cordless power tools, automotive wipers, window regulators, treadmill motors, RC cars, computer cooling fans (note: PC fans have internal brushless driver chips—see below).

2. **AC/DC Universal Motor (Series Wound)**:
   - *Physical Clues*: Carbon brushes present, but the stator has copper wire windings (field coils) instead of permanent magnets. Virtually zero magnetic cogging when spun by hand.
   - *Multimeter Test*: Low resistance (1 Ω to 15 Ω).
   - *Operating Nature*: Operates on either AC or DC current. The armature and stator windings are connected in series.
   - *Speed Nature*: Extremely high speed (10,000 to 25,000 RPM [TYPICAL]) with screaming noise under no-load. Will run away to destruction if not loaded or controlled.
   - *Found In*: Vacuum cleaners, blenders, routers, circular saws, angle grinders, older front-load washing machines.

3. **Shaded-Pole AC Induction Motor**:
   - *Physical Clues*: Only 2 wires exiting. Solid laminated iron stator stack with single AC coil. Prominent heavy copper rings embedded into one corner of each stator pole shoe (the "shading coils"). No brushes, no magnets, completely smooth rotor spin.
   - *Multimeter Test*: 10 Ω to 150 Ω resistance.
   - *Operating Nature*: Strictly single-phase AC mains (120V or 230V). Unidirectional rotation determined permanently by the physical placement of the copper shading rings.
   - *Found In*: Bathroom exhaust fans, microwave blower fans, old phonographs, refrigerator evaporator fans.

---

### B. Three-Wire Motors: 3-Phase BLDC vs. Single-Phase AC Capacitor-Run

```
3-Wire Resistance Test Matrix:
  Test across Pin 1-2, Pin 2-3, Pin 1-3.
  
  Condition A (BLDC):
    R(1-2) == R(2-3) == R(1-3)  [All Equal Low Resistance, e.g. 1.2 Ω]
    -> 3-Phase Brushless Motor (Star or Delta)
    
  Condition B (AC Capacitor-Run):
    R(Common-Run) = Low Ω (e.g., 20 Ω)
    R(Common-Start) = Higher Ω (e.g., 45 Ω)
    R(Run-Start) = Sum of Both (e.g., 65 Ω)
    -> Single-Phase Induction Motor requiring Run Capacitor
```

1. **3-Phase Brushless DC (BLDC) / PMSM**:
   - *Resistance*: Exactly identical resistance across all three wire combinations (typically 0.1 Ω to 10 Ω depending on power rating).
   - *Back-EMF Test*: Set DMM to **AC Volts**. Spin the shaft. Any pair of wires will generate clean AC sinusoidal voltage. Shorting all three wires together produces intense, smooth magnetic braking resistance.
   - *Found In*: Drone motors, hard drive spindles, optical drive spindles, hoverboards, washing machine direct drives.

2. **Single-Phase AC Induction (Capacitor-Run / PSC)**:
   - *Resistance*: One wire is Common (Neutral). The other two are Run winding and Start winding.
   - *Wiring*: Run capacitor (typically 5 µF to 30 µF, 370V AC rated) connects between Run and Start leads. AC Live connects to Run; AC Neutral connects to Common. Reversing which side of the capacitor connects to Live reverses motor direction.
   - *Found In*: Ceiling fans, garage door openers, HVAC blower fans, washing machine drain pumps.

---

### C. Four, Five & Six-Wire Motors: Stepper Motors

```
Bipolar (4-Wire):               Unipolar (5-Wire):              Unipolar (6-Wire):
   Coil A1 o---/\/\/\---o A2         Coil 1 o---/\/\/\---+            Coil A1 o---/\/\/\---o Center A
                                                         |                           |
   Coil B1 o---/\/\/\---o B2         Coil 2 o---/\/\/\---+---o Common                o---/\/\/\---o A2
                                                         |
                                     Coil 3 o---/\/\/\---+            Coil B1 o---/\/\/\---o Center B
                                                         |                           |
                                     Coil 4 o---/\/\/\---+                           o---/\/\/\---o B2
```

1. **4-Wire Bipolar Stepper**:
   - Contains two electrically isolated coils (Coil A and Coil B).
   - *Diagnostic Test*: Use a continuity beeper. Touch probe 1 to wire 1. Find the one matching wire that beeps (Coil A). The remaining two wires will beep together (Coil B). There should be infinite resistance between Coil A and Coil B.
   - *Phase Check*: Twist the two wires of Coil A together. The motor shaft will instantly become hard to turn by hand (dynamic braking). Untwisting them frees the shaft.

2. **5-Wire Unipolar Stepper**:
   - Contains four coils sharing one common center-tap wire connected internally.
   - *Diagnostic Test*: Measure resistance between all 10 possible wire pairs.
   - *Result*: The **Common wire** is the unique wire that shows resistance $R$ to all four other wires. Any two non-common wires will show exactly $2 \times R$ between each other!

3. **6-Wire Stepper (Universal)**:
   - Contains two independent coils, each with a center-tap wire brought outside.
   - *Flexibility*: Can be used as a unipolar motor (connecting center taps to VCC) or converted into a higher-torque bipolar motor by simply **taping off and ignoring the two center-tap wires**.

---

### D. Eight-Wire Motors: BLDC with Hall Effect Sensors

When you salvage a hoverboard hub motor, e-bike motor, or high-end robotics servo, you will find 8 wires exiting the hollow axle:

```
+-----------------------------------------------------------------------+
| 8-Wire BLDC Pinout Classification:                                    |
|                                                                       |
| 3 Heavy-Gauge Wires (Power Phases):                                   |
|   - Phase U (often Yellow)                                            |
|   - Phase V (often Green)                                             |
|   - Phase W (often Blue)                                              |
|                                                                       |
| 5 Thin Signal Wires (Hall Sensors):                                   |
|   - Sensor VCC (+5V DC, often Red)                                    |
|   - Sensor Ground (GND, often Black)                                  |
|   - Hall Sensor A (Signal, often Yellow)                              |
|   - Hall Sensor B (Signal, often Green)                               |
|   - Hall Sensor C (Signal, often Blue)                                |
+-----------------------------------------------------------------------+
```

#### Benchtop Hall Sensor Verification:
1. Connect +5V DC regulated power supply to Sensor Red (+5V) and Sensor Black (GND).
2. Connect a 10 kΩ pull-up resistor from each signal wire (Yellow, Green, Blue) to +5V (Hall sensors are open-collector outputs).
3. Connect your multimeter (DC Volts) between GND and one signal wire.
4. Slowly rotate the motor shaft by hand. The voltage will toggle crisply between **0V and 5V** as the rotor magnets pass each internal Hall sensor chip.

---

## 3. Quantitative Back-EMF $K_v$ and Torque Constant ($K_t$) Derivation

When salvaging unlabelled BLDC, PMSM, or PMDC motors (from hoverboards, power tools, washing machines, or drones), you must determine the motor's **Velocity Constant ($K_v$)** and **Torque Constant ($K_t$)** to select the correct battery voltage, gear reduction, and motor controller.

### A. The Chuck-Spin Dyno Test Setup

```
 [ Variable Speed Drill ] ===(Rigid Shaft Coupler)=== [ Mystery Motor [UNKNOWN] Under Test ]
       |                                                         |
  Fixed Speed RPM                                         Phase A o------+  (Multimeter AC Volts
  (e.g., 1,500 RPM [TYPICAL] via Strobe App)                                       |   or Oscilloscope)
                                                          Phase B o------+
```

1. **Coupling**: Chuck the mystery motor [UNKNOWN] shaft into a cordless drill press or hand drill using a flexible spider or rubber tubing coupler.
2. **Speed Calibration**: Lock the drill trigger and determine the exact shaft speed ($\text{RPM}$) using an optical tachometer, a reflective laser pickup, or a smartphone audio/strobe tachometer app (e.g., *Strobe RPM* or acoustic FFT) targeting a piece of white tape on the chuck. Standard high-gear cordless drills spin at $1,200\text{ to }1,800\text{ RPM}$.
3. **Voltage Measurement**:
   - For **3-Phase BLDC/PMSM**: Connect DMM test leads set to **AC Volts RMS** (or an oscilloscope) across any two phase wires (Phase A to Phase B).
   - For **Brushed PMDC**: Connect DMM leads set to **DC Volts** across the two motor brush terminals.

### B. Mathematical Derivation of $K_v$

For a 3-phase BLDC, calculate the peak phase-to-phase back-EMF voltage ($V_{\text{peak}}$):
- From AC RMS reading: $V_{\text{peak}} = V_{\text{RMS}} \times \sqrt{2} \approx V_{\text{RMS}} \times 1.414$
- From Oscilloscope: $V_{\text{peak}} = \frac{V_{\text{p-p}}}{2}$

The motor's **Velocity Constant ($K_v$)** in $\text{RPM per Volt}$ is:
$$K_v \approx \frac{\text{RPM}}{V_{\text{peak}}}$$ [CALCULATED]

*Worked Example:*
- Drill spinning at $1,500\text{ RPM}$.
- Multimeter reads $10.6\text{ V}_{\text{RMS}}$ AC across two phases.
- $V_{\text{peak}} = 10.6 \times 1.414 = 15.0\text{ V}$.
- $K_v = \frac{1,500\text{ RPM}}{15.0\text{ V}} = 100\text{ RPM/Volt}$.
- This informs you that at a $36\text{V}$ nominal battery pack, the motor's theoretical no-load speed will be: $36\text{ V} \times 100\text{ RPM/V} = 3,600\text{ RPM}$.

### C. Mathematical Derivation of the Torque Constant ($K_t$)

In electromechanical physics, mechanical power ($\text{Power}_{\text{mech}} = \tau \times \omega$) must equal electrical power ($\text{Power}_{\text{elec}} = V \times I$) in an ideal lossless motor:
$$\tau \times \omega = V \times I$$ [CALCULATED]
Where:
- $\tau$ = Torque ($\text{Newton-meters, Nm}$)
- $\omega$ = Rotational velocity ($\text{radians/second}$)
- $V$ = Back-EMF ($\text{Volts}$)
- $I$ = Phase current ($\text{Amperes}$)

Because $\omega = \text{RPM} \times \frac{2\pi}{60}$ and $V = \frac{\text{RPM}}{K_v}$, substituting into the equation yields the universal constant relating torque and back-EMF:
$$\tau = I \times \left( \frac{60}{2\pi \cdot K_v} \right)$$ [CALCULATED]

Therefore, the **Torque Constant ($K_t$)** in $\text{Nm per Ampere}$ is:
$$K_t = \frac{60}{2\pi \cdot K_v} \approx \frac{9.5493}{K_v}$$ [CALCULATED]

### D. Predicting Stall Torque Before Building
Using the $K_v = 100\text{ RPM/V}$ motor evaluated above:
$$K_t = \frac{9.55}{100} = 0.0955\text{ Nm/Amp}$$ [CALCULATED]

- If driven by a salvaged $20\text{A}$ e-bike/VESC speed controller:
  $$\tau_{\text{peak}} = 20\text{ A} \times 0.0955\text{ Nm/A} = 1.91\text{ Nm of torque}$$ [CALCULATED]
- If mated to a $10:1$ planetary gearbox with $85\%$ efficiency:
  $$\tau_{\text{output}} = 1.91 \times 10 \times 0.85 = 16.2\text{ Nm of usable shaft torque}$$ [CALCULATED]

This simple 2-minute bench test allows a builder to characterize any unlabeled scrap motor without manufacturer datasheets.

---

## 4. The Inductance Bridge ($L_d / L_q$) Salience Test for IPM Motors

Modern traction motors harvested from hybrid/electric vehicles (Toyota Prius transaxles, Nissan Leaf, Chevy Volt) and high-efficiency washing machines (LG Inverter Direct Drive) are rarely simple Surface Permanent Magnet (SPM) motors. Instead, they are engineered as **Interior Permanent Magnet (IPM)** machines.

```
Surface Permanent Magnet (SPM):        Interior Permanent Magnet (IPM):
   [ NdFeB Magnets on Surface ]           [ Magnets Buried Inside Steel Core ]
        (L_d ≈ L_q = Uniform)                  (L_q > L_d : Magnetic Salience!)

        +-----------------+                    +-----------------+
        |  [N]  [S]  [N]  |                    |   / \     / \   |
        |  === Rotor ===  |                    |  [N] \   [S] \  |
        +-----------------+                    +-----------------+
```

### A. The Magnetic Salience Physics
- In SPM motors (hoverboard hubs, drone outrunners), magnets are glued to the rotor perimeter. Because rare-earth magnets have a magnetic permeability nearly identical to vacuum/air ($\mu_r \approx 1.05$), the magnetic reluctance is identical regardless of rotor angle. Therefore, **Direct-axis inductance ($L_d$) equals Quadrature-axis inductance ($L_q$)**.
- In IPM motors, rectangular neodymium magnets are buried deep inside stamped silicon steel laminations in V-shaped or tangential slots. 
  - Magnetic flux along the magnet axis encounters the low permeability of the magnet ($L_d$ is low).
  - Magnetic flux along the iron ribs between magnets encounters high-permeability steel ($L_q$ is high).
  - Consequently, IPM motors exhibit **Magnetic Salience**: $L_q$ is typically **30% to 50% larger than $L_d$**.

### B. The Handheld LCR Meter Diagnostic SOP:
1. Connect an inexpensive handheld LCR meter set to **Inductance ($L$) at 1 kHz** across two phase leads (Phase A and Phase B).
2. Slowly rotate the motor shaft by hand through one mechanical revolution.
3. Observe the meter display:
   - **SPM Motor**: Inductance stays virtually flat with less than $\pm 5\%$ fluctuation.
   - **IPM Motor**: Inductance oscillates smoothly in a pronounced sinusoidal wave between minimum ($L_{\text{min}} = L_d$) and maximum ($L_{\text{max}} = L_q$).

### C. The Payoff: Unlocking Free Reluctance Torque via MTPA
Total electromagnetic torque in an IPM motor is the sum of permanent magnet torque plus **Reluctance Torque**:
$$\tau = \frac{3}{2} p \left[ \lambda_m i_q + (L_d - L_q) i_d i_q \right]$$ [CALCULATED]
Where:
- $p$ = Pole pair count
- $\lambda_m$ = Magnet flux linkage
- $i_q$ = Torque-producing quadrature current
- $i_d$ = Direct-axis flux-weakening current

When configuring advanced Field-Oriented Control (FOC) firmware on open-source controllers like **VESC** or **ODrive**:
- Normal SPM mode only applies positive $q$-axis current ($i_d = 0$).
- Enabling **MTPA (Maximum Torque Per Ampere)** algorithm causes the controller to inject a calculated negative $d$-axis current ($i_d < 0$).
- Because $(L_d - L_q)$ is negative, multiplying by negative $i_d$ creates **positive reluctance torque**!
- **Result**: You gain **20% to 35% higher stall torque and improved acceleration** from the exact same motor and battery pack without drawing an extra milliwatt of power or overheating windings!

---

## 5. The "Shorted-Turn" Ring-Down Test (Flyback Q-Factor Check)

The most insidious failure in salvaged electric motors, rewound transformers, and vehicle alternators is a **single shorted internal turn**. 

```
 Healthy Winding Ring-Down:               Winding with ONE Shorted Turn:
 Voltage                                  Voltage
   ^                                        ^
   |  /\                                    |  /\
   | /  \  /\                               | /  \
   0+----+---+--/\--/\---\---\---> Time     0+----+-------------> Time (Dead in 1 cycle!)
   |      \/  \/  \/  \---\---/             |      \/
   | (High Q: 8-15 Clean Oscillations)      | (Shorted turn acts as an eddy-brake!)
```

### A. The Multimeter Blind Spot:
In a motor stator winding consisting of 400 turns with a total DC resistance of $1.500\ \Omega$:
- If physical vibration or heat chafes the enamel insulation between turn 210 and turn 211, those two adjacent wires fuse together.
- The DC resistance drops by $1/400\text{th}$, from $1.500\ \Omega$ to $1.496\ \Omega$—a tiny $0.26\%$ shift that is completely invisible to a standard digital multimeter.
- However, the moment you connect that motor to a high-frequency PWM controller or AC mains, that single shorted turn acts as a **closed transformer secondary**. Intense magnetic flux induces tens of Amperes of circulating current inside that single copper loop, heating it to $400^\circ\text{C}$ in seconds, burning out the motor.

### B. The Resonant Ring-Down SOP:
1. **The Circuit**: Connect a healthy **$0.47\ \mu\text{F}\text{ to }1.0\ \mu\text{F}$ 250V metallized polypropylene (MKP) capacitor** in parallel with the mystery motor [UNKNOWN] phase winding.
2. **The Instrument**: Connect a budget oscilloscope (even a $25 DSO138 or handheld pocket scope) across the LC tank.
3. **The Pulse**: Touch a common 9V transistor battery momentarily across the parallel LC tank and release it (or use an Arduino digital pin through an NPN transistor to inject a 1-millisecond 5V pulse).
4. **Diagnostic Triage**:
   - **Healthy Phase**: The sudden pulse charges the tank, which rings down naturally at its resonant frequency ($f = \frac{1}{2\pi \sqrt{LC}}$). The screen displays a **smooth, beautiful decaying envelope of 8 to 15 sinusoidal waves**.
   - **Shorted-Turn Phase**: The shorted loop dissipates the stored magnetic field instantaneously through internal short-circuit resistance. The wave **flattens dead in 1 to 2 oscillations**.
5. **Phase Comparison**: Compare Phase U-V, V-W, and W-U. If two pairs ring for 12 cycles and the third pair dies in 1 cycle, the stator has internal insulation breakdown and must be rewound or rejected before you waste time building a machine around it!


---

## 7. The Inversion Exploit: Stepper Motor as a Rugged 800-CPR Quadrature Machine DRO & Absolute Resolver

Standard machine shop wisdom treats stepper motors exclusively as actuators: the microcontroller commands the driver, and the rotor turns. Inverting this relationship yields an extraordinary salvage exploit: **a scrap hybrid stepper motor is physically identical to a brushless two-phase resolver and high-resolution quadrature rotary encoder**.

```
  TURNING THE ACTUATOR INTO THE SENSOR:
  Mechanical Shaft Rotation ----> [NEMA 17/23 Stepper Motor]
                                        | Phase A: V_0 * sin(50 * theta)
                                        | Phase B: V_0 * cos(50 * theta)
                                        v
                            [LM393 Dual Comparator / Schmitt Trigger]
                                        |
               +------------------------+------------------------+
               | Channel A (TTL Square)                          | Channel B (TTL Square - 90 deg phase lead)
               v                                                 v
  [ESP32 / Arduino Hardware Pulse Counter] ----> 800 Quad Counts/Rev (0.45 deg resolution)
                                                 Completely immune to cutting oil & swarf!
```

### A. The Mechanical & Magnetic Physics
1. **Tooth Count Multiplier**: A standard $1.8^\circ$ NEMA 17 or NEMA 23 stepper contains a permanent-magnet rotor capped with two soft-iron cups, each ground with **50 teeth**. The stator possesses 8 salient poles with tooth pitches offset by $1/4$ tooth pitch between phases.
2. **True Quadrature Generation**: When you rotate the motor shaft externally, the teeth modulating the magnetic air gap induce sinusoidal back-EMF in the two stator windings:
   $$V_A(t) = K_e \cdot \omega \cdot \sin(50 \cdot \theta)$$ [CALCULATED]
   $$V_B(t) = K_e \cdot \omega \cdot \cos(50 \cdot \theta)$$ [CALCULATED]
   Because the winding geometries are mechanically displaced by 90 electrical degrees, $V_A$ and $V_B$ are in **perfect mathematical quadrature**.
3. **Native Resolution**: One full physical rotation produces exactly 50 electrical sine-wave cycles per phase. Passing both channels through a quadrature decoder (evaluating both rising and falling edges of channels A and B) yields:
   $$\text{Resolution} = 50 \text{ cycles} \times 4 \text{ quadrature states} = 200 \text{ pulses/rev} \times 4 = 800 \text{ Counts Per Revolution (CPR)}$$ [CALCULATED]
   This provides an angular resolution of $360^\circ / 800 = 0.45^\circ$ ($27\text{ arcminutes}$). When coupled to a $2\text{ mm}$ pitch lathe leadscrew, this delivers **$2.5\ \mu\text{m}$ ($0.0001"$) linear positioning feedback**.

### B. The Zero-Oil-Failure Circuitry (Conditioning the Winding Output)
Optical encoder disks fail catastrophically inside machine tools when flood coolant, mineral cutting oil, or hot metal swarf splashes onto the glass wheel or phototransistor. A sealed NEMA 23 stepper with shielded ball bearings is totally immune to swarf, oil, and dust.

```
       Phase A (+) ---[ 10k ]---+-------------------(+) Pin 3 (LM393)
                                |
                             [ 0.1uF ]  Filter       (-) Pin 2 ----+--[ 100k ]--+-- VCC (5V)
                                |                                  |            |
       Phase A (-) -------------+-- GND                           [10k]        [10k]
                                                                   |            |
                                                                  GND       Pin 1 Out (Channel A TTL)
```

1. **Passive Snubber & Anti-Aliasing**: Wire a $10\text{ k}\Omega$ resistor in series with Phase A(+) and a $0.1\ \mu\text{F}$ film capacitor to ground. This filters high-frequency motor brush noise or external VFD EMI while passing rotational frequencies up to $1\text{ kHz}$ ($1,200\text{ RPM}$).
2. **LM393 Zero-Crossing Detector with Hysteresis**:
   - Feed the filtered Phase A into the non-inverting input of an LM393 comparator.
   - Tie the inverting input to a virtual midpoint reference voltage ($2.5\text{V}$ created via a 10k/10k divider from 5V logic).
   - Add a $1\text{ M}\Omega$ positive-feedback resistor between output (pin 1) and non-inverting input (pin 3) to establish $\pm 25\text{ mV}$ of Schmitt trigger hysteresis, preventing bounce when the machine carriage stops or creeps slowly.
3. **Repeat for Phase B**: Wire the identical circuit for Phase B to pin 5, 6, and 7 of the LM393.
4. **Interface**: Connect Pin 1 (Channel A) and Pin 7 (Channel B) directly to the hardware quadrature encoder counter pins of an ESP32 (`pcnt` peripheral) or STM32 timer.

### C. The Zero-RPM Resolver Exploit (Carrier Wave Modulation)
At speeds below $5\text{ RPM}$, passive induced voltage drops below the millivolt comparator threshold. To convert the stepper into a **true zero-speed absolute resolver**:
1. Inject a continuous **$10\text{ kHz}\text{ to }20\text{ kHz}$, 2.0V peak-to-peak sinusoidal carrier wave** into Phase A using a PWM DAC or signal generator.
2. The rotor teeth act as variable magnetic bridges. The high-frequency flux couples from Phase A into Phase B through the rotor teeth with mutual inductance $M(\theta) = M_0 \sin(50 \theta)$.
3. Demodulate the amplitude of the Phase B carrier signal using a simple diode envelope detector or software synchronous rectifier:
   $$V_{\text{demod}} \propto \sin(50 \cdot \theta)$$ [CALCULATED]
4. The system now reports true static rotor position even when completely stationary, creating an indestructible $0.01\text{ mm}$ machine tool DRO for less than $2 in scrap components!
