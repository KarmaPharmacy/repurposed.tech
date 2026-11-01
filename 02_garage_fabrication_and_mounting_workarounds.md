# 🛠️ Volume 13.2: Garage Fabrication & Heavy Mounting Workarounds
*Rigid mechanical mounting, template transfer, vibration damping, and belt alignment without expensive CNC machinery.*

---

## 1. Mounting Odd-Shaped Motors Without a CNC Mill

Salvaged motors (wiper motors, alternators, treadmill motors) do not follow standardized NEMA faceplate bolt dimensions. They feature irregular, asymmetrical cast lugs, curved barrel casings, or triangular bolt circles.

```
Transferring Irregular Bolt Patterns to Steel Plate:
  Step 1: The Paper / Masking Tape Impression
    - Lay heavy cardstock or masking tape across the motor's mounting face.
    - Tap gently around the bolt holes and center pilot boss with a small ball-peen hammer.
    - The sharp edges of the holes cleanly shear the paper, leaving an exact 1:1 template!
    
  Step 2: Center Punch & Transfer
    - Glue the paper template to a 3/16" (4.5mm) or 1/4" (6mm) mild steel plate.
    - Dimple each hole center with a hardened steel center punch.
    
  Step 3: Concentric Stepped Drilling
    - Drill a tiny 1/8" (3mm) pilot hole at every punch mark.
    - Step up progressively using a Cobalt drill bit or Stepped Unibit to finished diameter.
```

---

## 2. Fabricating Slotted Tensioning Mounts

```
Filing Slotted Motor Adjustment Rails:
+-------------------------------------------------------------+
| Hole A (1/2") <====[File out central web]====> Hole B (1/2")|
|                                                             |
| ====> Creates 1.0" of continuous belt tensioning travel!    |
+-------------------------------------------------------------+
```

When building belt or chain-driven tools (belt grinders, lathes, go-karts), you **must have a method to tension the belt** as it stretches over time.
1. Mark the centerlines of your travel slot on your 3/16" mounting plate.
2. Drill Hole A at the beginning of the slot and Hole B at the end of the slot using a 3/8" or 1/2" drill bit.
3. Cut out the remaining metal web between the two holes using a drill bit or hacksaw blade, then smooth the slot flat using a coarse bastard mill file.
4. Use **Grade 8 heavy thick washers and flanged lock-nuts** so the motor cannot slip forward under heavy cutting torque.

---

## 3. Mounting Round Flangeless Motors: The Split Clamping Block

```
Split Block Motor Barrel Clamp:
+-------------------------------------------------------------+
| [Top Aluminum / Hardwood Split Block]                       |
|   |--- Semicircular cutout matching motor OD                |
|   |--- 2x Through-Bolts (Tightened to pinch barrel)         |
|                                                             |
| [Motor Barrel (PMDC / BLDC)] <--- (360° Friction Clamp)     |
|                                                             |
| [Bottom Aluminum / Hardwood Base Block]                     |
|   |--- Bolted solidly to machine frame                      |
+-------------------------------------------------------------+
```

- When a motor lacks face mounting holes (e.g., starter motors, drone outrunners, high-power DC spindle motors), **never attempt to drill holes into the motor frame**—you will pierce the stator windings or shatter internal permanent magnets.
- **The Split Clamp Solution**:
  - Bolt two thick rectangular blocks of 6061 aluminum (or high-density Baltic birch plywood) tightly together with a 1/8" shim spacer between them.
  - Bore a circular hole through the seam using a hole saw or boring head on a drill press, sized to the exact outer diameter of the motor barrel.
  - Remove the shim spacer.
  - Slip the motor inside and tighten the pinch bolts: The split block contracts uniformly around the motor casing, clamping it with thousands of pounds of static friction that cannot slip or vibrate loose.

---

## 4. Pulley & Belt Alignment: The Straight-Edge Protocol

```
Checking Pulley Coplanarity:
  [Motor Pulley]                      [Spindle Pulley]
  +============+                      +==============+
  |            |                      |              |
  |            | <==================> |              |
  +============+                      +==============+
        |                                    |
        +-----[ Machined Steel Straight-Edge ]
              *(Must touch all 4 outer pulley rims simultaneously!)*
```

### Why Visual Alignment Fails:
If two pulleys are misaligned by even **$1.5^\circ$ of angular skew or 2mm of parallel offset**:
- Timing belts will ride up against the pulley guide flanges, fraying their edges and snapping within hours.
- Poly-V multi-rib belts will squeal loudly, generate intense heat, and slip under load.

### The 4-Point Straight-Edge Test:
1. Place a precision ground steel ruler or aluminum box level across the front rim faces of both pulleys.
2. The straight-edge **must make solid contact with all four outer rim points simultaneously**:
   - Point 1 & 2 on the motor pulley outer rim.
   - Point 3 & 4 on the driven spindle pulley outer rim.
3. If there is a visible gap or rocking at any point, adjust motor shims or slide the pulley along the shaft until the ruler sits dead-flat across both wheels.

### Belt Tension Rule of Thumb:
- Apply moderate thumb pressure (approx. 10 lbs / 45 N) to the center of the belt span.
- **Correct Tension**: The belt should deflect by approximately **1/64-inch per inch of span distance** (e.g., on a 16-inch center-to-center span, the belt should deflect exactly **1/4-inch / 6mm**).

---

## 4. Thermal Shrink-Fitting: Zero-Hammer Bearing Preservation

When adapting pulleys, sprockets, or hardened steel collars onto salvage motor shafts, press-fits with an interference tolerance of $+0.02\text{ mm to }+0.04\text{ mm}$ cannot be pushed on by hand.

> [!CAUTION]
> **NEVER HAMMER A PULLEY ONTO A MOTOR SHAFT**: Hammering against a shaft drives shock loads directly through the internal hardened steel ball bearings, causing **brinelling** (permanent microscopic indentation of the bearing races). Within hours of operation, the motor will roar, vibrate violently, and seize.

```
       [ Cold Motor Shaft in Freezer / Dry Ice ]  (---> Contracts by -0.018 mm)
                            |
                            v
       [ Bored Steel Pulley in Toaster Oven (200°C) ]  (---> Expands by +0.032 mm)
                            |
                            v
       =====> SLIDES ON BY HAND WITH ZERO MECHANICAL FORCE!
              Locks with hundreds of foot-pounds of grip upon cooling!
```

### A. The Thermal Expansion Mathematics
Thermal expansion follows the linear relationship:
$$\Delta D = D_0 \cdot \alpha \cdot \Delta T$$ [CALCULATED]
Where:
- $D_0$ = Nominal bore or shaft diameter (mm).
- $\alpha$ = Coefficient of linear thermal expansion ($\text{Steel} \approx 12 \times 10^{-6}\text{ /}^\circ\text{C}$; $\text{Aluminum} \approx 23 \times 10^{-6}\text{ /}^\circ\text{C}$).
- $\Delta T$ = Temperature differential from ambient ($25^\circ\text{C}$).

*Worked Interference Example:*
1. **Heating the Steel Pulley**: Place the bored pulley in a garage toaster oven at $200^\circ\text{C}$ ($400^\circ\text{F}$) for 25 minutes ($\Delta T = +175^\circ\text{C}$):
   $$\Delta D_{\text{pulley}} = 15.0\text{ mm} \times (12 \times 10^{-6}) \times 175 = +0.0315\text{ mm expansion}$$ [CALCULATED]
2. **Chilling the Motor Shaft**: Wrap the motor casing in an insulated towel and immerse only the shaft extension in a bath of **dry ice and isopropyl alcohol** ($-78^\circ\text{C}$, $\Delta T = -103^\circ\text{C}$), or place the entire motor in a standard $-20^\circ\text{C}$ deep freezer:
   $$\Delta D_{\text{shaft}} = 15.0\text{ mm} \times (12 \times 10^{-6}) \times (-103) = -0.0185\text{ mm contraction}$$ [CALCULATED]
3. **Total Expansion Window**:
   $$\text{Total Clearance} = \Delta D_{\text{pulley}} - \Delta D_{\text{shaft}} = 0.0315 - (-0.0185) = 0.050\text{ mm} \approx 0.002\text{ inches}$$ [CALCULATED]
4. **Assembly**: Using insulated welding tongs, pick up the hot pulley and drop it smoothly over the freezing motor shaft. It will slide all the way to the shaft shoulder by hand with zero resistance. Within 45 seconds, the metals equalize to room temperature, creating an indestructible shrink-fit joint capable of transmitting full motor torque without set screws or keys.

---

## 5. Electrolytic Rust Removal with Salvaged ATX Power Supplies

Salvaged junkyard parts (cast-iron pulleys, automotive alternator brackets, EPS steering knuckles, drill press tables) often suffer from deep rust that would take hours of grinding or toxic chemical acid baths to remove.

```
       (-) Black Lead (12V GND)                      (+) Yellow Lead (+12V Rail)
                 |                                                |
                 v                                                v
      [ RUSTY WORKPIECE (CATHODE) ]                  [ REBAR ANODE (SACRIFICIAL) ]
                 |                                                |
                 +-----> [ Sodium Carbonate Bath (Washing Soda) ] <+
                         (Safe, Non-Toxic, Zero Metal Erosion)
```

### A. The Electrochemical Physics
Unlike acid baths (muriatic/phosphoric) which chemically attack both rust and healthy unoxidized steel—pitting machined surfaces and altering bore tolerances—**electrolysis is chemically selective**:
- The rusty steel part is made the **Cathode (Negative, Black wire)**.
- A piece of scrap mild steel rebar or plate is made the **Anode (Positive, Yellow wire)**.
- Electric current from the salvaged ATX PSU passes through an alkaline electrolyte solution containing **Sodium Carbonate ($\text{Na}_2\text{CO}_3$, Arm & Hammer Super Washing Soda)**:
  $$\text{Fe}_2\text{O}_3\text{ (Red Rust)} + 2e^- + \text{H}_2\text{O} \longrightarrow 2\text{Fe}_3\text{O}_4\text{ (Black Magnetite)} + 2\text{OH}^-$$
- Red rust is chemically converted back into soft black magnetite, while hydrogen bubbles scrubbing out of the metal pores mechanically blast the scale off the surface.
- **Healthy base metal is completely untouched**: Precision ground shaft diameters, keyways, and stamped part numbers are preserved to the micron!

### B. Workshop Electrolysis SOP:
1. **Electrolyte Mix**: Fill a 5-gallon plastic bucket with clean water and dissolve **1/3 cup of washing soda** (never use table salt / $\text{NaCl}$, which produces toxic chlorine gas!).
2. **Anode Ring**: Bend several pieces of clean steel rebar around the inside perimeter of the bucket and wire them together in parallel (ensures line-of-sight cleaning from all sides).
3. **Power Connection**:
   - Clip the **Negative (GND, Black wire)** of the ATX bench supply firmly to the rusty part using clean copper alligator teeth.
   - Clip the **Positive (+12V, Yellow wire)** to the sacrificial rebar anode.
4. **Run Time**: Power on the ATX supply. Current will settle between 5A and 15A. Run for 4 to 8 hours.
5. **Post-Clean**: Pull the part out, rinse under tap water, and wipe with a plastic dish scrubber. The black residue washes away effortlessly, revealing clean, bare silver steel. Spray immediately with WD-40 or paste wax to prevent flash rusting.

---

## 6. DIY "Rulon / Turcite" Low-Friction Way Liners from Salvaged PTFE

When restoring worn machine tools (lathe bed ways, vertical mill knee slides) or fabricating custom heavy CNC sliding dovetails, cast-iron on cast-iron contact suffers from high friction, rapid wear, and notorious low-speed stick-slip chatter.

```
       [ Machine Saddle / Carriage Casting ]
       =========================================================
       [ Structural Epoxy Bed (J-B Weld / Toughened Epoxy) ]
       ---------------------------------------------------------
       [ Mechanically Keyed Scrap PTFE / Teflon Sheet (1.5mm) ]
       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  <-- Flaked Oil Pockets
       [ Ground Machine Bed Way (Cast Iron / Steel Rail) ]
```

### A. Sourcing High-Grade Virgin PTFE:
- Scrap commercial non-stick heat-press baking sheets, laser printer fuser film sleeves, or chemical laboratory PTFE scrap plates.
- PTFE (Polytetrafluoroethylene) has the lowest static coefficient of friction of any solid ($\mu_s \approx 0.04$) and, uniquely, its static friction is **lower than its kinetic friction**—physically eliminating stick-slip chatter forever!

### B. Bonding the Unbondable:
PTFE's non-stick properties mean ordinary adhesives will peel off effortlessly:
1. **Mechanical Keying & Etching**: Thoroughly abrade the bottom bonding face with coarse 40-grit silicon carbide sandpaper in a crisscross pattern until the surface is completely matted and micro-grooved, or wipe with commercial sodium-naphthalene etchant (Fluorogrip).
2. **Epoxy Bedding**: Clean with pure acetone. Coat the machined cast-iron saddle underside with slow-cure structural epoxy (J-B Weld Original or West System with colloidal silica filler).
3. **Clamping & Curing**: Clamp the PTFE strip firmly against the bed ways overnight using wax-paper separator release film to ensure a dead-flat epoxy foundation.
4. **Scraping Oil Reservoirs**: Once cured, use a sharp carbide scraper to flake shallow **half-moon micro-dimples** ($0.05\text{ mm}$ deep) into the PTFE surface. These pockets trap way lubricant, creating a hydrodynamic oil cushion that allows a 300 lb lathe carriage to glide with the push of a pinky finger!

---

## 7. Home Precision Lapping: The Whitworth "Three-Plate Method"

How do you create an optical-grade machine reference surface flat to within **2 microns (0.0001 inches)** without spending $3,000 on a certified granite inspection plate?

```
      Step 1: Lap A on B        Step 2: Lap A on C        Step 3: Lap B on C
         +-------+                 +-------+                 +-------+
         |   A   |                 |   A   |                 |   B   |
         +-------+                 +-------+                 +-------+
         |   B   |                 |   C   |                 |   C   |
         +-------+                 +-------+                 +-------+
      (Convex meets             (Discrepancy              (Geometric necessity
       Concave!)                 revealed!)                forces absolute flatness!)
```

### A. The Inevitable Trap of Two Plates:
If you lap only two metal or glass plates ($A$ and $B$) together with abrasive slurry, they will wear into a spherical curve: one becomes slightly **concave** (a bowl) and the other becomes **convex** (a dome). They fit together seamlessly, yet neither is flat!

### B. Sir Joseph Whitworth’s 1840 Geometric Convergence:
By introducing a **third plate ($C$)** and cyclically rotating the pairing order:
1. Lap Plate $A$ against Plate $B$.
2. Lap Plate $A$ against Plate $C$.
3. Lap Plate $B$ against Plate $C$.
- A convex surface on Plate $A$ cannot simultaneously mate with a concave surface on Plate $B$ and Plate $C$ across cyclic rotations unless the radius of curvature approaches infinity ($R \rightarrow \infty$).
- **The mathematical convergence is absolute**: Geometric necessity eliminates high spots and hollows, forcing all three plates toward **dead, absolute planar flatness**!

### C. Garage Lapping SOP:
1. **Material Sources**: Three matching square scraps ($10"\times 10"$ or $12"\times 12"$) of **1/2" float glass**, salvaged cast-iron surface plates, or polished granite countertop sink cutouts.
2. **Abrasive Slurry**: Mix silicon carbide grinding powder with mineral oil or water:
   - Stage 1: 320-grit (bulk flattening, 30 minutes).
   - Stage 2: 600-grit (semi-finish, 20 minutes).
   - Stage 3: 1200-grit (mirror satin, 15 minutes).
3. **Motion**: Use slow, overlapping figure-eight strokes while rotating the top plate $90^\circ$ every 20 strokes to avoid directional grooves.
4. **Result**: You now own three verified master surface plates flat to within **$0.0001\text{ inches}$**, ready for precision scraping of machine ways, verifying micrometer calibration, and lapping heatsink surfaces to mirror finishes!

---

## 8. Cryogenic Freeze-Chucking for Machining Micro-Elastomers

Machining soft materials—silicone sheets, polyurethane suspension bushings, and neoprene gaskets—on a CNC router or milling machine is notoriously difficult because the rubber flexes away from the tool bit, tears at the edges, and wraps around rotating flutes.

```
       [ Chilled Aluminum Vacuum Chuck Plate (-30°C) ]
       =========================================================
       [ Thin Water Ice Boundary Layer (0.2mm) ]
       =========================================================
       [ Soft Neoprene / Silicone Rubber Workpiece ]
       (FROZEN ROCK-SOLID INTO GLASS-HARD PLASTIC!)
            |
            v
       =====> Standard Carbide Endmills Cut Flawless O-Ring Grooves!
```

### A. The Glass Transition ($\text{T}_g$) Exploit:
All elastomeric polymers exhibit a **Glass Transition Temperature ($\text{T}_g$)**. Above $\text{T}_g$, polymer chains slide freely (flexible rubber). Below $\text{T}_g$ (typically $-10^\circ\text{C}$ to $-40^\circ\text{C}$), molecular motion freezes: the rubber undergoes an abrupt physical phase change, turning into an **extremely brittle, glass-hard solid**.

### B. The Setup:
1. Salvage a Peltier TEC1-12706 thermoelectric cooling module stack (or route chilled evaporator tubing from a scrap dehumidifier) directly to an aluminum bed plate.
2. Place the soft elastomer on the bed and mist with water.
3. Turn on the chiller. In 3 minutes, the bed drops to **$-25^\circ\text{C}$ to $-35^\circ\text{C}$**. The water freezes into an immovable ice adhesive clamp, and the rubber turns glass-hard.
4. Machine with sharp 2-flute carbide endmills at high spindle speed ($18,000\text{ RPM}$) with shallow passes ($0.2\text{ mm}$).
5. Power off the chiller: the ice thaws, leaving a pristine, burr-free silicone gasket with micron-level feature accuracy!


---

## 9. The Scrap-Steel Spark Test: Instant Bench Metallurgy

When building heavy machinery from scrap yards, using mystery steel is hazardous: welding high-carbon steel causes brittle heat-affected zone (HAZ) cracking, while attempting to quench-harden low-carbon mild steel leaves cutting tools dead-soft. The **Spark Test** provides instantaneous metallurgical identification using only a bench grinder or 4.5" angle grinder in a shaded shop corner:

```
                  Scrap Steel Grinding Spark Signatures
                  
 Low-Carbon (1018/A36):     Medium-Carbon (1045):      High-Carbon (1095/52100):
 =====================      ====================       =========================
 Long, straight, smooth     Moderate length, yellow,   Short, dense, brilliant white,
 yellow lines; NO bursts.   frequent simple forks.     violent explosive starbursts!
 ─────────────────────────  ───────*───*──────*        ────***-*****-*******-*******
 (Dead-soft, easily welded) (Axles, shafts, tough)     (Hardens glass-hard, knives)
```

### A. The Physics of the Spark
As the grinding grit tears off microscopic molten steel particles, the hot iron reacts with atmospheric oxygen. **Carbon acts as a miniature explosive**: as carbon within the molten droplet burns into $\text{CO}_2$ gas, internal pressure shatters the droplet mid-flight into distinct **exploding starbursts** ("carbon sparks"). The higher the carbon content, the denser and more violent the explosions.

### B. The Diagnostic Identification Key:
1. **Low-Carbon Mild Steel (AISI 1018 / ASTM A36 / Structural Tubing)**:
   - *Stream*: Long ($20"\text{ to }30"$), smooth, straight straw-yellow stream.
   - *Bursts*: Almost zero bursts or forks. Sparks end in simple points.
   - *Working Rules*: Extremely ductile, easily bent cold, 100% weldable with any MIG/stick process. **Cannot be heat-treated or hardened** by oil/water quenching.
2. **Medium-Carbon Shaft Steel (AISI 1045 / Axles / Hydraulic Rods)**:
   - *Stream*: Medium length ($15"\text{ to }20"$), light straw yellow lines.
   - *Bursts*: Frequent, repeating simple "forked" starbursts along the outer third of the stream.
   - *Working Rules*: Ideal for high-strength machine spindles, leadscrews, and bolted brackets. Quenchable in oil for moderate wear resistance.
3. **High-Carbon Tool Steel (AISI 1095 / Leaf Springs / 52100 Ball Bearing Races)**:
   - *Stream*: Short ($10"\text{ to }15"$), compact, brilliant white shower.
   - *Bursts*: Dense, violent, multi-branched feathery explosions beginning immediately next to the grinding wheel.
   - *Working Rules*: Hardens glass-brittle when water- or oil-quenched from cherry red ($800^\circ\text{C}$). Ideal for shop-made cutting chisels, scrapers, and blades. **Do NOT weld directly** without preheating to $250^\circ\text{C}$, or the weld toe will snap like glass.
4. **Gray Cast Iron (Engine Blocks / Lathe Beds)**:
   - *Stream*: Very short ($8"\text{ to }10"$), dull reddish-orange stream.
   - *Bursts*: Sparks form tiny, dull red clusters that vanish quickly.
   - *Working Rules*: High free-graphite content. Produces fine black dust instead of chips when filed. Requires high-nickel (ENi-CI) welding electrodes or brazing.
5. **High-Speed Steel (M2 / Broken Endmills / Lathe Toolbits)**:
   - *Stream*: Dull red to dark orange carrier lines with distinctive **swollen clubbed tips (arrowheads)** at the end of each spark, with zero white carbon bursts.
   - *Working Rules*: Retains hardness up to $600^\circ\text{C}$ (red heat). Extreme wear resistance for lathe boring bars and metal scrapers.
