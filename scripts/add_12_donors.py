"""
Appends 12 new high-value industrial, medical, and utility donor scrap streams to DONORS_DATA in scripts/encarta_data.py,
expanding the donor database from 88 to 100 donors.
"""

import os
import sys

WORKSPACE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ENCARTA_DATA_PATH = os.path.join(WORKSPACE, "scripts", "encarta_data.py")

NEW_DONORS = [
    {
        "id": "hospital_bed_actuator",
        "name": "Medical Hospital Bed Linear Actuator (Linak / Dewert)",
        "cat": "mobility",
        "danger": "Pinch Hazard (4,000N Thrust)",
        "dangerColor": "#f59e0b",
        "harvest": [
            "24V DC Permanent Magnet Worm Gearmotor",
            "Heavy-Duty Acme / Ball Leadscrew Assembly (4,000N - 6,000N Thrust [TYPICAL])",
            "Dual Internal Hall Effect / Limit Microswitches",
            "10k-ohm Linear Feedback Positioning Potentiometer"
        ],
        "avoid": "Stripping internal nylon safety shear gears by applying dynamic hammering shock loads",
        "bestFor": "Heavy CNC Z-Axis Counterbalance, Solar Tracker Dual-Axis Positioner, Powered Scissor Lift Table, Shop Press Automation",
        "triage": "Measure terminal resistance ($1.5-3.0\\,\\Omega$ [TYPICAL]). Power with 12V-24V DC bench PSU; verify smooth stroke travel and current draw under 1.5A no-load [TYPICAL]. Test feedback pot linearity with DMM."
    },
    {
        "id": "infusion_pump_peristaltic",
        "name": "Clinical Peristaltic Infusion Pump (Alaris / Hospira)",
        "cat": "frontier",
        "danger": "Biohazard (Residual Fluids) / Moderate",
        "dangerColor": "#f59e0b",
        "harvest": [
            "NEMA 14/17 Bipolar Stepper Motor with 10:1 Planetary Reducer",
            "4-Roller Cam Peristaltic Pump Head (0.1 - 999 mL/hr [TYPICAL])",
            "Optical / Ultrasonic Air-in-Line Bubble Detector Sensor",
            "Precision Silicon Piezoresistive Occlusion Pressure Sensor"
        ],
        "avoid": "Direct contact with used fluid cassettes; decontaminate outer chassis with 10% sodium hypochlorite before tear-down",
        "bestFor": "Chemical Titration & Dosing Station, Microfluidic Lab-on-a-Chip Driver, Precision Solder Paste / Liquid Flux Dispenser, Automated Plant Nutrient Feeder",
        "triage": "Measure stepper winding resistance ($4-10\\,\\Omega$ per phase [TYPICAL]). Power ultrasonic bubble sensor with 5V; observe analog logic level shift on oscilloscope when air gap passes through sensor channel."
    },
    {
        "id": "copeland_scroll_compressor",
        "name": "Commercial HVAC Scroll Compressor (Copeland / Danfoss)",
        "cat": "frontier",
        "danger": "Pressurized Refrigerant / Mains 240V-480V 3-Phase",
        "dangerColor": "#ef4444",
        "harvest": [
            "Precision Cast-Iron Orbiting & Fixed Involute Scroll Spiral Set (100% Volumetric Efficiency [TYPICAL])",
            "High-Torque 3-Phase AC Induction Stator & Balanced Rotor Assembly",
            "Integrated High-Pressure Thermal Pressure Relief Bypass Valve",
            "Precision Ground Counterweighted Eccentric Spindle Shaft"
        ],
        "avoid": "Venting pressurized fluorocarbon refrigerant (EPA Section 608 violation); ensure certified recovery before cutting copper stubs",
        "bestFor": "Organic Rankine Cycle (ORC) Waste-Heat Expansion Engine, Ultra-Quiet High-Pressure Shop Compressor, Cryogenic Stirling Pre-Cooler",
        "triage": "Test terminal-to-shell insulation with 500V DC megohmmeter (must exceed 20 Megohms [VERIFIED]). Verify phase-to-phase winding symmetry matches within 2% [TYPICAL]."
    },
    {
        "id": "telecom_rectifier_shelf",
        "name": "Enterprise Telecom -48V DC Rectifier Module (Eltek / Emerson)",
        "cat": "workshop",
        "danger": "Mains 240V / Arc-Flash Stored Energy (3,000W)",
        "dangerColor": "#ef4444",
        "harvest": [
            "3,000W Active Power Factor Correction (PFC) Front-End Stage",
            "Synchronous Rectification GaN / MOSFET H-Bridge Inverter",
            "Planar Ferrite High-Frequency Isolation Power Transformer",
            "Regulated 48V-54V DC Output at 50A to 60A Continuous [TYPICAL]",
            "Isolated CAN-Bus Digital Telemetry & Voltage Adjustment Interface"
        ],
        "avoid": "Hot-swapping without locking ejector handle engaged; primary and secondary bus caps hold high current potential after disconnect",
        "bestFor": "Off-Grid 48V LiFePO4 Battery Fast Charger, Anodizing & Electro-Plating High-Current Power Source, High-Power DC Motor Dynamometer Supply",
        "triage": "Inspect gold edge fingers for pitting or arc carbon. Connect via isolated AC line; check open-circuit DC output voltage ($53.5\\,\\text{V} \\pm 0.5\\,\\text{V}$ default [TYPICAL]). Measure CAN-bus termination resistance ($120\\,\\Omega$ [TYPICAL])."
    },
    {
        "id": "marine_trim_tilt_pump",
        "name": "Marine Outboard Hydraulic Trim & Tilt Power Unit (Mercury / Yamaha)",
        "cat": "auto",
        "danger": "High-Pressure Hydraulic Fluid (2,500 PSI) / Corrosion",
        "dangerColor": "#f59e0b",
        "harvest": [
            "12V DC High-Torque Reversible PMDC Motor",
            "Miniature Bi-Directional High-Pressure Gear Pump Block",
            "Dual Pilot-Operated Check Valves & Overpressure Relief Cartridges",
            "Hard-Chromed Marine Grade Stainless Steel Double-Acting Hydraulic Rams"
        ],
        "avoid": "Shearing saltwater-corroded fasteners (apply penetrant and impact driver to avoid breaking case studs)",
        "bestFor": "Compact Hydraulic Tube Bender, Heavy Tooling Clamping Fixture, Mobile Robot Articulated Joint, Micro-Excavator Arm",
        "triage": "Bench-test 12V motor rotation in both polarities; verify no-load current < 4A [TYPICAL]. Inspect hydraulic fluid for milky emulsion (water contamination); flush with clean ISO 32 hydraulic fluid."
    },
    {
        "id": "coffee_burr_grinder",
        "name": "Commercial Espresso Burr Grinder (Mahlkönig / Mazzer)",
        "cat": "domestic",
        "danger": "Mains 120V/240V / Rotary Laceration Hazard",
        "dangerColor": "#f59e0b",
        "harvest": [
            "Matched Tool Steel / Titanium-Nitride Flat Burrs (64mm - 83mm Diameter [TYPICAL])",
            "Heavy Cast-Aluminum Threaded Micrometer Grinding Collar (10 um Pitch Adjustment [TYPICAL])",
            "350W-650W High-Torque Low-RPM Shaded-Pole / Capacitor Induction Motor",
            "Heavy Cast-Iron Anti-Vibration Motor Housing Base"
        ],
        "avoid": "Running grinder with burrs zeroed into metal-on-metal contact (permanently dulls precision cutting teeth)",
        "bestFor": "Mineral Powder & Pigment Pulverizer, Ceramic Glaze Micro-Crusher, Plastic Filament Shredder Granulator, Lab Particle Sizing Mill",
        "triage": "Spin burr carrier plate by hand to check thread smoothness. Verify runout with dial test indicator (< 0.01mm TIR [VERIFIED]). Test motor run capacitor with capacitance meter ($12-20\\,\\mu\\text{F}$ [TYPICAL])."
    },
    {
        "id": "forklift_hydraulic_valve",
        "name": "Industrial Forklift Multi-Spool Hydraulic Valve Block (Cascade / Parker)",
        "cat": "workshop",
        "danger": "Ultra-High Hydraulic Pressure (3,000 PSI) / Trapped Energy",
        "dangerColor": "#ef4444",
        "harvest": [
            "Hardened Cast-Ductile Iron Multi-Spool Valve Body",
            "Ground & Hard-Chromed Metering Spools (Clearance < 0.005mm [TYPICAL])",
            "Adjustable Main Pressure Relief Cartridge Valve (1,500 - 3,200 PSI [TYPICAL])",
            "Integrated Load-Holding Poppet Check Valves & Feathering Levers"
        ],
        "avoid": "Disconnecting hydraulic hoses under line pressure; cycle all control levers with pump off to relieve residual accumulator pressure",
        "bestFor": "20-Ton Hydraulic Log Splitter, Custom Hydraulic Sheet Metal Press Brake, Backhoe Implement Control Bank, Fluid Power Training Stand",
        "triage": "Slide spools manually: must glide smoothly by thumb pressure with zero notchiness or gritty binding. Remove relief valve cartridge and inspect seat for metal particulate."
    },
    {
        "id": "autoclave_sterilizer",
        "name": "Medical Steam Autoclave Sterilizer (Midmark / Tuttnauer)",
        "cat": "frontier",
        "danger": "Superheated Steam (134°C / 30 PSI) / Pressure Hazard",
        "dangerColor": "#ef4444",
        "harvest": [
            "ASME Code-Stamped Thick-Wall Seamless 316L Stainless Pressure Chamber",
            "1,400W-2,200W Band / Immersion Heating Elements",
            "Direct-Acting Stainless Steel High-Temperature Solenoid Exhaust Valves",
            "Mechanical Spring-Loaded Pressure Relief Valve (Certified 35 PSI [VERIFIED])",
            "Platinum Class-A PT100 Resistance Temperature Detector (RTD)"
        ],
        "avoid": "Operating with gouged or cracked door seals; never modify or bypass the mechanical ASME pressure relief valve",
        "bestFor": "Carbon Fiber Pre-Preg Pressure Curing Autoclave, Essential Oil Superheated Steam Distiller, Hydrothermal Mineral/Crystal Synthesis Reactor, High-Pressure Extraction Chamber",
        "triage": "Perform hydrostatic water proof test to 1.5x working pressure (45 PSI [CALCULATED]) before steam testing. Measure heater element resistance ($9-12\\,\\Omega$ at 120V, $25-30\\,\\Omega$ at 240V [CALCULATED])."
    },
    {
        "id": "three_phase_induction_motor",
        "name": "3-Phase Industrial AC Induction Motor (5 HP - 10 HP Baldor / WEG)",
        "cat": "workshop",
        "danger": "240V / 480V 3-Phase / Heavy Mass (> 50 kg)",
        "dangerColor": "#ef4444",
        "harvest": [
            "Heavy Cast-Iron Stator Housing & Copper/Aluminum Squirrel-Cage Rotor",
            "Heavy-Duty Deep-Groove Ball Bearings (6205 / 6306 Series [TYPICAL])",
            "Dual-Voltage 9-Lead or 12-Lead Stator Windings (Wye / Delta Configurable)",
            "Ground Steel Keyed Output Shaft (1.125\" - 1.375\" Diameter [TYPICAL])"
        ],
        "avoid": "Lifting without mechanical crane/hoist; dropping rotor onto stator teeth can gouge slot insulation varnish",
        "bestFor": "Rotary Phase Converter (RPC) Idler Generator (produces utility-grade 3-phase power from 240V single-phase), Heavy Wood Lathe Headstock, 100% Duty Shop Air Compressor Head",
        "triage": "Measure all 9 or 12 leads to identify 3 distinct phase winding groups with DMM. Verify phase resistance matches within 1.5% [TYPICAL]. Test stator insulation with 1,000V DC megohmmeter (must exceed 50 Megohms [VERIFIED])."
    },
    {
        "id": "commercial_vav_air_damper",
        "name": "Commercial HVAC VAV Damper & Airfoil Blades (Titus / Trane)",
        "cat": "kinematics",
        "danger": "Pinch Hazard / Fiberglass Insulation Dust",
        "dangerColor": "#10b981",
        "harvest": [
            "Extruded Aluminum Aerodynamic Airfoil Damper Blades with Molded Silicone Seals",
            "Precision Stainless Steel Hexagonal Interconnecting Drive Shafts (0.5\" Hex [TYPICAL])",
            "Synchronous Counter-Rotating Intermeshing Delrin Gear Train",
            "Low-Friction Celcon Bearing Bushings with < 0.05mm Play [TYPICAL]"
        ],
        "avoid": "Direct skin contact with fiberglass duct lining inside VAV box casing (wear gloves and N95 respirator)",
        "bestFor": "Laser Cutter Automated Clean-Air Blast Gate, Blacksmith Forge Air Blast Control Valve, Wind Tunnel Flow Collimating Vanes, Multi-Zone Ventilation Damper",
        "triage": "Rotate master drive shaft by hand: verify smooth 90-degree blade rotation with zero binding. Inspect silicone blade seals for complete elastic recovery."
    },
    {
        "id": "robotic_welder_wire_feeder",
        "name": "Industrial Robotic MIG Welder Wire Feeder (Lincoln / Miller)",
        "cat": "workshop",
        "danger": "Mechanical Pinch in Knurled Rollers / 42V DC Electrical",
        "dangerColor": "#f59e0b",
        "harvest": [
            "Heavy-Duty 24V/42V DC High-Torque Planetary Geared Drive Motor",
            "4-Roll Geared Hardened Knurled Steel Feed Roll Assembly with Spring Tensioners",
            "Heavy Forged Brass Euro-Torch Power & Shielding Gas Quick-Disconnect Block",
            "24V DC Direct-Acting High-Flow Shielding Gas Solenoid Valve"
        ],
        "avoid": "Running unguided wire through knurled rolls without correct drive groove profile (causes wire shaving and jam)",
        "bestFor": "Large-Format 3D Metal Wire Arc Extruder (WAAM), Automated Coil / Transformer Winding Machine, High-Tension Puller & Wire Straightener, CNC Sheet Metal Feed Table",
        "triage": "Power motor with 24V DC variable PSU; check speed range from 50 to 800 inches/minute [TYPICAL]. Test shielding gas solenoid with 24V DC; verify zero pneumatic leakage when closed."
    },
    {
        "id": "aircraft_starter_generator",
        "name": "Turboprop / Helicopter Starter-Generator (Lucas / Safran 28V 250A)",
        "cat": "auto",
        "danger": "Extreme Kinetic Power Density / High-Current Arc-Flash (Up to 400A)",
        "dangerColor": "#ef4444",
        "harvest": [
            "High Power-to-Weight 28V DC Starter-Generator (6 kW - 9 kW Continuous [TYPICAL], Weight < 18 kg)",
            "High-Altitude Silver-Graphite Brush Rig & Laminated Commutator Assembly",
            "Precision Involute Splined Drive Shaft with Internal Torsion Damping",
            "Dual Field Stator Windings (Series Starting Winding + Shunt Generating Winding)"
        ],
        "avoid": "Continuous cranking duty exceeding 30 seconds (causes thermal saturation and commutator bar desoldering)",
        "bestFor": "Off-Grid Micro-Hydro High-Output Turbine Generator, High-Current Electric Vehicle DC Fast-Charger, Heavy-Duty Electric Recovery Winch, Aircraft Ground Power Unit (GPU)",
        "triage": "Inspect commutator bars for uniform chocolate patina; measure brush remaining length (must exceed 15mm [TYPICAL]). Measure series winding resistance (< 0.02 ohms [TYPICAL]) and shunt field resistance (12-18 ohms [TYPICAL])."
    }
]

def add_new_donors():
    with open(ENCARTA_DATA_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the end of DONORS_DATA
    # DONORS_DATA = [ ... ]
    import json
    new_entries_str = ""
    for d in NEW_DONORS:
        # Check if already present
        if f'"id": "{d["id"]}"' in content:
            print(f"Donor {d['id']} already present in encarta_data.py")
            continue
        formatted = "    {\n"
        formatted += f'        "id": "{d["id"]}",\n'
        formatted += f'        "name": "{d["name"]}",\n'
        formatted += f'        "cat": "{d["cat"]}",\n'
        formatted += f'        "danger": "{d["danger"]}",\n'
        formatted += f'        "dangerColor": "{d["dangerColor"]}",\n'
        formatted += f'        "harvest": {json.dumps(d["harvest"])},\n'
        formatted += f'        "avoid": "{d["avoid"]}",\n'
        formatted += f'        "bestFor": "{d["bestFor"]}",\n'
        formatted += f'        "triage": "{d["triage"]}"\n'
        formatted += "    },\n"
        new_entries_str += formatted

    if not new_entries_str:
        print("No new donors to add.")
        return

    # Insert before the end of DONORS_DATA
    # Locate where BLUEPRINTS_DATA begins
    marker = "BLUEPRINTS_DATA = ["
    idx = content.find(marker)
    if idx == -1:
        raise ValueError("Could not find BLUEPRINTS_DATA marker in encarta_data.py")

    # Find the last closing bracket before BLUEPRINTS_DATA
    sub = content[:idx]
    last_bracket = sub.rfind("]")
    if last_bracket == -1:
        raise ValueError("Could not find end of DONORS_DATA bracket")

    updated_content = content[:last_bracket] + new_entries_str + content[last_bracket:]

    # Update donor count comment at top of file
    updated_content = updated_content.replace("- 88 Donor Scrap Streams", "- 100 Donor Scrap Streams")

    with open(ENCARTA_DATA_PATH, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print(f"[OK] Added {len(NEW_DONORS)} new donor streams to scripts/encarta_data.py.")

if __name__ == "__main__":
    add_new_donors()
