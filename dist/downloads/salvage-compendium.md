# The Master Electromechanical Salvage & Repurposing Compendium
*A comprehensive engineering handbook for harvesting, driving, and repurposing discarded motors, actuators, sensors, and electromechanical components.*

> [!IMPORTANT]
> ### Epistemic Status & Precision Engineering Standards
> All components in this Grand Master Matrix and corresponding Blueprints carry strict epistemological classification:
> - **`[VERIFIED]`**: Supported by direct manufacturer specifications or laboratory test-bench logging.
> - **`[CALCULATED]`**: Derived mathematically via first-principles physics equations.
> - **`[TYPICAL]`**: Statistical engineering estimate representative of common salvage stream donors.
> - **`[ASSUMED]`**: Stated baseline design assumption to be validated during prototype assembly.
> - **`[UNKNOWN]`**: Unverified scrap variable requiring active bench instrumentation before commissioning.

---

## Quick-Reference Master Matrix

| Donor Appliance / Device | Harvestable Component | Electrical / Mechanical Type | Typical Operating Spec [TYPICAL] | Best Repurposing Targets | Difficulty & Safety Rating |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Hoverboard** | Dual Outrunner Hub Motors | 3-Phase BLDC, Hall-Sensored | 36V, 250W–350W, ~15–20 Nm [TYPICAL] stall | Heavy robot rovers, ODrive servo arms, electric wheelbarrows, low-RPM wind turbines | 🟢 Moderate / Safe |
| **Hoverboard** | Mainboard & Gyro Boards | STM32 / GD32 MCU + Dual Inverter MOSFETs | 36V–42V, Dual 15A H-bridges | Custom robotics motor controller (re-flashed open firmware), dual-axis balance platforms | 🟡 Intermediate / Coding |
| **Washing Machine (Front Load)** | Direct Drive Stator & Rotor | Multi-pole Brushless PMSM (36–48 pole) | 3-Phase AC/DC, 300W–1000W, high torque | Direct-drive pottery wheel, low-RPM hydro/wind turbine generator, heavy telescope mount | 🟡 Intermediate / Heavy |
| **Washing Machine (Classic)** | Universal Motor with Tacho | Series-Wound AC/DC Universal Motor | 120V/230V AC, 10,000–15,000 RPM [TYPICAL] | Wood lathe spindle, band saw upgrade (with closed-loop TDA1085 speed board), jointer | 🔴 Mains High Voltage |
| **Treadmill** | Primary Drive Motor | Permanent Magnet DC (PMDC) | 90V–180V DC, 1.5–3.5 HP, 4000+ RPM | Machine lathe headstock, 2x72 belt grinder, heavy-duty drill press, disc sander | 🔴 Mains Rectified DC |
| **Treadmill** | Incline Actuator | AC/DC Linear Actuator (ACME screw) | 120V AC [TYPICAL] or 24V DC [TYPICAL], 400–1000 lb thrust | Workshop table lift, mower deck lift, hatch opener, solar tracker elevation | 🟡 Intermediate / High Force |
| **Windshield Wiper Assembly** | Wiper Motor | Brushed PMDC + Worm Gearbox | 12V DC [TYPICAL], 3–8A (low), 15–25A (stall), self-locking | Solar tracker azimuth drive, animatronics, rotisserie spit, battlebot pusher | 🟢 Beginner Friendly |
| **Power Window Unit** | Window Regulator Motor | Compact 12V Brushed DC + Worm Gear | 12V DC [TYPICAL], 5–15A, self-locking | Automated window blinds, small robotic lift, pan-tilt camera head, gate latch | 🟢 Beginner Friendly |
| **Electric Power Steering (EPS)** | Steering Column Motor | Ultra-high torque Brushless PMSM + Gearbox | 12V DC [TYPICAL] (50–80A peak), integrated torque sensor | Direct-drive Force Feedback (FFB) sim racing wheel, CNC 4th rotary axis, heavy robot arm | 🟡 Advanced Control |
| **Automotive Alternator** | 3-Phase Alternator | 3-Phase AC Stator + Wound Rotor Field | 12V–24V (output), convertible to 3–5 HP motor | Stick welder, pedal power station, brushless high-torque traction motor (with RC ESC) | 🟡 Intermediate / Heavy |
| **Refrigerator / Freezer** | Hermetic Compressor | Sealed Piston Pump + AC Induction Motor | 120V/230V AC, 1/8 to 1/4 HP, hermetic | Ultra-silent airbrush compressor, vacuum degas chamber (28+ inHg), wood stabilizer | 🔴 High Pressure & Mains |
| **Microwave Oven** | Turntable Motor | Synchronous AC Gearmotor | 110V/230V AC, 2.5–5 RPM [TYPICAL], high torque | Epoxy resin cup turner, rock tumbler, egg incubator rotator, slow camera panorama | 🟢 Safe (Low Voltage variant) / 🟡 Mains |
| **Microwave Oven** | High-Voltage Transformer (MOT) | Heavy Laminated Iron Core + Primary Coil | Primary 120V/230V (Secondary CUT OFF) | 18650 Battery pack spot welder (rewound with 2-3 turns heavy cable), induction forge | 🔴 LETHAL VOLTAGE (Prior to Mod) |
| **Flatbed Scanner / Printer** | Carriage Stepper Motors | Bipolar / Unipolar Hybrid Steppers | 12V–24V DC [TYPICAL], NEMA 14/17 form factor | 3D printer, mini CNC router, laser engraver, motorized camera rail | 🟢 Beginner Friendly |
| **Flatbed Scanner / Printer** | Linear Optical Encoder Strip | Transmissive Glass/Mylar Strip + Sensor | Quadrature 5V TTL pulses (150–300 DPI) | Lathe/Mill Digital Readout (DRO), closed-loop DC motor positioning system | 🟢 Electronics Beginner |
| **Optical Drive (CD/DVD/BD)** | Laser Sled Stepper | Micro-Stepper + Miniature Lead Screw | 5V DC, tiny pitch screw | Micro-CNC plotter, micro-pipette doser, focus stacking rig, laser galvo | 🟢 Beginner Friendly |
| **Optical Drive (CD/DVD/BD)** | Laser Pickup Voice Coils | 2-Axis Sub-micron Voice Coil Actuators | ±3V–5V DC, ultra-fine response | Atomic Force Microscope (AFM) scanner, optical audio pickup, laser steer mirror | 🟡 Micro-Electronics |
| **Hard Disk Drive (HDD)** | Read/Write Voice Coil Actuator | Rotary Voice Coil + Strong NdFeB Magnet | 5V–12V DC [TYPICAL], ultra-fast arc sweep | Optical laser projector galvanometer, seismic vibration detector, optical shutter | 🟢 Safe / High Precision |
| **Cordless Power Drill** | Motor + Planetary Gearbox | 550/775 DC or BLDC + Multi-stage Gearbox | 12V–20V DC, 24:1 to 36:1 reduction | Robot combat drive, electric skateboard/go-kart, motorized winch, wire twister | 🟢 Beginner Friendly |
| **Cordless Vacuum (Dyson type)**| Digital High-Speed Motor | Switched Reluctance / BLDC Turbine | 21V–28V DC, 100,000–125,000 RPM [TYPICAL] | Mini wind tunnel, extreme static pressure vacuum former, RC jet thruster | 🟡 Advanced ESC Required |
| **Dishwasher** | Magnetic Drain Pump | Brushless Permanent Magnet Impeller Pump | 120V AC [TYPICAL], continuous water circulation | Sump pump, hydroponic aeration, DIY TIG torch / laser water chiller loop | 🟡 Mains AC Plumbing |
| **Commercial Espresso Machine** | Procon Brass Rotary Vane Pump | Sliding Graphite Vane Positive Displacement | 120V/240V AC [TYPICAL] 1/3 HP, 150–250 PSI, 100 GPH | Micro-abrasive waterjet cutter, seawater reverse osmosis, high-pressure CNC mist cooler | 🟡 Intermediate / Pressure |
| **Industrial Sewing Machine** | Direct-Drive Brushless Servo | 3-Phase BLDC with Optical Encoder | 110V/220V AC, 550W–750W, 0–4500 RPM full low-end torque | Drop-in variable speed mini-lathe / drill press spindle, automated tapping machine | 🟡 Intermediate / Safe |
| **HVAC Damper Actuator (Belimo)** | Spring-Return Rotary Actuator | Micro-stepper + Planetary Gearbox + Spring | 24V AC [TYPICAL]/DC, 15–30 Nm [TYPICAL] (270 in-lb), continuous stall | Automated workshop dust blast gates, emergency water ball-valve shutoffs, robot clamps | 🟢 Beginner Friendly |
| **Commercial Dishwasher** | Peristaltic Dosing Pump | Geared DC Motor + Santoprene Squeeze Tube | 12V/24V DC [TYPICAL], 10–100 mL/min, 25 inHg suction | Automated two-part epoxy/silicone mixer, hydroponic pH dosing, MQL cutting oil meter | 🟢 Beginner Friendly |
| **Soft-Serve Ice Cream Machine** | Planetary Auger Reducer | All-Steel 40:1 Epicyclic Planetary Reducer | 1/2–1 HP AC motor, >150 Nm [TYPICAL] continuous torque | Recycled plastic filament extruder, pottery clay pug mill, heavy organic paste mixer | 🟡 Intermediate / Heavy |
| **Automotive Electric Radiator Fan** | Spal / Bosch Waterproof Blower | Hermetic IP68 3-Phase BLDC + Potted Inverter | 12V DC [TYPICAL] (30–40A), 100 Hz PWM signal, 1,800 CFM | Blacksmith forge forced blower, high-volume laser cutter exhaust, foundry crucible air | 🟢 High Current 12V |
| **DMX Moving-Head Stage Light** | Dual-Axis Pan/Tilt Yoke | 2x NEMA 17/23 3-Phase Steppers + Belt/Gimbals | 24V–36V DC [TYPICAL], 540° Pan / 270° Tilt, optical homing | Autonomous satellite tracker, motorized camera gimbal, solar concentrator heliostat | 🟡 Intermediate / Coding |
| **Electric Commuter Scooter** | Narrow Pneumatic Hub Motor | 36V 350W BLDC Hub + Drum/Disc Brake | 36V DC [TYPICAL], 15–20A, 8.5" or 10" pneumatic wheel | Motorized heavy shop carts / wheelbarrows, bandsaw variable drives, gantry traction | 🟢 Safe 36V |
| **Automotive Starter Motor** | 2.0 kW High-Torque Series DC Motor | Series/PMGR DC + Epicyclic Planetary (4:1) | 12V DC [TYPICAL], 150A–300A, extreme starting torque | Off-road recovery winches, car-pulling capstans, electric log splitters, heavy tugs | 🔴 High Current Inrush |
| **Automotive Electric Water Pump** | Canned Magnetic Brushless Pump | Hermetic Wet-Rotor BLDC (No Shaft Seals) | 12V DC [TYPICAL] (PWM controlled), 100–140 L/min | High-volume laser tube chillers, solar water circulation, high-power VFD cooling loops | 🟢 Low Voltage Safe |
| **Heavy Commercial Wiper Motor** | Dual-Speed Worm Drive Gearmotor | High-Torque Brushed PMDC + Hardened Worm (50:1) | 12V/24V DC [TYPICAL], 40–60 Nm [TYPICAL] stall, self-locking | Dual-axis solar trackers, automated chicken coop/greenhouse doors, heavy spit rotisseries | 🟢 Beginner Friendly |
| **Electronic Throttle Body (ETC)** | High-Bandwidth DC Servo Butterfly | Fast DC Servo + Dual Non-Contact TPS Hall Sensors | 12V DC [TYPICAL] (1 kHz PWM), 50–80mm bore, spring-return | Engine dyno air throttles, CNC dust blast gate modulation, pulsejet fuel/air valves | 🟡 Intermediate / Fast Snap |
| **Diesel Common-Rail System** | 2000-Bar Plunger Pump & Piezo Injectors | Hardened Ceramic Radial Plungers + Piezo Stacks | 2,000–30,000 PSI, sub-millisecond piezo stroke | Sub-micron piezo positioners, micro-waterjet orifices, high-pressure chemical reactors | 🔴 LETHAL Fluid Injection |
| **Forklift / Golf Cart DC Motor** | Series-Wound Traction Motor | 4-Pole Wound-Field Series DC + 19-Tooth Spline | 36V–48V DC [TYPICAL], 300A–500A peak, 5–10 HP | Workshop gantry crane hoists, mini-excavator electrification, heavy log splitters | 🔴 Extreme Current / Runaway |
| **Electronic Parking Brake (EPB)** | Heavy Linear Caliper Actuator | Rare-Earth DC + Planetary + Ball-Screw Jack | 12V DC [TYPICAL], 20 kN (4,500 lbs) clamping force | Miniature 2-ton hydraulic bench press, sheet metal clamping brakes, heavy robot grippers | 🟡 Intermediate / Crush |
| **Automotive A/C Compressor** | Sanden Swashplate + Magnetic Clutch | 5-7 Cyl Axial Swashplate + 12V Snap Clutch | 12V DC [TYPICAL] clutch (50 Nm [TYPICAL] disconnect), 300 PSI pump | Zero-power mechanical PTO disconnects, pneumatic radial air motors, high-pressure mist | 🟡 Intermediate / Pressure |
| **Automotive Power Seat Jack** | Worm-Drive Memory Actuator | Compact PMDC + Quadrature Hall Encoder + Acme Rod | 12V DC [TYPICAL], 500 lbs static thrust, self-locking | Closed-loop satellite/antenna trackers, heavy motorized hatch lifters, camera dollies | 🟢 Low Voltage Safe |
| **Large Flatbed / Drum Scanner** | Optical Carriage & CCD Line-Scan Bar | 3-Channel RGB CCD (10k pixels) + Linear Rods | 12V–24V DC [TYPICAL] stepper drive, front-surface mirrors | High-res optical spectrometers, micro-laser profilers, conveyor line-scan inspection | 🟢 Precision Optics Safe |
| **Laser Printer Polygon Scanner** | Polygon Mirror Scanner Unit | Aerodynamic Air/Fluid Bearing BLDC + Hex Mirror | 24V DC [TYPICAL], 30,000–45,000 RPM [TYPICAL], F-theta scan lens | Flying-spot ultra-fast laser engravers, 360-degree LiDAR 3D scanners, optical choppers | 🟡 Extreme RPM / Class 3B |
| **Audiophile Direct-Drive Turntable** | Coreless Axial-Flux Pancake BLDC | Slotless Brushless Pancake + Quartz Tachometer | 12V–24V DC [TYPICAL], zero cogging, ruby tonearm gimbals | Astronomical telescope RA drives, sub-milligram Cavendish gravity balances, spin coaters | 🟢 Safe / Ultra-Smooth |
| **Vending Bill Validator / Sorter** | Multi-Wavelength Optical Spectrometer | IR/UV/Red Transmissive/Reflective Sensor + Rollers | 12V/24V DC [TYPICAL] MDB serial bus, urethane pinch drive | 3D printer filament color/diameter monitors, metal strip feeders, automated coin sorters | 🟢 Electronics Beginner |
| **35mm SLR Camera Shutter** | Dual Focal-Plane Slit Shutter Curtain | Titanium/Carbon Blades + Swiss Lever Escapement | 1/8,000s speed, mechanical hairspring governor | Zero-power mechanical delay latches, ultra-fast laser beam choppers, micro-samplers | 🟢 Mechanical Precision |
| **CNC Optical Glass Linear Scale** | Heidenhain / Renishaw Linear Glass Scale | Chrome-on-Glass Grating (0.1–1.0 um) + Readhead | 5V DC, RS-422 differential quadrature / 1Vpp | Sub-micron CNC lathe/mill DRO conversions, CMM coordinate inspection, stage metrology | 🟢 Low Voltage / Fragile Glass |
| **Industrial Barcode Scanner** | Resonant Galvanometer Scanner | 100 Hz Oscillating Mirror + 650nm Laser + APD | 5V/12V DC [TYPICAL], high-gain avalanche photodiode | Fast laser line generators, optical triangulation distance sensors, optical choppers | 🟢 Safe / Low Voltage |
| **POS / Fax Thermal Print Head** | Thick-Film Ceramic Thermal Array | 203–300 DPI Micro-Resistor Array (832+ dots) | 12V–24V DC [TYPICAL], pulsed strobe shift registers | CNC pyrography wood carvers, direct PCB thermal toner transfer, hot-wire foam cutters | 🟢 Low Voltage Safe |
| **Dishwasher Circulation Pump** | Canned Wet-Rotor Circulation Pump | 1/4 HP Brushless PMSM + 1500W Flow-Thru Tube | 120V/240V AC [TYPICAL], integrated flow-through heater | Heated ultrasonic cleaning tanks, workshop parts washers, homebrew RIMS brewing loops | 🔴 Mains AC / Scalding |
| **Microwave Turntable Motor** | Synchronous Slow-Speed Gearmotor | Miniature PM Synchronous + All-Metal Gearbox | 21V/120V AC [TYPICAL], 3–5 RPM [TYPICAL], auto-reversing on stall | Epoxy resin rod dryers, lapidary rock tumblers, slow display rotators, clock escapements | 🟢 Low Voltage / 🟡 Mains |
| **Dryer Centrifugal Blower Assembly** | Double-Shaft Induction Motor & Blower | 1/3 HP Split-Phase (1,725 RPM [TYPICAL]) + Squirrel Cage | 120V AC [TYPICAL], high-CFM forward-curved fan wheel | Workshop dust collection scrubbers, spray booth exhaust extractors, forge blast air | 🔴 Mains AC / High CFM |
| **Kitchen Sink Garbage Disposal** | Stainless Shredder Induction Motor | 1/2–3/4 HP Induction/PMDC + 360° Swiveling Lugs | 120V AC [TYPICAL], stainless grinding chamber, lip seal | Organic bio-waste shredders, aluminum can pulverizers, recycled HDPE plastic pelletizers | 🔴 Extreme Shredding Force |
| **Robotic Vacuum Cleaner (Roomba)** | Modular Planetary Wheel Drives | Dual Independent Planetary Drives + Encoders | 14.4V–16.8V Lithium, 15,000 RPM [TYPICAL] BLDC turbine | Autonomous indoor mobile robots, desktop AGV tugs, low-profile pipe inspection rovers | 🟢 Low Voltage Safe |
| **Peltier Water Cooler / Dispenser** | Thermoelectric Cooler & Sump | TEC1-12706 (60W) + Aluminum Finned Heat Sump | 12V DC [TYPICAL], 6A, creates freezing and hot surfaces | Solid-state mini-chillers, Wilson cosmic ray cloud chambers, laser diode cooling blocks | 🟢 Low Voltage Safe |
| **Standing-Pilot Gas Water Heater** | 750mV Multi-Junction Powerpile | 35–50 Chromel-Alumel Junctions in Ceramic Tube | 750mV DC open circuit, 56 mW, R_int ~ 2.5 ohms | Autonomous battery-free off-grid chimney telemetry, galvanic seawater battery plates | 🟢 Safe Millivolts / 🔥 Heat |
| **Domestic Breadmaker Machine** | Heavy Kneader Planetary Reduction | 1/4 HP Universal/Induction + Aluminum Timing Belt | 120V AC [TYPICAL], 10:1 reduction, high-temp fluorocarbon seal | Carbon-fiber filament spoolers, planetary jar ball mills, heavy chemical slurry stirrers | 🟢 Beginner Friendly |
| **Heavy 9" Industrial Angle Grinder** | Spiral-Bevel 2 kW Universal Motor | 15A Universal AC/DC + Hardened Spiral Bevel (4:1) | 120V/240V AC [TYPICAL], 6,000–8,500 RPM [TYPICAL] output arbor | High-speed metal chop saws, 2x72 belt surface grinders, heavy portable DC arc welders | 🔴 Extreme Kinetic Energy |
| **2-Stroke Chainsaw Engine** | 45cc–55cc Air-Cooled Gas Engine | Single-Cylinder 2-Stroke + Diaphragm Carburetor | 2.5–4.0 HP @ 9,000 RPM [TYPICAL], centrifugal shoe clutch | Motorized drift trikes, emergency backpack generator sets, high-output salvage pumps | 🟡 Flammable Fuel / High RPM |
| **Electric Wheelchair Gearmotor** | High-Torque Right-Angle Drive | 24V 350W–500W PMDC + Helical Worm + 24V Brake | 24V DC [TYPICAL], 20:1 to 30:1 reduction, 1" solid axle | Heavy combat robots / BattleBots, automated warehouse AGVs, motorized snowblowers | 🟡 High Torque / Crush |
| **Rotary Hammer Drill (SDS-Max)** | Electro-Pneumatic Striker Mechanism | Free-Flying Flying Piston Striker + Ball Clutch | 120V AC [TYPICAL], 3–10 Joules impact per blow | Miniature pneumatic forging hammers, automated core sampling drills, scrap punches | 🔴 Extreme Kinetic Shock |
| **Cordless Brushless Chainsaw** | High-Voltage External Rotor BLDC | 1.5 kW–2.5 kW External Rotor Brushless Motor | 40V–60V DC, electronic inertia brake, planetary | Ultralight electric go-karts / minibikes, electric outboard thrusters, heavy winches | 🟡 High Power 60V BLDC |
| **RC Drone Outrunner BLDC Motor** | Extreme Power Density BLDC Motor | Multi-Pole Neodymium Outrunner (N52 Curved Arc) | 12V–25V DC (3S–6S LiPo), 1–3 kW, 30,000 RPM [TYPICAL] | Ultra-high-speed PCB milling spindles (35k RPM), micro ducted fans, dynamic balancers | 🔴 Extreme RPM / Current |
| **Electric Rotary Lawnmower** | Heavy Direct-Drive Motor & Flange | 1,000W–1,800W Induction/BLDC + 5/8" Ground Shaft | 36V–80V DC or 120V AC [TYPICAL], cast steel blade hub | 12"–14" workshop disc sanders, heavy wood shaper headstocks, direct-drive wood chippers | 🔴 High Inertia / Kinetic |
| **Turbomolecular Vacuum Pump** | Multi-Stage Bladed Turbine Rotor | Titanium Turbine (60k–90k RPM) + MagLev Bearings | Ultra-high vacuum (10^-7 to 10^-9 Torr), water cooled | High-vacuum sputtering/PVD chambers, tabletop fusors, particle beam accelerators | 🔴 Extreme RPM / Vacuum Shock |
| **Gas / Water Utility Meter** | Nutating Disc / Diaphragm Chamber | Zero-Leak Magnetic Bulkhead Coupling + Reed Pulse | 150 PSI brass/polymer housing, exact volume pulses | Precision chemical batch dosing, engine fuel/coolant telemetry, ultra-low-RPM air motors | 🟢 Fluidic Precision |
| **Defibrillator / Studio Strobe** | Pulse Metallized Film Capacitor Pack | 32–200 uF @ 2,000V–4,000V DC + 5,000A SCR Puck | 300–500 Joules, pulse current up to 5,000A | Capacitive-discharge tab spot welders, electromagnetic sheet metal forming, railguns | 🔴 LETHAL HIGH VOLTAGE |
| **Nd:YAG Laser Cavity Head** | Crystal Rod & Krypton Flashlamp | Gold-Plated Cavity + Nd:YAG Single Crystal Rod | 1064nm infrared laser pulses, dielectric mirrors | Laser rust cleaning & ablation, laser spark spectrometry (LIBS), optical shadowgraphy | 🔴 LETHAL Class 4 Laser |
| **Nanopositioning Piezo Stage** | Flexure-Guided PZT Actuator Stack | PZT Ceramic Stacks + Parallelogram Flexures | 0–150V DC, sub-nanometer travel, capacitive sense | Atomic force microscopes (AFM), laser beam steering, optical lithography alignment | 🟢 Low Voltage / Micro-Force |
| **UV-Vis Spectrophotometer** | Holographic Blazed Diffraction Grating | 1200–2400 lines/mm Grating + Sine-Bar Stepper | Deuterium UV + Halogen, photomultiplier tube | Chemical solution absorption analyzers, Raman spectroscopy, laser wavelength meters | 🟢 Optical Precision |
| **Clinical Blood Centrifuge** | High-G Brushless Centrifuge Rotor | Solid Anodized Aluminum Angle Rotor (14k RPM) | 120V AC [TYPICAL] / BLDC, steel armored containment ring | Nanoparticle separation, algae biofuel dewatering, high-G mechanical component testing | 🔴 Extreme G-Force / Inertia |
| **Triplex Plunger Pressure Washer** | Ceramic Plunger High-Pressure Pump | Solid Ceramic Plungers + Forged Brass Manifold | 1,500–3,500 PSI @ 2–4 GPM, unloader bypass valve | DIY desktop abrasive waterjets (cuts steel/carbon fiber), hydrostatic test rigs, RO | 🔴 Extreme Pressure (3500 PSI) |
| **Washer Drum LeBlanc Ring** | Annular Fluid/Ball Balancer Ring | Toroidal Steel Raceway + Silicone Oil + Chrome Balls | Automatically offsets unbalance mass above resonance | Self-balancing high-speed centrifuges, variable-load spin coaters, balanced spindles | 🟢 Mechanical Kinematics |
| **Geneva Indexing Mechanism** | Maltese Cross Intermittent Drive | 4-Slot or 6-Slot Geneva Wheel + Constant-Speed Pin | Pure 90° or 60° stepping with positive mechanical dwell | Multi-station rotary indexing tables, automated assembly carousels, camera gates | 🟢 Mechanical Kinematics |
| **Textile Winder Traverse Cam** | Helical Diamond Barrel Cam & Eyelets | Cylindrical Barrel Cam + Sintered Al2O3 Eyelets | Mohs hardness 9 ceramic guides, zero wear traverse | Level-wind wire & 3D printer filament spoolers, wire-EDM abrasive diamond wire guides | 🟢 Mechanical Kinematics |
| **Reciprocating Scotch Yoke** | Harmonic Pure Sinusoidal Mechanism | Hardened Slotted Yoke Frame + Eccentric Bearing Pin | Pure sinusoidal translation with zero side-thrust | Pure sinusoidal vibration testing shaker tables, linear slurry pumps, filing machines | 🟡 Mechanical Pinch |
| **Robotic Cycloidal Reducer** | Zero-Backlash Nabtesco Cycloidal Drive | Dual Lobed Cycloidal Discs + Ring Pin Housing | 30:1 to 100:1 reduction, 500% shock load tolerance | Zero-backlash heavy robotic arm joints, CNC 4th/5th axis trunnion tables, heavy steering | 🟡 High Torque |
| **Harmonic Strain-Wave Reducer** | Aerospace Zero-Backlash Flexspline | Elliptical Wave Generator + Cup Flexspline | 50:1 to 100:1 reduction in ultra-thin pancake frame | Telescope equatorial tracking drives, SCARA robot wrists, precision gimbals | 🟢 Precision Kinematics |
| **Starter Sprag One-Way Clutch** | Hardened Sprag Overrunning Clutch | Spring-Loaded Sprags / Rollers + Ground Races | Zero-backlash instantaneous one-way lockup (>300 Nm [TYPICAL]) | Flywheel kinetic energy freewheels, hybrid motor drives, anti-reverse hoist brakes | 🟢 Mechanical Kinematics |
| **Insulation Resistance Tester (Megger)**| Hand-Cranked High-Voltage Generator | 500V–1,000V DC Magneto Generator + Log Microammeter | High-voltage insulation leakage testing up to 1000MΩ | Non-destructive dielectric breakdown testing of mystery motors, transformers, wiring | 🟡 High Voltage Shock |
| **Custom Dual-MOT Spot Welder** | Rewound High-Current Secondary Core | 2 Rewound MOTs with 50mm² (1/0 AWG) Secondary | 1,500A–2,000A AC @ 2.5V, solid copper arms | Clean, sparkless 18650/21700 battery pack nickel tab welding, sheet metal fabrication | 🔴 High Current / Mains |
| **Electrolytic Rust Removal Tank** | Alkaline De-Oxidation Tank Rig | Washing Soda (Na2CO3) + 12V 30A DC + Rebar Anodes | 12V DC [TYPICAL], 10–30A, line-of-sight molecular rust reduction | Non-destructive restoration of antique machine castings, de-rusting seized donor parts | 🟡 Flammable Hydrogen Gas |
| **Granite Precision Surface Flat** | Metrology Lapping Reference Plate | Grade B Natural Black Granite + Cast Iron Lapping Plate| 0.0001" flatness, diamond suspensions (1u–14u) | Hand-scraping machine tool ways, polishing ceramic pump plungers, optical flat testing | 🟢 Metrology Reference |
| **Metallurgy Spark-Testing Bench** | Pedestal Grinder Spark Inspection Hood | 3,450 RPM [TYPICAL] Pedestal Grinder + 60-Grit Al2O3 Wheel | Darkened hood, calibrated steel alloy reference coupons | 10-second scrap steel alloy identification (mild steel vs 4140, O1, W1, high-speed steel) | 🟡 High-Speed Sparks |
| **E-Bike Torque Bottom Bracket** | Magnetostrictive Rotary Torque Sensor | Chromoly Spindle + Inverse Wiedemann Sense Coils | 5V DC, proportional 0.5V–2.5V output, 0–150 Nm [TYPICAL] range | Non-contact wireless rotary dynamometer for engines & motors, ergometer telemetry | 🟢 Electronics Beginner |

---

## Module 1: Precision & Micro-Motion (Printers, Scanners, Optical Drives, HDDs)

### 1. Optical Disc Drives (CD, DVD, Blu-Ray)
Optical drives are treasure troves of high-precision miniature mechanics manufactured to tolerances that DIYers cannot machine at home.

```
+-----------------------------------------------------------+
| Optical Sled Sub-Assembly:                                |
|  [Micro-Stepper] ===(Precision Leadscrew)===> [Laser Sled]|
|                                                 |         |
|  [Voice Coil 2-Axis Lens] <---------------------+         |
+-----------------------------------------------------------+
```

#### What to Extract:
1. **Sled Linear Stepper Motor**: Tiny bipolar stepper motor with an integrated fine-pitch steel leadscrew and brass/plastic nut (typically 3mm diameter, 0.5mm lead).
2. **Spindle Motor**: Sensorless 3-phase BLDC pancake motor (spins up to 10,000 RPM [TYPICAL]).
3. **Voice Coil Lens Actuator**: Dual-axis magnetic coil suspended between rare-earth magnets, designed to focus and track laser light within nanometer tolerances.
4. **Optics & Mechanics**: High-reflectivity front-surface mirrors, collimator lenses, precision ground 3mm steel guide rods, and small high-flux neodymium magnets.

#### How to Drive It:
- **Stepper Motor**: 4-wire bipolar. Drive using an **A4988**, **DRV8825**, or silent **TMC2209** stepper driver at 5V logic. Current limit must be set very low (under 200mA) or the tiny motor windings will incinerate.
- **Voice Coil**: Acts like a tiny loudspeaker voice coil. Drive directly from an audio amplifier or an Arduino PWM pin filtered through a low-pass RC filter. Polarity determines direction (+ pushes up, - pulls down).

#### Creative Repurposing Ideas:
- **Micro-Laser Engraver / Vector Plotter**: Two DVD sled assemblies mounted perpendicularly (X and Y axes) provide an ultra-rigid 40mm x 40mm work area. Mount a salvaged 250mW red DVD-writer laser diode or a fine pen to create business card engravers or PCB etch resist markers.
- **DIY Atomic Force Microscope (AFM) / Nanopositioning Stage**: The optical pickup's voice coil has sub-micron resolution. By applying tiny DC voltage offsets via a 16-bit DAC, you can create a piezo-substitute scanning head for scanning tunneling microscopy (STM) or nano-indentation testing.
- **Automated Macro Focus Stacking Rail**: The leadscrew yields linear movement steps down to ~5 microns per microstep. Clamp a camera macro lens to the sled for automated high-magnification insect photography.

---

### 2. Flatbed Scanners & Multifunction Inkjet/Laser Printers

```
Scanner Body:
+-----------------------------------------------------------------+
| [Guide Rod] ====================================== [Linear Rail]|
|   [Carriage] <==== (Timing Belt) ====> [NEMA 14/17 Stepper]     |
|       |                                                         |
|   [Optical Encoder Strip] -----------------> [Sensor PCB]       |
+-----------------------------------------------------------------+
```

#### What to Extract:
1. **Hybrid Stepper Motors**: Laser printers yield heavy NEMA 17 or NEMA 23 stepper motors (high holding torque, 1.8° or 0.9° step angle). Scanners yield flatter high-speed steppers.
2. **Precision Ground Linear Rods**: Hardened steel rods (usually 8mm, 10mm, or 12mm diameter) up to 450mm long, ground to bearing tolerances, often paired with sintered bronze or PTFE slide bushings.
3. **Linear Optical Encoder Strips**: A long, clear polyester strip printed with thousands of microscopic vertical black bars (typically 150 to 300 lines per inch) and its matching transmissive dual-photodiode reader.
4. **Rotary Quadrature Encoders**: Transparent plastic wheels mounted to the paper feed rollers with optical interrupter chips.
5. **Cold Cathode Lamps (CCFL) or High-CRI LED Bars**: Scanners contain uniform, high-color-rendering linear light sources with front-surface silvered mirrors.

#### How to Drive & Interface:
- **Optical Encoder Strip Hack**: The sensor has 4 pins: `VCC (5V)`, `GND`, `Channel A`, and `Channel B`. Connecting Channel A and B to the hardware interrupt pins of an Arduino, ESP32, or Teensy gives a true hardware quadrature decoder capable of sub-millimeter position tracking at zero cost.

#### Creative Repurposing Ideas:
- **Machine Tool Digital Readout (DRO)**: Mount the scanner linear encoder strip and optical read-head to your manual lathe's cross-slide or milling machine table. Wire it into an ESP32 displaying live position on an OLED screen or over Bluetooth to a tablet—providing $500 digital scale accuracy for free.
- **Motorized Camera Slider / Motion Timelapse Rig**: Use the scanner chassis, guide rail, timing belt, and stepper motor intact. Add an Arduino with an A4988 driver to slide a mirrorless camera smoothly over 1 to 2 hours for panoramic cinematic timelapses.
- **Large-Format Direct Contact Scanner**: Replace the scanning CCD bed with a UV LED strip to expose photoresist on custom printed circuit boards (PCBs) or cyanotype artwork with flawless linear motion.

---

### 3. Mechanical Hard Disk Drives (3.5" & 2.5" HDDs)

```
Inside an HDD:
+-----------------------------------------------+
|  (O) Spindle Motor (Multi-Platter BLDC)       |
|                                               |
|           /---\  Pivot                        |
|  [Head]--<  O  >====[Coil]                    |
|           \---/      |                        |
|             [Neodymium Curved Magnets]        |
+-----------------------------------------------+
```

#### What to Extract:
1. **Voice Coil Rotary Actuator**: A frictionless arm balanced on miniature precision ball bearings, sweeping between two extraordinarily powerful curved neodymium magnets.
2. **Spindle BLDC Motor**: High-balance, ultra-smooth fluid dynamic bearing (FDB) brushless motor designed to spin at 5,400 to 10,000 RPM [TYPICAL] silently.
3. **Mirror-Finish Platters**: Aluminum-magnesium or glass-ceramic disks polished to mirror flatness.
4. **N52 Rare-Earth Magnets**: Some of the strongest permanent magnets available anywhere in consumer scrap.

#### Creative Repurposing Ideas:
- **High-Speed Laser Vector Projector (Galvanometer / Galvo)**:
  - *The Hack*: Take two HDD voice coil arms. Remove the delicate read heads and glue a tiny front-surface mirror to each tip. Mount them at 90° to each other (X and Y axes).
  - *Control*: Connect the voice coils to the left and right audio channels of an ordinary 20W stereo audio amplifier. Feed the amplifier stereo audio generated by software (like LaserShowGen or pure audio waveforms). The voice coils deflect the mirrors at audio frequencies (up to 2–5 kHz), allowing you to project vector graphics, oscilloscope Lissajous figures, or text on your wall using a laser pointer.
- **Ultra-Sensitive Geophone / Seismometer**:
  - The voice coil acts in reverse as an electromagnetic velocity sensor. When resting on a solid floor, vibrations from footsteps, trucks passing miles away, or distant earthquakes shake the chassis while the balanced arm inertia lags behind. Feeding the coil output into a high-gain instrumentation op-amp (e.g., INA128) creates a professional-grade seismic monitoring station.
- **HDD Persistence-of-Vision (POV) Strobe Clock**:
  - Cut a tiny radial optical slit into an HDD platter. Mount RGB LEDs behind the spinning platter (driven by the spindle motor). By pulsing the LEDs at exact microsecond intervals synchronized to platter rotation, numbers and clock hands appear magically suspended in mid-air on the spinning disk.
- **Precision Rotary Optical Encoder / Input Knob**:
  - Spindle motors generate clean 3-phase sine waves when spun by hand. By connecting the three stator wires to a set of LM339 comparators, an old HDD motor becomes the most butter-smooth, heavy-feel digital volume knob or flight simulator trim wheel you will ever use.

---

## Module 2: Automotive Electromechanics (Rugged 12V DC [TYPICAL] Workhorses)

Automotive components are over-engineered for extreme temperatures (-40°C to +85°C), high vibration, road salt, and continuous torque.

```
Wiper / Window Worm Drive Topology:
  [12V PMDC Armature] ---> (Steel Worm Screw) 
                                 |
                                 v
                        [Nylon/Bronze Gear] ===> High Torque Output Shaft
                        *(Self-locking under back-drive load)*
```

### 1. Windshield Wiper Motors
The undisputed king of budget robotics and heavy DIY automation.

#### Key Specs:
- **Operating Voltage**: 12V–14V DC (runs happily from 5V to 18V).
- **Current Draw**: 2–4A no-load; 6–10A under load; 15–25A stall.
- **Speed**: Built-in 2 speeds (Low: ~45 RPM [TYPICAL]; High: ~65 RPM [TYPICAL]).
- **Torque**: 15–30 Nm [TYPICAL] (130–260 in-lbs)—enough to lift heavy assemblies or stall a human arm.
- **Mechanical Advantage**: Non-backdriveable worm drive (when power cuts, the shaft stays locked in place).

#### Wiring Demystified:
Wiper motors typically have 4 or 5 pins:
- `Ground (Case or black wire)`: Chassis ground.
- `Low Speed`: Connect to +12V for low RPM, maximum torque.
- `High Speed`: Connect to +12V for high RPM.
- `Park Switch (2 wires)`: An internal mechanical cam switch that remains closed until the motor returns to its home position (crucial for automated home-position indexing).

#### Creative Repurposing Ideas:
- **Dual-Axis Solar Tracker**: Use two wiper motors (one for azimuth east-to-west, one for zenith elevation). Because of the worm drive, heavy wind gusts cannot force the solar panels out of alignment, and the motors consume zero standby power when stationary.
- **Heavy Combat Robot / Robot Lawn Mower Drivetrain**: Two wiper motors driving wheelchair or kart wheels give a 40–80 lb robot unstoppable tank-steering push power.
- **Automated Heavy Chicken Coop / Greenhouse Vent Door**: Wire the wiper motor to open a vertical sliding door on a dawn/dusk light sensor. The self-locking gearbox guarantees raccoons and predators cannot pry the door open.
- **Rotisserie Spit Roaster / BBQ Pig Spit**: Mount directly to a spit rod for continuous 45 RPM [TYPICAL] rotation under a 50 lb carcass load.

---

### 2. Automotive Alternators

```
Alternator Anatomy:
[3-Phase Stator Windings] <--- (Rotating Magnetic Field from Rotor)
          |                                 ^
          v                                 |
[Bridge Rectifier Diodes]           [Rotor Field Coil] <--- [Slip Rings / Brushes]
          |
          v
    [14V DC Output]
```

#### What to Extract & Modify:
1. **Stock Mode (Alternator / Generator)**: Capable of generating 60A to 160A at 14V DC (800W to 2.2 kW). Requires an external 12V excitation current to the rotor brushes to create the magnetic field.
2. **Hacked Mode (Brushless 3-Phase AC/DC Motor)**:
   - *The Conversion*: Open the alternator case. Bypass or remove the internal diode rectifier pack to expose the 3 stator phase leads (U, V, W). Supply a constant 12V DC [TYPICAL] current to the rotor slip rings (field coil) via the brushes to create permanent electro-magnets, or machine the rotor to embed permanent neodymium magnets.
   - *Driving*: Connect the three stator phase leads to a high-power e-bike or RC aircraft brushless ESC (Electronic Speed Controller) rated for 48V–72V and 100A+.
   - *Result*: You now possess a 5 to 7 Horsepower Brushless Motor capable of 10,000 RPM [TYPICAL] for less than the cost of a cup of coffee.

#### Creative Repurposing Ideas:
- **DIY Stick / TIG Arc Welder**: Couple an alternator to an old 6.5 HP lawnmower gas engine. Bypass the internal voltage regulator and excite the field rotor with a potentiometer. You have a portable, 120A DC stick welder that can be hauled into the woods or onto a farm trailer.
- **Human-Powered Off-Grid Pedal Generator**: Mount an alternator to a bicycle trainer stand. One person pedaling at moderate effort produces 100–150W of continuous power directly into a 12V or 24V LiFePO4 battery bank.

---

### 3. Electric Power Steering (EPS) Columns

```
EPS Column Assembly:
  [Steering Input Shaft] ---> [Optical/Hall Torque Sensor]
                                     |
  [High-Torque BLDC Motor] ==(Gearbox)==> [Output Steering Shaft]
```

#### What to Extract:
Found in modern compact cars (e.g., Toyota Prius/Yaris, Opel Corsa, Ford Focus). Contains a monster 12V brushless PMSM servo motor, a heavy zero-backlash worm reduction gearbox, and an integrated high-resolution torque sensor.

#### Creative Repurposing Ideas:
- **Commercial-Grade Force Feedback (FFB) Sim Racing Wheel**:
  - Commercial direct-drive steering wheels (Fanatec, Simucube) cost $1,000–$2,000. An EPS column salvaged from a junkyard for $40, paired with an STM32 "BluePill" running open-source **OpenFFB** or **MMOS** firmware and a BTS7960 motor driver, produces 15 to 30 Nm [TYPICAL] of bone-crushing, realistic steering torque for *iRacing* or *Assetto Corsa*.
- **Heavy-Payload CNC 4th Rotary Axis**: The near-zero backlash and massive holding torque make it a drop-in rotary indexer for rotating billet aluminum on a CNC mill.

---

### 4. Power Window Regulators & Seat Track Actuators
- **Power Seat Actuators**: Precision screw jacks driven by high-torque 12V motors. Built-in lead nuts mean they can push or pull 200–500 lbs along a 6 to 10-inch stroke without tilting.
  - *Projects*: Motorized scissor-lift welding tables, motorized camera crane boom adjustments, adjustable height standing desks.
- **Power Window Motors**: Incredibly thin form factor with a cable drum or high-pitch spur gear.
  - *Projects*: Automatic sliding curtains, motorized pet feeders, motorized pegboard tool racks that descend from garage ceilings.

---

## Module 3: Heavy Household Appliances & Mains Electromechanics

Household appliances pack some of the most potent electric motors available in consumer society, often constructed with pure copper and hardened steel intended to run for 15+ years.

### 1. Washing Machines: Direct Drive vs. Universal Motors

```
Direct-Drive (LG/Fisher & Paykel) Pancake Stator:
           [ 36 to 48 Pole Stator Coils ]
                     |
       (Surrounded by Outer Rotor Ring)
                     v
   [ 36 to 48 Permanent Neodymium/Ferrite Magnets ]
   *Spins at 50-1400 RPM with enormous direct torque*
```

#### Type A: Modern Direct-Drive Motors (LG, Samsung, Whirlpool Cabrio, Fisher & Paykel SmartDrive)
- **Construction**: A massive pancake stator with 36, 42, or 48 copper-wound teeth, surrounded by an external rotor ring embedded with matching permanent neodymium/ferrite magnets.
- **Operating Mode**: 3-Phase Brushless Permanent Magnet Synchronous Motor (PMSM).

#### Creative Repurposing Ideas:
- **Low-RPM Direct-Drive Wind or Hydro Generator**:
  - Traditional motors require a 10:1 or 20:1 speed-up gearbox to spin fast enough to generate electricity from wind, causing friction, noise, and mechanical failure.
  - Because a direct-drive stator has up to 48 poles, spinning it by hand at just **120 RPM [TYPICAL]** produces 24V–48V AC [TYPICAL] across the phases. Connect the 3 phases to a 3-phase bridge rectifier, wire it to an MPPT solar/wind charge controller, and bolt wind blades or a waterwheel directly to the outer rotor hub. You get a bulletproof, near-silent, gearbox-free renewable energy station.
- **Direct-Drive Potter's Wheel**:
  - Pottery requires high torque at ultra-low speeds (0 to 300 RPM [TYPICAL]) with smooth pedal speed control. Traditional pottery wheels use noisy friction wheels or slipping belts. Wiring a direct-drive stator with a low-cost VESC (Vedder ESC) or 3-phase sensorless controller gives zero-noise, variable-speed, foot-pedal-controlled throwing power that will never bog down under 50 lbs of wet clay.

#### Type B: Classic Universal Brushed Motors (Older Front-Load Washers)
- **Characteristics**: Screaming 10,000–15,000 RPM [TYPICAL] universal motors with an integrated **Tacho-Generator** (a miniature AC alternator on the rear shaft that outputs voltage proportional to RPM).
- **The Hack (TDA1085 Controller)**:
  - If you plug this motor directly into AC mains with a simple light dimmer, the motor will stall instantly the moment a workpiece touches the blade.
  - By using an inexpensive **TDA1085 closed-loop speed controller board** (salvaged from the washer or bought on eBay), the controller reads the tacho-generator in real time. As you apply cutting force, the chip instantly pumps more current into the windings, maintaining rock-solid, constant RPM under variable load.
  - *Projects*: Upgrade old Craftsman wood lathes, drill presses, or homemade wood jointers.

---

### 2. Treadmills: The Holy Grail of Workshop Spindles

```
Treadmill PMDC Motor:
  [Heavy Cast Iron Flywheel / Poly-V Pulley]
                     |
  [90V - 180V High-Current Armature]
                     |
  [Massive Rare-Earth / Ferrite Stator Magnets]
```

#### What to Extract:
1. **Primary PMDC Motor**: Rated 90V–130V DC (North America) or 180V–230V DC (Europe/International). Delivers 1.5 to 3.5 true horsepower, with continuous RPM between 3,500 and 6,000. Features a balanced cast-iron flywheel with an integrated multi-rib Poly-V belt pulley.
2. **Incline Linear Actuator**: Heavy-duty AC or DC screw actuator with an integrated 10k potentiometer for absolute position feedback, rated for 600 to 1,200 lbs of dynamic thrust.
3. **Controller Board**: MC-60, MC-2100, or similar high-voltage PWM or SCR motor drive boards.

#### How to Drive the Motor:
- **Option 1 (Gold Standard)**: A **KB Electronics KBIC** or **KBMM** DC motor speed drive. Connects to 120V/240V AC [TYPICAL] mains and outputs 0–90V / 0–180V DC with armature back-EMF feedback for constant torque.
- **Option 2 (Digital PWM)**: A 100V–250V high-voltage DC PWM speed controller box ($20–$35 online).
- **Option 3 (Hacking OEM Board)**: Boards like the MC-60 can be controlled via an external 5k potentiometer; MC-2100 boards require a 20 Hz PWM signal from an Arduino or 555 timer.

#### Creative Repurposing Ideas:
- **2" x 72" Knifemaking Belt Grinder**: Commercial grinders (Bader, TW-90) cost $2,000+. A treadmill motor provides the raw horsepower and variable surface-feet-per-minute (SFPM) speed needed to grind tool steel without bogging down.
- **Mini-Lathe & Drill Press Variable Speed Upgrades**: Replace underpowered stock AC induction motors on mini-lathes (Sieg, Grizzly) to get instant variable-speed spindle control without moving drive belts between pulley steps.
- **Treadmill Incline Actuator as a Workbench Lift**: Mount the incline actuator under your main assembly table to build an adjustable-height ergonomic workbench that adjusts from sitting height to standing height at the flip of a switch.

---

### 3. Microwave Ovens (Proceed with Extreme Caution)

> [!CAUTION]
> **Lethal Voltage Hazard**: The internal High-Voltage Capacitor and Transformer (MOT) inside a microwave oven operate at **2,000 to 4,000 Volts AC/DC at over 500mA**—more than enough energy to cause instantaneous cardiac arrest. NEVER plug in, probe, or power a microwave transformer in its stock configuration. Always discharge the capacitor with an insulated screwdriver across its terminals before touching any internal parts.

#### 1. Turntable Synchronous Motor (Completely Safe)
- **Characteristics**: Compact metal gearmotor running on 120V/240V AC [TYPICAL] (or 21V AC from the fan tap). Turns at 2.5 to 5 RPM [TYPICAL] with high torque. Features an internal multi-stage gear train with a directional dog clutch.
- *Projects*:
  - **Custom Fishing Rod / Epoxy Tumbler**: Rotates freshly coated fishing rods or glitter epoxy tumblers slowly overnight so epoxy levels out smoothly without dripping.
  - **Egg Incubator Rocker**: Tilts egg trays automatically every hour.
  - **Ball Mill / Rock Tumbler**: Drives a rubber-lined PVC drum for polishing stones or milling pyrotechnic chemicals.

#### 2. Modified MOT (Microwave Oven Transformer) -> High-Current Spot Welder
- *The Safe Modification*:
  1. Remove the transformer from the chassis.
  2. Use a hacksaw or chisel to carefully cut out and drive out the **secondary high-voltage winding** (the fine, thin copper wire winding). **Discard it.**
  3. Leave the primary 120V/240V mains winding untouched.
  4. Thread 2 to 3 turns of ultra-thick, flexible welding cable (2 AWG or 0 AWG copper cable) through the empty secondary core space.
- *The Result*: You have converted a lethal 2,000V transformer into a completely safe **3.5V to 4V transformer delivering 500 to 800 Amps of instantaneous current**.
- *Repurposing*: Wire to solid copper welding prongs and a solid-state relay (SSR) with an Arduino timer to build a professional-grade **18650 Battery Pack Spot Welder** for welding nickel strips on DIY EV and powerwall batteries.

---

### 4. Refrigerator & Freezer Hermetic Compressors

```
Hermetic Compressor Cutaway:
+------------------------------------------------+
| Sealed Steel Pressure Dome                     |
|                                                |
|  [Suction Port] ---> [Internal Resonator/Trap] |
|                             |                  |
|  [Piston Crankshaft] <--- [Single-Phase Motor] |
|        |                                       |
|        v                                       |
|  [Exhaust Port] ===> 250+ PSI Compressed Air   |
+------------------------------------------------+
```

#### What Makes Them Special:
The compressor mechanism (a reciprocating piston and an electric induction motor) is permanently sealed inside an airtight, sound-insulated steel dome and immersed in lubricating oil.

#### Creative Repurposing Ideas:
- **The "Whisper-Quiet" Indoor Airbrush Compressor**:
  - Traditional workshop air compressors scream at 85–95 dB. A refrigerator compressor runs at **under 40 dB** (quieter than a library whisper).
  - *Setup*: Plumb the exhaust port to an old fire extinguisher or metal expansion tank via a check valve. Add an air pressure switch (set to 40 PSI off / 30 PSI on), an ASME safety relief valve, and an inline **oil-coalescing filter** (essential, as compressors spit minor oil vapor into the line). You have an ultra-silent airbrush and tire inflation rig.
- **Deep Vacuum Degassing Chamber**:
  - Connect the compressor's suction (inlet) port to a heavy stainless steel stockpot with a 1-inch thick clear polycarbonate lid (never use acrylic or glass, which can shatter).
  - *Capability*: Pulls a continuous vacuum down to **28 to 29 inHg**—perfect for boiling out trapped air bubbles from silicone molds, casting clear epoxy resin, or stabilizing punky wood in Cactus Juice resin.

---

### 5. Dishwashers: Pumps & Solenoids
- **Magnetic Impeller Drain Pump**:
  - Permanent-magnet synchronous motor with a hermetically isolated rotor cavity (no shaft seals to leak).
  - *Projects*: DIY water-chiller cooling loop for CO2 laser cutting tubes or TIG welding torches; fountain and garden hydroponics transfer pumps.
- **Dual Water Inlet Solenoids**:
  - Fast-acting 12V DC [TYPICAL] or 120V AC [TYPICAL] electromagnetic diaphragm valves designed for household water pressure (30–80 PSI).
  - *Projects*: Arduino-controlled automated greenhouse watering system, high-speed photography liquid splash drop synchronizers.

---

## Module 4: Mobility, Personal EVs & Power Tools

### 1. Hoverboard Hub Motors & Mainboard Hacking

```
Hoverboard Electronics Architecture:
[ 36V 4.4Ah 18650 Battery ] ---> [ Mainboard (STM32 MCU + Dual Inverter) ]
                                      |                    |
                                      v                    v
                             [Left Hub BLDC]        [Right Hub BLDC]
                             (30 Neodymium Poles)   (30 Neodymium Poles)
```

#### What to Extract:
1. **Dual Brushless Outrunner Hub Motors**: 6.5", 8", or 10" diameter solid/pneumatic rubber wheels with integrated 3-phase BLDC motors, 30 neodymium permanent magnet poles, and 3 internal Hall-effect sensors.
2. **Main Controller Board**: Typically powered by an **STM32F103** or GD32 ARM Cortex-M micro-controller driving 12 high-current MOSFETs configured as two 3-phase inverters.
3. **Lithium Battery Pack**: 36V (10S2P) battery pack consisting of 20 x 18650 high-discharge lithium-ion cells with an internal BMS.

#### The Open-Source Hack (Hoverboard-Firmware-Hack):
You do not need to throw away the controller! The maker community created custom open-source firmware (available on GitHub: `hoverboard-firmware-hack`).
- Flash custom firmware via an inexpensive ST-Link V2 programmer into the onboard STM32 chip.
- The board can then accept direct steering and speed commands via **UART serial commands from an Arduino/Raspberry Pi, standard RC hobby receivers (PWM), or analog joystick voltages**.

#### Creative Repurposing Ideas:
- **Autonomous Guided Vehicle (AGV) / Heavy Robot Rover**: Two hoverboard wheels provide 50+ lbs of direct payload drive power over grass, gravel, and curbs without any external gearboxes.
- **Electric Motorized Wheelbarrow / Yard Cart**: Add a thumb throttle to the handles of an ordinary wheelbarrow to effortlessly haul 300 lbs of wet concrete or soil up steep backyard hills.
- **ODrive Closed-Loop Robotics Actuator**: Pair the hub motor with an external capacitive or magnetic rotary encoder (e.g., AS5600) and an **ODrive motor controller**. The motor becomes a zero-backlash, high-bandwidth precision servo joint capable of powering quadruped robot legs (Boston Dynamics style) or heavy robotic arms.

---

### 2. Cordless Drills & Impact Drivers

```
Drill Modular Powertrain:
[Mabuchi 550 Motor] ===> [Multi-Stage Planetary Gearbox] ===> [Torque Clutch] ===> 1/2" Chuck
```

#### Anatomy of a Cordless Drill:
A complete self-contained electromechanical power pack:
- High-current 550 or 775-size brushed DC motor (or modern sensorless 3-phase BLDC).
- 2-stage or 3-stage steel planetary gearbox (yielding 24:1 to 36:1 gear reduction).
- Adjustable mechanical ball-detent clutch.
- Trigger switch with integrated high-frequency PWM speed controller and heat sink.

#### Combat Robotics Hack:
To repurpose drill gearboxes for combat or rough mobile robots:
1. Strip the outer ergonomic plastic clam-shell.
2. **Lock the Clutch**: Disassemble the clutch collar and epoxy, pin, or weld the ball-detent plate solid. Otherwise, sudden acceleration or hard impacts will slip the clutch.
3. Clamp the outer ring gear firmly inside a custom aluminum or 3D-printed bracket so the transmission housing doesn't spin freely under load.

#### Creative Repurposing Ideas:
- **Motorized Kayak Trolling Thruster**: Mount a sealed drill motor and gearbox inside a waterproofed PVC pod driving a model boat propeller for a silent kayak pusher.
- **Automatic Wire / Coil Winder**: Mount an optical turn counter to the drill chuck. Use the drill's variable trigger to wind thousands of turns of fine magnet wire for custom guitar pickups or transformers in seconds.

---

### 3. High-Speed Digital Vacuum Turbines (Dyson Type)
Modern bagless cordless vacuums utilize ultra-compact, high-frequency digital brushless switched reluctance motors spinning between **100,000 and 125,000 RPM [TYPICAL]**.

#### Creative Repurposing Ideas:
- **DIY Desktop Thermoforming Vacuum Former**: Traditional shop-vacs take several seconds to pull air down. A digital vacuum motor generates instantaneous high-static suction to pull heated sheets of plastic tightly over 3D-printed molds before the plastic cools.
- **High-Velocity Mini Wind Tunnel**: Aerodynamic testing of miniature model airfoils, drone propellers, or model rockets.

---

## Module 5: Lab, Office & Scientific Scrap Gems

```
                       [ Syringe Pump Stepper ]
                                  |
                           (Anti-Backlash Nut)
                                  |
                                  v
                      [ Microliter Liquid Dosing ]
```

### 1. Medical Infusion Pumps & Syringe Feeders
- **The Core Hardware**: Miniature hybrid bipolar stepper motors coupled to zero-backlash, ground ball-screws or micro-metric lead screws.
- **Repurposing**:
  - **Automated Solder Paste & Flux Dispenser**: Mount a standard 10cc solder paste syringe directly into the sled. Pressing a foot pedal microsteps the motor forward to deposit repeatable, microscopic solder paste dots on surface-mount PCB pads.
  - **Precision Hydroponic pH & Nutrient Dosing**: Micro-doses concentrated acid/base solutions in drops as small as 0.05 mL into aquaponic reservoirs.

### 2. Barcode Scanners & Laser Printers: Polygon Mirrors
- **The Core Hardware**: A tiny, ultra-high-speed motor spinning a multi-faceted optical polygonal mirror block at 10,000–30,000 RPM [TYPICAL] with rock-solid rotational phase stability.
- **Repurposing**:
  - **DIY 360-Degree LiDAR**: Bounce a focused time-of-flight (ToF) laser rangefinder sensor off the spinning polygonal mirror to create a sweeping horizontal laser radar for robot obstacle avoidance and room mapping.

### 3. Ultrasonic Humidifiers & Atomizers
- **The Core Hardware**: High-frequency piezoelectric ceramic discs resonating at 1.6 MHz to 2.4 MHz.
- **Repurposing**:
  - **Acoustic Levitation Chamber**: Arraying ultrasonic transducers creates standing sound waves with acoustic nodes capable of levitating small water droplets, styrofoam beads, or insects in mid-air.
  - **Aeroponic Plant Root Mist Systems**: Atomizes nutrient water into microscopic 5-micron droplets that nourish plant roots suspended in air for 3x faster growth rates.

---

## Module 6: Non-Motor Salvageable Electromechanical Gems

Never throw away the rest of the chassis when harvesting motors! Old equipment contains mechanical components that cost a fortune to purchase individually from industrial suppliers:

```
+-------------------------------------------------------------------------+
| SOURCING NON-MOTOR HARDWARE:                                            |
|                                                                         |
| Printers & Scanners  ---> Hardened ground steel shafts (6, 8, 10mm)     |
|                      ---> Sintered bronze & PTFE linear bushings        |
|                      ---> GT2-style timing belts & toothed pulleys      |
|                                                                         |
| Power Supplies       ---> Extruded aluminum finned heat sinks           |
|                      ---> High-current inductors & toroidal ferrite     |
|                      ---> 12V 40A switching rails & Schottky diodes     |
|                                                                         |
| Microwaves & Tools   ---> Heavy-duty Omron microswitches (15A snap)     |
|                      ---> Beefy SPST / DPDT rocker & toggle switches    |
+-------------------------------------------------------------------------+
```

1. **Precision Shafts & Bearings**:
   - Printers and scanners provide ground linear rails that do not rust. Match them with budget LM8UU linear bearings or salvage their native bronze bushings for custom 3D printers and laser cutters.
2. **Timing Belts & Pulleys**:
   - Modern printers use glass-fiber reinforced rubber timing belts (often MXL or GT2 profiles) and matching aluminum/nylon pulleys, ready for zero-slip mechanical gear reduction.
3. **High-Power Solid-State Components**:
   - Computer ATX power supplies are modular 12V, 5V, and 3.3V power stations. A 500W PC power supply can pump out 30–40 Amps at 12V DC [TYPICAL] continuously—the perfect free benchtop power supply for testing your salvaged automotive and drill motors.
4. **Snap-Action Microswitches**:
   - Microwave door interlocks contain three industrial-grade Omron microswitches rated for 15A at 250V AC. They make virtually indestructible homing limit switches for CNC routers and 3D printers.

---

## Module 7: The Master Driver & Diagnostic Field Guide

### 1. Decoding Unknown Motors by Wire Count

```
               [ Count the Motor Wires ]
                          |
      +-------------------+-------------------+
      |                   |                   |
   2 Wires             3 Wires             4 Wires
      |                   |                   |
[Brushed DC or AC]  [3-Phase BLDC or]   [Bipolar Stepper]
(Check resistance    [AC Cap-Run Ind.]  (Two distinct coil
 & back-EMF)         (Identical coils    pairs with equal
                      between phases)    resistance)
                          |
      +-------------------+-------------------+
      |                                       |
   5 or 6 Wires                            8+ Wires
      |                                       |
[Unipolar Stepper]                      [BLDC with Hall Sensors]
(Common center-taps                     (3 heavy phase wires +
 have 1/2 resistance                    5 thin Hall-effect wires:
 to coil ends)                           VCC, GND, Ha, Hb, Hc)
```

### 2. Universal Motor Controller Matchup Table

| Motor Type | Recommended Salvaged / Budget Driver | Control Interface | Notes |
| :--- | :--- | :--- | :--- |
| **Small Brushed DC (< 2A)** | L298N Dual H-Bridge module | Arduino PWM + Direction Pins | Simple, cheap; has ~1.5V internal transistor voltage drop |
| **Heavy Brushed DC (10A–40A)** | BTS7960 43A High-Power H-Bridge | 5V PWM + Enable pins | Robust, runs cool with 12V wiper, drill, and window motors |
| **Bipolar Steppers (< 1.5A)** | A4988 / DRV8825 / TMC2209 | STEP / DIR digital pulses | Must set current-limit potentiometer before connecting motor! |
| **High-Power Steppers (> 2.5A)**| TB6600 or DM542 Industrial Driver | Opto-isolated STEP / DIR | High-voltage capable (up to 48V DC [TYPICAL]) for smooth high-speed CNC |
| **Sensorless BLDC (High Speed)**| Hobby RC Electronic Speed Controller (ESC)| 50Hz Servo PWM signal (1ms–2ms) | High RPM; poor zero-speed startup torque |
| **Sensored BLDC (High Torque)** | E-Bike / Scooter Controller (or VESC / ODrive)| Analog throttle (0–5V) or UART / CAN | Full torque down to zero RPM; regenerative braking |
| **High-Voltage PMDC (Treadmill)**| KBIC-120/240 SCR Drive or HV-PWM Module | 5k Potentiometer or 0–10V analog | Excellent low-speed torque via armature back-EMF feedback |
| **AC Universal Motor (Washer)**| TDA1085 Closed-Loop Phase Angle Board | Speed Potentiometer + Tacho feedback | Maintains exact RPM under heavy cutting or sawing loads |

---

## Module 8: Scrapper's Safety & Survival Protocols

> [!IMPORTANT]
> 1. **The Dangerous Capacitors**: Disconnect all power before disassembly. CRT televisions, microwave ovens, photo-flash units, and variable frequency drives (VFDs) store lethal charge long after being unplugged. Discharge them across a 1k-ohm 20W cement resistor (or an insulated screwdriver blade touched across terminals to ground) before handling.
> 2. **Toxic Heavy Metals & Powders**: 
>    - Avoid breaking old fluorescent/CCFL tubes (mercury vapor).
>    - Avoid grinding or chipping ceramic magnetron insulators in microwaves (often contain **Beryllium Oxide (BeO)**, which is carcinogenic if inhaled as dust).
>    - Never cut open sealed lithium-ion battery cells.
> 3. **High-Tension Springs**: Mechanisms in garage door openers, lawnmower recoil pull-starters, and vacuum cord-retractor reels contain tightly wound coiled clockwork springs that can release violently upon disassembly. Wear full-face protection and gloves when prying housings open.

---

## Module 9: Modern E-Waste, High-Voltage EVs & Advanced Mechatronics

| Donor Device | Harvestable Component | Typical Specifications | Primary Repurposing Targets | Danger Rating |
| :--- | :--- | :--- | :--- | :--- |
| **CPAP / BiPAP Medical Units** | Micro-Centrifugal BLDC Blower | 12V–24V DC [TYPICAL], 30,000–60,000 RPM [TYPICAL], >60 cmH2O static pressure | High-static HEPA fume extractor, SMD vacuum pick-and-place pen, micro-CNC vacuum hold-down bed | 🟢 Safe (Low Voltage) |
| **Robot Vacuums (Roomba/Roborock)** | 360° LDS LiDAR Turret | 5V DC motor, optical ToF / triangulation, 115200 baud UART | Plug-and-play ROS2 / Nav2 autonomous mapping AGV rover (bypasses custom polygon builds) | 🟢 Electronics |
| **Induction Cooktops (1,800W)** | Litz-Wire Pancake Coil, 1200V IGBTs, MKP Caps | 20A–40A 1200V IGBTs, 0.3µF–5µF 1200V MKP pulse caps | Zero-Voltage Switching (ZVS) blacksmith induction forge, crucible metal melter, bolt heater | 🔴 High Voltage / RF |
| **Scrap Electric Vehicles (Leaf/Tesla/Volt)** | HV Sealed Contactors & 30Ω-50Ω 100W Resistors | 400V–900V DC 500A nitrogen-sealed relays; wirewound resistors | 48V–400V solar battery bank disconnects, high-power inverter soft-start pre-charge networks | 🔴 High-Voltage DC |
| **3D Printers & CNC Scrap** | Strain Gauge Load Cells & Optical Endstops | 1kg–5kg aluminum Wheatstone bridge flexures + HX711 24-bit ADC | Sub-gram resin/epoxy mixing scales, rocket/propeller thrust dynos, alternator dyno load cells | 🟢 Precision |
| **Bicycles, ATVs & Mowers** | Bowden Cables (Steel Inner Wire + Conduit) | 1.2mm–2.0mm braided stainless wire in compression-less housing | Remote mechanical tendon actuation: relocating heavy motors to base chassis to eliminate wrist inertia | 🟢 Mechanical |
| **Electric Scooters (Ninebot/Xiaomi)** | 36V 350W Narrow Front Hub + Hall Throttle | 8.5"–10" pneumatic tire BLDC hub, 36V 15A regen controller | Motorized heavy shop carts, variable-speed bandsaw drives, linear gantry traction drives | 🟢 Safe (36V DC [TYPICAL]) |
| **HVAC Condenser Units** | 40A Double-Pole Definite Purpose Contactors | 24V AC [TYPICAL] or 120V AC [TYPICAL] coil, heavy silver-alloy contact pads | Master emergency-stop power disconnect relays for 2x72 belt grinders, lathes, and kilns | 🟡 Mains |
| **Medical Oxygen Concentrators** | Oil-Free Wobble-Piston Compressor + 13X Sieve Beds | 120V AC [TYPICAL] 1/3 HP, 5–10 LPM @ 93% pure O2, 4-way valve | 2,600°C oxy-propane glass torch, carbide brazing, ozone water sterilizer, oil-free CNC air | 🟢 Chemical/Gas |
| **Hybrid / EV AC Compressors** | High-Voltage Hermetic Scroll + 3-Phase PMSM | 144V–400V DC (runs on 48V–72V ESC), orbital scroll | 15+ CFM ultra-quiet shop air compressor (zero piston clatter), organic Rankine steam expander | 🟡 High Voltage |
| **Industrial Sewing Machines** | 550W–750W TEFC Brushless Servo + Hall Foot Pedal | 110V AC, optical encoder, 0–4,500 RPM [TYPICAL], instant brake | Variable-speed metal lathe spindle (high low-RPM threading torque), drill press drive, tapping head | 🟢 Precision |
| **Commercial Ice Makers** | Hot-Gas Bypass Solenoids & 3–6 RPM [TYPICAL] Auger Motors | Cryogenic/heat rated brass valves; high-torque auger | Automated LN2 cryocooler dosing, heavy clay pug mills, recycled plastic filament extruders | 🟡 Pressure/Mains |
| **Semiconductor / Lab Surplus** | Thermal Mass Flow Controllers (MFCs — MKS/Brooks) | 0–5V / RS-485 proportional valve + capillary sensor | Precision shielding gas blender for exotic TIG welding, CVD carbon nanotube furnace gas metering | 🟢 Scientific |
| **Telecom / Ham Radio Surplus** | Motorized Variable Vacuum Capacitors & Roller Coils | 5 kV to 35 kV RF rating, evacuated copper bellows | MHz induction heating tank auto-tuner, RF plasma sputtering impedance matchbox | 🔴 High-Voltage RF |
| **Blown Subwoofers & PA Speakers** | Massive Strontium-Ferrite Rings & 2"–4" Voice Coils | 100W–2,000W linear electromagnetic travel (±25mm) | Heavy electrodynamic shaker table (avionics resonance / concrete degassing), Stirling alternator | 🟢 Safe (Low Voltage) |
| **Broken Camera Lenses** | Ultrasonic Traveling-Wave Ring Motors (USM / SWM) | Piezo traveling wave stator, hollow bore (Ø35–65mm) | Hollow-bore laser polarizer rotator, zero-backlash microscope turret, zero-EMI cleanroom stage | 🟢 Optics |
| **Hospital Beds & Patient Lifts** | 24V Sealed Medical Linear Actuators (Linak) | 1,000–2,000 lbs (4,000–8,000 N) thrust, IPX6 washdown | Heavy hydraulic dump trailer lift, seasonal solar array tilt jack, ergonomic welding positioner | 🟢 Mechanical |
| **Heavy Diesel Trucks** | Variable Geometry Turbochargers (Holset HE351VE) | Inconel 713C turbine + sliding vane CAN actuator | DIY micro-gas-turbine jet engine (Brayton cycle, 40 lbs thrust), extreme foundry forge blower | 🔴 High Temp/Speed |
| **Enterprise Server Racks** | Counter-Rotating Dual Fans & 2kVA UPS Toroids | 12V 3A–6A Delta blowers (>3" H2O); 2kVA iron toroids | Blast furnace tuyere air supply; heavy pure-sine off-grid inverter output transformers | 🟡 Mains/High Speed |
| **Broken Digital Calipers & Scales** | Capacitive Linear Encoder Strip + ASIC | 0.01mm (10 µm) resolution, 1.5V logic, 24-bit serial output | Multi-axis mini-lathe / mill DRO (immune to optical dust), closed-loop linear actuator feedback | 🟢 Precision |
| **CNC Scrap / CMM Machines** | Optical Linear Glass Scales (Heidenhain/Renishaw) | 1 µm to 0.1 µm (100 nm) resolution, 1Vpp / RS-422 TTL | Sub-micron closed-loop CNC conversion, coordinate measuring machine (CMM), lithography stage feedback | 🟢 Precision |
| **Auto Camshaft VVT Systems** | Oil-Control Spool Valves (OCV) | 12V DC [TYPICAL] high-frequency PWM 4-way spool valve (150+ Hz response) | Closed-loop electro-hydraulic servo press (paired with ABS pump), robotic hydraulic muscle controller | 🟢 Low-Voltage |
| **Gas & Water Utility Meters** | Nutating Disc / Diaphragm Chambers + Magnetic Drive | Zero-leak magnetic coupling through brass bulkhead; volumetric pulses | Closed-loop chemical batching, fuel telemetry, low-RPM positive displacement air motor | 🟢 Mechanical |
| **35mm SLR Cameras & Mech Watches** | Mechanical Escapement Timers & Focal-Plane Shutters | Swiss jewel gear train + balance wheel; 1 ms titanium/cloth slit | Zero-power mechanical time-delay latches, ultra-high-speed optical laser beam choppers | 🟢 Fine Mechanics |
| **Commercial Carpet Extractors & Washers** | Triplex Ceramic Plunger Pumps + Unloader Valves | 500–3,000 PSI ceramic plungers, forged brass manifold, bypass unloader | High-pressure abrasive waterjet cutter, hydrostatic burst-testing pressure rig | 🔴 Extreme Pressure |
| **Vending Machines (Bill/Coin Mechs)** | Multi-Spectral Optical Sensors + Geared Pinch Rollers | IR/UV/Red transmissive LEDs + sensors, 12V/24V urethane rollers | Automated 3D printer filament feeder, counterfeit/material optical sorting conveyor, sheet metal feeder | 🟢 Automation |
| **Audiophile Turntables & Broadcast Decks**| Coreless Slotless Direct-Drives & Ruby Gimbal Bearings| Zero-cogging ironless stator; low-friction tonearm jewel gimbals | Vibration-free micro-mirror galvanometer, ultra-sensitive mass balance comparator, low-stiction wind vane | 🟢 Precision |
| **Laser Printer Toner Cartridges** | Sub-Micron Magnetite (Fe3O4) Powder | 40%–50% Fe3O4 nanoparticles coated in resin, sub-micron | Custom magnetorheological (MR) fluids, programmable haptic dials, non-wearing variable torque brakes | 🟡 Chemical/Dust |
| **Defibrillators & Studio Strobes** | High-Current Pulse Capacitors & SCR Switches | 330V–450V low-ESR pulse electrolytics or 2.7V 3,000F supercaps | 3,000A capacitive-discharge (CD) battery tab spot welder, electromagnetic coilgun, magnetizer | 🔴 High Current/HV |
| **Bosch ABS Hydraulic Pump Blocks** | 12V PMDC Motor + Dual Opposed Radial Micro-Pistons | 12V 40A, 180 bar (2,600 PSI) working pressure, integrated block | Ultra-compact hydraulic power unit (HPU) for miniature servo presses, sheet metal dimplers, benders | 🟡 High Pressure |
| **Microwave Turntable Magnet Rings** | Sintered Multi-Pole Ferrite / Neodymium Magnet Rings | Concentric multipole radial geometry, high remanence | Coaxial magnetic planetary gearboxes, hermetic non-penetrating drives for chemical reactors & autoclaves | 🟢 Safe (Magnetic) |

---

## Complete Blueprint Compendium (50 Production Engineering Blueprints)

1. **Direct-Drive Wind / Hydro Generator**: LG Direct-Drive washing machine pancake stator + MDS-100A rectifier for 500W silent generation at 120–250 RPM [TYPICAL].
2. **Direct-Drive Sim Racing Wheel**: Automotive EPS steering column + STM32 "BluePill" (OpenFFB/MMOS) + BTS7960 driver for 25–30 Nm [TYPICAL] force feedback.
3. **Audio-Driven Laser Vector Galvanometer**: Dual HDD voice coils + front-surface mirrors + 20W stereo amplifier for vector laser projection.
4. **2" x 72" Knifemaker's Belt Grinder**: 2.5 HP Treadmill PMDC motor + KBIC-120/240 SCR speed drive with IR compensation.
5. **18650 Battery Pack Spot Welder**: Rewound Microwave Oven Transformer (2–3 turns of 2 AWG cable) delivering 3.5V @ 700A with Arduino dual-pulse SSR timing.
6. **Micro-Laser Engraver / 2D Plotter**: Dual DVD-RW sled micro-steppers + AixiZ laser diode + Arduino Nano running GRBL 1.1.
7. **Whisper-Quiet Airbrush & Vacuum Degas Chamber**: Refrigerator hermetic compressor (<40 dB) + coalescing filter + 1" Lexan polycarbonate vacuum lid.
8. **Heavy Autonomous Robot Rover (AGV)**: Reprogrammed 36V hoverboard motherboard (flashed via ST-Link) + dual 350W hub motors carrying 100+ lbs over rough terrain.
9. **DMD Maskless Semiconductor Photolithography Station**: Sub-micron UV direct-write lithography for custom microfluidics and FETs with Python tiled stepping code.
10. **Precision 30 kHz Ultrasonic Craft & Resin Knife**: Stepped titanium velocity booster horn + Langevin dental transducer for frictionless slicing of carbon fiber and resin supports.
11. **Alternator Steady-State Absorption Engine Dynamometer**: Trunnion cradle + S-beam load cell + Arduino closed-loop PID field coil control for real continuous horsepower/torque curves.
12. **Desktop Abrasive Slurry Micro-Waterjet Cutter**: Procon 250 PSI brass rotary vane pump + venturi abrasive mixer slicing sheet aluminum and carbon fiber cleanly.
13. **Solid-State Woodstove Seebeck Generator Stack**: Compression-clamped Bi2Te3 modules + LTC3780 buck-boost supplying 15W continuous off-grid emergency power.
14. **2,000W ZVS Induction Forge from a Scrap Induction Cooktop**: Mazzilli self-resonant ZVS oscillator + salvaged Litz/copper coil + MKP 1200V tank capacitors heating 1/2" steel to 1,000°C in 15 seconds.
15. **High-Static CNC Vacuum Chuck & Pick-and-Place Station from a CPAP Turbine**: 50,000 RPM [TYPICAL] CPAP micro-turbine + 30A RC ESC + mini cyclone chip separator holding 0.5mm PCB blanks flat and manipulating 0402 SMD components.
16. **Oil-Free Oxy-Propane Glassworking & Brazing Station from a Medical Oxygen Concentrator**: Arduino Nano cycling 4-way valve across twin 13X zeolite beds for continuous 8 LPM O2 feeding a 2,600°C torch with zero rented cylinders.
17. **Magnetorheological (MR) Programmable Haptic Knob & Torque Brake**: Sealed rotor cup filled with laser-printer toner magnetite + oil slurry driven by an ESP32 and HDD encoder to synthesize variable detents, viscous drag, and hard end-stops.
18. **Monolithic Flexure-Guided Interferometer & Sub-Micron Z-Stage**: Aluminum 4-bar parallelogram flexure stage driven by DVD-sled stepper + 20:1 lever arm paired with a Blu-Ray optical pickup to measure nanometer displacements via optical fringe counting.
19. **3,000A Supercapacitor Pulsed Spot Welder & Magnetizer**: Maxwell 2.7V 3,000F ultracaps + 8x parallel IRLB3034 MOSFET array + TC4420 gate driver delivering sub-millisecond pulses with zero cell heating.
20. **Closed-Loop Electro-Hydraulic Servo Press from an ABS Block & VVT Spool Valve**: Bosch ABS pump + automotive VVT 4-way spool valve + digital caliper scale + ESP32 nested PID loop for 2,000 PSI precision micro-pressing.
21. **Magnetic-Coupled Hermetic High-Pressure Autoclave & Vacuum Stirrer**: Non-contact concentric N52 neodymium magnetic transmission across a 316L stainless steel dome with ceramic bearings for 100-bar hydrothermal reactions.
22. **Zero-Cogging Astronomical Telescope Tracking Mount**: Technics SL-1200 style coreless axial-flux direct-drive BLDC motor + AS5600 magnetic encoder on polar axis running OnStep firmware for sub-arcsecond tracking with zero gear backlash.
23. **Ultra-High-Speed 40,000 RPM [TYPICAL] Micro-CNC PCB Milling Spindle**: 3548 1100KV outrunner BLDC + ER11 8mm precision collet arbor + dual ABEC-9 hybrid ceramic ball bearings in liquid-cooled aluminum water jacket for vibrationless 0.1mm micro-trace isolation routing.
24. **Heavy Workshop 12" Disc & Flap Surface Grinder**: 1,800W direct-drive lawnmower induction motor + 12" ground aluminum disc wheel + cast iron tilting table with dynamic reverse-current safety brake stopping 10,800 SFPM disc in under 3 seconds.
25. **Supercritical LeBlanc Self-Balancing High-Speed Centrifuge**: Front-load washer annular fluid/ball-balancer ring mounted on flexible quill shaft below 45-degree aluminum angle rotor, automatically eliminating unbalance vibration forces above 1,200 RPM [TYPICAL] resonance.
26. **Zero-Backlash Heavy Robotic Arm Cycloidal Reducer (50:1)**: Dual 180° opposed 1095 tool steel cycloid discs + 51 needle roller stationary pins + eccentric cam shaft delivering 150 N·m [TYPICAL] continuous torque with 500% shock load tolerance and zero backlash.
27. **Heavy Series-Wound DC Gantry Hoist & Mini-Excavator Drive**: 48V 5–8 HP forklift series DC motor + dual Albright SW180 reversing contactors + Curtis 300A PWM controller lifting 3,000 lbs dead weight with massive low-end torque.
28. **Sub-Micron Machine Tool Linear Optical Scale DRO**: Heidenhain / Renishaw CNC glass scales + MAX485 differential RS-422 transceivers + ESP32 hardware pulse counter (PCNT) displaying 0.1 micron (100nm) tool position on 7" touchscreen.
29. **Automated 6-Station Rotary Geneva Indexing Table**: Hardened steel 6-slot Maltese cross Geneva wheel + continuous pin drive with locking dwell disc + 10" aluminum tooling platter providing exact 60° indexing with positive mechanical dwell lock.
30. **Whisper-Quiet 15 CFM Orbital Scroll Workshop Compressor**: Automotive Prius/Leaf 3-phase hermetic scroll A/C compressor driven by 48V VESC controller running sensorless FOC with coalescing oil separator delivering 15+ CFM at 135 PSI under 50 dB noise.
31. **Decoupled Antagonistic Bowden-Cable Robotic Arm Wrist**: Stationary base-mounted NEMA 23 stepper motors + stepped dual-groove capstans driving 1/8" aircraft cables through Kevlar compressionless conduits for a zero-motor-mass 3-DOF robot wrist.
32. **Diamond-Traverse Filament & Wire Level-Winding Machine**: Cylindrical barrel cam with bidirectional crossed helical diamond grooves + sintered diamond-hard Al2O3 ceramic eyelet (Mohs 9) for level-wind spooling of 3D printer filament or transformer coils.
33. **Pure Sinusoidal Harmonic Shaker Table & Fatigue Tester**: Slotted Scotch yoke slider mechanism + 2.5 HP treadmill PMDC motor with heavy cast flywheel producing pure sinusoidal 0–60 Hz linear harmonic vibration without connecting-rod angular side-thrust.
34. **Full-Scale Abrasive Hydro-Carbide Waterjet Cutter (3,000 PSI)**: Commercial triplex plunger pump with solid ceramic plungers + 0.010" sapphire orifice + tungsten carbide mixing tube slicing 1/2" aluminum, steel, and titanium with zero heat-affected zone.
35. **Non-Contact Magnetostrictive Engine Dynamometer Torque Meter**: E-bike torque-sensing bottom bracket chromoly spindle + stationary coaxial high-frequency sense coils + INA128 instrumentation amp measuring dynamic shaft horsepower up to 150 N·m [TYPICAL].
36. **Desktop Submerged Wire Electrical Discharge Machine (Wire-EDM)**: Dual-axis scanner linear stepper stages + 80V 10A pulsed MOSFET power supply + continuous brass wire spooler slicing intricate shapes through hardened 52100 tool steel with 0.001" precision.
37. **High-Speed 45,000 RPM [TYPICAL] Polygon Mirror Laser Engraver**: Laser printer polygon mirror scanner + F-theta distortion-correcting scan lens + Teensy 4.1 microsecond modulation producing raster laser sweep speeds exceeding 200 meters/second.
38. **Ultra-Low-RPM Direct-Drive Vertical-Axis Wind Turbine (VAWT)**: Re-terminated 36-pole SmartDrive washing machine pancake stator in parallel Delta configuration + MDS-100A bridge rectifier generating 800W charging power at gentle 120 RPM [TYPICAL] breeze.
39. **Pneumatic Power Forging Hammer (10 Joules / 250 BPM)**: SDS-Max heavy rotary hammer drill impact piston assembly + 100 lb cast-iron anvil + foot-pedal speed control delivering 250 rapid forging blows/minute for drawing out damascus steel.
40. **Precision 4th-Axis Harmonic CNC Rotary Trunnion Table**: 100:1 zero-backlash harmonic strain-wave reducer + NEMA 23 stepper + 6" 3-jaw chuck for 4-axis simultaneous CNC contour milling of turbine impellers with 0.001° resolution.
41. **Electro-Hydraulic Servo Stamping Press (20 kN Force)**: Automotive electronic parking brake (EPB) planetary ball-screw ram + 20 kN S-beam load cell + BTS7960 H-bridge for closed-loop 2-ton stamping and hole punching with digital tonnage cutoff.
42. **Automated Multi-Axis CNC Coil & Transformer Winder**: Flatbed scanner ground linear guide rails + 2x NEMA 17 steppers (spindle & traverse) + Arduino CNC Shield winding 10,000 turns of humbucker pickup or transformer coil with automatic pitch indexing.
43. **Eddy-Current Absorption Dynamometer (25 HP Dissipation)**: Dual automotive alternator wound-field rotors exciting adjacent solid steel discs across 1.5mm air gap, absorbing and measuring 25 HP smoothly via S-type load cell with zero brake pad wear.
44. **Sub-Nanometer AFM Piezo Scanners & Beam-Steering Platform**: Monolithic 7075-T6 aluminum parallelogram flexure stage driven by multi-layer PZT ceramic stacks and ultra-low-noise 100V linear driver for 0.1nm atomic force microscopy translation.
45. **High-Vacuum Turbomolecular Sputtering Chamber (10^-7 Torr)**: 90,000 RPM [TYPICAL] magnetically levitated turbomolecular vacuum pump backed by two-stage rotary vane forepump for physical vapor deposition (PVD) sputtering of optical coatings at 10^-7 Torr.
46. **Workshop Metallurgy Spark-Testing Inspection Station**: 3,450 RPM [TYPICAL] pedestal grinder with dressed vitrified Al2O3 wheel + matte black spark containment hood + certified alloy coupons for 10-second scrap steel alloy classification by spark starburst morphology.
47. **Automated Continuous Recycled Plastic Filament Extruder**: Commercial soft-serve 40:1 all-steel planetary auger reducer + 1 HP AC induction motor + 3-zone PID heated barrel (260°C) converting shredded PET plastic bottles into 1.75mm 3D printer filament.
48. **Variable-Speed Lathe Spindle Drive Conversion**: 750W industrial direct-drive sewing machine brushless servo motor + DSP vector inverter box providing full rated torque down to 50 RPM [TYPICAL] with instant needle-positioning electromagnetic braking.
49. **Kinetic Energy Buffer Flywheel with Sprag Overrunning Clutch**: Automotive starter motor Bendix sprag one-way clutch + 15 lb cast iron treadmill flywheel on 1" shaft, absorbing motor shock and feeding stored kinetic inertia into high-load punch presses.
50. **Safe Multi-Stage Hydrostatic Pressure Testing Rig (5,000 PSI)**: Commercial triplex plunger pump + 6,000 PSI liquid-filled gauge + forged needle bleed valves + polycarbonate burst shield for non-compressible hydrostatic proof-testing of home-welded pressure vessels.
