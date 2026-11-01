# 💿 Volume 1.2: Optical Disc Drives & Hard Disk Drives
*Hacking micro-steppers, nanometer voice-coil actuators, FDB spindle motors, and N52 neodymium magnets.*

---

## 1. The Optical Disc Drive (CD / DVD / Blu-Ray) Goldmine

```
Inside an Optical Disc Drive:
+-------------------------------------------------------------+
| [Spindle BLDC] ---> Spins disc at 3,000 - 10,000 RPM [TYPICAL]        |
|                                                             |
| [Micro-Stepper] ===(M3x0.5mm Leadscrew)===> [Laser Sled]    |
|                                                    |        |
|                                   [2-Axis Voice Coil Lens]  |
|                                   [Laser Diode (650nm/405nm)|
|                                   [Front-Surface Mirrors]   |
| [Eject Mechanism] ---> Small 5V Brushed DC + Belt Reduction |
+-------------------------------------------------------------+
```

### Harvestable Components Breakdown:
1. **Sled Linear Actuator**: A 4-wire bipolar micro-stepper motor permanently coupled to a miniature hardened steel leadscrew (typically 3mm diameter with a 0.5mm thread pitch). Stroke length: ~38mm to 42mm.
2. **2-Axis Lens Voice Coil Actuator**: Suspended on four hair-thin beryllium-copper suspension wires, two sets of miniature electromagnetic coils sit immersed in high-flux permanent magnetic fields. One coil shifts the objective lens vertically (focus); the second tilts or shifts it laterally (tracking) with nanometer-scale resolution.
3. **Laser Diodes**:
   - *CD-ROM/CD-RW*: 780 nm (Infrared—Invisible and very dangerous to eyes; avoid).
   - *DVD-RW (Writer)*: 650 nm (Red, 200 mW to 300 mW)—capable of burning black electrical tape, cutting thin craft foam, and exposing UV/photoresist.
   - *Blu-Ray (BD-RE)*: 405 nm (Violet/Near-UV, 50 mW to 200 mW)—causes minerals and fluorescent dyes to glow brightly; cures UV resin instantaneously.
4. **Spindle BLDC Motor**: 3-phase slotless pancake brushless motor with a magnetic center-clamping ring.

---

### Creative Engineering Projects:

#### A. Micro-Laser Engraver / 2D Pen Plotter
By salvaging two identical DVD-RW drive mechanisms:
- Mount one sled assembly horizontally on a wooden baseplate (X-Axis).
- Mount the second sled assembly vertically at a 90° angle (Y-Axis).
- This produces a rigid, ultra-precise **38 mm x 38 mm motion platform**.
- Pair with an Arduino running **GRBL firmware** and two A4988 stepper drivers set to 1/16th microstepping:
  $$\text{Steps per mm} = \frac{200 \text{ steps/rev} \times 16 \text{ microsteps}}{0.5 \text{ mm/rev}} = 6,400 \text{ steps per mm!}$$ [CALCULATED]
- Mount the salvaged 250mW red DVD-writer laser diode with an AixiZ glass collimating lens to engrave detailed logos on leather, wood, and plastic cards.

#### B. Sub-Micron Atomic Force Microscope (AFM) Scanner
- The optical pick-up lens voice coil has a movement bandwidth from DC to over 10 kHz with zero mechanical backlash.
- By connecting the focus coil to the analog output of a 16-bit digital-to-analog converter (DAC) through an operational amplifier buffer, you can step the stage vertically in **sub-nanometer increments**.
- Hobbyist physicists utilize this exact voice coil mechanism to build low-cost Scanning Tunneling Microscopes (STM) capable of imaging individual atomic crystal lattices of graphite.

---

## 2. Mechanical Hard Disk Drives (HDDs)

```
HDD Rotary Voice Coil Actuator:
               Pivot Bearing
                   (O)
                  /   \
  [Read/Write Arm]     [Flat Triangular Copper Coil]
       (Front)                     (Rear)
                                     |
                          [N52 Sintered Neodymium]
                          [Top & Bottom Curved Plates]
```

### Harvestable Components Breakdown:
1. **Rotary Voice Coil Actuator**: A zero-backlash, counter-balanced aluminum arm pivoted on microscopic, aerospace-grade shielded ball bearings. The rear coil sits nestled inside an intense magnetic gap created by two gold-plated or nickel-plated sintered N52 neodymium arc magnets.
2. **Fluid Dynamic Bearing (FDB) Spindle Motor**: 3-phase brushless motor with hydrodynamic fluid bearings. Virtually zero acoustic noise and zero shaft play.
3. **Mirror Platters**: Polished aluminum or glass-ceramic substrates coated with magnetic thin films, finished to optical mirror smoothness.

---

### Creative Engineering Projects:

#### A. Dual-Voice-Coil Laser Vector Galvanometer (Audio-Driven Galvo)
Professional laser show galvos cost hundreds of dollars. You can build an audio-driven vector laser projector using two salvaged hard drive voice coil arms:

```
Laser Galvo Optical Path:
[Laser Pointer] ---> [Mirror X (HDD Arm 1)] ===> [Mirror Y (HDD Arm 2)] ===> [Wall / Screen]
                             ^                           ^
                             |                           |
                     [Left Audio Channel]        [Right Audio Channel]
```

1. Extract the voice coil arms from two matching 3.5" hard drives.
2. Cut off the delicate read head sliders. Glue a 5mm x 5mm front-surface mirror (salvaged from a flatbed scanner or DVD drive) directly onto each arm tip using a drop of cyanoacrylate (superglue).
3. Mount the two assemblies at right angles so the reflected laser beam hits the center of Mirror 2.
4. Add a light rubber band or tiny spring to provide a gentle mechanical center-return force.
5. Connect Coil X to the **Left Channel** and Coil Y to the **Right Channel** of a standard 20W stereo audio amplifier.
6. Play an audio file containing **Lissajous signals or stereo vector audio** (e.g., using open-source *LaserShowGen* or *Oscilloscope Music*).
7. The laser draws animated geometric figures, clocks, and text in real time on your wall at up to 3,000 points per second.

#### B. Ultra-Sensitive Geophone / Seismometer
- A voice coil is completely symmetrical: applying electrical current creates physical movement, but **physical movement generates electrical voltage**.
- Secure an HDD voice coil assembly to a heavy steel baseplate resting on your workshop floor or bedrock foundation.
- Add a 10-gram lead fishing weight to the head arm to act as an inertial proof mass.
- Connect the coil leads to an ultra-low-noise instrumentation amplifier (such as the **INA128** or **AD620**) with a gain of 1,000x, followed by a 10 Hz low-pass filter.
- The sensor easily registers footsteps down the hallway, heavy freight trains passing several miles away, and distant regional tectonic earthquake tremors.

#### C. The HDD Leather Stropping Wheel for Razor-Sharp Tools
- Remove the top lid, read arm, and magnet assembly, leaving the platter and spindle motor intact on the chassis.
- Cut a circular disk of vegetable-tanned tooling leather and adhere it to the top surface of the aluminum platter with contact cement.
- Charge the leather with green chromium oxide polishing compound.
- Drive the spindle motor using an inexpensive sensorless ESC or an Arduino running SimpleFOC at 3,000 RPM [TYPICAL].
- Touch wood chisels, carving gouges, and pocketknives to the leather wheel for 5 seconds to achieve a mirror-polished, surgical razor edge.

---

## 3. High-Power Voice Coils: Blown Subwoofers & PA Speakers

While miniature voice coils from CD/DVD pickups and hard drives provide microscopic precision, blown or discarded car audio subwoofers and commercial PA speakers (12", 15", and 18" drivers from JBL, Eminence, Rockford Fosgate) contain massive high-power linear electromagnetic motors:

```
        +-----------------------------------------------------------+
        | High-Excursion Speaker Motor Topology:                   |
        |                                                           |
        |    [ Massive 5-10 lb Strontium-Ferrite Ring Magnet ]      |
        |                           |                               |
        |                           v                               |
        |    (Narrow 1.5mm Annular Magnetic Air Gap: 1.2+ Tesla)    |
        |                           |                               |
        |                           v                               |
        |    [ 2" to 4" Kapton / Copper Ribbon Voice Coil Former ]  |
        |        (Travels ±15mm to ±30mm Linear Stroke!)            |
        +-----------------------------------------------------------+
```

### A. The Linear Electrodynamic Shaker Table
- **Construction**: Cut away the torn paper cone and outer foam surround. Bolt a rigid aluminum plate directly onto the center voice coil former dust cap, supported by a circular flexible spring-steel or carbon-fiber spider.
- **Drive Electronics**: Feed the coil from a salvaged 200W–500W mono audio amplifier driven by a frequency generator app on a smartphone.
- **Repurposing Exploits**:
  1. **Avionics & Drone Vibration Shaker**: Sweep sine waves from $10\text{ Hz to }2,000\text{ Hz}$ to find destructive mechanical resonance frequencies in custom 3D-printed drone arms, PCB solder joints, and battery brackets before flight.
  2. **Concrete & Epoxy Degassing Table**: Run at $50\text{ Hz to }60\text{ Hz}$ under a mold platform to blast trapped microscopic air bubbles out of casting resin, ultra-high-performance concrete (UHPC), and investment plaster molds within 30 seconds.

### B. Resonant Free-Piston Stirling Linear Alternator
- Coupling the speaker voice coil through a lightweight titanium connecting rod to a free-piston Stirling engine cylinder converts acoustic pressure oscillations directly into clean AC electricity with zero crankshafts, zero flywheel bearings, and zero oil lubrication.

---

## 4. Camera Optics Scrap: Ultrasonic Traveling-Wave Ring Motors (USM)

Defective autofocus camera lenses (Canon EF USM, Nikon AF-S SWM, Sigma HSM) tossed due to dropped optical elements or scratched front glass contain one of the most exotic electromechanical motors ever invented:

```
                  [ Hollow Center Light Path (Ø 35mm - 65mm) ]
                                       |
    [ Toothed Bronze Rotor ] <======== + ========> [ Toothed Bronze Rotor ]
      -----------------                               -----------------
    [ Piezo Traveling-Wave Stator ]                 [ Piezo Traveling-Wave Stator ]
```

### A. The Traveling-Wave Piezoelectric Principle
Unlike magnetic motors, an Ultrasonic Motor (USM) contains zero copper windings and zero magnets:
- A ring of segmented piezoelectric ceramics is bonded to an elastic bronze stator ring.
- Driven by two-phase ultrasonic AC signals ($30\text{ kHz to }45\text{ kHz}$ with a $90^\circ$ phase offset), the stator teeth undergo microscopic elliptical orbiting motion, creating a continuous mechanical **traveling surface wave** that drags the friction-coupled rotor ring around.

### B. Unique Exploits of USM Motors:
1. **Large Clear Central Aperture**: The motor is a hollow cylinder ($35\text{ mm to }65\text{ mm}$ clear center hole). Optical beams, fiber optic cables, or laser lines pass directly through the motor axis!
2. **Zero Magnetic Field**: Emits zero electromagnetic interference (EMI) and contains no ferromagnetic cores, making it 100% immune to high magnetic fields—the only motor capable of operating inside MRI scanners, electron beam microscopes, and high-energy physics chambers.
3. **Instantaneous Response & Unpowered Holding Brake**: Rotor inertia is microscopic. When power is removed, spring preload clamps the rotor against the stator, providing massive, rock-solid **unpowered holding torque with zero backlash**.
4. **Repurposing Target**: Precision motorized laser polarizer / waveplate rotators, hollow-shaft robotic microscope turret indexers, and motorized iris aperture controllers.

---

## 5. Audiophile Turntables: Coreless Direct-Drives & Ruby Gimbal Bearings

High-end direct-drive phonograph turntables (Technics SL-1200 series, Denon, Pioneer) yield components engineered for zero rotational noise and sub-milligram frictional drag:

```
        +-----------------------------------------------------------+
        | Slotless Coreless Direct-Drive Topology:                  |
        |                                                           |
        | [ Large-Diameter Multi-Pole NdFeB Rotor Ring ]            |
        |                            |                              |
        |                            v                              |
        | [ Flat Printed Stator Coils with ZERO IRON TEETH ]        |
        | (Pure Air-Core Winding = ZERO COGGING TORQUE FOREVER!)    |
        +-----------------------------------------------------------+
```

### A. The Zero-Cogging Slotless Motor:
- Standard brushless motors have copper wire wound around stamped iron teeth. As magnets pass each tooth, magnetic attraction causes **cogging torque** (the bumpy detent feeling when turning by hand).
- Audiophile direct-drive turntable motors eliminate iron cores completely. Coils are flat copper traces printed directly onto circuit boards or cast in resin.
- **The Result**: Butter-smooth, continuous electromagnetic torque with **zero torque ripple and zero acoustic noise**.
- **Exploits**: The ultimate direct-drive Right Ascension (RA) motor for astronomical telescopes—delivering sub-arcsecond tracking accuracy with zero periodic gear errors.

### B. Tonearm Ruby/Sapphire Pivot Gimbals:
- Precision turntable tonearms rotate on hardened needle points seated in polished **synthetic sapphire or ruby jewel cup bearings**.
- Frictional drag is under **5 milligrams**, offering the lowest mechanical friction of any physical bearing on Earth.
- **Exploits**:
  - The core pivot for a home **Cavendish Gravity Torsion Balance** (measuring the gravitational attraction between lead spheres).
  - Micro-Newton thrust measurement stands for experimental electrospray and ion propulsion thrusters.

---

## 6. Vintage 35mm SLR Cameras: Mechanical Escapements & Focal-Plane Shutters

Broken manual 35mm film cameras (Nikon FM/FE, Canon FTb, Pentax Spotmatic) contain Swiss-watch-grade micro-horology:

```
 [ Coiled Spring Cocked ] ---> [ Miniature Escapement Balance Wheel ] ---> [ Snap Trigger ]
                                (Regulates 1 to 10 Second Delay)
```

- **Mechanical Self-Timer Escapement**: A tiny jewel-bearing gear train and oscillating balance wheel that delays release for an exact mechanically governed 10 seconds without batteries or microchips.
  - *Exploit*: Safe, battery-free mechanical time-delay releases for high-altitude weather balloon payloads and sub-sea acoustic pingers.
- **Focal-Plane Slit Shutters**: Precision titanium foil or carbon-fiber curtains that accelerate across a 36mm aperture in **less than 1.0 millisecond ($1/1,000\text{ sec}$)**.
  - *Exploit*: High-speed non-electronic optical laser pulse choppers and shadowgraph ballistics photography triggers.
