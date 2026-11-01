# 🔬 Volume 5.1: Lab Salvage, Sensors & Structural Electromechanics
*Medical syringe pumps, barcode polygonal LiDAR, ATX power lab stations, and acoustic levitation.*

---

## 1. Medical & Laboratory Scrap Goldmine

```
Medical Infusion Syringe Pump Architecture:
+-------------------------------------------------------------+
| [Bipolar Micro-Stepper] ===(Ground Ball-Screw)===> [Carriage]|
|                                                      |      |
|                                       [Syringe Plunger Clamp]
|                                       [Linear Slide Bushing]|
|                                       [Optical Force Sensor]|
+-------------------------------------------------------------+
```

### A. Infusion Syringe Pumps
Medical syringe pumps are engineered to deliver micro-liters of medication per hour with life-critical accuracy.
- **Hardware**: Zero-backlash, ground micro-metric leadscrew, miniature high-step-angle hybrid stepper, precision linear rails, and optical force-limit sensors.
- **Repurposing Projects**:
  - **Automated Solder Paste & Flux Dispenser**:
    - Mount a standard 10cc or 30cc syringe filled with SMD solder paste or liquid tacky flux into the carriage.
    - Wire an Arduino with an A4988 driver connected to a foot-switch pedal.
    - Pressing the foot switch advances the leadscrew by exact microsteps (e.g., 20 microsteps), dispensing repeatable, microscopic solder paste dots on 0402 surface-mount PCB pads with zero mess or dripping.
  - **Precision Hydroponic pH & EC Micro-Dosing**:
    - Accurately meters concentrated phosphoric acid or nutrient solutions down to single drops (0.05 mL) into hydroponic reservoir tanks based on live pH sensor readings.

### B. Peristaltic Pumps (From Dialysis & Chemical Scrubbers)
- **Mechanism**: A rotor with 3 or 4 rollers compresses a flexible silicone tube. Fluid is moved via peristalsis and **never touches any mechanical parts or seals**.
- **Repurposing**:
  - **Automated Cocktail Drink Mixer ("BarBot")**: Multiple peristaltic pumps meter out spirits, syrups, and juices to the exact milliliter without contamination or sticky valve clogs.

### C. Laboratory Centrifuges
- **Hardware**: Heavy dynamically balanced rotors driven by high-speed brushless motors.
- **Repurposing**:
  - **DIY Spin Coater for Thin-Film Nanotechnology**: Mount a small vacuum chuck to the spindle. Drop liquid photoresist, conductive polymer, or graphene dispersion onto a glass slide or silicon wafer; spin at 4,000 RPM [TYPICAL] for 30 seconds to produce a uniform film just nanometers thick.

---

## 2. Optical Sensors & Ultrasonic Transducers

```
Polygonal Mirror LiDAR Architecture:
  [Laser Diode] ---> [Rotating 8-Sided Polygonal Mirror] ===> [Sweeping Beam (360°)]
                                   ^                                |
                                   |                                v
                    [15,000 RPM [TYPICAL] Brushless Motor]            [Target Object]
                                                                    |
  [High-Speed Photodiode] <=========================================+
```

### A. Barcode Scanner Polygonal Mirror Motors
- **Hardware**: An 8-sided or 12-sided optical polygonal mirror block mounted to an ultra-precise brushless DC motor running at 10,000 to 25,000 RPM [TYPICAL] with phase-locked rotational stability.
- **Repurposing**:
  - **360° Planar Optical LiDAR Scanner**: Sweep a focused time-of-flight (ToF) laser rangefinder beam across a room to generate real-time 2D spatial point clouds for autonomous robot vacuum mapping.

### B. Ultrasonic Humidifier Ceramic Piezo Transducers
- **Hardware**: High-frequency piezoelectric ceramic disks resonating at 1.7 MHz to 2.4 MHz.
- **Repurposing**:
  - **Acoustic Levitation (Standing Wave Tractor Beam)**: Arraying opposing ultrasonic transducers creates standing acoustic waves with high-pressure nodes that suspend water droplets, small beads, or insects motionless in mid-air.
  - **Aeroponic Root Fogging**: Disintegrates water and plant nutrients into an ultra-fine 5-micron dry fog that delivers maximum oxygen directly to suspended roots.

---

## 3. Power & Structural Hardware: The ATX Bench Power Supply

```
ATX 24-Pin Connector Conversion:
+-------------------------------------------------------------+
| Green Wire (Pin 16: PS_ON) ---> Connect to Black Wire (GND) |
|                                 (Turns power supply ON!)    |
|                                                             |
| Yellow Wires  ---> +12V Rail (Typically 30A to 50A!)        |
| Red Wires     ---> +5V Rail  (Typically 20A to 30A)         |
| Orange Wires  ---> +3.3V Rail (Typically 15A to 25A)        |
| Black Wires   ---> Common Ground                            |
+-------------------------------------------------------------+
```

### The Free 500W High-Current Benchtop Lab Station:
Discarded computer desktop ATX power supplies are among the most versatile resources on Earth.
1. Clip the green wire (`PS_ON`) and connect it through a toggle switch to any black wire (`GND`). Flipping this switch turns on the power supply without needing a computer motherboard.
2. Solder banana plug binding posts to:
   - **Yellow (+12V)**: Powers heavy windshield wiper motors, drill motors, and audio amplifiers.
   - **Red (+5V)**: Powers microcontrollers, logic circuits, and USB devices.
   - **Orange (+3.3V)**: Powers low-voltage ESP32, STM32, and Raspberry Pi boards.
   - **Black (GND)**: Common ground.
3. Features built-in short-circuit and over-temperature shutdown protection, making it virtually impossible to destroy on your test bench.

---

## 4. CPAP & BiPAP Brushless Micro-Turbines: Extreme Static Pressure

Continuous Positive Airway Pressure (CPAP) and BiPAP medical ventilators are frequently found at estate sales, thrift stores, and electronics bins for $5 to $15. Because these devices are engineered to pressurize human lungs silently at a patient's bedside, they contain an extraordinary electromechanical masterpiece:

```
+-------------------------------------------------------------------------+
| Disassembled CPAP Blower Unit:                                         |
|                                                                         |
| [ Sound-Deadening Silicone Shell ]                                     |
|    \---> [ 3-Phase Sensorless BLDC Motor ] (30,000 - 60,000 RPM [TYPICAL])       |
|    \---> [ Precision Magnesium/Composite Centrifugal Impeller ]        |
|    \---> [ Spiral Volute Casing with 22mm ISO Hose Port ]               |
|                                                                         |
| Performance: >60 cmH2O (>6 kPa) Static Pressure @ Under 30 dBA Audible |
+-------------------------------------------------------------------------+
```

### A. Why CPAP Blowers Crush Standard Axial PC Fans
Standard 120mm computer axial fans move reasonable air volume ($50\text{ to }100\text{ CFM}$) only in **free, unconstrained air**. The moment they encounter an airflow restriction (such as a true fiberglass HEPA filter, a thick bed of activated carbon pellets, or a vacuum tube), their static pressure is tiny ($\sim 2\text{ to }4\text{ mmH}_2\text{O}$), causing them to stall and churn air uselessly without pulling flow.

A CPAP centrifugal micro-turbine, by contrast, operates like a miniature industrial turbocharger. Its backward-curved centrifugal blades generate **over $60\text{ cmH}_2\text{O}$ ($6\text{ kPa}$ or $\sim 0.9\text{ PSI}$) of static vacuum pressure**, allowing it to force air through dense filter media or pull high vacuum through narrow needle orifices.

### B. Driving the 3-Phase Sensorless Motor
The blower is a 3-wire, 3-phase sensorless brushless motor wound for low inductance and high RPM:
- Drive it using a cheap **20A to 30A multirotor RC Electronic Speed Controller (ESC)** powered by $12\text{V to }24\text{V DC}$.
- Feed the ESC a standard $50\text{ Hz}$ PWM servo signal ($1.0\text{ ms to }2.0\text{ ms}$ pulse width) generated by an Arduino, a 555 timer servo tester, or a dedicated potentiometer module.

### C. Repurposing Exploits:
1. **Zero-Odor HEPA & Activated Carbon Fume Extractor**: Pulls rosin fumes, flux smoke, and noxious VOCs through a genuine multi-stage gas mask filter cartridge or a 2-inch packed bed of activated carbon pellets right at your soldering iron tip without deafening fan noise.
2. **SMD Vacuum Pick-and-Place Pen**: Couple the inlet hose through a miniature foot-pedal valve to a syringe needle fitted with a silicone suction cup. Provides instant, high-grip vacuum holding for placing 0402 resistors and dense BGA microchips.
3. **Micro-CNC Vacuum Hold-Down Table**: Draws vacuum across a porous MDF or grid plate to clamp paper-thin brass, copper-clad FR4 PCBs, and carbon fiber sheets flat during engraving without double-sided tape (see **Blueprint 15**).

---

## 5. 3D Printer & CNC Scrap: Precision Strain Gauge Load Cells

Scrapped FDM 3D printers (e.g., Anycubic Vyper, Creality CR-6, Prusa XL) and lab scales contain miniature aluminum **Wheatstone bridge strain gauge load cells** (typically rated for $1\text{ kg, }5\text{ kg, or }10\text{ kg}$):

```
       [ Fixed Mounting End ]                                 [ Load Application ]
          +-----------------------+-----------------------+--------+
          |       (Gauge R1)      |      (Gauge R2)       |        |
          |          /\/\/\       |         /\/\/\        |        v Force (F)
          |                       |                       |
          |          \/\/\/       |         \/\/\/        |
          |       (Gauge R3)      |      (Gauge R4)       |
          +-----------------------+-----------------------+
```

### A. Working Principle & Signal Conditioning
Four metallic foil strain gauges are bonded to the upper and lower surfaces of a machined aluminum parallel-beam flexure. Deflection causes minute micro-strain variations that unbalance the Wheatstone bridge, producing a millivolt-scale differential signal.
- Interfacing: Pair the 4-wire bridge with an inexpensive **HX711 24-bit Analog-to-Digital Converter (ADC)** board ($1 on Amazon/AliExpress).
- Resolution: Reading over 24 bits provides resolution down to **0.01 grams** when mechanically isolated.

### B. Repurposing Exploits:
1. **Sub-Gram Epoxy & Casting Resin Scale**: Allows precise stoichiometric ratio mixing of 2-part polyurethane, structural epoxy, and silicone rubber in tiny garage batches.
2. **Brushless Motor Thrust Stand**: Mount a multirotor motor on a hinged L-bracket pressing against the load cell to log exact thrust curves in grams vs electrical wattage.
3. **Alternator Dynamometer Torque Sensor**: Fix the load cell to the reaction torque arm of an automotive alternator dyno cradle (detailed in Blueprint 11) to measure real engine output torque with laboratory precision.

---

## 6. Medical Oxygen Concentrators: Pressure Swing Adsorption (PSA)

Home medical oxygen concentrators (Respironics EverFlo, Invacare Perfecto, DeVilbiss) are frequently discarded by durable medical equipment liquidators when an internal sensor drifts or a solenoid valve jams:

```
        +-------------------------------------------------------------+
        | Medical PSA Oxygen Generation Core:                         |
        |                                                             |
        | [ 120V AC [TYPICAL] 1/3 HP Oil-Free Twin Wobble-Piston Compressor ]   |
        |                           |                                 |
        |                           v (20-30 PSI Air)                 |
        |            [ 4-Way Motorized Spool Valve ]                  |
        |                   /               \                         |
        |                  v                 v                        |
        |     [ Sieve Bed A (13X Zeolite) ]   [ Sieve Bed B ]         |
        |     (Adsorbs N2 under pressure)     (Vents N2 to exhaust)   |
        |                  \                 /                        |
        |                   v               v                         |
        |     ===> 93% to 95% Pure Oxygen Stream (5 to 10 LPM)        |
        +-------------------------------------------------------------+
```

### A. The Pressure Swing Adsorption (PSA) Physics:
Air consists of approximately 78% Nitrogen ($N_2$) and 21% Oxygen ($O_2$). 
- The aluminum columns are packed with **13X Zeolite molecular sieve beads** (synthetic crystalline sodium aluminosilicate with precise $10\text{-angstrom}$ micro-pores).
- Under pressure ($20\text{ to }30\text{ PSI}$), the quadrupole moment of nitrogen molecules causes them to bond physically to the zeolite crystal lattice (**adsorption**), while non-polar oxygen passes through unimpeded.
- When the bed reaches nitrogen saturation, the 4-way valve flips: the bed is vented to atmospheric pressure, releasing the trapped nitrogen gas in a loud "whoosh" exhaust puff (**desorption**), regenerating the sieve bed for the next cycle.

### B. Repurposing Exploits:
1. **$2,600^\circ\text{C}$ High-Temperature Oxy-Propane Glassworking & Brazing Torch**:
   - High-temperature borosilicate lampworking (Pyrex) and tungsten carbide tool brazing require pure oxygen; compressed air cannot reach the required temperatures.
   - Routing the 93% $O_2$ output stream alongside cheap barbecue tank propane into a surface-mix glass torch produces a razor-sharp, whisper-quiet flame reaching **$2,500^\circ\text{C}$ to $2,800^\circ\text{C}$** without ever renting, transporting, or refilling hazardous 2,200 PSI industrial oxygen tanks (see **Blueprint 16**).
2. **High-Concentration Corona Discharge Ozone Generator**:
   - Feeding pure dry oxygen into a high-voltage corona cell yields $5\times$ higher ozone production than ambient air without generating toxic nitric oxide ($NO_x$) byproducts, perfect for chemical sterilization and water purification.

---

## 7. Semiconductor Thermal Mass Flow Controllers (MFCs)

Scrapped from semiconductor wafer processing chambers and biotechnology bioreactors (brands: MKS Instruments, Brooks, Horiba, Unit):

```
       Gas In ---> [ Laminar Flow Bypass Tube ] ---------------> Gas Out
                         |                     ^
                         v                     |
              [ Sensor Capillary Tube ]   [ Proportional Valve ]
              (Heater + Dual Temp Sense)  (Piezo or Solenoid)
```

### A. Thermal Capillary Mass Measurement
- An internal capillary tube is wrapped with a resistance heater flanked by upstream and downstream platinum resistance temperature detectors (RTDs).
- Gas flowing through the tube carries heat downstream; the temperature differential ($\Delta T$) is directly proportional to **true mass flow rate** regardless of ambient pressure or temperature fluctuations.
- An onboard analog or digital PID loop drives a proportional electromagnetic or piezoelectric diaphragm valve to maintain gas flow with accuracy down to **standard cubic centimeters per minute ($sccm$)**.

### B. Repurposing Exploits:
- **Precision Shielding Gas Blender for Exotic TIG Welding**: Mix customized shielding mixtures (e.g., 95% Argon / 5% Hydrogen for nickel alloys, or Argon/Helium blends for thick aluminum) with precision digital control rather than inaccurate ball-float rotameters.
- **Atmospheric Chemical Vapor Deposition (CVD) Furnace**: Accurately meters volatile precursor vapors and carrier gases when growing graphene or carbon nanotubes in a quartz tube furnace.

---

## 8. Enterprise Server Racks: Counter-Rotating Blowers & Giant UPS Toroids

Data center surplus bins yield two high-value power and airflow components:

### A. Counter-Rotating Dual-Rotor Axial Fans (Delta / San Ace)
- **Architecture**: Two high-speed BLDC motors placed back-to-back in a single 40mm or 80mm aluminum housing, turning **counter-rotating impellers** (front clockwise, rear counter-clockwise).
- **Aero Physics**: The second rotor straightens the turbulent swirl generated by the first, converting rotational energy directly into **insane static pressure ($>3\text{ to }5\text{ inches of }H_2O$)** while drawing 3A to 6A at 12V DC [TYPICAL].
- **Exploits**: High-pressure blast air supply for crucible foundry tuyeres, oil burners, and extreme-density electronic load banks.

### B. Giant Silicon-Steel Toroidal Inverter Transformers (APC Smart-UPS)
- Discarded 1,500VA to 3,000VA enterprise rackmount UPS units contain massive, low-loss **silicon-steel toroidal core transformers** weighing 20 to 45 lbs.
- **Exploits**:
  - Rewind the low-voltage secondary with 2 turns of 0000 AWG cable for an indestructible high-current AC resistance spot welder that outperforms microwave transformers by a factor of three.
  - The ultimate low-idle-current output transformer for building heavy DIY pure-sine-wave 48V off-grid solar inverters.

---

## 9. "Sacrificial Vein" Self-Diagnosing Structural Flexures

In composite machine gantries and 3D-printed robot links, catastrophic fatigue failure occurs without visible exterior deformation:

```
  [ Machine Axis Structural Matrix (Epoxy Granite / Carbon Plate) ]
  -----------------------------------------------------------------
  ========== [ SACRIFICIAL CONDUCTIVE SENSING VEIN ] ==============
  -----------------------------------------------------------------
  (Embedded 40 AWG enameled copper wire along highest shear stress plane)
```

- **The Exploit**: Embed a continuous strand of 40 AWG enamel magnet wire or a screen-printed conductive carbon line directly along the highest-stress tensile or shear concentration plane during part layup.
- **Predictive Interruption**: Under cyclic vibration, microscopic shear fatigue micro-cracks the brittle sensing trace hours before the primary structural matrix parts. An analog comparator monitors trace resistance; a sudden open-circuit alerts the CNC controller to park the spindle and initiate an orderly shutdown before an axis crashes.
