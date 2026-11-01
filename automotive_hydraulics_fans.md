# 💨 Volume 2.3: Automotive Hydraulics, High-Flow Blowers & Actuators
*Harvesting 2,000 PSI ABS hydraulic pumps, 3,000 CFM radiator fans, and electronic throttle servos.*

---

## 1. ABS Hydraulic Pump Modules: Micro-Hydraulic Powerhouses

```
ABS Pump Assembly Cutaway:
  +-----------------------------------------------------------+
  | [12V Heavy PMDC Motor]                                    |
  |            |                                              |
  |       (Eccentric Cam)                                     |
  |            |                                              |
  |            v                                              |
  | [Dual Miniature Piston Pumps inside Machined Aluminum Block]
  |            |                                              |
  |            v                                              |
  | ====> Produces 1,500 to 2,200 PSI Hydraulic Pressure!     |
  +-----------------------------------------------------------+
```

### What Makes Them Remarkable:
Every modern car Anti-lock Braking System (ABS) module contains a precision 12V DC [TYPICAL] electric motor mounted to a solid billet aluminum valve block.
- Inside the aluminum block is an eccentric camshaft that drives two opposing, hardened steel micro-pistons.
- These pumps are engineered to generate instantaneous hydraulic pressures between **1,500 PSI and 2,200 PSI (100 to 150 Bar)** to actuate brake calipers during emergency stops.

### Creative Repurposing Exploits:
- **Desktop DIY Hydraulic Press / Metal Forming Brake**:
  - Plumb the high-pressure output of an ABS pump block into a small single-acting hydraulic ram (e.g., from an 8-ton bottle jack or micro cylinder).
  - Actuated by a 12V foot switch, this compact setup easily generates 2 to 5 tons of pressing force to press bearings, punch sheet metal holes, or bend 1/4" steel brackets on a kitchen tabletop.
- **Scale-Model Hydraulic Excavator / Battlebot Actuators**:
  - RC and combat robotics builders use salvaged ABS pumps as the central hydraulic power unit for heavy-lifting robotic digging arms and hydraulic crushing jaws.

---

## 2. Automotive Radiator Fans & HVAC Blowers

```
Cooling Fan vs. Squirrel-Cage Blower:
  Axial Radiator Fan:                 Centrifugal HVAC Blower:
    - High CFM (2,000 - 3,500 CFM)      - High Static Pressure
    - Low Static Pressure               - Overcomes Duct & Filter Resistance
    - Moves Massive Free Air Volume     - Ideal for Dust Filters & Forges
```

### A. High-CFM Radiator Cooling Fans:
- **Specs**: 12V–14V DC, 10A to 25A draw. Fully weather-sealed permanent magnet DC motor spinning high-efficiency curved aerodynamic blades.
- **Airflow**: 1,800 to 3,500 Cubic Feet per Minute (CFM).
- **Repurposing**:
  - **Shop Spray Booth / Fume Evacuation**: Mount into a window frame with a standard furnace air filter to evacuate volatile paint and resin fumes outside in seconds.
  - **DIY Hovercraft Lift Fan**: Mount vertically inside a duct with an aerodynamic skirt. The massive airflow creates the air cushion required to lift a 150 lb rider off the ground over smooth concrete or grass.

### B. HVAC Centrifugal "Squirrel-Cage" Blowers:
- **Specs**: 12V DC [TYPICAL] multi-speed motor coupled to a forward-curved squirrel cage impeller.
- **Why It Matters**: Unlike axial fans that stall when encountering resistance, centrifugal blowers generate substantial **static pressure**—meaning they can force air through tight ducts, filters, and coal beds without losing velocity.
- **Repurposing**:
  - **Blacksmith Forge Blast Air Supply**: Connect the blower outlet to a 2" steel pipe leading into the bottom of a charcoal or coal forge. A simple 12V PWM motor controller provides precise air velocity adjustment to heat forge iron up to white-hot welding temperatures (2,300°F+).
  - **Woodworking Downdraft Sanding Table**: Mount underneath a pegboard tabletop to suck toxic wood dust downward directly into a collection bag before it reaches your lungs.

---

## 3. Electronic Drive-by-Wire Throttle Bodies (ETB)
Modern fuel-injected engines no longer connect the gas pedal to the intake manifold with a cable; they use an **Electronic Throttle Body**.
- **Internal Hardware**: High-speed, high-torque 12V DC [TYPICAL] servo motor, multi-stage reduction gears, heavy return spring, and dual redundant Hall-effect position sensors (TPS).
- **Repurposing**:
  - **Automated Wood Stove / Smoker Draft Damper**: Couple the throttle body to your barbecue smoker or wood-burning stove intake. An ESP32 reading a meat or pit thermocouple modulates the throttle plate from 0% to 100% to maintain cooking temperatures within ±1°F for 16-hour brisket smokes.
  - **Emergency Pneumatic Air-Shutoff Valve**: Acts as an instant fail-safe intake choke for diesel engines or industrial blowers to prevent engine runaway.

---

## 4. Heavy Diesel Variable Geometry Turbochargers (VGT)

Discarded or core-return heavy diesel truck turbochargers—most notably the **Holset HE351VE** from 6.7L Cummins Ram trucks—are widely available at scrap yards and diesel repair shops. Beyond standard fixed-vane turbos, the HE351VE contains advanced aerodynamic, thermal, and electronic servo systems:

```
        +-----------------------------------------------------------+
        | Holset HE351VE VGT Architecture:                          |
        |                                                           |
        | [ Inconel 713C Turbine Wheel ] (Survives 950°C Gas Temp)  |
        | [ Forged Billet Aluminum Compressor Wheel ] (>120,000 RPM [TYPICAL])|
        | [ Sliding Vane Unison Ring ] (Alters A/R Ratio on Fly)    |
        | [ 24V Smart Brushless Servo Actuator ] (CAN-Bus Converted)|
        +-----------------------------------------------------------+
```

### A. The Inconel Superalloy Core
- **Turbine Wheel**: Cast from **Inconel 713C** (a nickel-base precipitation-hardenable superalloy containing chromium, molybdenum, and aluminum). Unlike steel or cast iron, Inconel maintains full tensile yield strength at bright red heats ($950^\circ\text{C} / 1,740^\circ\text{F}$), resisting creep, oxidation, and centrifugal explosion at 130,000 RPM [TYPICAL].
- **The Unison Ring**: A rotating internal cage linked to aerodynamic stator nozzles. Rotating the ring varies the effective exhaust housing nozzle area ($A/R$ ratio), choking the exhaust flow to spool the compressor instantaneously at low gas velocities, then opening wide to prevent exhaust backpressure.

### B. Hacking the Electronic Actuator
The stock 24V DC [TYPICAL] actuator incorporates an internal micro-controller with J1939 CAN-bus communications:
- By transmitting standard 250 kbps CAN packets from an Arduino with an MCP2515 transceiver shield, you can command exact millimeter positioning of the sliding nozzle ring.
- Alternatively, strip the factory electronic housing and drive the internal sector gear with an external NEMA 23 stepper or high-torque RC servo.

### C. Repurposing Exploits:
1. **DIY Micro-Gas-Turbine Jet Engine (Brayton Cycle)**:
   - Mount the turbocharger to a rigid steel test stand with an auxiliary 12V high-pressure oil pump ($40\text{ to }60\text{ PSI}$) lubricating the journal bearings.
   - Fabricate an external reverse-flow combustion chamber from a spent stainless-steel fire extinguisher body.
   - Feed liquid propane or atomized diesel through a spray nozzle ignited by a stun-gun spark module.
   - Compressed air from the compressor wheel feeds the combustion can; the burning expansion gases blast through the Inconel turbine wheel.
   - Adjusting the VGT actuator nozzle ring enables the turbine to **bootstrap into self-sustaining idle** with zero starter assistance, producing **30 to 50 lbs of continuous static jet thrust**!
2. **Extreme Static-Pressure Blast Furnace Blower**:
   - Drive the compressor side using a salvaged 5 HP electric motor or 2-stroke engine to deliver over **20 PSI of boost air** into an iron foundry cupola, reaching temperatures exceeding $1,600^\circ\text{C}$ to melt high-carbon steel scrap effortlessly.

---

## 5. Camshaft Variable Valve Timing (VVT) Oil Control Spool Valves

Every modern fuel-injected engine cylinder head (Toyota 1NZ/2AZ, Honda K-Series, Ford Coyote) features 1 to 4 slide-in **Variable Valve Timing (VVT) Oil Control Valves (OCV)** easily harvested for $5 at automotive self-service junkyards:

```
        +-------------------------------------------------------------+
        | High-Speed Proportional Hydraulic Spool Valve (OCV):        |
        |                                                             |
        | [ 12V DC [TYPICAL] Low-Inductance Solenoid Coil (150-300 Hz PWM) ]    |
        |                           |                                 |
        |                           v                                 |
        | [ Hardened Micro-Lapped 4-Way 3-Position Steel Spool ]      |
        |                           |                                 |
        |    Port P (Pressure In)   |   Port T (Tank Return Out)      |
        |    Port A (Cylinder Ext)  |   Port B (Cylinder Retract)     |
        |                           |                                 |
        | ====> Sub-Millimeter Proportional Hydraulic Servo Control!  |
        +-------------------------------------------------------------+
```

### A. The Precision Spool Geometry:
- Unlike simple on/off solenoid valves, a VVT valve is a **precision-machined 4-way, 3-position proportional hydraulic spool valve**.
- Ground to tolerances under 3 microns inside a hardened steel sleeve, it controls oil flow to the intake/exhaust cam phaser cavities.
- Designed to modulate continuous hydraulic engine oil pressure ($30\text{ to }100\text{ PSI}$) at **150 Hz to 300 Hz PWM frequency**, providing continuous proportional flow metering proportional to PWM duty cycle.

### B. The Closed-Loop Electro-Hydraulic Servo Exploit:
- Pair two VVT valves with an **automotive 12V ABS hydraulic pump block** (Section 1) and a hydraulic cylinder fitted with a linear caliper encoder.
- Driven by an ESP32 or Arduino PID algorithm, this combination creates an industrial-grade **electro-hydraulic servo actuator** capable of positioning a 3-ton load with **$0.05\text{ mm}$ repeatability** at a tiny fraction of the cost of commercial Moog proportional servo valves (detailed in **Blueprint 20**)!

---

## 6. Luxury Car Air-Suspension Compressors (Wabco / AMK / Continental)

Harvested from junked luxury air-ride vehicles (Mercedes S-Class/E-Class, Range Rover Sport, BMW X5, Audi A8):

```
        +-----------------------------------------------------------+
        | Wabco Luxury Air Suspension Unit Architecture:            |
        |                                                           |
        | [ High-Torque 12V DC [TYPICAL] Sealed Motor ]                       |
        |                            |                              |
        |                            v                              |
        | [ Two-Stage Oil-Free Piston Pump: 200 - 260 PSI (18 Bar) ]|
        |                            |                              |
        |                            v                              |
        | [ Integrated Regenerative Silica-Gel Desiccant Dryer ]    |
        |                            |                              |
        |                            v                              |
        | ====> Bone-Dry, Oil-Free High-Pressure Pneumatic Air!     |
        +-----------------------------------------------------------+
```

### A. The Regenerative Desiccant Core:
- Commercial shop air compressors require expensive coalescing filters and refrigerated air dryers to remove moisture that ruins plasma torches and pneumatic air tools.
- Luxury air suspension compressors incorporate an **integrated silica-gel desiccant canister**. 
- Whenever the vehicle vents air to lower ride height, dry exhaust air reverses through the canister, continuously stripping moisture out of the beads and venting it outside (**regenerative desorption**). The desiccant never requires baking or replacement!

### B. Repurposing Exploits:
- **Mobile Plasma Cutter Air Supply**: Supplies clean, dry, oil-free 120 PSI air directly from a service truck's 12V battery, allowing clean CNC plasma cutting on remote job sites without a bulky gas generator.
- **Extreme-Pressure Pneumatic Robot Muscle Drivers**: Provides the 200 PSI pressure required to power high-density McKibben pneumatic artificial muscles and fast pneumatic robot flippers.
