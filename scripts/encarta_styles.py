"""
ENCARTA '95 : ELECTROMECHANICA - Stylesheet Module
Museum-grade skeuomorphic luxury styling for the vintage 1995 CD-ROM encyclopedia experience:
- Deep petrol obsidian velour backgrounds
- Gilded brass borders, embossed bevels, and gold foil accents
- Brass corner rivets and skeuomorphic inset displays
- Glowing status LEDs (emerald, amber, ruby)
- CRT scanlines and phosphor bloom
- Responsive custom scrollbars and print typography
"""

ENCARTA_CSS = """
  :root {
    --bg-base: #020b0e;
    --bg-surface: #06181c;
    --bg-panel: #0a252c;
    --bg-panel-dark: #030f13;
    --border-gold: #dfb15b;
    --border-gold-dark: #916a24;
    --border-gold-light: #fef08a;
    --gold-glow: rgba(223, 177, 91, 0.35);
    --cyan-accent: #06b6d4;
    --cyan-glow: rgba(6, 182, 212, 0.4);
    --text-main: #f1f5f9;
    --text-muted: #94a3b8;
  }

  body {
    background-color: var(--bg-base);
    color: var(--text-main);
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
    overflow-x: hidden;
  }

  /* CRT Scanline & Phosphor Overlay */
  .crt-overlay {
    pointer-events: none;
    position: fixed;
    top: 0; left: 0; width: 100vw; height: 100vh;
    background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.3) 50%), 
                linear-gradient(90deg, rgba(255, 0, 0, 0.04), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.04));
    background-size: 100% 3px, 6px 100%;
    z-index: 9999;
    opacity: 0.9;
    transition: opacity 0.3s;
  }
  .crt-off { opacity: 0 !important; }

  /* Gilded Encarta Plaque Header */
  .gold-plaque {
    background: linear-gradient(135deg, #fcedb6 0%, #dfb15b 35%, #b7811e 70%, #fcedb6 100%);
    color: #2b1802;
    text-shadow: 0 1px 0 rgba(255, 255, 255, 0.6);
    box-shadow: 0 4px 12px rgba(0,0,0,0.8), inset 0 1px 0 rgba(255,255,255,0.8), inset 0 -1px 0 rgba(0,0,0,0.4);
    border: 1px solid #ffe494;
  }

  /* 3D Skeuomorphic Windows */
  .encarta-window {
    background: linear-gradient(180deg, #071f25 0%, #041216 100%);
    border: 2px solid #1e5c6b;
    border-top-color: #388e9e;
    border-left-color: #388e9e;
    border-bottom-color: #030d0f;
    border-right-color: #030d0f;
    box-shadow: 0 10px 30px rgba(0,0,0,0.7), inset 1px 1px 0 rgba(255,255,255,0.1);
    position: relative;
  }

  .window-header {
    background: linear-gradient(90deg, #092c34 0%, #175463 50%, #092c34 100%);
    border-bottom: 2px solid var(--border-gold);
    color: #ffd978;
    font-weight: 700;
    letter-spacing: 0.5px;
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.2), 0 2px 4px rgba(0,0,0,0.5);
    position: relative;
  }

  /* Brass Screws / Rivets */
  .rivet {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: radial-gradient(circle at 30% 30%, #ffeaa7, #b8860b 60%, #4a3400);
    box-shadow: inset 0 0 1px rgba(0,0,0,0.9), 1px 1px 2px rgba(0,0,0,0.8);
    position: absolute;
  }
  .rivet.tl { top: 6px; left: 8px; }
  .rivet.tr { top: 6px; right: 8px; }

  /* Beveled CD-ROM Buttons */
  .encarta-btn {
    background: linear-gradient(180deg, #185260 0%, #0c2b33 100%);
    border: 1px solid #2a7c8e;
    border-top-color: #4db3c9;
    border-left-color: #4db3c9;
    border-bottom-color: #030c0e;
    border-right-color: #030c0e;
    box-shadow: 1px 1px 0px rgba(0,0,0,0.6);
    color: #e2e8f0;
    transition: all 0.08s ease;
    cursor: pointer;
    user-select: none;
  }
  .encarta-btn:hover {
    background: linear-gradient(180deg, #206778 0%, #113c47 100%);
    color: #ffffff;
    border-top-color: #6ed0e6;
    border-left-color: #6ed0e6;
  }
  .encarta-btn:active, .encarta-btn.active {
    background: linear-gradient(180deg, #081d22 0%, #164955 100%);
    border-top-color: #030c0e;
    border-left-color: #030c0e;
    border-bottom-color: #4db3c9;
    border-right-color: #4db3c9;
    box-shadow: inset 1px 1px 3px rgba(0,0,0,0.9);
    transform: translateY(1px);
    color: #fef08a;
  }

  /* Volume & Chapter Cards */
  .vol-card {
    background: linear-gradient(180deg, #07232a 0%, #031115 100%);
    border: 1px solid #1a5664;
    transition: all 0.15s ease;
  }
  .vol-card:hover {
    border-color: #dfb15b;
    box-shadow: 0 4px 12px rgba(0,0,0,0.5);
  }
  .vol-card.active-vol {
    border-color: #dfb15b;
    box-shadow: 0 0 12px rgba(223, 177, 91, 0.3);
  }

  .chapter-card {
    background: #05191e;
    border: 1px solid #144652;
    transition: all 0.12s ease;
  }
  .chapter-card:hover {
    background: #0b323c;
    border-color: #38bdf8;
    transform: translateX(2px);
  }
  .chapter-card.active-chapter {
    background: linear-gradient(90deg, #0e3d49 0%, #092329 100%) !important;
    border: 1px solid #dfb15b !important;
    border-left: 4px solid #dfb15b !important;
    box-shadow: 0 0 12px rgba(223, 177, 91, 0.4), inset 1px 1px 0 rgba(255,255,255,0.1);
  }
  .chapter-card.active-chapter .chap-title {
    color: #fef08a !important;
  }
  .chapter-card.active-chapter .chap-sub {
    color: #67e8f9 !important;
  }

  /* Glowing LED Indicators */
  .led {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    display: inline-block;
  }
  .led-green {
    background: #10b981;
    box-shadow: 0 0 8px #10b981;
  }
  .led-amber {
    background: #f59e0b;
    box-shadow: 0 0 8px #f59e0b;
  }
  .led-red {
    background: #ef4444;
    box-shadow: 0 0 8px #ef4444;
  }

  /* Typography for Encyclopedic Articles */
  .article-body h1 { 
    font-size: 1.85rem; 
    font-weight: 800; 
    color: #ffd978; 
    margin-top: 1.5rem; 
    margin-bottom: 1rem; 
    font-family: Georgia, 'Playfair Display', serif; 
    border-bottom: 2px solid #1b6170; 
    padding-bottom: 0.5rem; 
    letter-spacing: -0.5px;
  }
  .article-body h2 { 
    font-size: 1.4rem; 
    font-weight: 700; 
    color: #67e8f9; 
    margin-top: 2.2rem; 
    margin-bottom: 0.9rem; 
    font-family: Georgia, 'Playfair Display', serif; 
    border-left: 4px solid #dfb15b; 
    padding-left: 0.75rem; 
  }
  .article-body h3 { 
    font-size: 1.15rem; 
    font-weight: 700; 
    color: #f1f5f9; 
    margin-top: 1.6rem; 
    margin-bottom: 0.6rem; 
  }
  .article-body h4 { 
    font-size: 1.0rem; 
    font-weight: 600; 
    color: #cbd5e1; 
    margin-top: 1.2rem; 
    margin-bottom: 0.4rem; 
  }
  .article-body p { 
    margin-bottom: 1.2rem; 
    line-height: 1.75; 
    text-align: justify; 
    font-size: 0.94rem; 
    color: #cbd5e1; 
  }
  .article-body ul, .article-body ol { 
    margin-bottom: 1.3rem; 
    padding-left: 1.8rem; 
    font-size: 0.92rem; 
    color: #cbd5e1; 
  }
  .article-body li { margin-bottom: 0.45rem; line-height: 1.6; }
  .article-body pre { 
    background: #02090b; 
    border: 1px solid #164e5b; 
    color: #38bdf8; 
    font-family: 'Consolas', 'JetBrains Mono', monospace; 
    font-size: 0.84rem; 
    padding: 1.1rem; 
    border-radius: 6px; 
    overflow-x: auto; 
    margin-bottom: 1.4rem; 
    line-height: 1.5; 
    box-shadow: inset 0 2px 6px rgba(0,0,0,0.8);
  }
  .article-body code { 
    background: #08242b; 
    color: #67e8f9; 
    padding: 2px 6px; 
    border-radius: 4px; 
    font-family: 'Consolas', monospace; 
    font-size: 0.88em; 
    border: 1px solid #144955; 
  }
  .article-body pre code { background: transparent; padding: 0; border: none; }

  /* Drop Cap for first paragraph of chapter */
  .drop-cap::first-letter {
    font-size: 3.4rem;
    float: left;
    line-height: 0.8;
    margin-right: 0.75rem;
    color: #dfb15b;
    font-family: Georgia, 'Times New Roman', serif;
    font-weight: 900;
    text-shadow: 2px 2px 0px rgba(0,0,0,0.9);
  }

  /* Callout styling */
  .callout { 
    padding: 14px 18px; 
    border-left: 4px solid; 
    border-radius: 0 6px 6px 0; 
    margin-bottom: 20px; 
    font-size: 0.9rem; 
    box-shadow: 0 4px 12px rgba(0,0,0,0.4);
  }
  .callout-note { background: #07252c; border-color: #38bdf8; color: #e0f2fe; }
  .callout-warning { background: #3b0c0c; border-color: #ef4444; color: #fee2e2; }
  .callout-important { background: #3b2809; border-color: #f59e0b; color: #fef3c7; }
  .callout-tip { background: #062b1e; border-color: #10b981; color: #d1fae5; }

  /* Tables */
  .table-container { width: 100%; overflow-x: auto; margin-bottom: 24px; }
  table { width: 100%; border-collapse: collapse; font-size: 0.86rem; }
  th, td { padding: 9px 13px; border: 1px solid #1b6170; text-align: left; }
  th { background: #0b343d; color: #ffd978; font-weight: 700; }
  tr:nth-child(even) { background: rgba(14, 58, 68, 0.45); }

  /* Spinning CD Animation */
  @keyframes spinDisc {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
  }
  .spinning-cd { animation: spinDisc 6s linear infinite; }

  /* Custom Scrollbars */
  ::-webkit-scrollbar { width: 8px; height: 8px; }
  ::-webkit-scrollbar-track { background: #041215; }
  ::-webkit-scrollbar-thumb { background: #164f5d; border-radius: 4px; border: 1px solid #030e10; }
  ::-webkit-scrollbar-thumb:hover { background: #22768a; }

  /* Print Stylesheet */
  @media print {
    .crt-overlay, header, nav, aside, .no-print { display: none !important; }
    body, article, .encarta-window { background: #ffffff !important; color: #000000 !important; border: none !important; }
    .article-body h1, .article-body h2, .article-body h3 { color: #000000 !important; }
    .article-body p, .article-body li { color: #222222 !important; }
  }
"""
