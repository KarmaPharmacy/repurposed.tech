"""
REPURPOSED.TECH : THE MAKER'S BIBLE - Core Application Logic
Industrial Field-Engineering Console (Palantir Foundry / Blueprint UI Design System)
Contains:
- Channel Switching (CH-1: Compendium, CH-2: Blueprints, CH-3: Scrap Atlas)
- Obsidian-Inspired Knowledge-Base Tree Navigation with live grep & accordions
- Dense Technical Document Reader with section jumps, code copy buffers, and pagers
- 50 Engineering Blueprints grid & full specification dossier modal
- 88 Donor Streams Scrap Atlas telemetry cards
- Spotlight Command Palette (Ctrl+K / Cmd+K)
- Offline Exports Modal
"""

REPURPOSED_CORE_JS = r"""
// ================= GLOBAL STATE =================
let currentView = 'compendium';
let currentArticleIndex = 0;
let activeBpFilter = 'all';
let activeAtlasFilter = 'all';

// ================= FUNCTION BUS (VIEW SWITCHER) =================
function switchView(viewId) {
  currentView = viewId;
  document.querySelectorAll('nav .terminal-btn').forEach(b => {
    b.classList.remove('active');
    const led = b.querySelector('.led');
    if (led) led.className = 'led';
  });
  
  const activeTab = document.getElementById('tab-' + viewId);
  if (activeTab) {
    activeTab.classList.add('active');
    const activeLed = activeTab.querySelector('.led');
    if (activeLed) activeLed.className = 'led active-blue';
  }

  ['compendium', 'blueprints', 'atlas'].forEach(v => {
    const el = document.getElementById('view-' + v);
    if (el) el.classList.toggle('hidden', v !== viewId);
  });

  if (viewId === 'blueprints') initBlueprints();
  if (viewId === 'atlas') initAtlas();
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// ================= 1. THE COMPENDIUM DIRECTORY BUS =================
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
             class="tree-node p-2 rounded-[3px] cursor-pointer text-xs select-none relative group bg-[#202B33] border border-[#30404D] hover:bg-[#293742] transition-colors">
          <div class="flex items-center justify-between gap-1 mb-1 font-mono">
            <span class="px-1 py-0.2 rounded-[2px] text-[10px] font-bold text-[#2B95D6] bg-[#182026] border border-[#137CBD]/30">
              ${art.numBadge}
            </span>
            <div class="flex items-center gap-1.5">
              ${art.hasWarning ? '<span class="text-[9px] text-[#F55656] font-bold bg-[#DB3737]/15 px-1 py-0.2 rounded-[2px] border border-[#DB3737]/40">[!] HAZARD</span>' : ''}
              <span class="text-[10px] text-[#5C7080]">${art.readTime}m</span>
            </div>
          </div>
          <div class="font-semibold text-[#BFCCD6] group-hover:text-[#F5F8FA] transition-colors leading-snug node-title text-[11.5px]">
            ${art.cleanTitle}
          </div>
          <div class="text-[10.5px] text-[#8A9BA8] leading-tight mt-1 border-l border-[#30404D] pl-2 group-hover:border-[#137CBD] truncate">
            ${art.subTitle}
          </div>
        </div>
      `;
    });

    const isFirst = (vIdx === 0);
    const isLethal = vol.hazard.includes('HIGH') || vol.hazard.includes('LETHAL');
    const isShop = vol.hazard.includes('KINEMATICS') || vol.hazard.includes('SHOP');
    const ledColor = isLethal ? 'active-red' : (isShop ? 'active-amber' : 'active-blue');

    container.innerHTML += `
      <div class="rounded-[3px] border border-[#30404D] bg-[#202B33] overflow-hidden transition-all" id="volCard_${vIdx}">
        <!-- Volume Header Bar -->
        <div onclick="toggleVolume('${volId}', ${vIdx})" class="p-2.5 cursor-pointer flex flex-col gap-1 select-none hover:bg-[#293742] transition-colors">
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-1.5 font-mono">
              <span class="led ${ledColor}"></span>
              <span class="px-1.5 py-0.2 rounded-[2px] text-[10px] font-bold text-[#F5F8FA] bg-[#182026] border border-[#30404D]">
                ${vol.volCode}
              </span>
              <span class="text-[9px] font-bold uppercase px-1 py-0.2 rounded-[2px] ${isLethal ? 'bg-[#DB3737]/15 text-[#F55656] border border-[#DB3737]/40' : 'bg-[#182026] text-[#8A9BA8] border border-[#30404D]'}">
                ${vol.hazard}
              </span>
            </div>
            <span class="text-[11px] font-mono text-[#8A9BA8]" id="chevron_${volId}">
              ${isFirst ? '[-]' : '[+]'}
            </span>
          </div>

          <div class="text-xs font-bold text-[#F5F8FA] leading-tight pt-0.5">
            ${vol.title}
          </div>

          <div class="text-[11px] text-[#8A9BA8] leading-tight">
            ${vol.tagline}
          </div>

          <div class="flex items-center justify-between text-[10px] font-mono text-[#5C7080] pt-1 border-t border-[#30404D]">
            <span>${vol.articles.length} CHAPTERS</span>
            <span>TOTAL: ${vol.totalTime} MIN</span>
          </div>
        </div>

        <!-- Volume Chapters Container -->
        <div id="${volId}" class="vol-chaps px-2 pb-2 space-y-1.5 ${isFirst ? '' : 'hidden'} border-t border-[#30404D] pt-1.5 bg-[#182026]">
          ${chapsHtml}
        </div>
      </div>
    `;
  });

  if (ARTICLES.length > 0) {
    loadArticleByIndex(0);
  }
}

function toggleVolume(volId, vIdx) {
  const el = document.getElementById(volId);
  const chevron = document.getElementById('chevron_' + volId);
  if (!el) return;
  const isHidden = el.classList.toggle('hidden');
  if (chevron) chevron.innerText = isHidden ? '[+]' : '[-]';
}

function expandAllVolumes() {
  document.querySelectorAll('.vol-chaps').forEach(c => c.classList.remove('hidden'));
  document.querySelectorAll('[id^="chevron_"]').forEach(ch => ch.innerText = '[-]');
}

function collapseAllVolumes() {
  document.querySelectorAll('.vol-chaps').forEach(c => c.classList.add('hidden'));
  document.querySelectorAll('[id^="chevron_"]').forEach(ch => ch.innerText = '[+]');
}

function filterAtlasTree(query) {
  const q = (query || '').toLowerCase().trim();
  let matchCount = 0;

  VOL_TREE.forEach((vol, vIdx) => {
    const card = document.getElementById('volCard_' + vIdx);
    const chapsContainer = document.getElementById('volGroup_' + vIdx);
    let volHasMatch = false;

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
      if (chev) chev.innerText = '[-]';
    }
  });

  const countBadge = document.getElementById('atlasMatchCount');
  if (countBadge) countBadge.innerText = q ? `${matchCount} MATCHES` : '36 CHANNELS';
}

function loadArticleById(artId) {
  const idx = ARTICLES.findIndex(a => a.id === artId);
  if (idx !== -1) {
    switchView('compendium');
    loadArticleByIndex(idx);
  }
}

function loadArticleByIndex(idx) {
  if (idx < 0 || idx >= ARTICLES.length) return;
  currentArticleIndex = idx;
  const art = ARTICLES[idx];

  // Header Banner
  document.getElementById('articleCatIcon').innerText = art.catIcon || '⚡';
  document.getElementById('articleVolBadge').innerText = `${art.volCode || 'VOL'} // ${art.volTitle.toUpperCase()}`;
  document.getElementById('articleHeading').innerText = art.title;
  document.getElementById('articleSubLabel').innerText = art.subTitle || art.summary;
  document.getElementById('articleReadTime').innerText = art.readTime + 'm';
  document.getElementById('articleWords').innerText = art.wordCount.toLocaleString();
  document.getElementById('articleCounter').innerText = `CH ${idx + 1} OF ${ARTICLES.length}`;

  const hazardFlag = document.getElementById('articleHazardFlag');
  if (hazardFlag) {
    hazardFlag.classList.toggle('hidden', !art.hasWarning);
  }

  // Section Selector
  const secSelect = document.getElementById('sectionSelect');
  if (secSelect) {
    secSelect.innerHTML = '<option value="">Jump to section...</option>';
    art.sections.forEach(s => {
      secSelect.innerHTML += `<option value="${s}">&gt; ${s}</option>`;
    });
  }

  // Inject Unabridged Content
  const contentEl = document.getElementById('articleContent');
  contentEl.innerHTML = art.html;

  // Add Copy Code Buttons to Code Blocks (Palantir style)
  contentEl.querySelectorAll('pre').forEach((pre) => {
    const copyBtn = document.createElement('button');
    copyBtn.className = 'absolute top-2 right-2 px-2 py-0.5 rounded-[3px] bg-[#202B33] text-[#BFCCD6] hover:text-[#FFFFFF] hover:bg-[#293742] text-[10px] font-mono border border-[#30404D] transition cursor-pointer';
    copyBtn.innerText = '[COPY BUFFER]';
    copyBtn.onclick = () => {
      navigator.clipboard.writeText(pre.innerText.replace('[COPY BUFFER]', '').trim());
      copyBtn.innerText = '[COPIED!]';
      setTimeout(() => copyBtn.innerText = '[COPY BUFFER]', 1500);
    };
    pre.style.position = 'relative';
    pre.appendChild(copyBtn);
  });

  // Highlight Active Chapter in Atlas
  document.querySelectorAll('.tree-node').forEach(c => c.classList.remove('active-chapter'));
  const activeTreeItem = document.getElementById('treeItem_' + art.id);
  if (activeTreeItem) {
    activeTreeItem.classList.add('active-chapter');
    const parentVolGroup = activeTreeItem.closest('.vol-chaps');
    if (parentVolGroup && parentVolGroup.classList.contains('hidden')) {
      parentVolGroup.classList.remove('hidden');
      const chev = document.getElementById('chevron_' + parentVolGroup.id);
      if (chev) chev.innerText = '[-]';
    }
    activeTreeItem.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }

  // Prev / Next Navigation buttons
  document.getElementById('btnPrevArticle').disabled = (idx === 0);
  document.getElementById('btnNextArticle').disabled = (idx === ARTICLES.length - 1);

  // Close mobile sidebar if open
  const sidebar = document.getElementById('atlasSidebar');
  if (sidebar && window.innerWidth < 1024) {
    sidebar.classList.add('hidden');
  }

  window.scrollTo({ top: 0, behavior: 'smooth' });
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
      h.style.outline = '2px solid #137CBD';
      setTimeout(() => h.style.outline = 'none', 1800);
      break;
    }
  }
}

function copyCurrentChapterLink() {
  const url = `${window.location.origin}/#art_${currentArticleIndex + 1}`;
  navigator.clipboard.writeText(url).then(() => {
    alert(`BUFFER LINK STORED:\n${url}`);
  });
}

function toggleMobileSidebar() {
  const sidebar = document.getElementById('atlasSidebar');
  if (sidebar) sidebar.classList.toggle('hidden');
}

// ================= 2. 50 ENGINEERING BLUEPRINTS =================
function initBlueprints() {
  const grid = document.getElementById('blueprintsGrid');
  if (!grid || grid.children.length > 0) return;
  filterBlueprints('all');
}

function filterBlueprints(cat, evt) {
  activeBpFilter = cat;
  document.querySelectorAll('.bp-filter-btn').forEach(b => b.classList.remove('active'));
  const btn = (evt && evt.target && evt.target.classList) ? evt.target : document.getElementById('bpAllFilterBtn');
  if (btn && btn.classList) btn.classList.add('active');

  const grid = document.getElementById('blueprintsGrid');
  if (!grid) return;
  grid.innerHTML = '';

  const filtered = (cat === 'all') ? BLUEPRINTS : BLUEPRINTS.filter(b => b.cat === cat);
  const countEl = document.getElementById('blueprintsHeaderCount');
  if (countEl) countEl.innerText = filtered.length;

  filtered.forEach(bp => {
    let bomChips = '';
    (bp.bom || []).slice(0, 3).forEach(item => {
      bomChips += `<span class="px-1.5 py-0.5 rounded-[2px] bg-[#202B33] border border-[#30404D] text-[10px] text-[#BFCCD6] font-mono truncate max-w-[200px]">${escapeHtml(item)}</span>`;
    });

    const isAdv = bp.diff.includes('Advanced');
    const isInter = bp.diff.includes('Intermediate');
    const diffBadgeClass = isAdv ? 'bg-[#DB3737]/15 text-[#F55656] border-[#DB3737]/40' : 
                           (isInter ? 'bg-[#D9822B]/15 text-[#F29D49] border-[#D9822B]/40' : 'bg-[#0F9960]/15 text-[#15B371] border-[#0F9960]/40');

    grid.innerHTML += `
      <div id="blueprint-${bp.num}" onclick="openBlueprintModal(${bp.num})" 
           class="bg-[#293742] border border-[#30404D] rounded-[3px] p-4 flex flex-col justify-between space-y-3 shadow-sm hover:border-[#137CBD] hover:bg-[#293742]/95 cursor-pointer transition-all group select-none">
        <div class="space-y-2">
          <!-- Top Row Badges -->
          <div class="flex items-center justify-between text-xs">
            <span class="px-1.5 py-0.5 rounded-[2px] bg-[#202B33] text-[#2B95D6] font-mono font-bold border border-[#137CBD]/40 text-[10px]">
              SPEC_ID: BP-${bp.num < 10 ? '0' + bp.num : bp.num}
            </span>
            <span class="px-1.5 py-0.5 rounded-[2px] font-mono font-bold text-[10px] border ${diffBadgeClass}">
              ${bp.diff}
            </span>
          </div>

          <!-- Title -->
          <h3 class="text-sm font-bold text-[#F5F8FA] leading-snug hover:text-[#2B95D6] transition-colors">
            ${escapeHtml(bp.title)}
          </h3>

          <!-- Donor & Power Telemetry -->
          <div class="text-[11px] space-y-0.5 text-[#8A9BA8] font-sans">
            <div>DONOR: <span class="text-[#F5F8FA] font-mono">${escapeHtml(bp.donor)}</span></div>
            <div>POWER: <span class="text-[#F29D49] font-mono font-semibold">${escapeHtml(bp.power)}</span></div>
          </div>

          <!-- Description -->
          <p class="text-xs text-[#8A9BA8] leading-relaxed line-clamp-3">
            ${escapeHtml(bp.desc)}
          </p>

          <!-- BOM Preview -->
          <div class="flex flex-wrap gap-1 pt-1">
            ${bomChips}
          </div>
        </div>

        <!-- Action Button (Palantir Button) -->
        <button onclick="event.stopPropagation(); openBlueprintModal(${bp.num})" 
                class="terminal-btn w-full mt-2 py-1.5 px-3 rounded-[3px] bg-[#202B33] hover:bg-[#137CBD] border border-[#30404D] hover:border-[#137CBD] text-[#BFCCD6] hover:text-[#FFFFFF] text-xs font-semibold flex items-center justify-center space-x-1.5 transition cursor-pointer">
          <span class="font-mono">&gt;&gt;</span>
          <span>LOAD SCHEMATIC &amp; FABRICATION SOP</span>
        </button>
      </div>
    `;
  });
}

function escapeHtml(str) {
  return String(str || '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function openBlueprintModal(num) {
  const targetNum = typeof num === 'string' ? parseInt(num, 10) : num;
  const bp = BLUEPRINTS.find(b => b.num === targetNum);
  if (!bp) {
    console.error('Blueprint not found for num:', num);
    return;
  }

  const titleEl = document.getElementById('bpModalTitle');
  if (titleEl) {
    titleEl.innerText = `SPEC_DOSSIER // BP-${bp.num < 10 ? '0' + bp.num : bp.num}: ${bp.title}`;
  }
  
  let bomList = '';
  (bp.bom || []).forEach(b => bomList += `<li class="text-xs text-[#BFCCD6] font-mono">${escapeHtml(b)}</li>`);

  // Handle SOP whether it is an array or newline-separated string
  let steps = [];
  if (Array.isArray(bp.sop)) {
    steps = bp.sop;
  } else if (typeof bp.sop === 'string') {
    steps = bp.sop.split(/\r?\n/).map(s => s.trim()).filter(Boolean);
  }

  let sopList = '';
  steps.forEach((step, i) => {
    sopList += `<div class="p-3 rounded-[3px] bg-[#202B33] border border-[#30404D] space-y-1">
      <div class="font-bold text-[#2B95D6] font-mono text-[11px]">STEP 0${i+1} PROTOCOL:</div>
      <div class="text-[#BFCCD6] text-xs leading-relaxed font-sans">${escapeHtml(step)}</div>
    </div>`;
  });

  const body = document.getElementById('bpModalBody');
  if (body) {
    body.innerHTML = `
      <!-- Calibration Telemetry Line -->
      <div class="grid grid-cols-1 md:grid-cols-4 gap-2 p-3 rounded-[3px] bg-[#202B33] border border-[#30404D] text-xs font-sans">
        <div><span class="text-[#8A9BA8] text-[11px]">TARGET DONOR:</span> <div class="text-[#F5F8FA] font-bold font-mono">${escapeHtml(bp.donor)}</div></div>
        <div><span class="text-[#8A9BA8] text-[11px]">RATED POWER:</span> <div class="text-[#F29D49] font-bold font-mono">${escapeHtml(bp.power)}</div></div>
        <div><span class="text-[#8A9BA8] text-[11px]">DIFFICULTY:</span> <div class="text-[#BFCCD6] font-bold font-mono">${escapeHtml(bp.diff)}</div></div>
        <div><span class="text-[#8A9BA8] text-[11px]">EPISTEMIC GATE:</span> <div class="text-[#0F9960] font-bold font-mono">VERIFIED / CALCULATED</div></div>
      </div>

      <!-- Description -->
      <div>
        <div class="text-[11px] font-bold text-[#2B95D6] mb-1 font-mono">&gt;&gt; ENGINEERING OVERVIEW:</div>
        <p class="text-[#BFCCD6] text-xs leading-relaxed font-sans">${escapeHtml(bp.desc)}</p>
      </div>

      ${bp.formula ? `
      <!-- Formula / Calculation -->
      <div>
        <div class="text-[11px] font-bold text-[#2B95D6] mb-1 font-mono">&gt;&gt; GOVERNING KINEMATIC FORMULA:</div>
        <pre class="overflow-x-auto text-[#2B95D6] text-xs p-3 rounded-[3px] border border-[#137CBD]/40 border-l-4 border-l-[#2B95D6] bg-[#11161B] font-mono">${escapeHtml(bp.formula)}</pre>
      </div>
      ` : ''}

      <!-- Schematic -->
      <div>
        <div class="flex items-center justify-between mb-1">
          <span class="text-[11px] font-bold text-[#2B95D6] font-mono">&gt;&gt; KINEMATIC SCHEMATIC &amp; WIRING:</span>
          <button id="copySchematicBtn" onclick="copyBlueprintSchematic()" 
                  class="px-2 py-0.5 rounded-[2px] bg-[#202B33] text-[10px] text-[#BFCCD6] hover:text-[#F5F8FA] hover:bg-[#30404D] border border-[#30404D] font-mono cursor-pointer transition">
            [COPY SCHEMATIC]
          </button>
        </div>
        <pre id="bpSchematicContent" class="overflow-x-auto text-[#D8E1E8] text-xs p-3.5 rounded-[3px] border border-[#30404D] bg-[#11161B] whitespace-pre-wrap font-mono">${escapeHtml(bp.schematic)}</pre>
      </div>

      <!-- Bill of Materials -->
      <div>
        <div class="flex items-center justify-between mb-1">
          <span class="text-[11px] font-bold text-[#F29D49] font-mono">&gt;&gt; BILL OF MATERIALS:</span>
          <button id="copyBomBtn" onclick="copyBlueprintBOM()" 
                  class="px-2 py-0.5 rounded-[2px] bg-[#202B33] text-[10px] text-[#BFCCD6] hover:text-[#F5F8FA] hover:bg-[#30404D] border border-[#30404D] font-mono cursor-pointer transition">
            [COPY BOM]
          </button>
        </div>
        <ul id="bpBomList" class="space-y-1 list-disc pl-5 bg-[#202B33] p-3 rounded-[3px] border border-[#30404D]">${bomList}</ul>
      </div>

      <!-- Step-by-Step Fabrication SOP -->
      <div class="space-y-2">
        <div class="text-[11px] font-bold text-[#2B95D6] font-mono">&gt;&gt; STEP-BY-STEP FABRICATION SOP:</div>
        <div class="space-y-2">${sopList}</div>
      </div>
    `;
  }

  const modal = document.getElementById('blueprintModal');
  if (modal) {
    modal.classList.remove('hidden');
    modal.style.display = 'flex'; if (modal.style.setProperty) { modal.style.setProperty('display', 'flex', 'important'); }
    document.body.style.overflow = 'hidden';
  }
}

function closeBlueprintModal() {
  const modal = document.getElementById('blueprintModal');
  if (modal) {
    modal.classList.add('hidden');
    modal.style.display = 'none'; if (modal.style.setProperty) { modal.style.setProperty('display', 'none', 'important'); }
    document.body.style.overflow = '';
  }
}

function copyBlueprintSchematic() {
  const el = document.getElementById('bpSchematicContent');
  if (el) {
    navigator.clipboard.writeText(el.innerText).then(() => {
      const btn = document.getElementById('copySchematicBtn');
      if (btn) {
        btn.innerText = '[STORED]';
        setTimeout(() => btn.innerText = '[COPY SCHEMATIC]', 1500);
      }
    });
  }
}

function copyBlueprintBOM() {
  const items = Array.from(document.querySelectorAll('#bpBomList li')).map(li => li.innerText).join('\n');
  if (items) {
    navigator.clipboard.writeText(items).then(() => {
      const btn = document.getElementById('copyBomBtn');
      if (btn) {
        btn.innerText = '[STORED]';
        setTimeout(() => btn.innerText = '[COPY BOM]', 1500);
      }
    });
  }
}

// ================= 3. 88 DONOR STREAMS SCRAP ATLAS =================
function initAtlas() {
  const pills = document.getElementById('atlasFilterPills');
  if (!pills || pills.children.length > 0) return;

  let pillsHtml = `<button onclick="filterAtlas('all')" class="terminal-btn active atlas-pill">[ALL: ${DONORS.length}]</button>`;
  CATEGORIES.forEach(c => {
    const count = DONORS.filter(d => d.cat === c.id).length;
    if (count > 0) {
      pillsHtml += `<button onclick="filterAtlas('${c.id}')" class="terminal-btn atlas-pill">[${c.name.split(' ')[0].toUpperCase()}: ${count}]</button>`;
    }
  });
  pills.innerHTML = pillsHtml;
  renderDonors(DONORS);
}

function toggleDonorDrawer(id, evt) {
  if (evt) evt.stopPropagation();
  const drawer = document.getElementById('donor-drawer-' + id);
  const btn = document.getElementById('donor-toggle-btn-' + id);
  if (!drawer) return;
  const isHidden = drawer.classList.contains('hidden');
  drawer.classList.toggle('hidden', !isHidden);
  if (btn) {
    btn.innerHTML = isHidden 
      ? '<span class="font-mono">[-]</span> <span>COLLAPSE</span>' 
      : '<span class="font-mono">[+]</span> <span>QUICK VIEW</span>';
  }
}

function renderDonors(list) {
  const grid = document.getElementById('donorsGrid');
  if (!grid) return;
  grid.innerHTML = '';

  list.forEach(d => {
    const catObj = CATEGORIES.find(c => c.id === d.cat) || { name: (d.cat || 'GENERAL').toUpperCase() };
    
    let harvestTags = '';
    (d.harvest || []).slice(0, 4).forEach(h => {
      harvestTags += `<span class="bg-[#202B33] text-[#BFCCD6] border border-[#30404D] text-[10px] font-mono px-1.5 py-0.2 rounded-[2px]">${escapeHtml(h)}</span> `;
    });
    if ((d.harvest || []).length > 4) {
      harvestTags += `<span class="bg-[#182026] text-[#8A9BA8] border border-[#30404D] text-[9px] font-mono px-1 py-0.2 rounded-[2px]">+${d.harvest.length - 4} more</span>`;
    }

    const isDanger = (d.danger || '').toUpperCase().includes('LETHAL') || (d.danger || '').toUpperCase().includes('HIGH');

    let toolPills = '';
    (d.tools || ['Standard Hand Tools', 'Multimeter']).slice(0, 3).forEach(t => {
      toolPills += `<span class="bg-[#182026] text-[#D8E1E8] border border-[#30404D] text-[9px] font-mono px-1.5 py-0.2 rounded-[2px]">${escapeHtml(t)}</span> `;
    });

    let bpHtml = '';
    if (d.blueprints && d.blueprints.length > 0) {
      d.blueprints.slice(0, 2).forEach(bpNum => {
        bpHtml += `<button onclick="event.stopPropagation(); switchView('blueprints'); openBlueprintModal(${bpNum})" class="px-1.5 py-0.5 rounded-[2px] bg-[#11161B] text-[10px] text-[#2B95D6] hover:text-[#FFFFFF] hover:bg-[#137CBD] border border-[#137CBD]/40 font-mono transition">BP-${bpNum < 10 ? '0' + bpNum : bpNum}</button> `;
      });
    }

    grid.innerHTML += `
      <div id="donor-${d.id}" onclick="openDonorModal('${d.id}')" 
           class="bg-[#293742] border border-[#30404D] rounded-[3px] p-4 flex flex-col justify-between space-y-3 shadow-sm hover:border-[#137CBD] hover:bg-[#293742]/95 cursor-pointer transition-all group select-none">
        <div class="space-y-2">
          <!-- Top Row Badges -->
          <div class="flex items-center justify-between text-[10px] font-mono">
            <span class="px-1.5 py-0.5 rounded-[2px] bg-[#202B33] text-[#2B95D6] font-mono font-bold border border-[#137CBD]/40 text-[10px]">
              STREAM: ${d.id.toUpperCase()}
            </span>
            <span class="px-1.5 py-0.5 rounded-[2px] font-mono font-bold text-[10px] border ${isDanger ? 'bg-[#DB3737]/15 text-[#F55656] border-[#DB3737]/40' : 'bg-[#202B33] text-[#8A9BA8] border-[#30404D]'}">
              ${isDanger ? '[!] ' : ''}${escapeHtml(d.danger || 'STANDARD')}
            </span>
          </div>

          <!-- Category Indicator -->
          <div class="text-[10px] font-mono text-[#8A9BA8] uppercase">&gt; ${escapeHtml(catObj.name)}</div>

          <!-- Donor Name -->
          <h3 class="text-sm font-bold text-[#F5F8FA] group-hover:text-[#2B95D6] transition-colors leading-snug">
            ${escapeHtml(d.name)}
          </h3>
          
          <!-- Specifications Telemetry -->
          <div class="text-[11px] font-mono text-[#D8E1E8] bg-[#202B33] p-1.5 rounded-[2px] border border-[#30404D] truncate">
            <span class="text-[#8A9BA8]">SPECS:</span> ${escapeHtml(d.specs || 'Variable salvage ratings [TYPICAL]')}
          </div>

          <!-- Recoverable Primitives Preview -->
          <div class="flex flex-wrap gap-1 pt-0.5">${harvestTags}</div>
        </div>

        <div class="space-y-2 pt-2 border-t border-[#30404D] text-xs text-[#BFCCD6] leading-snug font-sans">
          <div class="truncate"><strong class="text-[#F5F8FA]">TARGET:</strong> ${escapeHtml(d.bestFor || 'Electromechanical builds')}</div>
          
          <!-- Inline Collapsible Drawer (Quick Specs Accordion) -->
          <div id="donor-drawer-${d.id}" class="hidden space-y-2 pt-2 border-t border-[#30404D] font-mono text-[11px] bg-[#202B33] p-2.5 rounded-[3px]">
            <div><span class="text-[#8A9BA8]">DIFF:</span> <span class="text-[#F5F8FA] font-bold">${escapeHtml(d.diff || 'Intermediate')}</span></div>
            <div><span class="text-[#8A9BA8]">INTERFACES:</span> <span class="text-[#BFCCD6]">${escapeHtml(d.interfaces || 'Standard mounting & terminals')}</span></div>
            <div><span class="text-[#8A9BA8]">TEARDOWN TOOLS:</span> <div class="flex flex-wrap gap-1 mt-1">${toolPills}</div></div>
            <div class="p-1.5 rounded-[2px] ${isDanger ? 'bg-[#DB3737]/20 text-[#F55656] border border-[#DB3737]/50' : 'bg-[#D9822B]/20 text-[#F29D49] border border-[#D9822B]/50'}">
              <strong>[SAFETY GATE]:</strong> ${escapeHtml(d.avoid || 'Standard precautions')}
            </div>
            <div><span class="text-[#0F9960] font-bold">TRIAGE:</span> <span class="text-[#BFCCD6]">${escapeHtml(d.triage || 'Bench test with DMM')}</span></div>
            ${bpHtml ? `<div class="pt-1 flex items-center gap-1.5"><span class="text-[#8A9BA8] text-[10px]">BLUEPRINTS:</span> ${bpHtml}</div>` : ''}
          </div>

          <!-- Action Buttons Bar -->
          <div class="grid grid-cols-2 gap-1.5 pt-1">
            <button id="donor-toggle-btn-${d.id}" onclick="toggleDonorDrawer('${d.id}', event)" 
                    class="terminal-btn py-1 px-2 rounded-[3px] bg-[#202B33] hover:bg-[#30404D] border border-[#30404D] text-[#BFCCD6] hover:text-[#FFFFFF] text-[11px] font-semibold flex items-center justify-center space-x-1 transition cursor-pointer">
              <span class="font-mono">[+]</span>
              <span>QUICK VIEW</span>
            </button>
            <button onclick="event.stopPropagation(); openDonorModal('${d.id}')" 
                    class="terminal-btn py-1 px-2 rounded-[3px] bg-[#202B33] hover:bg-[#137CBD] border border-[#137CBD]/40 hover:border-[#137CBD] text-[#2B95D6] hover:text-[#FFFFFF] text-[11px] font-semibold flex items-center justify-center space-x-1 transition cursor-pointer">
              <span class="font-mono">&gt;&gt;</span>
              <span>DOSSIER</span>
            </button>
          </div>
        </div>
      </div>
    `;
  });
}

function openDonorModal(donorId) {
  const d = DONORS.find(item => item.id === donorId);
  if (!d) {
    console.error('Donor not found for id:', donorId);
    return;
  }

  const titleEl = document.getElementById('donorModalTitle');
  if (titleEl) {
    titleEl.innerText = `DONOR_DOSSIER // ${d.id.toUpperCase()}: ${d.name}`;
  }

  const catObj = CATEGORIES.find(c => c.id === d.cat) || { name: (d.cat || 'GENERAL').toUpperCase() };
  const isLethal = (d.danger || '').toUpperCase().includes('LETHAL');
  const isHigh = (d.danger || '').toUpperCase().includes('HIGH');

  let harvestList = '';
  (d.harvest || []).forEach((h, i) => {
    harvestList += `<li class="text-xs text-[#BFCCD6] font-mono flex items-start space-x-2">
      <span class="text-[#2B95D6] font-bold">0${i+1}.</span>
      <span>${escapeHtml(h)}</span>
    </li>`;
  });

  let toolPills = '';
  (d.tools || ['Standard Hand Tools', 'Multimeter']).forEach(t => {
    toolPills += `<span class="bg-[#182026] text-[#D8E1E8] border border-[#30404D] text-[10px] font-mono px-2 py-0.5 rounded-[2px]">${escapeHtml(t)}</span> `;
  });

  let bpShortcuts = '';
  if (d.blueprints && d.blueprints.length > 0) {
    d.blueprints.forEach(bpNum => {
      const bp = BLUEPRINTS.find(b => b.num === bpNum);
      const bpTitle = bp ? bp.title : `Blueprint ${bpNum}`;
      bpShortcuts += `
        <button onclick="closeDonorModal(); switchView('blueprints'); openBlueprintModal(${bpNum})" 
                class="px-2.5 py-1.5 rounded-[2px] bg-[#11161B] text-[11px] text-[#2B95D6] hover:text-[#F5F8FA] hover:bg-[#137CBD] border border-[#137CBD]/40 font-mono transition text-left flex items-center justify-between">
          <span>BP-${bpNum < 10 ? '0' + bpNum : bpNum}: ${escapeHtml(bpTitle)}</span>
          <span class="text-[10px]">&gt;&gt;</span>
        </button>
      `;
    });
  }

  const body = document.getElementById('donorModalBody');
  if (body) {
    body.innerHTML = `
      <!-- Calibration Telemetry Line -->
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-2 p-3 rounded-[3px] bg-[#202B33] border border-[#30404D] text-xs font-sans">
        <div><span class="text-[#8A9BA8] text-[10px] font-mono">STREAM CATEGORY:</span> <div class="text-[#2B95D6] font-bold font-mono uppercase">${escapeHtml(catObj.name)}</div></div>
        <div><span class="text-[#8A9BA8] text-[10px] font-mono">HAZARD LEVEL:</span> <div class="${isLethal ? 'text-[#F55656]' : (isHigh ? 'text-[#F29D49]' : 'text-[#BFCCD6]')} font-bold font-mono">${escapeHtml(d.danger || 'STANDARD')}</div></div>
        <div><span class="text-[#8A9BA8] text-[10px] font-mono">EXTRACTION DIFFICULTY:</span> <div class="text-[#F5F8FA] font-bold font-mono">${escapeHtml(d.diff || 'Intermediate')}</div></div>
        <div><span class="text-[#8A9BA8] text-[10px] font-mono">EPISTEMIC GATE:</span> <div class="text-[#0F9960] font-bold font-mono">VERIFIED / TYPICAL</div></div>
      </div>

      <!-- Technical Operating Specifications -->
      <div>
        <div class="text-[11px] font-bold text-[#2B95D6] mb-1 font-mono">&gt;&gt; TYPICAL OPERATING SPECIFICATIONS &amp; RATINGS:</div>
        <div class="p-3 rounded-[3px] border border-[#137CBD]/40 border-l-4 border-l-[#2B95D6] bg-[#11161B] text-[#D8E1E8] text-xs font-mono">
          ${escapeHtml(d.specs || 'Variable electromechanical scrap stream [TYPICAL]')}
        </div>
      </div>

      <!-- Recoverable Machine Primitives -->
      <div>
        <div class="text-[11px] font-bold text-[#F29D49] mb-1 font-mono">&gt;&gt; RECOVERABLE MACHINE PRIMITIVES &amp; ASSEMBLIES:</div>
        <ul class="space-y-1.5 p-3 rounded-[3px] bg-[#202B33] border border-[#30404D]">${harvestList}</ul>
      </div>

      <!-- Mechanical & Electrical Interfaces -->
      <div>
        <div class="text-[11px] font-bold text-[#2B95D6] mb-1 font-mono">&gt;&gt; MECHANICAL &amp; ELECTRICAL INTERFACES:</div>
        <div class="p-3 rounded-[3px] bg-[#202B33] border border-[#30404D] text-xs text-[#BFCCD6] font-mono">
          ${escapeHtml(d.interfaces || 'Standard mounting flanges, keyed/splined shafts, and terminal blocks')}
        </div>
      </div>

      <!-- Required Workshop Tools -->
      <div>
        <div class="text-[11px] font-bold text-[#2B95D6] mb-1 font-mono">&gt;&gt; RECOMMENDED NON-DESTRUCTIVE TEARDOWN TOOLS:</div>
        <div class="flex flex-wrap gap-1.5 p-3 rounded-[3px] bg-[#202B33] border border-[#30404D]">${toolPills}</div>
      </div>

      <!-- Multi-Modal Safety Gate -->
      <div class="p-3.5 rounded-[3px] ${isLethal ? 'bg-[#DB3737]/15 border border-[#DB3737]/50' : 'bg-[#D9822B]/15 border border-[#D9822B]/50'} space-y-1">
        <div class="flex items-center space-x-2">
          <span class="px-1.5 py-0.2 rounded-[2px] font-mono font-bold text-[10px] ${isLethal ? 'bg-[#DB3737]/25 text-[#F55656] border border-[#DB3737]' : 'bg-[#D9822B]/25 text-[#F29D49] border border-[#D9822B]'}">[!] DANGER</span>
          <span class="font-bold font-mono text-[11px] ${isLethal ? 'text-[#F55656]' : 'text-[#F29D49]'}">
            CRITICAL EXTRACTION HAZARD &amp; SAFETY GATE:
          </span>
        </div>
        <div class="text-xs text-[#F5F8FA] leading-relaxed">
          <strong>AVOID / MITIGATE:</strong> ${escapeHtml(d.avoid || 'None reported')}
        </div>
        <div class="text-[11px] text-[#BFCCD6] pt-1">
          <strong>FAILURE MODE RISK:</strong> ${escapeHtml(d.hazards || 'General electromechanical workshop hazard')}
        </div>
      </div>

      <!-- Bench Triage Protocol -->
      <div>
        <div class="text-[11px] font-bold text-[#0F9960] mb-1 font-mono">&gt;&gt; BENCH TEST &amp; HEALTH TRIAGE PROTOCOL:</div>
        <div class="p-3.5 rounded-[3px] bg-[#11161B] border border-[#0F9960]/40 border-l-4 border-l-[#0F9960] text-xs text-[#D8E1E8] leading-relaxed font-sans">
          ${escapeHtml(d.triage || 'Perform 4-wire Kelvin resistance measurement and 500V megohmmeter insulation breakdown test before applying power.')}
        </div>
      </div>

      <!-- Repurposing Targets & Compatible Blueprints -->
      <div class="space-y-2">
        <div class="text-[11px] font-bold text-[#2B95D6] font-mono">&gt;&gt; PRIMARY REPURPOSING TARGETS:</div>
        <div class="p-3 rounded-[3px] bg-[#202B33] border border-[#30404D] text-xs text-[#BFCCD6] leading-relaxed">
          ${escapeHtml(d.bestFor || 'Custom robotics, CNC conversions, and rotary power machinery.')}
        </div>

        ${bpShortcuts ? `
        <div class="pt-2">
          <div class="text-[10px] font-mono font-bold text-[#8A9BA8] mb-1.5 uppercase">&gt; DIRECT BLUEPRINT RECIPES UTILIZING THIS DONOR:</div>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">${bpShortcuts}</div>
        </div>
        ` : ''}
      </div>
    `;
  }

  const modal = document.getElementById('donorModal');
  if (modal) {
    modal.classList.remove('hidden');
    modal.style.display = 'flex'; if (modal.style.setProperty) { modal.style.setProperty('display', 'flex', 'important'); }
    document.body.style.overflow = 'hidden';
  }
}

function closeDonorModal() {
  const modal = document.getElementById('donorModal');
  if (modal) {
    modal.classList.add('hidden');
    modal.style.display = 'none'; if (modal.style.setProperty) { modal.style.setProperty('display', 'none', 'important'); }
    document.body.style.overflow = '';
  }
}

function filterAtlas(catId, evt) {
  document.querySelectorAll('.atlas-pill').forEach(p => p.classList.remove('active'));
  const btn = (evt && evt.target && evt.target.classList) ? evt.target : document.querySelector('.atlas-pill');
  if (btn && btn.classList) btn.classList.add('active');

  if (catId === 'all') {
    renderDonors(DONORS);
  } else {
    renderDonors(DONORS.filter(d => d.cat === catId));
  }
}

// ================= 4. SPOTLIGHT COMMAND PALETTE (Ctrl+K) =================
function openSpotlight() {
  const modal = document.getElementById('spotlightModal');
  if (modal) {
    modal.classList.remove('hidden');
    modal.style.display = 'flex'; if (modal.style.setProperty) { modal.style.setProperty('display', 'flex', 'important'); }
    const input = document.getElementById('spotlightInput');
    if (input) {
      input.value = '';
      input.focus();
      handleSpotlightSearch('');
    }
  }
}

function closeSpotlight() {
  const modal = document.getElementById('spotlightModal');
  if (modal) {
    modal.classList.add('hidden');
    modal.style.display = 'none'; if (modal.style.setProperty) { modal.style.setProperty('display', 'none', 'important'); }
  }
}

function handleSpotlightSearch(query) {
  const container = document.getElementById('spotlightResults');
  if (!container) return;
  const q = (query || '').toLowerCase().trim();

  if (q.length < 2) {
    container.innerHTML = `
      <div class="p-6 text-center text-[#8A9BA8] text-xs">
        Type at least 2 characters to search across 15 Volumes, 50 Blueprints, and 100 Donors...
      </div>
    `;
    return;
  }

  const matchedArticles = ARTICLES.filter(a => a.title.toLowerCase().includes(q) || (a.subTitle && a.subTitle.toLowerCase().includes(q))).slice(0, 5);
  const matchedBlueprints = BLUEPRINTS.filter(b => b.title.toLowerCase().includes(q) || b.donor.toLowerCase().includes(q)).slice(0, 5);
  const matchedDonors = DONORS.filter(d => d.name.toLowerCase().includes(q) || (d.harvest && d.harvest.some(h => h.toLowerCase().includes(q)))).slice(0, 5);

  let html = '';

  if (matchedArticles.length > 0) {
    html += `<div class="px-2 py-1 text-[10px] font-mono text-[#2B95D6] font-bold uppercase">&gt;&gt; CHAPTERS &amp; FIELD GUIDES (${matchedArticles.length})</div>`;
    matchedArticles.forEach(a => {
      html += `
        <div onclick="closeSpotlight(); loadArticleById('${a.id}')" 
             class="p-2 rounded-[3px] hover:bg-[#202B33] cursor-pointer flex items-center justify-between group transition">
          <div>
            <div class="font-semibold text-[#F5F8FA] group-hover:text-[#2B95D6] text-xs">${escapeHtml(a.title)}</div>
            <div class="text-[11px] text-[#8A9BA8] truncate max-w-lg">${escapeHtml(a.subTitle)}</div>
          </div>
          <span class="text-[9px] font-mono text-[#2B95D6] bg-[#202B33] px-1.5 py-0.2 rounded-[2px] border border-[#30404D]">${escapeHtml(a.volCode)}</span>
        </div>
      `;
    });
  }

  if (matchedBlueprints.length > 0) {
    html += `<div class="px-2 py-1 text-[10px] font-mono text-[#F29D49] font-bold uppercase mt-1">&gt;&gt; ENGINEERING BLUEPRINTS (${matchedBlueprints.length})</div>`;
    matchedBlueprints.forEach(b => {
      html += `
        <div onclick="closeSpotlight(); switchView('blueprints'); openBlueprintModal(${b.num})" 
             class="p-2 rounded-[3px] hover:bg-[#202B33] cursor-pointer flex items-center justify-between group transition">
          <div>
            <div class="font-semibold text-[#F5F8FA] group-hover:text-[#2B95D6] text-xs">BP-${b.num}: ${escapeHtml(b.title)}</div>
            <div class="text-[11px] text-[#8A9BA8]">DONOR: ${escapeHtml(b.donor)} | POWER: ${escapeHtml(b.power)}</div>
          </div>
          <span class="text-[9px] font-mono text-[#F29D49] bg-[#202B33] px-1.5 py-0.2 rounded-[2px] border border-[#D9822B]/40">${escapeHtml(b.diff)}</span>
        </div>
      `;
    });
  }

  if (matchedDonors.length > 0) {
    html += `<div class="px-2 py-1 text-[10px] font-mono text-[#2B95D6] font-bold uppercase mt-1">&gt;&gt; DONOR HARVEST STREAMS (${matchedDonors.length})</div>`;
    matchedDonors.forEach(d => {
      html += `
        <div onclick="closeSpotlight(); switchView('atlas'); openDonorModal('${d.id}')" 
             class="p-2 rounded-[3px] hover:bg-[#202B33] cursor-pointer flex items-center justify-between group transition">
          <div>
            <div class="font-semibold text-[#F5F8FA] group-hover:text-[#2B95D6] text-xs">${escapeHtml(d.name)}</div>
            <div class="text-[11px] text-[#8A9BA8] truncate max-w-lg">${(d.harvest || []).map(escapeHtml).join(', ')}</div>
          </div>
          <span class="text-[9px] font-mono text-[#8A9BA8] bg-[#202B33] px-1.5 py-0.2 rounded-[2px] border border-[#30404D]">${escapeHtml(d.danger)}</span>
        </div>
      `;
    });
  }

  if (!html) {
    html = `<div class="p-6 text-center text-[#8A9BA8] text-xs">No records matching "${escapeHtml(query)}"</div>`;
  }

  container.innerHTML = html;
}

// Keyboard shortcuts (Cmd+K / Ctrl+K and Escape)
window.addEventListener('keydown', e => {
  if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
    e.preventDefault();
    openSpotlight();
  }
  if (e.key === 'Escape') {
    closeSpotlight();
    closeBlueprintModal();
    closeDonorModal();
    const dm = document.getElementById('downloadModal');
    if (dm && !dm.classList.contains('hidden')) dm.classList.add('hidden');
  }
});

// ================= 5. OFFLINE EXPORTS MODAL =================
function toggleDownloadModal() {
  const m = document.getElementById('downloadModal');
  if (m) m.classList.toggle('hidden');
}

// Global Initialization
window.addEventListener('DOMContentLoaded', () => {
  initEncyclopediaTree();
  initBlueprints();
  initAtlas();
});
"""
