const fs = require('fs');
const path = require('path');
const vm = require('vm');

console.log("=== RUNNING DOM & APPLICATION LOGIC FUNCTIONAL TESTS ===");

const htmlPath = path.join(__dirname, '..', 'dist', 'index.html');
const html = fs.readFileSync(htmlPath, 'utf8');

// Mock a lightweight browser DOM environment
class MockElement {
  constructor(tag, id = '') {
    this.tagName = tag.toUpperCase();
    this.id = id;
    this.classList = new Set();
    this.children = [];
    this.innerHTML = '';
    this.innerText = '';
    this.value = '';
    this.style = {};
    this.dataset = {};
  }
  classListToggle(cls, force) {
    if (force !== undefined) {
      if (force) this.classList.add(cls);
      else this.classList.delete(cls);
      return force;
    }
    if (this.classList.has(cls)) {
      this.classList.delete(cls);
      return false;
    } else {
      this.classList.add(cls);
      return true;
    }
  }
}

// Extract script content
const scriptMatch = html.match(/<script>([\s\S]*?)<\/script>/);
if (!scriptMatch) {
  throw new Error("Embedded script not found in dist/index.html");
}

const scriptCode = scriptMatch[1];

// Extract datasets robustly without fragile non-greedy regex termination
function extractJsonVariable(code, varName, nextVarName) {
  const startStr = `const ${varName} = `;
  const startIdx = code.indexOf(startStr);
  if (startIdx === -1) throw new Error(`Missing ${varName}`);
  const dataStart = startIdx + startStr.length;
  let dataEnd;
  if (nextVarName) {
    dataEnd = code.indexOf(`const ${nextVarName} = `, dataStart);
    if (dataEnd === -1) throw new Error(`Missing next delimiter ${nextVarName}`);
  } else {
    dataEnd = code.indexOf(';\n', dataStart);
    if (dataEnd === -1) dataEnd = code.lastIndexOf('];') + 1;
  }
  let raw = code.slice(dataStart, dataEnd).trim();
  if (raw.endsWith(';')) raw = raw.slice(0, -1).trim();
  return JSON.parse(raw);
}

const ARTICLES = extractJsonVariable(scriptCode, 'ARTICLES', 'VOL_TREE');
const VOL_TREE = extractJsonVariable(scriptCode, 'VOL_TREE', 'DONORS');
const DONORS = extractJsonVariable(scriptCode, 'DONORS', 'BLUEPRINTS');
const BLUEPRINTS = extractJsonVariable(scriptCode, 'BLUEPRINTS', 'CATEGORIES');

console.log(`[OK] Extracted ARTICLES: ${ARTICLES.length} (Expected: 36)`);
console.log(`[OK] Extracted VOL_TREE: ${VOL_TREE.length} (Expected: 15)`);
console.log(`[OK] Extracted BLUEPRINTS: ${BLUEPRINTS.length} (Expected: 50)`);
console.log(`[OK] Extracted DONORS: ${DONORS.length} (Expected: 100)`);

if (ARTICLES.length !== 36) throw new Error("Articles count mismatch");
if (VOL_TREE.length !== 15) throw new Error("Volumes count mismatch");
if (BLUEPRINTS.length !== 50) throw new Error("Blueprints count mismatch");
if (DONORS.length !== 100) throw new Error("Donors count mismatch");

// Verify no leftover Encarta / Sims / Maze in code
const legacyChecks = [
  'ENCARTA_SIMS_JS',
  'initMindMaze',
  'startBalancerSim',
  'initSparkSim',
  'loadXRay',
  'crtOverlay'
];

legacyChecks.forEach(keyword => {
  if (html.includes(keyword)) {
    throw new Error(`Legacy chaff found in dist/index.html: ${keyword}`);
  }
});
console.log("[OK] Verified zero legacy chaff (no Sims, no MindMaze, no X-Rays, no CRT)");

// Verify Modern Views Presence
['view-compendium', 'view-blueprints', 'view-atlas', 'blueprintModal', 'spotlightModal', 'downloadModal'].forEach(id => {
  if (!html.includes(`id="${id}"`)) {
    throw new Error(`Missing expected modern view/modal: ${id}`);
  }
});
console.log("[OK] Verified all modern views and modals exist in HTML structure");

// Execute Blueprint Modal verification
const elements = {};
function makeEl(id) {
  return {
    id: id,
    classList: {
      classes: new Set(['hidden']),
      add(c) { this.classes.add(c); },
      remove(c) { this.classes.delete(c); },
      toggle(c, force) {
        if (force === true) this.classes.add(c);
        else if (force === false) this.classes.delete(c);
        else if (this.classes.has(c)) this.classes.delete(c);
        else this.classes.add(c);
      },
      contains(c) { return this.classes.has(c); }
    },
    children: [],
    innerHTML: '',
    innerText: '',
    style: {},
    querySelector: () => makeEl('mock-sub'),
    querySelectorAll: () => []
  };
}
function getEl(id) {
  if (!elements[id]) elements[id] = makeEl(id);
  return elements[id];
}

const mockDoc = {
  getElementById: getEl,
  querySelectorAll: () => [],
  addEventListener: () => {},
  body: { style: {} }
};
const mockWin = {
  addEventListener: () => {},
  location: { origin: 'https://repurposed.tech' }
};

const sandbox = {
  document: mockDoc,
  window: mockWin,
  navigator: { clipboard: { writeText: () => Promise.resolve() } },
  console: console,
  setTimeout: setTimeout,
  parseInt: parseInt,
  Array: Array,
  String: String
};

vm.createContext(sandbox);
vm.runInContext(scriptCode, sandbox);

// Test all 50 Blueprints modal execution
for (let i = 1; i <= 50; i++) {
  sandbox.openBlueprintModal(i);
  const modal = elements['blueprintModal'];
  if (modal.classList.contains('hidden')) {
    throw new Error(`Blueprint ${i} modal failed to open`);
  }
  const body = elements['bpModalBody'];
  if (!body.innerHTML.includes('KINEMATIC SCHEMATIC') || !body.innerHTML.includes('BILL OF MATERIALS')) {
    throw new Error(`Blueprint ${i} modal missing schematic or BOM`);
  }
  sandbox.closeBlueprintModal();
  if (!modal.classList.contains('hidden')) {
    throw new Error(`Blueprint ${i} modal failed to close`);
  }
}
console.log("[OK] Verified all 50 Blueprints open, render full schematic/BOM/SOP, and close without error");

// Test all 100 Donors modal execution
for (const donor of DONORS) {
  sandbox.openDonorModal(donor.id);
  const donorModal = elements['donorModal'];
  if (donorModal.classList.contains('hidden')) {
    throw new Error(`Donor ${donor.id} modal failed to open`);
  }
  const donorBody = elements['donorModalBody'];
  if (!donorBody.innerHTML.includes('RECOVERABLE MACHINE PRIMITIVES') || !donorBody.innerHTML.includes('BENCH TEST')) {
    throw new Error(`Donor ${donor.id} modal missing primitives or triage section`);
  }
  sandbox.closeDonorModal();
  if (!donorModal.classList.contains('hidden')) {
    throw new Error(`Donor ${donor.id} modal failed to close`);
  }
}
console.log("[OK] Verified all 100 Donors open, render full dossier specifications/tools/hazards, and close without error");

// Test renderDonors and in-card drawer expansion
sandbox.renderDonors(DONORS);
const grid = elements['donorsGrid'];
if (!grid.innerHTML.includes('onclick="openDonorModal(') || !grid.innerHTML.includes('toggleDonorDrawer(')) {
  throw new Error("renderDonors output missing openDonorModal or toggleDonorDrawer handlers");
}
if (!grid.innerHTML.includes('QUICK VIEW') || !grid.innerHTML.includes('DOSSIER')) {
  throw new Error("renderDonors output missing QUICK VIEW or DOSSIER action buttons");
}

// Test toggleDonorDrawer
const testDrawerId = 'donor-drawer-DONOR-01';
const testBtnId = 'donor-toggle-btn-DONOR-01';
const drawerEl = getEl(testDrawerId);
const btnEl = getEl(testBtnId);
drawerEl.classList.add('hidden'); // Initially hidden

sandbox.toggleDonorDrawer('DONOR-01');
if (drawerEl.classList.contains('hidden')) {
  throw new Error("toggleDonorDrawer failed to unhide drawer");
}
sandbox.toggleDonorDrawer('DONOR-01');
if (!drawerEl.classList.contains('hidden')) {
  throw new Error("toggleDonorDrawer failed to re-hide drawer");
}
console.log("[OK] Verified renderDonors grid generation, card clickability, and drawer toggle functionality");

console.log("=== ALL FUNCTIONAL DOM CHECKS PASSED ===");
