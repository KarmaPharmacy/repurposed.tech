"""
Audit tool for Electromechanical Salvage Bible & Epistemic Standards.
Scans all 36 chapters, 50 blueprints, and 88 donor streams for:
- Epistemic classification tags: [VERIFIED], [CALCULATED], [TYPICAL], [ASSUMED], [UNKNOWN]
- Lethal safety hazard warnings (MOT, BeO, 400V DC bus capacitors)
- Bench verification protocols for unknown windings/pinouts
"""

import os
import re
import sys

WORKSPACE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if WORKSPACE not in sys.path:
    sys.path.insert(0, WORKSPACE)

from scripts.build_ebook import CHAPTER_VOLUMES, find_chapter_path
from scripts.encarta_data import BLUEPRINTS_DATA, DONORS_DATA

TAG_PATTERNS = {
    "VERIFIED": re.compile(r"\[VERIFIED\]"),
    "CALCULATED": re.compile(r"\[CALCULATED\]"),
    "TYPICAL": re.compile(r"\[TYPICAL\]"),
    "ASSUMED": re.compile(r"\[ASSUMED\]"),
    "UNKNOWN": re.compile(r"\[UNKNOWN\]"),
}

LETHAL_PATTERNS = {
    "MOT": re.compile(r"(MOT|microwave oven transformer|2[,.]?000\s*V|2[,.]?500\s*V)", re.IGNORECASE),
    "BeO": re.compile(r"(beryllium oxide|BeO|carcinogenic)", re.IGNORECASE),
    "Capacitor": re.compile(r"(discharge resistor|bus capacitor|300V|400V)", re.IGNORECASE),
    "Flywheel": re.compile(r"(flywheel|burst|containment|1/2\s*I\s*omega)", re.IGNORECASE),
}

def audit_entire_bible():
    report = {
        "chapters": [],
        "blueprints": [],
        "donors": [],
        "total_tags": {"VERIFIED": 0, "CALCULATED": 0, "TYPICAL": 0, "ASSUMED": 0, "UNKNOWN": 0},
        "hazard_coverage": {},
    }

    # 1. Audit Chapters
    for vol_title, chapters in CHAPTER_VOLUMES:
        for rel_path, chap_title in chapters:
            full_path = find_chapter_path(rel_path)
            content = ""
            if full_path and os.path.exists(full_path):
                with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

            tags = {k: len(p.findall(content)) for k, p in TAG_PATTERNS.items()}
            hazards = {k: len(p.findall(content)) for k, p in LETHAL_PATTERNS.items()}
            for k, count in tags.items():
                report["total_tags"][k] += count

            report["chapters"].append({
                "file": rel_path,
                "title": chap_title,
                "volume": vol_title,
                "word_count": len(content.split()),
                "tags": tags,
                "hazards": hazards,
            })

    # 2. Audit Blueprints
    for bp in BLUEPRINTS_DATA:
        bp_text = f"{bp.get('title','')} {bp.get('desc','')} {bp.get('donor','')} {bp.get('power','')} {bp.get('formula','')} {bp.get('sop','')} {' '.join(bp.get('bom',[]))}"
        tags = {k: len(p.findall(bp_text)) for k, p in TAG_PATTERNS.items()}
        report["blueprints"].append({
            "num": bp["num"],
            "title": bp["title"],
            "power": bp.get("power", ""),
            "formula": bp.get("formula", ""),
            "tags": tags,
        })

    # 3. Audit Donors
    for donor in DONORS_DATA:
        d_text = f"{donor.get('name','')} {donor.get('danger','')} {donor.get('avoid','')} {donor.get('triage','')} {donor.get('bestFor','')}"
        tags = {k: len(p.findall(d_text)) for k, p in TAG_PATTERNS.items()}
        report["donors"].append({
            "id": donor["id"],
            "name": donor["name"],
            "danger": donor.get("danger", ""),
            "triage": donor.get("triage", ""),
            "tags": tags,
        })

    return report

def print_audit_summary(report):
    print("=" * 80)
    print("REPURPOSED BIBLE: EPISTEMIC AUDIT & VERIFICATION REPORT")
    print("=" * 80)
    print(f"Total Volumes Scanned:    {len(CHAPTER_VOLUMES)}")
    print(f"Total Chapters Scanned:   {len(report['chapters'])}")
    print(f"Total Blueprints Scanned: {len(report['blueprints'])}")
    print(f"Total Donors Scanned:     {len(report['donors'])}")
    print("-" * 80)
    print("EPISTEMIC CLASSIFICATION TAG COUNTS (ACROSS CHAPTERS):")
    for tag, count in report["total_tags"].items():
        print(f"  [{tag:10}]: {count:5} occurrences")
    print("-" * 80)
    
    # Check chapters with 0 tags
    zero_tag_chaps = [c["file"] for c in report["chapters"] if sum(c["tags"].values()) == 0]
    print(f"Chapters with 0 epistemic tags: {len(zero_tag_chaps)} / {len(report['chapters'])}")
    
    # Check blueprints with tags
    tagged_bps = [b["num"] for b in report["blueprints"] if sum(b["tags"].values()) > 0]
    print(f"Blueprints with epistemic tags: {len(tagged_bps)} / {len(report['blueprints'])}")
    print("=" * 80)

if __name__ == "__main__":
    rep = audit_entire_bible()
    print_audit_summary(rep)
