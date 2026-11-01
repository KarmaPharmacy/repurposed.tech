"""
Production Build & Staging Pipeline for repurposed.tech
Compiles and packages the REPURPOSED Laboratory Instrument Console into dist/
ready for immediate deployment to Cloudflare Pages, Vercel, Netlify, Firebase,
or GitHub Pages.
"""

import os
import sys
import shutil
import subprocess
import struct
import zlib
from datetime import datetime

WORKSPACE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DIST_DIR = os.path.join(WORKSPACE, "dist")
ASSETS_DIR = os.path.join(DIST_DIR, "assets")
DOWNLOADS_DIR = os.path.join(DIST_DIR, "downloads")

DOMAIN = "https://repurposed.tech"

def log(msg):
    print(f"[PROD BUILD] {msg}")

def ensure_fresh_compilation():
    log("Rebuilding master eBook and REPURPOSED terminal suite...")
    subprocess.run([sys.executable, os.path.join(WORKSPACE, "scripts", "build_ebook.py")], check=True)
    subprocess.run([sys.executable, os.path.join(WORKSPACE, "scripts", "generate_encarta_suite.py")], check=True)

def setup_directories():
    log(f"Preparing output directory: {DIST_DIR}")
    if os.path.exists(DIST_DIR):
        shutil.rmtree(DIST_DIR)
    os.makedirs(DIST_DIR, exist_ok=True)
    os.makedirs(ASSETS_DIR, exist_ok=True)
    os.makedirs(DOWNLOADS_DIR, exist_ok=True)

def generate_png(filename, width=180, height=180, is_banner=False):
    """Generates a valid RGBA PNG using standard library zlib."""
    raw_data = bytearray()
    
    if is_banner:
        # 1200x630 banner in Phosphorescent Green Terminal Theme
        for y in range(height):
            raw_data.append(0) # filter byte: None
            for x in range(width):
                # Border frame
                if x < 4 or x > width - 5 or y < 4 or y > height - 5:
                    raw_data.extend([74, 222, 128, 255]) # Green #4ade80
                elif x < 8 or x > width - 9 or y < 8 or y > height - 9:
                    raw_data.extend([5, 9, 6, 255])
                elif x < 12 or x > width - 13 or y < 12 or y > height - 13:
                    raw_data.extend([30, 51, 37, 255])
                else:
                    # CRT Oscilloscope background grid
                    if (x % 40 == 0) or (y % 40 == 0):
                        raw_data.extend([15, 30, 20, 255])
                    else:
                        dx = (x - width / 2) / (width / 2)
                        dy = (y - height / 2) / (height / 2)
                        dist = (dx*dx + dy*dy)**0.5
                        g = max(9, int(22 - 12 * dist))
                        raw_data.extend([5, g, 7, 255])
    else:
        # Palantir Operational Console Icon (Blueprint Blue on Dark Gray)
        for y in range(height):
            raw_data.append(0) # filter byte: None
            for x in range(width):
                dx = x - width / 2
                dy = y - height / 2
                dist = (dx*dx + dy*dy)**0.5
                if dist > (width / 2 - 4):
                    # Background: #182026
                    raw_data.extend([24, 32, 38, 255])
                elif dist > (width / 2 - 12):
                    # Outer Blueprint Blue Rim: #137CBD
                    raw_data.extend([19, 124, 189, 255])
                elif dist < (width * 0.14):
                    # Center Core: #11161B
                    raw_data.extend([17, 22, 27, 255])
                elif dist < (width * 0.22):
                    # Bright Ring: #48AFF0
                    raw_data.extend([72, 175, 240, 255])
                else:
                    # Subtle Blueprint Blue gradient
                    val = int(70 + 80 * (1.0 - (dist / (width / 2))))
                    val = max(30, min(210, val))
                    raw_data.extend([int(val * 0.2), int(val * 0.65), val, 255])

    def chunk(tag, data):
        return struct.pack('>I', len(data)) + tag + data + struct.pack('>I', zlib.crc32(tag + data) & 0xffffffff)

    sig = b'\x89PNG\r\n\x1a\n'
    ihdr_data = struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0)
    ihdr = chunk(b'IHDR', ihdr_data)
    idat = chunk(b'IDAT', zlib.compress(bytes(raw_data), 9))
    iend = chunk(b'IEND', b'')

    with open(filename, 'wb') as f:
        f.write(sig + ihdr + idat + iend)

def generate_ico(filename):
    """Generates a valid 32x32 binary ICO."""
    width, height = 32, 32
    pixels = []
    for y in range(height):
        row = []
        for x in range(width):
            dx = x - 15.5
            dy = y - 15.5
            dist = (dx*dx + dy*dy)**0.5
            if dist > 15:
                row.append((0, 0, 0, 0)) # transparent
            elif dist > 13:
                row.append((189, 124, 19, 255)) # Blueprint Blue rim: BGRA
            elif dist < 4:
                row.append((27, 22, 17, 255)) # dark core
            elif dist < 6:
                row.append((240, 175, 72, 255)) # light blue ring
            else:
                val = int(100 + 70 * (1.0 - (dist / 16)))
                val = max(30, min(200, val))
                row.append((val, int(val * 0.65), int(val * 0.15), 255))
        pixels.append(row)

    bmp_data = bytearray()
    for row in reversed(pixels):
        for b, g, r, a in row:
            bmp_data.extend([b, g, r, a])

    and_mask = bytearray((width * height) // 8)
    header_size = 40
    img_size = header_size + len(bmp_data) + len(and_mask)
    bmp_header = struct.pack('<IIIHHIIIIII', 40, width, height * 2, 1, 32, 0, len(bmp_data), 0, 0, 0, 0)
    ico_header = struct.pack('<HHH', 0, 1, 1)
    offset = 6 + 16
    ico_entry = struct.pack('<BBBBHHII', width, height, 0, 0, 1, 32, img_size, offset)

    with open(filename, 'wb') as f:
        f.write(ico_header)
        f.write(ico_entry)
        f.write(bmp_header)
        f.write(bmp_data)
        f.write(and_mask)

def generate_svg_assets():
    log("Creating Palantir operational vector branding assets...")
    favicon_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <defs>
    <radialGradient id="beam" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#48AFF0"/>
      <stop offset="60%" stop-color="#2B95D6"/>
      <stop offset="100%" stop-color="#137CBD"/>
    </radialGradient>
  </defs>
  <rect width="64" height="64" rx="4" fill="#182026" stroke="#30404D" stroke-width="2"/>
  <circle cx="32" cy="32" r="22" fill="none" stroke="#293742" stroke-width="1.5" stroke-dasharray="3,3"/>
  <line x1="32" y1="10" x2="32" y2="54" stroke="#30404D" stroke-width="1.5"/>
  <line x1="10" y1="32" x2="54" y2="32" stroke="#30404D" stroke-width="1.5"/>
  <circle cx="32" cy="32" r="14" fill="url(#beam)"/>
  <circle cx="32" cy="32" r="6" fill="#182026" stroke="#48AFF0" stroke-width="1.5"/>
</svg>"""
    with open(os.path.join(DIST_DIR, "favicon.svg"), "w", encoding="utf-8") as f:
        f.write(favicon_svg)

    og_card_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#202B33"/>
      <stop offset="50%" stop-color="#182026"/>
      <stop offset="100%" stop-color="#11161B"/>
    </linearGradient>
  </defs>

  <!-- Background Surface -->
  <rect width="1200" height="630" fill="url(#bgGrad)"/>

  <!-- Subtle Analytical Grid -->
  <g stroke="#293742" stroke-width="1">
    <line x1="0" y1="105" x2="1200" y2="105"/>
    <line x1="0" y1="210" x2="1200" y2="210"/>
    <line x1="0" y1="315" x2="1200" y2="315"/>
    <line x1="0" y1="420" x2="1200" y2="420"/>
    <line x1="0" y1="525" x2="1200" y2="525"/>
    <line x1="200" y1="0" x2="200" y2="630"/>
    <line x1="400" y1="0" x2="400" y2="630"/>
    <line x1="600" y1="0" x2="600" y2="630"/>
    <line x1="800" y1="0" x2="800" y2="630"/>
    <line x1="1000" y1="0" x2="1000" y2="630"/>
  </g>

  <!-- Outer Console Border -->
  <rect x="20" y="20" width="1160" height="590" fill="none" stroke="#30404D" stroke-width="2" rx="4"/>
  <rect x="25" y="25" width="1150" height="580" fill="none" stroke="#202B33" stroke-width="1" rx="3"/>

  <!-- Top Status Annunciator -->
  <rect x="400" y="55" width="400" height="34" rx="3" fill="#202B33" stroke="#137CBD" stroke-width="1.5"/>
  <circle cx="420" cy="72" r="4" fill="#0F9960"/>
  <text x="610" y="77" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#2B95D6" text-anchor="middle" letter-spacing="2">SYSTEM ONLINE // OPERATIONAL FIELD CONSOLE</text>

  <!-- Title (No Word Count Spam) -->
  <text x="600" y="175" font-family="system-ui, -apple-system, sans-serif" font-size="64" font-weight="800" fill="#F5F8FA" text-anchor="middle" letter-spacing="2">REPURPOSED<tspan fill="#2B95D6">.TECH</tspan></text>

  <!-- Subtitle -->
  <text x="600" y="225" font-family="system-ui, sans-serif" font-size="18" font-weight="600" fill="#8A9BA8" text-anchor="middle" letter-spacing="1">ELECTROMECHANICAL SALVAGE &amp; KINEMATIC WORKSTATION</text>

  <!-- 3 Hardware Telemetry Modules -->
  <g transform="translate(150, 275)">
    <!-- Module 1 -->
    <rect x="30" y="0" width="260" height="135" rx="3" fill="#293742" stroke="#30404D" stroke-width="1.5"/>
    <text x="160" y="55" font-family="'SF Mono', monospace" font-size="44" font-weight="bold" fill="#2B95D6" text-anchor="middle">50</text>
    <text x="160" y="90" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#F5F8FA" text-anchor="middle">BLUEPRINTS</text>
    <text x="160" y="112" font-family="system-ui, sans-serif" font-size="12" fill="#8A9BA8" text-anchor="middle">Production Cookbooks</text>

    <!-- Module 2 -->
    <rect x="320" y="0" width="260" height="135" rx="3" fill="#293742" stroke="#30404D" stroke-width="1.5"/>
    <text x="450" y="55" font-family="'SF Mono', monospace" font-size="44" font-weight="bold" fill="#D9822B" text-anchor="middle">100</text>
    <text x="450" y="90" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#F5F8FA" text-anchor="middle">DONOR STREAMS</text>
    <text x="450" y="112" font-family="system-ui, sans-serif" font-size="12" fill="#8A9BA8" text-anchor="middle">Urban Mining Matrix</text>

    <!-- Module 3 -->
    <rect x="610" y="0" width="260" height="135" rx="3" fill="#293742" stroke="#30404D" stroke-width="1.5"/>
    <text x="740" y="55" font-family="'SF Mono', monospace" font-size="44" font-weight="bold" fill="#0F9960" text-anchor="middle">15</text>
    <text x="740" y="90" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#F5F8FA" text-anchor="middle">VOLUMES</text>
    <text x="740" y="112" font-family="system-ui, sans-serif" font-size="12" fill="#8A9BA8" text-anchor="middle">36 Technical Chapters</text>
  </g>

  <!-- Bottom Terminal Status Bar -->
  <rect x="80" y="480" width="1040" height="50" rx="3" fill="#202B33" stroke="#30404D" stroke-width="1.5"/>
  <text x="600" y="511" font-family="system-ui, sans-serif" font-size="13" font-weight="600" fill="#BFCCD6" text-anchor="middle" letter-spacing="1.5">OFFLINE COMPLIANT &bull; ZERO EXTERNAL DEPENDENCIES &bull; MISSION-CRITICAL SPECIFICATIONS</text>
</svg>"""
    with open(os.path.join(ASSETS_DIR, "og-card.svg"), "w", encoding="utf-8") as f:
        f.write(og_card_svg)

def build_dist_index():
    log("Processing and decorating dist/index.html...")
    with open(os.path.join(WORKSPACE, "index.html"), "r", encoding="utf-8") as f:
        html = f.read()

    # Meta Tags to inject
    prod_meta = f"""
  <!-- Canonical & Domain Verification -->
  <link rel="canonical" href="{DOMAIN}/">
  <meta name="description" content="REPURPOSED: The Maker's Bible of Electromechanical Salvage &amp; Repurposing. 15 Volumes, 36 Comprehensive Chapters, 50 Engineering Blueprints, 100 Donor Scrap Streams.">
  <meta name="keywords" content="repurposed, electromechanical salvage, hardware hacking, motor repurposing, brushless DC, ODrive, VESC, stepper motors, kinematics, engineering blueprints, urban mining">
  <meta name="author" content="The Advanced Electromechanical Salvage Guild">
  <meta name="robots" content="index, follow">

  <!-- OpenGraph / Facebook / LinkedIn / Discord -->
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="repurposed.tech">
  <meta property="og:title" content="REPURPOSED &bull; The Maker's Bible of Electromechanical Salvage">
  <meta property="og:description" content="15 Volumes, 36 Chapters, 50 Blueprints, 100 Donors. The definitive open-source salvage engineering workstation.">
  <meta property="og:url" content="{DOMAIN}/">
  <meta property="og:image" content="{DOMAIN}/assets/og-card.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">

  <!-- Twitter / X Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:domain" content="repurposed.tech">
  <meta name="twitter:url" content="{DOMAIN}/">
  <meta name="twitter:title" content="REPURPOSED &bull; The Maker's Bible of Electromechanical Salvage">
  <meta name="twitter:description" content="15 Volumes, 36 Chapters, 50 Blueprints, 100 Donors. The definitive open-source salvage engineering manual.">
  <meta name="twitter:image" content="{DOMAIN}/assets/og-card.png">

  <!-- Icons & Progressive Web App (PWA) -->
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="alternate icon" href="/favicon.ico">
  <link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
  <link rel="manifest" href="/manifest.json">
  <meta name="theme-color" content="#182026">
  <meta name="msapplication-TileColor" content="#182026">
"""
    # Replace title tag
    html = html.replace(
        "<title>REPURPOSED &bull; The Maker's Bible of Electromechanical Salvage</title>",
        f"<title>REPURPOSED &bull; The Maker's Bible of Electromechanical Salvage</title>\n{prod_meta}"
    )

    with open(os.path.join(DIST_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

def build_dist_ebook():
    log("Processing dist/ebook.html...")
    with open(os.path.join(WORKSPACE, "THE_MAKERS_BIBLE_OF_ELECTROMECHANICAL_SALVAGE.html"), "r", encoding="utf-8") as f:
        ebook_html = f.read()

    # Inject domain header and favicon
    ebook_meta = f"""
  <link rel="canonical" href="{DOMAIN}/ebook.html">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <meta name="description" content="The Complete 15-Volume Technical Handbook &amp; 50 Engineering Blueprints Reader Edition. Hosted at repurposed.tech.">
"""
    ebook_html = ebook_html.replace("<head>", f"<head>\n{ebook_meta}")
    
    # Inject modern navigation top bar
    nav_top = f"""
<div style="background: #202B33; border-bottom: 1px solid #30404D; padding: 10px 24px; font-family: system-ui, sans-serif; font-size: 13px; display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 100;">
  <a href="/" style="color: #2B95D6; text-decoration: none; font-weight: 600; display: flex; align-items: center; gap: 8px;">
    <span>&larr;</span> <span>[ RETURN TO REPURPOSED.TECH TERMINAL ]</span>
  </a>
  <span style="color: #8A9BA8; font-size: 11px; font-mono: monospace;">CHANNELS: 15 VOLUMES &bull; 36 CHAPTERS &bull; 50 BLUEPRINTS &bull; 100 DONORS</span>
</div>
"""
    ebook_html = ebook_html.replace("<body>", f"<body>\n{nav_top}")

    with open(os.path.join(DIST_DIR, "ebook.html"), "w", encoding="utf-8") as f:
        f.write(ebook_html)

def copy_downloads():
    log("Copying offline downloads to dist/downloads/...")
    shutil.copy2(
        os.path.join(WORKSPACE, "THE_MAKERS_BIBLE_OF_ELECTROMECHANICAL_SALVAGE.epub"),
        os.path.join(DOWNLOADS_DIR, "the-makers-bible-of-electromechanical-salvage.epub")
    )
    shutil.copy2(
        os.path.join(WORKSPACE, "THE_MAKERS_BIBLE_OF_ELECTROMECHANICAL_SALVAGE.md"),
        os.path.join(DOWNLOADS_DIR, "the-makers-bible-of-electromechanical-salvage.md")
    )
    shutil.copy2(
        os.path.join(WORKSPACE, "SALVAGE_COMPENDIUM.md"),
        os.path.join(DOWNLOADS_DIR, "salvage-compendium.md")
    )

def generate_web_configs():
    log("Generating robots.txt, sitemap.xml, manifest.json, 404.html & host configs...")

    # robots.txt
    robots = f"""User-agent: *
Allow: /

Sitemap: {DOMAIN}/sitemap.xml
"""
    with open(os.path.join(DIST_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots)

    # sitemap.xml
    now_iso = datetime.now().strftime("%Y-%m-%d")
    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>{DOMAIN}/</loc>
    <lastmod>{now_iso}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>{DOMAIN}/ebook.html</loc>
    <lastmod>{now_iso}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>{DOMAIN}/downloads/the-makers-bible-of-electromechanical-salvage.epub</loc>
    <lastmod>{now_iso}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>{DOMAIN}/downloads/the-makers-bible-of-electromechanical-salvage.md</loc>
    <lastmod>{now_iso}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>{DOMAIN}/downloads/salvage-compendium.md</loc>
    <lastmod>{now_iso}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
</urlset>
"""
    with open(os.path.join(DIST_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap)

    # manifest.json (PWA)
    manifest = """{
  "name": "REPURPOSED.TECH - Laboratory Terminal",
  "short_name": "REPURPOSED",
  "description": "The Maker's Bible of Electromechanical Salvage & Repurposing",
  "start_url": "/",
  "display": "standalone",
  "orientation": "any",
  "background_color": "#070b08",
  "theme_color": "#4ade80",
  "icons": [
    {
      "src": "/favicon.svg",
      "sizes": "any",
      "type": "image/svg+xml",
      "purpose": "any maskable"
    },
    {
      "src": "/assets/apple-touch-icon.png",
      "sizes": "180x180",
      "type": "image/png"
    }
  ]
}
"""
    with open(os.path.join(DIST_DIR, "manifest.json"), "w", encoding="utf-8") as f:
        f.write(manifest)

    # 404.html (Phosphor Green Laboratory Console 404)
    error_404 = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ERR 404: CHANNEL NOT FOUND &bull; repurposed.tech</title>
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<style>
  body {
    background-color: #070b08;
    color: #e2f5e8;
    font-family: ui-monospace, monospace;
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    margin: 0;
    padding: 20px;
  }
  .terminal-box {
    background: #050906;
    border: 1px solid #4ade80;
    box-shadow: 0 0 30px rgba(74, 222, 128, 0.15), inset 0 0 40px rgba(0, 0, 0, 0.8);
    max-width: 520px;
    width: 100%;
    border-radius: 4px;
    overflow: hidden;
    padding: 28px;
    text-align: center;
  }
  .badge {
    background: #112417;
    color: #86efac;
    border: 1px solid #1e3325;
    padding: 4px 10px;
    border-radius: 4px;
    font-size: 11px;
    font-weight: bold;
    display: inline-block;
    margin-bottom: 16px;
  }
  h1 {
    font-size: 20px;
    color: #ffffff;
    margin: 0 0 10px;
  }
  p {
    font-size: 12px;
    line-height: 1.6;
    color: #86b595;
    margin-bottom: 24px;
  }
  .btn {
    background: #13291a;
    border: 1px solid #345d3e;
    color: #86efac;
    padding: 8px 18px;
    font-weight: bold;
    font-size: 12px;
    border-radius: 4px;
    text-decoration: none;
    display: inline-block;
    transition: all 0.2s;
  }
  .btn:hover {
    background: #1e3e27;
    border-color: #4ade80;
    color: #ffffff;
    box-shadow: 0 0 10px rgba(74, 222, 128, 0.3);
  }
</style>
</head>
<body>
  <div class="terminal-box">
    <div class="badge">[ HTTP 404 // CHANNEL DE-INDEXED ]</div>
    <h1>SUBSYSTEM NOT LOCATED</h1>
    <p>
      The requested channel, blueprint schema, or donor telemetry could not be addressed in this sector of the matrix.
    </p>
    <a href="/" class="btn">&gt;&gt; RETURN TO PRIMARY WORKSTATION</a>
  </div>
</body>
</html>
"""
    with open(os.path.join(DIST_DIR, "404.html"), "w", encoding="utf-8") as f:
        f.write(error_404)

    # CNAME for GitHub Pages / Cloudflare Pages custom domain
    with open(os.path.join(DIST_DIR, "CNAME"), "w", encoding="utf-8") as f:
        f.write("repurposed.tech\n")

    # _headers for Cloudflare Pages & Netlify
    headers = """/*
  X-Frame-Options: SAMEORIGIN
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin

/assets/*
  Cache-Control: public, max-age=31536000, immutable

/downloads/*
  Cache-Control: public, max-age=86400

/favicon.svg
  Cache-Control: public, max-age=604800

/manifest.json
  Cache-Control: public, max-age=86400
"""
    with open(os.path.join(DIST_DIR, "_headers"), "w", encoding="utf-8") as f:
        f.write(headers)

    # _redirects for Cloudflare Pages & Netlify
    redirects = """/read            /ebook.html                                              200
/bible           /ebook.html                                              200
/bible.epub      /downloads/the-makers-bible-of-electromechanical-salvage.epub   301
/bible.md        /downloads/the-makers-bible-of-electromechanical-salvage.md     301
/compendium      /downloads/salvage-compendium.md                                 301
"""
    with open(os.path.join(DIST_DIR, "_redirects"), "w", encoding="utf-8") as f:
        f.write(redirects)

    # vercel.json for Vercel deployment
    vercel = """{
  "cleanUrls": true,
  "rewrites": [
    { "source": "/read", "destination": "/ebook.html" },
    { "source": "/bible.epub", "destination": "/downloads/the-makers-bible-of-electromechanical-salvage.epub" },
    { "source": "/bible.md", "destination": "/downloads/the-makers-bible-of-electromechanical-salvage.md" },
    { "source": "/compendium", "destination": "/downloads/salvage-compendium.md" }
  ],
  "headers": [
    {
      "source": "/assets/(.*)",
      "headers": [
        { "key": "Cache-Control", "value": "public, max-age=31536000, immutable" }
      ]
    }
  ]
}
"""
    with open(os.path.join(DIST_DIR, "vercel.json"), "w", encoding="utf-8") as f:
        f.write(vercel)

    # firebase.json in root
    firebase = """{
  "hosting": {
    "public": "dist",
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ],
    "rewrites": [
      {
        "source": "/read",
        "destination": "/ebook.html"
      }
    ]
  }
}
"""
    with open(os.path.join(WORKSPACE, "firebase.json"), "w", encoding="utf-8") as f:
        f.write(firebase)

def main():
    log("==================================================================")
    log("  STARTING PRODUCTION DISTRIBUTION BUILD FOR REPURPOSED.TECH     ")
    log("==================================================================")
    ensure_fresh_compilation()
    setup_directories()
    
    log("Generating phosphorescent green terminal icons & social cards...")
    generate_ico(os.path.join(DIST_DIR, "favicon.ico"))
    generate_png(os.path.join(ASSETS_DIR, "apple-touch-icon.png"), 180, 180, is_banner=False)
    generate_png(os.path.join(ASSETS_DIR, "og-card.png"), 1200, 630, is_banner=True)
    generate_svg_assets()

    build_dist_index()
    build_dist_ebook()
    copy_downloads()
    generate_web_configs()

    total_files = sum(len(files) for _, _, files in os.walk(DIST_DIR))
    total_bytes = sum(sum(os.path.getsize(os.path.join(root, name)) for name in files) for root, _, files in os.walk(DIST_DIR))
    log("==================================================================")
    log(f"  DISTRIBUTION BUNDLE READY IN: {DIST_DIR}")
    log(f"  Total Files: {total_files} | Total Size: {total_bytes / (1024*1024):.2f} MB")
    log(f"  Configured Target: {DOMAIN}")
    log("==================================================================")

if __name__ == "__main__":
    main()
