"""
ENCARTA '95 : ELECTROMECHANICA - Physics & Kinematics Simulations Module
Contains museum-grade HTML5 Canvas physics simulations:
1. LeBlanc Supercritical Dynamic Balancer (Rotordynamic Phase Inversion)
2. Scrap Steel Spark Metallurgy Chamber (10,000 RPM Grinder & Particle Detonations)
3. Simpson 260 / Triplett Analog Multimeter (Damped Inertial Needle Physics)
4. Geneva Mechanism & Scotch Yoke CAD Kinematics
5. CD Spot Welder Phosphor CRT Oscilloscope (RLC Discharge Waveform & HAZ)
6. MindMaze '95 2.5D Isometric Dungeon Explorer
"""

ENCARTA_SIMS_JS = """
// ================= SIM 1: LEBLANC SUPERCRITICAL BALANCER =================
let balancerRPM = 600;
let balancerHasUnbalance = true;
let balancerAngle = 0;
// 4 tungsten-carbide ball bearings inside fluid raceway (radians)
let balancerBalls = [0.15, 0.45, 0.75, 1.05];
let balancerBallVels = [0, 0, 0, 0];
let balancerAnimId = null;
let seismoData = new Array(120).fill(0);
let tubShakeX = 0, tubShakeY = 0;
let tubShakeVelX = 0, tubShakeVelY = 0;

function setBalancerRPM(val) {
  balancerRPM = parseInt(val);
  document.getElementById('rpmDisplay').innerText = balancerRPM + ' RPM';
  document.getElementById('rpmSlider').value = balancerRPM;
  updateBalancerStatus();
}

function toggleUnbalance() {
  AudioEngine.click();
  balancerHasUnbalance = !balancerHasUnbalance;
  document.getElementById('btnUnbalance').classList.toggle('active', balancerHasUnbalance);
  document.getElementById('btnUnbalance').innerText = balancerHasUnbalance ? 'Eccentric Slug: ATTACHED' : 'Eccentric Slug: REMOVED';
  updateBalancerStatus();
}

function updateBalancerStatus() {
  const alert = document.getElementById('balancerAlert');
  if (!balancerHasUnbalance) {
    alert.className = 'mt-3 text-xs font-mono px-3 py-1.5 rounded border border-cyan-500/50 bg-cyan-950/60 text-cyan-300 text-center';
    alert.innerHTML = '⚖️ <strong>BALANCED ROTOR:</strong> Concentric rotation. Tub vibration &lt; 0.2 mm.';
    return;
  }
  if (balancerRPM < 400) {
    alert.className = 'mt-3 text-xs font-mono px-3 py-1.5 rounded border border-amber-500/50 bg-amber-950/60 text-amber-300 text-center';
    alert.innerHTML = '🔄 <strong>SUBCRITICAL ZONE (&lt; 400 RPM):</strong> Center of rotation follows geometric shaft. Balls lag and cluster near the heavy slug, amplifying orbital vibration.';
  } else if (balancerRPM <= 550) {
    alert.className = 'mt-3 text-xs font-mono px-3 py-1.5 rounded border border-red-500/80 bg-red-950/80 text-red-200 text-center animate-pulse';
    alert.innerHTML = '⚠️ <strong>CRITICAL RESONANCE (&sim; 450 RPM):</strong> Structural natural frequency (&omega; = &omega;n)! Tub violently shakes (&gt; 15 mm P-P). Acoustic clatter peak!';
  } else {
    alert.className = 'mt-3 text-xs font-mono px-3 py-1.5 rounded border border-emerald-500/80 bg-emerald-950/80 text-emerald-200 text-center';
    alert.innerHTML = '✨ <strong>SUPERCRITICAL PHASE INVERSION (&gt; 600 RPM):</strong> Rotor pivots about center of mass! Balls migrate exactly 180&deg; opposite heavy slug. Vibration drops to &lt; 0.4 mm!';
  }
}

function startBalancerSim() {
  if (balancerAnimId) cancelAnimationFrame(balancerAnimId);
  const canvas = document.getElementById('balancerCanvas');
  const seismoCanvas = document.getElementById('seismoCanvas');
  if (!canvas || !seismoCanvas) return;
  const ctx = canvas.getContext('2d');
  const sCtx = seismoCanvas.getContext('2d');

  const cx = canvas.width / 2;
  const cy = canvas.height / 2;
  const R_drum = 135;
  const R_outerRace = 118;
  const R_innerRace = 94;
  const R_raceMid = (R_outerRace + R_innerRace) / 2;
  const ballRadius = 9.5;

  let lastTime = performance.now();

  function render(now) {
    const dt = Math.min(0.04, (now - lastTime) / 1000);
    lastTime = now;

    const omega = balancerRPM * (Math.PI / 30); // rad/s
    balancerAngle += omega * dt;

    // Resonant frequency calculation (omega_n ~ 45 rad/s ~ 430 RPM)
    const omega_n = 45;
    const ratio = omega / omega_n;
    const damping = 0.12;

    // Phase lag of tub: phi = atan2(2 * damping * ratio, 1 - ratio * ratio)
    const phaseLag = Math.atan2(2 * damping * ratio, 1 - ratio * ratio);

    // Vibration amplitude of tub
    let baseAmp = 0;
    if (balancerHasUnbalance) {
      const denom = Math.sqrt(Math.pow(1 - ratio * ratio, 2) + Math.pow(2 * damping * ratio, 2));
      baseAmp = (ratio * ratio) / Math.max(0.2, denom);
      baseAmp = Math.min(18.0, baseAmp * 3.5);
    }

    // Dynamic ball behavior inside fluid raceway:
    // When supercritical (ratio > 1.3), balls migrate to opposite side of unbalance (PI rad offset from unbalance)
    // When subcritical (ratio < 0.9), balls gather near unbalance (0 rad offset)
    const targetOffset = (ratio > 1.15) ? Math.PI : 0.0;
    const isSupercritical = ratio > 1.15;

    // Update ball physics with viscous damping and inter-ball collision repulsion
    const ballMass = 0.05;
    const unbalanceMass = balancerHasUnbalance ? 0.22 : 0.0;

    for (let i = 0; i < balancerBalls.length; i++) {
      let relAngle = balancerBalls[i] - balancerAngle;
      // Normalize relAngle to [-PI, PI]
      relAngle = ((relAngle + Math.PI) % (Math.PI * 2)) - Math.PI;

      // Desired relative angle has a spread so balls don't occupy same point
      const spread = (i - 1.5) * 0.26;
      const targetRel = targetOffset + spread;
      let angleDiff = targetRel - relAngle;
      angleDiff = ((angleDiff + Math.PI) % (Math.PI * 2)) - Math.PI;

      // Fluid drag force pulls ball towards rotor speed, restoring force pulls toward target
      const stiffness = isSupercritical ? 18.0 : (ratio > 0.8 ? 5.0 : 8.0);
      const accel = angleDiff * stiffness - balancerBallVels[i] * 6.0;
      balancerBallVels[i] += accel * dt;
      balancerBalls[i] += (omega + balancerBallVels[i]) * dt;
    }

    // Inter-ball collision checks
    for (let i = 0; i < balancerBalls.length; i++) {
      for (let j = i + 1; j < balancerBalls.length; j++) {
        let diff = balancerBalls[j] - balancerBalls[i];
        diff = ((diff + Math.PI) % (Math.PI * 2)) - Math.PI;
        const minDist = (ballRadius * 2.2) / R_raceMid;
        if (Math.abs(diff) < minDist) {
          const overlap = minDist - Math.abs(diff);
          const sign = diff >= 0 ? 1 : -1;
          balancerBalls[i] -= sign * overlap * 0.5;
          balancerBalls[j] += sign * overlap * 0.5;
          const vAvg = (balancerBallVels[i] + balancerBallVels[j]) / 2;
          balancerBallVels[i] = vAvg;
          balancerBallVels[j] = vAvg;
        }
      }
    }

    // Net vibration vector (sum of unbalance + balls)
    let netVx = 0, netVy = 0;
    if (balancerHasUnbalance) {
      netVx += Math.cos(balancerAngle) * unbalanceMass;
      netVy += Math.sin(balancerAngle) * unbalanceMass;
    }
    for (let i = 0; i < balancerBalls.length; i++) {
      netVx += Math.cos(balancerBalls[i]) * ballMass;
      netVy += Math.sin(balancerBalls[i]) * ballMass;
    }

    const netMag = Math.hypot(netVx, netVy);
    const netAngle = Math.atan2(netVy, netVx);
    const finalVibe = baseAmp * (netMag / Math.max(0.01, unbalanceMass || 0.1));

    // Dynamic tub displacement with spring-mass-damper inertia
    const targetTubX = Math.cos(netAngle - phaseLag) * finalVibe;
    const targetTubY = Math.sin(netAngle - phaseLag) * finalVibe;
    tubShakeX += (targetTubX - tubShakeX) * 0.25;
    tubShakeY += (targetTubY - tubShakeY) * 0.25;

    // ================= DRAWING ROUTINE =================
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // 1. Draw outer cabinet frame & 4 angled suspension springs
    const tubCenterActualX = cx + tubShakeX;
    const tubCenterActualY = cy + tubShakeY;

    // Corner suspension anchors
    const corners = [
      { x: 30, y: 30 },
      { x: canvas.width - 30, y: 30 },
      { x: 30, y: canvas.height - 30 },
      { x: canvas.width - 30, y: canvas.height - 30 }
    ];

    corners.forEach((c, idx) => {
      // Attachment point on outer drum
      const ang = (idx === 0) ? -Math.PI * 0.75 : (idx === 1) ? -Math.PI * 0.25 : (idx === 2) ? Math.PI * 0.75 : Math.PI * 0.25;
      const attachX = tubCenterActualX + Math.cos(ang) * (R_drum + 10);
      const attachY = tubCenterActualY + Math.sin(ang) * (R_drum + 10);

      // Draw coiled spring line
      ctx.save();
      ctx.beginPath();
      ctx.moveTo(c.x, c.y);
      const coils = 12;
      const dx = (attachX - c.x) / coils;
      const dy = (attachY - c.y) / coils;
      const perpX = -(attachY - c.y) / Math.hypot(attachX - c.x, attachY - c.y) * 6;
      const perpY = (attachX - c.x) / Math.hypot(attachX - c.x, attachY - c.y) * 6;

      for (let k = 1; k < coils; k++) {
        const factor = (k % 2 === 0) ? 1 : -1;
        ctx.lineTo(c.x + dx * k + perpX * factor, c.y + dy * k + perpY * factor);
      }
      ctx.lineTo(attachX, attachY);
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 1.5;
      ctx.stroke();

      // Damper cylinder along corner
      ctx.beginPath();
      ctx.arc(c.x, c.y, 4, 0, Math.PI * 2);
      ctx.fillStyle = '#dfb15b';
      ctx.fill();
      ctx.restore();
    });

    // 2. Draw Washing Machine Drum & Race
    ctx.save();
    ctx.translate(tubCenterActualX, tubCenterActualY);

    // Outer stainless wash tub body with metallic brushed radial gradient
    const drumGrad = ctx.createRadialGradient(0, 0, 20, 0, 0, R_drum + 12);
    drumGrad.addColorStop(0, '#0a232b');
    drumGrad.addColorStop(0.6, '#174350');
    drumGrad.addColorStop(0.85, '#327c8f');
    drumGrad.addColorStop(0.95, '#1e5463');
    drumGrad.addColorStop(1, '#0c262e');

    ctx.beginPath();
    ctx.arc(0, 0, R_drum + 12, 0, Math.PI * 2);
    ctx.fillStyle = drumGrad;
    ctx.fill();
    ctx.strokeStyle = '#4db2c7';
    ctx.lineWidth = 2.5;
    ctx.stroke();

    // Spun metal circular machining rings
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.08)';
    ctx.lineWidth = 1;
    [30, 50, 70, 90, 110, 130].forEach(r => {
      ctx.beginPath();
      ctx.arc(0, 0, r, 0, Math.PI * 2);
      ctx.stroke();
    });

    // Laser-etched angle ticks every 30 deg
    ctx.save();
    ctx.rotate(balancerAngle);
    ctx.strokeStyle = 'rgba(223, 177, 91, 0.35)';
    for (let deg = 0; deg < 360; deg += 30) {
      const rad = deg * (Math.PI / 180);
      const isCard = deg % 90 === 0;
      ctx.beginPath();
      ctx.moveTo(Math.cos(rad) * (R_drum - (isCard ? 10 : 5)), Math.sin(rad) * (R_drum - (isCard ? 10 : 5)));
      ctx.lineTo(Math.cos(rad) * R_drum, Math.sin(rad) * R_drum);
      ctx.lineWidth = isCard ? 2 : 1;
      ctx.stroke();
    }
    ctx.restore();

    // 3. Fluid Channel Raceway
    ctx.beginPath();
    ctx.arc(0, 0, R_outerRace, 0, Math.PI * 2);
    ctx.arc(0, 0, R_innerRace, 0, Math.PI * 2, true);
    ctx.fillStyle = 'rgba(2, 14, 18, 0.95)';
    ctx.fill();
    ctx.strokeStyle = '#2a7c8e';
    ctx.lineWidth = 2;
    ctx.stroke();

    // Dynamic viscous turquoise fluid shimmer inside raceway
    const fluidGrad = ctx.createRadialGradient(0, 0, R_innerRace, 0, 0, R_outerRace);
    fluidGrad.addColorStop(0, 'rgba(6, 182, 212, 0.05)');
    fluidGrad.addColorStop(0.5, 'rgba(6, 182, 212, 0.35)');
    fluidGrad.addColorStop(1, 'rgba(6, 182, 212, 0.15)');

    ctx.beginPath();
    ctx.arc(0, 0, R_outerRace - 1, 0, Math.PI * 2);
    ctx.arc(0, 0, R_innerRace + 1, 0, Math.PI * 2, true);
    ctx.fillStyle = fluidGrad;
    ctx.fill();

    // Fluid wave shimmer (lagging rotation)
    ctx.save();
    ctx.rotate(balancerAngle * 0.92);
    ctx.beginPath();
    ctx.arc(0, 0, R_raceMid, 0, Math.PI * 2);
    ctx.strokeStyle = 'rgba(103, 232, 249, 0.25)';
    ctx.setLineDash([8, 12]);
    ctx.lineWidth = 4;
    ctx.stroke();
    ctx.restore();

    // 4. Draw Imbalance Slug (Eccentric Mass)
    if (balancerHasUnbalance) {
      const slugAng = balancerAngle;
      const slugX = Math.cos(slugAng) * (R_innerRace - 22);
      const slugY = Math.sin(slugAng) * (R_innerRace - 22);

      // Radial dynamic force vector arrow
      ctx.save();
      ctx.beginPath();
      ctx.moveTo(slugX, slugY);
      const vecLen = Math.min(65, 12 + baseAmp * 2.8);
      ctx.lineTo(slugX + Math.cos(slugAng) * vecLen, slugY + Math.sin(slugAng) * vecLen);
      ctx.strokeStyle = '#ef4444';
      ctx.lineWidth = 3;
      ctx.stroke();
      // Arrowhead
      ctx.translate(slugX + Math.cos(slugAng) * vecLen, slugY + Math.sin(slugAng) * vecLen);
      ctx.rotate(slugAng);
      ctx.beginPath();
      ctx.moveTo(0, 0);
      ctx.lineTo(-7, -4);
      ctx.lineTo(-7, 4);
      ctx.closePath();
      ctx.fillStyle = '#ef4444';
      ctx.fill();
      ctx.restore();

      // Heavy brass/steel slug with hazard crosshatch
      ctx.beginPath();
      ctx.arc(slugX, slugY, 14, 0, Math.PI * 2);
      const slugGrad = ctx.createRadialGradient(slugX - 4, slugY - 4, 2, slugX, slugY, 14);
      slugGrad.addColorStop(0, '#f87171');
      slugGrad.addColorStop(0.7, '#dc2626');
      slugGrad.addColorStop(1, '#7f1d1d');
      ctx.fillStyle = slugGrad;
      ctx.fill();
      ctx.strokeStyle = '#ffd978';
      ctx.lineWidth = 2;
      ctx.stroke();

      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 9px monospace';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText('SLUG', slugX, slugY);
    }

    // 5. Draw 3D Chrome Spheres (Balls)
    balancerBalls.forEach(ballAng => {
      const bx = Math.cos(ballAng) * R_raceMid;
      const by = Math.sin(ballAng) * R_raceMid;

      // Drop shadow on raceway
      ctx.beginPath();
      ctx.arc(bx + 2, by + 2, ballRadius, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(0, 0, 0, 0.6)';
      ctx.fill();

      // High-realism 3D chrome sphere with specular highlight
      const sphereGrad = ctx.createRadialGradient(
        bx - ballRadius * 0.35, by - ballRadius * 0.35, ballRadius * 0.08,
        bx, by, ballRadius
      );
      sphereGrad.addColorStop(0, '#ffffff'); // Intense specular highlight
      sphereGrad.addColorStop(0.2, '#f1f5f9');
      sphereGrad.addColorStop(0.5, '#94a3b8');
      sphereGrad.addColorStop(0.85, '#334155');
      sphereGrad.addColorStop(1, '#0f172a'); // Outer shadow ring

      ctx.beginPath();
      ctx.arc(bx, by, ballRadius, 0, Math.PI * 2);
      ctx.fillStyle = sphereGrad;
      ctx.fill();
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.4)';
      ctx.lineWidth = 1;
      ctx.stroke();
    });

    // 6. Center Shaft & Bearing Hub
    const hubGrad = ctx.createRadialGradient(-4, -4, 2, 0, 0, 24);
    hubGrad.addColorStop(0, '#fef08a');
    hubGrad.addColorStop(0.4, '#dfb15b');
    hubGrad.addColorStop(0.8, '#916a24');
    hubGrad.addColorStop(1, '#3a2404');

    ctx.beginPath();
    ctx.arc(0, 0, 24, 0, Math.PI * 2);
    ctx.fillStyle = hubGrad;
    ctx.fill();
    ctx.strokeStyle = '#ffeaa7';
    ctx.lineWidth = 2;
    ctx.stroke();

    // Center Hex Nut
    ctx.save();
    ctx.rotate(balancerAngle);
    ctx.beginPath();
    for (let k = 0; k < 6; k++) {
      const a = (k * Math.PI) / 3;
      const hx = Math.cos(a) * 11;
      const hy = Math.sin(a) * 11;
      if (k === 0) ctx.moveTo(hx, hy);
      else ctx.lineTo(hx, hy);
    }
    ctx.closePath();
    ctx.fillStyle = '#1e293b';
    ctx.fill();
    ctx.strokeStyle = '#94a3b8';
    ctx.lineWidth = 1.5;
    ctx.stroke();
    ctx.restore();

    ctx.restore(); // Restore tub transform

    // 7. Update Seismograph Waveform
    seismoData.push(tubShakeX);
    seismoData.shift();

    sCtx.fillStyle = '#02090b';
    sCtx.fillRect(0, 0, seismoCanvas.width, seismoCanvas.height);

    // Oscilloscope grid lines
    sCtx.strokeStyle = 'rgba(22, 78, 91, 0.4)';
    sCtx.lineWidth = 1;
    for (let x = 0; x < seismoCanvas.width; x += 30) {
      sCtx.beginPath(); sCtx.moveTo(x, 0); sCtx.lineTo(x, seismoCanvas.height); sCtx.stroke();
    }
    sCtx.beginPath();
    sCtx.moveTo(0, seismoCanvas.height / 2);
    sCtx.lineTo(seismoCanvas.width, seismoCanvas.height / 2);
    sCtx.strokeStyle = 'rgba(22, 78, 91, 0.8)';
    sCtx.stroke();

    // Waveform line with neon glow
    sCtx.save();
    sCtx.shadowBlur = 8;
    sCtx.shadowColor = isSupercritical ? '#10b981' : (ratio > 0.85 && ratio < 1.15 ? '#ef4444' : '#f59e0b');
    sCtx.strokeStyle = isSupercritical ? '#34d399' : (ratio > 0.85 && ratio < 1.15 ? '#f87171' : '#fbbf24');
    sCtx.lineWidth = 2.2;
    sCtx.beginPath();
    for (let i = 0; i < seismoData.length; i++) {
      const x = (i / seismoData.length) * seismoCanvas.width;
      const y = (seismoCanvas.height / 2) + seismoData[i] * 1.6;
      if (i === 0) sCtx.moveTo(x, y);
      else sCtx.lineTo(x, y);
    }
    sCtx.stroke();
    sCtx.restore();

    // Readout text on seismograph
    document.getElementById('seismoValue').innerText = (finalVibe * 2.0).toFixed(1) + ' mm P-P';
    document.getElementById('seismoValue').className = (finalVibe > 8) ? 'text-red-400 font-bold font-mono' : (finalVibe < 1.5 ? 'text-emerald-400 font-bold font-mono' : 'text-amber-400 font-bold font-mono');

    balancerAnimId = requestAnimationFrame(render);
  }

  balancerAnimId = requestAnimationFrame(render);
  updateBalancerStatus();
}

// ================= SIM 2: SCRAP STEEL SPARK METALLURGY =================
const METALS = [
  { id: '1095', name: 'High-Carbon 1095 Spring Steel', desc: 'Dense golden shower with explosive multi-branched carbon starbursts (chrysanthemums). Carbon oxidizes into CO micro-explosions.' },
  { id: '1018', name: 'Low-Carbon 1018 Mild Steel', desc: 'Long, straight straw-yellow carrier lines with rare single-fork bursts. Smooth laminar trajectories.' },
  { id: 'castiron', name: 'Cast Iron (Engine Block / Brake Rotor)', desc: 'Short, dull cherry-red stream with tiny bursts close to grinding wheel. Heavy graphite damping.' },
  { id: 'hss', name: 'M2 High-Speed Tool Steel (Drill Bit / Lathe Tool)', desc: 'Slender orange-red carrier lines ending in characteristic feathered / spearhead arrowheads with zero starbursts.' },
  { id: 'titanium', name: 'Titanium Grade 5 (Aerospace Scrap)', desc: 'Intense, blinding snow-white laser streaks with brilliant white floral bursts. Extremely high burn temp (&gt; 2,000&deg;C).' }
];

let selectedMetal = METALS[0];
let isGrinding = false;
let sparkParticles = [];
let wheelAngle = 0;
let sparksAnimId = null;

function setMetal(metalId) {
  AudioEngine.click();
  selectedMetal = METALS.find(m => m.id === metalId) || METALS[0];
  document.querySelectorAll('.metal-btn').forEach(b => b.classList.remove('active'));
  const btn = document.getElementById('btnMetal_' + metalId);
  if (btn) btn.classList.add('active');
  document.getElementById('metalTitle').innerText = selectedMetal.name;
  document.getElementById('metalDesc').innerText = selectedMetal.desc;
}

function startGrinding() {
  isGrinding = true;
  document.getElementById('btnGrind').classList.add('active');
  document.getElementById('sparkStatus').innerHTML = '<span class="text-amber-300 font-bold animate-pulse">🔥 GRINDING WORKPIECE:</span> Analyzing spark geometry &amp; thermal decay...';
  AudioEngine.grinderScreech(true);
}

function stopGrinding() {
  isGrinding = false;
  document.getElementById('btnGrind').classList.remove('active');
  document.getElementById('sparkStatus').innerText = 'Grinder idling at 10,000 RPM. Press and hold button to contact workpiece.';
  AudioEngine.grinderScreech(false);
}

function initSparkSim() {
  if (sparksAnimId) cancelAnimationFrame(sparksAnimId);
  const canvas = document.getElementById('sparksCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  const contactX = 145;
  const contactY = 190;
  const wheelCenterX = 100;
  const wheelCenterY = 190;
  const wheelRadius = 45;

  let lastTime = performance.now();

  function loop(now) {
    const dt = Math.min(0.04, (now - lastTime) / 1000);
    lastTime = now;

    // Dark shop environment with faint background persistence trail
    ctx.fillStyle = 'rgba(2, 9, 12, 0.32)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Floor / Anvil plate
    ctx.fillStyle = '#061a20';
    ctx.fillRect(0, 310, canvas.width, 30);
    ctx.strokeStyle = '#1b5e6f';
    ctx.lineWidth = 1;
    ctx.strokeRect(0, 310, canvas.width, 30);

    // 1. Draw High-Speed Grinding Wheel (10,000 RPM)
    wheelAngle += 45 * dt * 30;
    ctx.save();
    ctx.translate(wheelCenterX, wheelCenterY);

    // Cast-aluminum protective wheel guard
    ctx.beginPath();
    ctx.arc(0, 0, wheelRadius + 8, Math.PI * 0.45, Math.PI * 1.85);
    ctx.strokeStyle = '#475569';
    ctx.lineWidth = 14;
    ctx.stroke();

    // Spinning abrasive disc
    ctx.rotate(wheelAngle);
    const discGrad = ctx.createRadialGradient(0, 0, 8, 0, 0, wheelRadius);
    discGrad.addColorStop(0, '#334155');
    discGrad.addColorStop(0.7, '#1e293b');
    discGrad.addColorStop(1, '#0f172a');
    ctx.beginPath();
    ctx.arc(0, 0, wheelRadius, 0, Math.PI * 2);
    ctx.fillStyle = discGrad;
    ctx.fill();

    // Wheel grit motion blur texture
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.12)';
    ctx.lineWidth = 1.5;
    for (let k = 0; k < 8; k++) {
      const a = (k * Math.PI) / 4;
      ctx.beginPath();
      ctx.moveTo(Math.cos(a) * 12, Math.sin(a) * 12);
      ctx.lineTo(Math.cos(a) * (wheelRadius - 2), Math.sin(a) * (wheelRadius - 2));
      ctx.stroke();
    }

    // Steel Arbor Flange & Center Nut
    ctx.beginPath();
    ctx.arc(0, 0, 12, 0, Math.PI * 2);
    ctx.fillStyle = '#94a3b8';
    ctx.fill();
    ctx.strokeStyle = '#cbd5e1';
    ctx.stroke();
    ctx.restore();

    // 2. Draw Workpiece Bar clamped in vise
    ctx.save();
    ctx.fillStyle = '#475569';
    ctx.fillRect(contactX, contactY - 10, 75, 20);
    ctx.strokeStyle = '#94a3b8';
    ctx.lineWidth = 1.5;
    ctx.strokeRect(contactX, contactY - 10, 75, 20);
    ctx.fillStyle = '#e2e8f0';
    ctx.font = 'bold 9px monospace';
    ctx.fillText('STEEL BAR', contactX + 10, contactY + 3);
    ctx.restore();

    // 3. Molten Contact Zone Hotspot & Ambient Dynamic Light
    if (isGrinding) {
      // Ambient warm flash
      const ambGrad = ctx.createRadialGradient(contactX, contactY, 5, contactX, contactY, 140);
      ambGrad.addColorStop(0, 'rgba(249, 115, 22, 0.35)');
      ambGrad.addColorStop(1, 'rgba(249, 115, 22, 0)');
      ctx.fillStyle = ambGrad;
      ctx.beginPath();
      ctx.arc(contactX, contactY, 140, 0, Math.PI * 2);
      ctx.fill();

      // Incandescent molten white hotspot at contact point
      const hotGrad = ctx.createRadialGradient(contactX - 1, contactY, 1, contactX, contactY, 12);
      hotGrad.addColorStop(0, '#ffffff');
      hotGrad.addColorStop(0.3, '#fef08a');
      hotGrad.addColorStop(0.7, '#f97316');
      hotGrad.addColorStop(1, 'rgba(239, 68, 68, 0)');
      ctx.beginPath();
      ctx.arc(contactX, contactY, 12, 0, Math.PI * 2);
      ctx.fillStyle = hotGrad;
      ctx.fill();

      // Spawn particles based on selected metal
      const spawnCount = selectedMetal.id === '1095' ? 14 : (selectedMetal.id === 'titanium' ? 12 : 7);
      for (let s = 0; s < spawnCount; s++) {
        const initSpeed = Math.random() * 260 + 280; // pixels/sec
        const spreadAngle = (Math.random() - 0.35) * 0.42; // downward cone
        sparkParticles.push({
          x: contactX,
          y: contactY + (Math.random() - 0.5) * 8,
          vx: Math.cos(spreadAngle) * initSpeed,
          vy: Math.sin(spreadAngle) * initSpeed,
          life: 1.0,
          decay: Math.random() * 0.018 + 0.012,
          metal: selectedMetal.id,
          hasBurst: false,
          size: Math.random() * 1.5 + 1.2
        });
      }
    }

    // 4. Update and Render Particles
    for (let i = sparkParticles.length - 1; i >= 0; i--) {
      const p = sparkParticles[i];
      p.x += p.vx * dt;
      p.y += p.vy * dt;
      p.vy += 320 * dt; // Gravity
      p.vx *= (1 - 0.45 * dt); // Air drag
      p.life -= p.decay;

      // Floor bounce check
      if (p.y >= 310) {
        p.y = 310;
        p.vy = -p.vy * 0.42; // Restitution
        p.vx *= 0.65; // Floor friction
      }

      // Thermal cooling color spectrum
      let r, g, b, alpha = p.life;
      if (p.metal === 'titanium') {
        // Blinding electric snow-white
        r = 255; g = 255; b = 255;
      } else if (p.metal === 'castiron') {
        // Dull dark cherry red
        r = 220; g = Math.floor(40 * p.life); b = 20;
      } else if (p.life > 0.7) {
        // Initial 1400C white-hot
        r = 255; g = 255; b = Math.floor(200 * (p.life - 0.7) / 0.3);
      } else if (p.life > 0.35) {
        // Straw yellow to orange
        r = 255; g = Math.floor(140 + 100 * (p.life - 0.35) / 0.35); b = 20;
      } else {
        // Deep orange to dull cherry red
        r = Math.floor(180 + 75 * p.life / 0.35); g = Math.floor(40 * p.life / 0.35); b = 10;
      }

      // Draw particle trail
      ctx.save();
      ctx.beginPath();
      ctx.moveTo(p.x, p.y);
      ctx.lineTo(p.x - p.vx * 0.02, p.y - p.vy * 0.02);
      ctx.strokeStyle = `rgba(${r}, ${g}, ${b}, ${alpha})`;
      ctx.lineWidth = p.size;
      ctx.stroke();
      ctx.restore();

      // High-Carbon Secondary Detonations (Starburst Fireworks!)
      if (p.metal === '1095' && !p.hasBurst && p.life < 0.65 && Math.random() < 0.28) {
        p.hasBurst = true;
        // Explode into 5-8 sharp secondary micro-sparks
        const rays = Math.floor(Math.random() * 4 + 4);
        for (let rIdx = 0; rIdx < rays; rIdx++) {
          const rAng = Math.random() * Math.PI * 2;
          const rLen = Math.random() * 16 + 8;
          ctx.beginPath();
          ctx.moveTo(p.x, p.y);
          ctx.lineTo(p.x + Math.cos(rAng) * rLen, p.y + Math.sin(rAng) * rLen);
          ctx.strokeStyle = 'rgba(255, 255, 255, 0.9)';
          ctx.lineWidth = 1;
          ctx.stroke();
        }
      }

      // HSS Spearhead / Feathered tips
      if (p.metal === 'hss' && !p.hasBurst && p.life < 0.3) {
        p.hasBurst = true;
        ctx.beginPath();
        ctx.arc(p.x, p.y, 3, 0, Math.PI * 2);
        ctx.fillStyle = '#f97316';
        ctx.fill();
      }

      // Remove dead particles
      if (p.life <= 0 || p.x > canvas.width || p.x < 0) {
        sparkParticles.splice(i, 1);
      }
    }

    sparksAnimId = requestAnimationFrame(loop);
  }

  sparksAnimId = requestAnimationFrame(loop);
}

// ================= SIM 3: WIRE WIZARD WITH SIMPSON 260 METER =================
const WIRE_DIAGNOSTICS = {
  2: {
    title: "2-Wire Motor Architecture (DC or Series Universal)",
    ohms: 12.4,
    scaleType: 'ohms',
    steps: [
      "1. Multimeter measures 12.4 &Omega; across the 2 leads.",
      "2. Slowly rotate output shaft by hand through 360 degrees.",
      "3. Strong magnetic cogging detents felt &rarr; Permanent Magnet DC (PMDC).",
      "4. Zero cogging detents + carbon brush sparking &rarr; Series-Wound AC/DC Universal."
    ],
    diagnosis: "<strong>Permanent Magnet DC (PMDC) Motor:</strong> Typical of treadmill spindles (130V DC), cordless power drills, and 12V automotive blowers. Drive with BTS7960 H-Bridge, KBIC SCR board, or DC battery directly.",
    controller: "BTS7960 43A PWM H-Bridge or KBIC-120 SCR Speed Controller"
  },
  3: {
    title: "3-Wire Motor Architecture (3-Phase Brushless BLDC / PMSM)",
    ohms: 0.8,
    scaleType: 'ohms',
    steps: [
      "1. Measure resistance between Phase A-B: 0.8 &Omega;.",
      "2. Measure resistance between Phase B-C: 0.8 &Omega;.",
      "3. Measure resistance between Phase A-C: 0.8 &Omega;.",
      "4. Exactly identical low resistance confirms symmetric 3-phase Wye/Delta winding."
    ],
    diagnosis: "<strong>3-Phase Brushless DC (BLDC) / Permanent Magnet Synchronous (PMSM):</strong> Typical of hoverboard hub motors, washing machine direct-drive stators, e-scooters, and drone motors. Requires 3-phase inverter.",
    controller: "VESC 6.0, ODrive Robotics Controller, or Sensored E-Bike Controller"
  },
  4: {
    title: "4-Wire Motor Architecture (Bipolar Stepper Motor)",
    ohms: 3.2,
    scaleType: 'ohms',
    steps: [
      "1. Probe all pairs to find 2 completely isolated winding coils.",
      "2. Pair A-B measures 3.2 &Omega;. Pair C-D measures 3.2 &Omega;.",
      "3. Cross-resistance between pairs (A-C, A-D) is Infinite (&infin; &Omega;).",
      "4. Shorting Phase A-B increases hand-shaft turning resistance (back-EMF brake test)."
    ],
    diagnosis: "<strong>Bipolar Stepper Motor (NEMA 17 / NEMA 23):</strong> Salvaged from laser printers, flatbed copiers, and 3D printers. High-precision microstepping positioning.",
    controller: "A4988, TMC2209 SilentStepStick, or DM542 Industrial Microstep Driver"
  },
  5: {
    title: "5-Wire Motor Architecture (Unipolar 4-Phase Stepper)",
    ohms: 28.0,
    scaleType: 'ohms',
    steps: [
      "1. Find the 1 Common wire that has identical resistance (28 &Omega;) to all other 4 wires.",
      "2. Resistance between any two non-common phase leads is exactly double (56 &Omega;).",
      "3. Common wire is tied to +12V/+24V power supply rail.",
      "4. Phase wires are switched sequentially to ground with low-side N-channel MOSFETs."
    ],
    diagnosis: "<strong>Unipolar 4-Phase Stepper Motor (28BYJ-48 style):</strong> Salvaged from air conditioner louver vanes, optical scanners, and robotic pan-tilt turrets.",
    controller: "ULN2003 Darlington Transistor Array or 4-channel N-Channel MOSFET Board"
  },
  6: {
    title: "6-Wire Motor Architecture (Universal Stepper or 3-Phase + Star)",
    ohms: 6.4,
    scaleType: 'ohms',
    steps: [
      "1. Identifies 2 independent center-tapped coils.",
      "2. Center tap to either end measures 6.4 &Omega;; end-to-end measures 12.8 &Omega;.",
      "3. Can be wired as Unipolar (using center taps) OR Bipolar (ignoring center taps for +40% torque)."
    ],
    diagnosis: "<strong>Universal 6-Wire Stepper Motor:</strong> Extremely versatile donor motor found in heavy industrial plotters and office copiers.",
    controller: "Can be driven as Unipolar (ULN2003) or High-Torque Bipolar (TB6600 / DM542)"
  },
  8: {
    title: "8-Wire Motor Architecture (4-Phase Bipolar / Switched Reluctance)",
    ohms: 1.8,
    scaleType: 'ohms',
    steps: [
      "1. 4 completely separate independent coils found.",
      "2. Can be wired in Series (maximum holding torque at low RPM) or Parallel (high RPM capability).",
      "3. Confirm phase polarity with 9V battery kick test."
    ],
    diagnosis: "<strong>8-Wire High-Torque Industrial Stepper:</strong> Top-tier CNC positioning motor from industrial automation gantry scrap.",
    controller: "Digital DSP Microstepping Drive (Leadshine DM860H or Geckodrive G203V)"
  }
};

let currentWireCount = 3;
let targetNeedleOhms = 0.8;
let currentNeedleAngle = Math.PI * 1.85; // Resting at infinity (left/right)
let needleVelocity = 0;
let meterAnimId = null;

function testWireCount(wires) {
  AudioEngine.click();
  currentWireCount = wires;
  document.querySelectorAll('.wire-btn').forEach(b => b.classList.remove('active'));
  const btn = document.getElementById('btnWire_' + wires);
  if (btn) btn.classList.add('active');

  const diag = WIRE_DIAGNOSTICS[wires];
  targetNeedleOhms = diag.ohms;

  // Update DOM readouts
  document.getElementById('wizardMotorTitle').innerHTML = diag.title;
  let stepsHtml = '<ul class="space-y-1">';
  diag.steps.forEach(s => stepsHtml += `<li class="text-[11px] font-mono text-cyan-200">${s}</li>`);
  stepsHtml += '</ul>';
  document.getElementById('wizardSteps').innerHTML = stepsHtml;
  document.getElementById('wizardDiagnosis').innerHTML = diag.diagnosis;
  document.getElementById('wizardController').innerText = diag.controller;
  document.getElementById('dmmReadout').innerHTML = `${diag.ohms.toFixed(1)} &Omega;`;
}

function initMeterSim() {
  if (meterAnimId) cancelAnimationFrame(meterAnimId);
  const canvas = document.getElementById('dmmCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  const pivotX = canvas.width / 2;
  const pivotY = canvas.height - 15;
  const arcRadius = 120;

  // Ohms scale non-linear mapping (Infinity on left, 0 on right)
  function ohmsToAngle(ohms) {
    const minAngle = Math.PI * 1.15; // Infinity
    const maxAngle = Math.PI * 1.85; // 0 Ohms
    // Logarithmic distribution
    const clamped = Math.max(0.01, Math.min(2000, ohms));
    const factor = Math.log10(clamped + 1) / Math.log10(2001);
    return maxAngle - factor * (maxAngle - minAngle);
  }

  let lastTime = performance.now();

  function render(now) {
    const dt = Math.min(0.04, (now - lastTime) / 1000);
    lastTime = now;

    // Second-order physical needle physics with mass, spring tension, and damping
    const targetAngle = ohmsToAngle(targetNeedleOhms);
    const stiffness = 85.0;
    const damping = 12.0;
    const accel = (targetAngle - currentNeedleAngle) * stiffness - needleVelocity * damping;
    needleVelocity += accel * dt;
    currentNeedleAngle += needleVelocity * dt;

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // 1. Simpson 260 Dial Background
    const dialGrad = ctx.createLinearGradient(0, 0, 0, canvas.height);
    dialGrad.addColorStop(0, '#f8fafc');
    dialGrad.addColorStop(1, '#e2e8f0');
    ctx.fillStyle = dialGrad;
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // 2. Mirrored Anti-Parallax Strip
    ctx.beginPath();
    ctx.arc(pivotX, pivotY, arcRadius - 16, Math.PI * 1.15, Math.PI * 1.85);
    ctx.arc(pivotX, pivotY, arcRadius - 24, Math.PI * 1.85, Math.PI * 1.15, true);
    ctx.fillStyle = '#cbd5e1';
    ctx.fill();
    ctx.strokeStyle = '#94a3b8';
    ctx.lineWidth = 1;
    ctx.stroke();

    // 3. Arched Resistance Scales & Ticks
    ctx.beginPath();
    ctx.arc(pivotX, pivotY, arcRadius, Math.PI * 1.15, Math.PI * 1.85);
    ctx.strokeStyle = '#0f172a';
    ctx.lineWidth = 1.5;
    ctx.stroke();

    // Major Ohms Ticks: Inf, 2k, 500, 100, 50, 20, 10, 5, 2, 0
    const ticks = [
      { val: 2000, label: '∞' },
      { val: 500, label: '500' },
      { val: 100, label: '100' },
      { val: 50, label: '50' },
      { val: 20, label: '20' },
      { val: 10, label: '10' },
      { val: 5, label: '5' },
      { val: 2, label: '2' },
      { val: 0, label: '0' }
    ];

    ctx.fillStyle = '#0f172a';
    ctx.font = 'bold 8px monospace';
    ctx.textAlign = 'center';

    ticks.forEach(t => {
      const a = ohmsToAngle(t.val);
      const x1 = pivotX + Math.cos(a) * (arcRadius - 10);
      const y1 = pivotY + Math.sin(a) * (arcRadius - 10);
      const x2 = pivotX + Math.cos(a) * arcRadius;
      const y2 = pivotY + Math.sin(a) * arcRadius;
      ctx.beginPath();
      ctx.moveTo(x1, y1);
      ctx.lineTo(x2, y2);
      ctx.stroke();
      const lx = pivotX + Math.cos(a) * (arcRadius - 16);
      const ly = pivotY + Math.sin(a) * (arcRadius - 16);
      ctx.fillText(t.label, lx, ly);
    });

    // Red DCV scale line
    ctx.beginPath();
    ctx.arc(pivotX, pivotY, arcRadius - 32, Math.PI * 1.15, Math.PI * 1.85);
    ctx.strokeStyle = '#dc2626';
    ctx.lineWidth = 1.2;
    ctx.stroke();

    // 4. Parallax Needle Shadow
    const shadowAng = currentNeedleAngle + 0.015;
    ctx.beginPath();
    ctx.moveTo(pivotX, pivotY);
    ctx.lineTo(pivotX + Math.cos(shadowAng) * (arcRadius + 5), pivotY + Math.sin(shadowAng) * (arcRadius + 5));
    ctx.strokeStyle = 'rgba(0, 0, 0, 0.25)';
    ctx.lineWidth = 1.5;
    ctx.stroke();

    // 5. Galvanometer Aluminum Pointer Needle
    ctx.save();
    ctx.beginPath();
    ctx.moveTo(pivotX, pivotY);
    ctx.lineTo(pivotX + Math.cos(currentNeedleAngle) * (arcRadius + 6), pivotY + Math.sin(currentNeedleAngle) * (arcRadius + 6));
    ctx.strokeStyle = '#b91c1c';
    ctx.lineWidth = 1.5;
    ctx.stroke();

    // Jeweled center pivot with brass cap
    ctx.beginPath();
    ctx.arc(pivotX, pivotY, 9, 0, Math.PI * 2);
    ctx.fillStyle = '#334155';
    ctx.fill();
    ctx.strokeStyle = '#dfb15b';
    ctx.lineWidth = 2;
    ctx.stroke();
    ctx.restore();

    meterAnimId = requestAnimationFrame(render);
  }

  meterAnimId = requestAnimationFrame(render);
}

// ================= SIM 4: GENEVA MECHANISM & SCOTCH YOKE =================
let kinematicMode = 'geneva';
let genevaSpeed = 25; // RPM
let genevaAngle = 0;
let genevaAnimId = null;

function setKinematicMode(mode) {
  AudioEngine.click();
  kinematicMode = mode;
  document.getElementById('btnModeGeneva').classList.toggle('active', mode === 'geneva');
  document.getElementById('btnModeYoke').classList.toggle('active', mode === 'scotchyoke');
  document.getElementById('kinematicTitle').innerText = mode === 'geneva' ? 'Maltese Cross Geneva Drive (Intermittent Motion)' : 'Scotch Yoke Mechanism (Harmonic Conversion)';
  document.getElementById('kinematicDesc').innerText = mode === 'geneva' 
    ? 'Converts continuous rotary input into precise, dwell-locked 90-degree indexing steps. Hallmark discontinuous acceleration spikes at slot entry.'
    : 'Converts rotary motion into pure simple harmonic linear motion with zero angular harmonic distortion (unlike crank-slider mechanisms).';
}

function initGenevaSim() {
  if (genevaAnimId) cancelAnimationFrame(genevaAnimId);
  const canvas = document.getElementById('genevaCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let lastTime = performance.now();

  function render(now) {
    const dt = Math.min(0.04, (now - lastTime) / 1000);
    lastTime = now;

    const omega = genevaSpeed * (Math.PI / 30);
    genevaAngle += omega * dt;

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    if (kinematicMode === 'geneva') {
      // 4-Slot Maltese Cross Geneva Drive
      const driverX = 145, driverY = 170;
      const wheelX = 300, wheelY = 170;
      const dDist = wheelX - driverX; // 155 px
      const driverR = 60;
      const pinR = 48;
      const wheelR = 85;

      // Pin position
      const pinX = driverX + Math.cos(genevaAngle) * pinR;
      const pinY = driverY + Math.sin(genevaAngle) * pinR;

      // Geneva wheel angle calculation based on pin engagement
      const normAng = ((genevaAngle % (Math.PI * 2)) + Math.PI * 2) % (Math.PI * 2);
      const isEngaged = (normAng < Math.PI * 0.25 || normAng > Math.PI * 1.75);
      let wheelAngle = 0;
      if (isEngaged) {
        const dx = pinX - wheelX;
        const dy = pinY - wheelY;
        wheelAngle = Math.atan2(dy, dx);
      } else {
        const step = Math.floor(genevaAngle / (Math.PI * 2));
        wheelAngle = step * (Math.PI / 2);
      }

      // Draw Driver Wheel
      ctx.save();
      ctx.translate(driverX, driverY);
      ctx.beginPath();
      ctx.arc(0, 0, driverR, 0, Math.PI * 2);
      ctx.fillStyle = '#0f2b33';
      ctx.fill();
      ctx.strokeStyle = '#2a7c8e';
      ctx.lineWidth = 2;
      ctx.stroke();

      // Locking crescent disk
      ctx.beginPath();
      ctx.arc(0, 0, driverR - 18, Math.PI * 0.35, Math.PI * 1.65);
      ctx.strokeStyle = '#4db2c7';
      ctx.lineWidth = 4;
      ctx.stroke();
      ctx.restore();

      // Drive Pin
      ctx.beginPath();
      ctx.arc(pinX, pinY, 7, 0, Math.PI * 2);
      ctx.fillStyle = '#ef4444';
      ctx.fill();
      ctx.strokeStyle = '#ffd978';
      ctx.lineWidth = 2;
      ctx.stroke();

      // Draw Machined Brass Geneva 4-Slot Wheel
      ctx.save();
      ctx.translate(wheelX, wheelY);
      ctx.rotate(wheelAngle);

      // Brass Maltese Cross body
      const brassGrad = ctx.createRadialGradient(0, 0, 10, 0, 0, wheelR);
      brassGrad.addColorStop(0, '#fef08a');
      brassGrad.addColorStop(0.5, '#dfb15b');
      brassGrad.addColorStop(1, '#916a24');

      ctx.beginPath();
      ctx.arc(0, 0, wheelR, 0, Math.PI * 2);
      ctx.fillStyle = brassGrad;
      ctx.fill();
      ctx.strokeStyle = '#ffd978';
      ctx.lineWidth = 2;
      ctx.stroke();

      // 4 Radial Drive Slots
      ctx.fillStyle = '#041216';
      for (let s = 0; s < 4; s++) {
        ctx.save();
        ctx.rotate((s * Math.PI) / 2);
        ctx.fillRect(0, -6, wheelR + 2, 12);
        ctx.beginPath();
        ctx.arc(wheelR - 20, 0, 14, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
      }

      // Center bronze bushing
      ctx.beginPath();
      ctx.arc(0, 0, 18, 0, Math.PI * 2);
      ctx.fillStyle = '#1e293b';
      ctx.fill();
      ctx.strokeStyle = '#dfb15b';
      ctx.lineWidth = 2;
      ctx.stroke();
      ctx.restore();

    } else {
      // Scotch Yoke Mechanism
      const crankX = 140, crankY = 170;
      const crankR = 52;
      const pinX = crankX + Math.cos(genevaAngle) * crankR;
      const pinY = crankY + Math.sin(genevaAngle) * crankR;

      // Linear slider displacement: X(t) = pinX
      const yokeX = pinX;

      // Draw Rotating Crank Wheel
      ctx.beginPath();
      ctx.arc(crankX, crankY, crankR + 10, 0, Math.PI * 2);
      ctx.fillStyle = '#08232a';
      ctx.fill();
      ctx.strokeStyle = '#1b6170';
      ctx.lineWidth = 2;
      ctx.stroke();

      // Crank Arm
      ctx.beginPath();
      ctx.moveTo(crankX, crankY);
      ctx.lineTo(pinX, pinY);
      ctx.strokeStyle = '#dfb15b';
      ctx.lineWidth = 6;
      ctx.stroke();

      // Drive Pin
      ctx.beginPath();
      ctx.arc(pinX, pinY, 7, 0, Math.PI * 2);
      ctx.fillStyle = '#ef4444';
      ctx.fill();
      ctx.stroke();

      // Vertical Slotted Yoke
      ctx.save();
      ctx.fillStyle = '#174a56';
      ctx.fillRect(yokeX - 10, crankY - 75, 20, 150);
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2;
      ctx.strokeRect(yokeX - 10, crankY - 75, 20, 150);

      // Internal Slot Groove
      ctx.fillStyle = '#030d0f';
      ctx.fillRect(yokeX - 5, crankY - 65, 10, 130);

      // Reciprocating Output Ram
      ctx.fillStyle = '#dfb15b';
      ctx.fillRect(yokeX + 10, crankY - 6, 180, 12);
      ctx.strokeStyle = '#ffffff';
      ctx.strokeRect(yokeX + 10, crankY - 6, 180, 12);
      ctx.restore();
    }

    genevaAnimId = requestAnimationFrame(render);
  }

  genevaAnimId = requestAnimationFrame(render);
}

// ================= SIM 5: CD SPOT WELDER CRT OSCILLOSCOPE =================
let spotCap = 1.0; // Farads
let spotVolts = 22.0; // Volts
let spotResistance = 0.003; // 3 milliohms
let spotInductance = 120e-9; // 120 nH

function updateSpotWelder() {
  const cap = parseFloat(document.getElementById('sliderCap').value);
  const v = parseFloat(document.getElementById('sliderVolts').value);
  document.getElementById('valCap').innerText = cap.toFixed(2) + ' F';
  document.getElementById('valVolts').innerText = v.toFixed(0) + ' V';

  const joules = 0.5 * cap * v * v;
  const peakCurrent = v / (spotResistance + 0.001);
  const pulseMs = (cap * spotResistance * 1000).toFixed(1);

  document.getElementById('spotJoules').innerText = joules.toFixed(1) + ' J';
  document.getElementById('spotCurrent').innerText = peakCurrent.toFixed(0) + ' A';
  document.getElementById('spotPulse').innerText = pulseMs + ' ms';

  drawSpotWaveform(cap, v, peakCurrent);
}

function drawSpotWaveform(cap, v, iPeak) {
  const canvas = document.getElementById('pulseCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  ctx.fillStyle = '#020b08';
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  // Phosphor Green CRT Graticule Grid
  ctx.strokeStyle = 'rgba(16, 185, 129, 0.2)';
  ctx.lineWidth = 1;
  for (let x = 0; x < canvas.width; x += 40) {
    ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height); ctx.stroke();
  }
  for (let y = 0; y < canvas.height; y += 30) {
    ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(canvas.width, y); ctx.stroke();
  }

  // CRT Beam Bloom Waveform
  ctx.save();
  ctx.shadowBlur = 12;
  ctx.shadowColor = '#10b981';
  ctx.strokeStyle = '#34d399';
  ctx.lineWidth = 2.5;

  ctx.beginPath();
  const baseline = canvas.height - 40;
  ctx.moveTo(30, baseline);

  // RLC discharge waveform equation: I(t) = (V/omega*L) * exp(-alpha*t) * sin(omega*t)
  const tau = cap * spotResistance * 1.5;
  for (let t = 0; t < canvas.width - 60; t++) {
    const timeNorm = t / 40.0;
    const current = Math.exp(-timeNorm / Math.max(0.2, tau)) * Math.sin(timeNorm * 1.2);
    const y = baseline - Math.max(0, current) * 160;
    ctx.lineTo(30 + t, y);
  }
  ctx.stroke();
  ctx.restore();

  // HAZ Warning Marker
  const joules = 0.5 * cap * v * v;
  ctx.fillStyle = (joules > 180) ? '#ef4444' : '#10b981';
  ctx.font = 'bold 11px monospace';
  ctx.fillText(`PULSE ENERGY: ${joules.toFixed(1)} J | ${joules > 180 ? 'DANGER: LITHIUM CAN PUNCTURE' : 'SAFE: 0.15mm PURE NICKEL WELD'}`, 40, 30);
}

// ================= SIM 6: MINDMAZE '95 ISOMETRIC DUNGEON =================
let playerPos = { x: 2, y: 2 };
let playerTorch = 0;
let currentQuestionIndex = 0;
let solvedRooms = new Set(['2,2']);
let playerInventory = [
  { name: 'Multimeter Probes (CAT III)', val: '$18' },
  { name: 'Insulated Crowbar (18-inch)', val: '$14' }
];

function initMindMaze() {
  const canvas = document.getElementById('mazeCanvas');
  if (!canvas) return;
  drawIsometricDungeon();
  updateInventoryUI();
}

function drawIsometricDungeon() {
  const canvas = document.getElementById('mazeCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  const tileW = 68, tileH = 34;
  const originX = canvas.width / 2, originY = 50;

  playerTorch += 0.08;
  const flicker = Math.sin(playerTorch * 3) * 4 + Math.cos(playerTorch * 7) * 2;

  // 1. Draw 5x5 Isometric Dungeon Grid
  for (let x = 0; x < 5; x++) {
    for (let y = 0; y < 5; y++) {
      const isoX = originX + (x - y) * (tileW / 2);
      const isoY = originY + (x + y) * (tileH / 2);
      const isCurrent = (x === playerPos.x && y === playerPos.y);
      const isSolved = solvedRooms.has(`${x},${y}`);

      // Floor slate tile
      ctx.beginPath();
      ctx.moveTo(isoX, isoY);
      ctx.lineTo(isoX + tileW / 2, isoY + tileH / 2);
      ctx.lineTo(isoX, isoY + tileH);
      ctx.lineTo(isoX - tileW / 2, isoY + tileH / 2);
      ctx.closePath();

      ctx.fillStyle = isCurrent ? '#0d3844' : (isSolved ? '#082329' : '#041317');
      ctx.fill();
      ctx.strokeStyle = isSolved ? '#2a7c8e' : '#144652';
      ctx.lineWidth = 1;
      ctx.stroke();

      // Outer castle dungeon walls
      if (x === 0 || y === 0) {
        ctx.fillStyle = '#020a0d';
        ctx.fillRect(isoX - tileW / 2, isoY - 24, tileW, 24);
        ctx.strokeStyle = '#1b5e6f';
        ctx.strokeRect(isoX - tileW / 2, isoY - 24, tileW, 24);
      }

      // Question Door with Runic Hazard Lock
      if ((x === 4 && y === 2) || (x === 0 && y === 4)) {
        ctx.fillStyle = '#b45309';
        ctx.fillRect(isoX - 8, isoY - 14, 16, 26);
        ctx.strokeStyle = '#ffd978';
        ctx.strokeRect(isoX - 8, isoY - 14, 16, 26);
      }

      // Player Scrapper Sprite
      if (isCurrent) {
        // Dynamic Torchlight Radial Bloom
        const torchGrad = ctx.createRadialGradient(isoX, isoY + 5, 2, isoX, isoY + 5, 65 + flicker);
        torchGrad.addColorStop(0, 'rgba(253, 224, 71, 0.45)');
        torchGrad.addColorStop(0.5, 'rgba(249, 115, 22, 0.2)');
        torchGrad.addColorStop(1, 'rgba(0, 0, 0, 0)');
        ctx.fillStyle = torchGrad;
        ctx.beginPath();
        ctx.arc(isoX, isoY + 5, 65 + flicker, 0, Math.PI * 2);
        ctx.fill();

        // Pixel-art Scrapper Body
        ctx.beginPath();
        ctx.arc(isoX, isoY + tileH / 2 - 12, 11, 0, Math.PI * 2);
        ctx.fillStyle = '#dfb15b';
        ctx.fill();
        ctx.strokeStyle = '#ffffff';
        ctx.lineWidth = 1.5;
        ctx.stroke();

        // Hard hat
        ctx.fillStyle = '#f59e0b';
        ctx.fillRect(isoX - 9, isoY + tileH / 2 - 24, 18, 7);

        ctx.fillStyle = '#020b0e';
        ctx.font = 'bold 8px monospace';
        ctx.textAlign = 'center';
        ctx.fillText('SCRAPPER', isoX, isoY + tileH / 2 - 26);
      }
    }
  }
}

function movePlayer(dx, dy) {
  AudioEngine.click();
  const nx = Math.max(0, Math.min(4, playerPos.x + dx));
  const ny = Math.max(0, Math.min(4, playerPos.y + dy));
  playerPos.x = nx;
  playerPos.y = ny;
  drawIsometricDungeon();

  // Trigger Chamber Quiz
  const roomKey = `${nx},${ny}`;
  if (!solvedRooms.has(roomKey)) {
    triggerRoomQuiz();
  }
}

function triggerRoomQuiz() {
  const q = MINDMAZE_QUESTIONS[currentQuestionIndex % MINDMAZE_QUESTIONS.length];
  document.getElementById('mazeDoorwayAlert').classList.remove('hidden');
  document.getElementById('quizQuestion').innerText = q.q;

  let choicesHtml = '';
  q.options.forEach((opt, idx) => {
    choicesHtml += `
      <button onclick="answerQuiz(${idx})" class="encarta-btn w-full text-left px-3 py-2 rounded text-xs hover:border-amber-400">
        <span class="text-amber-300 font-bold mr-2">${String.fromCharCode(65 + idx)}.</span> ${opt}
      </button>
    `;
  });
  document.getElementById('quizChoices').innerHTML = choicesHtml;
}

function answerQuiz(choiceIdx) {
  const q = MINDMAZE_QUESTIONS[currentQuestionIndex % MINDMAZE_QUESTIONS.length];
  if (choiceIdx === q.correct) {
    AudioEngine.victory();
    solvedRooms.add(`${playerPos.x},${playerPos.y}`);
    currentQuestionIndex++;
    document.getElementById('mazeDoorwayAlert').classList.add('hidden');

    // Add loot to pouch
    const loots = [
      { name: '36-Pole Pancake Stator', val: '$85' },
      { name: 'Bosch 180-Bar ABS Pump', val: '$60' },
      { name: 'DLP Micromirror Array', val: '$120' },
      { name: 'Heidenhain 0.1um Glass Scale', val: '$240' }
    ];
    playerInventory.push(loots[currentQuestionIndex % loots.length]);
    updateInventoryUI();
    drawIsometricDungeon();
    alert("✨ DOORWAY UNLOCKED! Runic seal broken. Harvested component added to inventory!");
  } else {
    AudioEngine.buzz();
    alert("❌ INCORRECT HARVEST PROTOCOL! The safety shunt blows. Study the Encyclopedia text and try again!");
  }
}

function updateInventoryUI() {
  const invContainer = document.getElementById('playerInventoryList');
  if (!invContainer) return;
  invContainer.innerHTML = '';
  playerInventory.forEach(item => {
    invContainer.innerHTML += `
      <div class="px-2.5 py-1 rounded bg-[#031317] border border-[#164e5b] text-[11px] font-mono flex items-center justify-between">
        <span class="text-slate-200">💎 ${item.name}</span>
        <span class="text-emerald-400 font-bold ml-2">${item.val}</span>
      </div>
    `;
  });
}
"""
