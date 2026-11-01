"""
ENCARTA '95 : ELECTROMECHANICA - Core Application Logic Module
Contains:
- Procedural Web Audio synthesizer
- 16-Band real-time VU audio visualizer
- Web Speech API Audio Tour voice narrator
- The Overhauled Volume & Chapter Atlas with labels, sub-labels, icons, and real-time filtering
- Unabridged reading room controller with section jump
- Pinpointer Omnisearch engine
- Blueprints grid & modal manager
- Appliance X-Ray cutaway engine
- 27-Donor Scrap Atlas matrix
"""

ENCARTA_CORE_JS = r"""
// ================= PROCEDURAL WEB AUDIO SYNTHESIZER =================
const AudioEngine = {
  ctx: null,
  muted: false,
  grinderNode: null,
  grinderGain: null,
  init() {
    if (!this.ctx) {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      this.ctx = new AudioCtx();
    }
    if (this.ctx.state === 'suspended') {
      this.ctx.resume();
    }
  },
  toggleMute() {
    this.muted = !this.muted;
    const btn = document.getElementById('btnSfx');
    if (btn) btn.innerText = this.muted ? '🔇 SFX: OFF' : '🔊 SFX: ON';
  },
  click() {
    if (this.muted) return;
    this.init();
    VU.trigger();
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'triangle';
    osc.frequency.setValueAtTime(800, this.ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(120, this.ctx.currentTime + 0.04);
    gain.gain.setValueAtTime(0.18, this.ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, this.ctx.currentTime + 0.04);
    osc.connect(gain);
    gain.connect(this.ctx.destination);
    osc.start();
    osc.stop(this.ctx.currentTime + 0.04);
  },
  buzz() {
    if (this.muted) return;
    this.init();
    VU.trigger();
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'sawtooth';
    osc.frequency.setValueAtTime(110, this.ctx.currentTime);
    gain.gain.setValueAtTime(0.22, this.ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, this.ctx.currentTime + 0.22);
    osc.connect(gain);
    gain.connect(this.ctx.destination);
    osc.start();
    osc.stop(this.ctx.currentTime + 0.22);
  },
  victory() {
    if (this.muted) return;
    this.init();
    VU.trigger();
    const now = this.ctx.currentTime;
    [440, 554.37, 659.25, 880].forEach((freq, i) => {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(freq, now + i * 0.1);
      gain.gain.setValueAtTime(0.18, now + i * 0.1);
      gain.gain.exponentialRampToValueAtTime(0.01, now + i * 0.1 + 0.35);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start(now + i * 0.1);
      osc.stop(now + i * 0.1 + 0.35);
    });
  },
  grinderScreech(active) {
    if (this.muted) return;
    this.init();
    if (active) {
      if (!this.grinderNode) {
        this.grinderNode = this.ctx.createOscillator();
        this.grinderGain = this.ctx.createGain();
        this.grinderNode.type = 'sawtooth';
        this.grinderNode.frequency.setValueAtTime(1450, this.ctx.currentTime);
        this.grinderGain.gain.setValueAtTime(0.14, this.ctx.currentTime);
        this.grinderNode.connect(this.grinderGain);
        this.grinderGain.connect(this.ctx.destination);
        this.grinderNode.start();
      }
      VU.isActive = true;
    } else {
      if (this.grinderNode) {
        this.grinderGain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.1);
        setTimeout(() => {
          if (this.grinderNode) {
            this.grinderNode.stop();
            this.grinderNode.disconnect();
            this.grinderNode = null;
          }
        }, 110);
      }
      VU.isActive = false;
    }
  }
};

// ================= 16-BAND VU EQUALIZER =================
const VU = {
  canvas: null,
  ctx: null,
  isActive: false,
  levels: new Array(16).fill(2),
  init() {
    this.canvas = document.getElementById('vuCanvas');
    if (!this.canvas) return;
    this.ctx = this.canvas.getContext('2d');
    this.loop();
  },
  trigger() {
    this.isActive = true;
    setTimeout(() => this.isActive = false, 350);
  },
  loop() {
    const ctx = this.ctx;
    const w = this.canvas.width;
    const h = this.canvas.height;
    ctx.clearRect(0, 0, w, h);

    const barW = Math.floor(w / 16) - 1;
    for (let i = 0; i < 16; i++) {
      if (this.isActive) {
        this.levels[i] = Math.min(h - 2, Math.floor(Math.random() * (h - 4) + 4));
      } else {
        this.levels[i] = Math.max(2, this.levels[i] * 0.88);
      }
      const val = this.levels[i];
      // Color gradient based on level (green to yellow to red)
      const grad = ctx.createLinearGradient(0, h, 0, 0);
      grad.addColorStop(0, '#10b981');
      grad.addColorStop(0.65, '#f59e0b');
      grad.addColorStop(1, '#ef4444');
      ctx.fillStyle = grad;
      ctx.fillRect(i * (barW + 1), h - val, barW, val);
    }
    requestAnimationFrame(() => this.loop());
  }
};

// ================= WEB SPEECH API VOICE NARRATOR =================
const SpeechNarrator = {
  synth: window.speechSynthesis,
  isSpeaking: false,
  utterance: null,
  toggle() {
    if (this.isSpeaking) this.stop();
    else this.speakCurrent();
  },
  speakCurrent() {
    if (!this.synth) {
      alert("Speech synthesis is not supported on this browser.");
      return;
    }
    this.synth.cancel();

    const art = ARTICLES[currentArticleIndex];
    const textToSpeak = `${art.title}. Volume: ${art.volTitle}. ${art.summary}`;

    this.utterance = new SpeechSynthesisUtterance(textToSpeak);
    this.utterance.rate = 1.0;
    this.utterance.pitch = 0.95;

    this.utterance.onstart = () => {
      this.isSpeaking = true;
      VU.isActive = true;
      document.getElementById('audioTourIcon').innerText = '⏹️';
      document.getElementById('audioTourLabel').innerText = 'AUDIO: PLAYING';
    };

    this.utterance.onend = () => {
      this.isSpeaking = false;
      VU.isActive = false;
      document.getElementById('audioTourIcon').innerText = '🎙️';
      document.getElementById('audioTourLabel').innerText = 'AUDIO TOUR';
    };

    this.utterance.onerror = () => {
      this.isSpeaking = false;
      VU.isActive = false;
      document.getElementById('audioTourIcon').innerText = '🎙️';
      document.getElementById('audioTourLabel').innerText = 'AUDIO TOUR';
    };

    this.synth.speak(this.utterance);
  },
  stop() {
    if (this.synth) this.synth.cancel();
    this.isSpeaking = false;
    VU.isActive = false;
    document.getElementById('audioTourIcon').innerText = '🎙️';
    document.getElementById('audioTourLabel').innerText = 'AUDIO TOUR';
  }
};

// ================= TAB NAVIGATION =================
function switchTab(tabId) {
  AudioEngine.click();
  document.querySelectorAll('nav button').forEach(b => b.classList.remove('active'));
  const btn = document.getElementById('tab-' + tabId);
  if (btn) btn.classList.add('active');

  ['encyclopedia', 'lab', 'xray', 'blueprints', 'mindmaze', 'atlas'].forEach(t => {
    const el = document.getElementById('view-' + t);
    if (el) el.classList.toggle('hidden', t !== tabId);
  });

  if (tabId === 'lab') startBalancerSim();
  if (tabId === 'xray') loadXRay('microwave');
  if (tabId === 'mindmaze') initMindMaze();
  if (tabId === 'blueprints') initBlueprints();
  if (tabId === 'atlas') initAtlas();
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function switchLabSim(simId) {
  AudioEngine.click();
  document.querySelectorAll('#view-lab .encarta-btn').forEach(b => b.classList.remove('active'));
  const btn = document.getElementById('btn-sim-' + simId);
  if (btn) btn.classList.add('active');

  ['balancer', 'sparks', 'wizard', 'geneva', 'spotwelder'].forEach(s => {
    const el = document.getElementById('sim-' + s);
    if (el) el.classList.toggle('hidden', s !== simId);
  });

  if (simId === 'balancer') startBalancerSim();
  if (simId === 'sparks') initSparkSim();
  if (simId === 'wizard') { initMeterSim(); testWireCount(currentWireCount); }
  if (simId === 'geneva') initGenevaSim();
  if (simId === 'spotwelder') updateSpotWelder();
}

function toggleCRT() {
  AudioEngine.click();
  document.getElementById('crtOverlay').classList.toggle('crt-off');
}

// ================= TAB 1: THE OVERHAULED VOLUME & CHAPTER ATLAS =================
let currentArticleIndex = 0;

function initEncyclopediaTree() {
  const container = document.getElementById('atlasTreeContainer');
  if (!container) return;
  container.innerHTML = '';

  VOL_TREE.forEach((vol, vIdx) => {
    const volId = 'volGroup_' + vIdx;
    let chapsHtml = '';

    vol.articles.forEach(art => {
      chapsHtml += `
        <div onclick="loadArticleById('${art.id}')" id="treeItem_${art.id}" 
             class="chapter-card p-2 rounded cursor-pointer text-xs select-none relative group">
          <div class="flex items-start justify-between gap-1 mb-1">
            <span class="px-1.5 py-0.5 rounded font-mono text-[9px] font-bold text-cyan-300 bg-cyan-950/80 border border-cyan-800/80">
              ${art.numBadge}
            </span>
            <div class="flex items-center gap-1.5">
              ${art.hasWarning ? '<span class="text-[9px] text-red-400 font-bold bg-red-950/80 px-1 py-0.5 rounded border border-red-800/60">⚠️ HAZARD</span>' : ''}
              <span class="text-[10px] text-cyan-400 font-mono">${art.readTime}m</span>
            </div>
          </div>
          <div class="font-semibold text-slate-200 group-hover:text-amber-200 transition-colors leading-snug chap-title">
            ${art.cleanTitle}
          </div>
          <div class="text-[10.5px] text-slate-400 font-sans leading-tight mt-1 border-l-2 border-[#164e5b] pl-1.5 group-hover:border-cyan-400 chap-sub">
            ${art.subTitle}
          </div>
        </div>
      `;
    });

    const isFirst = (vIdx === 0);

    container.innerHTML += `
      <div class="vol-card rounded-lg overflow-hidden border border-[#1a5b6a] shadow-md" id="volCard_${vIdx}">
        <!-- Volume Header Bar -->
        <div onclick="toggleVolume('${volId}', ${vIdx})" class="p-2.5 cursor-pointer flex flex-col gap-1.5 select-none bg-gradient-to-r from-[#062229] to-[#031317] hover:from-[#0b333d] transition-all">
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-1.5">
              <span class="text-base">${vol.catIcon}</span>
              <span class="px-1.5 py-0.5 rounded font-mono text-[10px] font-black tracking-wider text-amber-950 bg-gradient-to-r from-[#fcedb6] via-[#dfb15b] to-[#b8860b] shadow-sm border border-[#ffe494]">
                ${vol.volCode}
              </span>
              <span class="text-[9px] font-mono font-bold uppercase px-1.5 py-0.5 rounded" style="background: ${vol.hazardColor}22; color: ${vol.hazardColor}; border: 1px solid ${vol.hazardColor}66">
                ${vol.hazard}
              </span>
            </div>
            <span class="text-xs font-mono text-cyan-400 transition-transform duration-200" id="chevron_${volId}">
              ${isFirst ? '▲' : '▼'}
            </span>
          </div>

          <div class="text-xs font-bold text-amber-300 font-serif leading-tight">
            ${vol.title}
          </div>

          <div class="text-[10.5px] text-slate-400 font-sans leading-tight">
            ${vol.tagline}
          </div>

          <div class="flex items-center justify-between text-[9px] font-mono text-slate-400 pt-1 border-t border-[#164e5b]/40">
            <span>${vol.articles.length} ${vol.articles.length === 1 ? 'Chapter' : 'Chapters'}</span>
            <span>${vol.totalTime} min total</span>
          </div>
        </div>

        <!-- Volume Chapters Container -->
        <div id="${volId}" class="vol-chaps px-2 pb-2 space-y-1.5 ${isFirst ? '' : 'hidden'} border-t border-[#164e5b]/40 pt-2 bg-[#020a0d]/90">
          ${chapsHtml}
        </div>
      </div>
    `;
  });

  // Load first article initially
  if (ARTICLES.length > 0) {
    loadArticleByIndex(0);
  }
}

function toggleVolume(volId, vIdx) {
  AudioEngine.click();
  const el = document.getElementById(volId);
  const chevron = document.getElementById('chevron_' + volId);
  if (!el) return;
  const isHidden = el.classList.toggle('hidden');
  if (chevron) chevron.innerText = isHidden ? '▼' : '▲';
}

function expandAllVolumes() {
  AudioEngine.click();
  document.querySelectorAll('.vol-chaps').forEach(c => c.classList.remove('hidden'));
  document.querySelectorAll('[id^="chevron_"]').forEach(ch => ch.innerText = '▲');
}

function collapseAllVolumes() {
  AudioEngine.click();
  document.querySelectorAll('.vol-chaps').forEach(c => c.classList.add('hidden'));
  document.querySelectorAll('[id^="chevron_"]').forEach(ch => ch.innerText = '▼');
}

function filterAtlasTree(query) {
  const q = (query || '').toLowerCase().trim();
  let matchCount = 0;

  VOL_TREE.forEach((vol, vIdx) => {
    const card = document.getElementById('volCard_' + vIdx);
    const chapsContainer = document.getElementById('volGroup_' + vIdx);
    let volHasMatch = false;

    // Check volume title or tagline match
    if (vol.title.toLowerCase().includes(q) || vol.tagline.toLowerCase().includes(q) || vol.volCode.toLowerCase().includes(q)) {
      volHasMatch = true;
    }

    vol.articles.forEach(art => {
      const artEl = document.getElementById('treeItem_' + art.id);
      const isArtMatch = !q || art.title.toLowerCase().includes(q) || art.subTitle.toLowerCase().includes(q) || art.cleanTitle.toLowerCase().includes(q);
      if (artEl) {
        artEl.classList.toggle('hidden', !isArtMatch);
        if (isArtMatch) {
          volHasMatch = true;
          matchCount++;
        }
      }
    });

    if (card) card.classList.toggle('hidden', !volHasMatch);
    if (q && volHasMatch && chapsContainer) {
      chapsContainer.classList.remove('hidden');
      const chev = document.getElementById('chevron_volGroup_' + vIdx);
      if (chev) chev.innerText = '▲';
    }
  });

  const countBadge = document.getElementById('atlasMatchCount');
  if (countBadge) countBadge.innerText = q ? `${matchCount} Matches` : '15 Volumes';
}

function loadArticleById(artId) {
  const idx = ARTICLES.findIndex(a => a.id === artId);
  if (idx !== -1) loadArticleByIndex(idx);
}

function loadArticleByIndex(idx) {
  AudioEngine.click();
  if (idx < 0 || idx >= ARTICLES.length) return;
  currentArticleIndex = idx;
  const art = ARTICLES[idx];

  // Update Reading Room Header
  document.getElementById('articleCatIcon').innerText = art.catIcon || '⚡';
  document.getElementById('articleVolBadge').innerText = `${art.volCode || 'VOL'} • ${art.volTitle.toUpperCase()}`;
  document.getElementById('articleHeading').innerText = art.title;
  document.getElementById('articleSubLabel').innerText = art.subTitle || art.summary;
  document.getElementById('articleReadTime').innerText = art.readTime + ' min';
  document.getElementById('articleWords').innerText = art.wordCount.toLocaleString();
  document.getElementById('articleCounter').innerText = `Chapter ${idx + 1} of ${ARTICLES.length}`;

  const hazardFlag = document.getElementById('articleHazardFlag');
  if (hazardFlag) {
    hazardFlag.classList.toggle('hidden', !art.hasWarning);
  }

  // Populate Section Jump Selector
  const secSelect = document.getElementById('sectionSelect');
  if (secSelect) {
    secSelect.innerHTML = '<option value="">Table of Contents (Jump)</option>';
    art.sections.forEach(s => {
      secSelect.innerHTML += `<option value="${s}">${s}</option>`;
    });
  }

  // Inject unabridged content
  document.getElementById('articleContent').innerHTML = art.html;

  // Highlight Active Chapter in Left Atlas
  document.querySelectorAll('.chapter-card').forEach(c => c.classList.remove('active-chapter'));
  const activeTreeItem = document.getElementById('treeItem_' + art.id);
  if (activeTreeItem) {
    activeTreeItem.classList.add('active-chapter');
    // Ensure parent volume is open
    const parentVolGroup = activeTreeItem.closest('.vol-chaps');
    if (parentVolGroup && parentVolGroup.classList.contains('hidden')) {
      parentVolGroup.classList.remove('hidden');
      const chev = document.getElementById('chevron_' + parentVolGroup.id);
      if (chev) chev.innerText = '▲';
    }
    activeTreeItem.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }

  // Scroll reading room to top
  const room = document.getElementById('articleContent');
  if (room) room.scrollTop = 0;
  window.scrollTo({ top: 0, behavior: 'smooth' });

  // Update Prev / Next buttons
  document.getElementById('btnPrevArticle').disabled = (idx === 0);
  document.getElementById('btnNextArticle').disabled = (idx === ARTICLES.length - 1);
}

function navigateArticle(delta) {
  loadArticleByIndex(currentArticleIndex + delta);
}

function jumpToSection(title) {
  if (!title) return;
  const content = document.getElementById('articleContent');
  const headers = content.querySelectorAll('h2, h3, h4');
  for (let h of headers) {
    if (h.innerText.includes(title)) {
      h.scrollIntoView({ behavior: 'smooth', block: 'start' });
      h.classList.add('animate-pulse');
      setTimeout(() => h.classList.remove('animate-pulse'), 1500);
      break;
    }
  }
}

// ================= PINPOINTER OMNISEARCH =================
function handleSearch(query) {
  const dropdown = document.getElementById('searchDropdown');
  if (!query || query.trim().length < 2) {
    dropdown.classList.add('hidden');
    return;
  }
  const q = query.toLowerCase().trim();

  // Search articles
  const matchedArticles = ARTICLES.filter(a => 
    a.title.toLowerCase().includes(q) || 
    (a.subTitle && a.subTitle.toLowerCase().includes(q)) || 
    a.summary.toLowerCase().includes(q)
  );

  // Search donors
  const matchedDonors = DONORS.filter(d => 
    d.name.toLowerCase().includes(q) || 
    (d.harvest && d.harvest.some(h => h.toLowerCase().includes(q))) ||
    (d.bestFor && d.bestFor.toLowerCase().includes(q))
  );

  // Search blueprints
  const matchedBlueprints = BLUEPRINTS.filter(b => 
    b.title.toLowerCase().includes(q) || 
    (b.desc && b.desc.toLowerCase().includes(q)) ||
    (b.donor && b.donor.toLowerCase().includes(q))
  );

  if (matchedArticles.length === 0 && matchedDonors.length === 0 && matchedBlueprints.length === 0) {
    dropdown.innerHTML = '<div class="p-3 text-xs text-slate-400 font-mono">No matching records found.</div>';
    dropdown.classList.remove('hidden');
    return;
  }

  let html = '';
  matchedArticles.slice(0, 4).forEach(a => {
    html += `
      <div onclick="switchTab('encyclopedia'); loadArticleById('${a.id}'); document.getElementById('searchDropdown').classList.add('hidden');" 
           class="p-2.5 hover:bg-[#0e3a44] cursor-pointer border-b border-[#164e5b] text-xs">
        <span class="text-amber-300 font-bold">[ARTICLE] ${a.title}</span>
        <div class="text-[10px] text-slate-300 truncate">${a.subTitle || a.summary}</div>
      </div>
    `;
  });

  matchedDonors.slice(0, 3).forEach(d => {
    html += `
      <div onclick="switchTab('atlas'); filterAtlas('all'); setTimeout(() => { const el = document.getElementById('donor-${d.id}'); if (el) { el.scrollIntoView({behavior:'smooth', block:'center'}); el.classList.add('ring-2', 'ring-amber-400'); setTimeout(() => el.classList.remove('ring-2', 'ring-amber-400'), 2500); } }, 100); document.getElementById('searchDropdown').classList.add('hidden');" 
           class="p-2.5 hover:bg-[#0e3a44] cursor-pointer border-b border-[#164e5b] text-xs">
        <span class="text-emerald-300 font-bold">[DONOR] ${d.name}</span>
        <div class="text-[10px] text-slate-300 truncate">${(d.harvest || []).join(', ')}</div>
      </div>
    `;
  });

  matchedBlueprints.slice(0, 3).forEach(b => {
    html += `
      <div onclick="switchTab('blueprints'); openBlueprintModal(${b.num}); document.getElementById('searchDropdown').classList.add('hidden');" 
           class="p-2.5 hover:bg-[#0e3a44] cursor-pointer border-b border-[#164e5b] text-xs">
        <span class="text-cyan-300 font-bold">[BLUEPRINT] Build #${b.num}: ${b.title}</span>
        <div class="text-[10px] text-slate-300 truncate">${b.desc}</div>
      </div>
    `;
  });

  dropdown.innerHTML = html;
  dropdown.classList.remove('hidden');
}

// ================= TAB 3: BLUEPRINTS DOSSIER =================
function initBlueprints() {
  const grid = document.getElementById('blueprintsGrid');
  if (!grid) return;
  grid.innerHTML = '';

  const tabBadge = document.getElementById('blueprintsTabCount');
  if (tabBadge) tabBadge.innerText = `${BLUEPRINTS.length} Builds`;
  const headerCount = document.getElementById('blueprintsHeaderCount');
  if (headerCount) headerCount.innerText = BLUEPRINTS.length;
  const allBtn = document.getElementById('bpAllFilterBtn');
  if (allBtn) allBtn.innerText = `All ${BLUEPRINTS.length} Builds`;

  BLUEPRINTS.forEach(b => {
    grid.innerHTML += `
      <div class="encarta-window rounded-lg overflow-hidden flex flex-col justify-between p-4 shadow-lg hover:border-amber-400 transition-all group" id="bp-card-${b.num}">
        <div class="space-y-2">
          <div class="flex items-center justify-between text-[10px] font-mono">
            <span class="text-amber-400 font-bold font-serif">BUILD #${b.num} &bull; ${b.power || 'ACTIVE'}</span>
            <span class="px-2 py-0.5 rounded font-bold" style="background: ${b.diffColor || '#f59e0b'}22; color: ${b.diffColor || '#f59e0b'}; border: 1px solid ${b.diffColor || '#f59e0b'}55">
              ${b.diff || 'Intermediate'}
            </span>
          </div>
          <h3 class="text-sm font-bold text-slate-100 group-hover:text-amber-300 transition-colors font-serif">${b.title}</h3>
          <div class="text-[10.5px] text-cyan-300 font-mono">DONOR: ${b.donor}</div>
          <p class="text-[11px] text-slate-300 leading-snug">${b.desc}</p>
        </div>
        <div class="mt-4 pt-3 border-t border-[#164e5b] flex items-center justify-between">
          <span class="text-[10px] font-mono text-emerald-400 font-bold">SCHEMATIC READY</span>
          <button onclick="openBlueprintModal(${b.num})" class="encarta-btn px-3 py-1 rounded text-xs font-bold text-amber-200">
            Open Dossier &rarr;
          </button>
        </div>
      </div>
    `;
  });
}

function filterBlueprints(cat) {
  AudioEngine.click();
  document.querySelectorAll('.bp-filter-btn').forEach(b => b.classList.remove('active'));
  if (typeof event !== 'undefined' && event && event.target) event.target.classList.add('active');

  BLUEPRINTS.forEach(b => {
    const el = document.getElementById(`bp-card-${b.num}`);
    if (!el) return;
    if (cat === 'all') {
      el.classList.remove('hidden');
    } else if (cat === 'power') {
      const match = [1, 5, 14, 19, 38, 43, 49].includes(b.num) || b.cat === 'power';
      el.classList.toggle('hidden', !match);
    } else if (cat === 'machine') {
      const match = [4, 7, 10, 11, 13, 15, 17, 20, 21, 23, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 39, 40, 41, 42, 46, 47, 48, 50].includes(b.num) || b.cat === 'machine';
      el.classList.toggle('hidden', !match);
    } else if (cat === 'optics') {
      const match = [3, 6, 9, 12, 18, 22, 37, 44, 45].includes(b.num) || b.cat === 'optics';
      el.classList.toggle('hidden', !match);
    } else if (cat === 'mobility') {
      const match = [2, 8, 16, 27].includes(b.num) || b.cat === 'mobility';
      el.classList.toggle('hidden', !match);
    } else {
      el.classList.remove('hidden');
    }
  });
}

function openBlueprintModal(num) {
  AudioEngine.click();
  const bp = BLUEPRINTS.find(b => b.num === num);
  if (!bp) return;

  document.getElementById('bpModalTitle').innerText = `BLUEPRINT #${bp.num}: ${bp.title.toUpperCase()}`;
  const body = document.getElementById('bpModalBody');

  let bomHtml = '<ul class="list-disc pl-5 space-y-1">';
  (bp.bom || []).forEach(item => bomHtml += `<li>${item}</li>`);
  bomHtml += '</ul>';

  let sopHtml = '';
  if (Array.isArray(bp.sop)) {
    sopHtml = '<ol class="list-decimal pl-5 space-y-2">';
    bp.sop.forEach(step => sopHtml += `<li>${step}</li>`);
    sopHtml += '</ol>';
  } else if (typeof bp.sop === 'string') {
    sopHtml = '<ol class="list-decimal pl-5 space-y-2">';
    bp.sop.split('\n').filter(s => s.trim()).forEach(step => {
      const cleanStep = step.replace(/^[0-9]+\.\s*/, '');
      sopHtml += `<li>${cleanStep}</li>`;
    });
    sopHtml += '</ol>';
  }

  body.innerHTML = `
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 pb-4 border-b border-[#1b6170]">
      <div>
        <h4 class="text-xs font-bold text-amber-300 font-serif">Executive Summary</h4>
        <p class="text-slate-300 text-xs mt-1 leading-relaxed">${bp.desc}</p>
        <div class="mt-2 text-[11px] font-mono text-cyan-300"><strong class="text-amber-300">Physics Principle:</strong> ${bp.formula || 'N/A'}</div>
      </div>
      <div class="font-mono text-[11px] space-y-1 bg-[#04161b] p-3 rounded border border-[#164e5b]">
        <div><strong class="text-cyan-300">Target Donor:</strong> ${bp.donor}</div>
        <div><strong class="text-cyan-300">Power Rating:</strong> ${bp.power}</div>
        <div><strong class="text-cyan-300">Difficulty Rating:</strong> <span style="color: ${bp.diffColor || '#ffd978'}">${bp.diff}</span></div>
      </div>
    </div>

    <div>
      <h4 class="text-xs font-bold text-amber-300 uppercase font-serif mb-2">Kinematic Schematic &amp; Wiring Diagram</h4>
      <pre class="bg-[#020b0e] p-4 rounded border border-[#164e5b] text-cyan-300 text-[11px] font-mono leading-relaxed overflow-x-auto">${bp.schematic}</pre>
    </div>

    <div>
      <h4 class="text-xs font-bold text-amber-300 uppercase font-serif mb-2">Bill of Materials (Harvest &amp; Off-The-Shelf)</h4>
      <div class="bg-[#04161b] p-3 rounded border border-[#164e5b] text-slate-300">${bomHtml}</div>
    </div>

    <div>
      <h4 class="text-xs font-bold text-amber-300 uppercase font-serif mb-2">Step-by-Step Fabrication SOP</h4>
      <div class="bg-[#04161b] p-3 rounded border border-[#164e5b] text-slate-300 leading-relaxed">${sopHtml}</div>
    </div>
  `;

  document.getElementById('blueprintModal').classList.remove('hidden');
}

function closeBlueprintModal() {
  AudioEngine.click();
  document.getElementById('blueprintModal').classList.add('hidden');
}

// ================= TAB 4: APPLIANCE X-RAY CUTAWAY =================
const XRAY_MODELS = {
  microwave: {
    name: "Domestic Microwave Oven (1,200W)",
    layers: [
      { name: "Layer 0: Exterior Chassis & Interlocks", desc: "Sheet metal casing, door interlock snap switches, glass turntable tray, digital control PCB." },
      { name: "Layer 1: Kinematics & Cooling", desc: "Shaded-pole blower fan motor (30W), synchronous AC turntable gearmotor (3-5 RPM), plastic paddle ducting." },
      { name: "Layer 2: High-Voltage Circuitry", desc: "Microwave Oven Transformer (MOT, 2,000V AC), High-Voltage Diode (12kV), High-Voltage Oil-Filled Capacitor (0.9-1.1 uF)." },
      { name: "Layer 3: Lethal Hazard Hotspots", desc: "LETHAL: 2,000V - 4,000V capacitor charge retention. Beryllium Oxide (BeO) ceramic insulator in magnetron stalk (toxic if chipped). Bleeder resistor failure check." }
    ],
    hotspots: [
      { x: 340, y: 150, title: "Magnetron Vacuum Tube", desc: "Harvest 2x giant doughnut ferrite/neodymium magnets. Do NOT crush ceramic insulator stalk (toxic Beryllium Oxide)." },
      { x: 280, y: 220, title: "MOT (High-Voltage Transformer)", desc: "120V to 2,000V step-up. Cut secondary winding off with hacksaw to rewind with 2-gauge welding cable for 800A spot welder." },
      { x: 420, y: 240, title: "HV Capacitor & Diode", desc: "ALWAYS discharge with dual-insulated 10k 50W resistor shunt before touching. Stores lethal 2,000V charge even when unplugged." },
      { x: 120, y: 180, title: "Snap-Action Interlocks", desc: "3x 15A Omron/Honeywell microswitches. Harvest for CNC limit switches and high-reliability safety stops." }
    ]
  },
  washer: {
    name: "Direct-Drive Washing Machine",
    layers: [
      { name: "Layer 0: Exterior Cabinet", desc: "Enamelled steel shell, suspension struts, top door interlock." },
      { name: "Layer 1: Direct-Drive Stator & Tub", desc: "36-pole brushless permanent magnet stator, outer rotor bell with 48 rare-earth magnets, spider arm bearing housing." },
      { name: "Layer 2: Hall Sensor Board & Drainage", desc: "Digital Hall effect commutation board, drain pump BLDC motor, water inlet solenoids." },
      { name: "Layer 3: Supercritical Fluid Balancer", desc: "Hollow welded stainless steel toroidal ring filled with viscous fluid and chrome steel ball bearings. Self-balances high-speed rotordynamics above critical resonance." }
    ],
    hotspots: [
      { x: 260, y: 160, title: "36-Pole Pancake Stator", desc: "Massive 3-phase BLDC stator. Rewire from Wye to Delta for low-RPM 12V/24V high-yield wind turbine generator or 2x72 belt grinder drive." },
      { x: 380, y: 160, title: "Rotor Bell with Neodymium Magnets", desc: "High-strength outer rotor ring. Provides massive holding torque for direct-drive sim racing steering wheels." },
      { x: 260, y: 260, title: "LeBlanc Supercritical Balancer Ring", desc: "Hollow liquid-filled toroidal ring with ball bearings. Automatically cancels eccentric unbalance when spun past critical resonance." }
    ]
  },
  alternator: {
    name: "12V Automotive Alternator (130A)",
    layers: [
      { name: "Layer 0: Aluminum Casing", desc: "Die-cast vented aluminum housing, mounting ears, belt drive pulley." },
      { name: "Layer 1: Rotor Claw-Pole & Stator", desc: "3-phase delta-wound copper stator, claw-pole (Lundell) iron rotor with slip rings." },
      { name: "Layer 2: Brush Rig & Rectifier Bridge", desc: "6x high-current press-fit press diodes, graphite brush block, internal Zener regulator." },
      { name: "Layer 3: Variable-Reluctance Conversion", desc: "Bypassing internal regulator to supply variable rotor field current converts alternator into a 5 HP 3-phase synchronous AC motor or CNC lathe spindle!" }
    ],
    hotspots: [
      { x: 240, y: 150, title: "3-Phase Copper Stator", desc: "Tap directly into the 3 phase coils before the diode bridge to run with a high-current e-bike ESC as a 5HP brushless motor." },
      { x: 180, y: 150, title: "Claw-Pole Rotor Winding", desc: "Apply 12V through slip-ring brushes to magnetize rotor. Dynamic field weakening allows 10,000+ RPM without controller saturation." },
      { x: 320, y: 150, title: "60A Press-Fit Rectifier Diodes", desc: "Harvest heavy stud/press diodes for DIY arc welder rectifiers and solar reverse-current blocking." }
    ]
  }
};

let currentXrayModel = 'microwave';
let currentXrayLayer = 0;

function loadXRay(modelKey) {
  AudioEngine.click();
  currentXrayModel = modelKey;
  document.querySelectorAll('.xray-model-btn').forEach(b => b.classList.remove('active'));
  const btn = document.getElementById('btnXray' + modelKey.charAt(0).toUpperCase() + modelKey.slice(1));
  if (btn) btn.classList.add('active');

  currentXrayLayer = 0;
  document.getElementById('xrayLayerSlider').value = 0;
  renderXRay();
}

function setXRayLayer(layerIdx) {
  currentXrayLayer = parseInt(layerIdx);
  renderXRay();
}

function renderXRay() {
  const model = XRAY_MODELS[currentXrayModel];
  const layer = model.layers[currentXrayLayer];
  document.getElementById('xrayLayerName').innerText = layer.name;

  const container = document.getElementById('xrayCanvasContainer');
  let svg = `
    <svg viewBox="0 0 520 320" class="w-full h-full max-h-[380px]" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <radialGradient id="hotspotPing" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="#ffd978" stop-opacity="0.9"/>
          <stop offset="100%" stop-color="#ef4444" stop-opacity="0"/>
        </radialGradient>
      </defs>
      <!-- Base Chassis Outline -->
      <rect x="40" y="30" width="440" height="260" rx="10" fill="#041216" stroke="#164e5b" stroke-width="2"/>
      <rect x="60" y="50" width="400" height="220" rx="6" fill="#02090b" stroke="#1b6170" stroke-width="1.5" stroke-dasharray="4,4"/>
  `;

  // Draw model-specific internals
  if (currentXrayModel === 'microwave') {
    svg += `
      <!-- MOT Transformer -->
      <rect x="250" y="180" width="90" height="80" rx="4" fill="${currentXrayLayer >= 2 ? '#b45309' : '#08252d'}" stroke="#ffd978" stroke-width="2"/>
      <text x="295" y="225" fill="#fef08a" font-family="monospace" font-size="11" text-anchor="middle">MOT 2kV</text>

      <!-- Magnetron -->
      <rect x="310" y="110" width="90" height="70" rx="4" fill="${currentXrayLayer >= 1 ? '#0e3a44' : '#061a20'}" stroke="#38bdf8" stroke-width="2"/>
      <text x="355" y="145" fill="#67e8f9" font-family="monospace" font-size="10" text-anchor="middle">MAGNETRON</text>

      <!-- HV Capacitor -->
      <rect x="390" y="210" width="45" height="50" rx="6" fill="${currentXrayLayer >= 3 ? '#991b1b' : '#0a232b'}" stroke="#ef4444" stroke-width="2"/>
      <text x="412" y="240" fill="#fee2e2" font-family="monospace" font-size="9" text-anchor="middle">HV CAP</text>
    `;
  } else if (currentXrayModel === 'washer') {
    svg += `
      <!-- Stator -->
      <circle cx="260" cy="160" r="85" fill="${currentXrayLayer >= 1 ? '#0d3842' : '#04161b'}" stroke="#38bdf8" stroke-width="3"/>
      <circle cx="260" cy="160" r="50" fill="#020b0e" stroke="#164e5b" stroke-width="2"/>
      <text x="260" y="165" fill="#67e8f9" font-family="monospace" font-size="11" text-anchor="middle">36-POLE STATOR</text>

      <!-- Balancer Ring -->
      <circle cx="260" cy="160" r="105" fill="none" stroke="${currentXrayLayer >= 3 ? '#ffd978' : '#164e5b'}" stroke-width="6" stroke-dasharray="8,6"/>
    `;
  } else if (currentXrayModel === 'alternator') {
    svg += `
      <!-- Claw Rotor -->
      <circle cx="260" cy="160" r="75" fill="${currentXrayLayer >= 1 ? '#0e3a44' : '#04161b'}" stroke="#ffd978" stroke-width="3"/>
      <text x="260" y="165" fill="#fef08a" font-family="monospace" font-size="11" text-anchor="middle">CLAW ROTOR</text>
    `;
  }

  // Draw Hotspots (Radar Pings)
  model.hotspots.forEach((h, idx) => {
    svg += `
      <g onclick="inspectHotspot(${idx})" class="cursor-pointer group">
        <circle cx="${h.x}" cy="${h.y}" r="16" fill="url(#hotspotPing)" class="animate-ping" opacity="0.6"/>
        <circle cx="${h.x}" cy="${h.y}" r="9" fill="#ef4444" stroke="#ffffff" stroke-width="1.5"/>
        <text x="${h.x}" y="${h.y + 3}" fill="#ffffff" font-family="monospace" font-size="9" font-weight="bold" text-anchor="middle">${idx + 1}</text>
      </g>
    `;
  });

  svg += '</svg>';
  container.innerHTML = svg;
}

function inspectHotspot(idx) {
  AudioEngine.click();
  const model = XRAY_MODELS[currentXrayModel];
  const h = model.hotspots[idx];
  document.getElementById('hotspotTitle').innerHTML = `🔍 Hotspot #${idx + 1}: ${h.title}`;
  document.getElementById('hotspotDesc').innerHTML = h.desc;
}

// ================= TAB 6: 88-DONOR SCRAP ATLAS =================
function initAtlas() {
  const pills = document.getElementById('atlasFilterPills');
  if (!pills) return;
  
  const tabBadge = document.getElementById('atlasTabCount');
  if (tabBadge) tabBadge.innerText = `${DONORS.length} Donors`;
  const headerCount = document.getElementById('atlasHeaderCount');
  if (headerCount) headerCount.innerText = DONORS.length;

  let pillsHtml = `<button onclick="filterAtlas('all')" class="encarta-btn active px-3 py-1 rounded text-xs font-semibold atlas-pill">All (${DONORS.length})</button>`;
  CATEGORIES.forEach(c => {
    const count = DONORS.filter(d => d.cat === c.id).length;
    if (count > 0) {
      pillsHtml += `<button onclick="filterAtlas('${c.id}')" class="encarta-btn px-3 py-1 rounded text-xs font-semibold atlas-pill">${c.icon} ${c.name.split(' ')[0]} (${count})</button>`;
    }
  });
  pills.innerHTML = pillsHtml;
  renderDonors(DONORS);
}

function renderDonors(list) {
  const grid = document.getElementById('donorsGrid');
  if (!grid) return;
  grid.innerHTML = '';
  
  list.forEach(d => {
    const catObj = CATEGORIES.find(c => c.id === d.cat) || { name: (d.cat || 'GENERAL').toUpperCase(), icon: '📦' };
    
    let harvestTags = '';
    (d.harvest || []).forEach(h => {
      harvestTags += `<span class="bg-[#04161b] text-cyan-300 border border-[#164e5b] text-[10px] font-mono px-2 py-0.5 rounded leading-tight">${h}</span> `;
    });

    grid.innerHTML += `
      <div id="donor-${d.id}" class="encarta-window rounded-lg overflow-hidden p-4 space-y-3 shadow-md hover:border-amber-400 transition-all flex flex-col justify-between">
        <div class="space-y-2">
          <div class="flex items-center justify-between text-[10px] font-mono">
            <span class="text-amber-400 font-bold uppercase flex items-center gap-1">${catObj.icon} ${catObj.name}</span>
            <span class="px-2 py-0.5 rounded font-mono font-bold" style="background: ${d.dangerColor || '#f59e0b'}22; color: ${d.dangerColor || '#f59e0b'}; border: 1px solid ${d.dangerColor || '#f59e0b'}55">
              ${d.danger || 'Standard'}
            </span>
          </div>
          <h3 class="text-sm font-bold text-slate-100 font-serif">${d.name}</h3>
          <div class="flex flex-wrap gap-1">${harvestTags}</div>
        </div>
        <div class="space-y-1.5 pt-2 border-t border-[#164e5b] text-[11px] text-slate-300 font-sans leading-snug">
          <div><strong class="text-amber-300">Target Repurposing:</strong> ${d.bestFor || 'General Electromechanical Projects'}</div>
          <div><strong class="text-red-400">Critical Avoidance:</strong> ${d.avoid || 'None reported'}</div>
          <div class="text-[10px] font-mono text-cyan-200/80 bg-[#020b0e] p-2 rounded border border-[#164e5b]/60">
            <strong class="text-cyan-300">Field Triage:</strong> ${d.triage || 'Bench test with DMM before deployment'}
          </div>
        </div>
      </div>
    `;
  });
}

function filterAtlas(catId) {
  AudioEngine.click();
  document.querySelectorAll('.atlas-pill').forEach(p => p.classList.remove('active'));
  if (typeof event !== 'undefined' && event && event.target) {
    event.target.classList.add('active');
  }
  if (catId === 'all') {
    renderDonors(DONORS);
  } else {
    renderDonors(DONORS.filter(d => d.cat === catId));
  }
}

// Alias for safety
const filterDonors = filterAtlas;

// Global Initialization On DOM Ready
window.addEventListener('DOMContentLoaded', () => {
  VU.init();
  initEncyclopediaTree();
  initAtlas();
  initBlueprints();
  initSparkSim();
});
"""
