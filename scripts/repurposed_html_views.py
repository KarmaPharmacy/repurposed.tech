"""
REPURPOSED.TECH : THE MAKER'S BIBLE - Palantir Layout & Views Module
Industrial Field-Engineering Console (Palantir Foundry / Blueprint UI Design System)
- Strict panel hierarchy: Page (#182026) -> Section (#202B33) -> Widget (#293742) -> Inset (#11161B)
- Blueprint core semantic intent colors: Blue (#137CBD), Green (#0F9960), Orange (#D9822B), Red (#DB3737)
- Compact controls (3px radius), dense technical documents, searchable telemetry
- Obsidian technical knowledge-base tree and command-palette (Ctrl+K)
- Linear-inspired dark-surface interactions
- Prominent multi-modal safety warnings (never relying on color alone)
"""

REPURPOSED_HTML = """
<!-- Palantir Operational Console Container -->
<div class="min-h-screen flex flex-col bg-[#182026] text-[#BFCCD6]">

  <!-- Top Operational Control Bar (Header) -->
  <header class="bg-[#202B33] border-b border-[#30404D] px-4 py-2.5 sticky top-0 z-40">
    <div class="max-w-[1760px] mx-auto flex flex-wrap items-center justify-between gap-3">
      
      <!-- Left Hardware ID & Annunciators -->
      <div class="flex items-center space-x-3">
        <div class="flex items-center space-x-1.5 px-2 py-1 rounded-[3px] bg-[#182026] border border-[#30404D]">
          <span class="led active-green"></span>
          <span class="text-[10px] font-mono text-[#15B371] font-bold tracking-wider">ONLINE</span>
        </div>

        <div class="flex flex-col">
          <div class="flex items-center space-x-2">
            <span class="text-sm md:text-base font-bold text-[#F5F8FA] tracking-wide">REPURPOSED</span>
            <span class="text-[10px] font-mono text-[#2B95D6] px-1.5 py-0.2 rounded-[2px] bg-[#182026] border border-[#137CBD]/40 font-bold">TECH</span>
            <span class="text-[11px] font-mono text-[#8A9BA8] hidden sm:inline-block">// OPERATIONAL CONSOLE</span>
          </div>
          <span class="text-[10px] text-[#5C7080] font-sans tracking-wide hidden md:block">
            ELECTROMECHANICAL SALVAGE &amp; KINEMATIC FIELD WORKSTATION
          </span>
        </div>
      </div>

      <!-- Center Function Bus (Channel Switcher Tabs) -->
      <nav class="flex items-center gap-1 bg-[#182026] border border-[#30404D] p-1 rounded-[3px]">
        <button onclick="switchView('compendium')" id="tab-compendium" 
                class="terminal-btn active">
          <span class="led active-blue"></span>
          <span>CH-1: COMPENDIUM</span>
        </button>
        <button onclick="switchView('blueprints')" id="tab-blueprints" 
                class="terminal-btn">
          <span class="led"></span>
          <span>CH-2: BLUEPRINTS</span>
          <span class="text-[9px] font-mono px-1 rounded bg-[#202B33] text-[#8A9BA8]" id="tabBlueprintsBadge">50</span>
        </button>
        <button onclick="switchView('atlas')" id="tab-atlas" 
                class="terminal-btn">
          <span class="led"></span>
          <span>CH-3: SCRAP ATLAS</span>
          <span class="text-[9px] font-mono px-1 rounded bg-[#202B33] text-[#8A9BA8]" id="tabAtlasBadge">100</span>
        </button>
      </nav>

      <!-- Right Instrument Cluster: Prompt & Direct Exports -->
      <div class="flex items-center space-x-2">
        <!-- Command Prompt Search Trigger (Obsidian / Linear Style) -->
        <button onclick="openSpotlight()" 
                class="hidden sm:flex items-center space-x-2 bg-[#182026] border border-[#30404D] hover:border-[#137CBD] text-[#8A9BA8] hover:text-[#F5F8FA] px-2.5 py-1 rounded-[3px] text-xs transition">
          <span class="text-[#2B95D6] font-bold">&gt;</span>
          <span class="text-[11px]">QUERY_PROMPT</span>
          <kbd class="font-mono text-[9px] bg-[#202B33] text-[#BFCCD6] border border-[#30404D] px-1 rounded-[2px]">Ctrl K</kbd>
        </button>

        <!-- Reader Mode Direct Link -->
        <a href="/ebook.html" target="_blank" 
           class="terminal-btn text-[11px] py-1 px-2.5 border-[#30404D] hover:border-[#137CBD] text-[#BFCCD6]" 
           title="Standalone Reading Room">
          <span>[ READER ]</span>
        </a>

        <!-- Export Vault Modal Trigger -->
        <button onclick="toggleDownloadModal()" 
                class="terminal-btn text-[11px] py-1 px-2.5 bg-[#202B33] border-[#30404D] text-[#BFCCD6] hover:bg-[#293742] hover:text-[#F5F8FA]">
          <span>[ EXPORTS ]</span>
        </button>

        <!-- Mobile Drawer Toggle -->
        <button onclick="toggleMobileSidebar()" class="lg:hidden p-1 rounded-[3px] bg-[#182026] border border-[#30404D] text-[#BFCCD6]">
          <span class="font-bold text-xs">[MENU]</span>
        </button>
      </div>

    </div>
  </header>

  <!-- Main Analytical Workspace Frame -->
  <main class="max-w-[1760px] w-full mx-auto p-2 sm:p-4 flex-1">

    <!-- ================= CHANNEL 1: COMPENDIUM WORKSTATION ================= -->
    <section id="view-compendium" class="space-y-4">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-4 items-start">
        
        <!-- TECHNICAL KNOWLEDGE-BASE DIRECTORY (Left Sidebar, 4 Cols) -->
        <aside id="atlasSidebar" class="bg-[#202B33] border border-[#30404D] rounded-[4px] lg:col-span-4 max-h-[88vh] flex flex-col overflow-hidden sticky top-16 shadow-sm">
          
          <!-- Bus Header & Grep Search -->
          <div class="p-3 border-b border-[#30404D] bg-[#202B33] space-y-2">
            <div class="flex items-center justify-between text-xs font-sans">
              <span class="text-[#F5F8FA] font-bold tracking-wide flex items-center gap-1.5">
                <span class="text-[#2B95D6] font-mono">&gt;&gt;</span>
                <span>TECHNICAL COMPENDIUM (15 VOLUMES)</span>
              </span>
              <span id="atlasMatchCount" class="text-[10px] font-mono px-1.5 py-0.5 rounded-[2px] bg-[#182026] text-[#2B95D6] border border-[#30404D]">
                36 CHANNELS
              </span>
            </div>

            <!-- Grep Input (Obsidian style) -->
            <div class="relative">
              <input type="text" id="atlasSearchInput" onkeyup="filterAtlasTree(this.value)" 
                     placeholder="Filter chapters, motors, hazards..." 
                     class="w-full bg-[#182026] border border-[#30404D] rounded-[3px] px-2.5 py-1 text-xs text-[#F5F8FA] placeholder-[#5C7080] focus:outline-none focus:border-[#137CBD]">
              <button onclick="document.getElementById('atlasSearchInput').value=''; filterAtlasTree('')" 
                      class="absolute right-2 top-1 text-[#5C7080] hover:text-[#BFCCD6] text-xs font-mono">[CLR]</button>
            </div>

            <!-- Tree Bus Controls -->
            <div class="flex items-center justify-between text-[11px] text-[#8A9BA8] pt-0.5 font-sans">
              <div class="flex items-center space-x-2">
                <button onclick="expandAllVolumes()" class="hover:text-[#F5F8FA] transition cursor-pointer">[+ Expand All]</button>
                <span>|</span>
                <button onclick="collapseAllVolumes()" class="hover:text-[#F5F8FA] transition cursor-pointer">[- Collapse All]</button>
              </div>
              <span class="text-[10px] font-mono text-[#5C7080]">NAV // DENSE</span>
            </div>
          </div>

          <!-- Volume Groups Scrollable Container -->
          <div class="flex-1 overflow-y-auto p-2 space-y-1.5 bg-[#182026]" id="atlasTreeContainer">
            <!-- Injected via JavaScript -->
          </div>

        </aside>

        <!-- MAIN CALIBRATION & OPERATIONS MONITOR (Right Content Frame, 8 Cols) -->
        <article class="bg-[#293742] border border-[#30404D] rounded-[4px] lg:col-span-8 flex flex-col min-h-[88vh] overflow-hidden shadow-sm">
          
          <!-- Monitor Channel Telemetry Header -->
          <div class="p-4 md:p-5 border-b border-[#30404D] bg-[#202B33] space-y-3 relative" id="articleHeroBanner">
            
            <div class="flex flex-wrap items-center justify-between gap-2 text-xs">
              <div class="flex items-center gap-2">
                <span id="articleCatIcon" class="text-base">⚡</span>
                <span id="articleVolBadge" class="text-xs font-mono font-bold text-[#2B95D6] bg-[#182026] border border-[#137CBD]/40 px-2 py-0.5 rounded-[2px]">
                  VOL-00 // FOUNDATIONS
                </span>
                <span id="articleHazardFlag" class="text-[10px] font-mono font-bold uppercase px-2 py-0.5 rounded-[2px] bg-[#DB3737]/15 text-[#F55656] border border-[#DB3737]/50 hidden">
                  [!] CRITICAL HAZARD HOTSPOT
                </span>
              </div>

              <!-- Section Dropdown Jump -->
              <div class="flex items-center space-x-2">
                <select id="sectionSelect" onchange="jumpToSection(this.value)" 
                        class="bg-[#182026] border border-[#30404D] text-[#BFCCD6] text-xs rounded-[3px] px-2 py-1 focus:outline-none focus:border-[#137CBD] max-w-[220px] truncate">
                  <option value="">Jump to section...</option>
                </select>
              </div>
            </div>

            <!-- Chapter Heading -->
            <h1 id="articleHeading" class="text-xl md:text-2xl font-bold text-[#F5F8FA] tracking-tight leading-snug">
              INITIALIZING WORKSTATION...
            </h1>

            <!-- Technical Summary Callout -->
            <div id="articleSubLabel" class="text-xs md:text-sm text-[#8A9BA8] leading-relaxed border-l-2 border-[#137CBD] pl-3 bg-[#182026] p-2 rounded-r-[3px]">
              Awaiting channel selection.
            </div>

            <!-- Channel Telemetry Line -->
            <div class="flex flex-wrap items-center justify-between text-xs pt-2 border-t border-[#30404D] text-[#8A9BA8] font-mono gap-2">
              <div class="flex items-center space-x-3">
                <span>EST_READ: <span id="articleReadTime" class="text-[#F5F8FA] font-bold">--</span></span>
                <span>|</span>
                <span>LENGTH: <span id="articleWords" class="text-[#BFCCD6]">--</span> WORDS</span>
              </div>
              <div class="flex items-center space-x-2">
                <span id="articleCounter" class="text-[#F29D49] font-bold">CH 1 OF 36</span>
                <button onclick="copyCurrentChapterLink()" class="px-2 py-0.5 rounded-[2px] bg-[#182026] text-[#BFCCD6] hover:text-[#F5F8FA] border border-[#30404D] text-[10px] transition cursor-pointer">
                  [COPY URL]
                </button>
              </div>
            </div>

          </div>

          <!-- Unabridged Documentation Body -->
          <div id="articleContent" class="p-5 md:p-8 flex-1 overflow-y-auto terminal-prose max-w-full bg-[#293742]">
            <!-- Unabridged HTML injected here -->
          </div>

          <!-- Bottom Channel Pager -->
          <div class="p-3 border-t border-[#30404D] bg-[#202B33] flex items-center justify-between text-xs font-sans">
            <button id="btnPrevArticle" onclick="navigateArticle(-1)" 
                    class="terminal-btn text-xs py-1 px-3 disabled:opacity-30 disabled:pointer-events-none">
              <span>&larr; Previous Chapter</span>
            </button>
            
            <button onclick="window.scrollTo({top: 0, behavior: 'smooth'})" class="text-[11px] text-[#8A9BA8] hover:text-[#F5F8FA] transition cursor-pointer">
              Top of Document &uarr;
            </button>

            <button id="btnNextArticle" onclick="navigateArticle(1)" 
                    class="terminal-btn text-xs py-1 px-3 disabled:opacity-30 disabled:pointer-events-none">
              <span>Next Chapter &rarr;</span>
            </button>
          </div>

        </article>

      </div>
    </section>

    <!-- ================= CHANNEL 2: 50 ENGINEERING BLUEPRINTS ================= -->
    <section id="view-blueprints" class="space-y-4 hidden">
      <!-- Filter & Telemetry Console -->
      <div class="bg-[#202B33] border border-[#30404D] p-4 rounded-[4px] flex flex-wrap items-center justify-between gap-4">
        <div>
          <div class="flex items-center space-x-2">
            <span class="text-[#2B95D6] font-bold text-base font-mono">&gt;&gt;</span>
            <h2 class="text-base md:text-lg font-bold text-[#F5F8FA] tracking-wide">
              ENGINEERING BLUEPRINTS REPOSITORY (<span id="blueprintsHeaderCount" class="text-[#2B95D6]">50</span> BUILDS)
            </h2>
          </div>
          <p class="text-xs text-[#8A9BA8] mt-0.5">
            Operational fabrication dossiers: Kinematic Schematics, Bill of Materials, Wiring Pinouts, and SOP Execution Steps.
          </p>
        </div>
        
        <!-- Filter Button Group (Palantir style) -->
        <div class="flex flex-wrap gap-1" id="blueprintFilters">
          <button onclick="filterBlueprints('all')" class="terminal-btn active bp-filter-btn" id="bpAllFilterBtn">[ALL: 50]</button>
          <button onclick="filterBlueprints('power')" class="terminal-btn bp-filter-btn">[POWER &amp; GEN]</button>
          <button onclick="filterBlueprints('machine')" class="terminal-btn bp-filter-btn">[MACHINE TOOLS]</button>
          <button onclick="filterBlueprints('optics')" class="terminal-btn bp-filter-btn">[MICRO-OPTICS]</button>
          <button onclick="filterBlueprints('mobility')" class="terminal-btn bp-filter-btn">[TRACTION &amp; ROVERS]</button>
        </div>
      </div>

      <!-- Blueprints Grid (Palantir Widget Cards) -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4" id="blueprintsGrid">
        <!-- Injected via JavaScript -->
      </div>
    </section>

    <!-- ================= CHANNEL 3: 100 DONOR STREAMS SCRAP ATLAS ================= -->
    <section id="view-atlas" class="space-y-4 hidden">
      <!-- Header Filter Console -->
      <div class="bg-[#202B33] border border-[#30404D] p-4 rounded-[4px] flex flex-wrap items-center justify-between gap-4">
        <div>
          <div class="flex items-center space-x-2">
            <span class="text-[#2B95D6] font-bold text-base font-mono">&gt;&gt;</span>
            <h2 class="text-base md:text-lg font-bold text-[#F5F8FA] tracking-wide">
              SALVAGE HARVEST TELEMETRY MATRIX (<span id="atlasHeaderCount" class="text-[#2B95D6]">100</span> DONOR STREAMS)
            </h2>
          </div>
          <p class="text-xs text-[#8A9BA8] mt-0.5">
            Field extraction triage matrix across automotive, consumer, domestic mains, and industrial equipment.
          </p>
        </div>
        
        <!-- Category Filter Pills -->
        <div class="flex flex-wrap gap-1" id="atlasFilterPills">
          <!-- Injected via JavaScript -->
        </div>
      </div>

      <!-- Donors Matrix Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4" id="donorsGrid">
        <!-- Injected via JavaScript -->
      </div>
    </section>

  </main>

  <!-- ================= PALANTIR MODALS & COMMAND PROMPTS ================= -->

  <!-- 1. Blueprint Dossier Modal (Bench Schematic Viewer) -->
  <div id="blueprintModal" class="fixed inset-0 bg-[#182026]/85 backdrop-blur-sm z-50 flex items-center justify-center p-3 md:p-6 hidden" onclick="if(event.target === this) closeBlueprintModal()">
    <div class="modal-dialog-box bg-[#293742] max-w-4xl w-full max-h-[92vh] flex flex-col shadow-2xl border border-[#30404D] rounded-[4px] overflow-hidden">
      
      <!-- Modal Header -->
      <div class="px-4 py-3 border-b border-[#30404D] bg-[#202B33] flex items-center justify-between">
        <div class="flex items-center space-x-2">
          <span class="led active-blue"></span>
          <span id="bpModalTitle" class="font-bold text-sm md:text-base text-[#F5F8FA]">SPEC_DOSSIER // LOADED</span>
        </div>
        <button onclick="closeBlueprintModal()" class="terminal-btn text-xs py-1 px-2.5 text-[#F55656] border-[#DB3737]/40 hover:border-[#DB3737] hover:bg-[#DB3737]/15">[ESC: CLOSE]</button>
      </div>

      <!-- Modal Content Body -->
      <div class="p-5 overflow-y-auto space-y-5 flex-1 terminal-prose text-xs bg-[#293742]" id="bpModalBody">
        <!-- Injected via JavaScript -->
      </div>

      <!-- Modal Footer -->
      <div class="px-4 py-2.5 border-t border-[#30404D] bg-[#202B33] flex items-center justify-between text-xs text-[#8A9BA8] font-mono">
        <span>REPURPOSED.TECH // BENCH SPECIFICATION ARCHIVE</span>
        <button onclick="closeBlueprintModal()" class="terminal-btn py-1 px-3 text-xs">[DONE]</button>
      </div>
    </div>
  </div>

  <!-- 2. Donor Dossier Modal (Scrap Stream Inspection Viewer) -->
  <div id="donorModal" class="fixed inset-0 bg-[#182026]/85 backdrop-blur-sm z-50 flex items-center justify-center p-3 md:p-6 hidden" onclick="if(event.target === this) closeDonorModal()">
    <div class="modal-dialog-box bg-[#293742] max-w-4xl w-full max-h-[92vh] flex flex-col shadow-2xl border border-[#30404D] rounded-[4px] overflow-hidden">

      <!-- Modal Header -->
      <div class="px-4 py-3 border-b border-[#30404D] bg-[#202B33] flex items-center justify-between">
        <div class="flex items-center space-x-2">
          <span class="led active-amber"></span>
          <span id="donorModalTitle" class="font-bold text-sm md:text-base text-[#F5F8FA] font-mono">DONOR_DOSSIER // LOADED</span>
        </div>
        <button onclick="closeDonorModal()" class="terminal-btn text-xs py-1 px-2.5 text-[#F55656] border-[#DB3737]/40 hover:border-[#DB3737] hover:bg-[#DB3737]/15">[ESC: CLOSE]</button>
      </div>

      <!-- Modal Content Body -->
      <div class="p-5 overflow-y-auto space-y-5 flex-1 terminal-prose text-xs bg-[#293742]" id="donorModalBody">
        <!-- Injected via JavaScript -->
      </div>

      <!-- Modal Footer -->
      <div class="px-4 py-2.5 border-t border-[#30404D] bg-[#202B33] flex items-center justify-between text-xs text-[#8A9BA8] font-mono">
        <span>REPURPOSED.TECH // HARVEST TRIAGE &amp; SPECIFICATION ARCHIVE</span>
        <button onclick="closeDonorModal()" class="terminal-btn py-1 px-3 text-xs">[DONE]</button>
      </div>
    </div>
  </div>

  <!-- 3. Spotlight Command Palette (Obsidian / Linear Style Ctrl+K) -->
  <div id="spotlightModal" class="fixed inset-0 bg-[#182026]/85 backdrop-blur-sm z-50 flex items-start justify-center p-4 pt-16 md:pt-24 hidden" onclick="if(event.target === this) closeSpotlight()">
    <div class="modal-dialog-box bg-[#293742] max-w-2xl w-full shadow-2xl border border-[#30404D] rounded-[4px] overflow-hidden flex flex-col">
      <!-- Prompt Search Bar -->
      <div class="p-3 border-b border-[#30404D] flex items-center space-x-2.5 bg-[#202B33]">
        <span class="text-[#2B95D6] font-bold text-base font-mono">&gt;</span>
        <input type="text" id="spotlightInput" onkeyup="handleSpotlightSearch(this.value)" 
               placeholder="Search chapters, blueprints, motors, components, hazards..." 
               class="w-full bg-transparent text-sm text-[#F5F8FA] placeholder-[#5C7080] focus:outline-none">
        <kbd class="text-[9px] bg-[#182026] text-[#BFCCD6] border border-[#30404D] px-1.5 py-0.5 rounded-[2px] font-mono">ESC</kbd>
      </div>

      <!-- Prompt Results List -->
      <div id="spotlightResults" class="max-h-[60vh] overflow-y-auto p-2 space-y-1 divide-y divide-[#30404D] text-xs bg-[#182026]">
        <div class="p-6 text-center text-[#8A9BA8]">
          Type at least 2 characters to search across 15 Volumes, 50 Blueprints, and 100 Donors...
        </div>
      </div>
    </div>
  </div>

  <!-- 3. Offline Exports Vault Modal -->
  <div id="downloadModal" class="fixed inset-0 bg-[#182026]/85 backdrop-blur-sm z-50 flex items-center justify-center p-4 hidden" onclick="if(event.target === this) toggleDownloadModal()">
    <div class="modal-dialog-box bg-[#293742] max-w-lg w-full p-5 space-y-4 shadow-2xl border border-[#30404D] rounded-[4px]">
      <div class="flex items-center justify-between border-b border-[#30404D] pb-2.5">
        <div class="flex items-center space-x-2">
          <span class="led active-green"></span>
          <h3 class="font-bold text-sm text-[#F5F8FA]">EXPORTS // OFFLINE EDITIONS</h3>
        </div>
        <button onclick="toggleDownloadModal()" class="text-[#8A9BA8] hover:text-[#F5F8FA] text-sm cursor-pointer">[X]</button>
      </div>

      <p class="text-xs text-[#8A9BA8] leading-relaxed">
        Download complete uncompressed binary and text manuscripts for off-grid reading terminals:
      </p>

      <div class="space-y-2">
        <!-- EPUB -->
        <a href="/downloads/the-makers-bible-of-electromechanical-salvage.epub" download 
           class="block p-3 rounded-[3px] bg-[#202B33] border border-[#30404D] hover:border-[#137CBD] hover:bg-[#293742] transition text-xs">
          <div class="flex items-center justify-between font-bold text-[#F5F8FA]">
            <span>[1] STANDARD EPUB 3 READER EDITION</span>
            <span class="text-[10px] font-mono text-[#8A9BA8]">295 KB</span>
          </div>
          <p class="text-[11px] text-[#8A9BA8] mt-0.5">Compatible with Apple Books, Kindle, Kobo, and mobile readers.</p>
        </a>

        <!-- Markdown -->
        <a href="/downloads/the-makers-bible-of-electromechanical-salvage.md" download 
           class="block p-3 rounded-[3px] bg-[#202B33] border border-[#30404D] hover:border-[#137CBD] hover:bg-[#293742] transition text-xs">
          <div class="flex items-center justify-between font-bold text-[#F5F8FA]">
            <span>[2] MASTER MARKDOWN MANUSCRIPT (.MD)</span>
            <span class="text-[10px] font-mono text-[#8A9BA8]">672 KB</span>
          </div>
          <p class="text-[11px] text-[#8A9BA8] mt-0.5">Complete raw text for Obsidian, local vector embeddings, or offline indexing.</p>
        </a>

        <!-- Compendium Matrix -->
        <a href="/downloads/salvage-compendium.md" download 
           class="block p-3 rounded-[3px] bg-[#202B33] border border-[#30404D] hover:border-[#137CBD] hover:bg-[#293742] transition text-xs">
          <div class="flex items-center justify-between font-bold text-[#F5F8FA]">
            <span>[3] QUICK-REFERENCE SCRAP MATRIX (.MD)</span>
            <span class="text-[10px] font-mono text-[#8A9BA8]">79 KB</span>
          </div>
          <p class="text-[11px] text-[#8A9BA8] mt-0.5">Multi-attribute field tables covering 100 Donors &amp; 50 Blueprints.</p>
        </a>

        <!-- Standalone Reader HTML -->
        <a href="/ebook.html" target="_blank" 
           class="block p-3 rounded-[3px] bg-[#202B33] border border-[#30404D] hover:border-[#137CBD] hover:bg-[#293742] transition text-xs">
          <div class="flex items-center justify-between font-bold text-[#F5F8FA]">
            <span>[4] STANDALONE WEB READER EDITION</span>
            <span class="text-[10px] font-mono text-[#8A9BA8]">HTML</span>
          </div>
          <p class="text-[11px] text-[#8A9BA8] mt-0.5">Single-file zero-dependency reading room with print-to-PDF formatting.</p>
        </a>
      </div>

      <div class="pt-2 text-center">
        <button onclick="toggleDownloadModal()" class="terminal-btn w-full justify-center">
          [CLOSE WINDOW]
        </button>
      </div>
    </div>
  </div>

  <!-- Operational Footer Bar -->
  <footer class="border-t border-[#30404D] bg-[#202B33] py-3.5 px-6 text-center text-xs text-[#8A9BA8] font-sans mt-8">
    <div class="flex flex-wrap items-center justify-center gap-3">
      <span class="text-[#F5F8FA] font-bold">REPURPOSED.TECH</span>
      <span>|</span>
      <span>ELECTROMECHANICAL SALVAGE SPECIFICATION MANUAL</span>
      <span>|</span>
      <span>15 VOLUMES &bull; 36 CHAPTERS &bull; 50 BLUEPRINTS &bull; 100 DONOR STREAMS</span>
      <span>|</span>
      <span class="text-[#15B371] font-mono">[●] ALL SYSTEMS OPERATIONAL</span>
    </div>
  </footer>

</div>
"""
