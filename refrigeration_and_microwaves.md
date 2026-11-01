# ❄️ Volume 3.3: Refrigeration & Microwave Electromechanics
*Whisper-quiet hermetic compressors, synchronous turntable gearmotors, and rewound MOT spot welders.*

---

## 1. Refrigerator & Freezer Hermetic Compressors

```
Hermetic Compressor Cutaway Anatomy:
+--------------------------------------------------------------+
| Heavy Welded Steel Pressure Vessel                           |
|                                                              |
|   [Suction Stub] ---> [Internal Silencer / Oil Baffle]       |
|                                     |                        |
|   [Single-Phase Induction Motor] <---+                       |
|   (Submerged in mineral oil)        |                        |
|                 |                   v                        |
|          (Eccentric Crank) ===> [Reciprocating Piston]       |
|                                     |                        |
|   [Discharge Stub] <----------------+ (High-Pressure Reed)   |
|   (Pumps up to 250+ PSI or pulls 28+ inHg Vacuum)            |
+--------------------------------------------------------------+
```

### Why Makers Love Fridge Compressors:
Standard piston workshop air compressors roar at deafening noise levels (85 to 95 dB).
- Because a refrigerator compressor is permanently sealed inside a heavy welded steel sound-insulating shell and suspended on internal dampening springs, it operates at **under 40 dB (virtually silent)**.
- Can deliver air pressure upwards of **250 PSI** or pull a continuous vacuum down to **28 to 29 inHg**.

---

### Step-by-Step Repurposing Exploits:

#### A. The Ultra-Silent Indoor Airbrush / Shop Air Station
```
Airbrush System Flow:
[Compressor Exhaust] ---> [Check Valve] ---> [Air Tank (Fire Extinguisher)]
                                                   |
                                            [Pressure Switch (30-40 PSI)]
                                            [ASME Safety Pop-Off Valve]
                                                   |
                                            [Oil Coalescing Filter]
                                                   |
                                                   v
                                          [Clean, Dry 30 PSI to Airbrush]
```
1. **Oil Management**: Because the compressor's mechanical components splash in an internal oil bath, the exhaust air contains a fine mist of mineral oil. You **must** install a high-efficiency **oil-coalescing filter** before the airbrush line to prevent paint contamination.
2. **Pressure Control**: Wire an automatic pressure switch set to turn the compressor ON at 30 PSI and OFF at 45 PSI.
3. **Safety Relief Valve**: Never omit an ASME-rated 100 PSI safety pop-off valve on your receiver tank.

#### B. Deep Vacuum Degassing & Wood Stabilization Chamber
- Plumb the **suction (inlet)** stub to a heavy stainless steel stockpot.
- Cap the pot with a **3/4-inch to 1-inch thick clear polycarbonate (Lexan) lid** equipped with a soft silicone perimeter gasket. (Never use glass or brittle acrylic!).
- Pulls vacuum down to **28.5 inHg within 60 seconds**:
  - **Silicone & Resin Degassing**: Expands and violently boils out all trapped microscopic air bubbles from platinum silicone and clear casting resins before pouring.
  - **Cactus Juice Wood Stabilization**: Evacuates all air from punky, spalted wood blanks, allowing stabilizing monomer resin to saturate the wood cells completely.

---

## 2. Microwave Ovens: Safe Turntable Motors & Modified MOTs

```
Turntable Gearmotor Internal Gear Train:
[120V/240V AC [TYPICAL] Synchronous Stator] ===(Multi-Stage Plastic Gears)===> [Output D-Shaft]
                                                                          |
                                                                          v
                                                                Turns at 2.5 to 5 RPM [TYPICAL]
                                                                with ~10-15 lb-in Torque
```

### A. The Turntable Synchronous Gearmotor (100% Safe)
- **Characteristics**: Compact metal can running directly from 120V or 240V AC [TYPICAL] mains. Internal planetary gear reduction produces **2.5 to 5 RPM [TYPICAL]** with surprising torque. Features a mechanical dog clutch that reverses direction automatically if the shaft hits a physical obstruction.
- **Repurposing Projects**:
  - **Epoxy Resin Cup / Tumbler Rotator**: Rotates custom glitter tumblers continuously for 8 hours while two-part epoxy cures, ensuring a mirror-flat coat without sags or drips.
  - **Rock & Shell Polishing Tumbler**: Drives a rubber-lined PVC drum for tumbling raw gemstones and sea glass.
  - **Slow-Motion Camera Panorama Mount**: Pan a DSLR camera 360° over 15 to 20 seconds for seamless panoramic shots.

---

### B. The Modified MOT (Microwave Oven Transformer) Battery Spot Welder

> [!CAUTION]
> **LETHAL HAZARD**: As stated in Volume 0.1, the stock secondary winding of an MOT carries **2,000V+ at 1 Amp**. You must physically cut out and remove the secondary winding before connecting this transformer to any circuit.

```
MOT Spot Welder Conversion Topology:
+-------------------------------------------------------------+
| [Primary Coil (Untouched 120V/240V Mains)]                  |
|                             |                               |
|               (Heavy Iron Transformer Core)                 |
|                             |                               |
| [New Secondary: 2 to 3 Turns of 2 AWG Welding Cable]        |
|                             |                               |
|                             v                               |
| ====> Safe 3.5V AC @ 600 to 800 Amps Instantaneous Current! |
+-------------------------------------------------------------+
```

#### The Conversion Protocol:
1. Unplug the microwave and discharge the high-voltage capacitor safely. Remove the transformer.
2. Clamp the MOT in a bench vise. Using a hacksaw or oscillating multi-tool, carefully saw off the protruding loops of the **fine-wire high-voltage secondary winding**. Be extremely careful not to scratch or nick the primary coil (the thicker copper wire winding at the bottom).
3. Knock out the remaining secondary copper wire chunks using a hammer and wooden dowel. Remove the small magnetic shunt plates if necessary.
4. Pass **two to three turns of ultra-thick, flexible 2 AWG or 0 AWG copper welding cable** through the core window where the secondary used to sit.
5. Terminate the cable ends into solid copper welding tip electrodes.
6. **The Result**: When connected to mains power, the transformer steps down voltage to a completely safe **3.5V to 4.0V**, while stepping up available current to an astronomical **600 to 800 Amps**.
7. Connect the primary side to an AC solid-state relay (SSR) controlled by an Arduino timer (pulsing for 20 to 50 milliseconds) to build a professional-grade spot welder that welds nickel strips onto 18650 lithium battery cells instantly without heating the battery chemistry.

---

## 3. Omron 15A Snap-Action Microswitches
- Microwave oven door interlocks contain three heavy-duty snap-action microswitches rated for **15 Amps at 250V AC**.
- These switches feature hardened silver-cadmium contacts and audible positive click detents.
- *Repurposing*: The ultimate indestructible homing and emergency limit switches for large CNC routers, milling machines, and automated gates.

---

## 4. Induction Cooktops (1,800W): High-Frequency Resonant Salvage

Discarded portable single-burner and slide-in induction cooktops (cracked ceran glass tops frequently tossed on curbsides or found at thrift stores for $5–$15) contain an extraordinary treasure trove of high-frequency power electronics and thermal hardware:

```
+--------------------------------------------------------------------------+
| Scrap Induction Cooktop Power Core:                                      |
|                                                                          |
| [ Heavy Litz-Wire Pancake Coil ] <---> [ 0.3µF-5µF 1200V MKP Capacitors ] |
|               ^                                      ^                   |
|               |                                      |                   |
|               +---- [ High-Current 1200V IGBTs ] ----+                   |
|                     (H20R1203 / FGA25N120 on Heatsink)                   |
+--------------------------------------------------------------------------+
```

### A. The Litz-Wire Induction Pancake Coil
- **Component**: Spiral-wound pancake work coil sitting directly underneath the cooking glass.
- **Construction**: Made from hundreds of individually enameled fine copper strands braided together (**Litz wire**). This geometry completely eliminates the **high-frequency skin effect** (where current is forced to flow only on the outer perimeter of solid conductors) at resonant frequencies between $20\text{ kHz}$ and $50\text{ kHz}$.
- **Center Ferrite Bars**: The back of the coil is lined with radial ferrite flux concentrator bars that direct electromagnetic field lines upward and prevent magnetic flux from coupling into the internal electronics chassis.

### B. High-Voltage, High-Current Resonant IGBTs & MKP Capacitors
- **IGBTs**: Heavy-duty discrete power transistors—typically **H20R1203, FGA25N120, or IHW20N120R3** rated for **20A to 40A continuous** at **1,200V breakdown voltage**, with integrated ultra-fast anti-parallel freewheeling diodes.
- **MKP Resonant Tank Capacitors**: Heavy metallized polypropylene film capacitors rated for **0.3 µF to 5.0 µF at 1,200V DC / 400V AC pulse rating**. These capacitors feature ultra-low equivalent series resistance (ESR) and can pass tens of amperes of continuous high-frequency circulating current without dielectric heating.
- **Heatsink & Blower**: A high-efficiency extruded aluminum tunnel heatsink with an integrated low-profile centrifugal blower fan designed to cool the bridge rectifier and IGBTs.

### C. Repurposing Exploits:
1. **Zero-Voltage Switching (ZVS) Blacksmith Induction Forge**: Wire the salvaged MKP capacitors in parallel with a custom water-cooled copper tube work coil, driven by the salvaged IGBTs in a self-resonant Mazzilli ZVS topology (detailed in **Blueprint 14**). Heats 1/2" steel rebar to bright cherry red ($1,000^\circ\text{C}$) in 15 seconds without smoke or combustion.
2. **Crucible Induction Metal Melter**: Wind the Litz wire or copper tubing around a ceramic or graphite crucible to melt aluminum, brass, or copper scrap indoors using pure electromagnetic induction.
3. **Automotive Rusted Bolt Heater**: Drive a flexible coiled cable head with high-frequency AC to inductively heat seized suspension bolts red-hot in seconds without an open oxy-acetylene torch flame near brake lines or fuel tanks.

---

## 5. HVAC Definite Purpose Contactors: Master E-Stops

Harvested from central air conditioner condenser units and heat pumps:
- **Component**: 30A to 50A double-pole definite purpose contactors with heavy silver-alloy contact pads and enclosed mechanical arc chutes.
- **Coil Options**: Typically 24V AC [TYPICAL] (residential thermostat control) or 120V AC [TYPICAL] (commercial units).
- **Repurposing Target**: The ideal master safety interlock for multi-horsepower garage tools (2x72 belt grinders, heavy lathes, drill presses, ceramic kilns). Wire the contactor in a **self-latching circuit** with a red twist-to-release emergency-stop mushroom button. If mains power fluctuates or the E-stop is slapped, the contactor snaps open instantly, physically severing both hot conductors and preventing automatic unexpected tool restarts when power is restored.
