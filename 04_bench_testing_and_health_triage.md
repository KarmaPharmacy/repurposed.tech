# 🛠️ Volume 13.4: Bench Testing & Motor Health Triage
*The 4-step go/no-go health check to verify salvaged motors before investing time and money building around them.*

---

## The Golden Rule of Salvage: Test Before You Build

Nothing is more disheartening than spending 20 hours machining custom mounting plates, welding brackets, and wiring controllers, only to flip the power switch and discover the salvaged motor has an internal ground short or burned commutator bar.

```
The 4-Step Bench Triage Workflow:
+-------------------------------------------------------------------------+
| [Step 1: Insulation Resistance to Ground] ---> Must be > 10 Megohms [VERIFIED]     |
| [Step 2: Winding Symmetry & Rotation Resistance] -> Smooth, balanced    |
| [Step 3: Commutator & Brush Visual Inspection] --> Chocolate patina     |
| [Step 4: Acoustic Bearing Spin-Down Test] -------> Zero grumble / play  |
+-------------------------------------------------------------------------+
```

---

## 1. Step 1: Insulation Resistance to Ground (The Short-Circuit Check)

```
Testing for Insulation Breakdown:
  [Multimeter set to Highest Resistance Range (20 MΩ) or Megohmmeter]
         |
         +--- Probe 1: Scratched bare metal on motor frame / casing
         |
         +--- Probe 2: Motor power lead / winding terminal
         
  Target Result: INFINITE RESISTANCE (Open Circuit "OL" or > 10 MΩ)
```

- If your meter reads **under 1.0 MΩ (or beeps on continuity)** between the winding leads and the motor chassis:
  - The magnet wire enamel insulation has burned through or degraded.
  - **Verdict**: The motor is dangerous. In a 120V treadmill motor, powering this will energize your entire lathe or grinder frame with mains AC voltage! Discard or rewire.

---

## 2. Step 2: Winding Resistance & Symmetry Testing

### For 3-Phase Brushless Motors (BLDC / Direct-Drive Stators):
- Measure resistance across all three phase pairs using your lowest DMM range:
  - $R_{1-2}$
  - $R_{2-3}$
  - $R_{1-3}$
- **All three values must match within 2% to 3%** (e.g., $1.21\,\Omega, 1.20\,\Omega, 1.22\,\Omega$).
- If one pair reads significantly lower (e.g., $0.6\,\Omega$), that phase has internal shorted turns and will overheat and shudder under load.

### For Brushed DC Motors (Treadmill, Wiper, Cordless Drill):
- Connect your multimeter across the two motor leads.
- **Slowly turn the output shaft by hand through 360°**:
  - The resistance should remain steady, fluctuating smoothly between adjacent commutator bars.
  - **The Red Flag**: If the resistance spikes to infinite or jumps by $5\times$ as you rotate, you have a **broken armature wire or a burned-out commutator bar**. The motor will develop dead spots where it refuses to start.

---

## 3. Step 3: Commutator & Brush Inspection

```
Commutator Visual Health Guide:
  HEALTHY:
    - Smooth, uniform chocolate-brown or copper patina.
    - Carbon brushes have at least 1/4" (6mm) length remaining.
    - Brush springs exert firm, positive pressure.
    
  FAILED:
    - Blackened, charred, or pitted copper bars.
    - Deep circumferential grooves worn by brushes.
    - Mica insulation protruding above the copper segments.
```

### The Deadly Emery Cloth Mistake:
- **NEVER use emery cloth or sandpaper to clean a dirty commutator.**
- Emery cloth and silicon carbide sandpaper contain conductive, ultra-hard abrasive particles. When rubbed against soft copper bars, microscopic grains become permanently embedded in the copper.
- When powered, these embedded grains act as tiny chisels that rapidly chew up the carbon brushes and cause massive arcing.
- **The Correct Method**: Clean commutators using a piece of **fine maroon Scotch-Brite pad**, or dress the commutator lightly on a lathe using a sharp carbide tool bit, then undercut the mica separators using a modified hacksaw blade.

---

## 4. Step 4: The Acoustic Bearing Spin-Down Test

```
Spin-Down Deceleration Check:
  - Grasp the shaft firmly and shake radially: Must have ZERO detectable play.
  - Give the shaft an aggressive manual spin:
  
  [Healthy Bearings]: 
    - Glides smoothly for 3 to 6 seconds before gently stopping.
    - Produces a smooth, uniform whisper.
    
  [Failed Bearings]:
    - Stops abruptly in under 1 second (dried, hardened grease).
    - Emits a dry, gravelly grumble or high-pitched squeal.
```

### Replacing Bearings from Standard Stock:
Most salvaged appliances and automotive motors utilize standard industrial deep-groove ball bearings that cost **under $2.00 to replace**:
- **608-2RS**: Found in skateboards, optical drives, and small power tools (8mm bore, 22mm OD).
- **6202-2RS**: Found in alternators and washing machines (15mm bore, 35mm OD).
- **6203-2RS**: Found in alternators and treadmill motors (17mm bore, 40mm OD).
- **6205-2RS / 6206-2RS**: Found in washing machine drum spiders (25mm / 30mm bore).
- Use a small mechanical gear puller to draw off the worn bearings. Press the new rubber-sealed (2RS) bearings on by pressing **only against the inner race** with a matching socket.


---

## 5. DIY Stroboscopic Tachometer & Dynamic Vibration Phase Balancer

### A. Non-Contact RPM Measurement & Motion Freezing
Optical laser tachometers require aiming reflective tape at a spinning shaft. A **tunable stroboscopic tachometer** allows you to visually "freeze" spinning shafts, diagnose belt flutter, inspect gear meshing in real time, and determine exact RPM from across the shop:

```
  [ Rotary Encoder / Potentiometer ] ──> [ Arduino Nano ]
                                                │
                                                ▼ (Microsecond Pulses: 20 µs)
                                         [ IRLZ44N MOSFET ]
                                                │
                                                ▼
                                    [ 10W High-Power White LED ]
                                                │
                                                ▼ (Strobe Flashes Freeze Shaft in Mid-Air!)
                                         [ Spinning Spindle ]
```

1. **The Flash Physics**:
   - To freeze a shaft spinning at $6,000\text{ RPM}$ ($100\text{ revolutions/second}$) without motion blur, the flash duration must be extremely short:
     $$t_{\text{flash}} \le 20\text{ to }50\text{ microseconds}$$
   - An ordinary incandescent bulb is too slow; high-power white LEDs (harvested from scrap floodlights or car headlamps) driven by an N-channel logic-level MOSFET switch on and off in nanoseconds.
2. **Determining True Spindle RPM**:
   - Paint a single white chalk dot on the pulley rim.
   - Adjust the potentiometer strobe frequency until the dot appears **completely stationary**.
   - Watch for harmonic sub-multiples: If you see two stationary dots $180^\circ$ apart, your flash rate is running at $2\times$ the true shaft speed. The highest flash rate that shows a **single sharp stationary dot** equals the true fundamental RPM:
     $$\text{RPM} = 60 \times f_{\text{flash}}\text{ (Hz)}$$ [CALCULATED]

### B. Dynamic Vibration Phase Balancer (The HDD Seismometer)
How do you dynamically balance a spinning armature or 2x72 grinder contact wheel without a $10,000 balancing rig?

```
      [ Spinning Rotor Under Test ] ── (Vibration Shake)
                     │
                     ▼
      [ Hard Drive Voice Coil Seismometer Contact Probe ]
                     │
                     ▼ (Generates 50 mV Sine Wave at Peak Displacement)
         [ LM393 Comparator Zero-Cross Trigger ]
                     │
                     ▼
         [ Fires 20 µs LED Strobe Pulse! ]
                     │
                     ▼
      =====> Strobe Freezes the Heavy Spot at its Exact Angular Angle!
```

1. **The Vibration Sensor**:
   - Salvage a voice-coil arm from a scrapped 3.5" hard drive. Mount a blunt brass stylus to the coil arm and rest the tip lightly against the bearing block of the spinning motor.
   - Mechanical vibration causes the voice coil to oscillate inside its neodymium magnet bracket, acting as a sensitive **electrodynamic seismometer** that outputs a sinusoidal AC voltage proportional to vibration velocity.
2. **Phase-Locked Strobe Triggering**:
   - Run the voice coil signal through an LM393 voltage comparator to generate a sharp digital rising-edge pulse at the exact moment of peak vibration excursion.
   - Trigger the LED strobe with this pulse.
3. **Reading the Phase**:
   - Because the strobe flashes only at peak positive acceleration, the rotating reference mark will appear stationary at an angle $\theta$.
   - Mount a small trial clay or set-screw mass at **$180^\circ$ opposite the illuminated mark**. Spin up again: if vibration amplitude drops, refine the balance mass until the seismometer output voltage drops to near-zero!


---

## 6. The Scrap Yard Rapid Alloy ID Checklist (Zero Lab Tools)

In the field at a municipal scrap yard or equipment demolition site, you rarely have an X-ray fluorescence (XRF) alloy spectrometer. This 4-tier physical and chemical triage protocol identifies mystery metals in 30 seconds using everyday pocket tools:

```
                      [Mystery Metal Cutoff]
                                │
               Strong Neodymium Magnet Test:
              ├── YES (Strong Pull) ──► Carbon Steel, Cast Iron, or 400-Series Stainless
              │                         (Differentiate via Spark Grinding Test!)
              │
              └── NO (Weak or Non-Magnetic)
                   │
         Pocket File Scratch Test:
         ├── SOFT / GOUGES EASILY:
         │   ├── Very Heavy / Gray ──► Lead / Babbit Bearing Alloy
         │   ├── Yellowish / Heavy ──► Brass / Bronze (Machinable bushing material)
         │   └── Very Light / Silver ─► Aluminum OR Magnesium
         │                              │
         │           [Vinegar / Citric Acid Drop Test]:
         │           ├── Bubbles vigorously within 15 seconds ──► MAGNESIUM (Fire hazard!)
         │           └── Zero reaction / inert ─────────────────► ALUMINUM (6061 / 7075)
         │
         └── HARD / SLIPS OFF FILE:
              ├── DULL RED / STRAW SPARKS ──► 300-Series Austenitic Stainless (304 / 316)
              └── BRILLIANT SNOW-WHITE   ──► TITANIUM GRADE 5 (Lightweight, laser-straight)
```

### The Vinegar Fizz Test for Magnesium
- Scrap housings from chainsaws, premium laptop chassis, and weed-eaters are frequently cast from **magnesium alloy (AZ91D)** rather than aluminum to save weight.
- While lighter and stiffer than aluminum, magnesium cannot be welded with standard TIG filler, dissolves rapidly in acidic environments, and creates an explosive fire hazard if machined on a lathe without flood coolant.
- **Field Test**: Scrape clean bare metal and place one drop of ordinary household white vinegar (5% acetic acid). Magnesium vigorously effervesces tiny bubbles of hydrogen gas within 10 to 15 seconds; aluminum remains completely inert.

---

## 7. Non-Destructive Shaft & Pulley Extraction (Thermal Shock Engineering)

```
Thermal Shock Differential Extraction:
              [ Propane Torch Flame Directed at Aluminum Hub ]
                                   │
                                   ▼
        +-----------------------------------------------------+
        | Expanding Aluminum Pulley: alpha = 23 x 10^-6 / °C  |
        |                                                     |
        |   (Heat Shield Barrier: Wet Sheet Metal Card)       |
        |                                                     |
        | Shrinking Steel Shaft: Spray with Freeze Spray!     |
        |                        alpha = 12 x 10^-6 / °C      |
        +-----------------------------------------------------+
                                   │
                                   ▼
        =====> 0.002" Press-Fit Clearance Opens Automatically!
               Pops off with light finger pressure on bearing splitter!
```

### Why Claw Pullers Destroy Salvaged Motors:
- Standard 3-jaw claw pullers grab the thin outer rim of cast-iron or aluminum pulleys. Under heavy screw pressure, the brittle outer lip fractures, ruining the pulley, or the drive screw mushrooms the end of the motor shaft, preventing the bearing from ever sliding off.

### The Professional Extraction Protocol:
1. **Never Pull on the Outer Flange**: Always position a **bearing splitter plate** directly behind the solid inner hub of the pulley so pulling force is applied against the mass of the hub face.
2. **Thermal Expansion Differential Physics**:
   $$\Delta L = L_0 \cdot \alpha \cdot \Delta T$$ [CALCULATED]
   Aluminum expands at **$23 \times 10^{-6}\text{ /}^\circ\text{C}$**, while a steel shaft expands at only **$12 \times 10^{-6}\text{ /}^\circ\text{C}$**.
3. **Execution**:
   - Shield the motor front bearing and rubber oil seal with a square of wet cardboard or sheet metal.
   - Play a propane or butane torch flame evenly around the aluminum pulley hub for 45 to 60 seconds until it reaches $\sim 150^\circ\text{C}$ (a drop of water sizzles instantly).
   - Invert an aerosol can of compressed air duster (or spray automotive freeze spray) directly onto the center steel shaft for 10 seconds.
   - The rapid temperature delta ($\Delta T \approx 170^\circ\text{C}$) opens up over **$0.002\text{ inches (0.05 mm)}$ of mechanical clearance**. A light turn of the bearing splitter center bolt pops the pulley off cleanly without galling or bending the shaft.

---

## 8. Brushless Motor Phase & Hall Angle Mapping (60° vs 120° Commutation)

```
3-Phase Hall Commutation Truth Table (120° Phase Spacing):
  +-------------------------------------------------------------+
  | Step | Rotor Angle | Hall A | Hall B | Hall C | Phase Active|
  | :--- | :---        | :---:  | :---:  | :---:  | :---        |
  | 1    | 0° - 60°    | 1      | 0      | 0      | U+ / V-     |
  | 2    | 60° - 120°  | 1      | 1      | 0      | U+ / W-     |
  | 3    | 120° - 180° | 0      | 1      | 0      | V+ / W-     |
  | 4    | 180° - 240° | 0      | 1      | 1      | V+ / U-     |
  | 5    | 240° - 300° | 0      | 0      | 1      | W+ / U-     |
  | 6    | 300° - 360° | 0      | 0      | 1      | W+ / V-     |
  +-------------------------------------------------------------+
  Notice: States '000' and '111' NEVER occur in a healthy 120° sensor!
```

### The 36-Combination Hall Puzzle:
When pairing an unknown salvaged brushless motor (hoverboard hub, washing machine stator, e-bike motor) with a generic brushless controller, matching the 3 heavy phase wires ($U, V, W$) and 3 thin Hall signal wires ($H_a, H_b, H_c$) results in **$3! \times 3! = 36$ possible wiring combinations**.
- Only **6 combinations** produce smooth forward rotation; 6 produce reverse; the remaining 24 combinations cause violent current spikes, motor shudder, or blown MOSFETs.

### The Systematic 5-Minute Solution (The Current-Limited Sweep):
1. **Current-Limit Your Bench Supply**: Set your DC bench power supply to the motor's nominal voltage, but dial the current limit down to **1.0 Amp to 1.5 Amps max**. This completely prevents burning out the controller MOSFETs while testing mismatched combinations.
2. **Lock the Hall Wires**: Connect the 3 Hall wires in any arbitrary order (e.g., Red to $+5\text{V}$, Black to $\text{GND}$, and Yellow/Green/Blue to $H_a, H_b, H_c$). Leave them fixed.
3. **Cycle the 6 Phase Permutations**:
   - Combo 1: Phase $U \to A$, Phase $V \to B$, Phase $W \to C$
   - Combo 2: Phase $U \to A$, Phase $V \to C$, Phase $W \to B$
   - Combo 3: Phase $U \to B$, Phase $V \to A$, Phase $W \to C$
   - Combo 4: Phase $U \to B$, Phase $V \to C$, Phase $W \to A$
   - Combo 5: Phase $U \to C$, Phase $V \to A$, Phase $W \to B$
   - Combo 6: Phase $U \to C$, Phase $V \to B$, Phase $W \to A$
4. **Identify the True Match**:
   - *False combinations*: The motor will growl, vibrate violently, hesitate, or draw the full 1.0A current limit while barely spinning.
   - *The true combination*: The motor spins up instantly, produces a clean, high-frequency acoustic hum, and draws **under 0.35 Amps of no-load idle current**.
   - If the motor spins smoothly but in the wrong direction, simply swap any two Hall sensor wires and repeat the 6-phase sweep.
