"""
Comprehensive Generator for ENCARTA '95 : ELECTROMECHANICA
The Interactive Multimedia Encyclopedia, Physics Laboratory & Salvage Simulator.
Embeds ALL 15 VOLUMES (36 Unabridged Chapters, 50 Blueprints, 88 Donors).
Features:
- Encarta '95 Multimedia Skeuomorphic Chrome with Audio VU Visualizer
- Web Speech API 'Audio Tour' Narrator
- Web Audio Procedural Sound Engine (Clicks, Chimes, Grinder Screech, Motor Whine, Fanfare)
- CRT Phosphor & Scanline Shader
- 5 Live HTML5 Canvas Physics Simulators (LeBlanc with Seismograph, Spark Metallurgy, Wire Wizard with Multimeter, Geneva/Scotch Yoke, CD Spot Welder Oscilloscope)
- Multi-Layer Appliance X-Ray Cutaway with Layer Peel Slider
- Playable MindMaze '95 2.5D Isometric Dungeon Adventure with Inventory Pouch & Diploma
- Full-text Pinpointer Omnisearch across all 500+ KB of technical documentation
"""

import os
import sys
import json
import re
import html
from datetime import datetime

WORKSPACE = r"C:\Users\karma\Desktop\REPURPOSE"
sys.path.insert(0, WORKSPACE)
sys.path.insert(0, os.path.join(WORKSPACE, "scripts"))

from build_ebook import CHAPTER_VOLUMES, find_chapter_path, markdown_to_html
ARTIFACT_DIR = r"C:\Users\karma\.gemini\antigravity\brain\5e9a81ab-3e75-499e-94e7-7e11fb483cbb"

print("--- Step 1: Loading and Parsing All 36 Compendium Chapters ---")

articles = []
chapter_index = 1

for vol_title, chapters in CHAPTER_VOLUMES:
    vol_num_match = re.search(r'Volume\s+([0-9\.]+)', vol_title)
    vol_num = vol_num_match.group(1) if vol_num_match else "Ref"
    
    for rel_path, chap_title in chapters:
        file_path = find_chapter_path(rel_path)
        if not file_path or not os.path.exists(file_path):
            print(f"Warning: Missing file {rel_path}")
            continue
            
        with open(file_path, "r", encoding="utf-8") as f:
            raw_md = f.read()
            
        # Parse HTML
        chap_html = markdown_to_html(raw_md, f"art_{chapter_index}")
        
        # Extract plain text summary for search & audio tour
        plain_text = re.sub(r'<[^>]+>', ' ', chap_html)
        plain_text = re.sub(r'\s+', ' ', plain_text).strip()
        
        # Extract executive summary (first 2 paragraphs)
        paragraphs = [p for p in raw_md.split("\n\n") if p.strip() and not p.strip().startswith('#') and not p.strip().startswith('```')]
        summary = " ".join(paragraphs[:2]) if paragraphs else "Technical electromechanical salvage documentation."
        summary = re.sub(r'[*_`#\[\]]', '', summary)[:300] + "..."
        
        # Extract hazard warnings if present
        has_warning = "[!WARNING]" in raw_md or "[!CAUTION]" in raw_md or "[!IMPORTANT]" in raw_md or "LETHAL" in raw_md
        
        articles.append({
            "id": f"art_{chapter_index}",
            "num": chapter_index,
            "volTitle": vol_title,
            "volNum": vol_num,
            "title": chap_title,
            "summary": summary,
            "hasWarning": has_warning,
            "html": chap_html,
            "wordCount": len(plain_text.split()),
            "readTime": max(1, round(len(plain_text.split()) / 200))
        })
        chapter_index += 1

print(f"[OK] Parsed {len(articles)} full unabridged articles ({sum(a['wordCount'] for a in articles)} total words).")
