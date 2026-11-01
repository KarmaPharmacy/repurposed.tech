# ⚠️ Volume 0.1: Scrapper's Safety Protocols & Lethal Hazards Field Guide
*The non-negotiable rules for hardware dismantling, toxic mitigation, and life preservation.*

> [!IMPORTANT]
> ### Salvage Engineering Epistemic Classification Standard
> All technical parameters, ratings, formulas, and procedures in this field guide adhere to the five-state epistemological framework:
> - **`[VERIFIED]`**: Empirically measured in shop tests or confirmed by manufacturer datasheet.
> - **`[CALCULATED]`**: Mathematically derived from first physical principles and stated inputs.
> - **`[TYPICAL]`**: Standard industrial component benchmark or statistical salvage average.
> - **`[ASSUMED]`**: Stated engineering design assumption; subject to prototype validation.
> - **`[UNKNOWN]`**: Unverified scrap variable requiring active bench instrumentation before power-up.

---

## 1. Electrical Hazards: The Silent Killers

### A. High-Voltage Capacitors & Stored Energy
Electronic equipment can hold lethal energy hours, days, or months after being disconnected from wall power. 

```
Stored Energy Formula:
  E = 0.5 * C * V^2  [VERIFIED]
  Where:
    E = Energy in Joules
    C = Capacitance in Farads
    V = Voltage across terminals
```
*Note: A shock exceeding **10 Joules** is hazardous; **50 Joules** across the chest is frequently fatal.*

| Donor Equipment | Component | Typical Stored Voltage | Typical Capacitance | Stored Energy | Danger Level |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Microwave Oven** | High-Voltage Capacitor | 2,100V – 2,500V AC/DC [TYPICAL] | 0.9 µF – 1.1 µF [TYPICAL] | ~3.0 J (High Voltage Arc) | 🔴 Extremely High |
| **Old CRT Monitors / TVs** | Anode Tube / Flyback Cap | 15,000V – 30,000V DC [TYPICAL] | 1,000 pF – 2,000 pF [TYPICAL] | ~0.5 – 1.0 J (Reflex shock) | 🔴 High / Fall hazard |
| **Camera Strobe / Xenon Flash** | Photoflash Electrolytic | 330V DC [TYPICAL] | 120 µF – 350 µF [TYPICAL] | ~10 J – 19 J | 🔴 Severe Burn / Fibrillation |
| **Variable Frequency Drive (VFD)**| DC Bus Filter Banks | 320V – 650V DC [TYPICAL] | 1,000 µF – 4,700 µF [TYPICAL] | **100 J to 1,000+ J** | ☠️ LETHAL |
| **Desktop ATX Power Supply** | Primary Electrolytic Caps | 200V – 400V DC [TYPICAL] | 470 µF – 1,000 µF [TYPICAL] | ~20 J – 80 J | 🔴 Severe Shock / Burn |

#### Safe Discharge Procedure (The "Resistor Stick"):
- **NEVER** use a bare screwdriver to short capacitor terminals directly. The instantaneous microsecond discharge produces an explosive arc flash that can weld the screwdriver tip, vaporize metal into your eyes, and rupture the capacitor casing.
- **Fabricate a Discharge Wand**: Connect a **1 kΩ to 5 kΩ, 25-Watt to 50-Watt ceramic wirewound resistor** across two heavily insulated probes (rated for 1,000V+).
- Connect the alligator clip of one probe to the capacitor's negative or chassis ground terminal.
- Firmly press the insulated resistor probe to the positive terminal and hold for **10 full seconds**.
- Verify zero residual potential with a digital multimeter set to DC volts before touching any part of the circuit.

---

### B. Microwave Oven Transformers (MOT)

> [!CAUTION]
> **LETHAL HAZARD: MICROWAVE OVEN TRANSFORMERS (MOT)**
> An unmodified MOT produces 2,100V–2,500V AC at 500mA–1,000mA `[TYPICAL]`. This current is **10 to 20 times the threshold for instantaneous fatal ventricular fibrillation** `[VERIFIED]`. Unlike ignition coils or stun guns, an MOT has zero internal current limiting. Contact with the secondary winding is almost universally fatal. **Never power an unmodified MOT on an open workbench.**
The stock high-voltage transformer from a domestic microwave oven step-ups 120V/240V mains up to **2,000V–2,400V AC at 500mA to 1,000mA (0.5 to 1 Amp) [TYPICAL]**.

> [!CAUTION]
> **Zero Tolerance**: The human threshold for "cannot let go" muscular paralysis is roughly **10 to 16 mA**. Ventricular fibrillation occurs at **50 to 100 mA**. A stock microwave transformer delivers **10 times the current required to stop a human heart instantly**.
> - **RULE**: NEVER power on a stock microwave transformer on your bench. 
> - **RULE**: The ONLY safe way to repurpose an MOT is to physically cut out and remove the secondary high-voltage winding while completely unpowered, replacing it with 2–3 turns of low-voltage heavy-gauge welding cable (turning it into a safe 3.5V high-current source for spot welding).

---

## 2. Chemical, Heavy Metal & Toxic Substance Hazards

```
+--------------------------------------------------------------------------+
| TOXIC CONTAMINANT MATRIX                                                 |
|                                                                          |
| Component                 Toxin                 Action Required          |
| ------------------------------------------------------------------------ |
| Microwave Magnetron Dome  Beryllium Oxide (BeO) NEVER grind/sand ceramic |
| Fluorescent Backlights    Mercury Vapor         Do not fracture glass    |
| Old Thermostats/Switches  Liquid Mercury        Seal in glass jar if found|
| Lead-Acid / CRT Glass     Lead / Lead Oxide     Wash hands, do not grind |
| NiCad Power Tool Packs    Cadmium               Recycle intact           |
| Lithium Pouch / Cylinders Flammable Electrolyte No puncture; sand bucket |
+--------------------------------------------------------------------------+
```

### A. Beryllium Oxide (BeO) in Microwave Magnetrons

> [!WARNING]
> **CARCINOGENIC HAZARD: BERYLLIUM OXIDE (BeO) CERAMIC**
> The pink, white, or off-white ceramic insulators at the top and base of magnetron antenna domes frequently consist of sintered Beryllium Oxide (`BeO`) `[TYPICAL]`. While inert in solid form, **inhalation of BeO particulate causes chronic beryllium disease (berylliosis), an incurable and fatal pulmonary granulomatosis** `[VERIFIED]`. Never scratch, saw, sand, dremel, file, or crush magnetron ceramic rings.
- **Where it is found**: Inside the microwave magnetron assembly (the RF generator tube), the ceramic insulator collars (often colored off-white, light grey, or pink) frequently contain **Beryllium Oxide**.
- **The Risk**: In solid form, BeO ceramic is safe to handle. However, if you attempt to crush, cut, sand, or grind this ceramic, the resulting microscopic airborne dust causes **Berylliosis**—an incurable, chronic, and potentially fatal granulomatous lung disease.
- **Protocol**: When harvesting the large ferrite ring magnets from a microwave magnetron, **unbolt or bend the sheet metal casing only**. Do not chisel, saw, or fracture the ceramic insulator core.

### B. Mercury in CCFL Tubes & Vintage Switches
- Flatbed scanners, older LCD monitors, and photocopy machines often use Cold Cathode Fluorescent Lamps (CCFLs) for illumination.
- These long glass tubes contain small amounts of elemental mercury and phosphor coatings. If fractured, mercury vapor is released instantly. Always remove the CCFL intact, or choose newer LED-illuminated donors.

### C. Lithium-Ion Thermal Runaway & Battery Salvage
Harvesting 18650 or 21700 lithium-ion cells from discarded laptop batteries, hoverboards, and power tool packs is one of the most rewarding parts of maker life, but demands rigorous safety protocols:
1. **Never Harvest Cells Below 1.5V**: If an 18650 cell has sat discharged below 1.5V for extended periods, internal copper shunts and dendrites form. Recharging such cells can cause internal micro-shorts leading to violent thermal runaway days later.
2. **Never Cut Through Nickel Strips with Conductive Wire Cutters Across Terminals**: Touching the positive rim and negative can simultaneously causes an immediate short circuit that will weld your cutters and ignite the cell.
3. **Emergency Suppression**: Lithium battery fires cannot be extinguished with water or standard ABC dry chemical extinguishers. Keep a metal bucket of clean, dry play sand nearby to bury any cell that begins venting or overheating.

---

## 3. Stored Mechanical Energy (Springs & Implosions)

### A. Coiled Clockwork Torsional Springs
```
        /-----\
      /   ---   \
     |   / - \   |  <=== Tightly coiled spiral spring under immense
      \  \---/  /        tension inside plastic housing!
        \-----/
```
- **Where found**: Lawnmower pull-start assemblies, retractable vacuum cleaner cord winders, tape measures, roll-up window blinds, and garage door openers.
- **Hazard**: These housings enclose several feet of hardened spring steel coiled under high rotational tension. Opening the shell without releasing tension causes the spring to explode outward like a razor-sharp steel whip.
- **Mitigation**: Wear heavy leather welding gloves and a polycarbonate full-face shield. Slowly unwind the spool until all mechanical tension is relieved before unfastening central pins.

### B. Vacuum Chamber Implosion Physics
When repurposing refrigerator compressors to create DIY vacuum chambers:
- **Atmospheric Pressure**: Atmospheric pressure at sea level is **14.7 pounds per square inch (PSI)**.
- Over a modest 12-inch diameter circular chamber lid, the total atmospheric crushing force pressing down under full vacuum is:
  $$\text{Area} = \pi \times r^2 = \pi \times 6^2 \approx 113.1 \text{ sq inches}$$ [CALCULATED]
  $$\text{Total Force} = 113.1 \times 14.7 \approx 1,662 \text{ pounds of force!}$$ [CALCULATED]
- **Material Rules**:
  - **NEVER use flat window glass or plate glass**: Glass possesses microscopic surface flaws. Under 1,600 lbs of load, it shatters without warning, spraying thousands of glass daggers inward and outward.
  - **NEVER use cheap extruded acrylic (Plexiglas)**: Acrylic suffers from "crazing" when exposed to alcohol, solvents, or cyclic tension, and shatters brittlely under vacuum.
  - **USE Cast Polycarbonate (Lexan)**: Minimum **3/4-inch to 1-inch thickness**. Polycarbonate has exceptional impact resistance and will bow noticeably rather than shatter if overloaded.
  - **USE Heavy Stainless Steel Stockpots or Pressure Cooker Bases**: Avoid thin sheet aluminum pots that can collapse like soda cans.

---

## 4. Refrigerant & Pressurized Gas Regulations
- **Environmental & Legal Mandate**: In many jurisdictions (e.g., US EPA Section 608), venting fluorocarbon refrigerants (R-12, R-22, R-134a) to the atmosphere is a severe federal violation. 
- **Hydrocarbon Hazard (R-600a / Isobutane)**: Modern domestic refrigerators frequently utilize **R-600a (isobutane)**. It is ozone-friendly but **extremely flammable**. Cutting compressor lines with an angle grinder or torch while flammable refrigerant remains inside can trigger an explosion.
- **Protocol**: Only harvest compressors from refrigerators that have been professionally evacuated and tagged by a certified HVAC recovery technician, or score scrap units where lines are already cleanly opened.

---

## 5. High-Voltage DC Arc-Flash & EV Pre-Charge Physics

### A. The Continuous DC Plasma Arc vs AC Zero-Crossing
When scrapping or repurposing modern **Electric Vehicles (Nissan Leaf, Chevy Volt, Tesla Model S/3)** or building high-voltage solar battery banks (48V to 400V DC), you enter a completely different electrical physics regime than 120V/240V AC [TYPICAL] mains.

```
AC Waveform (Naturally Extinguishes Arcs):
Voltage
   ^      +---\         /---\
   |     /     \       /     \
  0+----+-------*-----+-------*-----+--> Time (crosses zero 120x/sec)
   |             \---/         \---/

DC Potential (Sustains Continuous Incinerating Arc):
Voltage
   ^    =================================> 400V Constant DC
   |    (NO zero-crossing! Continuous plasma flame melts switches)
  0+-------------------------------------> Time
```

- **The Zero-Crossing Difference**: Standard AC voltage cycles at 50 Hz or 60 Hz, crossing zero volts 100 to 120 times every second. This momentary zero potential allows the ionized air gap across opening switch contacts to cool and naturally de-ionize, extinguishing sparks.
- **The DC Arc Trap**: DC voltage maintains a **continuous, non-zero electrical potential**. If you open an ordinary AC knife switch, circuit breaker, or automotive 12V relay carrying 100A+ at 48V–400V DC, the current ionizes the air into an incandescent, deafening plasma arc that will not extinguish. The arc acts as an open-air plasma cutting torch, vaporizing copper contacts, melting terminal blocks, and causing explosive flash fires.
- **Mandatory Salvage Hardware**: Always use **hermetically sealed, nitrogen- or hydrogen-filled DC contactors** (e.g., Gigavac, Kilovac, or salvaged EV contactors) equipped with internal permanent magnetic blowout magnets that physically push the plasma arc against ceramic arc-chute splitters.

### B. The Pre-Charge Rule (Preventing Contactor Welding)
When connecting a high-voltage battery pack (48V–400V) to motor controllers (VESC, ODrive, Kelly, or EV inverters), the input stage consists of massive, low-ESR electrolytic capacitor banks.

```
       +-------------------[ Main Contactor ]-------------------+
       |                                                        |
(+) ---+                                                        +---> To Controller (+)
       |                                                        |     (Massive Low-ESR
       +---[ Momentary Pushbutton ]---[ 30Ω-50Ω 100W Resistor ]-+      Capacitor Bank)
                                                                        [C_in = 2000µF]
(-) -----------------------------------------------------------------> To Controller (-)
```

- **Inrush Current Mechanics**: Uncharged capacitors appear as a **dead electrical short** ($R \approx 0$). At the microsecond of contact closure, inrush current is limited only by cable impedance:
  $$I_{\text{inrush}} = \frac{V_{\text{pack}}}{R_{\text{cable}}} = \frac{400\text{ V}}{0.05\ \Omega} \approx 8,000\text{ Amperes!}$$ [CALCULATED]
- **Contactor Destruction**: An 8,000A transient creates instantaneous micro-arcing that liquifies the silver alloy contact tips, permanently **welding the main contactor shut**. If a subsequent control failure occurs, the system cannot be disconnected.
- **The Pre-Charge Protocol**:
  1. Wire a salvaged **30$\Omega$–50$\Omega$, 50W–100W wirewound ceramic resistor** in series with a momentary high-voltage pushbutton (or secondary pre-charge relay) across the main contactor terminals.
  2. Press and hold the pre-charge button for **2 to 3 seconds** prior to engaging the main contactor. Current is safely throttled ($I_{\text{peak}} \approx 400\text{V} / 50\Omega = 8\text{A}$), charging the DC-link capacitor bank to $\ge 90\%$ of battery voltage.
  3. Close the heavy main contactor only after capacitor voltage has equalized ($V_{\text{contactor}} \approx 0\text{V}$ across terminals). Zero differential voltage means zero inrush and zero contact erosion.

---

## 6. Piezoelectric Pyroelectricity & Langevin Transducer Shock

When harvesting or modifying **Langevin ultrasonic transducers**, ultrasonic cleaning baths, or dental scalers (detailed in Volume 7.2):

```
       [ Aluminum Tail Mass ]
      ------------------------
       (+) Copper Electrode   <=== SPONTANEOUS HIGH VOLTAGE GENERATION
      ========================     DURING SOLDERING OR FLAME HEATING!
       (PZT Ceramic Ring 1)
      ------------------------     Terminals MUST be shorted with clip leads
       (-) Copper Electrode
      ========================
       (PZT Ceramic Ring 2)
      ------------------------
       [ Titanium Horn Mass ]
```

- **The Pyroelectric Effect**: Lead Zirconate Titanate (PZT) piezoceramic rings are ferroelectric crystals with polar domains aligned during factory manufacturing. Rapid temperature changes ($\Delta T$) cause rapid thermal expansion/contraction of the crystal lattice, generating a spontaneous surface charge displacement.
- **The Hazard**: Soldering wire leads to the electrode rings or applying a heat gun / torch to loosen retaining bolts can generate **several hundred volts to over 1,000 volts DC** across the bare terminals without any external power source. Touching the leads will deliver a painful, high-voltage jolt.
- **Assembly Protocol**:
  1. **Short the Terminals**: Always clip an insulated alligator jumper wire directly across the positive and negative electrode tabs before soldering, brazing, or mechanically unbolting transducer stacks.
  2. **Never Run Unloaded in Air**: PZT transducers driven at resonance with an RF amplifier without an acoustic mechanical load (water bath, sonotrode cutting blade, or dampener) experience uncontrolled mechanical Q-factor amplification. Internal mechanical stress exceeds the tensile limit of the ceramic, causing the PZT rings to instantaneously shatter into fragments. Always bench-test transducers immersed in liquid or coupled to their designed tool horn.

---

## 7. Neodymium "Pinch-Shatter" Shrapnel & Curie Demagnetization

Salvaging heavy rare-earth permanent magnets (N45 to N52 NdFeB) from 3.5" enterprise server hard drives, hoverboard hub motors, wind turbine direct-drives, or medical MRI surplus introduces severe mechanical and thermal hazards:

```
 [ Magnet A (Free) ] ============> 40 MPH Impact Velocity! <============ [ Magnet B (Clamped) ]
                                            |
                                            v
                      * * * PYROPHORIC SHRAPNEL EXPLOSION! * * *
                      (Razor-sharp flying shards + spontaneous sparking)
```

### A. Mechanical Impact & Pyrophoric Fracturing
- **Extreme Kinetic Acceleration**: Two 2-inch neodymium magnets separated by 4 inches generate attractive forces exceeding **100 to 200 lbs**. When released, they accelerate toward each other at over **40 MPH**, creating bone-crushing pinch points that can shear fingertips or fracture finger bones.
- **Ceramic Brittleness**: Sintered Neodymium-Iron-Boron is not ductile metal; it is a brittle sintered intermetallic ceramic. Upon violent collision, the magnets do not dent—they **explosively shatter into microscopic razor-sharp slivers**.
- **Pyrophoric Sparking**: Freshly exposed neodymium metal powder is **pyrophoric** (it oxidizes exothermically in air). Violent fractures spark spontaneously, creating an ignition risk around flammable degreasing solvents or battery venting gases.
- **Handling SOP**:
  1. Never pry magnets apart face-to-face. Always **slide magnets apart laterally** along their shear plane using a non-magnetic wooden or high-density plastic wedge jig.
  2. Keep salvaged magnets wrapped in thick bubble wrap or stored inside individual wooden separator boxes with at least 2 inches of spacing.
  3. Wear ANSI-rated safety goggles and thick split-cowhide work gloves whenever separating high-strength magnets.

### B. The $80^\circ\text{C}$ Curie Temperature Trap
- **Thermal Demagnetization**: Standard commercial N-grade neodymium magnets have a maximum operating temperature of only **$80^\circ\text{C}$ ($176^\circ\text{F}$)**. Above this threshold, thermal vibration disrupts the aligned magnetic domains, causing permanent, irreversible loss of magnetic flux.
- **Machining Destruction**: Cutting neodymium magnets with dry abrasive Dremel wheels or angle grinders instantly heats the cut zone past $200^\circ\text{C}$, completely destroying their magnetism while producing toxic, flammable rare-earth dust.
- **Welding Near Rotors**: When fabricating custom steel motor mounts, never weld directly onto an alternator rotor bell, hoverboard casing, or direct-drive wheel with magnets installed. Always dismantle the rotor completely before welding, or clamp wet soaking-wet cotton rags directly against the magnets to maintain core temperature below $50^\circ\text{C}$.

---

## 8. $SF_6$ (Sulfur Hexafluoride) & Decomposed Arc Byproducts

Surplus high-voltage industrial distribution equipment, utility substation circuit breakers, medium-voltage switchgear (13.8 kV+), and high-power medical radar/X-ray pulse tanks frequently utilize **Sulfur Hexafluoride ($SF_6$)** as a dielectric insulating gas.

> [!CAUTION]
> **LETHAL ARC BYPRODUCT HAZARD**: While pure $SF_6$ is non-toxic (though a potent greenhouse gas), electrical arcing decomposes $SF_6$ into lethal chemical compounds.

- **Decomposition Chemistry**: Under high-energy electrical discharge or internal arc faults, $SF_6$ reacts with moisture and copper/tungsten contacts to form:
  - **Disulfur decafluoride ($S_2F_{10}$)**: A gas roughly as toxic as phosgene, destroying lung tissue upon inhalation.
  - **Thionyl fluoride ($SOF_2$) & Sulfur tetrafluoride ($SF_4$)**: Highly corrosive acidic vapors.
  - **Hydrofluoric Acid ($HF$) Residue**: Forms a fine white, gray, or yellowish powder coating the interior walls and contact assemblies.
- **Triage & Refusal Rules**:
  1. If an industrial HV gas tank or sealed switchgear enclosure shows signs of blackening, scorching, or internal pressure loss, **DO NOT DRILL, CUT, OR CRACK THE FLANGES**.
  2. Inhaling microgram quantities of hydrolyzed $SF_6$ powder produces delayed-onset pulmonary edema (fluid in the lungs) and severe chemical pneumonia hours after exposure.
  3. Any salvaged high-voltage gas chamber with an active pressure gauge or sealed rupture disc must be verified clean and vented by professional utility recovery specialists prior to scrap teardown.

---

## 9. Dielectric Absorption ("Capacitor Rebound" Voltage)

When servicing or salvaging high-energy capacitors—such as large electrolytic DC-bus capacitors from variable frequency drives (VFDs), photoflash capacitors from studio strobes, defibrillator energy storage cans, or oil-filled microwave/laser capacitors:

```
  Step 1: Probe Discharge Wand               Step 2: Remove Wand & Wait 5 Minutes
  +--------------------------------+         +--------------------------------+
  | [ Capacitor Voltage = 0.0V ]   |         | [ SPONTANEOUS RECHARGE! ]      |
  | (Probe momentarily shorts bus) |         | (Voltage Rebounds to 15-25%!)  |
  +--------------------------------+         +--------------------------------+
                                                             |
                                                             v
                                             Lethal 50V - 250V Jolt to Hand!
```

- **The Molecular Relaxation Physics**: Under high-voltage stress, polar molecules in the dielectric material (polymer film, ceramic, paper-oil, or aluminum oxide electrolyte) physically twist and align with the electric field. Discharging the terminals with a 1 k$\Omega$ safety wand empties the free charge on the metal plates in seconds, reading $0.0\text{V}$ on a DMM.
- **The Rebound Hazard**: The moment the external discharge wand is removed, the polarized dipole molecules inside the thick dielectric slowly relax back to their random resting states. This internal molecular relaxation releases trapped displacement charge back onto the conductor plates, causing **lethal voltages (up to 15% to 25% of the original charged voltage—easily 50V to 300V DC)** to spontaneously reappear across the open terminals minutes later!
- **Mandatory Safe Storage Rule**:
  - Never store discharged high-voltage capacitors with open terminals.
  - After discharging with a safety wand, permanently wrap a **heavy bare copper jumper wire or clip lead directly shorting the positive and negative terminals together**.
  - Keep this dead short in place until the capacitor is physically soldered into its final protected circuit.

---

## 10. High-Pressure Hydraulic Fluid Injection Hazards

When testing salvaged automotive ABS pump blocks ($2,000\text{ PSI}$), commercial pressure washer triplex pumps ($3,000\text{ PSI}$), or diesel common-rail fuel injection equipment ($25,000\text{ to }30,000\text{ PSI}$):

```
       [ Microscopic Pin-Hole in 2,500 PSI Hose ]
                           |
                           v
       ===========================================> Supersonic Invisible Needle Jet!
                           |
                           v
       [ Leather Glove / Hand Touches Fitting ] ===> DEEP SUBCUTANEOUS INJECTION!
```

- **The Supersonic Pinhole Needle**: At hydraulic pressures exceeding $2,000\text{ PSI}$, a microscopic pinhole defect in a braided hose, crimp ferrule, or threaded NPT fitting creates a velocity jet traveling at over **600 MPH**. The stream is virtually invisible to the naked eye.
- **Subcutaneous Injection Trauma**: If an operator runs a gloved or bare hand along a pressurized line searching for a leak, the microscopic fluid jet cuts through leather work gloves and skin like a scalpel with zero initial pain (often feeling like a mild bee sting or static snap).
- **The Medical Catastrophe**: Hydraulic oil, brake fluid, or diesel fuel is forced deeply into subcutaneous muscle fascia and tendon sheaths. Within 2 hours, acute chemical toxicity and compartment syndrome set in, leading to massive gangrenous tissue necrosis and systemic blood poisoning. Emergency surgical fasciotomy (cutting the limb open to scrape out poisoned tissue) or amputation is frequently required.
- **The Cardboard Sweep Protocol**:
  - **NEVER** touch, feel, or visually inspect pressurized hydraulic lines with your hands or face.
  - When pressurizing a hydraulic circuit for the first time, stand behind a clear polycarbonate blast shield.
  - To check for suspected micro-leaks, clamp a **long piece of corrugated cardboard or thick paperboard to a wooden dowel** and slowly pass the cardboard surface 2 inches away from all fittings. A pinhole leak will instantly blast an obvious wet puncture dot across the cardboard.
