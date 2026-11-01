# 🛠️ Volume 13.1: Step-by-Step Field Teardown SOPs
*Standard Operating Procedures for extracting intact, undamaged electromechanical assemblies from the top 5 common donors.*

---

## SOP 1: The Curbside Treadmill Teardown (12-Minute Extraction)

```
Treadmill Anatomy & Cut Points:
+-------------------------------------------------------------+
| [Motor Hood (Plastic Cowling)]                              |
|   |--- 4 to 6 Phillips / Robertson perimeter screws         |
|                                                             |
| Inside the Belly:                                           |
|   [1] Flywheel & PMDC Motor (Mounted on adjustable pivot)   |
|   [2] MC-60 / MC-2100 Motor Controller PCB (In lower corner)|
|   [3] AC Power Cord & Power Switch (Keep intact!)           |
|   [4] Incline Actuator (Center under the walking deck)      |
+-------------------------------------------------------------+
```

### Required Tools:
- Cordless drill/driver with #2 Phillips and #2 Robertson (Square) bits.
- 1/2" and 9/16" (or 13mm and 15mm) combination ratcheting wrenches.
- Flush diagonal wire cutters.
- Sharp utility knife.

### Step-by-Step Protocol:
1. **Safety Verification**: Ensure the unit is unplugged.
2. **Hood Removal**: Unscrew the 4 to 6 perimeter screws holding the front plastic motor shroud. Set plastic aside.
3. **Controller Harvest (First!)**:
   - Locate the main motor controller board (typically an **MC-60, MC-2100, or MC-1000**).
   - **DO NOT cut wires randomly at the board.** Unplug the spade connectors or unclip the multi-pin header intact.
   - Snip the AC mains wires **leaving 6 inches of wire attached to the board tabs** so you know which terminal is Live (`L1`), Neutral (`L2`), `A+`, and `A-`.
   - Unscrew the controller board mounting standoffs and place the board in a padded bag.
4. **Belt & Motor Release**:
   - The motor sits on an adjustable stamped steel pivot bracket secured by two heavy tensioning bolts.
   - Loosen the belt tensioning pivot bolt using your 9/16" wrench until the multi-rib Poly-V belt goes slack. Roll the belt off the flywheel.
   - **Keep the Poly-V drive belt intact**—matching replacement belts cost $25+.
5. **Motor Extraction**:
   - Remove the two main pivot through-bolts holding the motor frame to the treadmill chassis.
   - Lift the heavy PMDC motor (weight: 18 to 28 lbs) by its steel barrel, **never by the wiring leads or plastic fan blades**.
6. **Incline Actuator Harvest**:
   - Tip the treadmill onto its side.
   - The incline linear actuator is pinned at both ends with heavy steel clevis pins secured by cotter pins or hairpin clips.
   - Pull the cotter pins with pliers, slide out the clevis pins, and snip the actuator wiring harness at the controller plug.
7. **Leave Clean**: Set the plastic hood back onto the metal frame. You walk away with a 2.5 HP variable-speed spindle motor, flywheel, motor controller, belt, and 1,000 lb linear actuator.

---

## SOP 2: The Scrap Microwave Oven Teardown (Zero-Shock Protocol)

```
Microwave Interior Layout:
+-------------------------------------------------------------+
| [Upper Cavity: Waveguide & Magnetron]                       |
|   *(DANGER: Ceramic collars contain Beryllium Oxide!)*      |
|                                                             |
| [Lower Right Corner: The High-Voltage Danger Zone]          |
|   [1] High-Voltage Capacitor (Must be discharged FIRST!)    |
|   [2] High-Voltage Transformer (MOT) (Heavy iron core)      |
|   [3] High-Voltage Rectifier Diode                          |
|                                                             |
| [Door Perimeter]: 3x 15A Snap-Action Microswitches          |
| [Underneath Floor]: 120V Synchronous Turntable Motor        |
+-------------------------------------------------------------+
```

### Required Tools:
- T15 or T20 Security Torx driver (with center pin-hole) or flat-blade driver.
- Insulated Capacitor Discharge Wand (1 kΩ 50W resistor across insulated probes).
- 10mm socket or nut driver.
- Heavy leather gloves.

### Step-by-Step Protocol:
1. **Remove Outer Cover**:
   - Microwave outer shells are secured by 4 to 6 **Security Torx (Tamper-Proof) screws** along the back and bottom flange.
   - Back out the screws, slide the sheet metal cover backward 1 inch, and lift it upward.
2. **THE MANDATORY DISCHARGE STEP**:
   - Locate the oval metal cylinder in the lower right corner (the High-Voltage Capacitor).
   - Even if the microwave has been unplugged for a month, **assume it holds 2,500 Volts**.
   - Clip one lead of your discharge wand to the metal chassis.
   - Firmly touch the insulated resistor probe tip to each capacitor terminal for **5 seconds**.
   - Touch an insulated screwdriver across both capacitor terminals to confirm zero residual spark.
3. **Harvesting the Transformer (MOT)**:
   - The MOT is bolted to the microwave floor by four 10mm hex-head sheet metal screws.
   - Unclip the spade terminals from the primary (bottom) and secondary (top) windings.
   - Back out the four floor screws. Lift out the heavy 10–12 lb transformer core.
4. **Harvesting the Microswitches**:
   - Look behind the door latch mechanism on the front right.
   - You will see a plastic carrier housing three snap-action microswitches.
   - Depress the plastic retaining tabs to pop out each switch intact with its wires.
5. **Harvesting the Turntable Motor**:
   - Flip the microwave upside down.
   - In the center of the bottom floor is an embossed circular metal plate.
   - Snip the two small metal bridge tabs holding the plate, or unscrew the central screw.
   - Unbolt the 2.5–5 RPM [TYPICAL] synchronous turntable gearmotor and disconnect its two push-on spade terminals.
6. **Magnetron Protocol**:
   - If you want the two large ring magnets inside the magnetron: Unbolt the magnetron from the waveguide.
   - Use a hacksaw or pliers to bend back the aluminum outer cooling fins.
   - **DO NOT strike, cut, crush, or grind the pink or white ceramic insulator rings**—they contain toxic Beryllium Oxide. Slide the ring magnets off the tube intact.

---

## SOP 3: Laser Printers & Photocopiers (Precision Motion Harvest)

```
Laser Printer Chassis Breakdown:
+-------------------------------------------------------------+
| [Print Head Assembly]: Laser Scanner Unit (Polygon Mirror)  |
|                                                             |
| [Carriage & Paper Path]: Hardened 8/10/12mm Ground Rods     |
|   |--- Secured by E-clips / Stamped Steel End Clamps        |
|                                                             |
| [Side Gearbox Drive]: Heavy NEMA 17 / NEMA 23 Steppers      |
|   |--- High-torque hybrid stepper motors + gear trains      |
|                                                             |
| [Exit Path]: Fuser Assembly (Halogen Tube + Silicone Roller)|
+-------------------------------------------------------------+
```

### Critical Extraction Rule: Protecting Ground Shafts
- **Never bend, pry, or hammer on the ground steel shafts.** Even a microscopic 0.05 mm bow ruins them for linear ball bearings (LM8UU).
- Locate the small **E-clips or stamped sheet metal spring retainers** at each end of the rod.
- Pry off the E-clips using a flathead screwdriver while holding a rag over them so they don't fly across the room.
- Slide the hardened steel shaft out through its side bushings smoothly.

---

## SOP 4: Junkyard Automotive Steering Columns & Alternators

### Extracting Electric Power Steering (EPS) Columns:
1. **Target Vehicles**: 2004–2009 Toyota Prius, 2000–2006 Opel Corsa C, 2007–2012 Nissan Versa, 2006–2011 Hyundai Accent.
2. **Access**: Drop the lower dashboard knee bolster panel (usually 2 screws and push-pins).
3. **Electrical Harness Triage**:
   - Locate the heavy high-current 2-pin power plug leading directly into the motor casing.
   - Locate the thin multi-pin ribbon harness leading to the **torsion-bar torque sensor** at the top of the column.
   - **DO NOT cut the torque sensor plug.** Carefully press the locking tab and unplug it cleanly. If you rip this harness, closed-loop force feedback becomes impossible.
4. **Mechanical Unbolting**:
   - Unbolt the steering shaft pinch-bolt at the lower universal joint near the floorboard (12mm or 14mm socket).
   - Unbolt the two or four main column mounting bracket bolts holding the column to the dashboard cross-member.
   - Slide the column assembly backward off the splines. You walk out with a complete 25 Nm [TYPICAL] direct-drive brushless servo column.
