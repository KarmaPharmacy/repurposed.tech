# ⚙️ Volume 10.5: Cams, Geneva Drives & Intermittent Mechanisms
*Harvesting Maltese cross Geneva drives, ratchet-and-pawl indexers, and barrel cams for pure mechanical automation.*

---

## 1. The Geneva Mechanism (Maltese Cross): Hardware Indexing

```
4-Slot Geneva Drive Geometry:
      [Continuous Drive Wheel]
           |
           +--- [Drive Pin]  <--- Enters slot to advance wheel by 90°
           |
           +--- [Locking Crescent Cam] <--- Glides against concave rim to hold
                                            wheel dead stationary during dwell
                 |
                 v
      [4-Slot Geneva Wheel (Maltese Cross)]
```

### Why Geneva Mechanisms Beat Software Stepper Indexing:
When automating rotary carousels, tool turrets, or packaging lines, programming a stepper motor to start, move, and hold position requires encoders, drivers, microcontrollers, and holding current (which heats up the motor).
- **The Geneva Miracle**: A Geneva drive is powered by a **cheap, single-speed, continuously spinning AC or DC motor**.
- As the drive wheel rotates 360° continuously:
  - For **90° of rotation**, the pin engages a radial slot and smoothly accelerates/decelerates the Geneva wheel to the next station.
  - For the remaining **270° of rotation**, the crescent cam locks the Geneva wheel mechanically rigid in place with **zero holding current and zero sensor drift**.

---

### Step-by-Step Kinematic Design & Scrap Fabrication:
$$\text{Index Angle } \beta = \frac{360^\circ}{n}$$ [CALCULATED]
*(Where $n = \text{number of slots. For a 4-slot wheel, } \beta = 90^\circ; \text{ for a 6-slot wheel, } \beta = 60^\circ$).*

```
Kinematic Parameters:
  - Center Distance (C): Distance between drive wheel axis and Geneva axis.
  - Drive Pin Radius (R_drive) = C * sin(180° / n)
  - Geneva Wheel Radius (R_geneva) = C * cos(180° / n)
```

#### Fabrication from Scrap:
- Laser-cut the Geneva wheel from **1/4" cast acrylic or POM Delrin sheet**, or machine from 6061 aluminum plate.
- Solder or press-fit a roller needle bearing onto the drive wheel to serve as the low-friction drive pin.

#### Repurposing Exploits:
- **CNC Automatic Tool Changer (ATC) Carousel**: Mount an 8-slot Geneva wheel to a carousel holding 8 router collets. Driven by a salvaged 12V wiper motor, a single microswitch pulse advances the carousel exactly one tool position with flawless mechanical repeatability.
- **Automated Multi-Angle Photogrammetry Turret**: Positions an object under a camera in exact 45° or 60° increments, holding rock-steady for a 5-second long exposure before advancing to the next angle.

---

## 2. Cylindrical Barrel Cams: The Secret of Level-Wind Wire Spooling

```
Barrel Cam Reciprocating Guide:
  +-----------------------------------------------------------+
  | [Rotating Cylinder with Endless Diamond / Helical Groove]  |
  |                 |                                         |
  |                 v                                         |
  | [Cam Follower Boat / Dog Pin riding in the groove]        |
  |                 |                                         |
  |                 v                                         |
  | ====> Slides Back and Forth with Constant Velocity!       |
  +-----------------------------------------------------------+
```

### What Makes Barrel Cams Unique:
Standard leadscrews require reversing motor direction with electronic switches when reaching the end of travel.
- An **endless diamond-groove barrel cam** (salvaged from fishing reels, sewing machines, or vintage level-wind spools) features a continuous groove that crosses over itself at each end.
- As the cylinder spins in **one constant direction**, the follower pin glides smoothly from left to right, smoothly reverses at the end-point, and travels back from right to left at continuous constant velocity.

### Repurposing Exploits:
- **Automatic Transformer & Guitar Pickup Wire Winder**:
  - Eliminates the second stepper motor and complex software needed to guide wire evenly across a spool.
  - Couple the barrel cam to the spool drive via a fixed gear ratio: As the coil turns, the cam follower lays down hair-thin magnet wire (42 AWG) in flawless, non-overlapping side-by-side passes across hundreds of layers automatically.

---

## 3. Clockwork Escapements & Governors: Zero-Electricity Autonomous Motion

When electronics, microcontrollers, and batteries cannot survive—such as extreme cryogenic temperatures ($-40^\circ\text{C}$), high-radiation zones, or ultra-long standby periods where battery self-discharge ruins deployments—the ancient art of **mechanical horology** provides unmatched reliability:

```
        +-----------------------------------------------------------+
        | Clockwork Constant-Velocity Power Drive:                  |
        |                                                           |
        | [ Heavy Coiled Mainspring (Dog Leash / Lawnmower Pull) ]  |
        |                            |                              |
        |                            v (Raw Unwinding Torque)       |
        | [ Step-Up Gear Train (1:60 Ratio) ]                       |
        |                            |                              |
        |                            v                              |
        | [ Graham Deadbeat Escape Wheel ] <---> [ Pendulum Pallet ]|
        |                            |                              |
        |                            v                              |
        | ====> Flawless Constant-Velocity Output: Zero Electricity!|
        +-----------------------------------------------------------+
```

### A. Sourcing High-Energy Spiral Power Springs:
- Discarded retractable dog leashes (e.g., Flexi leashes), 30-foot tape measures, and heavy vacuum cleaner cord winders contain **carbon spring steel mainsprings** capable of storing tens of Joules of elastic mechanical energy across 15 to 30 rotations.

### B. The Graham Deadbeat Escapement:
- A laser-cut or 3D-printed **Deadbeat Escapement wheel** and dual-pallet anchor locks and releases the gear train once per pendulum swing.
- Unlike recoil escapements, the deadbeat pallets have concentric resting faces that prevent the gear train from being pushed backward during pallet drop, eliminating gear train chatter and delivering an **absolutely uniform timebase**.

### C. Repurposing Exploits:
1. **Zero-Battery Astronomical Star Tracker (Equatorial Barn-Door Mount)**:
   - Deep-sky astrophotography requires rotating a DSLR camera at the exact sidereal tracking rate ($15.04^\circ\text{ per hour}$) to prevent star trailing.
   - An escapement drive powered by a salvaged dog-leash spring drives the camera platform smoothly for **over 2 hours on a single wind**—completely eliminating battery cold-drain during freezing winter nights!
2. **Sub-Zero Arctic Time-Lapse Trigger**:
   - Drops an mechanical shutter release every 15 minutes across weeks of polar deployment where lithium batteries would freeze and die within 4 hours.

---

## 4. EMP-Proof Mechanical Machine State Loggers

When operating high-energy experimental machinery—such as 2,000W induction forges, high-voltage MOT pulse spot welders, or capacitor-discharge metal vaporizers—electromagnetic interference (EMI) and radio frequency spikes frequently corrupt microcontroller flash memory, freeze I2C buses, and scramble digital OLED displays.

```
       [ Machine Axis Lead Screw / Spindle ]
                         |
                         v (100:1 Worm Reduction)
       [ Geneva 10-Position Indexing Wheel ]
                         |
                         v
       [ Mechanical 5-Digit Brass / Nylon Odometer Tumbler Wheels ]
       (Tracks 100,000 Cycles with ZERO Silicon & 100% EMP Immunity!)
```

- **Harvested Donors**: Mechanical residential water meters, gas flow meters, and vintage automobile analog instrument clusters.
- **The Construction**:
  - Connect the input shaft through a 100:1 worm reduction directly to the machine's primary moving gantry, punch press eccentric, or grinder arm.
  - Each rotation of the worm drives a single-pin Geneva wheel, advancing the lowest tumbler drum by exactly one digit ($0\text{ to }9$).
  - A pin at the $9\rightarrow 0$ transition indexes the next higher drum.
- **The Payoff**:
  - Automatically records operational machine runtime hours, cycle counts, and tool wear life in physical stamped brass/nylon wheels.
  - Immune to direct lightning strikes, multi-kilovolt arcs, RF interference, and utility brownouts. If power fails mid-cycle, the mechanical state log remains 100% accurate down to the exact stroke.
