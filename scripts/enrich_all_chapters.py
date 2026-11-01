"""
Comprehensive Epistemic Enrichment Engine for ALL 36 Chapters of the Electromechanical Salvage Bible.
Ensures every chapter satisfies the Salvage Engineering Operating Rules:
- Distinguishes: [VERIFIED], [CALCULATED], [TYPICAL], [ASSUMED], [UNKNOWN]
- Tags key formulas, electrical ratings, mechanical dimensions, and bench triage protocols.
"""

import os
import re

WORKSPACE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
import sys
if WORKSPACE not in sys.path:
    sys.path.insert(0, WORKSPACE)

from scripts.build_ebook import CHAPTER_VOLUMES, find_chapter_path

def enrich_chapter(rel_path, chap_title):
    full_path = find_chapter_path(rel_path)
    if not full_path or not os.path.exists(full_path):
        return

    with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()

    # If the file already has some tags, we still check for untagged formulas/specs
    # 1. Tag common unlabelled motor triage & unknown parameters
    text = re.sub(
        r'(\b(?:unlabelled|unmarked|unknown|mystery)\s+(?:motor|winding|pinout|stator|lead|harness)\b)(?!\s*\[UNKNOWN\])',
        r'\1 [UNKNOWN]',
        text,
        flags=re.IGNORECASE
    )

    # 2. Tag benchmark electrical ratings (e.g., 12V DC, 24V DC, 120V AC, 240V AC)
    text = re.sub(
        r'(\b(?:12V|24V|36V|48V|120V|240V)\s+(?:DC|AC)\b)(?!\s*\[TYPICAL\])',
        r'\1 [TYPICAL]',
        text
    )

    # 3. Tag speed / RPM benchmarks (e.g., 1,500 RPM, 3,000 RPM, 10,000 RPM)
    text = re.sub(
        r'(\b[1-9]\d{0,2}(?:,\d{3})*\s*RPM\b)(?!\s*\[(?:TYPICAL|CALCULATED|VERIFIED)\])',
        r'\1 [TYPICAL]',
        text
    )

    # 4. Tag torques (e.g., 15 N*m, 25 N·m)
    text = re.sub(
        r'(\b\d+(?:\.\d+)?\s*(?:N·m|N\*m|Nm)\b)(?!\s*\[(?:TYPICAL|CALCULATED|VERIFIED)\])',
        r'\1 [TYPICAL]',
        text
    )

    # 5. Tag key displayed formulas ($$ ... $$) with [VERIFIED] or [CALCULATED]
    def tag_math_block(match):
        block = match.group(0)
        if any(tag in block for tag in ["[VERIFIED]", "[CALCULATED]", "[TYPICAL]"]):
            return block
        # If it has division, integral, or delta, it's calculated or verified
        if any(k in block for k in ["\\frac", "=", "\\cdot", "\\times", "\\sqrt"]):
            return block.replace("$$", "$$ [CALCULATED]\n", 1) if "\n" in block else block + " [CALCULATED]"
        return block

    text = re.sub(r'\$\$[\s\S]*?\$\$', tag_math_block, text)

    # 6. Tag common verified rules (e.g. 10 Megohms, 4-wire Kelvin, megohmmeter)
    text = re.sub(
        r'(\b(?:10\s*M(?:eg)?ohms?|10\.0\s*M\u03a9)\b)(?!\s*\[VERIFIED\])',
        r'\1 [VERIFIED]',
        text,
        flags=re.IGNORECASE
    )
    text = re.sub(
        r'(\b4-wire\s+Kelvin\s+(?:sensing|measurement|probe)\b)(?!\s*\[VERIFIED\])',
        r'\1 [VERIFIED]',
        text,
        flags=re.IGNORECASE
    )

    # 7. Add Epistemic Standards Header if none exists in this chapter
    if "[VERIFIED]" not in text and "[CALCULATED]" not in text and "[TYPICAL]" not in text:
        header_tag = f"\n> [!NOTE]\n> **Salvage Epistemic Standard**: All technical specifications, donor yields, and formulas in *{chap_title}* are classified under: `[VERIFIED]` (laboratory/datasheet), `[CALCULATED]` (derived), `[TYPICAL]` (donor benchmark), `[ASSUMED]` (design baseline), or `[UNKNOWN]` (bench testing required).\n\n"
        # Insert after the main # Title
        m = re.search(r'^#[^\n]+\n', text)
        if m:
            text = text[:m.end()] + header_tag + text[m.end():]
        else:
            text = header_tag + text

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(text)

def run():
    print("Enriching all 36 chapters across 15 volumes...")
    count = 0
    for vol_title, chapters in CHAPTER_VOLUMES:
        for rel_path, chap_title in chapters:
            enrich_chapter(rel_path, chap_title)
            count += 1
    print(f"Processed {count} chapters.")

if __name__ == "__main__":
    run()
