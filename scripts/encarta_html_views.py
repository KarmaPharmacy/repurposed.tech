"""
ENCARTA '95 : ELECTROMECHANICA - HTML Layout & Views Module
Defines the complete skeuomorphic user interface:
- Top CD-ROM Navigation Bar & Audio VU Visualizer
- The Overhauled Left Volume & Chapter Atlas with labels, sub-labels, and icons
- Unabridged Article Reading Room
- Physics & Kinematics Laboratory (5 Simulators)
- 50 Engineering Blueprints Dossier
- Appliance X-Ray 4-Layer Peeler
- MindMaze '95 Isometric Dungeon Explorer
- Scrap Atlas (88 Donors Matrix)
"""

ENCARTA_HTML = """
<!-- Top Title Bar (Classic Multimedia CD-ROM Chrome) -->
<header class="gold-plaque px-4 py-2 flex flex-wrap items-center justify-between shadow-xl relative z-40 border-b-2 border-[#ffd978]">
  <div class="flex items-center space-x-3">
    <!-- Spinning Gold CD-ROM Icon -->
    <div class="w-9 h-9 rounded-full bg-gradient-to-tr from-amber-600 via-yellow-200 to-amber-700 p-0.5 shadow-lg flex items-center justify-center">
      <div class="w-full h-full rounded-full bg-[#1e1302] flex items-center justify-center relative overflow-hidden spinning-cd">
        <div class="w-3 h-3 rounded-full bg-gradient-to-tr from-yellow-300 to-amber-600 border border-amber-950"></div>
        <div class="absolute inset-0 bg-gradient-to-r from-transparent via-white/40 to-transparent transform -rotate-45"></div>
      </div>
    </div>
    <div>
      <h1 class="text-base md:text-lg font-black tracking-wider uppercase font-serif flex items-center space-x-2 text-[#381f02]">
        <span>ENCARTA '95 : ELECTROMECHANICA</span>
      </h1>
      <p class="text-[10px] md:text-[11px] font-sans font-bold text-[#5c3707] tracking-tight">
        The Maker's Bible of Electromechanical Salvage &bull; 15 Volumes &bull; 36 Chapters &bull; 50 Blueprints &bull; 88 Donors &bull; 82,000+ Words
      </p>
    </div>
  </div>

  <!-- Audio Controls & Real-Time VU Visualizer -->
  <div class="flex items-center space-x-3 my-1">
    <!-- 16-Band VU Equalizer -->
    <div class="hidden lg:flex flex-col items-center bg-[#02080a] border border-[#164e5b] px-2.5 py-1 rounded shadow-inner">
      <div class="text-[9px] font-mono text-[#38bdf8] uppercase tracking-wider mb-0.5">AUDIO SPECTRUM</div>
      <canvas id="vuCanvas" width="110" height="18"></canvas>
    </div>

    <!-- Speech Tour Button -->
    <button onclick="SpeechNarrator.toggle()" id="btnAudioTour" 
            class="encarta-btn px-3 py-1.5 rounded text-xs flex items-center space-x-1.5 font-bold shadow">
      <span id="audioTourIcon">🎙️</span>
      <span id="audioTourLabel">AUDIO TOUR</span>
    </button>

    <!-- CRT Filter Toggle -->
    <button onclick="toggleCRT()" class="encarta-btn px-2.5 py-1.5 rounded text-xs font-mono font-bold">
      CRT FX
    </button>

    <!-- Sound FX Toggle -->
    <button onclick="AudioEngine.toggleMute()" id="btnSfx" class="encarta-btn px-2.5 py-1.5 rounded text-xs font-mono font-bold">
      🔊 SFX: ON
    </button>
  </div>
</header>

<!-- Main Navigation Bar -->
<nav class="bg-[#041418] border-b-2 border-[#164e5b] px-4 py-2 flex flex-wrap items-center justify-between gap-2 shadow-lg sticky top-0 z-30">
  <div class="flex flex-wrap items-center gap-1.5">
    <button onclick="switchTab('encyclopedia')" id="tab-encyclopedia" class="encarta-btn active px-3.5 py-1.5 rounded text-xs font-bold flex items-center space-x-1.5">
      <span>📖</span> <span>The Encyclopedia</span>
    </button>
    <button onclick="switchTab('lab')" id="tab-lab" class="encarta-btn px-3.5 py-1.5 rounded text-xs font-bold flex items-center space-x-1.5">
      <span>🧪</span> <span>Physics Lab</span>
      <span class="bg-cyan-500/20 text-cyan-300 text-[10px] px-1.5 rounded border border-cyan-500/40">5 Sims</span>
    </button>
    <button onclick="switchTab('blueprints')" id="tab-blueprints" class="encarta-btn px-3.5 py-1.5 rounded text-xs font-bold flex items-center space-x-1.5">
      <span>📐</span> <span>Blueprints</span>
      <span class="bg-amber-500/20 text-amber-300 text-[10px] px-1.5 rounded border border-amber-500/40" id="blueprintsTabCount">50 Builds</span>
    </button>
    <button onclick="switchTab('xray')" id="tab-xray" class="encarta-btn px-3.5 py-1.5 rounded text-xs font-bold flex items-center space-x-1.5">
      <span>🔬</span> <span>Appliance X-Ray</span>
      <span class="bg-purple-500/20 text-purple-300 text-[10px] px-1.5 rounded border border-purple-500/40">4 Layers</span>
    </button>
    <button onclick="switchTab('mindmaze')" id="tab-mindmaze" class="encarta-btn px-3.5 py-1.5 rounded text-xs font-bold flex items-center space-x-1.5">
      <span>🧠</span> <span>MindMaze '95</span>
      <span class="bg-red-500/20 text-red-300 text-[10px] px-1.5 rounded border border-red-500/40">Dungeon</span>
    </button>
    <button onclick="switchTab('atlas')" id="tab-atlas" class="encarta-btn px-3.5 py-1.5 rounded text-xs font-bold flex items-center space-x-1.5">
      <span>🏛️</span> <span>Scrap Atlas</span>
      <span class="text-[10px] text-slate-300 font-mono" id="atlasTabCount">88 Donors</span>
    </button>
  </div>

  <!-- Pinpointer Omnisearch -->
  <div class="flex-1 flex justify-end min-w-[240px] max-w-sm">
    <div class="relative w-full">
      <input type="text" id="omniSearch" onkeyup="handleSearch(this.value)" placeholder="🔎 Pinpointer Omnisearch..." 
             class="w-full bg-[#020a0d] border border-[#2a7c8e] rounded px-3 py-1.5 text-xs text-slate-100 placeholder-slate-400 focus:outline-none focus:border-amber-400 font-mono shadow-inner">
      <div id="searchDropdown" class="absolute left-0 right-0 top-9 bg-[#04161b] border border-[#2a7c8e] rounded shadow-2xl z-50 max-h-80 overflow-y-auto hidden"></div>
    </div>
  </div>
</nav>

<!-- Main Experience Container -->
<main class="flex-1 max-w-[1700px] w-full mx-auto p-3 md:p-5">

  <!-- ================= TAB 1: THE FULL ENCYCLOPEDIA ================= -->
  <section id="view-encyclopedia" class="space-y-4">
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-5 items-start">
      
      <!-- LEFT SIDEBAR: THE OVERHAULED VOLUME & CHAPTER ATLAS (4 Cols) -->
      <aside class="encarta-window rounded-lg overflow-hidden lg:col-span-4 max-h-[88vh] flex flex-col shadow-2xl">
        <div class="rivet tl"></div>
        <div class="rivet tr"></div>
        <div class="window-header px-4 py-2.5 text-xs flex justify-between items-center">
          <div class="flex items-center space-x-2">
            <span class="text-amber-400">🏛️</span>
            <span class="font-serif tracking-wide">VOLUME &amp; CHAPTER ATLAS</span>
          </div>
          <span class="font-mono text-[10px] text-emerald-400 font-bold bg-emerald-950/80 px-2 py-0.5 rounded border border-emerald-700/60">36 ARTICLES</span>
        </div>

        <!-- Search & Quick Toggles Strip -->
        <div class="p-2.5 border-b border-[#164e5b] bg-[#031115] space-y-2">
          <input type="text" id="atlasSearchInput" oninput="filterAtlasTree(this.value)" placeholder="🔎 Filter 36 chapters, topics &amp; donors..." 
                 class="w-full bg-[#02080a] border border-[#1a5b6a] rounded px-3 py-1.5 text-xs text-slate-100 placeholder-slate-400 focus:outline-none focus:border-amber-400 font-mono shadow-inner">
          <div class="flex items-center justify-between text-[10px] font-mono">
            <button onclick="expandAllVolumes()" class="text-cyan-400 hover:text-amber-300 font-semibold">[+ Expand All]</button>
            <button onclick="collapseAllVolumes()" class="text-cyan-400 hover:text-amber-300 font-semibold">[- Collapse All]</button>
            <span id="atlasMatchCount" class="text-slate-400">15 Volumes</span>
          </div>
        </div>

        <!-- Volume Cards Container -->
        <div class="p-2.5 overflow-y-auto flex-1 space-y-2.5" id="atlasTreeContainer">
          <!-- Dynamically populated with rich volume and chapter cards -->
        </div>
      </aside>

      <!-- RIGHT MAIN AREA: UNABRIDGED READING ROOM (8 Cols) -->
      <article class="encarta-window rounded-lg overflow-hidden lg:col-span-8 min-h-[88vh] flex flex-col shadow-2xl">
        <div class="rivet tl"></div>
        <div class="rivet tr"></div>
        <!-- Article Header Plaque -->
        <div class="window-header px-5 py-3 flex flex-wrap items-center justify-between gap-3">
          <div>
            <div class="flex items-center space-x-2">
              <span id="articleCatIcon" class="text-base">⚡</span>
              <span id="articleVolBadge" class="text-[10px] font-mono text-cyan-300 font-bold uppercase tracking-wider">VOL. 00 &bull; FOUNDATIONS</span>
            </div>
            <h2 id="articleHeading" class="text-lg md:text-xl font-black text-amber-300 font-serif leading-tight mt-0.5">Loading Article...</h2>
            <div id="articleSubLabel" class="text-[11px] text-cyan-200/90 font-mono mt-0.5">Technical topic preview loading...</div>
          </div>
          <div class="flex items-center space-x-2">
            <button onclick="SpeechNarrator.speakCurrent()" class="encarta-btn px-3 py-1.5 rounded text-xs flex items-center space-x-1 text-amber-200 font-bold">
              <span>🎙️</span>
              <span>Audio Tour</span>
            </button>
            <button onclick="window.print()" class="encarta-btn px-3 py-1.5 rounded text-xs font-semibold">🖨️ Print Dossier</button>
          </div>
        </div>

        <!-- Article Quick Dossier & Outline Strip -->
        <div class="bg-[#031317] px-5 py-2.5 border-b border-[#164e5b] flex flex-wrap items-center justify-between text-xs font-mono text-slate-300 gap-2">
          <div class="flex items-center space-x-4">
            <span>⏱️ <span id="articleReadTime" class="text-cyan-300 font-bold">5 min</span> read</span>
            <span>📝 <span id="articleWords" class="text-cyan-300 font-bold">1,200</span> words</span>
            <span id="articleHazardFlag" class="text-red-400 font-bold hidden bg-red-950/80 px-2 py-0.5 rounded border border-red-700/60">⚠️ HIGH HAZARD</span>
          </div>
          <div class="flex items-center space-x-2 text-[11px]">
            <span class="text-slate-400">Jump to section:</span>
            <select id="sectionSelect" onchange="jumpToSection(this.value)" class="bg-[#061e25] border border-[#1b6170] rounded px-2.5 py-1 text-slate-200 focus:outline-none focus:border-amber-400">
              <!-- Section options populated dynamically -->
            </select>
          </div>
        </div>

        <!-- Full Unabridged Text Body -->
        <div class="p-6 md:p-8 overflow-y-auto flex-1 article-body text-slate-200 max-w-none" id="articleContent">
          <!-- Full parsed HTML populated here -->
        </div>

        <!-- Article Footer Controls (Next / Prev) -->
        <div class="bg-[#020b0e] border-t border-[#164e5b] px-5 py-3 flex justify-between items-center text-xs">
          <button id="btnPrevArticle" onclick="navigateArticle(-1)" class="encarta-btn px-4 py-1.5 rounded flex items-center space-x-1.5 font-bold">
            <span>&larr;</span> <span>Previous Chapter</span>
          </button>
          <span id="articleCounter" class="font-mono text-slate-400 font-semibold">Chapter 1 of 36</span>
          <button id="btnNextArticle" onclick="navigateArticle(1)" class="encarta-btn px-4 py-1.5 rounded flex items-center space-x-1.5 font-bold">
            <span>Next Chapter</span> <span>&rarr;</span>
          </button>
        </div>
      </article>

    </div>
  </section>

  <!-- ================= TAB 2: PHYSICS & KINEMATICS LAB ================= -->
  <section id="view-lab" class="space-y-5 hidden">
    <!-- Sub-tab selector -->
    <div class="flex flex-wrap gap-2 border-b border-[#164e5b] pb-2">
      <button onclick="switchLabSim('balancer')" id="btn-sim-balancer" class="encarta-btn active px-3.5 py-1.5 rounded text-xs font-bold">1. LeBlanc Balancer</button>
      <button onclick="switchLabSim('sparks')" id="btn-sim-sparks" class="encarta-btn px-3.5 py-1.5 rounded text-xs font-bold">2. Spark Metallurgy</button>
      <button onclick="switchLabSim('wizard')" id="btn-sim-wizard" class="encarta-btn px-3.5 py-1.5 rounded text-xs font-bold">3. Simpson 260 Wire Wizard</button>
      <button onclick="switchLabSim('geneva')" id="btn-sim-geneva" class="encarta-btn px-3.5 py-1.5 rounded text-xs font-bold">4. Geneva &amp; Scotch Yoke</button>
      <button onclick="switchLabSim('spotwelder')" id="btn-sim-spotwelder" class="encarta-btn px-3.5 py-1.5 rounded text-xs font-bold">5. Spot Welder CRT Scope</button>
    </div>

    <!-- SIM 1: LeBlanc Ball Balancer with Seismograph -->
    <div id="sim-balancer" class="encarta-window rounded-lg overflow-hidden">
      <div class="rivet tl"></div>
      <div class="rivet tr"></div>
      <div class="window-header px-4 py-2.5 flex items-center justify-between text-xs">
        <span class="flex items-center space-x-2">
          <span>🔄</span>
          <span class="font-serif">PHYSICS SIMULATOR: LeBlanc Supercritical Dynamic Balancer (Rotordynamics)</span>
        </span>
        <span class="font-mono text-emerald-400 font-bold">60 FPS REAL-TIME ROTORDYNAMICS</span>
      </div>
      <div class="p-5 grid grid-cols-1 lg:grid-cols-3 gap-6">
        <!-- Canvas Visualizer with Seismograph -->
        <div class="lg:col-span-2 flex flex-col items-center justify-center bg-[#02080a] border border-[#164e5b] rounded p-4 relative shadow-inner">
          <canvas id="balancerCanvas" width="500" height="350" class="max-w-full"></canvas>
          <div class="w-full mt-3 bg-[#030e11] border border-[#164e5b] rounded p-2.5">
            <div class="flex justify-between items-center text-[10px] font-mono text-slate-400 mb-1">
              <span>REAL-TIME SEISMOGRAPH VIBRATION TRACE (mm P-P)</span>
              <span id="seismoValue" class="text-red-400 font-bold">12.4 mm P-P</span>
            </div>
            <canvas id="seismoCanvas" width="470" height="45" class="w-full rounded bg-[#010608]"></canvas>
          </div>
          <div id="balancerAlert" class="mt-2 text-xs font-mono px-3 py-1.5 rounded border w-full text-center"></div>
        </div>
        <!-- Controls & Physics Readout -->
        <div class="space-y-4">
          <div class="bg-[#04161b] p-4 rounded border border-[#1b6170] space-y-3">
            <h4 class="text-xs font-bold text-amber-300 uppercase tracking-wider font-serif">Rotor Speed Controller</h4>
            <div>
              <div class="flex justify-between text-xs mb-1 font-mono">
                <span>Rotor Speed:</span>
                <span id="rpmDisplay" class="text-cyan-300 font-bold">600 RPM</span>
              </div>
              <input type="range" id="rpmSlider" min="100" max="1800" step="50" value="600" oninput="setBalancerRPM(this.value)" class="w-full accent-amber-400">
              <div class="flex justify-between text-[10px] text-slate-400 font-mono mt-1">
                <span>100 (Subcritical)</span>
                <span class="text-red-400 font-bold">450 (Resonance)</span>
                <span>1800 (Supercritical)</span>
              </div>
            </div>
            <div class="pt-2 border-t border-[#164e5b]">
              <button onclick="toggleUnbalance()" id="btnUnbalance" class="encarta-btn active w-full py-2 rounded text-xs font-bold">
                Eccentric Slug: ATTACHED
              </button>
            </div>
          </div>
          <div class="bg-[#04161b] p-4 rounded border border-[#1b6170] text-xs space-y-2">
            <h4 class="font-bold text-cyan-300 uppercase font-serif">Salvage Exploitation:</h4>
            <p class="text-slate-300 text-[11px] leading-relaxed">
              Harvest the hollow welded toroidal balancer ring from scrap front-load washing machines (LG, Samsung, Whirlpool). Mount directly onto high-speed woodworking spindle arbors, 2x72 belt grinder contact wheels, or custom alternator turbines. It automatically achieves sub-micron balance without knife-edge balancing arbors!
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- SIM 2: Angle Grinder Spark Metallurgy -->
    <div id="sim-sparks" class="encarta-window rounded-lg overflow-hidden hidden">
      <div class="rivet tl"></div>
      <div class="rivet tr"></div>
      <div class="window-header px-4 py-2.5 flex items-center justify-between text-xs">
        <span class="flex items-center space-x-2">
          <span>✨</span>
          <span class="font-serif">PHYSICS SIMULATOR: Scrap Steel Spark Testing Chamber (Bench Metallurgy)</span>
        </span>
        <span class="font-mono text-amber-400 font-bold">GRINDER: 10,000 RPM &bull; MULTI-STAGE DETONATIONS</span>
      </div>
      <div class="p-5 grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div class="lg:col-span-2 flex flex-col items-center justify-center bg-[#02080a] border border-[#164e5b] rounded p-4 relative shadow-inner">
          <canvas id="sparksCanvas" width="520" height="350" class="max-w-full"></canvas>
          <div class="w-full flex justify-between items-center mt-3 pt-2 border-t border-[#164e5b]">
            <button id="btnGrind" onmousedown="startGrinding()" onmouseup="stopGrinding()" onmouseleave="stopGrinding()" 
                    class="encarta-btn px-6 py-2 rounded text-xs font-bold text-amber-300 border-amber-500/50 flex items-center space-x-2 shadow-lg">
              <span>⚡</span>
              <span>HOLD TO CONTACT WORKPIECE</span>
            </button>
            <div id="sparkStatus" class="text-xs font-mono text-slate-300">Grinder idling at 10,000 RPM. Press and hold button.</div>
          </div>
        </div>
        <div class="space-y-4">
          <div class="bg-[#04161b] p-4 rounded border border-[#1b6170] space-y-2">
            <h4 class="text-xs font-bold text-amber-300 uppercase tracking-wider font-serif">Select Metal Specimen:</h4>
            <div class="space-y-1.5">
              <button onclick="setMetal('1095')" id="btnMetal_1095" class="encarta-btn active w-full text-left px-3 py-1.5 rounded text-xs metal-btn font-semibold">1. High-Carbon 1095 (Spring Steel)</button>
              <button onclick="setMetal('1018')" id="btnMetal_1018" class="encarta-btn w-full text-left px-3 py-1.5 rounded text-xs metal-btn font-semibold">2. Low-Carbon 1018 (Mild Steel)</button>
              <button onclick="setMetal('castiron')" id="btnMetal_castiron" class="encarta-btn w-full text-left px-3 py-1.5 rounded text-xs metal-btn font-semibold">3. Cast Iron (Brake Rotor / Block)</button>
              <button onclick="setMetal('hss')" id="btnMetal_hss" class="encarta-btn w-full text-left px-3 py-1.5 rounded text-xs metal-btn font-semibold">4. M2 High-Speed Tool Steel (Drill)</button>
              <button onclick="setMetal('titanium')" id="btnMetal_titanium" class="encarta-btn w-full text-left px-3 py-1.5 rounded text-xs metal-btn font-semibold">5. Titanium Grade 5 (Aerospace)</button>
            </div>
          </div>
          <div class="bg-[#04161b] p-4 rounded border border-[#1b6170] space-y-2">
            <h4 id="metalTitle" class="text-xs font-bold text-cyan-300 font-serif">High-Carbon 1095 Spring Steel</h4>
            <p id="metalDesc" class="text-[11px] text-slate-300 leading-relaxed">
              Dense golden shower with explosive multi-branched carbon starbursts (chrysanthemums). Carbon oxidizes into CO micro-explosions in mid-flight.
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- SIM 3: Wire Wizard with Simpson 260 Analog Multimeter -->
    <div id="sim-wizard" class="encarta-window rounded-lg overflow-hidden hidden">
      <div class="rivet tl"></div>
      <div class="rivet tr"></div>
      <div class="window-header px-4 py-2.5 flex items-center justify-between text-xs">
        <span class="flex items-center space-x-2">
          <span>⚡</span>
          <span class="font-serif">DIAGNOSTIC WIZARD: Simpson 260 / Triplett Analog Multimeter Motor Triage</span>
        </span>
        <span class="font-mono text-cyan-300 font-bold">DAMPED INERTIAL NEEDLE PHYSICS</span>
      </div>
      <div class="p-5 space-y-5">
        <!-- Wire Count Selector Buttons -->
        <div class="flex flex-wrap gap-2">
          <button onclick="testWireCount(2)" id="btnWire_2" class="encarta-btn px-4 py-2 rounded text-xs font-bold wire-btn">2-Wire (DC / Universal)</button>
          <button onclick="testWireCount(3)" id="btnWire_3" class="encarta-btn active px-4 py-2 rounded text-xs font-bold wire-btn">3-Wire (BLDC / PMSM)</button>
          <button onclick="testWireCount(4)" id="btnWire_4" class="encarta-btn px-4 py-2 rounded text-xs font-bold wire-btn">4-Wire (Bipolar Stepper)</button>
          <button onclick="testWireCount(5)" id="btnWire_5" class="encarta-btn px-4 py-2 rounded text-xs font-bold wire-btn">5-Wire (Unipolar Stepper)</button>
          <button onclick="testWireCount(6)" id="btnWire_6" class="encarta-btn px-4 py-2 rounded text-xs font-bold wire-btn">6-Wire (Universal Stepper)</button>
          <button onclick="testWireCount(8)" id="btnWire_8" class="encarta-btn px-4 py-2 rounded text-xs font-bold wire-btn">8-Wire (Switched Reluctance)</button>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 items-start">
          <!-- Simpson 260 Analog Multimeter Display -->
          <div class="bg-[#02080a] p-4 rounded border border-[#164e5b] flex flex-col items-center shadow-inner">
            <div class="text-[10px] font-mono text-amber-300 uppercase tracking-wider mb-2 font-bold">SIMPSON 260 ANALOG VOM</div>
            <canvas id="dmmCanvas" width="240" height="150" class="rounded bg-white"></canvas>
            <div class="mt-3 w-full bg-[#031317] border border-[#1b6170] rounded px-3 py-1.5 flex justify-between items-center font-mono text-xs">
              <span class="text-slate-400">DIGITAL DMM:</span>
              <span id="dmmReadout" class="text-cyan-300 font-bold text-sm">0.8 &Omega;</span>
            </div>
          </div>

          <!-- Diagnostic Results Card -->
          <div class="md:col-span-2 bg-[#04161b] p-5 rounded border border-[#1b6170] space-y-4">
            <div>
              <h3 id="wizardMotorTitle" class="text-sm font-bold text-amber-300 font-serif">3-Wire Motor Architecture (3-Phase BLDC / PMSM)</h3>
            </div>
            <div>
              <div class="text-[11px] font-mono uppercase text-slate-400 font-bold mb-1">Step-by-Step Bench Test:</div>
              <div id="wizardSteps" class="bg-[#020b0e] p-3 rounded border border-[#164e5b]"></div>
            </div>
            <div>
              <div class="text-[11px] font-mono uppercase text-slate-400 font-bold mb-1">Diagnostic Verdict:</div>
              <div id="wizardDiagnosis" class="text-xs text-slate-200 leading-relaxed"></div>
            </div>
            <div class="pt-2 border-t border-[#164e5b] flex items-center justify-between text-xs font-mono">
              <span class="text-slate-400">Recommended Controller:</span>
              <span id="wizardController" class="text-emerald-400 font-bold">VESC 6.0 or ODrive Robotics Controller</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SIM 4: Geneva Mechanism & Scotch Yoke -->
    <div id="sim-geneva" class="encarta-window rounded-lg overflow-hidden hidden">
      <div class="rivet tl"></div>
      <div class="rivet tr"></div>
      <div class="window-header px-4 py-2.5 flex items-center justify-between text-xs">
        <span class="flex items-center space-x-2">
          <span>⚙️</span>
          <span class="font-serif">KINEMATICS LAB: Maltese Cross Geneva Indexing Drive &amp; Scotch Yoke CAD</span>
        </span>
        <span class="font-mono text-cyan-300 font-bold">PRECISION MECHANICAL CAD SIMULATION</span>
      </div>
      <div class="p-5 grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div class="lg:col-span-2 flex flex-col items-center justify-center bg-[#02080a] border border-[#164e5b] rounded p-4 shadow-inner">
          <canvas id="genevaCanvas" width="480" height="340" class="max-w-full"></canvas>
        </div>
        <div class="space-y-4">
          <div class="bg-[#04161b] p-4 rounded border border-[#1b6170] space-y-3">
            <h4 class="text-xs font-bold text-amber-300 uppercase tracking-wider font-serif">Kinematic Mechanism:</h4>
            <div class="flex gap-2">
              <button onclick="setKinematicMode('geneva')" id="btnModeGeneva" class="encarta-btn active flex-1 py-1.5 rounded text-xs font-bold">Geneva 4-Slot</button>
              <button onclick="setKinematicMode('scotchyoke')" id="btnModeYoke" class="encarta-btn flex-1 py-1.5 rounded text-xs font-bold">Scotch Yoke</button>
            </div>
          </div>
          <div class="bg-[#04161b] p-4 rounded border border-[#1b6170] space-y-2">
            <h4 id="kinematicTitle" class="text-xs font-bold text-cyan-300 font-serif">Maltese Cross Geneva Drive (Intermittent Motion)</h4>
            <p id="kinematicDesc" class="text-[11px] text-slate-300 leading-relaxed">
              Converts continuous rotary motion into precise 90-degree dwell-locked indexing steps. Salvaged from movie projectors, rotary assembly indexing tables, and analog watch escapements.
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- SIM 5: CD Spot Welder CRT Scope -->
    <div id="sim-spotwelder" class="encarta-window rounded-lg overflow-hidden hidden">
      <div class="rivet tl"></div>
      <div class="rivet tr"></div>
      <div class="window-header px-4 py-2.5 flex items-center justify-between text-xs">
        <span class="flex items-center space-x-2">
          <span>⚡</span>
          <span class="font-serif">PULSED POWER LAB: Capacitive Discharge (CD) Spot Welder CRT Oscilloscope</span>
        </span>
        <span class="font-mono text-emerald-400 font-bold">TEKTRONIX PHOSPHOR CRT EMULATION</span>
      </div>
      <div class="p-5 grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div class="lg:col-span-2 flex flex-col items-center justify-center bg-[#02080a] border border-[#164e5b] rounded p-4 shadow-inner">
          <canvas id="pulseCanvas" width="500" height="300" class="max-w-full rounded bg-[#020b08]"></canvas>
          <div class="w-full grid grid-cols-3 gap-2 mt-4 text-center font-mono text-xs">
            <div class="bg-[#04161b] p-2 rounded border border-[#164e5b]">
              <span class="text-slate-400 text-[10px] block">STORED ENERGY:</span>
              <span id="spotJoules" class="text-amber-300 font-bold text-sm">242.0 J</span>
            </div>
            <div class="bg-[#04161b] p-2 rounded border border-[#164e5b]">
              <span class="text-slate-400 text-[10px] block">PEAK SURGE CURRENT:</span>
              <span id="spotCurrent" class="text-red-400 font-bold text-sm">5,500 A</span>
            </div>
            <div class="bg-[#04161b] p-2 rounded border border-[#164e5b]">
              <span class="text-slate-400 text-[10px] block">PULSE DURATION:</span>
              <span id="spotPulse" class="text-cyan-300 font-bold text-sm">3.0 ms</span>
            </div>
          </div>
        </div>
        <div class="space-y-4">
          <div class="bg-[#04161b] p-4 rounded border border-[#1b6170] space-y-3">
            <h4 class="text-xs font-bold text-amber-300 uppercase tracking-wider font-serif">Bank Parameters:</h4>
            <div>
              <div class="flex justify-between text-xs mb-1 font-mono">
                <span>Capacitance (F):</span>
                <span id="valCap" class="text-cyan-300 font-bold">1.00 F</span>
              </div>
              <input type="range" id="sliderCap" min="0.1" max="3.0" step="0.1" value="1.0" oninput="updateSpotWelder()" class="w-full accent-cyan-400">
            </div>
            <div>
              <div class="flex justify-between text-xs mb-1 font-mono">
                <span>Bank Voltage (V):</span>
                <span id="valVolts" class="text-amber-300 font-bold">22 V</span>
              </div>
              <input type="range" id="sliderVolts" min="10" max="35" step="1" value="22" oninput="updateSpotWelder()" class="w-full accent-amber-400">
            </div>
          </div>
          <div class="bg-[#04161b] p-4 rounded border border-[#1b6170] text-xs space-y-2">
            <h4 class="font-bold text-red-400 uppercase font-serif">HAZ Safety Boundary:</h4>
            <p class="text-slate-300 text-[11px] leading-relaxed">
              Unlike rewound AC Microwave Oven Transformers (MOTs) that dump continuous 60Hz current and burn battery can walls, Capacitive Discharge delivers sub-5ms pulse energy. Heat is strictly confined to the nickel-steel boundary layer without heating the volatile lithium electrolyte!
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ================= TAB 3: BLUEPRINTS & COOKBOOKS ================= -->
  <section id="view-blueprints" class="space-y-6 hidden">
    <div class="encarta-window rounded-lg p-5 flex flex-wrap items-center justify-between gap-4">
      <div>
        <h2 class="text-lg font-black text-amber-300 font-serif flex items-center space-x-2">
          <span>📐</span>
          <span><span id="blueprintsHeaderCount">50</span> Production Engineering Blueprints</span>
        </h2>
        <p class="text-xs text-slate-300">Complete fabrication dossiers: Schematics, Bill of Materials, Wiring Pinouts &amp; Build SOPs.</p>
      </div>
      <div class="flex flex-wrap gap-1.5" id="blueprintFilters">
        <button onclick="filterBlueprints('all')" class="encarta-btn active px-3 py-1 rounded text-xs font-semibold bp-filter-btn" id="bpAllFilterBtn">All 50 Builds</button>
        <button onclick="filterBlueprints('power')" class="encarta-btn px-3 py-1 rounded text-xs font-semibold bp-filter-btn">Power &amp; Energy</button>
        <button onclick="filterBlueprints('machine')" class="encarta-btn px-3 py-1 rounded text-xs font-semibold bp-filter-btn">Machine Tools</button>
        <button onclick="filterBlueprints('optics')" class="encarta-btn px-3 py-1 rounded text-xs font-semibold bp-filter-btn">Optics &amp; Micro</button>
        <button onclick="filterBlueprints('mobility')" class="encarta-btn px-3 py-1 rounded text-xs font-semibold bp-filter-btn">Mobility &amp; Robotics</button>
      </div>
    </div>

    <!-- Blueprints Card Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5" id="blueprintsGrid">
      <!-- Dynamically Populated -->
    </div>

    <!-- Blueprint Modal Dossier -->
    <div id="blueprintModal" class="fixed inset-0 bg-black/80 z-50 flex items-center justify-center p-4 hidden backdrop-blur-sm">
      <div class="encarta-window rounded-lg max-w-3xl w-full max-h-[90vh] flex flex-col shadow-2xl overflow-hidden border-2 border-amber-400">
        <div class="window-header px-5 py-3 flex justify-between items-center">
          <span id="bpModalTitle" class="font-serif text-sm md:text-base font-bold text-amber-300">Blueprint Dossier</span>
          <button onclick="closeBlueprintModal()" class="encarta-btn px-2.5 py-1 rounded text-xs font-bold text-red-400">&times; CLOSE</button>
        </div>
        <div class="p-6 overflow-y-auto space-y-5 text-xs text-slate-200" id="bpModalBody">
          <!-- Populated dynamically -->
        </div>
      </div>
    </div>
  </section>

  <!-- ================= TAB 4: APPLIANCE X-RAY CUTAWAY ================= -->
  <section id="view-xray" class="space-y-6 hidden">
    <div class="encarta-window rounded-lg p-5 flex flex-wrap items-center justify-between gap-4">
      <div>
        <h2 class="text-lg font-black text-amber-300 font-serif flex items-center space-x-2">
          <span>🔬</span>
          <span>Appliance X-Ray Cutaway Engine</span>
        </h2>
        <p class="text-xs text-slate-300">Interactive 4-layer inspection peeler revealing hidden electromechanical mechanisms and lethal hazard shunts.</p>
      </div>
      <div class="flex gap-2">
        <button onclick="loadXRay('microwave')" id="btnXrayMicrowave" class="encarta-btn active px-3.5 py-1.5 rounded text-xs font-bold xray-model-btn">Microwave Oven</button>
        <button onclick="loadXRay('washer')" id="btnXrayWasher" class="encarta-btn px-3.5 py-1.5 rounded text-xs font-bold xray-model-btn">Direct-Drive Washer</button>
        <button onclick="loadXRay('alternator')" id="btnXrayAlternator" class="encarta-btn px-3.5 py-1.5 rounded text-xs font-bold xray-model-btn">Car Alternator</button>
      </div>
    </div>

    <!-- X-Ray Display -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <div class="lg:col-span-2 encarta-window rounded-lg p-5 flex items-center justify-center bg-[#02080a] relative min-h-[420px] shadow-inner" id="xrayCanvasContainer">
        <!-- SVG Rendered Here -->
      </div>
      <div class="space-y-4">
        <!-- Layer Peel Slider -->
        <div class="bg-[#04161b] p-4 rounded border border-[#1b6170] space-y-3">
          <div class="flex justify-between items-center text-xs font-mono font-bold">
            <span class="text-amber-300 uppercase font-serif">Layer Peel Depth:</span>
            <span id="xrayLayerName" class="text-cyan-300">Layer 1: Structural Chassis</span>
          </div>
          <input type="range" id="xrayLayerSlider" min="0" max="3" step="1" value="0" oninput="setXRayLayer(this.value)" class="w-full accent-cyan-400">
          <div class="flex justify-between text-[10px] font-mono text-slate-400">
            <span>Chassis</span>
            <span>Motors</span>
            <span>Electrical</span>
            <span class="text-red-400 font-bold">Hazards</span>
          </div>
        </div>

        <!-- Hotspot Inspection Card -->
        <div id="xrayHotspotCard" class="bg-[#04161b] p-4 rounded border border-[#1b6170] space-y-2">
          <h4 id="hotspotTitle" class="text-xs font-bold text-amber-300 font-serif">Select an X-Ray Hotspot</h4>
          <p id="hotspotDesc" class="text-[11px] text-slate-300 leading-relaxed">
            Click any pulsing radar ping on the cutaway diagram to inspect its electromechanical specifications and harvest procedure.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- ================= TAB 5: MINDMAZE '95 ISOMETRIC DUNGEON ================= -->
  <section id="view-mindmaze" class="space-y-6 hidden">
    <div class="encarta-window rounded-lg overflow-hidden">
      <div class="rivet tl"></div>
      <div class="rivet tr"></div>
      <div class="window-header px-5 py-3 flex justify-between items-center">
        <div class="flex items-center space-x-2">
          <span>🧠</span>
          <span class="font-serif">MindMaze '95: The Scrapper's Dungeon</span>
        </div>
        <span class="font-mono text-xs text-amber-300 font-bold">2.5D ISOMETRIC DUNGEON CRAWLER</span>
      </div>

      <div class="p-6 space-y-6">
        <!-- 2.5D Isometric Canvas Display -->
        <div class="bg-[#02080a] border border-[#164e5b] rounded-lg p-3 flex flex-col items-center relative overflow-hidden shadow-inner">
          <canvas id="mazeCanvas" width="580" height="280" class="max-w-full"></canvas>
          <div class="absolute top-4 left-4 bg-[#04161b]/90 border border-[#1b6170] px-3 py-1.5 rounded text-[11px] font-mono text-cyan-300 shadow">
            USE ARROW BUTTONS TO MOVE &bull; APPROACH RUNIC GATES TO SOLVE SALVAGE QUIZ
          </div>
        </div>

        <!-- Directional D-Pad Controls -->
        <div class="flex flex-col items-center space-y-2">
          <button onclick="movePlayer(0, -1)" class="encarta-btn px-6 py-2 rounded font-bold text-xs shadow">&uarr; NORTH</button>
          <div class="flex space-x-3">
            <button onclick="movePlayer(-1, 0)" class="encarta-btn px-6 py-2 rounded font-bold text-xs shadow">&larr; WEST</button>
            <button onclick="movePlayer(1, 0)" class="encarta-btn px-6 py-2 rounded font-bold text-xs shadow">EAST &rarr;</button>
          </div>
          <button onclick="movePlayer(0, 1)" class="encarta-btn px-6 py-2 rounded font-bold text-xs shadow">&darr; SOUTH</button>
        </div>

        <!-- Doorway Quiz Alert Box -->
        <div id="mazeDoorwayAlert" class="bg-[#04161b] border-2 border-amber-400/80 rounded-lg p-5 space-y-4 hidden shadow-2xl">
          <div class="flex items-center space-x-2 text-amber-300 font-serif font-bold text-sm">
            <span>🗝️</span>
            <span>RUNIC HAZARD GATE ENCOUNTERED!</span>
          </div>
          <p id="quizQuestion" class="text-xs text-slate-100 font-mono leading-relaxed">Loading question...</p>
          <div id="quizChoices" class="grid grid-cols-1 md:grid-cols-2 gap-2.5">
            <!-- Populated dynamically -->
          </div>
        </div>

        <!-- Salvage Loot Inventory Pouch -->
        <div class="bg-[#04161b] border border-[#164e5b] rounded-lg p-4 space-y-2">
          <div class="flex justify-between items-center text-xs font-mono text-amber-300 font-bold font-serif">
            <span>🎒 SALVAGE INVENTORY POUCH:</span>
            <span class="text-emerald-400">MARKET VALUE TELEMETRY</span>
          </div>
          <div id="playerInventoryList" class="flex flex-wrap gap-2">
            <!-- Populated dynamically -->
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ================= TAB 6: SCRAP ATLAS (88 DONORS MATRIX) ================= -->
  <section id="view-atlas" class="space-y-6 hidden">
    <div class="encarta-window rounded-lg overflow-hidden p-5 flex flex-wrap items-center justify-between gap-4">
      <div>
        <h2 class="text-lg font-black text-amber-300 font-serif flex items-center space-x-2">
          <span>🏛️</span>
          <span>The Grand Master Salvage Matrix (<span id="atlasHeaderCount">88</span> Donor Streams)</span>
        </h2>
        <p class="text-xs text-slate-300">Complete urban mining catalog across all domestic, commercial, automotive, and industrial appliances.</p>
      </div>
      <div class="flex flex-wrap gap-1.5" id="atlasFilterPills">
        <!-- Category filter buttons populated dynamically -->
      </div>
    </div>

    <!-- Donors Matrix Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5" id="donorsGrid">
      <!-- Populated dynamically -->
    </div>
  </section>

</main>

<!-- Encyclopedic Footer -->
<footer class="bg-[#02090b] border-t-2 border-[#164e5b] py-4 px-6 text-center text-xs text-slate-400 font-mono">
  <p>ENCARTA '95 : ELECTROMECHANICA &bull; Published by The Advanced Electromechanical Salvage Guild &bull; Offline Compliant &bull; Zero CDN Dependencies</p>
</footer>
"""
