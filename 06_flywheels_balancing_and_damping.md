# ⚙️ Volume 10.6: Flywheels, Dynamic Balancing & Mechanical Damping
*Rotational inertia physics, knife-edge static balancing rigs, two-plane dynamic math, and viscous fluid damping.*

---

## 1. Flywheels: The Kinetic Energy Reservoir

```
Flywheel Geometry & Mass Distribution:
  Solid Disc Flywheel:               Rim-Weighted Flywheel:
  [Uniform Density Material]        [Thin Spokes + Heavy Concentrated Rim Ring]
  I = 0.5 * m * r^2                 I ≈ m * r^2  <--- (2x MORE INERTIA for same mass!)
```

### The Physics of Rotational Energy:
$$E_k = \frac{1}{2} I \omega^2$$ [CALCULATED]
*(Where $I = \text{Moment of Inertia in kg}\cdot\text{m}^2, \omega = \text{Rotational Velocity in radians/sec}$).*

### Why Flywheels Save Machine Spindles:
When cutting steel on a lathe, milling an interrupted keyway, or chipping wood in a chipper, the cutting tool hits the workpiece intermittently.
- Without a flywheel, the electric motor's armature bogs down, creating sudden current spikes that trip circuit breakers, induce chatter marks on finished surfaces, and snap carbide tool inserts.
- **The Flywheel Effect**: The rotating flywheel stores kinetic energy proportional to the square of its speed ($\omega^2$). When the tool strikes the steel, the flywheel supplies instantaneous kinetic torque from its stored momentum, absorbing the shock without slowing the motor armature.

---

## 2. Static & Dynamic Balancing of Salvaged Rotors

An unbalanced rotor spinning at 3,600 RPM [TYPICAL] creates devastating centrifugal forces:
$$F_{\text{centrifugal}} = m_{\text{unbalance}} \cdot r \cdot \omega^2$$ [CALCULATED]
*(Even a tiny 5-gram unbalance on a 4-inch pulley at 3,600 RPM [TYPICAL] creates **over 14 pounds of hammering centrifugal force** 60 times a second, rapidly destroying ball bearings and shaking benches apart).*

---

### A. The Knife-Edge Static Balancing Rig (Zero Cost)

```
Static Knife-Edge Balancing Setup:
  [Hardened Steel Ground Parallel 1]             [Hardened Steel Ground Parallel 2]
  =================================             =================================
                 \                                     /
                  \                                   /
                   ---(Precision Ground Center Mandrel)---
                                    |
                          [Flywheel Under Test]
                                    |
                                    v
                    (Heavy Spot Rotates to the Bottom!)
```

1. **Setup**: Level two hardened ground steel parallels (or precision box levels) on your bench using a machinist's spirit level.
2. **Mounting**: Press a precision-ground steel arbor rod through the central bore of your flywheel or pulley.
3. **Execution**: Place the arbor across the knife-edges. Give the flywheel a microscopic spin.
   - Because the knife-edge contact has virtually zero friction, **the heaviest radial point of the wheel will always swing downward and settle at 6 o'clock**.
4. **Correction**:
   - Mark the heavy spot at 6 o'clock with a marker.
   - **Method A (Drilling)**: Drill shallow divots into the heavy spot rim to remove excess metal.
   - **Method B (Adding Mass)**: Tap a hole at 12 o'clock and insert a set-screw with lead washers until the wheel rests completely motionless at any angle without rolling.

---

## 3. Mechanical Damping & Vibration Isolation

```
Types of Salvaged Damping Elements:
  A. Viscous Rotary Silicone Dampers:   B. Washing Machine Hydraulic Struts:
     [ Sealed Fluid Shear Cavity ]         [ Piston with Internal Metering Orifice ]
     - Sourced from car gloveboxes         - Sourced from front-load washer tubs
     - Smooth, silent velocity damping     - Dampens heavy low-frequency oscillations
```

### Sourcing & Exploits:
1. **Automotive Glovebox Rotary Dampers**:
   - Miniature nylon gearboxes filled with high-viscosity (100,000 cSt) silicone fluid.
   - *Repurposing*: Smooth, slow-gravity drop mechanisms for trapdoors, motorized projector screens, and soft-closing cabinet doors.
2. **Front-Load Washing Machine Suspension Struts**:
   - Every front-load washer contains two to four heavy friction/hydraulic dampening struts supporting the wash tub.
   - *Repurposing*: Seismic isolation feet for heavy workshop metal lathes, compressor vibration dampeners, and shock-absorbing camera crane stabilizers.


---

## 4. The LeBlanc Automatic Ball-Balancer & Supercritical Rotordynamics

### A. The Magic of Supercritical Self-Balancing
Dynamic balancing typically requires stationary balancing machines and fixed counterweights. But what happens if the payload imbalance changes dynamically during operation (such as wet, clumping laundry in a washing machine, or unevenly wearing grinding wheels)? 

The **LeBlanc Automatic Ball Balancer (ABB)** provides **automatic, continuous, real-time dynamic balancing** with zero electronics or sensors:

```
              Rotordynamic Phase Inversion
              
      Subcritical (ω < ω_n):              Supercritical (ω > ω_n):
      Balls cluster near Heavy Spot!      Balls migrate 180° opposite Heavy Spot!
           [Heavy Spot]                        [Heavy Spot]
               (●)                                 (●)
             /     \                             /     \
            |       |                           |       |
             \     /                             \  ●● /  <-- Balls Cancel Imbalance!
```

### B. The Physics of the $180^\circ$ Phase Shift
1. **Subcritical Regime ($\omega < \omega_n$)**:
   - At low speeds below the system's mechanical resonance frequency $\omega_n$, the rotor rotates about its geometric center. 
   - The deflection is in phase with the unbalance mass. Free-rolling steel balls in an annular ring are flung toward the unbalance point, temporarily increasing vibration.
2. **Supercritical Inversion ($\omega > \sqrt{2}\ \omega_n$)**:
   - Once the shaft accelerates through resonance, the rotor's center of rotation abruptly shifts from its geometric center to its **true center of mass**.
   - This creates a **$180^\circ$ phase inversion** between the physical unbalance and the rotor's geometric orbit displacement.
   - The centrifugal force field inside the annular race now forces the loose steel balls to roll smoothly through the dampening oil to the exact position **diametrically opposite ($180^\circ$) the heavy spot**.
   - The dynamic unbalance drops to virtually zero, and the system runs glass-smooth!

### C. Salvage & Workshop Implementation:
- **Salvage Sources**: Liquid and ball balance rings attached to the upper perimeter of front-load washing machine wash drums, or high-end industrial angle grinder safety hubs.
- **Shop Fabrication**: Machine an annular circular groove into the hub of a custom 2x72 belt grinder drive wheel or high-speed arbor. Fill the groove with 6 to 10 hardened chrome steel ball bearings and light 10W machine oil (to dampen transient ball hunting), and seal with an O-ring faceplate. Ensure motor accelerates through critical speed rapidly to lock in supercritical balance.
