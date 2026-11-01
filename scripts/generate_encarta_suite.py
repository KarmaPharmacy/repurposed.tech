"""
REPURPOSED : THE MAKER'S BIBLE - Master Build Suite
Compiles the complete single-page modern interactive engineering application:
- 15 Volumes & 36 Unabridged Chapters (82,448 words)
- Modern UI Max Pro Cyber-Engineering Design System
- Interactive Left Volume & Chapter Atlas with live filtering & accordions
- 50 Production Engineering Blueprints with schematics, BOMs, and SOPs
- 88-Donor Streams Scrap Atlas Matrix
- Spotlight Command Palette (Ctrl+K / Cmd+K)
- Offline Digital Editions Download Vault
"""

import os
import sys
import json
import re

WORKSPACE = r"C:\Users\karma\Desktop\REPURPOSE"
sys.path.insert(0, WORKSPACE)
sys.path.insert(0, os.path.join(WORKSPACE, "scripts"))

from build_ebook import CHAPTER_VOLUMES, find_chapter_path, markdown_to_html
from encarta_data import CATEGORIES, DONORS_DATA, BLUEPRINTS_DATA
from encarta_metadata import VOLUME_METADATA, CHAPTER_SUBTITLES
from repurposed_styles import REPURPOSED_CSS
from repurposed_html_views import REPURPOSED_HTML
from repurposed_core_js import REPURPOSED_CORE_JS

ARTIFACT_DIR = r"C:\Users\karma\.gemini\antigravity\brain\5e9a81ab-3e75-499e-94e7-7e11fb483cbb"

print("=" * 70)
print("  REPURPOSED.TECH : THE MAKER'S BIBLE - MASTER SUITE COMPILER")
print("=" * 70)

print("1. Parsing all 36 compendium chapters and merging enriched metadata...")
articles = []
chapter_index = 1

for vIdx, (vol_title, chapters) in enumerate(CHAPTER_VOLUMES):
    vm = VOLUME_METADATA[vIdx] if vIdx < len(VOLUME_METADATA) else {}
    vol_code = vm.get("volCode", f"VOL. {vIdx:02d}")
    vol_tagline = vm.get("tagline", "")
    cat_icon = vm.get("catIcon", "⚡")
    hazard = vm.get("hazard", "TECHNICAL")
    hazard_color = vm.get("hazardColor", "#06b6d4")

    for rel_path, chap_title in chapters:
        file_path = find_chapter_path(rel_path)
        if not file_path or not os.path.exists(file_path):
            print(f"   [WARNING] File missing: {rel_path}")
            continue

        with open(file_path, "r", encoding="utf-8") as f:
            raw_md = f.read()

        chap_html = markdown_to_html(raw_md, f"art_{chapter_index}")
        plain_text = re.sub(r'<[^>]+>', ' ', chap_html)
        plain_text = re.sub(r'\s+', ' ', plain_text).strip()
        word_count = len(plain_text.split())

        paragraphs = [p for p in raw_md.split("\n\n") if p.strip() and not p.strip().startswith('#') and not p.strip().startswith('```')]
        summary = " ".join(paragraphs[:2]) if paragraphs else "Technical electromechanical salvage documentation."
        summary = re.sub(r'[*_`#\[\]]', '', summary)[:280] + "..."

        has_warning = "[!WARNING]" in raw_md or "[!CAUTION]" in raw_md or "[!IMPORTANT]" in raw_md or "LETHAL" in raw_md

        # Extract section titles for outline
        sections = re.findall(r'<h[23][^>]*>(.*?)</h[23]>', chap_html)
        clean_sections = [re.sub(r'<[^>]+>', '', s).strip() for s in sections][:8]

        clean_title = chap_title.split(': ', 1)[1] if ': ' in chap_title else chap_title
        subtitle = CHAPTER_SUBTITLES.get(chap_title, "")

        articles.append({
            "id": f"art_{chapter_index}",
            "num": chapter_index,
            "numBadge": f"CH. {chapter_index:02d}",
            "volTitle": vol_title,
            "volCode": vol_code,
            "volTagline": vol_tagline,
            "catIcon": cat_icon,
            "volHazard": hazard,
            "volHazardColor": hazard_color,
            "title": chap_title,
            "cleanTitle": clean_title,
            "subTitle": subtitle,
            "summary": summary,
            "hasWarning": has_warning,
            "sections": clean_sections,
            "html": chap_html,
            "wordCount": word_count,
            "readTime": max(1, round(word_count / 200))
        })
        chapter_index += 1

total_words = sum(a["wordCount"] for a in articles)
print(f"   Loaded {len(articles)} articles ({total_words:,} words).")

print("2. Constructing hierarchical Volume Tree for Atlas...")
vol_tree = []
for vIdx, (vol_title, chapters) in enumerate(CHAPTER_VOLUMES):
    vm = VOLUME_METADATA[vIdx] if vIdx < len(VOLUME_METADATA) else {}
    vol_articles = [a for a in articles if a["volTitle"] == vol_title]
    v_words = sum(a["wordCount"] for a in vol_articles)
    v_time = sum(a["readTime"] for a in vol_articles)

    vol_tree.append({
        "volIndex": vIdx,
        "volCode": vm.get("volCode", f"VOL. {vIdx:02d}"),
        "title": vm.get("title", vol_title),
        "tagline": vm.get("tagline", ""),
        "catIcon": vm.get("catIcon", "📦"),
        "hazard": vm.get("hazard", "TECHNICAL"),
        "hazardColor": vm.get("hazardColor", "#06b6d4"),
        "totalWords": v_words,
        "totalTime": v_time,
        "articles": [{
            "id": a["id"],
            "num": a["num"],
            "numBadge": a["numBadge"],
            "title": a["title"],
            "cleanTitle": a["cleanTitle"],
            "subTitle": a["subTitle"],
            "readTime": a["readTime"],
            "wordCount": a["wordCount"],
            "hasWarning": a["hasWarning"],
            "summary": a["summary"]
        } for a in vol_articles]
    })

print(f"   Built volume tree: {len(vol_tree)} volumes.")

print("3. Assembling Master Application HTML...")

articles_json = json.dumps(articles)
vol_tree_json = json.dumps(vol_tree)
donors_json = json.dumps(DONORS_DATA)
blueprints_json = json.dumps(BLUEPRINTS_DATA)
categories_json = json.dumps(CATEGORIES)

full_html = f"""<!DOCTYPE html>
<html lang="en" class="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>REPURPOSED &bull; The Maker's Bible of Electromechanical Salvage</title>
<script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
<style>
{REPURPOSED_CSS}
</style>
</head>
<body class="min-h-screen flex flex-col bg-[#182026] text-[#BFCCD6]">

{REPURPOSED_HTML}

<script>
// ================= EMBEDDED COMPLETE DATASETS =================
const ARTICLES = {articles_json};
const VOL_TREE = {vol_tree_json};
const DONORS = {donors_json};
const BLUEPRINTS = {blueprints_json};
const CATEGORIES = {categories_json};

{REPURPOSED_CORE_JS}
</script>

</body>
</html>
"""

print("4. Writing standalone distribution targets...")
targets = [
    os.path.join(WORKSPACE, "index.html"),
    os.path.join(WORKSPACE, "repurposed.html"),
    os.path.join(WORKSPACE, "encarta_encyclopedia.html"),
    os.path.join(WORKSPACE, "interactive_encyclopedia.html"),
    os.path.join(ARTIFACT_DIR, "encarta_salvage_encyclopedia.html")
]

for p in targets:
    with open(p, "w", encoding="utf-8") as f:
        f.write(full_html)
    size_kb = os.path.getsize(p) / 1024
    print(f"   [SUCCESS] Written {p} ({size_kb:.1f} KB)")

print("=" * 70)
print(f"BUILD COMPLETE: 36 Articles, {len(BLUEPRINTS_DATA)} Blueprints, {len(DONORS_DATA)} Donors.")
print(f"Total Content: {total_words:,} words across 15 Volumes.")
print("=" * 70)
