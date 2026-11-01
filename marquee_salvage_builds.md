# 🛠️ Volume 6: Marquee Salvage Project Cookbooks (Builds 1 to 8)
*Complete, end-to-end engineering blueprints for 8 legendary electromechanical builds (Builds 1 to 8).*

---

## Blueprint 1: Low-RPM Direct-Drive Wind Generator
*Turning an LG Inverter Direct Drive washing machine motor into a silent, gearbox-free 500W [TYPICAL] renewable energy generator.*

```
Mechanical & Electrical Architecture:
[Aerodynamic 3-Blade Hub] ===(Bolted Directly)===> [LG Outer Magnet Rotor]
                                                            |
                                                 (Spins at 100-250 RPM [TYPICAL])
                                                            |
                                                            v
[Tower Mount / Stationary Pipe] <================= [LG 36-Pole Pancake Stator]
                                                            |
                                                   (3-Phase AC Output)
                                                            |
                                                            v
                                            [MDS-100A 3-Phase Diode Rectifier]
                                                            |
                                                    (Rectified DC Out)
                                                            |
                                                            v
                                            [MPPT Wind Charge Controller] ===> [24V Battery Bank]
```

### Bill of Materials:
1. Discarded LG front-load direct-drive washer (extract stator, outer rotor, and center splined shaft).
2. MDS-100A 100-Amp 3-phase bridge rectifier ($12 online).
3. 3x 48-inch aerodynamic fiberglass or PVC wind blades.
4. Heavy steel mounting plate (1/4" thick) welded to a 2" schedule 40 steel pipe mast.

### Assembly Steps:
1. **Stator Inspection**: The LG stator has 36 or 42 teeth wound with heavy copper wire, terminating in a 3-pin connector (Phases U, V, W).
2. **Mounting**: Bolt the stator rigidly to your steel mounting plate via its four central factory bolt holes. Ensure the hub bearing is packed with fresh marine grease.
3. **Blade Assembly**: Fabricate an aluminum circular adapter plate that bolts to the outer rotor drum using the factory tub-bolt pattern. Fasten your wind blades to this plate.
4. **Wiring & Rectification**:
   - Run three 10 AWG copper wires down the tower from the stator terminals into the `~` AC inputs of the MDS-100A 3-phase bridge rectifier.
   - Connect the `+` and `-` DC output studs of the rectifier to your battery charge controller.
5. **Testing**: Spin the rotor by hand. At just 120 RPM [TYPICAL], the output produces ~28V DC; in a 25 MPH wind (approx. 250 RPM [TYPICAL]), the generator pumps over **450 Watts** continuously into a 24V battery bank with near-zero acoustic noise.

---

## Blueprint 2: Direct-Drive Force Feedback (FFB) Sim Racing Wheel
*Converting an automotive Electric Power Steering (EPS) column into an ultra-realistic 25 Nm [TYPICAL] sim racing steering wheel.*

```
Wiring Schematic:
[PC Racing Sim (Assetto Corsa)] <---(USB Cable)---> [STM32 "BluePill" MCU]
                                                            |
                                                    (PWM Forward & Reverse)
                                                            |
                                                            v
[12V 50A Server PSU] ------------(High Current)----> [BTS7960 43A H-Bridge]
                                                            |
                                                    (High-Power 12V Drive)
                                                            |
                                                            v
                                                 [EPS Steering Column Motor]
                                                            |
                                                  (Integrated Worm Gear)
                                                            |
                                                            v
                                                [Full-Size Racing Wheel]
```

### Bill of Materials:
1. Automotive EPS steering column (e.g., Toyota Prius, Opel Corsa B/C, Nissan Versa).
2. STM32F103C8T6 "BluePill" microcontroller board ($4).
3. BTS7960 43A High-Power H-Bridge motor driver ($10).
4. 12V 50A switching server power supply ($20).
5. Aftermarket steering wheel + 3D printed / machined hub adapter.

### Step-by-Step Build:
1. **Firmware Installation**:
   - Download the open-source **OpenFFB** or **MMOS** firmware.
   - Flash the firmware onto the STM32 via an ST-Link V2 programmer.
   - The STM32 presents itself to Windows as a native DirectInput Force Feedback gaming device.
2. **Wiring**:
   - Connect STM32 pin `PA8` (RPWM) and `PA9` (LPWM) to the BTS7960 inputs.
   - Connect `R_EN` and `L_EN` on the BTS7960 to +5V logic to enable the driver.
   - Connect the EPS motor's two heavy power leads to `M+` and `M-` on the BTS7960.
3. **Mounting**:
   - Fabricate a heavy 1/4" steel bracket clamping the EPS housing rigidly to your simulator cockpit or desk frame. (Do not mount to flimsy particle board; the torque will crack it).
4. **Calibration**: Launch *Assetto Corsa* or *iRacing*. Configure force feedback damping, inertia, and max gain. Experience up to 25 Nm [TYPICAL] of bone-jarring tire forces, curb rumbles, and counter-steer slip.

---

## Blueprint 3: Dual-Voice-Coil Laser Vector Galvanometer (Audio Galvo)
*Repurposing two dead 3.5" hard disk drive voice coils into an audio-driven vector laser projector.*

```
Optical & Electronic Routing:
                                    [Left Audio Channel (20W)]
                                                |
                                                v
[Laser Diode] ---> [Mirror X (HDD Arm 1)] ===> [Mirror Y (HDD Arm 2)] ===> [Wall / Screen]
                             ^
                             |
                [Right Audio Channel (20W)]
```

### Bill of Materials:
1. Two matching dead 3.5" desktop SATA hard drives.
2. 20W + 20W stereo audio amplifier board (e.g., TPA3116D2 module).
3. 5mW to 50mW red or green laser pointer diode module.
4. Two 5mm x 5mm front-surface mirrors (cut from flatbed scanner mirror glass).
5. Two light rubber bands or miniature guitar spring wire (for mechanical centering).

### Step-by-Step Build:
1. **Actuator Extraction**: Disassemble both hard drives down to the bare aluminum chassis. Carefully extract the read/write pivot arm with its coil intact.
2. **Mirror Mounting**: Snip off the delicate read-head sliders. Use a single drop of cyanoacrylate (superglue) to affix a tiny front-surface mirror to the very tip of each arm.
3. **Orthogonal Frame Alignment**:
   - Mount Arm 1 horizontally (deflects laser horizontally = X-Axis).
   - Mount Arm 2 vertically at a 90° angle (deflects laser vertically = Y-Axis).
   - Aim the laser beam so it bounces off Mirror X onto Mirror Y, and out toward the wall.
4. **Mechanical Neutral Spring**: Attach a light rubber band or fine guitar wire to each arm so that when unpowered, the mirrors rest centered at neutral 45° angles.
5. **Electronic Drive**:
   - Solder speaker wire leads to the voice coils. Connect Voice Coil X to the Left speaker output of the amplifier, and Voice Coil Y to the Right speaker output.
6. **Playback**: Connect your PC headphone jack to the amplifier input. Play Lissajous audio files, oscilloscope vector music, or output vector coordinates from *LaserShowGen*. Enjoy vector graphics projected crisply at audio speed!

---

## Blueprint 4: Professional 2" x 72" Knife Grinder from a Treadmill Motor
*Building an industrial-grade knife profiling grinder powered by a salvaged 2.5 HP PMDC motor.*

```
Mechanical Drive Layout:
  [2.5 HP Treadmill Motor (90V-130V DC)]
                    |
      (5" Crowned Aluminum Drive Wheel)
                    |
                    v
   ============(2" x 72" Grinding Belt)============
   |                                              |
[Tracking Wheel (Crowned)]               [Flat Platen Work Rest]
```

### Bill of Materials:
1. Salvaged treadmill PMDC motor (1.5 HP to 3.0 HP, 90V–130V DC, 4,000+ RPM).
2. KB Electronics **KBIC-120** or **KBIC-240** DC motor speed control drive.
3. 0.025 Ω or 0.05 Ω plug-in horsepower resistor (matched to motor amperage).
4. 5" diameter crowned aluminum drive wheel with matching shaft bore.
5. Standard 2x72 grinder chassis (welded steel tubing or aluminum tooling plate).

### Step-by-Step Build:
1. **Mounting**: Fabricate a 3/8" steel motor mount plate. Bolt the treadmill motor rigidly to the rear of your grinder chassis. Press-fit the 5" drive wheel onto the motor output shaft, securing with keyway and set screws.
2. **KBIC Controller Setup**:
   - Mount the KBIC board inside a sealed, fan-cooled NEMA electrical enclosure (metal grinding dust is conductive and will instantly short out unshielded circuit boards!).
   - Insert the proper plug-in horsepower scaling resistor into the board socket.
   - Connect AC Mains Live and Neutral to terminals `L1` and `L2`.
   - Connect Motor Armature leads to `A+` and `A-`.
   - Wire a 5kΩ linear potentiometer to terminals `P1`, `P2`, and `P3` on the board apron.
3. **Tuning IR Compensation**:
   - Turn on the grinder. Slowly turn up the potentiometer until the belt runs at moderate speed.
   - Adjust the `IR COMP` trimpot on the KBIC board while pressing a scrap steel bar into the grinding platen until the motor actively compensates and maintains constant speed under heavy cutting pressure.
4. **Result**: Delivers continuous, adjustable grinding speeds from **500 to 5,500 SFPM**, allowing rapid steel hogging and delicate temper-preserving knife edge grinding.

---

## Blueprint 5: 18650 Battery Pack Spot Welder from a Rewound MOT
*Transforming a lethal microwave oven transformer into a safe, high-current precision spot welder.*

```
Electrical Circuit Diagram:
[AC Mains 120V/240V] ---> [Solid-State Relay (SSR-40DA)] ---> [MOT Primary Coil]
                                     ^                                |
                                     |                     (Iron Transformer Core)
                             (Trigger Pulse)                          |
                                     |                                v
                             [Arduino Timer]        [Rewound Secondary: 2-3 Turns 2 AWG]
                                     ^                                |
                                     |                     (Delivers 3.5V @ 700A)
                             [Foot Pedal Switch]                      |
                                                                      v
                                                         [Dual Solid Copper Welding Tips]
```

### Bill of Materials:
1. Scrap microwave oven transformer (MOT).
2. 5 feet of ultra-flexible **2 AWG or 0 AWG copper welding cable**.
3. SSR-40DA 40-Amp AC Solid-State Relay ($6).
4. Arduino Nano microcontroller + momentary foot switch pedal.
5. Solid copper welding prongs (e.g., 6 AWG solid copper wire or brass rods).

### Step-by-Step Build:
1. **De-Coring the Secondary**:
   - Clamp the MOT securely. Saw through the outer loops of the thin-wire secondary high-voltage coil with a hacksaw.
   - Knock the remaining secondary wire out of the core window using a punch. **Keep the primary mains coil 100% undamaged.**
2. **Rewinding**:
   - Feed the thick 2 AWG welding cable through the transformer core window, wrapping **two to three tight turns**.
   - Strip the cable ends and clamp into solid copper welding tip electrodes.
3. **Pulse Timing Circuit**:
   - Wire the Arduino to trigger the SSR-40DA for an exact **dual-pulse** sequence when the foot pedal is pressed:
     - *Pre-weld pulse*: 15 ms (cleans surface oxidation and seats nickel strip).
     - *Pause*: 20 ms.
     - *Main weld pulse*: 45 ms (creates instantaneous, clean metallurgical nugget weld).
4. **Operation**: Position a 0.15mm pure nickel strip over an 18650 battery cell terminal. Press the copper tips firmly against the nickel. Tap the foot pedal. The weld completes in 80 milliseconds without heating the lithium battery cell.

---

## Blueprint 6: Micro-Laser Engraver from Dual Optical DVD Drives
*Building an ultra-compact 40mm x 40mm desktop CNC laser cutter using scrap DVD drive sleds.*

```
Mechanical Cross-Axis Configuration:
  +-------------------------------------------------------------+
  | [X-Axis DVD Sled Assembly] (Base horizontal motion)         |
  |         |                                                   |
  |         v                                                   |
  | [Rigid 90° Vertical Bracket]                                |
  |         |                                                   |
  |         v                                                   |
  | [Y-Axis DVD Sled Assembly] (Vertical/Cross motion)          |
  |         |                                                   |
  |         v                                                   |
  | [250mW Red Laser Diode + Collimator Lens + Constant Current]|
  +-------------------------------------------------------------+
```

### Bill of Materials:
1. Two matching discarded DVD-RW writer drives (extract sled micro-steppers and steel guide rails).
2. Arduino Nano running **GRBL 1.1** CNC firmware.
3. CNC Shield v4 or breadboard with two **A4988** stepper driver modules.
4. 250mW 650nm red laser diode in an AixiZ 12mm brass module with glass focusing lens.
5. LM317 or dedicated constant-current laser diode driver board (set to 250mA).

### Step-by-Step Build:
1. **Frame Construction**: Fasten the X-axis DVD metal chassis flat to a small wooden board. Fasten the Y-axis chassis vertically at a right angle above it using a 3D printed or aluminum corner bracket.
2. **Driver Calibration**: Set the $V_{ref}$ trimpot on both A4988 drivers to **0.35V** to prevent overheating the miniature stepper coils.
3. **GRBL Configuration**: Connect over USB via LaserGRBL software. Set:
   ```
   $100=6400 (X steps/mm: 200 steps * 16 microsteps / 0.5mm lead)
   $101=6400 (Y steps/mm)
   $110=500  (Max rate mm/min)
   $120=50   (Acceleration mm/sec^2)
   ```
4. **Operation**: Focus the laser beam down to a microscopic pinpoint dot on your workpiece. Load vector SVG files to burn intricate artwork, wood business cards, and leather keytags.

---

## Blueprint 7: Ultra-Silent Indoor Airbrush & Resin Degassing Station
*Repurposing a discarded refrigerator compressor into a dual-purpose <40 dB silent air supply and 28+ inHg vacuum chamber.*

```
Pneumatic Plumbing Diagram:
  [Heavy Stainless Stockpot + 1" Lexan Lid] <---(Suction Stub)--- [Fridge Compressor]
  *(Vacuum Degassing: Pulls 28.5 inHg)*                                   |
                                                                   (Exhaust Stub)
                                                                          |
                                                                          v
[Clean 30 PSI to Airbrush] <--- [Oil Filter] <--- [Air Tank] <--- [One-Way Check Valve]
```

### Bill of Materials:
1. Hermetic compressor from a decommissioned refrigerator or dehumidifier.
2. Discarded fire extinguisher or small steel expansion tank (pressure rated).
3. 1/4" NPT air compressor pressure switch (30 PSI cut-in / 45 PSI cut-out).
4. ASME-certified 100 PSI brass safety pop-off relief valve.
5. High-efficiency oil-coalescing pneumatic filter.
6. Stainless steel 6-quart stockpot + 1-inch thick clear polycarbonate circular lid + silicone gasket.

### Step-by-Step Build:
1. **Compressor Extraction**: Cut the copper lines cleanly with a tubing cutter. Identify the three stubs:
   - *Suction stub*: Pulls vacuum.
   - *Discharge stub*: Pumps high pressure.
   - *Process stub*: Capped/crimped (used for factory refrigerant charging).
2. **Pressure Line Assembly**: Plumb the discharge stub through a brass one-way check valve into the fire extinguisher receiver tank. Install the pressure switch and safety pop-off valve into the tank manifold. Route output through the oil-coalescing filter to remove oil vapors before reaching your airbrush.
3. **Vacuum Line Assembly**: Connect heavy-duty vacuum-rated reinforced hose from the suction stub to your stainless steel degassing pot. Install a brass ball valve and vacuum gauge (0 to 30 inHg) on the lid.
4. **Dual Capability**: Flip the power switch. The system purrs at 38 dB. Open the vacuum valve to boil bubbles out of casting resin, or grab your airbrush to lay down silky smooth paint without waking anyone up in the next room.

---

## Blueprint 8: Autonomous Heavy Robot Rover (AGV) from Hoverboard Hubs
*Building an all-terrain, 100 lb payload robot platform using reprogrammed hoverboard motors.*

```
Hardware Control Hierarchy:
[Raspberry Pi 4 (ROS / Navigation)]
               |
         (UART Serial: 115200 Baud)
               |
               v
[Hoverboard Mainboard (STM32 Hacked Firmware)]
          |                                  |
    (Left 3-Phase Phase Inverter)      (Right 3-Phase Phase Inverter)
          |                                  |
          v                                  v
[Left 350W Hub Motor]              [Right 350W Hub Motor]
```

### Bill of Materials:
1. Complete scrap hoverboard (wheels, mainboard, wiring harness, and 36V battery pack).
2. ST-Link V2 USB programmer ($4).
3. Two rear heavy-duty swivel caster wheels.
4. Aluminum extrusion (2020 or 2040) or 3/4" marine plywood chassis base.
5. Microcontroller (Arduino, ESP32, or Raspberry Pi).

### Step-by-Step Build:
1. **Mechanical Mounting**: Mount the two hoverboard wheel axles rigidly into custom slotted aluminum brackets at the front of your robot chassis. Install the two swivel casters at the rear.
2. **Flashing Firmware**:
   - Solder a 4-pin header to the programming pads of the mainboard.
   - Connect the ST-Link V2 to your PC and flash the open-source `hoverboard-firmware-hack` configured for **USART serial mode at 115200 baud**.
3. **Serial Control Protocol**:
   - Send binary data packets from your microcontroller over UART to set left and right motor speeds:
   ```c
   typedef struct {
     int16_t steer;
     int16_t speed;
   } SerialCommand;
   ```
4. **Deployment**: Mount sensors, laptops, or cameras to the chassis. The rover handles grass, gravel, steep inclines, and 100 lb loads effortlessly with whisper-quiet, high-torque direct-drive agility.
