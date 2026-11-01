"""
Enriched metadata catalog for all 15 volumes and 36 chapters of
The Maker's Bible of Electromechanical Salvage & Repurposing.
Provides rich labels, sub-labels, icons, and summaries for the visually striking left atlas.
"""

VOLUME_METADATA = [
    {
        "volCode": "VOL. 00",
        "title": "Foundations, Diagnostics & Control",
        "tagline": "Lethal Capacitors, Wire Triage Trees & Universal Driving Topologies",
        "catIcon": "⚡",
        "hazard": "HIGH HAZARD",
        "hazardColor": "#ef4444"
    },
    {
        "volCode": "VOL. 01",
        "title": "Precision Consumer Electronics & Optics",
        "tagline": "Hardened Ground Rails, Optical DRO Scales, DVD Sleds & Voice Coils",
        "catIcon": "🖨️",
        "hazard": "PRECISION",
        "hazardColor": "#06b6d4"
    },
    {
        "volCode": "VOL. 02",
        "title": "Automotive 12V Workhorses & Traction",
        "tagline": "Wiper Worm Drives, 5HP Alternator Hacks, ABS Pumps & VVT Valves",
        "catIcon": "🚗",
        "hazard": "HIGH CURRENT / HYDRAULIC",
        "hazardColor": "#f59e0b"
    },
    {
        "volCode": "VOL. 03",
        "title": "Domestic Mains Appliances",
        "tagline": "36-Pole Pancake BLDCs, 3HP Treadmill Spindles, Hermetic Pots & MOTs",
        "catIcon": "🌪️",
        "hazard": "MAINS AC / 2,000V",
        "hazardColor": "#ef4444"
    },
    {
        "volCode": "VOL. 04",
        "title": "Mobility & Power Tools",
        "tagline": "36V Hub BLDCs, Flashed Firmware, Drill Planetary Gearboxes & Turbines",
        "catIcon": "🛴",
        "hazard": "HIGH RPM / BATTERY",
        "hazardColor": "#10b981"
    },
    {
        "volCode": "VOL. 05",
        "title": "Non-Motor Electromechanical Gems & Lab Scrap",
        "tagline": "Syringe Dosing Pumps, Barcode Polygon LiDAR, Server PSUs & Omron Switches",
        "catIcon": "🔬",
        "hazard": "PRECISION / RF",
        "hazardColor": "#8b5cf6"
    },
    {
        "volCode": "VOL. 06",
        "title": "Marquee Project Cookbooks (Builds 1 to 8)",
        "tagline": "8 Step-by-Step Blueprints (Builds 1–8): Wind Turbines, Sim Wheels, Grinders & AGVs",
        "catIcon": "🛠️",
        "hazard": "FABRICATION",
        "hazardColor": "#dfb15b"
    },
    {
        "volCode": "VOL. 07",
        "title": "Unexplored Frontiers & Exotic Electromechanics",
        "tagline": "DMD Photolithography, Ultrasonic Horns, Coaxial Magnetic Gears & Stirling",
        "catIcon": "🔮",
        "hazard": "ADVANCED PHYSICS",
        "hazardColor": "#a855f7"
    },
    {
        "volCode": "VOL. 08",
        "title": "Frontier Project Cookbooks (Builds 9 to 50)",
        "tagline": "42 Advanced Blueprints (Builds 9–50): Supercritical Rotors, 40k Spindles, Cycloidals, Wire-EDM & Waterjets",
        "catIcon": "📐",
        "hazard": "FRONTIER LEVEL",
        "hazardColor": "#ec4899"
    },
    {
        "volCode": "VOL. 09",
        "title": "Field Acquisition & Rapid Sourcing Manual",
        "tagline": "Urban Mining Channels, 12 lb Backpack Loadout & 30-Second Field Triage",
        "catIcon": "🎒",
        "hazard": "FIELD TACTICS",
        "hazardColor": "#14b8a6"
    },
    {
        "volCode": "VOL. 10",
        "title": "Mechanical Engineering & Transmissions",
        "tagline": "Epicyclic Reducers, Inverted Pantographs, Geneva Drives & Supercritical Balancers",
        "catIcon": "⚙️",
        "hazard": "KINEMATICS",
        "hazardColor": "#3b82f6"
    },
    {
        "volCode": "VOL. 11",
        "title": "Radical Mechanical Exploits & Kinematics",
        "tagline": "Inverted Differentials, Capstan Winches, Tape Measure Snaps & Whipple Pivots",
        "catIcon": "💡",
        "hazard": "EXPERIMENTAL",
        "hazardColor": "#f97316"
    },
    {
        "volCode": "VOL. 12",
        "title": "Battle-Tested Forum Lore & Scrapper's Calculus",
        "tagline": "Treadmill Lathe Pitfalls, Hall Mapping Secrets & Junkyard Core Economics",
        "catIcon": "💬",
        "hazard": "COMMUNITY WISDOM",
        "hazardColor": "#84cc16"
    },
    {
        "volCode": "VOL. 13",
        "title": "Viable Salvage & Garage Build Manual",
        "tagline": "Teardown SOPs, Spark Test Metallurgy, Inrush Mathematics & Bench Triage",
        "catIcon": "🔧",
        "hazard": "SHOP PRACTICE",
        "hazardColor": "#eab308"
    },
    {
        "volCode": "VOL. 14",
        "title": "Grand Master Salvage Matrix & Compendium",
        "tagline": "The Complete Multi-Attribute Master Matrix of 88 Donor Streams & 50 Engineering Blueprints",
        "catIcon": "🏛️",
        "hazard": "MASTER ARCHIVE",
        "hazardColor": "#dfb15b"
    }
]

CHAPTER_SUBTITLES = {
    "Chapter 1: Scrapper's Safety Protocols & Lethal Hazards": "Dielectric absorption rebound, BeO dust, pinhole hydraulic injection & bleeder shunts",
    "Chapter 2: Motor Identification & Bench Diagnostics": "Wire-count decision trees, back-EMF generator tests & Q-factor ring-down",
    "Chapter 3: Universal Driving Topologies & Control Architectures": "Dual H-bridges, VESC, ODrive, SCR phase control & dual-wound pull-hold PWM",
    "Chapter 4: Printers, Scanners & Office Copiers": "Hardened 8mm ground rods, NEMA steppers, digital caliper DROs & bill acceptor rollers",
    "Chapter 5: Optical Disc Drives & Hard Disk Drives": "M3 micro-leadscrews, voice-coil galvos, audiophile turntables & camera escapements",
    "Chapter 6: Automotive 12V Workhorses": "High-torque wiper motors, power window regulators & seat-track ACME screw rams",
    "Chapter 7: Heavy Automotive Traction & Alternator Hacking": "3-phase alternator conversions, Albright reversing contactors & EV hermetic scroll pumps",
    "Chapter 8: Automotive Hydraulics & High-Flow Blowers": "Bosch ABS 180-bar pumps, camshaft VVT spool valves & regenerative desiccant dryers",
    "Chapter 9: Washing Machines & Clothes Dryers": "Direct-drive pancake wind generators, LeBlanc ball balancers & TDA1085 tacho boards",
    "Chapter 10: Treadmills & Exercise Equipment": "130V PMDC spindle motors, cast-iron flywheels, SCR boards & heavy incline jacks",
    "Chapter 11: Refrigeration & Microwave Electromechanics": "Ultra-quiet hermetic vacuum compressors, 15A snap switches & rewound 800A MOT spot welders",
    "Chapter 12: Mobility Electromechanics & Power Tools": "Hoverboard STM32 firmware hacking, Ninebot e-scooter hub decryption, 10S BMS salvage & Dyson turbines",
    "Chapter 13: Lab Scrap, Sensors & Structural Hardware": "Sub-microliter paste dispensers, 360° laser radars, 100A server rails & Omron switches",
    "Chapter 14: Marquee Salvage Project Cookbooks (Builds 1 to 8)": "Step-by-step blueprints (Builds 1 to 8): wind turbine, sim wheel, laser galvo, 2x72 grinder, spot welder, AGV",
    "Chapter 14: Marquee Salvage Project Cookbooks": "Step-by-step blueprints (Builds 1 to 8): wind turbine, sim wheel, laser galvo, 2x72 grinder, spot welder, AGV",
    "Chapter 15: Spatial Light Modulators & Micro-Optics Scrap": "DLP micromirror arrays for maskless UV semiconductor direct-write & 5-axis IBIS stages",
    "Chapter 16: Ultrasonics, Sonotrodes & Acoustic Cavitation": "Langevin transducers, stepped titanium booster horns & 30 kHz frictionless knives",
    "Chapter 17: Commercial Fluidics & Rotary Vane Pumps": "Procon brass sliding vane pumps, dishwasher peristaltic dosers, soft-serve augers & venturi vacuums",
    "Chapter 18: Exotic Electromagnetics, Dynos & Resolvers": "Coaxial magnetic gearboxes, CD pulsed power vs AC MOT & aircraft resolvers",
    "Chapter 19: Thermal & Exotic Energy Harvesting": "Thermoacoustic Stirling engines, subwoofer voice-coil alternators & woodstove TEGs",
    "Chapter 20: Frontier Project Blueprints (Builds 9 to 50)": "42 Production blueprints (Builds 9 to 50): lithography, 40k RPM spindle, 3k PSI waterjet, cycloidal reducers, wire-EDM, lathe conversions, hydrostatic rigs",
    "Chapter 20: Frontier Project Blueprints": "42 Production blueprints (Builds 9 to 50): lithography, 40k RPM spindle, 3k PSI waterjet, cycloidal reducers, wire-EDM, lathe conversions, hydrostatic rigs",
    "Chapter 21: The Scrapper's Field Sourcing & Toolkit Manual": "Curbside triage protocols, junkyard tactics, legal scrap streams & field triage loadout",
    "Chapter 22: Shaft Couplings, Hub Adapters & Hardened Machining": "Metric-imperial split sleeves, bismuth anti-chatter mandrels & Trantorque keyless locking hubs",
    "Chapter 23: Gearboxes, Cycloidal Drives & Speed Reducers": "Planetary cascades, zero-backlash cycloidal drives & worm gear axial thrust",
    "Chapter 24: Linear Kinematics, Leadscrews & Linkages": "Inverted 50:1 pantographs, Roberts/Watt straight-line linkages & anti-backlash split nuts",
    "Chapter 25: Clutches, Electromagnetic Brakes & Freewheels": "Car 12V AC compressor clutches, sprag one-way bearings, centrifugal soft-starts & magnetic particle brakes",
    "Chapter 26: Cams, Geneva Drives & Intermittent Mechanisms": "Maltese cross Geneva indexing, barrel cams for wire winders & harmonic lifters",
    "Chapter 27: Flywheels, Dynamic Balancing & Mechanical Damping": "Supercritical rotordynamic phase inversion, LeBlanc ball balancers & knife-edge arbors",
    "Chapter 28: Radical Mechanical Exploits & Kinematic Brainstorming": "Dual-motor summing differentials, capstans, bistable tape springs & Whipple flexures",
    "Chapter 29: Battle-Tested Forum Lore & Unwritten Scrapper Rules": "The 5 deadly treadmill traps, component hoarding fallacy & systematic Hall mapping",
    "Chapter 30: Obscure Donor Gems & Underground Maker Exploits": "Belimo 30Nm actuators, Juki sewing servos, Spal 600W blowers, EEV micro-steppers & coin eddy sensors",
    "Chapter 31: Scrapper's Economics, Core Resale & Scrap Yard Calculus": "Hourly salvage yield formula, $2/hr copper vs $150/hr modules & PCB grading",
    "Chapter 32: Step-by-Step Field Teardown SOPs": "12-minute treadmill extraction, zero-shock microwave teardown & EPS column removal",
    "Chapter 33: Garage Fabrication & Heavy Mounting Workarounds": "Scrap-steel spark test metallurgy, paper template transfer, lapping & slotted mounts",
    "Chapter 34: Electrical Sanity & Power Architecture": "Inrush current math (I = V/R), battery buffering, Schottky diodes & star grounding",
    "Chapter 35: Bench Testing & Motor Health Triage": "Scrap alloy ID checklist, thermal shock pulley pullers, 60°/120° Hall mapping & LED strobe tachos",
    "Appendix A: The Grand Master Electromechanical Matrix & Field Compendium (88 Donors • 50 Blueprints)": "Comprehensive multi-attribute field reference matrix covering all 88 donor scrap streams and 50 production engineering blueprints",
    "Appendix A: The Grand Master Electromechanical Matrix & Field Compendium": "Comprehensive multi-attribute field reference matrix covering all 88 donor scrap streams and 50 production engineering blueprints"
}
