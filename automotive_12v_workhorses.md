# 🚗 Volume 2.1: Automotive 12V Workhorses
*Tearing into windshield wiper gearmotors, power window regulators, seat-track leadscrews, and door actuators.*

---

## 1. Windshield Wiper Motors: The King of Scrap Automation

```
Wiper Motor Internal Electrical Schematic:
           +-----------------------------+
           | Armature Housing            |
           |                             |
           |      [Low Speed Brush] -----> Wire 1: Low Speed (+12V)
           |             |               |
   (Ground) <-- [Common Ground Brush]    |
           |             |               |
           |      [High Speed Brush] ----> Wire 2: High Speed (+12V)
           +-----------------------------+
                         |
                 (Worm Gearbox)
                         |
           +-------------v---------------+
           | Park Switch Assembly        |
           |                             |
           |  [Cam Disc] ===[Contacts]---> Wires 3 & 4: Park Signal
           +-----------------------------+
```

### Why They Are Unique:
1. **Three-Brush Armature Architecture**: Wiper motors achieve two distinct operating speeds without electronic PWM controllers. The common ground brush is positioned at 0°. The **Low-Speed brush** is placed at 180° (utilizing all armature windings for maximum counter-electromotive force and maximum torque at ~45 RPM [TYPICAL]). The **High-Speed brush** is positioned at ~120° (bypassing a portion of the windings to increase current and rotational speed to ~65 RPM [TYPICAL]).
2. **Self-Locking Worm Drive**: The motor shaft terminates in a precision-ground steel worm screw that drives a heavy nylon or bronze spur wheel. **You cannot back-drive the shaft by hand.** When power is cut, the output shaft remains physically locked in place under load.
3. **Internal Park Switch**: A mechanical copper wiper arm rides on a rotating circular conductive track inside the gearbox. The circuit breaks only when the crank reaches its exact mechanical resting "park" position.

---

### Step-by-Step Benchtop Wiring & Speed Hookup:
- **Test with Multimeter**: Set to Ohms (Ω). Touch one probe to the metal motor chassis (Chassis Ground). Probe each wire in the plug:
  - The wire with **lowest resistance to case** (typically ~1.0 Ω to 1.5 Ω) is **High Speed**.
  - The wire with **slightly higher resistance to case** (typically ~1.8 Ω to 2.5 Ω) is **Low Speed**.
  - The remaining two wires show infinite resistance until the shaft turns; these are your **Park Switch** contacts.
- **Bi-Directional Driving**: To reverse direction, the motor must be electrically isolated from chassis ground (in many wiper motors, the negative brush is spot-welded to the outer metal casing. Drill out or desolder this ground strap and run a dedicated negative wire out of the housing to pair with a BTS7960 H-Bridge).

---

### Creative Repurposing Exploits:

```
Automated Chicken Coop Door / Security Trapdoor:
  +-------------------------------------------------------+
  | [Wiper Motor Output Arm]                              |
  |         |                                             |
  |         v                                             |
  |    (Steel Cable)                                      |
  |         |                                             |
  |         v                                             |
  |  +==============+  <--- Vertical Sliding Predator-    |
  |  | Heavy Oak /  |       Proof Door                    |
  |  | Steel Door   |                                     |
  |  +==============+                                     |
  +-------------------------------------------------------+
```

#### A. Predator-Proof Automatic Chicken Coop / Greenhouse Door
- Raccoons, foxes, and predators routinely pry open automated chicken coop doors operated by simple gravity strings.
- Because a wiper motor uses a non-backdriveable worm gear, pairing it with a linkage arm or rack-and-pinion means **no animal on Earth can force the door upward**.
- Wire an Arduino with a photoresistor (LDR) to detect dusk and dawn. Use the wiper motor's internal park switch to halt the motor automatically at top and bottom dead center.

#### B. Heavy-Payload Dual-Axis Solar Tracker
- A 400-Watt solar panel array weighs 50 to 80 lbs and acts like a sail in windstorms.
- Two wiper motors (one for East-West azimuth, one for North-South elevation) provide ample torque to orient the array smoothly across the sky.
- Under 60 MPH wind gusts, the worm gearboxes lock rigidly, consuming zero electrical standby current while resisting hundreds of pounds of wind-buffeting force.

#### C. Continuous Heavy-Duty BBQ Spit Roaster
- Bolt the wiper motor directly to a food-grade stainless steel spit rod using a rubber spider coupling.
- Run on 5V DC (from an old phone charger or ATX PSU) to drop the speed down to an ideal, ultra-quiet **15 to 20 RPM [TYPICAL]**. Easily turns a whole 60 lb pig or lamb for 12 hours straight without heating up.

---

## 2. Power Window Regulators

```
Scissor vs. Cable Window Mechanism:
  [12V Compact DC Motor] ---> (Worm Reducer) ---> [Cable Drum / Sector Gear]
                                                        |
                                                        v
                                             [Lifts 40-70 lb Glass Panel]
```

### Harvestable Characteristics:
- **Form Factor**: Extremely flat (often under 1.25 inches / 32mm thick).
- **Lifting Capacity**: Designed to lift a heavy car window glass through tight weatherstripping friction (rated for 40 to 80 lbs of direct vertical lift).
- **Repurposing**:
  - **Motorized Drop-Down TV / Monitor Ceiling Mount**: Use two matching left/right window regulators to build a motorized ceiling flap that conceals a computer monitor flush against the ceiling when not in use.
  - **Secret Bookcase / Furniture Latch**: Conceal the regulator inside a bookshelf to slide open a hidden false wall or sliding compartment at the press of an RFID badge.

---

## 3. Power Seat Track Actuators (Precision 12V Screw Jacks)

```
Power Seat Linear Screw Jack:
  [12V High-Torque Motor] ===> [ACME Threaded Leadscrew (8"-12" Stroke)]
                                              |
                                              v
                                   [Heavy Bronze Lead Nut]
                                   (500+ lbs Dynamic Thrust)
```

### Harvestable Characteristics:
- Cars with 8-way or 10-way power seats contain two to three independent, heavy-duty linear screw-drive actuators.
- Each actuator consists of a small, high-torque permanent magnet DC motor driving a hardened steel ACME leadscrew through an internal worm reduction box.
- Dynamic thrust: **300 to 600 lbs**; static holding capacity: **1,000+ lbs**.

### Repurposing Exploits:
- **Motorized Woodworking Router Lift**: Mount a seat track actuator vertically under your router table. Wire an up/down momentary toggle switch on the front apron to adjust router bit cutting height to within 0.1 mm precision without reaching under the table.
- **Snowblower Chute Deflector & Rotation**: Remote-control the angle and throw direction of your snowblower chute from the comfort of the heated tractor cab using 12V seat actuators.
- **Micro-Tractor / Mower Deck Elevation**: Electrify the manual lifting lever on lawn tractors to raise heavy mowing decks or front snow blades at the touch of a thumb switch.

---

## 4. Automotive Door Lock Solenoids & Actuators
- **Characteristics**: Compact rack-and-pinion linear actuators delivering a 0.75-inch (19mm) stroke with 10 to 15 lbs of force in **50 milliseconds**.
- **Repurposing**:
  - **Automated Sentry Airsoft / Paintball Turret Trigger**: Mount the actuator arm directly behind the trigger shoe of an airsoft marker to achieve instantaneous electronic semi-auto firing controlled by computer vision.
  - **Emergency Drop-Pin Safety Latches**: Serves as a spring-loaded mechanical interlock pin for pneumatic elevators, counterweights, and automated gates.
