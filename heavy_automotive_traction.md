# ⚡ Volume 2.2: Heavy Automotive Electromechanics & Traction
*Converting alternators into 5 HP brushless beasts, EPS columns into direct-drive sim wheels, and taming starter motors.*

---

## 1. The Car Alternator: From Generator to High-Power Brushless Motor

```
Alternator BLDC Conversion Topology:
+------------------------------------------------------------------------+
|                                                                        |
|  [Rotor Field Slip Rings] <--- External 12V DC [TYPICAL] (Field Excitation)      |
|                                                                        |
|  [3-Phase Stator (U, V, W)] <--- (48V–72V 100A 3-Phase E-Bike ESC)     |
|          |                                                             |
|          +==================> Delivers 5 to 7 HP @ 8,000+ RPM!        |
+------------------------------------------------------------------------+
```

### Why It Works:
A standard automotive alternator is mechanically and electromagnetically identical to an industrial 3-phase Permanent Magnet Synchronous Motor (PMSM), with one key difference: instead of permanent magnets on the rotor, it uses an **electromagnet (field coil)** fed through two carbon brushes and slip rings.

---

### Step-by-Step Conversion Procedure:
1. **Teardown & Rectifier Removal**:
   - Unbolt the through-bolts holding the alternator aluminum end-housings together.
   - Locate the internal diode rectifier bridge (usually 6 high-current press-fit diodes on a curved aluminum heat sink).
   - **Desolder or clip the three stator phase wires** from the rectifier. Discard or bypass the diode bridge and voltage regulator.
   - Solder three heavy, high-strand silicone wires (10 AWG or 8 AWG) directly to the three stator phase leads. Bring them outside the case as phases `U`, `V`, and `W`.
2. **Rotor Field Excitation**:
   - The two slip-ring brushes feed the claw-pole rotor coil.
   - Connect a switchable, fused 12V DC [TYPICAL] power source across these brushes. This energizes the rotor, creating alternating North and South magnetic poles across the rotor claws.
3. **Electronic Speed Controller (ESC) Connection**:
   - Connect the three heavy stator wires to a standard 48V to 72V, 100A+ brushless motor speed controller (such as a generic e-bike controller or high-power VESC).
4. **Operation**:
   - Energize the rotor with 12V DC [TYPICAL].
   - Apply throttle to the ESC.
   - The converted alternator spins up with breathtaking speed, producing up to **5,000 Watts (approx. 6.7 Horsepower)** of clean, smooth rotary power.

---

### Creative Engineering Projects:

#### A. Electric Go-Kart / Minibike Traction Drive
- Couple the modified alternator to a go-kart live axle via a 4:1 or 5:1 chain sprocket.
- Powered by a 48V lithium-ion battery pack, the motor propels an adult driver up to 35–45 MPH with immense low-end punch.

#### B. Off-Grid Engine-Driven Stick / TIG Welder
- Couple an unhacked alternator to a 6.5 HP horizontal-shaft gas engine (e.g., Predator 212cc) via a 2:1 speed-up pulley.
- Supply adjustable 0–12V excitation current to the rotor via a manual potentiometer.
- Connect heavy 2 AWG welding leads directly to the alternator's B+ output stud and chassis ground.
- Turning the potentiometer dial adjusts welding current smoothly from **40 Amps up to 140 Amps DC**—producing butter-smooth DC stick welding arcs in the field with zero mains power.

---

## 2. Electric Power Steering (EPS) Columns: Direct-Drive Sim Racing Wheel

```
EPS Force Feedback Sim Racing Architecture:
[PC Running Assetto Corsa / iRacing]
               |
         (USB Telemetry)
               v
[STM32 "BluePill" Running OpenFFB Firmware]
               |
         (PWM + Direction)
               v
[BTS7960 43A Driver or Discrete MOSFET Inverter]
               |
         (High-Current 12V)
               v
[EPS Steering Column Motor] ===> [Full-Size Race Steering Wheel]
*(Delivers 25-30 Nm [TYPICAL] Realistic Force Feedback Torque)*
```

### Why Commercial Sim Racers Fear This Hack:
High-end "Direct-Drive" force feedback steering wheels (Fanatec Podium, Simucube) cost between **$1,200 and $2,500**.
- Modern compact cars (e.g., Toyota Prius, Opel Corsa B/C, Nissan Versa) use column-mounted Electric Power Steering (C-EPS).
- An EPS unit consists of a high-power brushless servo motor coupled to the steering shaft through a precision, high-efficiency worm reduction gear, equipped with a torsion-bar torque sensor.
- A salvaged EPS column from a local auto scrap yard costs **$30 to $50**.

### Repurposing into an OpenFFB Racing Simulator:
1. **Mechanical Mounting**: Fabricate a heavy steel plate clamping the EPS housing to your sim rig or desk frame. Bolt a real aftermarket racing wheel directly to the splined input shaft.
2. **Electronics**:
   - Microcontroller: STM32F103C8T6 ("BluePill") running open-source **OpenFFB** or **MMOS** firmware.
   - Interfacing: The STM32 reads in-game physics telemetry (tire slip, curb rumble, weight transfer) over USB and calculates exact real-time counter-steering torque.
3. **Power Delivery**: Drive the EPS motor using a heavy 12V 50A server power supply through a BTS7960 H-Bridge module.
4. **Performance**: Produces **20 to 30 Nm [TYPICAL] of instantaneous steering torque**—enough force to physically rip the wheel out of your hands if you clip a curb at 150 MPH.

---

## 3. Automotive Starter Motors: Taming the Series-Wound Beast

```
Starter Motor Motor Characteristics:
  - Architecture: Series-Wound DC (Field coils in series with armature)
  - Voltage: 12V DC [TYPICAL]
  - Current: 150A to 300A continuous; 600A+ locked-rotor stall!
  - Output Power: 1.5 to 2.5 kW (~2 to 3.5 HP)
  - Duty Cycle: Strictly Intermittent (30 seconds ON / 5 minutes cooling)
```

### Safety & Mechanical Realities:
- **No-Load Runaway Hazard**: In a series-wound motor, magnetic field strength decreases as motor speed increases. If powered without any mechanical load attached, a starter motor will accelerate exponentially until centrifugal force **explodes the armature windings outward against the casing**. ALWAYS keep starter motors mechanically loaded.
- **Bushing Conversion**: The nose cone of a starter motor often lacks an internal bearing, relying on a bronze bushing pressed into the car's engine bellhousing. When salvaging a starter for standalone projects, select models with a **self-contained snout bearing**, or machine a custom bronze support carrier.

### Repurposing Exploits:
- **Ultra-High-Pull Off-Road Recovery Winch**: Mount a starter motor through a 100:1 planetary or worm reduction box to create an unstoppable 8,000 lb pulling winch for trailers and tractors.
- **Short-Track Dragster Launch Drive**: Delivers instantaneous, explosive torque off the line for junior dragsters and custom experimental vehicles.

---

## 4. Scrap Electric Vehicles (Leaf, Volt, Tesla): High-Voltage Mechatronics

Modern automotive junkyards and salvage auctions (Copart, IAAI) increasingly yield total-loss electric vehicles (Nissan Leaf, Chevrolet Volt/Bolt, Tesla Model S/3). Beyond their valuable lithium-ion battery modules (e.g., Leaf pouch cells or Tesla 18650/2170 modules), these donor vehicles contain industrial-grade high-voltage electromechanical safety hardware that is exceptionally difficult or costly to source commercially.

```
       +--------------------------------------------------------------+
       | EV Junction Box / Battery Disconnect Unit (BDU)              |
       |                                                              |
       |  (+) HV Bus in ---> [ 500A Sealed Contactor ] ----> HV Out (+) |
       |                           ^ (12V Coil)                       |
       |                           |                                  |
       |  [ Pre-Charge Relay ] - [ 30Ω-50Ω 100W Wirewound Resistor ]  |
       |                                                              |
       |  (-) HV Bus in ---> [ 500A Sealed Contactor ] ----> HV Out (-) |
       +--------------------------------------------------------------+
```

### A. Hermetically Sealed High-Voltage DC Contactors
- **Component**: Heavy-duty EV main contactors (Panasonic, Kilovac, Gigavac, or TE Connectivity).
- **Specs**: Rated for **400V to 900V DC continuous**, carrying **200A to 500A continuous (up to 2,000A interrupt capacity)** with a safe, isolated **12V DC [TYPICAL] coil**.
- **Internal Construction**: The contact chamber is hermetically sealed in a rugged ceramic enclosure backfilled with high-purity pressurized **nitrogen or hydrogen**. Rare-earth permanent magnets embedded beside the contacts produce transverse magnetic blowout fields that physically stretch and blast DC plasma arcs into ceramic splitter fins within milliseconds.
- **Repurposing Targets**:
  - **48V / 96V / 400V Off-Grid Solar Storage Master Disconnect**: Connects an entire whole-house battery bank to inverter arrays with complete arc-safe isolation during overcurrent or BMS fault events.
  - **Emergency Kill Switch for Heavy Inverters**: Provides true zero-wear galvanic disconnection that standard 120V AC [TYPICAL] contactors fail to perform under direct current.

### B. High-Power Wirewound Pre-Charge Resistors
- **Component**: Dale / Vishay aluminum-housed or ceramic tubular wirewound power resistors mounted on the EV junction block heatsink.
- **Specs**: Typically **30$\Omega$ to 50$\Omega$**, rated for **50W to 100W continuous**, capable of absorbing multi-kilowatt pulse inrush surges for 2–5 seconds without thermal breakdown.
- **Repurposing Targets**: Essential for building soft-start pre-charge networks in large capacitor-buffered DC systems, motor dynamometers, high-voltage spot welders, and EV retrofits.

### C. Ceramic PTC High-Voltage Cabin Heaters
- **Component**: PTC (Positive Temperature Coefficient) electric resistance heater blocks harvested from the HVAC module of Nissan Leafs or Chevy Volts.
- **Specs**: Operates directly at **300V to 420V DC**, drawing **3 kW to 6 kW** of thermal output. The ceramic barium titanate honeycomb elements are intrinsically self-regulating—their electrical resistance spikes exponentially above $220^\circ\text{C}$, making thermal runaway physically impossible even if airflow ceases.
- **Repurposing Targets**:
  - **High-Voltage Dynamic Braking & Dump Loads**: Safe, silent, passive dump load for off-grid wind turbines, hydro generators, or alternator dynamometer benches.
  - **Off-Grid Winter Workshop Space Heating**: Direct DC radiant space heating fed from high-voltage solar string arrays or stationary EV battery packs without inverter conversion losses.

---

## 5. Industrial Forklifts & Golf Carts: Series Traction & Albright Contactors

Scrapped electric pallet jacks, warehouse forklifts (Crown, Hyster, Raymond), and 36V/48V golf carts yield heavy industrial DC powertrains built for commercial continuous abuse:

```
        +-------------------------------------------------------------+
        | Heavy 48V Forklift Powertrain:                              |
        |                                                             |
        | [ 48V 300A-500A Series-Wound DC Traction Motor (8-15 HP) ]  |
        |                            |                                |
        |                            v (Massive Stall Torque: τ ∝ I²) |
        | [ Albright DPDT Dual Reversing Contactor Block ]            |
        |                            |                                |
        |                            v                                |
        | ====> Unstoppable 20-Ton Hydraulic & Winch Drives!          |
        +-------------------------------------------------------------+
```

### A. The Series-Wound Torque Beast
- In series-wound motors, the armature and field windings are in series. Motor current ($I$) flows through both, meaning electromagnetic torque scales quadratically:
  $$\tau \propto I^2$$
- At zero RPM (locked rotor stall), a 48V forklift motor draws 400+ Amps, producing an explosive **100+ Nm of instant starting torque**—enough to shear steel pins or climb steep loading ramps without stalling.

### B. Albright Heavy DPDT Reversing Contactors:
- These contactor bricks feature dual coils and four heavy silver-alloy contact tips that swap armature polarity to reverse rotation under full electrical load without welding.
- **Exploits**:
  - **20-Ton Electric Hydraulic Log Splitter**: Direct-couples to a 2-stage Haldex hydraulic gear pump, splitting gnarly oak and hickory logs in total silence inside an enclosed barn.
  - **Electrified Mini-Excavators & Yard Tractors**: Replaces unreliable, fumey 13 HP Honda gas engines with clean, silent 48V electric torque.

---

## 6. Hybrid & EV Hermetic Scroll Compressors (Prius / Leaf / Tesla)

Modern hybrid and electric vehicles do not drive their air conditioning compressor from an engine belt; they incorporate an internal high-voltage **3-phase Permanent Magnet Synchronous Motor (PMSM)** hermetically sealed directly inside an orbital scroll pump housing:

```
        +-----------------------------------------------------------+
        | High-Voltage Electric Scroll Compressor (Denso ES18/ES27):|
        |                                                           |
        | [ 3-Phase High-Voltage PMSM Stator (144V to 400V DC) ]     |
        |                            |                              |
        |                            v (Runs on 48V-72V VESC / ESC!)|
        | [ Precision Lapped Cast-Iron Orbital Scroll Spiral ]      |
        |                            |                              |
        |                            v                              |
        | ====> 15+ CFM Ultra-Quiet Air Output with ZERO Vibration! |
        +-----------------------------------------------------------+
```

### A. The Orbital Scroll Advantage:
- Unlike reciprocating piston compressors that clatter loudly and produce pulsating airflow, an orbital scroll compressor compresses air continuously through interleaved Archimedean spirals.
- **Vibration & Sound**: Operates at under **45 dBA**—you can stand next to it and whisper while it pumps high-pressure air!

### B. Running High-Voltage Compressors on Low Voltage:
- Although factory-rated for 200V–400V DC, the internal 3-phase PMSM motor runs smoothly on a cheap **48V to 72V e-bike controller or VESC**.
- Back-EMF is lower, meaning it spins at ~1,500 RPM [TYPICAL] rather than 6,000 RPM [TYPICAL], pumping a cool, continuous **8 to 12 CFM at 120 PSI** with immense mechanical efficiency.
- **Exploits**:
  1. **The Ultimate Silent Workshop Air Compressor**: Plumb into a 20-gallon air tank with an oil separator. Delivers continuous, high-volume pneumatic air for die grinders and sanders with zero piston noise.
  2. **Closed-Loop Organic Rankine Cycle (ORC) Expander**: Run in reverse as a high-efficiency vapor expander to generate electricity from geothermal hot water or solar-concentrated thermal loops.
