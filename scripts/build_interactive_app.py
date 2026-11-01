import os
import json
import html

WORKSPACE = r"C:\Users\karma\Desktop\REPURPOSE"
ARTIFACT_DIR = r"C:\Users\karma\.gemini\antigravity\brain\5e9a81ab-3e75-499e-94e7-7e11fb483cbb"

# Data definitions
CATEGORIES = [
    {"id": "auto", "name": "Automotive & Traction", "icon": "🚗", "desc": "Wipers, EPS Columns, Alternators, Starters, ABS Pumps, VVT Valves"},
    {"id": "consumer", "name": "Precision Optics & Office", "icon": "🖨️", "desc": "NEMA Steppers, Linear Rods, Caliper DROs, HDD Galvos, Turntables"},
    {"id": "domestic", "name": "Domestic Appliances", "icon": "🌪️", "desc": "Direct-Drive Washing Machines, Treadmill PMDC Spindles, Hermetic Compressors, MOTs"},
    {"id": "mobility", "name": "Mobility & Power Tools", "icon": "🛴", "desc": "Hoverboard BLDC Hubs, Cordless Drill Planetary Gearboxes, 125k RPM Turbines"},
    {"id": "frontier", "name": "Exotic Frontiers & Lab", "icon": "🔬", "desc": "DMD Spatial Light Modulators, Ultrasonic Transducers, Procon Vane Pumps, Stirling"},
    {"id": "kinematics", "name": "Kinematics & Transmissions", "icon": "⚙️", "desc": "Epicyclic Reducers, Geneva Indexers, Scotch Yokes, LeBlanc Ball Balancers"},
    {"id": "workshop", "name": "Workshop Fabrication & SOPs", "icon": "🛠️", "desc": "Scrap Steel Spark Testing, Electrolysis Rust Baths, Lapping Plates, Megohmmeters"},
    {"id": "blueprints", "name": "50 Engineering Blueprints", "icon": "📐", "desc": "Complete Schematics, BOMs, and Fabrication Steps for 50 Frontier Projects"},
]

DONORS_DATA = [
    {
        "id": "microwave",
        "name": "Microwave Oven",
        "cat": "domestic",
        "danger": "LETHAL",
        "dangerColor": "#ef4444",
        "harvest": ["High-Voltage Transformer (MOT)", "15A Omron Snap Switches (x3)", "Turntable AC Sync Motor (3-5 RPM)", "High-CFM Shaded-Pole Blower", "Cooling Fan"],
        "avoid": "Magnetron Ceramic Insulator (Contains Carcinogenic Beryllium Oxide - NEVER grind or chip!)",
        "bestFor": "18650 Battery Pack Spot Welder (Blueprint 5), Induction Forge (Blueprint 14), Rock Tumblers, CNC Homing Switches",
        "triage": "Snip and discharge the 2,200V capacitor with a 1k-ohm 20W cement resistor BEFORE touching any internal wires!"
    },
    {
        "id": "washing_machine_dd",
        "name": "Direct-Drive Washing Machine (LG / Fisher & Paykel)",
        "cat": "domestic",
        "danger": "Moderate",
        "dangerColor": "#f59e0b",
        "harvest": ["36-Pole Brushless Pancake Stator", "Neodymium Multi-Pole Outer Rotor", "LeBlanc Annular Fluid/Ball Balancer Ring", "High-Flow Drain Pump"],
        "avoid": "Corroded cast aluminum drum spider brackets (prone to galvanic embrittlement)",
        "bestFor": "Direct-Drive Wind / Hydro Generator (Blueprint 1), Heavy Pottery Wheel Spindle, Silent Lathe Headstock",
        "triage": "Inspect copper windings for scratches; test each phase-to-phase pair with DMM (should measure 5 to 15 ohms matched within 2%)."
    },
    {
        "id": "treadmill",
        "name": "Exercise Treadmill",
        "cat": "domestic",
        "danger": "High (Mains / High DC)",
        "dangerColor": "#ef4444",
        "harvest": ["2.0 - 3.5 HP 90V-180V PMDC Motor", "Heavy Cast-Iron Flywheel with Poly-V Pulley", "SCR / PWM Motor Controller Board", "Heavy ACME Linear Incline Jack"],
        "avoid": "Torn PVC walk belts (low salvage value, high disposal bulk)",
        "bestFor": "2\" x 72\" Knifemaker's Belt Grinder (Blueprint 4), Metal Lathe Variable Speed Spindle, Heavy Drill Press",
        "triage": "Rotate shaft by hand while checking resistance across leads; ensure continuous, smooth resistance with zero open-circuit dead spots."
    },
    {
        "id": "hoverboard",
        "name": "Self-Balancing Hoverboard",
        "cat": "mobility",
        "danger": "Low / Moderate (36V)",
        "dangerColor": "#10b981",
        "harvest": ["Dual 36V 350W Brushless Outrunner Hub Motors (30 NdFeB poles)", "Mainboard with STM32F103 MCU & 12 High-Current MOSFETs", "36V 10S2P Lithium-Ion Battery Pack"],
        "avoid": "Puffy or physically punctured battery packs (thermal runaway risk)",
        "bestFor": "Heavy Autonomous Robot Rover (Blueprint 8), Electric Motorized Wheelbarrow, High-Torque ODrive Robotic Joints",
        "triage": "Flash custom open-source 'hoverboard-firmware-hack' via ST-Link V2 to unlock UART / RC PWM control."
    },
    {
        "id": "eps_steering",
        "name": "Automotive Electric Power Steering (EPS)",
        "cat": "auto",
        "danger": "Low Voltage / High Current (12V 60A)",
        "dangerColor": "#10b981",
        "harvest": ["Ultra-High Torque Brushless PMSM Motor", "Integrated Zero-Backlash Reduction Gearbox", "Dual-Channel Hall / Optical Torque Sensor", "Ground Splined Output Shaft"],
        "bestFor": "Direct-Drive Force Feedback (FFB) Sim Racing Wheel (Blueprint 2), Heavy Robotic Arm Base, CNC 4th Rotary Axis",
        "triage": "Source from Toyota Prius, Nissan Versa, or GM column-assist assemblies; drive with BTS7960 43A H-bridge or VESC."
    },
    {
        "id": "abs_pump",
        "name": "Bosch ABS Hydraulic Pump Block",
        "cat": "auto",
        "danger": "High Pressure (2,600 PSI)",
        "dangerColor": "#ef4444",
        "harvest": ["12V DC 40A Permanent Magnet Motor", "Dual Opposed Radial Micro-Pistons (180 bar / 2,600 PSI)", "Integrated Forged Aluminum Manifold with Solenoid Valves"],
        "bestFor": "Closed-Loop Electro-Hydraulic Servo Press (Blueprint 20), Sheet Metal Hole Punch, Hydraulic Bender",
        "triage": "Flush thoroughly with clean ISO VG 32 hydraulic oil; avoid running dry for more than 5 seconds to prevent plunger galling."
    },
    {
        "id": "medical_o2",
        "name": "Medical Oxygen Concentrator (Respironics / Invacare)",
        "cat": "frontier",
        "danger": "Compressed Gas / High Temp Flame",
        "dangerColor": "#f59e0b",
        "harvest": ["1/3 HP Oil-Free Wobble-Piston AC Compressor (25 PSI)", "Twin Molecular Sieve Beds (13X Zeolite)", "4-Way 12V Spool Solenoid Pilot Valve", "Solid-State Flowmeter"],
        "bestFor": "Oil-Free Oxy-Propane Glassworking & Brazing Station (Blueprint 16), Ozone Water Sterilizer, CNC Mist Air",
        "triage": "Bypass broken logic alarms with an Arduino Nano cycling the 4-way valve every 7.0 seconds in PSA sequence."
    },
    {
        "id": "dlp_projector",
        "name": "DLP Video Projector",
        "cat": "frontier",
        "danger": "Low Voltage / Precision Optics",
        "dangerColor": "#10b981",
        "harvest": ["Digital Micromirror Device (DMD - 2+ million tilting mirrors)", "TIR Prisms & Relay Condenser Lenses", "High-Power High-CRI LED / Laser Engine", "Ultra-Quiet Blower"],
        "bestFor": "DMD Maskless Semiconductor Photolithography Station (Blueprint 9), Structured Light 3D Scanner, Micro-Stereolithography",
        "triage": "Clean optical faces with spectroscopic-grade isopropanol and zero-pressure camelhair brush; avoid touching gold DMD bond wires."
    },
    {
        "id": "printer_scanner",
        "name": "Office Laser Printer / All-In-One Scanner",
        "cat": "consumer",
        "danger": "Low Voltage",
        "dangerColor": "#10b981",
        "harvest": ["Precision Ground Hardened Steel Shafts (6mm, 8mm, 10mm)", "NEMA 14 & 17 Bipolar Hybrid Stepper Motors", "Linear Quadrature Optical Encoder Strip & Readhead", "Polygon Laser Mirror"],
        "bestFor": "Micro-Laser Engraver / 2D Plotter (Blueprint 6), Lathe/Mill Digital Readout (DRO), 360-Degree Robot LiDAR",
        "triage": "Handle optical encoder strips by edges only; clean dust with distilled water and cotton swabs (solvents will dissolve printed grid lines!)."
    },
    {
        "id": "supercaps",
        "name": "Maxwell Ultracapacitors / Defibrillator Units",
        "cat": "frontier",
        "danger": "Extreme Pulsed Current (3,000A)",
        "dangerColor": "#ef4444",
        "harvest": ["2.7V 3,000F Low-ESR Supercapacitors", "High-Current SCR / Thyristor Puck Modules", "Solid Copper Interconnect Busbars"],
        "bestFor": "3,000A Supercapacitor Pulsed Spot Welder (Blueprint 19), Electromagnetic Magnetizer, Railgun Coil Driver",
        "triage": "Always wire 2.7V active balancing boards across series cells; never exceed 2.70V per cell to prevent gas venting."
    },
    {
        "id": "cpap_blower",
        "name": "CPAP / BiPAP Medical Sleep Apnea Unit",
        "cat": "consumer",
        "danger": "Low Voltage / High RPM",
        "dangerColor": "#10b981",
        "harvest": ["Micro-Centrifugal BLDC Turbine (30,000 - 60,000 RPM)", "Whisper-Quiet Silencing Chamber", "Closed-Loop Differential Air Pressure Transducer"],
        "bestFor": "High-Static CNC Vacuum Chuck & Pick-and-Place Station (Blueprint 15), Solder Fume HEPA Extractor, PCB Hold-Down",
        "triage": "Drive with budget 30A RC sensorless ESC; provide smooth 50Hz PWM ramp-up to prevent rotor slip."
    },
    {
        "id": "hard_drive",
        "name": "3.5\" Computer Hard Disk Drive (HDD)",
        "cat": "consumer",
        "danger": "Safe",
        "dangerColor": "#10b981",
        "harvest": ["Ultra-Fast Rotary Voice Coil Actuator Arm", "Twin N52 Neodymium Arc Magnets", "Fluid Dynamic Bearing 3-Phase Spindle Motor", "Precision Mirror-Polished Platters"],
        "bestFor": "Audio-Driven Laser Vector Galvanometer (Blueprint 3), Dynamic Seismometer Balancer, Magnetorheological Haptic Knob (Blueprint 17)",
        "triage": "Pry voice coil magnets apart using a brass wedge; keep fingers clear of magnetic pinch points (crush hazard)."
    }
]

BLUEPRINTS_DATA = [
    {
        "num": 1,
        "title": "Direct-Drive Wind / Hydro Generator",
        "donor": "LG Washing Machine Direct-Drive Stator",
        "power": "500W @ 120-250 RPM",
        "diff": "Intermediate",
        "diffColor": "#f59e0b",
        "desc": "Converts a 36-pole brushless pancake motor into a whisper-quiet, low-RPM alternator delivering 500W to off-grid battery banks without noisy step-up gearboxes.",
        "bom": ["LG direct-drive wash motor assembly", "MDS-100A 3-phase bridge rectifier", "35mm pillow block bearings", "Savonius / Pelton impeller wheel", "MPPT solar/wind charge controller"],
        "schematic": "[ LG 36-Pole Pancake Stator ] ===(3-Phase AC)===> [ MDS-100A Rectifier ] ===(48V DC)===> [ MPPT Controller ] ===> [ 48V Battery Bank ]",
        "formula": "V_phase = 4.44 * f * N * Phi_m",
        "sop": "1. Unbolt outer rotor and stator from scrap LG washer drum.\n2. Machine custom 1\" steel center shaft.\n3. Mount stator to steel tower plate.\n4. Route 3 phase leads through MDS-100A rectifier.\n5. Connect output to 48V battery bank with 60A dump-load resistor."
    },
    {
        "num": 2,
        "title": "Direct-Drive Sim Racing Wheel",
        "donor": "Automotive Electric Power Steering (EPS)",
        "power": "25-30 N*m Force Feedback",
        "diff": "Intermediate",
        "diffColor": "#f59e0b",
        "desc": "Builds a professional esports direct-drive sim racing steering wheel rivaling $1,500 Fanatec/Simucube bases using a junkyard EPS steering column.",
        "bom": ["Toyota Prius or Nissan EPS column", "STM32F103 'BluePill' MCU running OpenFFB", "BTS7960 43A dual H-bridge motor driver", "14-bit AS5600 magnetic rotary encoder", "12V 40A server power supply"],
        "schematic": "[ PC Sim (Assetto Corsa/iRacing) ] ===(USB HID 1kHz)===> [ STM32 BluePill ] ===(PWM)===> [ BTS7960 43A ] ===(12V 40A)===> [ EPS Column Spindle ]",
        "formula": "Tau_feedback = K_t * I_armature",
        "sop": "1. Remove steering column from scrap car; grind off mounting tabs.\n2. Pin steering shaft solid to eliminate collapsible safety slip.\n3. Wire STM32 running OpenFFB firmware.\n4. Connect BTS7960 gate pins to STM32 timer PWM.\n5. Mount 13\" real leather rally wheel to splined shaft."
    },
    {
        "num": 3,
        "title": "Audio-Driven Laser Vector Galvanometer",
        "donor": "Dual 3.5\" Hard Disk Drive Voice Coils",
        "power": "12V 2A / Audio Signal",
        "diff": "Novice",
        "diffColor": "#10b981",
        "desc": "Repurposes two HDD voice-coil head arms into an ultra-fast XY optical galvanometer projecting real-time music Lissajous patterns and vector laser graphics.",
        "bom": ["2x 3.5\" dead SATA hard drives", "Two 10mm front-surface optical mirrors", "TDA7297 15W+15W stereo audio amplifier", "5mW to 50mW 532nm green laser diode", "Dual rubber torsion return springs"],
        "schematic": "[ Audio Source / PC Soundcard ] ===> [ TDA7297 15W Stereo Amp ] ===> [ X Voice Coil ] + [ Y Voice Coil ] ===> [ Front-Surface Mirrors ] ===> Laser Vector Image",
        "formula": "Theta_deflection = (B * L * I) / K_torsion",
        "sop": "1. Extract voice coil actuator arms from two identical hard drives.\n2. Mount front-surface mirrors to tips at 90 degree orthogonal angles.\n3. Add silicone rubber damper strips to eliminate resonance ringing.\n4. Connect Left/Right audio channels directly to coil windings.\n5. Aim green laser diode through X then Y mirror onto wall."
    },
    {
        "num": 4,
        "title": "2\" x 72\" Knifemaker's Belt Grinder",
        "donor": "Treadmill PMDC Motor & Speed Board",
        "power": "2.5 HP @ 4,000 RPM (Variable)",
        "diff": "Advanced",
        "diffColor": "#ef4444",
        "desc": "Constructs an industrial knifemaking 2x72 belt grinder with variable speed and continuous low-RPM torque for bevel grinding, profiling, and hollow grinding.",
        "bom": ["2.5 HP 130V DC Treadmill Motor", "KBIC-120 / KBIC-240 SCR speed control board", "10k ohm speed potentiometer", "4\" crowned drive wheel + 2\" tracking idlers", "2\" square steel box tubing chassis"],
        "schematic": "[ 120V AC Mains ] ===> [ KBIC-120 SCR Controller ] ===(0-130V Rectified DC)===> [ Treadmill PMDC Motor ] ===(Poly-V Belt)===> [ 2x72 Grinder Drive Wheel ]",
        "formula": "SFPM = (RPM * Pi * Diameter_inches) / 12",
        "sop": "1. Fabricate three-wheel C-frame from 2\" square tubing.\n2. Mount treadmill motor on rear pivoting tension plate.\n3. Wire KBIC-120 board with 0.015 ohm internal IR compensation resistor.\n4. Wire 10k speed pot and emergency stop mushroom switch.\n5. Track 2x72 ceramic grinding belt to dead-center at 4,500 SFPM."
    },
    {
        "num": 5,
        "title": "18650 Battery Pack Spot Welder",
        "donor": "Microwave Oven Transformer (MOT)",
        "power": "3.5V AC @ 800A (Sub-Cycle)",
        "diff": "Intermediate",
        "diffColor": "#f59e0b",
        "desc": "Rewinds a dangerous 2,000V microwave transformer into an ultra-high-current low-voltage spot welder to weld 0.15mm pure nickel strips onto 18650 lithium cells.",
        "bom": ["800W - 1200W Microwave Transformer", "6 feet of 2 AWG ultra-flexible copper welding cable", "Arduino Nano + 40A SSR board (dual-pulse timing)", "Solid copper weld electrode handpiece", "Momentary foot trigger pedal"],
        "schematic": "[ 120V Mains ] ===[ 40A Solid-State Relay ]===> [ Rewound MOT (Primary) ] || [ Rewound MOT (2 Turns 2 AWG) ] ===(3.5V 800A)===> [ Dual Copper Electrodes ]",
        "formula": "Heat = I^2 * R_contact * t_pulse",
        "sop": "1. Hacksaw through secondary high-voltage fine copper coil; punch core clean.\n2. Wind 2 to 3 turns of heavy 2 AWG copper welding cable through open core.\n3. Program Arduino for double-pulse timing: 20ms pre-pulse + 50ms dwell + 120ms main weld.\n4. Connect 40A SSR to primary mains AC input.\n5. Test weld on nickel strip; verify nugget tears metal without heating cell."
    },
    {
        "num": 6,
        "title": "Micro-Laser Engraver & 2D Plotter",
        "donor": "Two DVD-RW Laser Sled Micro-Steppers",
        "power": "5V 2A / 500mW 405nm Laser",
        "diff": "Novice",
        "diffColor": "#10b981",
        "desc": "Combines two optical disc sled micro-steppers into a sub-millimeter XY Cartesian laser engraving station for marking wood, leather, acrylic, and cutting PCB resist.",
        "bom": ["2x DVD-RW optical drive assemblies", "2x A4988 stepper driver modules", "Arduino Nano running GRBL 1.1 firmware", "500mW 405nm violet focusable laser module", "12V 2A wall adapter"],
        "schematic": "[ PC (LaserGRBL / LightBurn) ] ===(G-Code)===> [ Arduino Nano GRBL ] ===> [ A4988 Drivers (X & Y) ] ===> [ DVD Leadscrew Sleds (40mm x 40mm) ]",
        "formula": "Step_Resolution = Lead_Screw_Pitch / (Steps_per_Rev * Microstepping)",
        "sop": "1. Remove optical sled assemblies from two scrap DVD drives.\n2. Fasten X and Y stages perpendicularly to aluminum base plate.\n3. Wire bipolar 4-wire micro-steppers to A4988 drivers.\n4. Set GRBL steps/mm to 106.67.\n5. Mount 500mW laser on Z carriage and engrave intricate vector logos."
    },
    {
        "num": 7,
        "title": "Whisper-Quiet Airbrush & Vacuum Degas Chamber",
        "donor": "Refrigerator Hermetic Compressor",
        "power": "1/6 HP / 28.5 inHg Vacuum / 120 PSI",
        "diff": "Novice",
        "diffColor": "#10b981",
        "desc": "Converts a whisper-quiet (<40 dB) sealed refrigerator compressor into a dual-mode silent studio airbrush supply and high-vacuum degassing chamber for casting resins.",
        "bom": ["1/6 HP hermetic refrigerator compressor", "Empty 2.5 gallon fire extinguisher cylinder", "Oil-mist coalescing coalescent filter + oil trap", "1\" clear Lexan polycarbonate vacuum pot lid", "Adjustable 0-100 PSI air regulator"],
        "schematic": "[ Suction Port (-28.5 inHg) ] <=== [ Hermetic Compressor ] ===> [ Discharge Port (+120 PSI) ] ===> [ Oil Trap ] ===> [ Airbrush Regulator ]",
        "formula": "P_ultimate_vacuum = P_atm - Delta_P_pump",
        "sop": "1. Safely recover freon; cut lines and extract compressor pot.\n2. Solder 1/4\" brass NPT fittings onto suction and discharge stubs.\n3. Plumb coalescing filter on discharge to catch internal pump oil.\n4. Plumb vacuum pot to suction port with isolation ball valve.\n5. Run test: pulls 28.5 inHg in 45 seconds with near-zero acoustic noise."
    },
    {
        "num": 8,
        "title": "Heavy Autonomous Robot Rover (AGV)",
        "donor": "36V Hoverboard Hubs & Flashed Mainboard",
        "power": "36V 700W (Carries 150+ lbs)",
        "diff": "Intermediate",
        "diffColor": "#f59e0b",
        "desc": "Converts a broken hoverboard into an autonomous heavy-payload robotic gantry capable of hauling 150 lbs over grass, curbs, and shop floors via ROS2 navigation.",
        "bom": ["Scrap hoverboard with wheels and motherboard", "ST-Link V2 programmer dongle", "Raspberry Pi 4 / ESP32 rover brain", "Aluminum 1\" square tubing chassis", "36V 4.4Ah hoverboard lithium pack"],
        "schematic": "[ Raspberry Pi / ROS2 ] ===(UART Serial 115200)===> [ Flashed Hoverboard STM32 MCU ] ===> [ Dual 3-Phase Inverters ] ===> [ Dual 350W Hub Motors ]",
        "formula": "Velocity_Linear = (RPM * 2 * Pi * Wheel_Radius) / 60",
        "sop": "1. Strip hoverboard plastics; preserve central frame casting and wiring harness.\n2. Solder 4-pin SWD header to STM32 mainboard.\n3. Flash open-source hoverboard firmware with ST-Link.\n4. Connect ESP32 / Raspberry Pi to USART3 pins.\n5. Send velocity/steering commands via serial protocol; rover carries 150 lbs effortlessly."
    },
    {
        "num": 9,
        "title": "DMD Maskless Semiconductor Photolithography Station",
        "donor": "DLP Projector Digital Micromirror Device (DMD)",
        "power": "405nm UV Direct-Write (Sub-Micron Res.)",
        "diff": "Wizard",
        "diffColor": "#8b5cf6",
        "desc": "Converts a salvaged DLP projector optical core and DMD chip into a maskless direct-write photolithography station for exposing custom silicon FETs and microfluidic channels.",
        "bom": ["DLP Projector optical engine with DMD chip", "405nm 5W UV high-power LED array", "20x Plan Achromat metallurgical microscope objective", "Dual DVD-RW micro-stepping leadscrew stages", "Python tiled coordinate stepping software"],
        "schematic": "[ PC Mask Image / GDSII ] ===(HDMI)===> [ Projector DMD Controller ] ===> [ 405nm UV LED ] ===> [ 20x Objective ] ===> [ Sub-Micron Photoresist Wafer ]",
        "formula": "Diffraction_Limit = 0.61 * lambda / NA (Res: 0.85 um)",
        "sop": "1. Extract DMD board and TIR prism from projector.\n2. Replace white projection lamp with collimated 405nm UV LED.\n3. Couple output through reversed 20x infinity microscope objective.\n4. Calibrate optical reduction: 1 display pixel maps to 0.85 microns on silicon.\n5. Expose SU-8 photoresist on glass slides for microfluidic lab-on-a-chip prototyping."
    },
    {
        "num": 10,
        "title": "Precision 30 kHz Ultrasonic Craft & Resin Knife",
        "donor": "Langevin Dental Scaler Piezoelectric Transducer",
        "power": "30 kHz Resonant Acoustic Booster Horn",
        "diff": "Advanced",
        "diffColor": "#ef4444",
        "desc": "Repurposes a piezo Langevin transducer and custom titanium booster horn into a 30 kHz ultrasonic scalpel that glides through cured 3D resin supports and carbon fiber like butter.",
        "bom": ["Langevin bolt-clamped piezoelectric sandwich transducer", "Grade 5 Titanium (Ti-6Al-4V) stepped booster horn", "Self-resonant 30 kHz phase-locked-loop driver board", "Standard surgical scalpel blade collet", "Foot pedal power switch"],
        "schematic": "[ 30 kHz PLL Driver ] ===(250V RMS AC)===> [ Langevin PZT Disc Stack ] ===(Piezo Contraction)===> [ Titanium Booster Horn ] ===(30 um Tip Oscillation)===> [ Scalpel ]",
        "formula": "Acoustic_Velocity = sqrt(Elastic_Modulus / Density) = 5,090 m/s in Ti",
        "sop": "1. Machine half-wavelength titanium horn resonant at 30 kHz.\n2. Torque central PZT assembly bolt to 35 N*m preload.\n3. Tune PLL oscillator to acoustic anti-resonance for maximum tip excursion.\n4. Clamp surgical blade in horn tip slot.\n5. Slice 3D print supports with zero blade resistance and zero resin fracturing."
    },
    {
        "num": 11,
        "title": "Alternator Absorption Engine Dynamometer",
        "donor": "High-Output Car Alternator (12V 140A)",
        "power": "Continuous 2.5 HP Absorption Bench",
        "diff": "Intermediate",
        "diffColor": "#f59e0b",
        "desc": "Builds a professional trunnion-mounted absorption dynamometer to measure continuous horsepower and torque curves of small engines and electric motors.",
        "bom": ["140A GM/Delco automotive alternator", "Pivoting trunnion cradle with low-friction ball bearings", "S-Beam strain gauge load cell (10kg) + HX711 24-bit ADC", "Arduino closed-loop PWM field-current regulator", "Water-cooled 12V 100A resistive dummy load bank"],
        "schematic": "[ Test Engine ] ===(Shaft Coupler)===> [ Trunnion Alternator ] ===(Torque Reaction)===> [ S-Beam Load Cell ] <===> [ Arduino Dyno Logger ]",
        "formula": "Horsepower = (Torque_ft_lbs * RPM) / 5252",
        "sop": "1. Mount alternator on free-floating pillow blocks allowing stator rotation.\n2. Affix 12\" calibration torque arm to stator, pressing on S-beam load cell.\n3. Connect field coil to Arduino PWM MOSFET driver.\n4. Route 3-phase rectified DC output into heavy immersion water heater loads.\n5. Modulate field current to hold steady engine RPM; log true brake torque in real time."
    },
    {
        "num": 12,
        "title": "Desktop Abrasive Slurry Micro-Waterjet Cutter",
        "donor": "Procon 250 PSI Rotary Vane Pump",
        "power": "250 PSI Venturi Garnet Slurry Stream",
        "diff": "Advanced",
        "diffColor": "#ef4444",
        "desc": "Combines a commercial espresso Procon rotary vane pump with an abrasive venturi mixer to cut sheet aluminum, glass, and carbon fiber without heat-affected zones.",
        "bom": ["Procon Series 2 or 3 brass rotary vane pump", "1/2 HP continuous-duty electric motor", "Venturi abrasive injector block", "80-mesh Barton garnet abrasive hopper", "Tungsten carbide micro-orifice nozzle (0.5mm)"],
        "schematic": "[ Water Supply ] ===> [ Procon Pump (250 PSI) ] ===> [ Venturi Abrasive Mixer ] <===[ Garnet Hopper ] ===> [ Tungsten Micro-Nozzle ] ===> Slices Carbon Fiber",
        "formula": "Kinetic_Energy = 0.5 * m_garnet * v_waterjet^2",
        "sop": "1. Couple 1/2 HP induction motor to Procon slotted drive shaft.\n2. Plumb water supply through 5-micron pre-filter to protect brass vanes.\n3. Machine aluminum venturi body with angled garnet vacuum suction port.\n4. Install 0.5mm carbide nozzle tube.\n5. Cut 1.5mm carbon fiber sheet and G10 circuit boards cleanly with zero thermal delamination."
    },
    {
        "num": 13,
        "title": "Solid-State Woodstove Seebeck Generator Stack",
        "donor": "Thermoelectric Peltier Modules (TEC1-12706)",
        "power": "15W - 25W Continuous Off-Grid 12V",
        "diff": "Novice",
        "diffColor": "#10b981",
        "desc": "Harvests waste heat from a woodstove or camp stove using clamping bismuth telluride modules to charge smartphones and LED battery banks during winter blackouts.",
        "bom": ["4x TEC1-12706 or TEG modules", "1/2\" thick copper heat spreader base plate", "CPU liquid cooling radiator + 12V low-draw pump", "LTC3780 high-efficiency buck-boost converter", "Thermal ceramic heatsink paste"],
        "schematic": "[ Woodstove Top (250°C) ] ===> [ Copper Base ] ===> [ 4x TEG Modules (Delta-T: 180°C) ] ===> [ Liquid Chilled Radiator ] ===> [ LTC3780 Buck-Boost ] ===> 12V 2A Output",
        "formula": "V_open_circuit = N_couples * Seebeck_Coeff * Delta_T",
        "sop": "1. Sand copper baseplate mirror-flat using 1200-grit lapping paper.\n2. Apply thin ceramic thermal compound across all TEG faces.\n3. Clamp modules between baseplate and liquid heat exchanger with Belleville spring washers.\n4. Wire modules in series-parallel for nominal 16V open-circuit output.\n5. Route power through LTC3780 regulator; provides 15W continuous power indefinitely from wood heat."
    },
    {
        "num": 14,
        "title": "2,000W Scrap Induction Cooktop ZVS Forge",
        "donor": "Induction Cooktop IGBTs & Litz Pancake Coil",
        "power": "1,800W - 2,200W @ 30-50 kHz",
        "diff": "Advanced",
        "diffColor": "#ef4444",
        "desc": "Harvests high-current 1200V IGBTs and resonant MKP capacitors from an induction cooktop to construct an ultra-compact blacksmith induction forge.",
        "bom": ["Induction cooktop pancake coil + 2x 1200V 40A IGBTs", "0.33uF 1200V MKP pulse resonant capacitors", "Heavy copper water-cooled work coil", "30V-48V 40A DC power supply", "Submersible water cooling pump"],
        "schematic": "[ 48V 40A DC ] ===> [ Mazzilli ZVS Driver Array (Cooktop IGBTs) ] <===> [ MKP Resonant Tank ] <===> [ Copper Work Coil ] ===> 1,000°C Steel Glow in 15s",
        "formula": "f_resonant = 1 / (2 * Pi * sqrt(L_work * C_tank))",
        "sop": "1. Desolder H20R1203 IGBTs and MKP film capacitors from cooktop motherboard.\n2. Wind 6-turn helical work coil from 1/4\" soft copper refrigeration tubing.\n3. Connect coil to water pump loop for internal cooling.\n4. Wire ZVS driver with fast ultrafast feedback diodes.\n5. Power up with 48V DC; heats 1/2\" steel rebar to bright cherry red in 15 seconds."
    },
    {
        "num": 15,
        "title": "High-Static CNC Vacuum Chuck & Pick-and-Place",
        "donor": "CPAP / BiPAP Sleep Apnea Micro-Blower",
        "power": "50,000 RPM BLDC (>60 cmH2O Static Suction)",
        "diff": "Intermediate",
        "diffColor": "#f59e0b",
        "desc": "Repurposes an ultra-high-RPM medical CPAP blower into a vacuum hold-down table for micro-milling delicate 0.5mm PCBs and an SMD vacuum pick-and-place pen.",
        "bom": ["CPAP micro-centrifugal BLDC turbine (30,000 - 60,000 RPM)", "30A sensorless RC ESC + 12V 10A power supply", "Miniature cyclone swarf separator filter", "Milled acrylic vacuum plenum bed with silicone gasket", "Foot-pedal solenoid vacuum release valve"],
        "schematic": "[ CPAP Blower (50k RPM) ] <===[ Cyclone Chip Trap ] <===[ Vacuum Chuck Bed ] ===> Holds 0.5mm PCB Flat with 60 cmH2O Negative Pressure",
        "formula": "F_clamping = Delta_P * Vacuum_Area",
        "sop": "1. Solder 3 phase wires of CPAP blower to 30A RC ESC.\n2. Program microcontroller to send 50 Hz servo PWM ramp (1.0ms to 1.8ms).\n3. Plumb suction port through transparent acrylic cyclone filter to trap dust.\n4. Mill matrix of 1mm vacuum suction holes in acrylic fixture plate.\n5. Clamps warped copper-clad board dead-flat without mechanical hold-down clamps."
    },
    {
        "num": 16,
        "title": "Oil-Free Oxy-Propane Glassworking Station",
        "donor": "Medical Oxygen Concentrator (10 LPM)",
        "power": "Continuous 8-10 LPM @ 93% O2",
        "diff": "Intermediate",
        "diffColor": "#f59e0b",
        "desc": "Converts a discarded medical oxygen concentrator into an autonomous tank-free oxygen generator supplying continuous 93% pure O2 for a 2,600°C borosilicate glass torch.",
        "bom": ["Scrap Respironics / Invacare oxygen concentrator", "Arduino Nano + 2-channel 5V relay module", "2.5-gallon aluminum accumulator surge tank", "Dual inline oxygen & propane flashback arrestors", "Surface-mix glassworking torch"],
        "schematic": "[ 1/3 HP Compressor ] ===(25 PSI)===> [ 4-Way Valve ] <===> [ Twin 13X Zeolite Sieve Beds ] ===(93% O2)===> [ Accumulator Tank ] ===> [ 2,600°C Torch ]",
        "formula": "Purity_O2 = (1 - (N2_flow / Air_flow)) * 100",
        "sop": "1. Gut malfunctioning alarm motherboard from concentrator chassis.\n2. Connect 4-way pilot solenoid to Arduino Nano relay board.\n3. Program PSA cycle: 7.0s Bed A, 0.5s Equalization, 7.0s Bed B.\n4. Route pure O2 outlet into surge accumulator tank through check valve.\n5. Connect to torch with flashback arrestor; melts heavy borosilicate glass effortlessly."
    },
    {
        "num": 17,
        "title": "Magnetorheological (MR) Programmable Haptic Dial",
        "donor": "Laser Printer Toner Magnetite + HDD Motor",
        "power": "50 kPa Bingham Yield Stress / 12V 2A",
        "diff": "Advanced",
        "diffColor": "#ef4444",
        "desc": "Extracts sub-micron magnetite (Fe3O4) nanoparticles from discarded laser printer toner to formulate magnetorheological fluid, driving a software-programmable haptic feedback knob.",
        "bom": ["100g pure magnetite extracted from laser printer toner", "40ml light paraffin mineral oil + 2ml oleic acid", "3.5\" HDD fluid-dynamic bearing spindle motor", "14-bit AS5600 absolute magnetic rotary encoder", "ESP32 MCU + IRLB8721 MOSFET + 500-turn electromagnetic bobbin"],
        "schematic": "[ HDD Spindle + AS5600 ] ===(Angle Data 1kHz)===> [ ESP32 Controller ] ===(PWM)===> [ MR Electromagnetic Coil ] ===> 50 kPa Yield Lockup in 3ms",
        "formula": "Tau_yield = Tau_0 + Alpha * B^2",
        "sop": "1. Wash magnetic toner powder in acetone to strip polymer coatings, settling pure Fe3O4.\n2. Suspend magnetite in light mineral oil (40% volume fraction) with oleic acid surfactant.\n3. Fill 1mm shear gap between stationary coil housing and rotor spindle.\n4. Program ESP32 to compute dynamic current: clicks, viscous damping, and virtual end-stops.\n5. Solidifies fluid into rigid solid in under 5ms, creating rock-solid physical detents."
    },
    {
        "num": 18,
        "title": "Monolithic Flexure Interferometer & Z-Stage",
        "donor": "DVD-RW Leadscrew + Blu-Ray Optical Pickup",
        "power": "Sub-Micron Elastic Motion / 325nm Fringe Res.",
        "diff": "Master",
        "diffColor": "#ef4444",
        "desc": "Mills an elastic 4-bar parallelogram flexure from aircraft aluminum scrap, driven by a DVD sled leadscrew and monitored by a Blu-Ray laser pickup to count nanometer interference fringes.",
        "bom": ["6061-T6 aluminum tool plate (6\" x 6\" x 1/2\")", "DVD-RW laser sled stepper motor + M3 leadscrew", "20:1 ground steel lever reduction arm", "Blu-Ray optical pickup (polarizing beam-splitter + PIN diode)", "650nm red laser diode + 2x front-surface mirrors"],
        "schematic": "[ DVD Sled Stepper ] ===(20:1 Lever Arm)===> [ Monolithic Parallelogram Flexure ] ===> [ Michelson Interferometer ] ===> Photodiode Counts 325nm Fringes",
        "formula": "k_flexure = (2 * E * b * t^2.5) / (9 * Pi * r^0.5)",
        "sop": "1. Mill 4 notch flexure hinges (0.8mm web thickness) in aluminum plate.\n2. Mount DVD stepper with 20:1 lever arm to achieve 62.5 nanometer physical steps.\n3. Align salvaged polarizing beam-splitter cube and front-surface mirrors.\n4. Route red laser beam to photodiode; each half-wavelength cycle equals 325 nm.\n5. Count fringes with Arduino comparator to measure sub-micron thermal expansion of metals."
    },
    {
        "num": 19,
        "title": "3,000A Supercapacitor Pulsed Spot Welder",
        "donor": "Two Maxwell 2.7V 3,000F Supercaps",
        "power": "5.4V 1,500F / 3,000A Sub-Millisecond",
        "diff": "Master",
        "diffColor": "#ef4444",
        "desc": "Builds an industrial-grade capacitive-discharge spot welder delivering 3,000A pulses of 1-3 ms duration to weld pure nickel tabs onto lithium cells with zero cell substrate heating.",
        "bom": ["2x Maxwell DuraBlue 2.7V 3,000F ultracapacitors", "8x parallel IRLB3034 MOSFET array (R_ds < 0.2 mOhm)", "TC4420 6A peak gate driver IC", "1/4\" solid copper busbars", "Arduino Nano double-pulse timer"],
        "schematic": "[ 12V Charger ] ===> [ Supercap Bank: 5.4V 1500F ] ===> [ Solid Copper Probes ] ===(Workpiece)===> [ 8x IRLB3034 Array ] <===[ TC4420 Driver ]",
        "formula": "E = 0.5 * C * V^2 (21,870 Joules Stored)",
        "sop": "1. Bolt capacitors in series using 1/4\" solid copper busbar plates.\n2. Mount 8x IRLB3034 MOSFETs in parallel on solid copper ground plane.\n3. Wire TC4420 gate driver with isolated 15V supply to guarantee V_gs = 12V.\n4. Set double-pulse timing: 0.5ms pre-pulse + 1.5ms pause + 2.5ms main weld.\n5. Weld nickel tabs; peel test proves circular steel buttons tear without heating battery."
    },
    {
        "num": 20,
        "title": "Closed-Loop Hydraulic Servo Press",
        "donor": "Bosch ABS Pump + Camshaft VVT Spool Valve",
        "power": "2,000 PSI / 0.01mm Position Loop",
        "diff": "Master",
        "diffColor": "#ef4444",
        "desc": "Converts an automotive ABS radial micro-piston pump and a camshaft VVT proportional spool valve into a 2,000 PSI closed-loop hydraulic servo press with programmable tonnage limits.",
        "bom": ["Bosch 8.0/9.0 ABS hydraulic pump assembly", "Automotive camshaft VVT oil control spool valve", "2-ton hydraulic press ram cylinder", "0-250 bar piezoresistive pressure transducer", "ESP32 dual-loop controller + BTS7960 PWM driver"],
        "schematic": "[ ABS Pump (180 bar) ] ===> [ VVT 4-Way Spool Valve (150Hz PWM) ] ===> [ Hydraulic Ram ] <===> [ 0.01mm DRO Scale + 250 Bar Sensor ] <===> [ ESP32 PID ]",
        "formula": "F_ram = Pressure * Area_piston",
        "sop": "1. Plumb ABS pump high-pressure discharge port to VVT spool valve inlet.\n2. Connect VVT advance and retract ports to dual-acting press cylinder.\n3. Inject 150 Hz dither PWM signal into VVT valve to eliminate spool stiction.\n4. Feed digital caliper DRO data and pressure sensor into ESP32 nested PID loop.\n5. Press-fit delicate sleeve bearings to 0.01mm depth with automatic tonnage cutoff."
    },
    {
        "num": 21,
        "title": "Magnetic-Coupled Hermetic High-Pressure Autoclave",
        "donor": "N52 Neodymium Ring + 316L Stainless Can",
        "power": "100 Bar / Zero Dynamic Rotary Seals",
        "diff": "Wizard",
        "diffColor": "#8b5cf6",
        "desc": "Builds a completely seal-less, non-penetrating rotary magnetic drive transmitting 5 N*m of torque across a solid 316L stainless steel wall for 100-bar hydrothermal reactions and vacuum chambers.",
        "bom": ["12x N52 Neodymium wedge magnets (Outer Rotor)", "12x Encapsulated N52 magnets (Inner Rotor)", "316L austenitic stainless steel containment dome (2mm wall)", "Silicon Nitride (Si3N4) full-ceramic ball bearings", "Brushless BLDC drive motor"],
        "schematic": "[ External BLDC Motor ] ===> [ External 12-Pole N52 Ring ] || (Solid 316L Dome) || [ Internal 12-Pole Ring ] ===> [ Ceramic Bearings ] ===> [ Autoclave Impeller ]",
        "formula": "Tau_max = (B_gap^2 * Area * r_gap) / (2 * mu_0)",
        "sop": "1. Machine 316L non-magnetic stainless containment dome with high-pressure Viton O-ring seal.\n2. Assemble external 12-pole alternating magnet carrier on motor spindle.\n3. TIG-weld hermetic stainless jacket around internal matching magnet rotor.\n4. Install Si3N4 ceramic bearings (lubricant-free, chemically inert).\n5. Test magnetic coupling: delivers 5.5 N*m of torque with zero seal leakage at 100 bar."
    }
]

MINDMAZE_QUESTIONS = [
    {
        "q": "You find an unmarked motor with 3 identical yellow wires. Resistance between any pair is exactly 0.8 ohms. What type of motor is this?",
        "options": ["Bipolar Stepper Motor", "3-Phase Brushless BLDC / PMSM", "Series-Wound AC Universal Motor", "Capacitor-Start Induction Motor"],
        "answer": 1,
        "explain": "Three identical phase resistances with 120-degree symmetry indicate a 3-Phase Brushless BLDC or Permanent Magnet Synchronous Motor (PMSM). Drive it with an ESC, VESC, or E-bike controller!"
    },
    {
        "q": "You touch a mystery piece of scrap steel to a bench grinder. The sparks are short, dense, brilliant white, and explode violently in multi-branched starbursts. What is it?",
        "options": ["AISI 1018 Mild Steel", "AISI 1045 Medium Carbon Shaft Steel", "AISI 1095 / 52100 High-Carbon Tool Steel", "Gray Cast Iron"],
        "answer": 2,
        "explain": "Carbon reacts with atmospheric oxygen as molten steel flies off the wheel; higher carbon creates explosive starbursts. Dense white starburst showers signify High-Carbon Tool Steel (1095/52100), perfect for making cutting tools!"
    },
    {
        "q": "Why is it FORBIDDEN in professional salvage lore to clean a dirty copper motor commutator with emery cloth or sandpaper?",
        "options": ["It generates dangerous static electricity", "Microscopic conductive carborundum grit embeds in the copper, shredding brushes", "It demagnetizes the stator magnets", "It alters the armature timing angle"],
        "answer": 1,
        "explain": "Emery cloth and sandpaper shed ultra-hard abrasive particles that lodge permanently inside the soft copper commutator bars. Under power, these embedded grains act as miniature chisels that rapidly chew up carbon brushes. Clean ONLY with maroon Scotch-Brite!"
    },
    {
        "q": "Before disassembling a microwave oven to harvest the transformer, how must you safely neutralize the high-voltage capacitor?",
        "options": ["Spray it with water", "Touch a screwdriver between terminals with your bare hands", "Discharge across terminals using an insulated 1k-ohm 20W cement resistor", "Leave it unplugged for 10 minutes"],
        "answer": 2,
        "explain": "Microwave capacitors store up to 2,200V at lethal energy levels. Bleeder resistors inside can fail open. Always bridge the terminals with an insulated 1k-ohm 20W power resistor or insulated clip lead before touching!"
    },
    {
        "q": "In rotordynamic balancing, what extraordinary phenomenon occurs in the LeBlanc Automatic Ball Balancer when rotor speed exceeds its natural critical resonance frequency (omega > omega_n)?",
        "options": ["The balls fly out of the race due to centrifugal failure", "A 180-degree phase shift occurs, forcing balls to migrate opposite the heavy spot to cancel vibration", "The balls lock solid at the unbalance spot, quadrupling vibration", "The rotor undergoes gyroscopic precession and reverses direction"],
        "answer": 1,
        "explain": "Supercritical rotordynamics (Jeffcott model) dictates a 180-degree phase inversion above resonance: the rotor orbits about its true center of mass rather than its geometric center, automatically flinging the free balls diametrically opposite to the heavy spot!"
    },
    {
        "q": "When harvesting an Electric Power Steering (EPS) column for a DIY force-feedback racing wheel, why must you pin or weld the collapsible safety shaft?",
        "options": ["To increase the motor's electrical voltage", "To prevent the collapsible impact joint from twisting and introducing sloppy backlash under 30 Nm torque", "To ground the Hall-effect sensors", "To disable the factory airbag detonator"],
        "answer": 1,
        "explain": "Automotive steering columns feature a telescoping safety joint designed to collapse during a collision. Under intense 25-30 Nm sim racing forces, this joint flexes and introduces rotational play unless pinned or welded rigid."
    }
]

print(f"Data verified: {len(CATEGORIES)} categories, {len(DONORS_DATA)} donors, {len(BLUEPRINTS_DATA)} blueprints, {len(MINDMAZE_QUESTIONS)} quiz questions.")

def build_html():
    donors_json = json.dumps(DONORS_DATA)
    blueprints_json = json.dumps(BLUEPRINTS_DATA)
    questions_json = json.dumps(MINDMAZE_QUESTIONS)
    categories_json = json.dumps(CATEGORIES)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ENCARTA '95 : ELECTROMECHANICA &bull; Interactive Salvage Encyclopedia</title>
<script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
<style>
  :root {{
    --bg-base: #06171b;
    --bg-surface: #0a242a;
    --bg-panel: #0f343d;
    --border-gold: #dfb15b;
    --gold-glow: rgba(223, 177, 91, 0.25);
    --cyan-accent: #06b6d4;
    --text-main: #f1f5f9;
    --text-muted: #94a3b8;
  }}

  body {{
    background-color: var(--bg-base);
    color: var(--text-main);
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
    user-select: none;
    overflow-x: hidden;
  }}

  /* CRT Scanline Overlay */
  .crt-overlay {{
    pointer-events: none;
    position: fixed;
    top: 0; left: 0; width: 100vw; height: 100vh;
    background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.03), rgba(0, 255, 0, 0.01), rgba(0, 0, 255, 0.03));
    background-size: 100% 3px, 6px 100%;
    z-index: 9999;
    opacity: 0.85;
    transition: opacity 0.3s;
  }}
  .crt-off {{ opacity: 0 !important; }}

  /* Beveled 90s CD-ROM Buttons */
  .encarta-btn {{
    background: linear-gradient(180deg, #164e5b 0%, #0c2d35 100%);
    border: 1px solid #2a7c8e;
    border-top-color: #45a4b9;
    border-left-color: #45a4b9;
    border-bottom-color: #06191d;
    border-right-color: #06191d;
    box-shadow: 1px 1px 0px rgba(0,0,0,0.6);
    color: #e2e8f0;
    transition: all 0.08s ease;
  }}
  .encarta-btn:hover {{
    background: linear-gradient(180deg, #1d6272 0%, #103b45 100%);
    color: #ffffff;
  }}
  .encarta-btn:active, .encarta-btn.active {{
    background: linear-gradient(180deg, #092228 0%, #144652 100%);
    border-top-color: #06191d;
    border-left-color: #06191d;
    border-bottom-color: #45a4b9;
    border-right-color: #45a4b9;
    box-shadow: inset 1px 1px 2px rgba(0,0,0,0.8);
    transform: translateY(1px);
  }}

  /* Gold Ribbon Badges */
  .gold-badge {{
    background: linear-gradient(180deg, #f7d788 0%, #c89532 100%);
    color: #382404;
    border: 1px solid #ffd978;
    text-shadow: 0 1px 0 rgba(255,255,255,0.4);
    box-shadow: 0 2px 4px rgba(0,0,0,0.4);
  }}

  /* Encarta Window Box */
  .encarta-window {{
    background: var(--bg-surface);
    border: 2px solid #236574;
    box-shadow: 0 8px 24px rgba(0,0,0,0.6), inset 1px 1px 0 rgba(255,255,255,0.1);
  }}

  .window-header {{
    background: linear-gradient(90deg, #0d3842 0%, #185c6c 50%, #0d3842 100%);
    border-bottom: 2px solid var(--border-gold);
    color: #ffd978;
    font-weight: 700;
    letter-spacing: 0.5px;
  }}

  /* Custom Scrollbars */
  ::-webkit-scrollbar {{ width: 8px; height: 8px; }}
  ::-webkit-scrollbar-track {{ background: #071c21; }}
  ::-webkit-scrollbar-thumb {{ background: #1c5d6c; border-radius: 4px; }}
  ::-webkit-scrollbar-thumb:hover {{ background: #267c91; }}

  /* Animation spinning disc */
  @keyframes spinDisc {{
    from {{ transform: rotate(0deg); }}
    to {{ transform: rotate(360deg); }}
  }}
  .spinning-cd {{
    animation: spinDisc 6s linear infinite;
  }}
</style>
</head>
<body class="min-h-screen flex flex-col">

<!-- CRT Scanline Filter -->
<div id="crtOverlay" class="crt-overlay crt-off"></div>

<!-- Top Title Bar (Classic Multimedia CD-ROM Chrome) -->
<header class="bg-[#041215] border-b-2 border-[#164e5b] px-4 py-2 flex flex-wrap items-center justify-between shadow-md">
  <div class="flex items-center space-x-3">
    <!-- Spinning Disc Icon -->
    <div class="relative w-8 h-8 rounded-full border-2 border-[#dfb15b] flex items-center justify-center bg-[#0d3842] shadow-inner">
      <svg class="spinning-cd w-6 h-6 text-[#dfb15b]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="12" cy="12" r="10"></circle>
        <circle cx="12" cy="12" r="3"></circle>
        <path d="M12 2a10 10 0 0 1 10 10"></path>
      </svg>
    </div>
    <div>
      <div class="flex items-center space-x-2">
        <span class="gold-badge text-[11px] font-black uppercase px-2 py-0.5 rounded tracking-wider">ENCARTA '95</span>
        <h1 class="text-lg font-black text-[#f8fafc] tracking-wide font-serif">ELECTROMECHANICA</h1>
      </div>
      <p class="text-xs text-[#67e8f9] font-mono tracking-tight">The Interactive Multimedia Bible of Salvage &amp; Hardware Hacking</p>
    </div>
  </div>

  <!-- Multimedia Utility Buttons -->
  <div class="flex items-center space-x-2 mt-2 sm:mt-0">
    <button onclick="AudioEngine.toggle(); this.classList.toggle('active')" class="encarta-btn px-3 py-1 rounded text-xs flex items-center space-x-1.5" title="Toggle 90s Sound Effects">
      <span id="soundIcon">🔊</span>
      <span id="soundLabel" class="font-mono">SFX: ON</span>
    </button>
    <button onclick="toggleCRT(); this.classList.toggle('active')" class="encarta-btn px-3 py-1 rounded text-xs flex items-center space-x-1.5" title="Toggle Retro CRT Monitor Filter">
      <span>📺</span>
      <span class="font-mono">CRT: OFF</span>
    </button>
    <button onclick="randomArticle()" class="encarta-btn px-3 py-1 rounded text-xs flex items-center space-x-1.5" title="Jump to Random Donor or Blueprint">
      <span>🎲</span>
      <span class="font-mono">Random Discovery</span>
    </button>
    <div class="bg-[#030d0f] border border-[#164e5b] px-3 py-1 rounded text-xs font-mono text-[#38bdf8] hidden md:block">
      DISK BUFFER: <span class="text-emerald-400">100% READY</span>
    </div>
  </div>
</header>

<!-- Main Navigation Ribbon (Encarta Tabs) -->
<nav class="bg-[#092228] border-b border-[#1b6170] px-3 py-2 flex flex-wrap gap-2 shadow-inner">
  <button onclick="switchTab('atlas')" id="tab-atlas" class="encarta-btn active px-4 py-1.5 rounded text-xs font-bold flex items-center space-x-2">
    <span>🏛️</span>
    <span>Atlas of Scrap</span>
  </button>
  <button onclick="switchTab('lab')" id="tab-lab" class="encarta-btn px-4 py-1.5 rounded text-xs font-bold flex items-center space-x-2">
    <span>🔬</span>
    <span>InterActivities Lab</span>
    <span class="bg-amber-500/20 text-amber-300 text-[10px] px-1.5 rounded border border-amber-500/40">5 Physics Sims</span>
  </button>
  <button onclick="switchTab('xray')" id="tab-xray" class="encarta-btn px-4 py-1.5 rounded text-xs font-bold flex items-center space-x-2">
    <span>🔍</span>
    <span>Appliance X-Ray</span>
    <span class="bg-cyan-500/20 text-cyan-300 text-[10px] px-1.5 rounded border border-cyan-500/40">Teardowns</span>
  </button>
  <button onclick="switchTab('blueprints')" id="tab-blueprints" class="encarta-btn px-4 py-1.5 rounded text-xs font-bold flex items-center space-x-2">
    <span>📐</span>
    <span>Blueprint Studio</span>
    <span class="bg-emerald-500/20 text-emerald-300 text-[10px] px-1.5 rounded border border-emerald-500/40">50 Blueprints</span>
  </button>
  <button onclick="switchTab('mindmaze')" id="tab-mindmaze" class="encarta-btn px-4 py-1.5 rounded text-xs font-bold flex items-center space-x-2">
    <span>🧠</span>
    <span>MindMaze '95</span>
    <span class="bg-purple-500/20 text-purple-300 text-[10px] px-1.5 rounded border border-purple-500/40">Dungeon Quiz</span>
  </button>
  <div class="flex-1 flex justify-end">
    <div class="relative w-full max-w-xs">
      <input type="text" id="omniSearch" onkeyup="handleSearch(this.value)" placeholder="🔎 Pinpointer Omnisearch..." 
             class="w-full bg-[#05171b] border border-[#2a7c8e] rounded px-3 py-1 text-xs text-slate-100 placeholder-slate-400 focus:outline-none focus:border-amber-400 font-mono">
      <div id="searchDropdown" class="absolute left-0 right-0 top-8 bg-[#071c21] border border-[#2a7c8e] rounded shadow-2xl z-50 max-h-60 overflow-y-auto hidden"></div>
    </div>
  </div>
</nav>

<!-- Main Workspace Body -->
<main class="flex-1 p-4 max-w-7xl mx-auto w-full">

  <!-- ================= TAB 1: ATLAS OF SCRAP ================= -->
  <section id="view-atlas" class="space-y-6">
    <!-- Category Hero Header -->
    <div class="encarta-window rounded-lg overflow-hidden p-5 flex flex-col md:flex-row items-center justify-between gap-4">
      <div class="space-y-1">
        <div class="flex items-center space-x-2">
          <span class="text-2xl">🗺️</span>
          <h2 class="text-xl font-black text-amber-300 font-serif">The Atlas of Electromechanical Scrap</h2>
        </div>
        <p class="text-xs text-slate-300 max-w-2xl">
          Explore the urban mining ecosystem across 14 volumes. Select a donor appliance to unlock diagnostic wire trees, dangerous hazard warnings, harvestable sub-assemblies, and direct project conversion recipes.
        </p>
      </div>
      <!-- Filter Badges -->
      <div class="flex flex-wrap gap-1.5 justify-end" id="categoryFilterPills">
        <!-- populated by JS -->
      </div>
    </div>

    <!-- Donors Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4" id="donorsGrid">
      <!-- populated by JS -->
    </div>
  </section>

  <!-- ================= TAB 2: INTERACTIVITIES LAB ================= -->
  <section id="view-lab" class="space-y-6 hidden">
    <!-- Sub-tab selector -->
    <div class="flex flex-wrap gap-2 border-b border-[#1b6170] pb-2">
      <button onclick="switchLabSim('balancer')" id="btn-sim-balancer" class="encarta-btn active px-3 py-1 rounded text-xs font-semibold">1. LeBlanc Rotordynamic Balancer</button>
      <button onclick="switchLabSim('sparks')" id="btn-sim-sparks" class="encarta-btn px-3 py-1 rounded text-xs font-semibold">2. Angle Grinder Spark Metallurgy</button>
      <button onclick="switchLabSim('wizard')" id="btn-sim-wizard" class="encarta-btn px-3 py-1 rounded text-xs font-semibold">3. Motor Wire Diagnostic Wizard</button>
      <button onclick="switchLabSim('geneva')" id="btn-sim-geneva" class="encarta-btn px-3 py-1 rounded text-xs font-semibold">4. Geneva &amp; Kinematic Linkage</button>
      <button onclick="switchLabSim('spotweld')" id="btn-sim-spotweld" class="encarta-btn px-3 py-1 rounded text-xs font-semibold">5. CD Pulse Spot Weld Calculator</button>
    </div>

    <!-- SIM 1: LeBlanc Ball Balancer -->
    <div id="sim-balancer" class="encarta-window rounded-lg overflow-hidden">
      <div class="window-header px-4 py-2 flex items-center justify-between text-xs">
        <span class="flex items-center space-x-2">
          <span>🔄</span>
          <span>PHYSICS SIMULATOR: LeBlanc Supercritical Dynamic Ball Balancer (Washing Machine Rotordynamics)</span>
        </span>
        <span class="font-mono text-emerald-400">STATUS: ACTIVE</span>
      </div>
      <div class="p-5 grid grid-cols-1 lg:grid-cols-3 gap-6">
        <!-- Canvas Visualizer -->
        <div class="lg:col-span-2 flex flex-col items-center justify-center bg-[#041215] border border-[#164e5b] rounded p-4 relative">
          <canvas id="balancerCanvas" width="460" height="380" class="max-w-full"></canvas>
          <div id="balancerAlert" class="mt-2 text-xs font-mono px-3 py-1 rounded border">
            <!-- Alert updated dynamically -->
          </div>
        </div>
        <!-- Controls & Physics Readout -->
        <div class="space-y-4">
          <div class="bg-[#092228] p-4 rounded border border-[#1b6170] space-y-3">
            <h4 class="text-xs font-bold text-amber-300 uppercase tracking-wider">Dynamic Parameters</h4>
            <div>
              <div class="flex justify-between text-xs mb-1 font-mono">
                <span>Rotor Speed (RPM):</span>
                <span id="rpmDisplay" class="text-cyan-300 font-bold">600 RPM</span>
              </div>
              <input type="range" id="rpmSlider" min="0" max="3600" step="50" value="600" oninput="updateBalancerRPM(this.value)" class="w-full accent-cyan-400">
              <div class="flex justify-between text-[10px] text-slate-400 font-mono mt-1">
                <span>0 RPM (Stopped)</span>
                <span class="text-amber-400">Resonance (1,200)</span>
                <span>3,600 RPM</span>
              </div>
            </div>

            <div class="pt-2 border-t border-[#164e5b] flex gap-2">
              <button onclick="toggleUnbalance()" id="btnUnbalance" class="encarta-btn flex-1 py-1.5 rounded text-xs font-semibold">
                Toggle Heavy Spot
              </button>
              <button onclick="resetBalls()" class="encarta-btn py-1.5 px-3 rounded text-xs font-semibold">
                Reset Balls
              </button>
            </div>
          </div>

          <!-- Theory Card -->
          <div class="bg-[#05171b] p-4 rounded border border-[#164e5b] text-xs space-y-2">
            <h5 class="font-bold text-cyan-300 font-mono">&bull; The Supercritical Phase Inversion Law</h5>
            <p class="text-slate-300 text-[11px] leading-relaxed">
              When &omega; &lt; &omega;<sub>n</sub> (subcritical), the shaft deflects in-phase with the unbalance mass, clustering loose balls near the heavy spot and worsening vibrations.
            </p>
            <p class="text-slate-300 text-[11px] leading-relaxed">
              Once accelerating past resonance (&omega; &gt; &radic;2 &omega;<sub>n</sub>), a <strong>180&deg; phase shift occurs</strong>: the rotor orbits about its true center of mass. Centrifugal force flings the steel balls diametrically opposite to the heavy spot, restoring glass-smooth operation automatically!
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- SIM 2: Angle Grinder Spark Metallurgy -->
    <div id="sim-sparks" class="encarta-window rounded-lg overflow-hidden hidden">
      <div class="window-header px-4 py-2 flex items-center justify-between text-xs">
        <span class="flex items-center space-x-2">
          <span>✨</span>
          <span>PHYSICS SIMULATOR: Scrap Steel Spark Testing Chamber (Bench Metallurgy)</span>
        </span>
        <span class="font-mono text-amber-400">GRINDER: 10,000 RPM</span>
      </div>
      <div class="p-5 grid grid-cols-1 lg:grid-cols-3 gap-6">
        <!-- Canvas Stage -->
        <div class="lg:col-span-2 flex flex-col items-center justify-center bg-[#02090b] border border-[#164e5b] rounded p-4 relative">
          <canvas id="sparksCanvas" width="500" height="340" class="max-w-full"></canvas>
          <div class="w-full flex justify-between items-center mt-3 pt-2 border-t border-[#164e5b]">
            <button id="btnGrind" onmousedown="startGrinding()" onmouseup="stopGrinding()" onmouseleave="stopGrinding()" 
                    class="encarta-btn px-6 py-2 rounded text-xs font-bold text-amber-300 border-amber-500/50 flex items-center space-x-2">
              <span>⚡</span>
              <span>HOLD TO CONTACT WORKPIECE</span>
            </button>
            <div id="sparkStatus" class="text-xs font-mono text-slate-400">Wheel idling. Press and hold button.</div>
          </div>
        </div>

        <!-- Metallurgy Selector & Card -->
        <div class="space-y-4">
          <div class="bg-[#092228] p-4 rounded border border-[#1b6170] space-y-3">
            <h4 class="text-xs font-bold text-amber-300 uppercase tracking-wider">Select Mystery Steel Sample</h4>
            <div class="grid grid-cols-1 gap-1.5" id="steelSampleButtons">
              <!-- populated by JS -->
            </div>
          </div>

          <div id="steelReadoutCard" class="bg-[#05171b] p-4 rounded border border-[#164e5b] text-xs space-y-2">
            <!-- populated by JS -->
          </div>
        </div>
      </div>
    </div>

    <!-- SIM 3: Motor Diagnostic Wizard -->
    <div id="sim-wizard" class="encarta-window rounded-lg overflow-hidden hidden">
      <div class="window-header px-4 py-2 flex items-center justify-between text-xs">
        <span class="flex items-center space-x-2">
          <span>⚡</span>
          <span>DIAGNOSTIC WIZARD: Motor Identification by Wire Count &amp; Bench Triage</span>
        </span>
        <span class="font-mono text-cyan-300">INTERACTIVE TREE</span>
      </div>
      <div class="p-6 max-w-3xl mx-auto space-y-6">
        <div class="text-center space-y-2">
          <h3 class="text-lg font-bold text-amber-300 font-serif">How Many Wires Exit the Motor Chassis?</h3>
          <p class="text-xs text-slate-300">Select the wire grouping to begin the step-by-step bench identification tree.</p>
        </div>

        <!-- Wire Count Buttons -->
        <div class="flex flex-wrap justify-center gap-3">
          <button onclick="runWireTree(2)" class="encarta-btn px-4 py-2 rounded text-xs font-bold">2 Wires (DC / Universal)</button>
          <button onclick="runWireTree(3)" class="encarta-btn px-4 py-2 rounded text-xs font-bold">3 Wires (BLDC / AC Ind.)</button>
          <button onclick="runWireTree(4)" class="encarta-btn px-4 py-2 rounded text-xs font-bold">4 Wires (Bipolar Stepper)</button>
          <button onclick="runWireTree(5)" class="encarta-btn px-4 py-2 rounded text-xs font-bold">5 or 6 Wires (Unipolar)</button>
          <button onclick="runWireTree(8)" class="encarta-btn px-4 py-2 rounded text-xs font-bold">8+ Wires (BLDC + Hall)</button>
        </div>

        <!-- Wizard Card Output -->
        <div id="wizardResult" class="bg-[#092228] p-5 rounded border border-[#1b6170] space-y-4">
          <div class="text-xs text-slate-400 font-mono text-center">Click a wire count above to inspect diagnostic paths.</div>
        </div>
      </div>
    </div>

    <!-- SIM 4: Geneva Mechanism Kinematics -->
    <div id="sim-geneva" class="encarta-window rounded-lg overflow-hidden hidden">
      <div class="window-header px-4 py-2 flex items-center justify-between text-xs">
        <span class="flex items-center space-x-2">
          <span>⚙️</span>
          <span>KINEMATIC SIMULATOR: Maltese Cross Geneva Indexing Drive &amp; Scotch Yoke</span>
        </span>
        <span class="font-mono text-purple-300">INTERMITTENT MOTION</span>
      </div>
      <div class="p-5 grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div class="lg:col-span-2 flex flex-col items-center justify-center bg-[#02090b] border border-[#164e5b] rounded p-4">
          <canvas id="genevaCanvas" width="460" height="340" class="max-w-full"></canvas>
        </div>
        <div class="space-y-4">
          <div class="bg-[#092228] p-4 rounded border border-[#1b6170] space-y-3">
            <h4 class="text-xs font-bold text-amber-300 uppercase tracking-wider">Kinematic Mode</h4>
            <div class="flex gap-2">
              <button onclick="setKinematicMode('geneva')" id="btnModeGeneva" class="encarta-btn active flex-1 py-1.5 rounded text-xs font-semibold">Geneva 4-Slot</button>
              <button onclick="setKinematicMode('scotchyoke')" id="btnModeYoke" class="encarta-btn flex-1 py-1.5 rounded text-xs font-semibold">Scotch Yoke</button>
            </div>
            <div>
              <div class="flex justify-between text-xs mb-1 font-mono">
                <span>Drive Speed:</span>
                <span id="genevaSpeedText" class="text-cyan-300">30 RPM</span>
              </div>
              <input type="range" id="genevaSpeed" min="5" max="100" value="30" oninput="updateGenevaSpeed(this.value)" class="w-full accent-cyan-400">
            </div>
          </div>
          <div class="bg-[#05171b] p-4 rounded border border-[#164e5b] text-xs space-y-2">
            <h5 class="font-bold text-amber-300 font-mono">&bull; Pure Mechanical Logic</h5>
            <p class="text-slate-300 text-[11px] leading-relaxed">
              The Geneva drive converts continuous rotation into intermittent 90&deg; indexed steps with automatic mechanical locking during dwell. Found in vintage movie projectors, tool changers, and automated assembly indexers.
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- SIM 5: CD Spot Weld Pulse Calculator -->
    <div id="sim-spotweld" class="encarta-window rounded-lg overflow-hidden hidden">
      <div class="window-header px-4 py-2 flex items-center justify-between text-xs">
        <span class="flex items-center space-x-2">
          <span>💥</span>
          <span>ELECTRICAL SIMULATOR: Capacitive-Discharge (CD) Spot Welder Pulse &amp; Joules Calculator</span>
        </span>
        <span class="font-mono text-emerald-300">ENERGY STORAGE</span>
      </div>
      <div class="p-5 grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div class="lg:col-span-2 flex flex-col items-center justify-center bg-[#02090b] border border-[#164e5b] rounded p-4">
          <canvas id="pulseCanvas" width="480" height="300" class="max-w-full"></canvas>
          <div id="pulseMetrics" class="w-full grid grid-cols-3 gap-2 mt-4 text-center font-mono text-xs">
            <!-- populated by JS -->
          </div>
        </div>
        <div class="space-y-4">
          <div class="bg-[#092228] p-4 rounded border border-[#1b6170] space-y-3">
            <h4 class="text-xs font-bold text-amber-300 uppercase tracking-wider">Capacitor Bank Controls</h4>
            <div>
              <div class="flex justify-between text-xs mb-1 font-mono">
                <span>Bank Capacitance (Farads):</span>
                <span id="capDisplay" class="text-cyan-300 font-bold">1,500 F</span>
              </div>
              <input type="range" id="capSlider" min="100" max="3000" step="50" value="1500" oninput="updatePulseSim()" class="w-full accent-cyan-400">
            </div>
            <div>
              <div class="flex justify-between text-xs mb-1 font-mono">
                <span>Charge Voltage (V):</span>
                <span id="voltDisplay" class="text-cyan-300 font-bold">5.4 V</span>
              </div>
              <input type="range" id="voltSlider" min="2.5" max="8.0" step="0.1" value="5.4" oninput="updatePulseSim()" class="w-full accent-cyan-400">
            </div>
            <div>
              <div class="flex justify-between text-xs mb-1 font-mono">
                <span>Pulse Duration (ms):</span>
                <span id="pulseDisplay" class="text-cyan-300 font-bold">2.5 ms</span>
              </div>
              <input type="range" id="pulseSlider" min="0.5" max="8.0" step="0.1" value="2.5" oninput="updatePulseSim()" class="w-full accent-cyan-400">
            </div>
          </div>
          <div id="weldVerdictCard" class="bg-[#05171b] p-4 rounded border border-[#164e5b] text-xs space-y-1 font-mono">
            <!-- populated by JS -->
          </div>
        </div>
      </div>
    </div>

  </section>

  <!-- ================= TAB 3: APPLIANCE X-RAY ================= -->
  <section id="view-xray" class="space-y-6 hidden">
    <div class="encarta-window rounded-lg overflow-hidden p-5 flex flex-wrap items-center justify-between gap-4">
      <div class="space-y-1">
        <h2 class="text-lg font-black text-amber-300 font-serif flex items-center space-x-2">
          <span>🔍</span>
          <span>Interactive Appliance X-Ray Cutaways</span>
        </h2>
        <p class="text-xs text-slate-300">Hover and click highlighted hotspots on donor anatomy to inspect internal electromechanics, extraction protocols, and hazard ratings.</p>
      </div>
      <!-- Appliance Selector -->
      <div class="flex flex-wrap gap-2">
        <button onclick="loadXRay('microwave')" id="btnXRay-microwave" class="encarta-btn active px-3 py-1.5 rounded text-xs font-semibold">Microwave Oven</button>
        <button onclick="loadXRay('washer')" id="btnXRay-washer" class="encarta-btn px-3 py-1.5 rounded text-xs font-semibold">Direct-Drive Washer</button>
        <button onclick="loadXRay('treadmill')" id="btnXRay-treadmill" class="encarta-btn px-3 py-1.5 rounded text-xs font-semibold">Exercise Treadmill</button>
        <button onclick="loadXRay('abspump')" id="btnXRay-abspump" class="encarta-btn px-3 py-1.5 rounded text-xs font-semibold">ABS Brake Unit</button>
        <button onclick="loadXRay('printer')" id="btnXRay-printer" class="encarta-btn px-3 py-1.5 rounded text-xs font-semibold">Laser Printer</button>
      </div>
    </div>

    <!-- X-Ray Interactive Display -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <div class="lg:col-span-2 encarta-window rounded-lg p-5 flex items-center justify-center bg-[#02090b] relative min-h-[380px]" id="xrayCanvasContainer">
        <!-- SVG Rendered Here -->
      </div>
      <div class="encarta-window rounded-lg p-5 space-y-4" id="xrayDetailCard">
        <div class="text-xs text-slate-400 font-mono text-center pt-10">Select or hover over any glowing component hotspot on the X-Ray schematic.</div>
      </div>
    </div>
  </section>

  <!-- ================= TAB 4: BLUEPRINT STUDIO ================= -->
  <section id="view-blueprints" class="space-y-6 hidden">
    <div class="encarta-window rounded-lg overflow-hidden p-5 flex flex-wrap items-center justify-between gap-4">
      <div>
        <h2 class="text-lg font-black text-amber-300 font-serif flex items-center space-x-2">
          <span>📐</span>
          <span>The 21 Frontier Engineering Blueprints</span>
        </h2>
        <p class="text-xs text-slate-300">Exhaustive step-by-step schematics, bills of materials, and operational SOPs for complete machines built from scrap.</p>
      </div>
      <!-- Difficulty Filters -->
      <div class="flex gap-2">
        <button onclick="filterBlueprints('all')" class="encarta-btn active px-3 py-1 rounded text-xs font-semibold bp-filter-btn">All (21)</button>
        <button onclick="filterBlueprints('Novice')" class="encarta-btn px-3 py-1 rounded text-xs font-semibold bp-filter-btn">Novice</button>
        <button onclick="filterBlueprints('Intermediate')" class="encarta-btn px-3 py-1 rounded text-xs font-semibold bp-filter-btn">Intermediate</button>
        <button onclick="filterBlueprints('Advanced')" class="encarta-btn px-3 py-1 rounded text-xs font-semibold bp-filter-btn">Advanced</button>
        <button onclick="filterBlueprints('Master')" class="encarta-btn px-3 py-1 rounded text-xs font-semibold bp-filter-btn">Master</button>
      </div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4" id="blueprintsGrid">
      <!-- populated by JS -->
    </div>
  </section>

  <!-- ================= TAB 5: MINDMAZE '95 ================= -->
  <section id="view-mindmaze" class="space-y-6 hidden">
    <div class="encarta-window rounded-lg overflow-hidden max-w-3xl mx-auto">
      <div class="window-header px-4 py-2 flex items-center justify-between text-xs">
        <span class="flex items-center space-x-2">
          <span>🏰</span>
          <span>MINDMAZE '95: Escape the Abandoned Megafactory</span>
        </span>
        <div class="flex items-center space-x-4 font-mono">
          <span>ROOM: <span id="mazeRoomNumber" class="text-amber-300 font-bold">1 / 5</span></span>
          <span>SCORE: <span id="mazeScore" class="text-emerald-400 font-bold">0 PTS</span></span>
        </div>
      </div>

      <div class="p-6 space-y-6">
        <!-- Room Visualizer -->
        <div class="bg-[#020b0d] border border-[#164e5b] rounded-lg p-5 text-center relative overflow-hidden">
          <div class="text-4xl mb-2" id="mazeRoomIcon">🏭</div>
          <h3 class="text-base font-bold text-amber-300 font-serif" id="mazeRoomTitle">Room 1: The Scrap Loading Dock</h3>
          <p class="text-xs text-slate-300 mt-1 max-w-md mx-auto" id="mazeRoomDesc">
            Heavy steel doors bar your path. A triage puzzle lock requires solving the motor mystery below to energize the pneumatic door actuators.
          </p>
        </div>

        <!-- Question Box -->
        <div class="bg-[#092228] p-5 rounded-lg border border-[#1b6170] space-y-4">
          <div class="text-xs font-bold text-cyan-300 font-mono flex items-center space-x-1.5">
            <span>❓</span>
            <span id="mazeQuestionText">Loading Question...</span>
          </div>

          <div class="grid grid-cols-1 gap-2.5" id="mazeOptionsContainer">
            <!-- Options populated by JS -->
          </div>

          <div id="mazeFeedback" class="hidden text-xs p-3 rounded font-mono"></div>
        </div>

        <!-- Action / Advance -->
        <div class="flex justify-between items-center pt-2">
          <button onclick="resetMaze()" class="encarta-btn px-4 py-1.5 rounded text-xs font-semibold">Restart Maze</button>
          <button id="btnNextRoom" onclick="advanceMazeRoom()" class="encarta-btn px-6 py-1.5 rounded text-xs font-bold text-amber-300 hidden">
            Advance to Next Chamber &rarr;
          </button>
        </div>
      </div>
    </div>
  </section>

</main>

<!-- Modal Viewer for Blueprint Dossiers -->
<div id="blueprintModal" class="fixed inset-0 bg-black/80 flex items-center justify-center p-4 z-50 hidden">
  <div class="encarta-window rounded-lg max-w-3xl w-full max-h-[90vh] flex flex-col overflow-hidden">
    <div class="window-header px-4 py-2 flex items-center justify-between text-xs">
      <span id="modalHeaderTitle" class="font-mono">BLUEPRINT DOSSIER</span>
      <button onclick="closeBlueprintModal()" class="text-amber-300 hover:text-white font-bold px-2">&times;</button>
    </div>
    <div class="p-6 overflow-y-auto space-y-5 text-xs text-slate-200" id="modalBody">
      <!-- populated dynamically -->
    </div>
  </div>
</div>

<footer class="bg-[#041215] border-t border-[#164e5b] py-3 text-center text-[11px] text-slate-400 font-mono">
  The Maker's Bible of Electromechanical Salvage &amp; Repurposing &bull; Encarta '95 Multimedia Edition &bull; Open Source Maker Lore
</footer>

<!-- Application Logic -->
<script>
// Load Databases
const DONORS = {donors_json};
const BLUEPRINTS = {blueprints_json};
const QUESTIONS = {questions_json};
const CATEGORIES = {categories_json};

// Web Audio API Sound Synthesizer (Zero External Dependencies)
const AudioEngine = {{
  ctx: null,
  muted: false,
  init() {{
    if (!this.ctx) {{
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      this.ctx = new AudioCtx();
    }}
  }},
  toggle() {{
    this.muted = !this.muted;
    document.getElementById('soundIcon').innerText = this.muted ? '🔇' : '🔊';
    document.getElementById('soundLabel').innerText = this.muted ? 'SFX: OFF' : 'SFX: ON';
    if (!this.muted) this.chime();
  }},
  click() {{
    if (this.muted) return;
    this.init();
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'triangle';
    osc.frequency.setValueAtTime(800, this.ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(140, this.ctx.currentTime + 0.04);
    gain.gain.setValueAtTime(0.2, this.ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, this.ctx.currentTime + 0.04);
    osc.connect(gain);
    gain.connect(this.ctx.destination);
    osc.start();
    osc.stop(this.ctx.currentTime + 0.04);
  }},
  chime() {{
    if (this.muted) return;
    this.init();
    const now = this.ctx.currentTime;
    [523.25, 659.25, 783.99, 1046.50].forEach((freq, idx) => {{
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(freq, now + idx * 0.05);
      gain.gain.setValueAtTime(0.12, now + idx * 0.05);
      gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.05 + 0.35);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start(now + idx * 0.05);
      osc.stop(now + idx * 0.05 + 0.35);
    }});
  }},
  buzz() {{
    if (this.muted) return;
    this.init();
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'sawtooth';
    osc.frequency.setValueAtTime(110, this.ctx.currentTime);
    gain.gain.setValueAtTime(0.25, this.ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, this.ctx.currentTime + 0.25);
    osc.connect(gain);
    gain.connect(this.ctx.destination);
    osc.start();
    osc.stop(this.ctx.currentTime + 0.25);
  }},
  victory() {{
    if (this.muted) return;
    this.init();
    const now = this.ctx.currentTime;
    [440, 554.37, 659.25, 880].forEach((freq, i) => {{
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(freq, now + i * 0.1);
      gain.gain.setValueAtTime(0.2, now + i * 0.1);
      gain.gain.exponentialRampToValueAtTime(0.01, now + i * 0.1 + 0.4);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start(now + i * 0.1);
      osc.stop(now + i * 0.1 + 0.4);
    }});
  }}
}};

// Tab Navigation
function switchTab(tabId) {{
  AudioEngine.click();
  document.querySelectorAll('nav button').forEach(b => b.classList.remove('active'));
  document.getElementById('tab-' + tabId).classList.add('active');

  ['atlas', 'lab', 'xray', 'blueprints', 'mindmaze'].forEach(t => {{
    const el = document.getElementById('view-' + t);
    if (el) el.classList.toggle('hidden', t !== tabId);
  }});

  if (tabId === 'lab') startBalancerSim();
  if (tabId === 'xray') loadXRay('microwave');
  window.scrollTo({{ top: 0, behavior: 'smooth' }});
}}

// CRT Toggle
function toggleCRT() {{
  AudioEngine.click();
  const overlay = document.getElementById('crtOverlay');
  overlay.classList.toggle('crt-off');
}}

// Random Article Discovery
function randomArticle() {{
  AudioEngine.chime();
  if (Math.random() > 0.5) {{
    const bp = BLUEPRINTS[Math.floor(Math.random() * BLUEPRINTS.length)];
    switchTab('blueprints');
    openBlueprintModal(bp.num);
  }} else {{
    const donor = DONORS[Math.floor(Math.random() * DONORS.length)];
    switchTab('atlas');
    const el = document.getElementById('donor-' + donor.id);
    if (el) {{
      el.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
      el.classList.add('ring-2', 'ring-amber-400');
      setTimeout(() => el.classList.remove('ring-2', 'ring-amber-400'), 2500);
    }}
  }}
}}

// Populate Atlas
function initAtlas() {{
  const pills = document.getElementById('categoryFilterPills');
  pills.innerHTML = '<button onclick="filterAtlas(\\'all\\')" class="encarta-btn active px-2.5 py-1 rounded text-[11px] font-semibold atlas-pill">All</button>';
  CATEGORIES.forEach(c => {{
    pills.innerHTML += `<button onclick="filterAtlas('${{c.id}}')" class="encarta-btn px-2.5 py-1 rounded text-[11px] font-semibold atlas-pill">${{c.icon}} ${{c.name.split(' ')[0]}}</button>`;
  }});

  renderDonors(DONORS);
}}

function renderDonors(list) {{
  const grid = document.getElementById('donorsGrid');
  grid.innerHTML = '';
  list.forEach(d => {{
    grid.innerHTML += `
      <div id="donor-${{d.id}}" class="encarta-window rounded p-4 flex flex-col justify-between space-y-3 hover:border-amber-400 transition-all">
        <div class="space-y-2">
          <div class="flex items-start justify-between">
            <h3 class="font-bold text-amber-300 text-sm font-serif">${{d.name}}</h3>
            <span class="text-[10px] font-bold px-2 py-0.5 rounded font-mono" style="background:${{d.dangerColor}}22; color:${{d.dangerColor}}; border:1px solid ${{d.dangerColor}}44">
              ${{d.danger}}
            </span>
          </div>
          <div>
            <div class="text-[11px] font-bold text-cyan-300 font-mono mb-1">Harvestable Goldmine:</div>
            <ul class="text-[11px] text-slate-300 space-y-0.5 list-disc list-inside">
              ${{d.harvest.map(h => `<li>${{h}}</li>`).join('')}}
            </ul>
          </div>
          <div class="text-[11px] text-slate-300 pt-1 border-t border-[#164e5b]">
            <strong class="text-amber-200">Best Repurposing:</strong> ${{d.bestFor}}
          </div>
        </div>
        <div class="bg-[#05171b] p-2 rounded border border-[#164e5b] text-[10px] font-mono text-emerald-300">
          <strong>Triage:</strong> ${{d.triage}}
        </div>
      </div>
    `;
  }});
}}

function filterAtlas(catId) {{
  AudioEngine.click();
  document.querySelectorAll('.atlas-pill').forEach(p => p.classList.remove('active'));
  event.target.classList.add('active');
  if (catId === 'all') renderDonors(DONORS);
  else renderDonors(DONORS.filter(d => d.cat === catId));
}}

// ================= SIM 1: LEBLANC BALANCER =================
let balancerRPM = 600;
let balancerHasUnbalance = true;
let balancerAngle = 0;
let balancerBalls = [0.2, 0.4, 0.6, 0.8]; // Ball angular positions in radians
let balancerAnimId = null;

function startBalancerSim() {{
  const canvas = document.getElementById('balancerCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  function render() {{
    const w = canvas.width, h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const cx = w / 2, cy = h / 2;
    const R_outer = 140;
    const R_inner = 115;
    const omega = balancerRPM * (Math.PI / 30); // rad/s
    const dt = 0.016;

    balancerAngle += omega * dt;

    // Resonant frequency threshold = 1200 RPM
    const isSupercritical = balancerRPM > 1200;
    const unbalanceTarget = isSupercritical ? Math.PI : 0; // 180 deg phase shift!

    // Shift balls dynamically
    balancerBalls = balancerBalls.map(angle => {{
      const target = isSupercritical ? (Math.PI + (Math.random() - 0.5) * 0.4) : (0 + (Math.random() - 0.5) * 0.4);
      return angle + (target - angle) * 0.05;
    }});

    // Vibration shake
    let shakeX = 0, shakeY = 0;
    if (balancerHasUnbalance) {{
      const vibeAmp = isSupercritical ? Math.max(1, 14 - (balancerRPM - 1200) / 180) : Math.min(18, (balancerRPM / 1200) * 16);
      shakeX = Math.cos(balancerAngle) * vibeAmp;
      shakeY = Math.sin(balancerAngle) * vibeAmp;
    }}

    ctx.save();
    ctx.translate(cx + shakeX, cy + shakeY);

    // Annular Balance Ring Outer Wall
    ctx.beginPath();
    ctx.arc(0, 0, R_outer, 0, Math.PI * 2);
    ctx.strokeStyle = '#2a7c8e';
    ctx.lineWidth = 6;
    ctx.stroke();

    // Damping Fluid Cavity
    ctx.beginPath();
    ctx.arc(0, 0, R_outer - 3, 0, Math.PI * 2);
    ctx.arc(0, 0, R_inner + 3, 0, Math.PI * 2, true);
    ctx.fillStyle = 'rgba(6, 182, 212, 0.15)';
    ctx.fill();

    // Inner Hub Wall
    ctx.beginPath();
    ctx.arc(0, 0, R_inner, 0, Math.PI * 2);
    ctx.strokeStyle = '#1b6170';
    ctx.lineWidth = 4;
    ctx.stroke();

    // Heavy Unbalance Spot
    if (balancerHasUnbalance) {{
      const hx = Math.cos(balancerAngle) * (R_inner - 20);
      const hy = Math.sin(balancerAngle) * (R_inner - 20);
      ctx.beginPath();
      ctx.arc(hx, hy, 14, 0, Math.PI * 2);
      ctx.fillStyle = '#ef4444';
      ctx.fill();
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = 2;
      ctx.stroke();
      ctx.fillStyle = '#ffffff';
      ctx.font = '10px monospace';
      ctx.fillText('HEAVY', hx - 16, hy - 18);
    }}

    // Chrome Steel Balls
    balancerBalls.forEach((bOffset, idx) => {{
      const bAngle = balancerAngle + bOffset;
      const bx = Math.cos(bAngle) * ((R_outer + R_inner) / 2);
      const by = Math.sin(bAngle) * ((R_outer + R_inner) / 2);

      const grad = ctx.createRadialGradient(bx - 3, by - 3, 1, bx, by, 10);
      grad.addColorStop(0, '#ffffff');
      grad.addColorStop(0.5, '#cbd5e1');
      grad.addColorStop(1, '#334155');

      ctx.beginPath();
      ctx.arc(bx, by, 10, 0, Math.PI * 2);
      ctx.fillStyle = grad;
      ctx.fill();
      ctx.strokeStyle = '#0f172a';
      ctx.lineWidth = 1;
      ctx.stroke();
    }});

    // Center Spindle
    ctx.beginPath();
    ctx.arc(0, 0, 16, 0, Math.PI * 2);
    ctx.fillStyle = '#dfb15b';
    ctx.fill();

    ctx.restore();

    // Update Banner
    const alertEl = document.getElementById('balancerAlert');
    if (balancerRPM < 1200) {{
      alertEl.className = 'mt-2 text-xs font-mono px-3 py-1 rounded border bg-red-950/60 border-red-500 text-red-300';
      alertEl.innerText = `SUBCRITICAL (0° Phase Lag): Vibration High (${{(balancerRPM/12).toFixed(0)}}% Severity). Balls cluster near unbalance.`;
    }} else {{
      alertEl.className = 'mt-2 text-xs font-mono px-3 py-1 rounded border bg-emerald-950/60 border-emerald-500 text-emerald-300';
      alertEl.innerText = `SUPERCRITICAL (180° Inversion): Dynamic Cancellation Active! 98.4% Vibration Damped.`;
    }}

    balancerAnimId = requestAnimationFrame(render);
  }}

  if (balancerAnimId) cancelAnimationFrame(balancerAnimId);
  render();
}}

function updateBalancerRPM(val) {{
  balancerRPM = parseInt(val);
  document.getElementById('rpmDisplay').innerText = val + ' RPM';
}}

function toggleUnbalance() {{
  AudioEngine.click();
  balancerHasUnbalance = !balancerHasUnbalance;
  document.getElementById('btnUnbalance').innerText = balancerHasUnbalance ? 'Disable Heavy Spot' : 'Enable Heavy Spot';
}}

function resetBalls() {{
  AudioEngine.click();
  balancerBalls = [0.2, 0.4, 0.6, 0.8];
}}

// ================= SIM 2: SPARK METALLURGY =================
const STEELS = [
  {{ id: "1018", name: "AISI 1018 Mild Steel", carbon: "0.18% C", burst: "Zero / Long smooth yellow stream", weld: "100% (No Pre-Heat)", quench: "Cannot Harden", desc: "Long straight straw-yellow stream. Almost no forks. Safe to weld directly with any MIG/stick process." }},
  {{ id: "1045", name: "AISI 1045 Medium Carbon Axle", carbon: "0.45% C", burst: "Frequent single forks", weld: "Moderate (Preheat 150°C)", quench: "Oil / Water Quenchable", desc: "Moderate stream length with frequent repeating simple starbursts along the outer third. Common for machine spindles and hydraulic shafts." }},
  {{ id: "1095", name: "AISI 1095 / 52100 Tool Steel", carbon: "0.95% - 1.0% C", burst: "Violent dense white starbursts!", weld: "Difficult (Preheat 250°C mandatory)", quench: "Glass-Hard Oil Quench", desc: "Short, brilliant white shower with dense, multi-branched explosions beginning right at the wheel face. Ideal for shop-made knives, chisels, and scrapers." }},
  {{ id: "castiron", name: "Gray Cast Iron", carbon: "3.2% C + Free Graphite", burst: "Short dull red spurts", weld: "Specialist (Nickel ENi-CI)", quench: "Brittle", desc: "Very short, dark reddish-orange sparks breaking into tiny clusters near the wheel. High graphite content produces black dust when filed." }},
  {{ id: "hss", name: "M2 High Speed Steel (HSS)", carbon: "0.85% C + Tungsten/Moly", burst: "Dull orange with clubbed arrowheads", weld: "Do Not Weld", quench: "Air / Oil Hardening", desc: "Dull red/orange lines ending in distinctive swollen arrowheads with zero carbon starbursts. Retains hardness up to red heat (600°C)." }},
  {{ id: "ss304", name: "304 Stainless Steel", carbon: "18% Cr / 8% Ni", burst: "Short dull orange, few bursts", weld: "Excellent (TIG 308L)", quench: "Non-Hardenable (Work Hardens)", desc: "Short dull orange carrier lines with clubbed tips. Non-magnetic. Prone to severe work-hardening under machining tools." }}
];

let selectedSteel = STEELS[2]; // Default to 1095
let isGrinding = false;
let sparkParticles = [];

function initSparkSim() {{
  const container = document.getElementById('steelSampleButtons');
  container.innerHTML = '';
  STEELS.forEach(s => {{
    container.innerHTML += `
      <button onclick="selectSteel('${{s.id}}')" id="btnSteel-${{s.id}}" class="encarta-btn text-left px-3 py-1.5 rounded text-xs ${{s.id === selectedSteel.id ? 'active' : ''}}">
        <div class="font-bold text-amber-200">${{s.name}}</div>
        <div class="text-[10px] text-slate-400 font-mono">${{s.carbon}} &bull; ${{s.burst.split(' ')[0]}}</div>
      </button>
    `;
  }});
  updateSteelCard();
  runSparkLoop();
}}

function selectSteel(id) {{
  AudioEngine.click();
  selectedSteel = STEELS.find(s => s.id === id);
  document.querySelectorAll('#steelSampleButtons button').forEach(b => b.classList.remove('active'));
  document.getElementById('btnSteel-' + id).classList.add('active');
  updateSteelCard();
}}

function updateSteelCard() {{
  const card = document.getElementById('steelReadoutCard');
  card.innerHTML = `
    <h5 class="font-bold text-amber-300 font-serif">${{selectedSteel.name}}</h5>
    <div class="text-[11px] font-mono text-cyan-300">Carbon Content: ${{selectedSteel.carbon}}</div>
    <div class="text-[11px] text-slate-300"><strong>Spark Signature:</strong> ${{selectedSteel.burst}}</div>
    <div class="text-[11px] text-slate-300"><strong>Weldability:</strong> ${{selectedSteel.weld}}</div>
    <div class="text-[11px] text-slate-300"><strong>Heat Treatment:</strong> ${{selectedSteel.quench}}</div>
    <p class="text-[10px] text-slate-400 italic pt-1 border-t border-[#164e5b]">${{selectedSteel.desc}}</p>
  `;
}}

function startGrinding() {{
  isGrinding = true;
  document.getElementById('sparkStatus').innerHTML = '<span class="text-amber-400 font-bold">CONTACT DETECTED: SPARK SHOWER EMITTING</span>';
}}

function stopGrinding() {{
  isGrinding = false;
  document.getElementById('sparkStatus').innerText = 'Wheel idling. Press and hold button.';
}}

function runSparkLoop() {{
  const canvas = document.getElementById('sparksCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  function loop() {{
    ctx.fillStyle = 'rgba(2, 9, 11, 0.25)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Grinding Wheel
    ctx.save();
    ctx.translate(60, 170);
    ctx.beginPath();
    ctx.arc(0, 0, 48, 0, Math.PI * 2);
    ctx.fillStyle = '#475569';
    ctx.fill();
    ctx.strokeStyle = '#94a3b8';
    ctx.lineWidth = 3;
    ctx.stroke();

    // Spindle center
    ctx.beginPath();
    ctx.arc(0, 0, 10, 0, Math.PI * 2);
    ctx.fillStyle = '#0f172a';
    ctx.fill();

    // Workpiece metal bar
    ctx.fillStyle = '#64748b';
    ctx.fillRect(44, -10, 50, 20);
    ctx.strokeStyle = '#cbd5e1';
    ctx.strokeRect(44, -10, 50, 20);
    ctx.restore();

    // Emit sparks
    if (isGrinding) {{
      const count = selectedSteel.id === '1095' ? 12 : 6;
      for (let i = 0; i < count; i++) {{
        sparkParticles.push({{
          x: 108,
          y: 170 + (Math.random() - 0.5) * 6,
          vx: Math.random() * 8 + 8,
          vy: (Math.random() - 0.45) * 4,
          life: 1.0,
          decay: Math.random() * 0.02 + 0.015,
          steel: selectedSteel.id,
          burstDone: false
        }});
      }}
    }}

    // Update & draw sparks
    for (let i = sparkParticles.length - 1; i >= 0; i--) {{
      const p = sparkParticles[i];
      p.x += p.vx;
      p.y += p.vy;
      p.vy += 0.08; // gravity
      p.vx *= 0.985; // drag
      p.life -= p.decay;

      // Color selection
      let color = '#fbbf24';
      if (p.steel === '1095') color = '#ffffff';
      else if (p.steel === 'castiron') color = '#dc2626';
      else if (p.steel === 'hss') color = '#ea580c';

      ctx.beginPath();
      ctx.arc(p.x, p.y, p.life * 2, 0, Math.PI * 2);
      ctx.fillStyle = color;
      ctx.fill();

      // Starburst explosions for high carbon!
      if (p.steel === '1095' && p.life < 0.65 && !p.burstDone) {{
        p.burstDone = true;
        for (let j = 0; j < 5; j++) {{
          const bx = p.x + (Math.random() - 0.5) * 12;
          const by = p.y + (Math.random() - 0.5) * 12;
          ctx.beginPath();
          ctx.moveTo(p.x, p.y);
          ctx.lineTo(bx, by);
          ctx.strokeStyle = '#ffffff';
          ctx.lineWidth = 1;
          ctx.stroke();
        }}
      }}

      if (p.life <= 0 || p.x > canvas.width || p.y > canvas.height) {{
        sparkParticles.splice(i, 1);
      }}
    }}

    requestAnimationFrame(loop);
  }}

  loop();
}}

// ================= SIM 3: MOTOR WIRE WIZARD =================
const WIRE_TREES = {{
  2: {{
    title: "2-Wire Motor Architecture (DC or Series Universal)",
    steps: [
      "Step 1: Measure resistance with DMM set to low ohms.",
      "Step 2: Slowly spin shaft by hand through 360 degrees.",
      "Step 3: Check for magnetic detents (cogging)."
    ],
    diagnosis: "If resistance is 10-50 ohms with strong cogging detents, it is a Permanent Magnet DC (PMDC) motor (treadmills, cordless drills). Drive with an H-Bridge or SCR board.\\n\\nIf resistance is 1-3 ohms with near-zero cogging, it is a Series-Wound AC/DC Universal Motor (washing machines, blenders). Drive with a TDA1085 phase-angle board!"
  }},
  3: {{
    title: "3-Wire Motor Architecture (3-Phase BLDC or Cap-Run AC)",
    steps: [
      "Step 1: Measure phase-to-phase resistance across all three pairs (A-B, B-C, A-C).",
      "Step 2: Spin shaft with cordless drill and measure AC back-EMF."
    ],
    diagnosis: "If all 3 pairs have IDENTICAL low resistance (e.g., 0.8 ohms each), you have a 3-Phase Brushless BLDC / PMSM (hoverboard hubs, drone motors, washing machine pancakes). Drive with a 3-phase ESC, VESC, or E-bike controller!\\n\\nIf one pair equals the sum of the other two, it is a single-phase AC Capacitor-Run Induction motor (fans, blowers)."
  }},
  4: {{
    title: "4-Wire Motor Architecture (Bipolar Hybrid Stepper)",
    steps: [
      "Step 1: Check continuity to find two distinct isolated coil pairs (Phase A and Phase B).",
      "Step 2: Short one coil pair together with wire; shaft will instantly resist turning (magnetic braking test)."
    ],
    diagnosis: "Standard Bipolar Hybrid Stepper Motor (NEMA 14, 17, 23 from printers and 3D printers). Drive with A4988, DRV8825, or TMC2209 STEP/DIR drivers with current limiting set properly!"
  }},
  5: {{
    title: "5 or 6-Wire Motor Architecture (Unipolar Stepper)",
    steps: [
      "Step 1: Find common center-tap wires (they measure half the resistance to coil ends).",
      "Step 2: Ignore common pins to convert directly into a 4-wire bipolar stepper for 40% more torque!"
    ],
    diagnosis: "Unipolar Stepper Motor (found in vintage copiers and medical instruments). Can be driven directly by ULN2003 transistor arrays or converted to bipolar."
  }},
  8: {{
    title: "8+ Wire Motor Architecture (Brushless BLDC with Hall Sensors)",
    steps: [
      "Step 1: Separate the 3 heavy gauge wires (Phases U, V, W) from 5 thin wires (Hall sensors).",
      "Step 2: Thin wires are VCC (5V, Red), GND (Black), and Hall A, B, C (Yellow, Green, Blue)."
    ],
    diagnosis: "Sensored Brushless BLDC Motor (scooters, hoverboards, e-bikes). Provides full rated torque right down to 0 RPM without startup shudder. Drive with sensored e-bike controllers or ODrive!"
  }}
}};

function runWireTree(count) {{
  AudioEngine.click();
  const res = WIRE_TREES[count];
  const container = document.getElementById('wizardResult');
  container.innerHTML = `
    <h4 class="font-bold text-amber-300 font-serif text-sm">${{res.title}}</h4>
    <div class="space-y-1">
      <strong class="text-cyan-300 font-mono text-[11px]">Bench Protocol:</strong>
      <ul class="list-disc list-inside text-slate-300 text-xs space-y-1">
        ${{res.steps.map(s => `<li>${{s}}</li>`).join('')}}
      </ul>
    </div>
    <div class="bg-[#05171b] p-3 rounded border border-[#164e5b] text-emerald-300 font-mono text-xs whitespace-pre-line">
      ${{res.diagnosis}}
    </div>
  `;
}}

// ================= SIM 4: GENEVA MECHANISM =================
let kinematicMode = 'geneva';
let genevaSpeed = 30;
let genevaAngle = 0;

function setKinematicMode(m) {{
  AudioEngine.click();
  kinematicMode = m;
  document.getElementById('btnModeGeneva').classList.toggle('active', m === 'geneva');
  document.getElementById('btnModeYoke').classList.toggle('active', m === 'scotchyoke');
}}

function updateGenevaSpeed(v) {{
  genevaSpeed = parseInt(v);
  document.getElementById('genevaSpeedText').innerText = v + ' RPM';
}}

function runGenevaLoop() {{
  const canvas = document.getElementById('genevaCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  function render() {{
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const dt = 0.016;
    const omega = genevaSpeed * (Math.PI / 30);
    genevaAngle += omega * dt;

    if (kinematicMode === 'geneva') {{
      // Render Geneva 4-Slot
      const cx1 = 150, cy1 = 170; // Driver
      const cx2 = 300, cy2 = 170; // Driven Geneva Cross

      // Driver wheel
      ctx.beginPath();
      ctx.arc(cx1, cy1, 60, 0, Math.PI * 2);
      ctx.fillStyle = '#0f343d';
      ctx.fill();
      ctx.strokeStyle = '#2a7c8e';
      ctx.stroke();

      // Pin
      const px = cx1 + Math.cos(genevaAngle) * 50;
      const py = cy1 + Math.sin(genevaAngle) * 50;
      ctx.beginPath();
      ctx.arc(px, py, 7, 0, Math.PI * 2);
      ctx.fillStyle = '#dfb15b';
      ctx.fill();

      // Geneva Cross (4 slots)
      const genevaRot = (Math.floor(genevaAngle / (Math.PI * 2)) * (Math.PI / 2)) + Math.max(0, (genevaAngle % (Math.PI * 2) - Math.PI) * 0.5);
      ctx.save();
      ctx.translate(cx2, cy2);
      ctx.rotate(genevaRot);
      ctx.fillStyle = '#164e5b';
      ctx.fillRect(-50, -50, 100, 100);
      ctx.strokeStyle = '#45a4b9';
      ctx.strokeRect(-50, -50, 100, 100);
      // Slots
      ctx.fillStyle = '#02090b';
      ctx.fillRect(-4, -55, 8, 40);
      ctx.fillRect(-4, 15, 8, 40);
      ctx.fillRect(-55, -4, 40, 8);
      ctx.fillRect(15, -4, 40, 8);
      ctx.restore();

      ctx.fillStyle = '#67e8f9';
      ctx.font = '11px monospace';
      ctx.fillText('Driver (Continuous)', 90, 250);
      ctx.fillText('Geneva Wheel (Intermittent)', 240, 250);
    }} else {{
      // Scotch Yoke
      const cx = 150, cy = 170;
      ctx.beginPath();
      ctx.arc(cx, cy, 60, 0, Math.PI * 2);
      ctx.strokeStyle = '#2a7c8e';
      ctx.stroke();

      const crankX = cx + Math.cos(genevaAngle) * 50;
      const crankY = cy + Math.sin(genevaAngle) * 50;

      // Crank pin
      ctx.beginPath();
      ctx.arc(crankX, crankY, 6, 0, Math.PI * 2);
      ctx.fillStyle = '#dfb15b';
      ctx.fill();

      // Yoke Slider
      ctx.strokeStyle = '#45a4b9';
      ctx.lineWidth = 3;
      ctx.strokeRect(crankX - 10, 70, 20, 200);
      ctx.fillStyle = '#10b981';
      ctx.fillRect(crankX + 10, 160, 140, 20);

      ctx.fillStyle = '#67e8f9';
      ctx.font = '11px monospace';
      ctx.fillText('Pure Harmonic Linear Translation', 150, 40);
    }}

    requestAnimationFrame(render);
  }}

  render();
}}

// ================= SIM 5: CD SPOT WELD =================
function updatePulseSim() {{
  const C = parseFloat(document.getElementById('capSlider').value);
  const V = parseFloat(document.getElementById('voltSlider').value);
  const t = parseFloat(document.getElementById('pulseSlider').value);

  document.getElementById('capDisplay').innerText = C.toLocaleString() + ' F';
  document.getElementById('voltDisplay').innerText = V.toFixed(1) + ' V';
  document.getElementById('pulseDisplay').innerText = t.toFixed(1) + ' ms';

  const E = 0.5 * C * Math.pow(V, 2);
  const R_total = 0.0018; // 1.8 mOhm loop impedance
  const I_peak = V / R_total;

  document.getElementById('pulseMetrics').innerHTML = `
    <div class="bg-[#05171b] p-2 rounded border border-[#164e5b]">
      <span class="text-slate-400">STORED ENERGY</span>
      <div class="text-amber-300 font-bold text-sm">${{E.toFixed(0)}} Joules</div>
    </div>
    <div class="bg-[#05171b] p-2 rounded border border-[#164e5b]">
      <span class="text-slate-400">PEAK CURRENT</span>
      <div class="text-cyan-300 font-bold text-sm">${{I_peak.toFixed(0)}} A</div>
    </div>
    <div class="bg-[#05171b] p-2 rounded border border-[#164e5b]">
      <span class="text-slate-400">NUGGET DEPTH</span>
      <div class="text-emerald-300 font-bold text-sm">${{(Math.sqrt(E)*0.015).toFixed(2)}} mm</div>
    </div>
  `;

  const card = document.getElementById('weldVerdictCard');
  if (t > 4.0) {{
    card.innerHTML = `<span class="text-red-400 font-bold">⚠️ HAZARD: Pulse exceeds 4.0 ms!</span> Excessive thermal diffusion will melt the lithium cell gasket, causing toxic venting. Decrease pulse time!`;
  }} else if (E < 80) {{
    card.innerHTML = `<span class="text-amber-300">UNDER-POWERED: Energy &lt; 80 Joules.</span> Nickel weld will peel off easily during tear test. Increase voltage or capacitance.`;
  }} else {{
    card.innerHTML = `<span class="text-emerald-400 font-bold">✅ OPTIMAL SPOT WELD:</span> Ultra-fast ${{t}} ms discharge vaporizes interfacial resistance to form a clean fusion nugget with near-zero cell temperature rise.`;
  }}

  drawPulseWaveform(t, I_peak);
}}

function drawPulseWaveform(t_pulse, I_peak) {{
  const canvas = document.getElementById('pulseCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Grid
  ctx.strokeStyle = '#0e3a44';
  ctx.lineWidth = 1;
  for (let x = 0; x < canvas.width; x += 40) {{
    ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height); ctx.stroke();
  }}
  for (let y = 0; y < canvas.height; y += 40) {{
    ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(canvas.width, y); ctx.stroke();
  }}

  // Waveform
  ctx.beginPath();
  ctx.moveTo(40, 240);
  ctx.lineTo(80, 240);
  // Pre-pulse
  ctx.lineTo(90, 160);
  ctx.lineTo(110, 160);
  ctx.lineTo(120, 240);
  // Dwell
  ctx.lineTo(150, 240);
  // Main pulse
  const peakY = Math.max(40, 240 - (I_peak / 3500) * 190);
  ctx.lineTo(160, peakY);
  ctx.lineTo(160 + t_pulse * 15, peakY);
  ctx.lineTo(170 + t_pulse * 15, 240);
  ctx.lineTo(canvas.width - 20, 240);

  ctx.strokeStyle = '#38bdf8';
  ctx.lineWidth = 3;
  ctx.stroke();

  ctx.fillStyle = '#f8fafc';
  ctx.font = '10px monospace';
  ctx.fillText('0 A', 10, 245);
  ctx.fillText(`${{I_peak.toFixed(0)}} A`, 10, peakY + 4);
  ctx.fillText(`Pre-Pulse (0.5ms)`, 70, 145);
  ctx.fillText(`Main Fusion Pulse (${{t_pulse}}ms)`, 160, peakY - 10);
}}

function switchLabSim(simId) {{
  AudioEngine.click();
  document.querySelectorAll('#view-lab .encarta-btn').forEach(b => b.classList.remove('active'));
  document.getElementById('btn-sim-' + simId).classList.add('active');

  ['balancer', 'sparks', 'wizard', 'geneva', 'spotweld'].forEach(s => {{
    const el = document.getElementById('sim-' + s);
    if (el) el.classList.toggle('hidden', s !== simId);
  }});

  if (simId === 'balancer') startBalancerSim();
  if (simId === 'sparks') initSparkSim();
  if (simId === 'wizard') runWireTree(2);
  if (simId === 'geneva') runGenevaLoop();
  if (simId === 'spotweld') updatePulseSim();
}}

// ================= APPLIANCE X-RAY =================
const XRAY_DATA = {{
  microwave: {{
    title: "Microwave Oven Teardown Anatomy",
    svg: `
      <svg viewBox="0 0 500 320" class="w-full h-full max-h-[340px]">
        <rect x="20" y="20" width="460" height="280" rx="8" fill="#061c21" stroke="#2a7c8e" stroke-width="2"/>
        <rect x="40" y="40" width="280" height="240" fill="#02090b" stroke="#164e5b" stroke-width="2"/>
        <circle cx="180" cy="160" r="80" fill="none" stroke="#1e3a8a" stroke-width="2" stroke-dasharray="4"/>
        <circle cx="180" cy="160" r="16" fill="#38bdf8" class="cursor-pointer hover:opacity-80" onclick="showXRayHotspot('turntable')"/>
        <text x="145" y="195" fill="#38bdf8" font-size="10" font-family="monospace">Turntable AC Motor</text>

        <!-- Right Service Chamber -->
        <rect x="340" y="40" width="120" height="240" fill="#092228" stroke="#1b6170"/>
        
        <!-- Magnetron -->
        <rect x="350" y="50" width="100" height="50" fill="#450a0a" stroke="#ef4444" stroke-width="2" class="cursor-pointer" onclick="showXRayHotspot('magnetron')"/>
        <text x="360" y="80" fill="#fca5a5" font-size="10" font-family="monospace" font-weight="bold">⚠️ MAGNETRON</text>

        <!-- High-Voltage MOT -->
        <rect x="350" y="115" width="100" height="65" fill="#14532d" stroke="#22c55e" stroke-width="2" class="cursor-pointer hover:opacity-80" onclick="showXRayHotspot('mot')"/>
        <text x="365" y="152" fill="#86efac" font-size="11" font-family="monospace" font-weight="bold">MOT CORE</text>

        <!-- Cap & Diode -->
        <rect x="355" y="195" width="40" height="35" fill="#78350f" stroke="#f59e0b" class="cursor-pointer" onclick="showXRayHotspot('hvcap')"/>
        <text x="360" y="217" fill="#fde68a" font-size="9" font-family="monospace">HV CAP</text>

        <!-- Microswitches -->
        <rect x="410" y="195" width="35" height="35" fill="#1e1b4b" stroke="#818cf8" class="cursor-pointer" onclick="showXRayHotspot('switches')"/>
        <text x="415" y="217" fill="#c7d2fe" font-size="9" font-family="monospace">15A SW</text>
      </svg>
    `
  }},
  washer: {{
    title: "Direct-Drive Washing Machine Anatomy",
    svg: `
      <svg viewBox="0 0 500 320" class="w-full h-full max-h-[340px]">
        <rect x="40" y="20" width="420" height="280" rx="8" fill="#061c21" stroke="#2a7c8e" stroke-width="2"/>
        <circle cx="250" cy="150" r="110" fill="#02090b" stroke="#164e5b" stroke-width="2"/>
        <circle cx="250" cy="150" r="95" fill="none" stroke="#0ea5e9" stroke-width="4" stroke-dasharray="6" class="cursor-pointer" onclick="showXRayHotspot('ballring')"/>
        <text x="180" y="80" fill="#38bdf8" font-size="10" font-family="monospace">Annular Ball Balancer Ring</text>

        <!-- Pancake Stator -->
        <circle cx="250" cy="150" r="55" fill="#14532d" stroke="#22c55e" stroke-width="2" class="cursor-pointer" onclick="showXRayHotspot('pancake')"/>
        <text x="205" y="154" fill="#86efac" font-size="11" font-family="monospace" font-weight="bold">36-POLE STATOR</text>

        <!-- Drain Pump -->
        <rect x="80" y="240" width="80" height="40" fill="#1e1b4b" stroke="#818cf8" class="cursor-pointer" onclick="showXRayHotspot('drainpump')"/>
        <text x="95" y="265" fill="#c7d2fe" font-size="10" font-family="monospace">Drain Pump</text>
      </svg>
    `
  }},
  treadmill: {{
    title: "Exercise Treadmill Power Base Anatomy",
    svg: `
      <svg viewBox="0 0 500 320" class="w-full h-full max-h-[340px]">
        <rect x="30" y="60" width="440" height="200" rx="6" fill="#061c21" stroke="#2a7c8e" stroke-width="2"/>
        <!-- 2.5HP PMDC Motor -->
        <rect x="60" y="90" width="130" height="70" rx="4" fill="#14532d" stroke="#22c55e" stroke-width="2" class="cursor-pointer" onclick="showXRayHotspot('treadmotor')"/>
        <text x="75" y="130" fill="#86efac" font-size="11" font-family="monospace" font-weight="bold">2.5 HP PMDC MOTOR</text>

        <!-- Cast-Iron Flywheel -->
        <circle cx="220" cy="125" r="32" fill="#78350f" stroke="#f59e0b" stroke-width="2" class="cursor-pointer" onclick="showXRayHotspot('flywheel')"/>
        <text x="195" y="130" fill="#fde68a" font-size="9" font-family="monospace">FLYWHEEL</text>

        <!-- SCR Speed Board -->
        <rect x="280" y="90" width="100" height="60" fill="#1e1b4b" stroke="#818cf8" class="cursor-pointer" onclick="showXRayHotspot('speedboard')"/>
        <text x="295" y="125" fill="#c7d2fe" font-size="10" font-family="monospace">SCR Board</text>

        <!-- Incline Jack -->
        <rect x="180" y="190" width="140" height="35" fill="#450a0a" stroke="#ef4444" class="cursor-pointer" onclick="showXRayHotspot('incline')"/>
        <text x="195" y="212" fill="#fca5a5" font-size="10" font-family="monospace">ACME Incline Jack</text>
      </svg>
    `
  }},
  abspump: {{
    title: "Bosch ABS Hydraulic Pump Block Anatomy",
    svg: `
      <svg viewBox="0 0 500 320" class="w-full h-full max-h-[340px]">
        <rect x="80" y="40" width="340" height="240" rx="6" fill="#061c21" stroke="#2a7c8e" stroke-width="2"/>
        <!-- 12V 40A Motor -->
        <circle cx="170" cy="160" r="65" fill="#14532d" stroke="#22c55e" stroke-width="2" class="cursor-pointer" onclick="showXRayHotspot('absmotor')"/>
        <text x="125" y="165" fill="#86efac" font-size="11" font-family="monospace" font-weight="bold">12V 40A MOTOR</text>

        <!-- Hydraulic Manifold -->
        <rect x="260" y="90" width="120" height="140" fill="#092228" stroke="#38bdf8" stroke-width="2" class="cursor-pointer" onclick="showXRayHotspot('manifold')"/>
        <text x="270" y="130" fill="#38bdf8" font-size="10" font-family="monospace">2,600 PSI PISTONS</text>
        <circle cx="320" cy="180" r="15" fill="#f59e0b" class="cursor-pointer" onclick="showXRayHotspot('sensor')"/>
        <text x="295" y="215" fill="#fde68a" font-size="9" font-family="monospace">250 Bar Sensor</text>
      </svg>
    `
  }},
  printer: {{
    title: "Laser Printer & Scanner Bed Anatomy",
    svg: `
      <svg viewBox="0 0 500 320" class="w-full h-full max-h-[340px]">
        <rect x="30" y="40" width="440" height="240" rx="6" fill="#061c21" stroke="#2a7c8e" stroke-width="2"/>
        <!-- Ground Rods -->
        <line x1="60" y1="90" x2="440" y2="90" stroke="#cbd5e1" stroke-width="6" class="cursor-pointer" onclick="showXRayHotspot('shafts')"/>
        <line x1="60" y1="230" x2="440" y2="230" stroke="#cbd5e1" stroke-width="6" class="cursor-pointer" onclick="showXRayHotspot('shafts')"/>
        <text x="180" y="80" fill="#cbd5e1" font-size="10" font-family="monospace">Ground 8mm Steel Rods</text>

        <!-- Carriage & Optical Strip -->
        <rect x="180" y="110" width="100" height="100" fill="#14532d" stroke="#22c55e" class="cursor-pointer" onclick="showXRayHotspot('dro')"/>
        <text x="195" y="150" fill="#86efac" font-size="10" font-family="monospace" font-weight="bold">CARRIAGE &amp; DRO</text>

        <!-- NEMA Stepper -->
        <rect x="60" y="130" width="60" height="60" fill="#1e1b4b" stroke="#818cf8" class="cursor-pointer" onclick="showXRayHotspot('stepper')"/>
        <text x="68" y="165" fill="#c7d2fe" font-size="9" font-family="monospace">NEMA 17</text>
      </svg>
    `
  }}
}};

const HOTSPOT_DOSSIERS = {{
  mot: {{ title: "Microwave Oven Transformer (MOT)", danger: "LETHAL (Pre-Mod)", text: "Heavy laminated core producing 2,000V AC in native state. Hacksaw the fine secondary winding and replace with 2-3 turns of 2 AWG welding cable to deliver 3.5V @ 800A for spot welding lithium battery tabs." }},
  magnetron: {{ title: "Magnetron Vacuum Tube", danger: "TOXIC / CARCINOGENIC", text: "Contains white Beryllium Oxide (BeO) ceramic insulator collars. Do NOT chip, grind, or inhale dust. Safely harvest outer neodymium/ferrite ring magnets and discard tube intact." }},
  turntable: {{ title: "AC Synchronous Turntable Motor", danger: "Mains 120V", text: "Self-contained steel gear train outputting 3 to 5 RPM with high torque. Ideal for epoxy resin cup turners, egg incubators, and automated panorama camera pivots." }},
  hvcap: {{ title: "2,200V High-Voltage Capacitor", danger: "LETHAL CHARGE", text: "Stores dangerous charge even after unplugging. Bridge with 1k 20W resistor prior to handling. Do not reuse in low-voltage circuits." }},
  switches: {{ title: "Omron 15A Snap Microswitches", danger: "Safe", text: "Three industrial microswitches with heavy silver contacts. The gold standard for CNC router and 3D printer homing limit switches." }},
  pancake: {{ title: "36-Pole Brushless Pancake Stator", danger: "High Torque", text: "Direct-drive wash motor. Produces 500W at only 200 RPM when spun as a generator. Ideal for home wind turbines and silent pottery wheels." }},
  ballring: {{ title: "LeBlanc Annular Ball Balance Ring", danger: "Mechanical", text: "Self-contained plastic race with chrome balls and viscous oil. Automatically cancels unbalance when spun supercritical (>1,200 RPM)." }},
  drainpump: {{ title: "Magnetic Wash Drain Pump", danger: "Mains 120V", text: "Hermetically isolated permanent magnet impeller pump. Excellent for shop coolant circulation loops and laser water chillers." }},
  treadmotor: {{ title: "2.5 HP Permanent Magnet DC Motor", danger: "High DC (130V)", text: "Produces high low-RPM torque with zero stalling when driven by SCR boards with IR compensation. The premier drive for 2x72 belt grinders and lathes." }},
  flywheel: {{ title: "Cast-Iron Poly-V Flywheel", danger: "High Inertia", text: "Stores kinetic energy (E = 0.5 * I * omega^2). Prevents motor stall when cutting tools hit steel workpieces intermittently." }},
  speedboard: {{ title: "SCR Speed Control Board", danger: "Mains 120V", text: "Bridges mains AC to variable DC using dual SCRs. Features adjustable current limiting and minimum/maximum RPM trimpots." }},
  incline: {{ title: "Heavy ACME Screw Incline Jack", danger: "Pinch Hazard", text: "Self-locking ACME linear actuator producing 500-1,000 lbs of linear thrust. Ideal for lifting welding tables and solar tracker arrays." }},
  absmotor: {{ title: "12V 40A DC Micro-Piston Pump Motor", danger: "High Current", text: "Ultra-compact radial micro-piston pump producing 180 bar (2,600 PSI) for miniature hydraulic presses and hole dimplers." }},
  manifold: {{ title: "Integrated Hydraulic Valve Manifold", danger: "Extreme Pressure", text: "Precision CNC aluminum manifold containing high-pressure check valves and solenoid dump valves. Never exceed 250 bar." }},
  sensor: {{ title: "Piezoresistive Pressure Sensor", danger: "5V Logic", text: "Measures 0 to 250 bar with linear 0.5V to 4.5V analog output for closed-loop hydraulic tonnage limiting." }},
  shafts: {{ title: "Hardened Ground Steel Rods (8mm)", danger: "Safe", text: "Precision induction-hardened linear motion guide rails with sub-micron straightness. Immune to rust; perfect for custom 3D printers and laser cutters." }},
  dro: {{ title: "Linear Optical Quadrature DRO Strip", danger: "5V TTL", text: "Mylar transmissive grid strip generating 150-300 DPI quadrature pulses. Turns manual lathes and mini-mills into digital readout machine tools." }},
  stepper: {{ title: "NEMA 17 Bipolar Hybrid Stepper", danger: "Low Voltage", text: "1.8 degree step angle (200 steps/rev). Reliable, ubiquitous prime mover for micro-plotters and robotic linear stages." }}
}};

function loadXRay(appId) {{
  AudioEngine.click();
  document.querySelectorAll('#view-xray .encarta-btn').forEach(b => b.classList.remove('active'));
  document.getElementById('btnXRay-' + appId).classList.add('active');

  const data = XRAY_DATA[appId];
  document.getElementById('xrayCanvasContainer').innerHTML = data.svg;
}}

function showXRayHotspot(hKey) {{
  AudioEngine.chime();
  const d = HOTSPOT_DOSSIERS[hKey];
  if (!d) return;
  document.getElementById('xrayDetailCard').innerHTML = `
    <div class="window-header px-3 py-1.5 rounded text-xs flex justify-between items-center">
      <span>HOTSPOT DOSSIER</span>
      <span class="text-[10px] text-amber-200">${{d.danger}}</span>
    </div>
    <h4 class="font-bold text-amber-300 text-sm font-serif">${{d.title}}</h4>
    <p class="text-xs text-slate-300 leading-relaxed">${{d.text}}</p>
    <div class="pt-2 border-t border-[#164e5b]">
      <button onclick="switchTab('blueprints')" class="encarta-btn px-3 py-1 rounded text-[11px] font-semibold text-cyan-300">
        View Related Blueprints &rarr;
      </button>
    </div>
  `;
}}

// ================= BLUEPRINT STUDIO =================
function initBlueprints() {{
  renderBlueprints(BLUEPRINTS);
}}

function renderBlueprints(list) {{
  const grid = document.getElementById('blueprintsGrid');
  grid.innerHTML = '';
  list.forEach(b => {{
    grid.innerHTML += `
      <div class="encarta-window rounded p-4 flex flex-col justify-between space-y-3 hover:border-amber-400 transition-all">
        <div class="space-y-2">
          <div class="flex items-start justify-between">
            <span class="gold-badge text-[10px] font-bold px-2 py-0.5 rounded">BP #${{b.num}}</span>
            <span class="text-[10px] font-bold px-2 py-0.5 rounded font-mono" style="background:${{b.diffColor}}22; color:${{b.diffColor}}; border:1px solid ${{b.diffColor}}44">
              ${{b.diff}}
            </span>
          </div>
          <h3 class="font-bold text-amber-200 text-sm font-serif leading-snug">${{b.title}}</h3>
          <p class="text-[11px] text-slate-300 leading-relaxed line-clamp-3">${{b.desc}}</p>
          <div class="text-[11px] font-mono text-cyan-300 pt-1 border-t border-[#164e5b]">
            <strong>Core Donor:</strong> ${{b.donor}}
          </div>
        </div>
        <button onclick="openBlueprintModal(${{b.num}})" class="encarta-btn w-full py-1.5 rounded text-xs font-bold text-amber-300 flex items-center justify-center space-x-1.5">
          <span>📜</span>
          <span>Open Full Blueprint &amp; Schematic</span>
        </button>
      </div>
    `;
  }});
}}

function filterBlueprints(diff) {{
  AudioEngine.click();
  document.querySelectorAll('.bp-filter-btn').forEach(b => b.classList.remove('active'));
  event.target.classList.add('active');
  if (diff === 'all') renderBlueprints(BLUEPRINTS);
  else renderBlueprints(BLUEPRINTS.filter(b => b.diff === diff));
}}

function openBlueprintModal(bNum) {{
  AudioEngine.chime();
  const bp = BLUEPRINTS.find(b => b.num === bNum);
  if (!bp) return;

  document.getElementById('modalHeaderTitle').innerText = `BLUEPRINT #${{bp.num}}: ${{bp.title.toUpperCase()}}`;
  document.getElementById('modalBody').innerHTML = `
    <div class="space-y-4">
      <div class="flex items-center justify-between border-b border-[#164e5b] pb-2">
        <span class="text-xs text-amber-300"><strong>Primary Donor:</strong> ${{bp.donor}}</span>
        <span class="font-mono text-cyan-300"><strong>Output Power:</strong> ${{bp.power}}</span>
      </div>

      <div>
        <h4 class="font-bold text-amber-300 font-serif mb-1">Architecture Overview:</h4>
        <p class="text-slate-300 leading-relaxed">${{bp.desc}}</p>
      </div>

      <div>
        <h4 class="font-bold text-amber-300 font-serif mb-1">Kinematic / Electrical Schematic:</h4>
        <pre class="bg-[#02090b] p-3 rounded border border-[#164e5b] text-cyan-300 font-mono text-[11px] overflow-x-auto">${{bp.schematic}}</pre>
      </div>

      <div>
        <h4 class="font-bold text-amber-300 font-serif mb-1">Governing Physical Law:</h4>
        <div class="bg-[#05171b] p-2 rounded border border-[#164e5b] font-mono text-emerald-300 text-xs">
          ${{bp.formula}}
        </div>
      </div>

      <div>
        <h4 class="font-bold text-amber-300 font-serif mb-1">Bill of Materials (BOM):</h4>
        <ul class="list-disc list-inside text-slate-300 space-y-1">
          ${{bp.bom.map(item => `<li>${{item}}</li>`).join('')}}
        </ul>
      </div>

      <div>
        <h4 class="font-bold text-amber-300 font-serif mb-1">Step-by-Step Fabrication SOP:</h4>
        <div class="bg-[#092228] p-3 rounded border border-[#1b6170] text-slate-200 whitespace-pre-line leading-relaxed">
          ${{bp.sop}}
        </div>
      </div>
    </div>
  `;
  document.getElementById('blueprintModal').classList.remove('hidden');
}}

function closeBlueprintModal() {{
  AudioEngine.click();
  document.getElementById('blueprintModal').classList.add('hidden');
}}

// ================= TAB 5: MINDMAZE '95 =================
let mazeRoom = 0;
let mazeScore = 0;
const MAZE_ROOMS = [
  {{ title: "Room 1: The Scrap Loading Dock", icon: "🚛", desc: "A locked roller door requires decoding an unknown 3-phase motor." }},
  {{ title: "Room 2: The Grinding & Metallurgy Booth", icon: "✨", desc: "Before quenching cutting tools, you must identify scrap steel sparks." }},
  {{ title: "Room 3: The Motor Rewind Station", icon: "⚡", desc: "A copper commutator needs maintenance. One false tool destroys the armature." }},
  {{ title: "Room 4: The High-Voltage Substation", icon: "⚠️", desc: "Lethal 2,200V charges block the vault door. Safe discharge is mandatory." }},
  {{ title: "Room 5: The Supercritical Rotordynamics Vault", icon: "🏆", desc: "Master the 180° phase inversion law to claim the Master Scrapper Diploma!" }}
];

function initMindMaze() {{
  renderMazeQuestion();
}}

function renderMazeQuestion() {{
  const qData = QUESTIONS[mazeRoom % QUESTIONS.length];
  const rData = MAZE_ROOMS[mazeRoom];

  document.getElementById('mazeRoomNumber').innerText = `${{mazeRoom + 1}} / 5`;
  document.getElementById('mazeScore').innerText = `${{mazeScore}} PTS`;
  document.getElementById('mazeRoomTitle').innerText = rData.title;
  document.getElementById('mazeRoomIcon').innerText = rData.icon;
  document.getElementById('mazeRoomDesc').innerText = rData.desc;

  document.getElementById('mazeQuestionText').innerText = qData.q;
  const optContainer = document.getElementById('mazeOptionsContainer');
  optContainer.innerHTML = '';

  qData.options.forEach((opt, idx) => {{
    optContainer.innerHTML += `
      <button onclick="submitMazeAnswer(${{idx}})" class="encarta-btn text-left p-3 rounded text-xs hover:border-amber-400">
        <span class="font-mono text-amber-300 font-bold mr-2">${{String.fromCharCode(65 + idx)}})</span>
        <span>${{opt}}</span>
      </button>
    `;
  }});

  document.getElementById('mazeFeedback').classList.add('hidden');
  document.getElementById('btnNextRoom').classList.add('hidden');
}}

function submitMazeAnswer(chosen) {{
  const qData = QUESTIONS[mazeRoom % QUESTIONS.length];
  const fb = document.getElementById('mazeFeedback');
  fb.classList.remove('hidden');

  if (chosen === qData.answer) {{
    AudioEngine.chime();
    mazeScore += 100;
    document.getElementById('mazeScore').innerText = `${{mazeScore}} PTS`;
    fb.className = 'text-xs p-3 rounded font-mono bg-emerald-950/80 border border-emerald-500 text-emerald-300';
    fb.innerHTML = `<strong>CORRECT! +100 PTS</strong><br>${{qData.explain}}`;
    document.getElementById('btnNextRoom').classList.remove('hidden');
  }} else {{
    AudioEngine.buzz();
    fb.className = 'text-xs p-3 rounded font-mono bg-red-950/80 border border-red-500 text-red-300';
    fb.innerHTML = `<strong>INCORRECT! DOOR LOCK ENGAGED.</strong><br>${{qData.explain}}`;
  }}
}}

function advanceMazeRoom() {{
  AudioEngine.click();
  mazeRoom++;
  if (mazeRoom >= MAZE_ROOMS.length) {{
    AudioEngine.victory();
    document.getElementById('mazeRoomTitle').innerText = "🎉 THE MASTER SCRAP VAULT REACHED!";
    document.getElementById('mazeRoomIcon').innerText = "🏆";
    document.getElementById('mazeRoomDesc').innerHTML = `
      <div class="text-center space-y-3 py-3">
        <div class="text-amber-300 font-bold text-sm">CONGRATULATIONS, GRAND MASTER SCRAPPER!</div>
        <p class="text-xs text-slate-200">You successfully navigated the 1995 Industrial Megafactory and mastered electromechanical triage with a score of <strong>${{mazeScore}} Points</strong>.</p>
        <button onclick="resetMaze()" class="encarta-btn px-6 py-2 rounded text-xs font-bold text-amber-300">Play Again</button>
      </div>
    `;
    document.getElementById('mazeOptionsContainer').innerHTML = '';
    document.getElementById('mazeQuestionText').innerText = "DIPLOMA CONFERRED: ELECTROMECHANICAL MASTER ARCHITECT";
    document.getElementById('btnNextRoom').classList.add('hidden');
  }} else {{
    renderMazeQuestion();
  }}
}}

function resetMaze() {{
  AudioEngine.click();
  mazeRoom = 0;
  mazeScore = 0;
  renderMazeQuestion();
}}

// ================= PINPOINTER OMNISEARCH =================
function handleSearch(query) {{
  const dropdown = document.getElementById('searchDropdown');
  if (!query || query.trim().length < 2) {{
    dropdown.classList.add('hidden');
    return;
  }}

  const q = query.toLowerCase();
  const matchedDonors = DONORS.filter(d => d.name.toLowerCase().includes(q) || d.harvest.some(h => h.toLowerCase().includes(q)));
  const matchedBlueprints = BLUEPRINTS.filter(b => b.title.toLowerCase().includes(q) || b.donor.toLowerCase().includes(q));

  if (matchedDonors.length === 0 && matchedBlueprints.length === 0) {{
    dropdown.innerHTML = '<div class="p-3 text-xs text-slate-400 font-mono">No matching salvage artifacts found.</div>';
    dropdown.classList.remove('hidden');
    return;
  }}

  let html = '';
  matchedDonors.slice(0, 4).forEach(d => {{
    html += `
      <div onclick="switchTab('atlas'); document.getElementById('donor-${{d.id}}').scrollIntoView({{behavior:'smooth'}}); document.getElementById('searchDropdown').classList.add('hidden');" 
           class="p-2.5 hover:bg-[#0e3a44] cursor-pointer border-b border-[#164e5b] text-xs">
        <span class="text-amber-300 font-bold">[DONOR] ${{d.name}}</span>
        <div class="text-[10px] text-slate-300 truncate">${{d.harvest.join(', ')}}</div>
      </div>
    `;
  }});

  matchedBlueprints.slice(0, 4).forEach(b => {{
    html += `
      <div onclick="switchTab('blueprints'); openBlueprintModal(${{b.num}}); document.getElementById('searchDropdown').classList.add('hidden');" 
           class="p-2.5 hover:bg-[#0e3a44] cursor-pointer border-b border-[#164e5b] text-xs">
        <span class="text-cyan-300 font-bold">[BLUEPRINT #${{b.num}}] ${{b.title}}</span>
        <div class="text-[10px] text-slate-300 truncate">${{b.donor}} &bull; ${{b.power}}</div>
      </div>
    `;
  }});

  dropdown.innerHTML = html;
  dropdown.classList.remove('hidden');
}}

// Initialize On Load
window.addEventListener('DOMContentLoaded', () => {{
  initAtlas();
  initBlueprints();
  initMindMaze();
}});
</script>

</body>
</html>
"""
    return html_content

if __name__ == "__main__":
    html_data = build_html()
    
    # 1. Output to workspace as index.html and interactive_encyclopedia.html
    path_index = os.path.join(WORKSPACE, "index.html")
    path_app = os.path.join(WORKSPACE, "interactive_encyclopedia.html")
    with open(path_index, "w", encoding="utf-8") as f:
        f.write(html_data)
    with open(path_app, "w", encoding="utf-8") as f:
        f.write(html_data)
        
    print(f"[OK] Workspace index.html written ({os.path.getsize(path_index)} bytes)")
    print(f"[OK] Workspace interactive_encyclopedia.html written ({os.path.getsize(path_app)} bytes)")

    # 2. Output to artifact directory as encarta_salvage_encyclopedia.html
    artifact_path = os.path.join(ARTIFACT_DIR, "encarta_salvage_encyclopedia.html")
    with open(artifact_path, "w", encoding="utf-8") as f:
        f.write(html_data)
    print(f"[OK] Artifact encarta_salvage_encyclopedia.html written ({os.path.getsize(artifact_path)} bytes)")
