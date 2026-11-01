# 🖨️ Volume 1.1: Printers, Scanners & Copiers Salvage Guide
*Harvesting precision linear motion, optical scales, fusers, and high-torque hybrid steppers from office e-waste.*

---

## 1. Anatomy of Office E-Waste: What to Harvest

```
+-----------------------------------------------------------------------------------------------+
| Component             | Donor Device            | Primary Mechanical / Electrical Spec        |
| --------------------- | ----------------------- | ------------------------------------------- |
| Linear Ground Rods    | Inkjets, Lasers, Scanners| 6mm, 8mm, 10mm, 12mm hardened steel, h6 tol|
| Hybrid Stepper Motors | Laser Printers, Copiers | NEMA 17 & NEMA 23, 1.8° step, 4-wire bipolar|
| Linear Optical Strip  | Inkjet Printers         | 150–300 LPI transparent polyester strip + IC|
| Rotary Optical Disc   | Paper Feed Rollers      | High-PPR transparent disc + quadrature IC   |
| Fuser Assembly        | Laser Printers          | Halogen heat lamp (180°C–210°C) + silicone roll|
| Polygon Mirror Unit   | Laser Scanner Assemblies| 10,000–30,000 RPM [TYPICAL] BLDC with faceted mirror   |
| High-Voltage PSU      | Laser Printers          | 1,000V–6,000V DC (microamp corona charging) |
| Front-Surface Mirrors | Flatbed Scanners        | 98%+ optical reflectivity, zero ghosting    |
| Solenoids & Clutches  | Paper Feed Trays        | 12V / 24V DC [TYPICAL] electromagnetic clutches/stops |
+-----------------------------------------------------------------------------------------------+
```

---

## 2. In-Depth Subsystem Teardowns & Engineering Exploits

### A. The Linear Optical Encoder Strip: Free Machine Tool DRO
Modern inkjet printers do not use expensive stepper motors for their print carriages; they use cheap DC motors combined with an **optical linear encoder strip** to achieve sub-millimeter closed-loop positioning.

```
Encoder Read-Head Architecture:
  +----------------------------------------------------+
  | [IR LED Emitter]                                   |
  |         |                                          |
  |         v                                          |
  | =======[Transparent Strip with 150-300 LPI Grid]== |
  |         |                                          |
  |         v                                          |
  | [Dual Photodiode Receiver (Phase A & Phase B)]     |
  +----------------------------------------------------+
```

#### Pinout Identification:
The miniature reader PCB clipped to the print head typically has 4 to 6 solder pads:
- `VCC`: +3.3V or +5V DC
- `GND`: Ground
- `Channel A`: Digital square wave pulse
- `Channel B`: Digital square wave pulse (shifted 90° in phase for direction detection)

#### The Lathe / Milling Machine Digital Readout (DRO) Hack:
1. Unclip the clear encoder strip and unscrew the optical reader PCB from the carriage.
2. Fasten the optical reader to your lathe's cross-slide carriage and stretch the encoder strip along the lathe bed inside a protective 3D-printed or aluminum channel to shield it from metal shavings.
3. Wire Channel A and Channel B to Arduino/ESP32 pins `D2` and `D3` (Hardware Interrupts).
4. Run the firmware below: Each transition corresponds to **1/300th or 1/600th of an inch (approx. 40 to 80 microns)**, providing instant sub-millimeter digital measurement on an OLED screen.

```cpp
// Arduino Dual-Interrupt Quadrature Decoder for Printer Strips
const byte pinA = 2;
const byte pinB = 3;
volatile long encoderTicks = 0;

void setup() {
  Serial.begin(115200);
  pinMode(pinA, INPUT_PULLUP);
  pinMode(pinB, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(pinA), handleA, CHANGE);
  attachInterrupt(digitalPinToInterrupt(pinB), handleB, CHANGE);
}

void handleA() {
  if (digitalRead(pinA) == digitalRead(pinB)) {
    encoderTicks++;
  } else {
    encoderTicks--;
  }
}

void handleB() {
  if (digitalRead(pinA) != digitalRead(pinB)) {
    encoderTicks++;
  } else {
    encoderTicks--;
  }
}

void loop() {
  static long lastTicks = 0;
  if (encoderTicks != lastTicks) {
    lastTicks = encoderTicks;
    float positionMM = (encoderTicks / 600.0) * 25.4; // Assuming 600 quadrature counts/inch
    Serial.print("Position: ");
    Serial.print(positionMM, 3);
    Serial.println(" mm");
  }
}
```

---

### B. Laser Printer Fuser Assembly: Flawless PCB Toner Transfer & Foil Laminator
Inside every laser printer is a **fuser unit** designed to melt plastic toner powder into paper fibers under intense heat and spring-loaded pressure.

```
Fuser Mechanical Cross-Section:
  [ Quartz Halogen Tube Lamp (~1,000 Watts) ]
                      |
                      v
      ====(Teflon-Coated Aluminum Tube)====  <--- Reaches 180°C - 205°C
                      |
               [ Workpiece ]  <--- (PCB Copper Board + Glossy Toner Paper)
                      |
      ====(Silicone Rubber Pressure Roller)====
                      ^
                      |
            [ Heavy Steel Springs ]
```

#### The Hack:
- In DIY PCB etching, ironing toner onto copper boards with a clothes iron is unreliable and uneven.
- By extracting the fuser assembly and wiring the internal halogen lamp through an AC solid-state relay (SSR) controlled by a K-type thermocouple or PID temperature controller, you create a motorized PCB toner applicator.
- Feed your copper clad board with printed laser glossy paper through the heated rollers at 185°C. In one 10-second pass, the fuser transfers 100% of toner onto the copper with zero trace smearing down to 6-mil traces.

---

### C. Laser Printer High-Voltage Power Supply (HVPS): Electrostatic Flocking & Powder Coating
Laser printers contain a specialized high-voltage power board that supplies:
- **Corona Wire / Charge Roller**: -5,000V to -6,000V DC at under 500 µA.
- **Developer Bias**: -300V to -600V DC.
- **Transfer Roller**: +1,000V to +3,000V DC.

#### Repurposing Exploits:
- **DIY Electrostatic Grass / Flocking Applicator**: Connect the negative 5kV output to a fine wire mesh sieve and positive ground to the workpiece coated with glue. Flocking fibers or synthetic grass become electrostatically charged and shoot downward at high speed, embedding vertically for hyper-realistic diorama scenery or velvet-lined luxury boxes.
- **Desktop DIY Powder Coating Gun**: Charge powder coat paint particles negatively as they spray past an electrode, causing them to wrap around grounded metal parts electrostatically for zero overspray.

---

### D. Flatbed Scanner Guides & Front-Surface Mirrors
- **Front-Surface Mirrors**: Ordinary household mirrors have their reflective silver coating on the *back* of glass, causing double-refraction "ghosting." Scanner mirrors are front-surface silvered (reflective coating on the top surface).
  - *Projects*: Laser light show galvo mirrors, 3D printer SLA beam deflecting optics, high-magnification microscope splitters.
- **Ground Steel Guide Rods**: Laser printers and copiers yield hardened 8mm, 10mm, and 12mm ground steel guide shafts that fit standard **LM8UU** or **LM10UU** linear ball bearings perfectly for building budget 3D printers, laser engravers, or CNC plotters.

---

## 3. Hacking Broken Digital Calipers into Industrial DRO Machine Scales

While optical linear encoder strips from printers (Section 2.A) provide high resolution, they have a fatal flaw in machine shop environments: cutting oil splash, kerosene mist, and conductive cast-iron swarf instantly blind the tiny transmissive optical slits, causing CNC axes to lose steps.

```
       [ Stainless Steel Caliper Beam with Capacitive PCB Grid ]
       =========================================================
          [ Slider Readhead: 4-Pad Serial Data Port Under Rubber Plug ]
                (PAD 1: GND | PAD 2: DATA | PAD 3: CLK | PAD 4: +1.5V)
                                   |
                                   v
             [ Dual NPN Transistor 1.5V -> 3.3V Level Shifter ]
                                   |
                                   v
             [ ESP32 Microcontroller: 0.01mm Resolution Machine DRO! ]
```

### A. Why Capacitive Caliper Encoders Outclass Optical Strips:
- **Environmentally Sealed**: The capacitive stator grid is etched into a copper PCB layer protected under a thick, oil-resistant mylar decal on the stainless steel spine. Coolant spray, machine oil, and abrasive dust do not impede capacitive field coupling.
- **Microscopic Accuracy**: Resolves **$0.01\text{ mm}$ ($0.0005\text{ inches}$)** natively with zero cumulative gear backlash.
- **Cheap & Ubiquitous**: Calipers with broken carbide jaws, cracked glass LCDs, or dead batteries are thrown away in machine shops daily.

### B. Tapping the 24-Bit Synchronous Serial Bus:
Pry open the small rubber plug on top of the caliper slider body. You will reveal four circular gold test pads:
- **Pad 1 (GND)**: System battery ground.
- **Pad 2 (DATA)**: Serial data output (1.5V logic level).
- **Pad 3 (CLK)**: Serial clock line (pulses high at ~77 kHz during transmission bursts).
- **Pad 4 (VCC)**: +1.5V button cell power supply.

```cpp
// ESP32 Caliper Data Reader (24-bit Synchronous Bit-Bang)
const int CLK_PIN = 18;
const int DATA_PIN = 19;

long readCaliper() {
  while (digitalRead(CLK_PIN) == LOW); // Wait for clock burst
  while (digitalRead(CLK_PIN) == HIGH);
  
  long value = 0;
  for (int i = 0; i < 24; i++) {
    while (digitalRead(CLK_PIN) == LOW);
    if (digitalRead(DATA_PIN) == HIGH) {
      value |= (1L << i);
    }
    while (digitalRead(CLK_PIN) == HIGH);
  }
  // Value is in hundredths of a millimeter (0.01mm)
  return value; 
}
```

### C. Repurposing Exploits:
1. **Multi-Axis Mini-Lathe & Mill DRO**: Bolt caliper beams to the cross-slide and carriage of a mini-lathe. An ESP32 reads both calipers, drives an OLED display, and transmits wireless telemetry over Bluetooth/Wi-Fi to a tablet running a full digital readout interface with tool offsets.
2. **Closed-Loop Linear Actuator Conversion**: Fix a caliper beam alongside a cheap 12V automotive power seat actuator or power window motor to transform crude open-loop DC motors into precision CNC positioning stages with closed-loop micron positioning!

---

## 4. Vending Machine Bill Acceptors: Multi-Spectral Sensors & Pinch Drives

Discarded commercial vending machine bill validators (MEI Mars, CashCode, Coinco) tossed due to outdated currency firmware contain specialized precision electromechanics:

```
        +-------------------------------------------------------------+
        | Bill Validator Hardware Extraction:                         |
        |                                                             |
        | [ High-Torque 12V/24V Worm-Drive Dual Urethane Pinch Rollers]|
        | [ Multi-Wavelength Optical Array (IR, UV, 520nm Green, 660nm)]
        | [ High-Speed Optical Transmission / Reflection Transceivers ]|
        +-------------------------------------------------------------+
```

### A. Non-Slip Urethane Pinch Rollers:
- Powered by high-reduction 12V DC [TYPICAL] worm gearmotors, the rollers use high-friction, non-marking cast urethane rubber.
- **Exploits**:
  - The ultimate slip-free filament feeder for flexible 3D printing filaments (TPU, TPE) that strip inside standard brass extruder gears.
  - Automatic precision strip feeder for sheet metal stamping and thin brass foil stamping dies.

### B. Multi-Spectral Material Sorting Spectrometers:
- Bill validators detect counterfeit banknotes by measuring light transmission and reflectance across **Infrared ($880\text{ nm}$)**, **Ultraviolet ($365\text{ nm}$)**, and visible wavelengths simultaneously.
- **Exploits**: Automated optical recycling sorting gates—differentiating between clear PET plastic, PVC, and polycarbonate fragments on a vibrating conveyor before mechanical recycling.
