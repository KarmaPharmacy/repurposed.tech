"""
Builds detailed engineering specifications, interfaces, extraction tools, and failure modes
for all 100 donor streams in scripts/encarta_data.py.
"""

import os
import sys
import json
import re

WORKSPACE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if WORKSPACE not in sys.path:
    sys.path.insert(0, WORKSPACE)

import scripts.encarta_data as d

# Detailed domain data dictionary keyed by donor ID
ENRICHMENT_MAP = {
    # DOMESTIC APPLIANCES
    "microwave": {
        "diff": "Intermediate",
        "specs": "120V/240V AC mains input, 2,100V–2,500V AC secondary @ 500mA–1,000mA [TYPICAL], 800W–1,200W continuous",
        "tools": ["Insulated HV Discharge Wand (20W 2k-ohm)", "Torx T20 Security Bit", "Linesman Wire Cutters", "Digital Multimeter"],
        "interfaces": "1/4\" quick-connect spade lugs, 4-hole base plate mounting, 10mm D-profile turntable shaft",
        "hazards": "LETHAL 2,500V secondary winding shock hazard; Carcinogenic Beryllium Oxide (BeO) ceramic insulator rings; 1.0 uF 2,200V capacitor stored energy [VERIFIED]",
        "blueprints": [5, 14]
    },
    "washing_machine_dd": {
        "diff": "Intermediate",
        "specs": "36-pole 3-phase BLDC pancake stator, 48V–300V back-EMF, 500W–1,200W @ 120–800 RPM [TYPICAL]",
        "tools": ["17mm & 19mm Deep Sockets", "3-Jaw Mechanical Gear Puller", "Deadblow Mallet", "External Circlip Pliers"],
        "interfaces": "4-bolt stator spider mount (M8), 25mm tapered splined drum shaft, 3-pin UVW high-current terminal connector",
        "hazards": "Extreme magnetic pinch hazard between rotor neodymium magnets and iron stator teeth; galvanic embrittlement of cast aluminum spider bracket",
        "blueprints": [1, 27]
    },
    "washing_machine_classic": {
        "diff": "Novice",
        "specs": "120V/240V AC series universal motor, 8,000–16,000 RPM armature speed, 600W–1,000W [TYPICAL]",
        "tools": ["10mm Socket", "Slot Screwdriver", "Wire Strippers", "Tachometer Probe"],
        "interfaces": "Poly-V 5-rib drive belt pulley, 6-pin harness block (armature, field, tacho generator coils)",
        "hazards": "Runaway centrifugal explosion if operated unloaded on AC mains [VERIFIED]; commutator brush arcing and ozone generation",
        "blueprints": [48]
    },
    "treadmill": {
        "diff": "Intermediate",
        "specs": "90V–180V DC permanent magnet motor, 1.5–3.0 HP @ 4,000 RPM, 15A–25A continuous [TYPICAL]",
        "tools": ["Metric Allen Keys (5mm, 6mm)", "1/2\" Drive Socket Set", "Multimeter", "Soldering Iron"],
        "interfaces": "Pivoting steel base tension mount, 16mm keyed/threaded shaft with cast-iron inertia flywheel/pulley",
        "hazards": "320V DC bus filter capacitors on SCR drive board; heavy kinetic momentum of cast flywheel (requires rigid containment)",
        "blueprints": [4, 49]
    },
    "refrigerator": {
        "diff": "Advanced",
        "specs": "Hermetic reciprocating single-phase induction compressor, 1/6 to 1/4 HP, 120V/240V AC [TYPICAL]",
        "tools": ["Refrigerant Tubing Cutter", "4.5\" Angle Grinder with Cut-Off Wheel", "EPA Recovery Gauge Manifold", "Tubing Flare Kit"],
        "interfaces": "1/4\" & 5/16\" copper process and suction stubs, 3-pin hermetic glass-to-metal electrical feedthrough",
        "hazards": "Pressurized R134a/R600a refrigerant (EPA Section 608 recovery mandatory); mineral oil mist aerosolization upon decapping",
        "blueprints": [7, 47]
    },
    "induction_cooktop": {
        "diff": "Intermediate",
        "specs": "1,800W–2,200W ZVS resonant inverter, 20 kHz–35 kHz switching frequency, 120V/240V AC [TYPICAL]",
        "tools": ["Phillips #2 Screwdriver", "Plastic Spudger", "Oscilloscope with 100:1 HV Probe", "Soldering Iron"],
        "interfaces": "Litz-wire pancake work coil terminals, NTC surface thermistor sensor header, touch capacitive user interface ribbon",
        "hazards": "High-voltage high-frequency AC resonance (> 1,000V peak across resonant capacitor bank); 400V DC filter bus",
        "blueprints": [14]
    },
    "softserve_auger": {
        "diff": "Advanced",
        "specs": "1.5 HP to 2.5 HP single/three-phase gearmotor, 60–120 RPM continuous output, high-torque helical reducer [TYPICAL]",
        "tools": ["Metric Box Wrenches (13mm, 17mm, 19mm)", "Gear Puller", "Hex Bit Sockets", "Food-Grade Lubricant"],
        "interfaces": "Square-drive stainless output coupling, 6-bolt face mount, 304/316 stainless freeze cylinder",
        "hazards": "Extreme mechanical shear torque in auger flights; high thermal inertia in refrigerant cooling jacket",
        "blueprints": [21, 32]
    },
    "dishwasher_circulation": {
        "diff": "Novice",
        "specs": "120V/240V AC high-flow centrifugal pump, 80W–150W, integrated PTC flow-through heater (1,200W) [TYPICAL]",
        "tools": ["Hose Clamp Pliers", "Torx T15 & T20 Bits", "Multimeter"],
        "interfaces": "1\" & 1.25\" barbed hose ports, 4-pin quick connect harness, silicone anti-vibration rubber boots",
        "hazards": "Water and mains electricity proximity; dry-fire burning hazard if flow heater is energized without fluid",
        "blueprints": [21]
    },
    "microwave_turntable": {
        "diff": "Novice",
        "specs": "Synchronous permanent magnet geared motor, 21V–120V AC, 3–5 RPM, 2.5W–4W [TYPICAL]",
        "tools": ["Cross-Head Screwdriver", "Wire Strippers", "DMM"],
        "interfaces": "Plastic 3-lobe clover drive spindle, dual solder/push-on tabs, 2-hole flange mount",
        "hazards": "Shock hazard if energized on AC mains without grounding; gear stripping under rapid reverse shock load",
        "blueprints": [22]
    },
    "clothes_dryer_blower": {
        "diff": "Novice",
        "specs": "1/3 to 1/2 HP split-phase AC induction motor, 1,725 RPM, double-ended shaft with squirrel-cage blower [TYPICAL]",
        "tools": ["5/16\" Nut Driver", "Adjustable Wrench", "External Snap Ring Pliers"],
        "interfaces": "1/2\" left-hand threaded blower shaft, 1/2\" keyed pulley shaft, belt tensioner arm switch",
        "hazards": "Lint fire hazard; centrifugal start switch failure if lint clogs mechanical weights",
        "blueprints": [31]
    },
    "garbage_disposal": {
        "diff": "Intermediate",
        "specs": "1/2 to 3/4 HP capacitor-start induction motor, 1,725 RPM, massive stainless shredder flywheel [TYPICAL]",
        "tools": ["Pipe Wrench", "1/4\" Hex Disposal Wrench", "Hammer & Cold Chisel", "Impact Driver"],
        "interfaces": "Quick-lock sink flange ring, 1.5\" discharge elbow, 1/2\" threaded conduit electrical entry",
        "hazards": "High rotational kinetic energy; laceration hazard from centrifugal stainless impellers",
        "blueprints": [33]
    },
    "roomba_vacuum": {
        "diff": "Novice",
        "specs": "14.4V NiMH / Li-Ion battery pack, dual high-torque brushed worm drive wheels with optical encoders [TYPICAL]",
        "tools": ["Phillips #1 & #2 Screwdrivers", "Plastic Pry Tool", "DMM"],
        "interfaces": "Modular snap-in wheel modules, 4-pin battery connector, IR cliff sensor headers",
        "hazards": "Lithium cell short-circuit hazard during pack teardown; high-RPM side brush pinch points",
        "blueprints": [8, 24]
    },
    "water_dispenser_peltier": {
        "diff": "Novice",
        "specs": "TEC1-12706 thermoelectric Peltier cooler (12V DC, 6A, 60W), aluminum heatsink + 12V fan [TYPICAL]",
        "tools": ["Phillips Screwdriver", "Thermal Paste", "DC Power Supply"],
        "interfaces": "Flat 40x40mm ceramic thermal faces, 2-wire red/black DC lead, spring-loaded thermal clamp bar",
        "hazards": "Thermal stress cracking of Peltier bismuth telluride crystals if operated without heatsink",
        "blueprints": [13]
    },
    "gas_water_heater": {
        "diff": "Intermediate",
        "specs": "Thermopile generator producing 750 mV DC from pilot flame, millivolt gas safety solenoid valve [TYPICAL]",
        "tools": ["Tubing Wrenches (7/16\", 1/2\")", "Pipe Wrench", "Digital Multimeter (mV range)"],
        "interfaces": "1/2\" NPT gas inlet and outlet, 7/16\" pilot gas tube fitting, 2-screw thermocouple terminal block",
        "hazards": "Flammable natural gas / propane explosion hazard; verify main gas supply is shut off and lines purged",
        "blueprints": [13]
    },
    "breadmaker_kneader": {
        "diff": "Novice",
        "specs": "100W–200W shaded-pole / PMDC motor, dual-stage cogged timing belt reduction (10:1 ratio) [TYPICAL]",
        "tools": ["Phillips #2 Screwdriver", "Snap Ring Pliers", "Metric Hex Wrenches"],
        "interfaces": "Flatted kneader shaft with bronze oilite bushings, HTD 3M/5M timing pulleys and fiberglass belts",
        "hazards": "Pinch points in high-torque timing belt drives; thermal fuse blow-out if stalled",
        "blueprints": [23]
    },
    "coffee_burr_grinder": {
        "diff": "Intermediate",
        "specs": "350W–650W capacitor induction motor, 64mm–83mm tool steel flat burrs, 1,400 RPM [TYPICAL]",
        "tools": ["10mm Socket", "Spanner Wrench", "Dial Test Indicator", "Feeler Gauges"],
        "interfaces": "Threaded brass/aluminum micrometer collar (10 um pitch adjustment), 3-bolt burr carrier flange",
        "hazards": "Rotary cutting edge laceration; dulling precision cutting teeth if run with zero burr clearance",
        "blueprints": [21, 34]
    },

    # AUTOMOTIVE & TRANSPORTATION
    "eps_steering": {
        "diff": "Intermediate",
        "specs": "12V 40A brushless DC servo motor, 25–35 N*m force feedback torque through internal worm drive [TYPICAL]",
        "tools": ["12mm, 14mm, 17mm Sockets", "Angle Grinder with Flap Disc", "Wire Strippers", "Torque Wrench"],
        "interfaces": "Splined input and output steering shafts (36-tooth automotive spline), high-current 2-pin/3-pin power block",
        "hazards": "High-torque rotational whip if energized open-loop without software torque saturation limits [VERIFIED]",
        "blueprints": [2, 17]
    },
    "auto_alternator": {
        "diff": "Intermediate",
        "specs": "12V 100A–160A 3-phase Lundell rotor alternator with internal full-wave 6-diode rectifier bridge [TYPICAL]",
        "tools": ["15mm Socket", "Impact Gun", "Soldering Iron (60W+)", "Bearing Puller"],
        "interfaces": "V-belt or serpentine 6-groove pulley, 2-bolt pivot bracket, B+ high-current stud, rotor slip rings",
        "hazards": "High-current battery short-circuit arc flash; voltage spike (up to 80V load dump) if battery disconnected while spinning",
        "blueprints": [11, 28]
    },
    "abs_pump": {
        "diff": "Intermediate",
        "specs": "12V 25A high-pressure dual-piston hydraulic pump, capable of 2,000–2,500 PSI burst pressure [TYPICAL]",
        "tools": ["10mm & 11mm Flare Nut Wrenches", "T25 Torx Bit", "Brake Line Flaring Tool", "Safety Glasses"],
        "interfaces": "M10x1.0 & M12x1.0 inverted flare hydraulic ports, integrated 12V brushed PMDC motor with eccentric cam",
        "hazards": "Brake fluid injection hazard under line pressure; corrosive glycol-ether fluid attacks paint and skin",
        "blueprints": [12, 20]
    },
    "vvt_valves": {
        "diff": "Novice",
        "specs": "12V PWM proportional hydraulic spool valve (300 Hz carrier frequency), 1.0A–1.8A coil draw [TYPICAL]",
        "tools": ["10mm Socket", "Multimeter", "Pick Tool", "Clean Solvent"],
        "interfaces": "O-ring sealed cartridge sleeve (18mm–22mm diameter), 2-pin sealed automotive waterproof connector",
        "hazards": "Hot engine oil scald; solenoid inductive kickback voltage spikes (requires external flyback diode)",
        "blueprints": [20]
    },
    "air_suspension": {
        "diff": "Intermediate",
        "specs": "12V 30A oil-free single-cylinder reciprocating compressor with desiccant air dryer, 200–250 PSI [TYPICAL]",
        "tools": ["10mm Socket", "Push-to-Connect Tubing Release Tool", "Multimeter"],
        "interfaces": "4mm & 6mm nylon high-pressure pneumatic ports, 12V 40A sealed automotive relay harness",
        "hazards": "High pneumatic pressure burst hazard; thermal cylinder burn hazard under continuous duty",
        "blueprints": [15, 30]
    },
    "spal_fan": {
        "diff": "Novice",
        "specs": "12V DC high-output brushless / sealed brushed motor, 1,200–2,500 CFM airflow, 15A–30A draw [TYPICAL]",
        "tools": ["10mm Wrench", "Wire Crimpers", "Multimeter"],
        "interfaces": "Molded glass-filled nylon aerodynamic shroud, 2-pin Delphi Weatherpack high-current connector",
        "hazards": "Finger amputation hazard from high-velocity glass-filled nylon fan blades; high starting current surge",
        "blueprints": [30]
    },
    "starter_motor": {
        "diff": "Intermediate",
        "specs": "12V 1.4 kW to 2.2 kW series/compound DC motor, 150–250 N*m stall torque, planetary gear reduction [TYPICAL]",
        "tools": ["13mm, 15mm, 17mm Sockets", "Bench Vise", "High-Current Battery Cables", "Deadblow Hammer"],
        "interfaces": "Heavy cast aluminum nose cone with 2-bolt flange, 9-to-11 tooth pinion gear with sprag overrunning clutch",
        "hazards": "Massive 300A–500A starting arc flash; thermal burnout if cranked for more than 15 consecutive seconds",
        "blueprints": [49]
    },
    "electric_water_pump": {
        "diff": "Intermediate",
        "specs": "12V 15A–25A canned-rotor sensorless BLDC centrifugal water pump, 100–150 L/min flow rate [TYPICAL]",
        "tools": ["10mm Socket", "Hose Clamp Pliers", "PWM Signal Generator", "Multimeter"],
        "interfaces": "1.25\" & 1.5\" hose barb connections, 4-pin sealed connector (12V, GND, PWM speed in, Tach out)",
        "hazards": "Sensorless commutation loss if run dry (fluid serves as bearing lubricant); reverse polarity destruction",
        "blueprints": [27]
    },
    "wiper_motor": {
        "diff": "Novice",
        "specs": "12V DC 2-speed worm-drive PMDC gearmotor, 45/65 RPM, 20–35 N*m stall torque, self-locking [TYPICAL]",
        "tools": ["10mm & 13mm Sockets", "Flat Screwdriver", "Wire Cutters"],
        "interfaces": "Tapered knurled drive post with M8 nut, 3-bolt face mounting, 5-pin park-switch harness",
        "hazards": "Mechanical pinch in high-torque crank linkage; internal park switch arcing",
        "blueprints": [2, 26]
    },
    "throttle_body": {
        "diff": "Novice",
        "specs": "12V H-bridge driven DC servo motor, dual redundant analog potentiometer / Hall TPS sensors [TYPICAL]",
        "tools": ["10mm Socket", "Torx T20 Bit", "Digital Multimeter"],
        "interfaces": "Precision ground aluminum butterfly valve (50mm–75mm bore), 6-pin waterproof connector",
        "hazards": "High spring-loaded snap closure pinch hazard; sensor misalignment if throttle plate is forced",
        "blueprints": [17]
    },
    "diesel_common_rail": {
        "diff": "Master",
        "specs": "Radial 3-piston mechanical high-pressure fuel pump, 1,600 to 2,000 bar (23,000 to 29,000 PSI) [TYPICAL]",
        "tools": ["High-Pressure Flare Wrenches", "Triple-Square Sockets", "Cleanroom Bench Setup"],
        "interfaces": "Tapered keyed drive shaft, forged steel rail manifold, M14x1.5 high-pressure steel tube fittings",
        "hazards": "FATAL high-pressure hydraulic fluid injection hazard (> 1,500 bar cuts skin effortlessly) [VERIFIED]",
        "blueprints": [12, 34]
    },
    "golf_cart_traction": {
        "diff": "Intermediate",
        "specs": "36V–48V DC series/shunt wound traction motor, 3.0 HP–5.0 HP continuous, 19-tooth female splined shaft [TYPICAL]",
        "tools": ["1/2\" Drive Socket Set", "Snap Ring Pliers", "Heavy-Duty Cable Crimpers"],
        "interfaces": "19-tooth internal involute spline, 4-bolt differential transaxle flange, heavy copper 5/16\" terminal studs",
        "hazards": "Heavy weight (> 25 kg); massive DC arc flash when connecting to 48V battery banks without pre-charge resistor",
        "blueprints": [8, 41]
    },
    "electric_parking_brake": {
        "diff": "Novice",
        "specs": "12V DC planetary-plus-wobble-plate gearmotor, 150:1 gear reduction ratio, capable of 15 kN clamping force [TYPICAL]",
        "tools": ["Torx T30 Bit", "13mm Wrench", "12V Bench PSU"],
        "interfaces": "Torx spline output drive shaft, 2-bolt caliper mounting ears, 2-pin sealed connector",
        "hazards": "High clamping force can crush fingers; motor stall current reaches 15A–20A during full lockup",
        "blueprints": [20]
    },
    "ac_clutch_compressor": {
        "diff": "Intermediate",
        "specs": "12V electromagnetic friction clutch (40W coil, 45 N*m hold), multi-piston swashplate compressor [TYPICAL]",
        "tools": ["Snap Ring Pliers", "Clutch Spanner Tool", "A/C Manifold Gauges", "Metric Sockets"],
        "interfaces": "6-rib serpentine pulley with electromagnetic clutch hub, 4-bolt engine bracket mount",
        "hazards": "Pressurized R134a refrigerant venting hazard; clutch snap-engagement pinch hazard",
        "blueprints": [25]
    },
    "auto_seat_actuator": {
        "diff": "Novice",
        "specs": "12V DC compact worm gearmotor with flexible drive cable output, 150–300 RPM, high back-drive resistance [TYPICAL]",
        "tools": ["Torx T20 & T25 Bits", "Phillips Screwdriver", "Wire Cutters"],
        "interfaces": "Square-drive speedometer-style flexible drive cable socket, plastic snap-in bracket",
        "hazards": "Mechanical pinch hazard in scissor linkages; stripping plastic drive gears if stalled",
        "blueprints": [24]
    },
    "marine_trim_tilt_pump": {
        "diff": "Intermediate",
        "specs": "12V DC reversible PMDC motor, bi-directional gear pump, 2,500 PSI, integrated pilot check valves [TYPICAL]",
        "tools": ["Flare Wrenches", "Hex Sockets", "DMM", "Fluid Drain Pan"],
        "interfaces": "1/8\" NPT / flared hydraulic ports, hard-chromed stainless piston rod, 2-wire high-current harness",
        "hazards": "High-pressure hydraulic oil injection; galvanic corrosion seizing aluminum casing bolts",
        "blueprints": [20]
    },
    "aircraft_starter_generator": {
        "diff": "Master",
        "specs": "28V DC shunt-wound generator, 200A–300A (6 kW–9 kW continuous), 6,000–10,000 RPM, weight < 18 kg [TYPICAL]",
        "tools": ["Spline Coupler Adapter", "Heavy Torque Wrench", "Megohmmeter", "Force-Air Cooling Duct"],
        "interfaces": "Involute splined drive shaft, 6-bolt QAD (Quick Attach/Detach) flange, high-current copper terminal lugs",
        "hazards": "Extreme rotational kinetic energy; commutator thermal saturation if started > 30s; 400A short circuit arc flash",
        "blueprints": [11, 28]
    },

    # CONSUMER ELECTRONICS & OPTICS
    "printer_scanner": {
        "diff": "Novice",
        "specs": "NEMA 14/17 bipolar stepping motors, 8mm precision ground steel guide rods, linear optical encoder strips [TYPICAL]",
        "tools": ["Phillips #1 & #2 Screwdrivers", "Small Flat Screwdriver", "Flush Cutters"],
        "interfaces": "GT2/2mm pitch timing belts, 4-pin JST stepper headers, linear brass/polymer guide bushings",
        "hazards": "Sharp sheet metal chassis edges; eye strain from optical sensor alignment lasers",
        "blueprints": [6, 18]
    },
    "optical_drives": {
        "diff": "Novice",
        "specs": "Dual linear stepper axes with leadscrews (0.02mm resolution), 650nm Red & 405nm Violet laser diodes [TYPICAL]",
        "tools": ["Precision Screwdriver Set (#00, #0)", "Tweezers", "Soldering Iron with Fine Tip"],
        "interfaces": "M3x0.5 fine-pitch leadscrew, 4-pin micro-stepper FPC cable, 3-pin laser diode TO-18 can",
        "hazards": "CLASS 3B / CLASS 4 LASER RADIATION: Invisible or focused beam causes instant irreversible retinal blindness [VERIFIED]",
        "blueprints": [3, 6]
    },
    "hard_drive": {
        "diff": "Novice",
        "specs": "Ultra-fast voice coil rotary actuator (sub-millisecond response), N52 curved neodymium magnets, FDB spindle [TYPICAL]",
        "tools": ["Torx T6 & T8 Screwdrivers", "Plastic Wedge Tool", "Razor Blade"],
        "interfaces": "2-pin voice coil solder pads, mirror-polished aluminum/glass platter disks, 3-phase slotless spindle pads",
        "hazards": "Extreme neodymium magnet pinch hazard (can pinch blood blisters or shatter brittle sintered NdFeB)",
        "blueprints": [3]
    },
    "digital_calipers": {
        "diff": "Novice",
        "specs": "Capacitive linear quadrature scale (10 um resolution), 1.5V button cell power, serial sync/data port [TYPICAL]",
        "tools": ["Micro Eyeglass Screwdriver", "Soldering Iron", "Oscilloscope / Logic Analyzer"],
        "interfaces": "Printed PCB capacitive stator tracks, 4-pad gold synchronous serial debug header",
        "hazards": "Static ESD destruction of high-impedance CMOS interpolation ASIC; brittle LCD glass",
        "blueprints": [18]
    },
    "flatbed_scanner": {
        "diff": "Novice",
        "specs": "High-density linear CCD/CIS sensor (2,048–10,680 pixels), front-surface optical float glass mirrors, cold cathode lamp [TYPICAL]",
        "tools": ["Phillips Screwdriver", "ESD Grounding Strap", "Non-Magnetic Tweezers"],
        "interfaces": "Long flat flex cable (FFC), front-surface aluminum mirror brackets, ground steel guide rod",
        "hazards": "Mercury vapor inhalation hazard if CCFL tube is broken; fragile front-surface mirror coating easily scratched",
        "blueprints": [6, 18]
    },
    "laser_printer_polygon": {
        "diff": "Intermediate",
        "specs": "Ultra-high-speed slotless 3-phase BLDC motor spinning polygonal mirror at 25,000–45,000 RPM [TYPICAL]",
        "tools": ["Torx Screwdrivers", "Variable DC Power Supply", "Oscilloscope"],
        "interfaces": "Gold/aluminum coated multi-facet rotating polygonal prism, 5-pin driver header (Vcc, GND, CLK, Start, Lock)",
        "hazards": "Extreme rotational speed; mirror facet detachment hazard if spinning unbalanced; Class 3B laser diode",
        "blueprints": [3]
    },
    "audiophile_turntable": {
        "diff": "Intermediate",
        "specs": "Direct-drive multi-pole flat brushless motor, quartz-locked PLL feedback, zero-cogging precision bearing [TYPICAL]",
        "tools": ["Metric Hex Keys", "Slot Screwdrivers", "Stroboscopic Light Probe"],
        "interfaces": "Tapered brass spindle hub, cast aluminum platter with stroboscopic rim markings, Hall commutation PCB",
        "hazards": "Mains voltage exposure during bench testing; damaging high-precision spindle thrust sapphire bearing",
        "blueprints": [22]
    },
    "vending_bill_acceptor": {
        "diff": "Novice",
        "specs": "Multi-spectral optical validation array (UV, IR, Red, Green), motorized rubber drive rollers, optical interrupt sensors [TYPICAL]",
        "tools": ["Phillips #1 Screwdriver", "Wire Cutters", "DMM"],
        "interfaces": "MDB / Pulse interface harness, 12V/24V DC power input, removable cash cassette chassis",
        "hazards": "Mechanical roller pinch points; optical sensor misalignment if cleaned with harsh chemical solvents",
        "blueprints": [8]
    },
    "slr_shutter_curtain": {
        "diff": "Advanced",
        "specs": "High-precision mechanical escapement gear train, carbon fiber / titanium shutter blades, micro-solenoids (1/8000s speed) [TYPICAL]",
        "tools": ["Watchmaker Screwdriver Set", "00-ESD Tweezers", "Jeweler Loupe (10x)"],
        "interfaces": "Micro-gear train pivots, hairspring tension adjusters, miniature electromagnetic release coils",
        "hazards": "Spring-loaded escapement explosive disassembly; loss of micro-springs and jewel bearings",
        "blueprints": [18]
    },
    "linear_glass_scale": {
        "diff": "Advanced",
        "specs": "Photolithographic chrome-on-glass optical grating (20 um pitch), RS-422 differential quadrature output (0.1 um to 1 um) [TYPICAL]",
        "tools": ["Hex Keys (2.5mm, 3mm)", "Non-Magnetic Screwdrivers", "Digital Storage Oscilloscope"],
        "interfaces": "Extruded aluminum scale spar with rubber sealing lips, 9-pin D-sub or round DIN industrial connector",
        "hazards": "Brittle glass spar fracturing under bending torque; permanent optical destruction if grating face is touched",
        "blueprints": [18]
    },
    "barcode_scanner": {
        "diff": "Novice",
        "specs": "High-speed oscillating galvanometer mirror or multi-line rotating polygon, visible 650nm laser diode [TYPICAL]",
        "tools": ["Torx T10 Bit", "Precision Screwdrivers", "Multimeter"],
        "interfaces": "USB / RS-232 serial cable, wide-angle scan window, internal photodiode receiver stage",
        "hazards": "Laser beam eye hazard; micro-flexure fatigue failure if driven outside resonant frequency",
        "blueprints": [3]
    },
    "fax_thermal_head": {
        "diff": "Novice",
        "specs": "High-density thick-film resistive heating element array (200–300 DPI, 8 dots/mm), integrated shift register [TYPICAL]",
        "tools": ["Phillips Screwdriver", "Logic Analyzer", "DC Bench PSU"],
        "interfaces": "Gold card-edge or FPC data connector, heavy aluminum heatsink bar, 24V high-current power rails",
        "hazards": "Thermal burn hazard; static ESD damage to CMOS shift register circuitry",
        "blueprints": [6]
    },

    # MOBILITY & POWER TOOLS
    "hoverboard": {
        "diff": "Intermediate",
        "specs": "Dual 350W 36V 30-pole brushless hub motors, 30–40 N*m stall torque, 36V 4.4Ah 18650 Li-ion battery pack [TYPICAL]",
        "tools": ["Phillips #2 Screwdriver", "14mm & 17mm Wrenches", "Heat Shrink Tubing", "Soldering Iron"],
        "interfaces": "Solid 16mm flatted axle shaft with M14 threads, 3 heavy phase wires + 5-pin Hall sensor harness",
        "hazards": "EXTREME FIRE HAZARD: Damaged or shorted 36V 18650 lithium packs undergo violent self-sustaining thermal runaway [VERIFIED]",
        "blueprints": [8, 38]
    },
    "cordless_drills": {
        "diff": "Novice",
        "specs": "18V–20V high-torque brushed or brushless motor, 2-speed all-metal epicyclic planetary gearbox (15:1 to 50:1) [TYPICAL]",
        "tools": ["Left-Hand Thread Chuck Screw Torx Bit", "Hex Key for Chuck Removal", "Phillips Screwdriver"],
        "interfaces": "1/2\"-20 UNF threaded output spindle, 3-jaw Jacobs chuck, 4-bolt motor face flange",
        "hazards": "Violent rotational wrist torque kickback if drill chuck seizes under heavy load; reverse-thread screw breakage",
        "blueprints": [23]
    },
    "dyson_vacuum": {
        "diff": "Intermediate",
        "specs": "100,000–125,000 RPM slotless digital BLDC turbine motor, precision CNC dynamic balanced aluminum impeller, 350W–500W [TYPICAL]",
        "tools": ["Torx T8 & T10 Long-Shank Security Drivers", "Plastic Spudger", "High-Frequency BLDC ESC"],
        "interfaces": "Compact cylindrical aluminum motor housing, 3-wire UVW solder pads, aerodynamic flow straighteners",
        "hazards": "Catastrophic centrifugal impeller shrapnel burst if driven past rated speed or if foreign debris strikes blades [VERIFIED]",
        "blueprints": [15, 23]
    },
    "cpap_blower": {
        "diff": "Novice",
        "specs": "Ultra-quiet miniature 3-phase BLDC centrifugal blower, 24V DC, 35,000–50,000 RPM, sealed silicone vibration cradle [TYPICAL]",
        "tools": ["Torx T10 Screwdriver", "Hobby Brushless ESC", "Multimeter"],
        "interfaces": "22mm standard medical tapered breathing tube port, 3-pin motor phase harness with Hall sensors",
        "hazards": "Bearing seizure if operated in dusty workshop environments without fine inlet HEPA filtering",
        "blueprints": [15]
    },
    "escooter_hub": {
        "diff": "Intermediate",
        "specs": "36V–48V 350W–500W brushless hub motor, integrated drum or disc brake mount, 10\" pneumatic tire [TYPICAL]",
        "tools": ["18mm Axle Nut Wrench", "Tire Levers", "Hex Sockets (4mm, 5mm)"],
        "interfaces": "Dual 12mm flatted axle with torque washers, 6-bolt ISO brake rotor flange, waterproof 9-pin Julet motor cable",
        "hazards": "Pinch hazard during tire demounting; electrical shock from regenerative back-EMF if spun rapidly by hand",
        "blueprints": [8, 38]
    },
    "angle_grinder": {
        "diff": "Intermediate",
        "specs": "120V/240V AC 15A series universal motor, 8,500–11,000 RPM spindle speed, spiral bevel right-angle gearbox [TYPICAL]",
        "tools": ["Spanner Pin Wrench", "Impact Driver", "Snap Ring Pliers", "Gear Puller"],
        "interfaces": "5/8\"-11 UNC threaded arbor spindle, cast aluminum gearcase with 4-bolt face mount",
        "hazards": "Abrasive disc disintegration at 10,000 RPM produces lethal flying shrapnel [VERIFIED]; high gyro precession forces",
        "blueprints": [4, 48]
    },
    "chainsaw_engine": {
        "diff": "Intermediate",
        "specs": "45cc–55cc 2-stroke single-cylinder air-cooled gasoline engine, 2.5–3.5 HP @ 9,000–12,000 RPM, centrifugal clutch [TYPICAL]",
        "tools": ["Spark Plug Deep Socket", "T27 Torx Driver", "Clutch Removal Tool", "Carburetor Adjustment Screwdriver"],
        "interfaces": "Tapered keyed crankshaft with centrifugal clutch drum, sprocket rim, Walbro diaphragm carburetor",
        "hazards": "Extreme fire hazard from gasoline fumes; high vibration loosening fasteners; hot exhaust muffler burns",
        "blueprints": [34]
    },
    "wheelchair_motor": {
        "diff": "Intermediate",
        "specs": "24V DC 250W–450W heavy-duty brushed gearmotor, right-angle worm reducer, integrated 24V spring-applied failsafe brake [TYPICAL]",
        "tools": ["13mm, 15mm, 17mm Sockets", "Hex Keys", "DMM", "Soldering Torch"],
        "interfaces": "Heavy keyed output hub with 4-bolt wheel pattern, 2-pin motor leads + 2-pin brake release leads",
        "hazards": "Motor shaft is mechanically locked until 24V DC is applied to electromagnetic brake coil [VERIFIED]",
        "blueprints": [8, 25]
    },
    "rotary_hammer": {
        "diff": "Advanced",
        "specs": "800W–1,200W universal motor with pneumatic striker piston mechanism, SDS-Plus chuck, 3.0 Joules impact energy [TYPICAL]",
        "tools": ["Torx Drivers", "Circlip Pliers", "Solvent Wash Tank", "High-Pressure Grease Gun"],
        "interfaces": "SDS-Plus spring-loaded locking ball chuck, mode selector dial (Drill, Hammer-Drill, Chisel)",
        "hazards": "Pneumatic striker piston spring explosion during gearcase opening; extreme recoil shock loads",
        "blueprints": [34]
    },
    "cordless_chainsaw": {
        "diff": "Intermediate",
        "specs": "40V–60V DC high-torque brushless outrunner motor, 1.5 kW–2.5 kW peak power, automatic oiler pump [TYPICAL]",
        "tools": ["Screwdriver Set", "Socket Set", "DMM", "BLDC Test ESC"],
        "interfaces": "Direct drive sprocket shaft, heavy-gauge 3-phase silicone phase leads, tool-less chain tensioner cam",
        "hazards": "High DC voltage (> 50V) on battery contacts; rapid blade acceleration with zero warm-up warning",
        "blueprints": [38]
    },
    "rc_lipo_brushless": {
        "diff": "Novice",
        "specs": "High-Kv brushless outrunner motor, 1,000W–3,000W power density, 11.1V–22.2V (3S–6S LiPo), 15,000+ RPM [TYPICAL]",
        "tools": ["Hex Drivers (1.5mm, 2.0mm, 2.5mm)", "Bullet Connector Crimpers", "Optical Tachometer"],
        "interfaces": "4-hole rear cross mount (16x19mm or 25x25mm), 3.17mm / 5mm ground shaft with collet prop adapter",
        "hazards": "Propeller blade laceration hazard; severe stator overheating if operated without adequate rotor airflow",
        "blueprints": [23]
    },
    "electric_lawnmower": {
        "diff": "Novice",
        "specs": "120V AC 12A universal/induction motor or 40V-80V cordless brushless motor, 3,200 RPM direct drive blade [TYPICAL]",
        "tools": ["14mm & 15mm Deep Sockets", "Deadblow Hammer", "Multimeter"],
        "interfaces": "Flanged blade adapter with dual shear pins, 4-bolt deck mount, heavy safety deadman switch bar",
        "hazards": "Heavy rotating blade inertia; sudden motor braking current surges during emergency shut-off",
        "blueprints": [48]
    },
    "hospital_bed_actuator": {
        "diff": "Intermediate",
        "specs": "24V DC PM worm gearmotor, acme leadscrew (4,000N - 6,000N thrust [TYPICAL]), 5-15 mm/s travel speed",
        "tools": ["Hex Bit Sockets", "Snap Ring Pliers", "DMM", "24V Bench PSU"],
        "interfaces": "10mm/12mm clevis pin mounting holes at both ends, 4-pin DIN / molex connector with limit switch lines",
        "hazards": "Extreme mechanical pinch and crushing force; stripping internal nylon shear gears if back-driven violently",
        "blueprints": [20, 24]
    },

    # FRONTIER LAB & EXOTIC SCRAP
    "dlp_projector": {
        "diff": "Advanced",
        "specs": "Texas Instruments Digital Micromirror Device (DMD - 1920x1080 array), TIR prism, high-radiance RGB LEDs [TYPICAL]",
        "tools": ["Precision Phillips #00", "Torx T6 & T8 Bits", "ESD Grounded Tweezers", "Lens Tissue"],
        "interfaces": "High-density multi-pin LGA socket for DMD chip, HDMI video input board, telecentric projection optics",
        "hazards": "Intense UV/blue light radiation damaging eyes; high-voltage ballast (300V+) if using mercury arc bulb model",
        "blueprints": [9]
    },
    "dental_scaler": {
        "diff": "Intermediate",
        "specs": "High-power Langevin piezoelectric transducer, 28 kHz–32 kHz resonant frequency, 30W–50W acoustic power [TYPICAL]",
        "tools": ["Wrench for Scaler Tip", "Oscilloscope", "Signal Generator", "Ultrasonic Power Meter"],
        "interfaces": "Internal axial fluid cooling tube, M3 fine-threaded acoustic horn stud, 2-pin shielded drive cable",
        "hazards": "Lethal high-frequency RF drive voltage (200V–500V peak-to-peak); acoustic cavitation burns if touched while resonant",
        "blueprints": [10]
    },
    "espresso_machine": {
        "diff": "Intermediate",
        "specs": "Ulka vibrating solenoid piston pump (120V 41W, 15 bar peak pressure), brass thermal block with capillary thermostat [TYPICAL]",
        "tools": ["Metric Wrenches (10mm, 12mm, 14mm)", "Flare Nut Wrench", "Multimeter"],
        "interfaces": "1/8\" BSPP threaded brass outlet, silicone suction tube, 2-pin spade lugs for solenoid coil",
        "hazards": "Superheated steam and scalding water spray; high internal pump pressure (up to 200 PSI); limescale clogging",
        "blueprints": [12]
    },
    "medical_o2": {
        "diff": "Advanced",
        "specs": "Dual molecular sieve zeolite canisters, Thomas oil-free rocking piston compressor (120V 350W, 35 PSI) [TYPICAL]",
        "tools": ["Hose Clamp Pliers", "Torx Screwdrivers", "Oxygen Analyzer", "Adjustable Wrench"],
        "interfaces": "1/4\" brass pneumatic fittings, 4-way pilot-operated rotary distributor valve, pressure relief manifold",
        "hazards": "FIRE HAZARD: Concentrated oxygen gas (> 93% O2) dramatically accelerates combustion of grease, oil, and cloth [VERIFIED]",
        "blueprints": [16]
    },
    "supercaps": {
        "diff": "Intermediate",
        "specs": "Maxwell 2.7V 3,000F ultracapacitor cells, internal ESR < 0.3 milliohms, short-circuit current > 2,000A [TYPICAL]",
        "tools": ["Insulated Socket Wrench", "Heavy 50W Discharge Resistor", "Digital Multimeter"],
        "interfaces": "M16 threaded aluminum terminal posts, laser-welded busbars, active cell-balancing PCB tabs",
        "hazards": "EXPLOSIVE ARC FLASH: 3,000A short-circuit current vaporizes copper wire and welds hand tools instantly [VERIFIED]",
        "blueprints": [19]
    },
    "espresso_procon": {
        "diff": "Intermediate",
        "specs": "Procon brass/stainless positive displacement rotary vane pump, 100–250 L/hr @ 10–14 bar (150–200 PSI) [TYPICAL]",
        "tools": ["V-Band Clamp Pliers", "Adjustable Wrench", "Flat Screwdriver", "Thread Sealant"],
        "interfaces": "3/8\" NPT female fluid ports, double-flat slotted bronze drive tang, circular V-band motor mounting clamp",
        "hazards": "Fluid cavitation and graphite vane shattering if operated completely dry for > 10 seconds",
        "blueprints": [34]
    },
    "dishwasher_peristaltic": {
        "diff": "Novice",
        "specs": "Multi-roller peristaltic chemical metering pump, 24V DC / 120V AC geared motor, 10–100 mL/min self-priming [TYPICAL]",
        "tools": ["Phillips Screwdriver", "Tubing Cutters", "DMM"],
        "interfaces": "Santoprene / Norprene flexible elastomer tubing, barbed quick-connect inlet/outlet ports",
        "hazards": "Corrosive detergent chemical residue (concentrated sodium hydroxide); wear chemical splash goggles",
        "blueprints": [31]
    },
    "ev_scroll_compressor": {
        "diff": "Master",
        "specs": "Hermetic 3-phase high-voltage BLDC scroll compressor, 200V–400V DC input, integrated high-voltage inverter [TYPICAL]",
        "tools": ["High-Voltage Insulated Gloves (Class 0, 1000V)", "HV Multimeter Probes", "Torx Sockets"],
        "interfaces": "High-voltage orange shielded power cable connector, aluminum A/C flange blocks with HNBR O-rings",
        "hazards": "LETHAL 400V DC TRACTION BUS VOLTAGE: Requires verified capacitor bank discharge before touching internal terminals [VERIFIED]",
        "blueprints": [7]
    },
    "mass_spectrometer_turbo": {
        "diff": "Master",
        "specs": "Turbomolecular high-vacuum pump, 60,000–90,000 RPM magnetic/ceramic bearings, ultimate vacuum < 10^-8 mbar [TYPICAL]",
        "tools": ["Cleanroom Nitrile Gloves", "ConFlat (CF) Flange Wrenches", "Dedicated Turbo Driver Controller"],
        "interfaces": "CF or ISO-K stainless vacuum flange, multi-pin Fischer/Amphenol motor connector, foreline exhaust port",
        "hazards": "Catastrophic rotor explosion if exposed to sudden atmospheric venting while spinning at 90,000 RPM [VERIFIED]",
        "blueprints": [15, 23]
    },
    "gas_meter": {
        "diff": "Novice",
        "specs": "Positive displacement bellows diaphragm / nutating disc mechanism, magnetic drive coupling, reed pulse output [TYPICAL]",
        "tools": ["Pipe Wrenches", "Slot Screwdrivers", "Multimeter"],
        "interfaces": "Heavy cast iron/aluminum body, threaded gas spud unions, magnetic index drive face",
        "hazards": "Mercaptan chemical odor residue; trapped residual combustible gas inside bellows chambers",
        "blueprints": [21]
    },
    "defibrillator_aed": {
        "diff": "Master",
        "specs": "Biphasic truncated exponential pulse capacitor (150–360 Joules @ 1,500V–2,200V DC), high-speed IGBT H-bridge [TYPICAL]",
        "tools": ["1000V Insulated Screwdrivers", "Ceramic Wirewound Bleeder Resistor", "Safety Face Shield"],
        "interfaces": "High-voltage paddle/pad connectors, optical isolation barrier, high-current busbar tracks",
        "hazards": "FATAL ELECTRIC SHOCK HAZARD: Delivers 2,000V high-energy cardiac discharge instantly; verify zero voltage with HV probe [VERIFIED]",
        "blueprints": [19]
    },
    "laser_cavity_nd_yag": {
        "diff": "Master",
        "specs": "Solid-state Nd:YAG laser crystal rod (1064nm infrared), krypton/xenon flashlamp, gold-plated elliptical cavity [TYPICAL]",
        "tools": ["Laser Safety Goggles (OD 7+ @ 1064nm)", "Non-Magnetic Hex Keys", "Dielectric Mirror Mounts"],
        "interfaces": "Deionized water cooling jacket barbs, high-voltage flashlamp trigger electrodes (15 kV trigger, 1 kV pulse)",
        "hazards": "CLASS 4 INVISIBLE INFRARED LASER: 1064nm beam causes instant, permanent retinal burn and blindness [VERIFIED]",
        "blueprints": [9]
    },
    "piezo_nanostage": {
        "diff": "Advanced",
        "specs": "Monolithic EDM wire-cut flexure guide, low-voltage PZT piezo stack actuator (0–100V DC), sub-nanometer resolution [TYPICAL]",
        "tools": ["Micro-Torx Drivers", "Precision Low-Noise High-Voltage Op-Amp", "Interferometer"],
        "interfaces": "High-precision tapped metric mounting pattern (M2/M3), high-voltage LEMO / BNC connector, capacitive sensor pins",
        "hazards": "Brittle PZT ceramic fracturing under shear or tensile stress; pyroelectric high-voltage shock under thermal change",
        "blueprints": [18]
    },
    "spectrophotometer": {
        "diff": "Intermediate",
        "specs": "Czerny-Turner optical monochromator, 1200 lines/mm blazed diffraction grating, deuterium & halogen lamp housing [TYPICAL]",
        "tools": ["Optical Tweezers", "Non-Magnetic Screwdrivers", "Spectral Lamp Calibration Source"],
        "interfaces": "Optical bench rail mounts, quartz cuvette holder stage, stepper sine-bar wavelength drive mechanism",
        "hazards": "DO NOT TOUCH GRATING SURFACE: Touching or wiping ruins micro-grooves permanently; UV-C photokeratitis from D2 lamp",
        "blueprints": [9]
    },
    "blood_centrifuge": {
        "diff": "Intermediate",
        "specs": "High-speed brushless induction/BLDC motor, 10,000–15,000 RPM, forged aluminum aerodynamic tube rotor [TYPICAL]",
        "tools": ["Rotor Locking Nut Wrench", "Allen Keys", "Tachometer Probe"],
        "interfaces": "Tapered motor shaft with keyed rotor locking nut, motorized lid latch safety interlock switch",
        "hazards": "Biohazard blood aerosol contamination; violent rotor disintegration if operated unbalanced",
        "blueprints": [23]
    },
    "triplex_pressure_washer": {
        "diff": "Intermediate",
        "specs": "Triplex reciprocating plunger pump with solid ceramic plungers, 2,500–4,000 PSI @ 3–4 GPM [TYPICAL]",
        "tools": ["Metric Sockets (14mm, 17mm, 19mm)", "Unloader Valve Spanner", "Pressure Gauge"],
        "interfaces": "3/4\" or 1\" keyed shaft for engine/motor coupling, 3/8\" high-pressure quick-connect outlet, 3/4\" garden hose inlet",
        "hazards": "HIGH-PRESSURE INJECTION: Water jet at 3,000 PSI penetrates human flesh instantly requiring surgical debridement [VERIFIED]",
        "blueprints": [34, 50]
    },
    "infusion_pump_peristaltic": {
        "diff": "Intermediate",
        "specs": "NEMA 14/17 stepper motor with 10:1 planetary gearbox, 4-roller cam peristaltic head (0.1 - 999 mL/hr [TYPICAL])",
        "tools": ["Precision Screwdrivers", "DMM", "Oscilloscope", "Tubing Strippers"],
        "interfaces": "Drop-in silicone cassette carrier, optical bubble sensor channel, piezoresistive pressure strain bridge",
        "hazards": "Residual bio-fluid chemical contamination; ensure full bleach washdown before mechanical extraction",
        "blueprints": [31]
    },
    "copeland_scroll_compressor": {
        "diff": "Advanced",
        "specs": "Matched precision cast-iron involute scroll set (100% volumetric efficiency [TYPICAL]), 3-phase hermetic motor",
        "tools": ["Tubing Cutter", "Angle Grinder to slice can", "Refrigerant Gauge Set", "500V Megohmmeter"],
        "interfaces": "Suction/discharge welded copper stubs, 3-pin hermetic terminal cluster, internal eccentric drive spindle",
        "hazards": "Pressurized fluorocarbon refrigerant (EPA Section 608 violation); 240V/480V 3-phase mains voltage",
        "blueprints": [7, 47]
    },
    "autoclave_sterilizer": {
        "diff": "Advanced",
        "specs": "ASME 316L seamless stainless pressure vessel, 1,400W-2,200W heating elements, 134°C @ 30 PSI [TYPICAL]",
        "tools": ["Pipe Wrenches", "Socket Set", "DMM", "Hydrostatic Water Test Pump"],
        "interfaces": "Threaded pipe bungs (1/4\", 1/2\" NPT), heavy silicone door gasket ring, certified ASME 35 PSI safety relief valve",
        "hazards": "SUPERHEATED STEAM: Escaping steam causes severe deep-tissue thermal burns; explosion risk if safety relief valve is modified",
        "blueprints": [21, 50]
    },

    # KINEMATICS & TRANSMISSIONS
    "belimo_actuator": {
        "diff": "Novice",
        "specs": "24V AC/DC spring-return damper actuator, 10–20 N*m torque, brushless DC motor with planetary gear train [TYPICAL]",
        "tools": ["10mm Wrench", "Flat Screwdriver", "Multimeter"],
        "interfaces": "Universal V-bolt shaft clamp (accepts 3/8\" to 1\" round or hex shafts), auxiliary microswitch cams",
        "hazards": "High spring-loaded mechanical energy stored in clockwork return spring; sudden uncoiling if casing is split",
        "blueprints": [24, 30]
    },
    "leblanc_ring": {
        "diff": "Novice",
        "specs": "Toroidal annular plastic balancing ring containing precision steel balls submerged in silicone viscous fluid [TYPICAL]",
        "tools": ["Socket Set", "Flat Screwdriver", "Deadblow Hammer"],
        "interfaces": "Front-lip snap-fit mounting groove on washing machine drum, balanced concentric alignment track",
        "hazards": "Slicing open ring spills high-viscosity silicone damping oil; steel balls produce slipping hazard",
        "blueprints": [27]
    },
    "geneva_indexer": {
        "diff": "Intermediate",
        "specs": "4-slot or 6-slot Maltese cross Geneva intermittent mechanism, converts constant rotation into locked indexing steps [TYPICAL]",
        "tools": ["Allen Keys", "Gear Puller", "Feeler Gauges", "Machinist Stone"],
        "interfaces": "Precision ground input pin shaft and output cross shaft, matched center distance mounting plate",
        "hazards": "Extreme mechanical pinch hazard at pin entry slot; mechanical shock loading if driven at > 300 RPM",
        "blueprints": [26]
    },
    "sewing_thread_traverse": {
        "diff": "Intermediate",
        "specs": "Cylindrical cross-helical barrel cam with diamond ceramic thread eyelet guide, bi-directional reciprocating stroke [TYPICAL]",
        "tools": ["Metric Hex Keys", "Snap Ring Pliers", "Bearing Puller"],
        "interfaces": "Precision hardened barrel cam shaft with helical grooves, sliding follower shuttle block",
        "hazards": "Follower binding or shattering if operated without continuous lubrication; pinch hazard in shuttle path",
        "blueprints": [26]
    },
    "scotch_yoke": {
        "diff": "Intermediate",
        "specs": "Pure simple harmonic motion linear scotch yoke mechanism, converts rotary crank into exact sinusoidal translation [TYPICAL]",
        "tools": ["Socket Set", "Machinist Square", "Dial Test Indicator", "Feeler Gauges"],
        "interfaces": "Hardened 4140 steel slotted yoke bracket, bronze sliding block with needle roller pin bearing",
        "hazards": "Heavy reciprocating inertia forces; mechanical pinch between slider block and yoke slot walls",
        "blueprints": [26]
    },
    "cycloidal_reducer": {
        "diff": "Advanced",
        "specs": "Nabtesco / Sumitomo cycloidal speed reducer, 29:1 to 119:1 single-stage ratio, zero backlash (< 1 arcmin) [TYPICAL]",
        "tools": ["Metric Allen Sockets", "Torque Wrench", "Bearing Puller", "Clean Bench Setup"],
        "interfaces": "Input eccentric camshaft, dual 180-degree opposed cycloidal disc lobes, ring pin housing with needle rollers",
        "hazards": "Incorrect disc phasing (discs MUST be assembled 180 degrees out of phase or unit locks completely) [VERIFIED]",
        "blueprints": [23]
    },
    "harmonic_drive": {
        "diff": "Advanced",
        "specs": "Strain-wave gear reducer (Flexspline, Circular Spline, Wave Generator), 50:1 to 160:1 ratio, zero backlash [TYPICAL]",
        "tools": ["Watchmaker Hex Keys", "Torque Screwdriver", "Non-Magnetic Tweezers"],
        "interfaces": "Thin-wall flexible cup (Flexspline), internal elliptical bearing plug, rigid internal tooth outer ring",
        "hazards": "Extreme fragility of thin-wall alloy Flexspline: bending or denting permanently destroys gear mesh [VERIFIED]",
        "blueprints": [22, 23]
    },
    "overrunning_clutch": {
        "diff": "Intermediate",
        "specs": "Sprag / roller ramp one-way overrunning freewheel clutch, 100% instantaneous lockup in drive direction [TYPICAL]",
        "tools": ["Bearing Press", "External Circlip Pliers", "Micrometer"],
        "interfaces": "Precision ground inner and outer steel bearing races, keyway or press-fit outer sleeve",
        "hazards": "Installing backwards causes freewheeling in drive direction and complete lockup under reverse load",
        "blueprints": [49]
    },
    "commercial_vav_air_damper": {
        "diff": "Novice",
        "specs": "Extruded aluminum aerodynamic airfoil blades with molded silicone seals, counter-rotating Delrin gears [TYPICAL]",
        "tools": ["Nut Drivers", "Allen Keys", "Pliers"],
        "interfaces": "0.5\" hex drive shafts, celcon low-friction bushings, intermeshing opposed blade gear train",
        "hazards": "Mechanical finger pinch hazard in intermeshing gear train; fiberglass duct insulation contact",
        "blueprints": [24, 30]
    },

    # WORKSHOP FABRICATION & HEAVY SALVAGE
    "industrial_sewing": {
        "diff": "Intermediate",
        "specs": "3/4 HP to 1.0 HP clutch motor or brushless AC servo drive, 3,500–5,000 RPM, needle positioning synchronizer [TYPICAL]",
        "tools": ["Metric Sockets (10mm, 13mm, 17mm)", "Large Flat Screwdriver", "DMM"],
        "interfaces": "Heavy cast-iron under-table mount, 3-groove V-belt pulley, optical needle-up/needle-down sync hub",
        "hazards": "Heavy cast iron motor (> 15 kg); clutch drag causing sudden unexpected belt acceleration",
        "blueprints": [25, 48]
    },
    "server_psu": {
        "diff": "Novice",
        "specs": "12V DC 60A–100A (750W–1,200W) 80-Plus Platinum switchmode power supply, active PFC, 94% efficiency [TYPICAL]",
        "tools": ["Soldering Iron", "1k-ohm 1/4W Resistor (for jumpering PS_ON to GND)", "Multimeter"],
        "interfaces": "Gold-plated card edge power fingers (12V bus bars + 12-pin control pad block)",
        "hazards": "Shorting 100A output bus produces violent molten copper splatter; loud high-RPM cooling fan",
        "blueprints": [2, 5]
    },
    "sewing_servo": {
        "diff": "Novice",
        "specs": "550W–750W direct-drive brushless AC servo motor, 500–4,500 RPM adjustable, high torque from standstill [TYPICAL]",
        "tools": ["Hex Keys", "Open-End Wrenches", "Digital Multimeter"],
        "interfaces": "Standard 3-bolt sewing machine under-bench bracket, optical synchronizer cable, analog treadle speed arm",
        "hazards": "High acceleration torque; sudden rotation if foot treadle potentiometer linkage shifts",
        "blueprints": [4, 48]
    },
    "megohmmeter": {
        "diff": "Novice",
        "specs": "Generates 250V, 500V, or 1,000V DC test voltage to measure dielectric insulation resistance up to 2,000 M-ohms [TYPICAL]",
        "tools": ["Heavy-Duty Alligator Probes", "Hand Crank or Internal Battery Pack"],
        "interfaces": "Line, Earth, and Guard 4mm banana jacks, analog ballistic mirror scale or high-contrast LCD",
        "hazards": "Produces 1,000V DC electric shock hazard across test leads; charges capacitive motor windings [VERIFIED]",
        "blueprints": [11, 35]
    },
    "spot_welder_mot": {
        "diff": "Intermediate",
        "specs": "Rewound microwave transformer with 2 turns of 2/0 AWG welding cable, delivering 3.5V AC @ 800A–1,000A [CALCULATED]",
        "tools": ["Hacksaw / Dremel to remove HV coil", "2/0 Welding Cable", "Solid Copper TIG Rod Tips", "Pneumatic Clamps"],
        "interfaces": "Pneumatic or lever-actuated solid copper electrode arms, solid-state relay (SSR) AC mains trigger",
        "hazards": "Thermal burns from incandescent spot-weld nuggets; secondary leads heat up rapidly under cyclic duty",
        "blueprints": [5]
    },
    "electrolysis_tank": {
        "diff": "Novice",
        "specs": "Sacrificial steel rebar anodes, sodium carbonate (washing soda) electrolyte, 12V 10A–20A DC power supply [TYPICAL]",
        "tools": ["Plastic Rubbermaid Tank", "12V Battery Charger", "Steel Rebar", "Hydrometer"],
        "interfaces": "Submerged cathode clamp (part under de-rusting), parallel steel anode ring busbar",
        "hazards": "EXPLOSIVE HYDROGEN GAS: Produces stoichiometric H2 and O2 gas; operate exclusively in outdoor/ventilated space [VERIFIED]",
        "blueprints": [35]
    },
    "surface_plate_granite": {
        "diff": "Intermediate",
        "specs": "Grade 00 / Grade B black granite surface flat, lapped to < 0.002 mm flatness, zero thermal expansion [TYPICAL]",
        "tools": ["Precision India Oilstone", "Denatured Alcohol", "Cast Iron Lapping Plate", "Diamond Paste"],
        "interfaces": "3-point Airy / Bessel kinematic mounting support pads on bottom face",
        "hazards": "Crushing hazard due to massive deadweight (> 40 kg to 150 kg); brittle edge chipping if struck with steel tools",
        "blueprints": [18, 51]
    },
    "spark_testing_bench": {
        "diff": "Novice",
        "specs": "3,450 RPM clean vitrified aluminum oxide wheel, matte black viewing background, optical spark visor [TYPICAL]",
        "tools": ["60-Grit Grinding Wheel", "Wheel Dressing Tool", "Alloy Reference Coupons (1018, 4140, O1, HSS)"],
        "interfaces": "Heavy cast iron pedestal base, adjustable steel spark rest (1/8\" clearance to wheel)",
        "hazards": "Eye hazard from high-velocity incandescent metal sparks; never grind flammable magnesium alloys [VERIFIED]",
        "blueprints": [35]
    },
    "ebike_torque_bottom_bracket": {
        "diff": "Novice",
        "specs": "Magnetostrictive torque transducer on chromoly crank spindle, dual-channel quadrature cadence sensors (0.5V–2.5V out) [TYPICAL]",
        "tools": ["Splined Bottom Bracket Tool", "Crank Puller", "Multimeter", "5V Power Supply"],
        "interfaces": "Standard BSA 68mm/73mm threaded bottom bracket shell, square-taper or ISIS crank spindles, 4-pin cable",
        "hazards": "Sensor decalibration if excessive localized heat or welding ground current passes through bottom bracket spindle",
        "blueprints": [11]
    },
    "telecom_rectifier_shelf": {
        "diff": "Intermediate",
        "specs": "3,000W active PFC synchronous rectifier, -48V to 54V DC @ 50A-60A [TYPICAL], isolated CAN-bus interface",
        "tools": ["Torx Drivers", "Insulated Hand Tools", "DMM", "CAN-Bus Transceiver"],
        "interfaces": "Gold edge card power busbars, hot-swap lever lock, rear backplane blind-mate connector",
        "hazards": "240V AC mains input; high-current DC arc flash; stored charge in bulk primary filter caps",
        "blueprints": [19]
    },
    "forklift_hydraulic_valve": {
        "diff": "Intermediate",
        "specs": "Multi-spool ductile iron hydraulic valve block, 3,000 PSI rating, adjustable cartridge relief (1,500 - 3,200 PSI [TYPICAL])",
        "tools": ["Flare Wrenches", "Hex Sockets", "Clean Lint-Free Rags", "Pressure Gauge"],
        "interfaces": "SAE O-ring boss / JIC hydraulic ports, hardened chrome spools (clearance < 0.005mm), manual feathering levers",
        "hazards": "Ultra-high hydraulic pressure injection; trapped hydraulic accumulator pressure must be relieved before disassembly",
        "blueprints": [20, 50]
    },
    "three_phase_induction_motor": {
        "diff": "Intermediate",
        "specs": "5 HP to 10 HP 3-phase NEMA/IEC induction motor, dual-voltage (240V/480V), 1,750 RPM, 6205/6306 bearings [TYPICAL]",
        "tools": ["Crane / Hoist", "Socket Set", "1,000V Megohmmeter", "Phase Rotation Meter"],
        "interfaces": "1.125\" - 1.375\" keyed output shaft, 9-lead or 12-lead junction box, NEMA rigid base foot mount",
        "hazards": "High voltage 480V 3-phase; heavy crushing hazard during transport (> 50 kg)",
        "blueprints": [28, 48]
    },
    "robotic_welder_wire_feeder": {
        "diff": "Intermediate",
        "specs": "24V/42V DC planetary geared drive motor, 4-roll geared knurled steel mechanism (50-800 IPM [TYPICAL])",
        "tools": ["Hex Keys", "DMM", "24V Power Supply", "Screwdrivers"],
        "interfaces": "Euro-torch brass power/gas quick-disconnect block, 24V gas solenoid port, adjustable spring tension arms",
        "hazards": "Mechanical pinch in geared drive rollers; electrical shorts from high welding current if isolation washer is cracked",
        "blueprints": [24]
    }
}

def enrich_donors_in_encarta_data():
    with open(d.__file__, "r", encoding="utf-8") as f:
        content = f.read()

    # Iterate through all donors in DONORS_DATA and enrich
    updated_donors = []
    for donor in d.DONORS_DATA:
        donor_id = donor["id"]
        meta = ENRICHMENT_MAP.get(donor_id, {})
        
        # Build enriched donor object
        enr = {
            "id": donor["id"],
            "name": donor["name"],
            "cat": donor["cat"],
            "danger": donor.get("danger", "Moderate"),
            "dangerColor": donor.get("dangerColor", "#f59e0b"),
            "diff": meta.get("diff", "Intermediate"),
            "specs": meta.get("specs", "Standard electromechanical ratings [TYPICAL]"),
            "interfaces": meta.get("interfaces", "Standard shaft, flange, and wiring harness terminals"),
            "tools": meta.get("tools", ["Standard Screwdrivers", "Socket Set", "Digital Multimeter"]),
            "harvest": donor.get("harvest", []),
            "avoid": donor.get("avoid", "None reported"),
            "hazards": meta.get("hazards", f"Standard workshop hazards associated with {donor['name']}"),
            "bestFor": donor.get("bestFor", "Custom electromechanical projects"),
            "triage": donor.get("triage", "Bench test with DMM before deployment"),
            "blueprints": meta.get("blueprints", [])
        }
        updated_donors.append(enr)

    # Format into python code
    donor_code_lines = ["DONORS_DATA = ["]
    for enr in updated_donors:
        donor_code_lines.append("    {")
        for k in ["id", "name", "cat", "danger", "dangerColor", "diff", "specs", "interfaces", "tools", "harvest", "avoid", "hazards", "bestFor", "triage", "blueprints"]:
            v = enr[k]
            donor_code_lines.append(f'        "{k}": {json.dumps(v)},')
        donor_code_lines.append("    },")
    donor_code_lines.append("]")
    new_donors_code = "\n".join(donor_code_lines)

    # Replace in file
    start_idx = content.find("DONORS_DATA = [")
    end_idx = content.find("BLUEPRINTS_DATA = [", start_idx)
    # Find the closing bracket before BLUEPRINTS_DATA
    sub = content[start_idx:end_idx]
    last_bracket = sub.rfind("]")
    
    full_new_content = content[:start_idx] + new_donors_code + content[start_idx + last_bracket + 1:]

    with open(d.__file__, "w", encoding="utf-8") as f:
        f.write(full_new_content)

    print(f"[OK] Successfully enriched all {len(updated_donors)} donors in {d.__file__}!")

if __name__ == "__main__":
    enrich_donors_in_encarta_data()
