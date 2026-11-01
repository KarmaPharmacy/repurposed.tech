# 🏃 Volume 3.2: Treadmills & Exercise Equipment
*Harvesting 3 HP permanent-magnet DC spindle motors, 1,000 lb linear incline jacks, and heavy steel rollers.*

---

## 1. Treadmill PMDC Motors: The King of Workshop Machinery

```
Treadmill PMDC Motor Anatomy:
+-------------------------------------------------------------+
| [Heavy Cast Iron Flywheel / Poly-V Pulley]                  |
|                 |                                           |
| [Balanced High-Voltage Armature (90V - 180V DC)]            |
|                 |                                           |
| [Massive Curved Ferrite Stator Magnets]                     |
|                 |                                           |
| [Internal Heavy Radial Cooling Fan]                         |
+-------------------------------------------------------------+
```

### Why Treadmill Motors Beat Standard AC Induction Motors:
Standard workshop machine tools (drill presses, band saws, small metal lathes) typically come equipped with single-speed 1/3 HP or 1/2 HP AC induction motors. Changing speeds requires unbolting motor mounts and wrestling rubber V-belts across stepped pulleys.
- **The Treadmill Advantage**:
  - Delivers **1.5 to 3.5 true continuous horsepower**.
  - High voltage (90V DC in North America, 180V–230V DC internationally) keeps operating current relatively low (10A to 18A).
  - Produces buttery-smooth variable speed from **50 RPM [TYPICAL] to 5,000+ RPM** at the turn of a single dial.
  - The heavy integrated cast-iron flywheel acts as a kinetic energy reservoir, preventing the spindle from chattering or stalling during heavy, interrupted metal-cutting passes.

---

### Driving the Treadmill Motor:

```
MC-60 OEM Board Hacking:
+-------------------------------------------------------------+
| [AC Hot & Neutral Mains] ---> [MC-60 L1 & L2 Tabs]          |
|                                                             |
| [Motor Leads]            <--- [A+ & A- Output Tabs]         |
|                                                             |
| [5k Ohm Linear Pot]      ---> Connect to [H, W, L] Terminals|
|                                (High, Wiper, Low)           |
+-------------------------------------------------------------+
```

#### Method 1: The KB Electronics KBIC / KBMM SCR Drive (Recommended)
- Connects directly to 120V or 240V AC [TYPICAL] mains.
- Provides smooth DC output with **Armature Back-EMF (IR Compensation)** feedback.
- When grinding tool steel on a 2x72 belt grinder, the drive senses the load spike and instantly raises DC voltage to maintain constant belt speed.

#### Method 2: Hacking the OEM Treadmill Board (MC-60 / MC-2100)
- **MC-60 Boards**: Locate the 3-pin spade connector labeled `H` (High), `W` (Wiper), and `L` (Low). Connect the outer legs of a standard 5kΩ or 10kΩ linear potentiometer to `H` and `L`, and the center wiper pin to `W`. You now have a free variable speed controller.
- **MC-2100 Boards**: Requires a digital 20 Hz PWM signal on the control header (easily generated with an Arduino or a 555 timer chip):
  - `0% Speed`: Pulse width 0 ms (0% duty cycle)
  - `Full Speed`: Pulse width approx. 21 ms (85% duty cycle)

---

### Marquee Workshop Machine Projects:

#### A. 2" x 72" Knifemaking Belt Grinder
- Commercial knifemaking grinders (e.g., TW-90, Brodbeck) cost upwards of $2,500.
- Knife profiling requires high surface speed (approx. 4,500 to 5,500 SFPM) to hog off annealed tool steel rapidly; fine edge finishing and handle shaping require slow speeds (under 1,500 SFPM) to avoid burning the temper of the blade.
- Direct-coupling a 2.5 HP treadmill motor to a 5-inch crowned drive wheel provides the exact variable SFPM range needed for professional bladesmithing.

#### B. Mini-Lathe (7x12 / 7x14) Variable Spindle Upgrade
- Stock Chinese mini-lathes (Sieg, Grizzly, Central Machinery) use fragile plastic high/low gears that strip easily.
- Mount a treadmill motor behind the lathe headstock with a timing belt driving the spindle directly. You eliminate the noisy plastic gearbox entirely and gain silky-smooth electronic spindle speed adjustment down to threading speeds.

---

## 2. Treadmill Incline Linear Actuators (Heavy 1,000 lb Screw Jacks)

```
Incline Actuator Mechanics:
  [Heavy 120V AC [TYPICAL] / 24V DC [TYPICAL] Motor] ===> [Steel Reduction Gearbox]
                                                    |
                                                    v
                                      [Heavy ACME Threaded Screw]
                                                    |
                                                    v
                                      [Heavy Tubular Piston Rod]
                                      (600 to 1,200 lbs Thrust)
```

### Harvestable Characteristics:
- **Thrust Force**: Engineered to lift the weight of a heavy treadmill deck plus a 300 lb human running on it (rated for 600 to 1,200 lbs of dynamic linear force).
- **Position Feedback**: Contains an internal **10 kΩ rotary potentiometer** mechanically geared to the lead screw. Reading this potentiometer with an Arduino analog pin provides absolute, zero-drift position tracking down to 0.5 mm.

### Creative Repurposing Exploits:
- **Ergonomic Motorized Height-Adjustable Workbench**:
  - Mount an incline actuator vertically under a heavy 400 lb butcher-block woodworking workbench.
  - Wire a simple rocker switch on the front edge to adjust bench height effortlessly from 30 inches (comfortable hand-planing height) to 42 inches (comfortable standing assembly and electronics soldering height).
- **Lawn Tractor Snow Blade / Mower Deck Electric Lift**:
  - Replaces manual arm-straining lift levers with effortless push-button electric raising and lowering on garden tractors.
- **Automated Trapdoor / Secret Storm Cellar Hatch**:
  - Easily pushes open a 200 lb heavy floor trapdoor flush-mounted into a living room or workshop hardwood floor.

---

## 3. Precision Steel Rollers & Sealed Bearings
- Discarded treadmills yield two large-diameter (typically 1.75" to 2.5" OD) precision-turned steel rollers equipped with heavy-duty sealed deep-groove ball bearings.
- *Projects*: Sheet metal slip roll machines for rolling cylindrical steel stovepipes, custom belt conveyors, and belt grinder idler wheels.

---

## 4. Industrial Sewing Machine Servos: The Lathe Spindle Holy Grail

While treadmill motors are the traditional budget choice for lathe conversions, experienced machinists increasingly hunt for **brushless industrial sewing machine servo packages** (Consew CSM1000, Juki, Sailrite, Brother):

```
+-------------------------------------------------------------------------+
| Industrial Sewing Servo Powertrain Architecture:                        |
|                                                                         |
| [ 110V/220V AC Mains ] ---> [ Digital Control Box & Parameter Display ] |
|                                   |                    |                |
|               (Hall Foot Pedal) --+                    v                |
|                                        [ 550W-750W TEFC Brushless Motor]|
|                                        [ Integrated Optical DRO Encoder]|
|                                        [ Electromagnetic Brake Solenoid]|
+-------------------------------------------------------------------------+
```

### A. Why Sewing Servos Demolish Treadmill PMDC Motors:
1. **Totally Enclosed Construction (TEFC)**: Treadmill motors are open-frame, fan-cooled motors that suck ambient air through their windings. In a metal lathe or milling environment, conductive cast-iron dust and metal chips get sucked directly into the commutator, causing catastrophic short-circuits. Sewing servos are **hermetically sealed, brushless motors** completely impervious to swarf, grinding dust, and coolant splash.
2. **True Closed-Loop Optical Vector Control**: Treadmill SCR drives rely on crude open-loop IR compensation. A sewing servo has an internal optical encoder feeding position and velocity back to an onboard DSP. When turning steel at **150 RPM [TYPICAL] for single-point thread cutting**, the sewing servo delivers **100% full rated torque**, instantly ramping current to prevent stalling when the carbide tool digs into the cut.
3. **Instantaneous Reversing & Braking**: Treadmill motors coast down for 5–10 seconds under flywheel inertia. A sewing servo incorporates active regenerative electronic braking and a friction brake, stopping dead in **under 0.2 seconds**—a life-saving feature when cutting threads up to a shoulder.
4. **Digital Speed Tuning**: The external control box allows setting exact minimum RPM (down to 100 RPM [TYPICAL]), maximum RPM (up to 4,500 RPM [TYPICAL]), acceleration rates, and rotational direction at the press of a button.

---

## 5. Hospital Bed & Patient Lift Actuators (Linak / TiMotion)

Scrapped motorized hospital beds, bariatric stretchers, and mobile patient lifts contain the most over-engineered linear actuators in consumer/medical surplus:

```
        +-------------------------------------------------------------+
        | Medical-Grade Linear Actuator:                              |
        |                                                             |
        | [ High-Torque 24V DC [TYPICAL] Motor with Dual-Stage Worm Reduction ] |
        |                          |                                  |
        |                          v                                  |
        | [ Hardened Steel Acme Screw + Bronze Safety Backup Nut ]    |
        |                          |                                  |
        |                          v                                  |
        | [ Heavy Stainless Steel Extension Tube: IPX6 Sealed ]       |
        |                                                             |
        | Performance: 4,000 N to 8,000 N (1,000 to 2,000 lbs) Thrust |
        +-------------------------------------------------------------+
```

### A. Medical-Grade Engineering Standards:
- **Colossal Thrust Capacity**: Built to lift heavy patients, these actuators deliver **1,000 to 2,000 lbs (4,000 N to 8,000 N) of dynamic thrust**, with static holding ratings exceeding **3,500 lbs**.
- **Sanitary Sealing**: Enclosed in heavy aluminum and composite housings with dynamic shaft wipers rated for **IPX6 washdown and autoclave sanitation**, making them 100% dustproof and weatherproof for outdoor machinery.
- **Fail-Safe Bronze Safety Nut**: In addition to the primary drive nut, an internal unloaded bronze safety nut catches the load if the main nut ever shears, preventing uncommanded collapse.

### B. Repurposing Exploits:
1. **Hydraulic-Substitute Dump Trailer Lift**: Pair two 24V actuators in parallel to tilt a utility trailer bed for dumping gravel or firewood without hydraulic fluid leaks, pumps, or hoses.
2. **Solar Array Seasonal Elevation & Storm Stow Jack**: Elevates an 8-panel ground-mount solar array to track winter vs summer sun angles, retracting the array flat against the ground during 60 MPH wind alerts.
3. **Motorized Heavy Welding Positioner**: Adjusts the height and tilt angle of heavy steel weldments so the maker can weld comfortably in the horizontal flat position.
