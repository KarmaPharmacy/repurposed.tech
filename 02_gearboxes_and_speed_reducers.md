# ⚙️ Volume 10.2: Gearboxes, Cycloidal Drives & Mechanical Speed Reducers
*Kinematics, gear train cascading, zero-backlash cycloidal reducers, and preloading worm gears.*

---

## 1. Epicyclic (Planetary) Gearbox Kinematics & Cascading

```
Planetary Gear Topology:
           +---------------------------------------+
           | [Outer Ring Gear (R Teeth)]           |
           |     +---------------------------+     |
           |     | [Planet Gears (P Teeth)]  |     |
           |     |      (Mounted to Carrier) |     |
           |     |            +-----+        |     |
           |     |            | Sun |        |     |
           |     |            | (S) |        |     |
           |     |            +-----+        |     |
           |     +---------------------------+     |
           +---------------------------------------+
```

### The Fundamental Planetary Ratio Formula:
$$(R + S) \cdot \omega_{\text{Carrier}} = R \cdot \omega_{\text{Ring}} + S \cdot \omega_{\text{Sun}}$$ [CALCULATED]

Depending on which component is held stationary, a salvaged planetary stage (from a cordless drill, winch, or starter motor) provides three distinct kinematic modes:

| Fixed Component | Input Element | Output Element | Gear Ratio Equation | Physical Behavior |
| :--- | :--- | :--- | :--- | :--- |
| **Ring Gear (Fixed)** | Sun Gear | Carrier | $\text{Ratio} = 1 + \frac{R}{S}$ | **High Reduction (Forward)**: Maximum torque multiplication. Standard drill mode. |
| **Carrier (Fixed)** | Sun Gear | Ring Gear | $\text{Ratio} = -\frac{R}{S}$ | **Reversed Speed Reduction**: Output rotates opposite to input. |
| **Sun Gear (Fixed)** | Ring Gear | Carrier | $\text{Ratio} = 1 + \frac{S}{R}$ | **Low Reduction (Forward)**: Mild torque increase. |

### Cascading Cordless Drill Stages:
Cordless drills utilize modular planetary stages that can be stacked like LEGO blocks:
- Stage 1 (High-speed reduction): Sun $S = 9$, Ring $R = 45 \rightarrow \text{Ratio} = 1 + (45/9) = \mathbf{6:1}$.
- Stage 2 (High-torque reduction): Sun $S = 15$, Ring $R = 45 \rightarrow \text{Ratio} = 1 + (45/15) = \mathbf{4:1}$.
- Cascaded Total Ratio: $6 \times 4 = \mathbf{24:1}$.
- Stacking three stages yields reductions upwards of **120:1**, transforming an 18,000 RPM [TYPICAL] motor into an ultra-high-torque **150 RPM [TYPICAL] industrial powerhead**.

---

## 2. Cycloidal Speed Reducers: Zero-Backlash Robotics Joints

```
Cycloidal Drive Architecture:
  [Motor High-Speed Shaft] ===(Eccentric Cam Bearing)===> [Cycloidal Disc (N Lobes)]
                                                                    |
                                        (Wobbles inside Ring of N+1 Stationary Pins)
                                                                    |
  [Output Carrier with Roller Pins] <===============================+
  *(Delivers 20:1 to 50:1 Reduction in a SINGLE Compact Stage with ZERO Backlash)*
```

### Why Cycloidal Beats Spur Gears for Heavy Robotics:
In standard spur or planetary gears, only **one or two gear teeth contact at any given moment**, making them vulnerable to tooth shearing under shock loads.
- In a Cycloidal Reducer, the disc's epitrochoid curved lobes engage **up to 50% of the outer roller pins simultaneously**.
- **Shock Tolerance**: Can absorb instantaneous shock overloads of **over 500%** without damage.
- **Backlash**: Less than 1 arc-minute (virtually zero play), making it the gold standard for robot arm elbows, pan-tilt turrets, and telescope mounts.

### Cycloidal Reduction Formula:
$$\text{Reduction Ratio } = \frac{N_{\text{pins}} - N_{\text{lobes}}}{N_{\text{lobes}}}$$ [CALCULATED]
*(Example: A disc with 19 lobes rolling inside an outer ring of 20 pins yields a ratio of $1 / 19 \rightarrow \mathbf{19:1}$ reduction).*

#### Fabricating Cycloidal Drives from Scrap:
- Laser-cut or CNC-mill the cycloidal disc from **1/4" POM / Delrin sheet** (for self-lubricating, zero-chatter meshing) or 6061-T6 aluminum.
- Use salvaged skate bearings or miniature needle-roller bearings as the outer ring pins to eliminate sliding friction completely.

---

## 3. Worm Drives: Self-Locking Mechanics & Axial Thrust Management

```
Worm Drive Force Vectors:
                      [Tangential Drive Force]
                                 ^
                                 |
  [Motor Shaft] ===> (Steel Worm Screw)
                                 |
                                 v
                      [Massive Axial Thrust Force!] ===> [Thrust Needle Bearing Needed!]
                                 |
                                 v
                     [Bronze / Nylon Spur Gear] ===> [Output High-Torque Shaft]
```

### The Self-Locking Physics:
A worm drive locks when the lead angle of the worm thread ($\gamma$) is smaller than the static friction angle:
$$\gamma < \arctan(\mu_{\text{static}})$$
- For steel worm screws on bronze gears ($\mu \approx 0.15$), any lead angle under **$6^\circ \text{ to } 8^\circ$ is completely self-locking**.
- When power is removed, no amount of output torque can force the worm to turn (perfect for vertical hoists and winches).

### Managing Destructive Axial Thrust:
As the worm pushes the spur gear, an equal and opposite **axial thrust force** pushes back along the length of the motor shaft:
$$F_{\text{axial}} = \frac{T_{\text{output}}}{r_{\text{gear}}}$$ [CALCULATED]
- Standard motor radial ball bearings cannot survive high axial thrust and will quickly develop play and fail.
- **The Solution**: When adapting heavy worm drives (wiper motors, winches), always install a **hardened steel thrust needle bearing and thrust washer** behind the worm shaft shoulder to transfer axial thrust directly into the rigid gearbox housing.

---

## 4. Power Transmission Mediums: Belts vs. Chains vs. Gears

```
+-----------------------------------------------------------------------------------------------+
| Transmission Type     | Typical Profiles / Sizes   | Efficiency | Backlash  | Best Application |
| --------------------- | -------------------------- | ---------- | --------- | ---------------- |
| **GT2 / GT3 Timing**  | 2mm, 3mm pitch (neoprene)  | 98%        | Near-Zero | 3D printers, DROs|
| **HTD High-Torque**   | 3M, 5M, 8M curvilinear     | 97%        | Minimal   | Heavy robotics   |
| **Poly-V Multi-Rib**  | J-section, K-section       | 96%        | Zero slip | Treadmill spindles|
| **Roller Chain**      | #25 (1/4"), #35 (3/8")      | 92% - 95%  | Moderate  | Combat robot axles|
| **Precision Gears**   | Module 0.5 to Module 2.0   | 90% - 94%  | Moderate  | Lathe headstocks  |
+-----------------------------------------------------------------------------------------------+
```

---

## 5. DIY 3D-Printed & Scrap-Bearing Strain Wave (Harmonic) Drives

While commercial Harmonic Drive® units cost thousands of dollars and are rarely found intact in scrap bins, the fundamental kinematics can be replicated in a garage shop using a 3D printer and salvaged skateboard ball bearings (608 bearings):

```
       +-------------------------------------------------------------+
       | Strain Wave Drive Architecture:                             |
       |                                                             |
       |   [ Rigid Circular Spline (External Ring, e.g. 102 Teeth) ]  |
       |          |                                                  |
       |          v                                                  |
       |   [ Flexible Flexspline (Thin-Wall Cup, e.g. 100 Teeth) ]   |
       |          ^                                                  |
       |          |                                                  |
       |   [ Elliptical Wave Generator (Dual 608 Ball Bearings) ]     |
       |               ^                                             |
       |               +--- High-Speed Motor Input Shaft             |
       +-------------------------------------------------------------+
```

### A. The Kinematic Formula
A harmonic drive achieves colossal single-stage reduction through tooth difference between a rigid circular ring gear and an elastic flexspline deformed into an oval:

$$\text{Reduction Ratio} = \frac{N_{\text{flexspline}} - N_{\text{circular spline}}}{N_{\text{flexspline}}}$$ [CALCULATED]

*Worked Example:*
- Rigid Circular Spline: $N_{\text{circular spline}} = 102\text{ teeth}$
- Flexible Flexspline: $N_{\text{flexspline}} = 100\text{ teeth}$
$$\text{Ratio} = \frac{100 - 102}{100} = -\frac{2}{100} = -\frac{1}{50} \implies 50:1\text{ Reduction (Reverse Rotation)}$$ [CALCULATED]

Each full $360^\circ$ clockwise revolution of the elliptical wave generator causes the flexspline to advance counterclockwise by exactly **2 teeth**, yielding a **50:1 reduction in a single stage less than 2 inches thick**.

### B. Why It Achieves True Zero Backlash
In standard spur or planetary gearing, clearance must exist between tooth flanks to prevent binding, creating unavoidable rotational play (**backlash**). In a strain wave gear, the elliptical wave generator elastically forces teeth into full-depth engagement across two opposing zones simultaneously. The elastic preload eliminates clearance completely, delivering **true zero backlash** ($<1\text{ arcminute}$).

### C. Garage Fabrication SOP:
1. **The Wave Generator**: 3D print an elliptical cam hub (major axis offset by $1.5\text{ mm}$ to $2.0\text{ mm}$) with pockets for two salvaged **608 skate bearings** (from old inline skates or fidget spinners). Mount this cam directly to a NEMA 17 or NEMA 23 stepper motor shaft.
2. **The Flexspline**: Print the flexible cup on an FDM printer using **Nylon (PA6/PA12)**, **PETG**, or stiff **95A–98A Shore Hardness TPU**. The cylindrical wall thickness should be thin ($0.8\text{ mm to }1.2\text{ mm}$, exactly 2 to 3 perimeter perimeters) to allow elastic flexing without fatigue cracking.
3. **Lubrication**: Coat gear teeth with lithium-moly EP grease or PTFE grease.
4. **Repurposing Targets**: Robotic arm shoulder, elbow, and wrist joints; astronomy telescope star-tracking mounts; and CNC 4th rotary dividing axes where zero backlash is mandatory.
