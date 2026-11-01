import os
import re
import zipfile
import html
import uuid
from datetime import datetime, timezone

WORKSPACE = r"C:\Users\karma\Desktop\REPURPOSE"

def find_chapter_path(rel_path):
    """Finds the chapter path whether files are flat or in subdirectories."""
    p1 = os.path.join(WORKSPACE, rel_path)
    if os.path.exists(p1):
        return p1
    p2 = os.path.join(WORKSPACE, os.path.basename(rel_path))
    if os.path.exists(p2):
        return p2
    return None

CHAPTER_VOLUMES = [
    # Volume 0: Foundations & Safety
    ("Volume 0: Foundations, Diagnostics & Control", [
        ("safety_and_hazards.md", "Chapter 1: Scrapper's Safety Protocols & Lethal Hazards"),
        ("motor_identification_diagnostics.md", "Chapter 2: Motor Identification & Bench Diagnostics"),
        ("universal_driving_guide.md", "Chapter 3: Universal Driving Topologies & Control Architectures"),
    ]),
    # Volume 1: Consumer Electronics & Optics
    ("Volume 1: Precision Consumer Electronics & Optics", [
        ("printers_and_scanners.md", "Chapter 4: Printers, Scanners & Office Copiers"),
        ("optical_drives_and_storage.md", "Chapter 5: Optical Disc Drives & Hard Disk Drives"),
    ]),
    # Volume 2: Automotive 12V Workhorses & Traction
    ("Volume 2: Automotive 12V Workhorses & Traction", [
        ("automotive_12v_workhorses.md", "Chapter 6: Automotive 12V Workhorses"),
        ("heavy_automotive_traction.md", "Chapter 7: Heavy Automotive Traction & Alternator Hacking"),
        ("automotive_hydraulics_fans.md", "Chapter 8: Automotive Hydraulics & High-Flow Blowers"),
    ]),
    # Volume 3: Domestic Mains Appliances
    ("Volume 3: Domestic Mains Appliances", [
        ("washing_machines_and_dryers.md", "Chapter 9: Washing Machines & Clothes Dryers"),
        ("treadmills_and_exercise.md", "Chapter 10: Treadmills & Exercise Equipment"),
        ("refrigeration_and_microwaves.md", "Chapter 11: Refrigeration & Microwave Electromechanics"),
    ]),
    # Volume 4: Mobility & Power Tools
    ("Volume 4: Mobility & Power Tools", [
        ("hoverboards_and_power_tools.md", "Chapter 12: Mobility Electromechanics & Power Tools"),
    ]),
    # Volume 5: Non-Motor Electromechanical Gems
    ("Volume 5: Non-Motor Electromechanical Gems & Lab Scrap", [
        ("lab_sensors_structural.md", "Chapter 13: Lab Scrap, Sensors & Structural Hardware"),
    ]),
    # Volume 6: Marquee Build Cookbooks
    ("Volume 6: Marquee Project Cookbooks (Builds 1 to 8)", [
        ("marquee_salvage_builds.md", "Chapter 14: Marquee Salvage Project Cookbooks (Builds 1 to 8)"),
    ]),
    # Volume 7: Unexplored Frontiers
    ("Volume 7: Unexplored Frontiers & Exotic Electromechanics", [
        ("01_optical_and_spatial_light_modulators.md", "Chapter 15: Spatial Light Modulators & Micro-Optics Scrap"),
        ("02_ultrasonics_and_cavitation.md", "Chapter 16: Ultrasonics, Sonotrodes & Acoustic Cavitation"),
        ("03_commercial_fluidics_and_pumps.md", "Chapter 17: Commercial Fluidics & Rotary Vane Pumps"),
        ("04_exotic_electromagnetics_and_dynos.md", "Chapter 18: Exotic Electromagnetics, Dynos & Resolvers"),
        ("05_thermal_and_energy_harvesting.md", "Chapter 19: Thermal & Exotic Energy Harvesting"),
    ]),
    # Volume 8: Frontier Project Cookbooks
    ("Volume 8: Frontier Project Cookbooks (Builds 9 to 50)", [
        ("frontier_project_blueprints.md", "Chapter 20: Frontier Project Blueprints (Builds 9 to 50)"),
    ]),
    # Volume 9: Field Acquisition & Toolkit
    ("Volume 9: Field Sourcing & Rapid Toolkit Manual", [
        ("field_acquisition_manual.md", "Chapter 21: The Scrapper's Field Sourcing & Toolkit Manual"),
    ]),
    # Volume 10: Mechanical Engineering & Transmissions
    ("Volume 10: Mechanical Engineering & Transmissions", [
        ("01_shaft_couplings_and_mounting.md", "Chapter 22: Shaft Couplings, Hub Adapters & Hardened Machining"),
        ("02_gearboxes_and_speed_reducers.md", "Chapter 23: Gearboxes, Cycloidal Drives & Speed Reducers"),
        ("03_linear_kinematics_and_linkages.md", "Chapter 24: Linear Kinematics, Leadscrews & Linkages"),
        ("04_clutches_brakes_and_freewheels.md", "Chapter 25: Clutches, Electromagnetic Brakes & Freewheels"),
        ("05_cams_geneva_and_intermittent_motion.md", "Chapter 26: Cams, Geneva Drives & Intermittent Mechanisms"),
        ("06_flywheels_balancing_and_damping.md", "Chapter 27: Flywheels, Dynamic Balancing & Mechanical Damping"),
    ]),
    # Volume 11: Radical Mechanical Brainstorming
    ("Volume 11: Radical Mechanical Exploits & Kinematics", [
        ("radical_mechanical_exploits.md", "Chapter 28: Radical Mechanical Exploits & Kinematic Brainstorming"),
    ]),
    # Volume 12: Community Wisdom & Forum Lore
    ("Volume 12: Community Wisdom & Forum Lore", [
        ("01_unwritten_rules_and_pitfalls.md", "Chapter 29: Battle-Tested Forum Lore & Unwritten Scrapper Rules"),
        ("02_obscure_donor_gems_and_secret_hacks.md", "Chapter 30: Obscure Donor Gems & Underground Maker Exploits"),
        ("03_the_scrapper_economics_and_triage.md", "Chapter 31: Scrapper's Economics, Core Resale & Scrap Yard Calculus"),
    ]),
    # Volume 13: Viable Salvage & Garage Build Manual
    ("Volume 13: Viable Salvage & Garage Build Manual", [
        ("01_step_by_step_teardown_sops.md", "Chapter 32: Step-by-Step Field Teardown SOPs"),
        ("02_garage_fabrication_and_mounting_workarounds.md", "Chapter 33: Garage Fabrication & Heavy Mounting Workarounds"),
        ("03_electrical_sanity_and_power_architecture.md", "Chapter 34: Electrical Sanity & Power Architecture"),
        ("04_bench_testing_and_health_triage.md", "Chapter 35: Bench Testing & Motor Health Triage"),
    ]),
    # Volume 14: Grand Master Salvage Compendium
    ("Volume 14: Master Salvage Compendium & Reference Matrix", [
        ("SALVAGE_COMPENDIUM.md", "Appendix A: The Grand Master Electromechanical Matrix & Field Compendium (100 Donors • 50 Blueprints)"),
    ]),
]

def markdown_to_html(md_text, chapter_id=""):
    """Converts a chapter's markdown text to structured semantic HTML."""
    lines = md_text.split("\n")
    html_lines = []
    in_code_block = False
    code_lang = ""
    code_content = []
    in_table = False
    table_rows = []
    in_list = False
    list_type = "ul"
    in_quote = False
    quote_lines = []

    def flush_list():
        nonlocal in_list, list_type
        if in_list:
            html_lines.append(f"</{list_type}>")
            in_list = False

    def flush_table():
        nonlocal in_table, table_rows
        if in_table and table_rows:
            html_lines.append('<div class="table-container"><table>')
            header = table_rows[0]
            html_lines.append('<thead><tr>')
            for cell in header:
                html_lines.append(f'<th>{cell}</th>')
            html_lines.append('</tr></thead><tbody>')
            for row in table_rows[1:]:
                html_lines.append('<tr>')
                for cell in row:
                    html_lines.append(f'<td>{cell}</td>')
                html_lines.append('</tr>')
            html_lines.append('</tbody></table></div>')
            table_rows = []
            in_table = False

    def flush_quote():
        nonlocal in_quote, quote_lines
        if in_quote and quote_lines:
            content = "<br/>".join(quote_lines)
            alert_class = "callout-note"
            if "[!WARNING]" in content or "[!CAUTION]" in content:
                alert_class = "callout-warning"
                content = content.replace("[!WARNING]", "<strong>WARNING:</strong>").replace("[!CAUTION]", "<strong>CAUTION:</strong>")
            elif "[!IMPORTANT]" in content:
                alert_class = "callout-important"
                content = content.replace("[!IMPORTANT]", "<strong>IMPORTANT:</strong>")
            elif "[!TIP]" in content:
                alert_class = "callout-tip"
                content = content.replace("[!TIP]", "<strong>TIP:</strong>")
            elif "[!NOTE]" in content:
                alert_class = "callout-note"
                content = content.replace("[!NOTE]", "<strong>NOTE:</strong>")
            html_lines.append(f'<div class="callout {alert_class}">{content}</div>')
            quote_lines = []
            in_quote = False

    def format_inline(text):
        text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
        text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
        text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
        text = re.sub(r'\$\$([^$]+)\$\$', r'<div class="math-display">\[\1\]</div>', text)
        text = re.sub(r'\$([^$]+)\$', r'<span class="math-inline">\(\1\)</span>', text)
        text = re.sub(r'\[([^\]]+)\]\(file:///[^)]+?\)', r'<strong>\1</strong>', text)
        text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
        return text

    for line in lines:
        stripped = line.strip()

        if line.startswith("```"):
            flush_list()
            flush_table()
            flush_quote()
            if in_code_block:
                escaped_code = html.escape("\n".join(code_content))
                html_lines.append(f'<pre><code class="language-{code_lang}">{escaped_code}</code></pre>')
                in_code_block = False
                code_content = []
                code_lang = ""
            else:
                in_code_block = True
                code_lang = line[3:].strip()
            continue

        if in_code_block:
            code_content.append(line)
            continue

        if "|" in line and (line.startswith("|") or line.strip().startswith("|")):
            flush_list()
            flush_quote()
            if re.match(r'^\s*\|(\s*[-:]+[-|\s:]*)\|\s*$', line):
                in_table = True
                continue
            parts = [format_inline(p.strip()) for p in line.strip().split("|")[1:-1]]
            if parts:
                in_table = True
                table_rows.append(parts)
            continue
        else:
            flush_table()

        if line.startswith("> "):
            flush_list()
            flush_table()
            in_quote = True
            quote_lines.append(format_inline(line[2:].strip()))
            continue
        else:
            flush_quote()

        if re.match(r'^\s*[-*]\s+', line):
            flush_table()
            flush_quote()
            if not in_list:
                in_list = True
                list_type = "ul"
                html_lines.append("<ul>")
            item_text = re.sub(r'^\s*[-*]\s+', '', line)
            html_lines.append(f"<li>{format_inline(item_text)}</li>")
            continue

        if re.match(r'^\s*\d+\.\s+', line):
            flush_table()
            flush_quote()
            if not in_list:
                in_list = True
                list_type = "ol"
                html_lines.append("<ol>")
            item_text = re.sub(r'^\s*\d+\.\s+', '', line)
            html_lines.append(f"<li>{format_inline(item_text)}</li>")
            continue

        flush_list()

        if line.startswith("# "):
            title = format_inline(line[2:].strip())
            html_lines.append(f'<h1 class="chapter-title">{title}</h1>')
            continue
        if line.startswith("## "):
            title = format_inline(line[3:].strip())
            html_lines.append(f'<h2 class="section-title">{title}</h2>')
            continue
        if line.startswith("### "):
            title = format_inline(line[4:].strip())
            html_lines.append(f'<h3 class="subsection-title">{title}</h3>')
            continue
        if line.startswith("#### "):
            title = format_inline(line[5:].strip())
            html_lines.append(f'<h4 class="subsubsection-title">{title}</h4>')
            continue

        if stripped in ["---", "***", "___"]:
            html_lines.append('<hr class="divider"/>')
            continue

        if not stripped:
            continue

        html_lines.append(f'<p>{format_inline(line)}</p>')

    flush_list()
    flush_table()
    flush_quote()

    return "\n".join(html_lines)


def build_consolidated_markdown():
    """Builds the single-file master manuscript in Markdown."""
    output_path = os.path.join(WORKSPACE, "THE_MAKERS_BIBLE_OF_ELECTROMECHANICAL_SALVAGE.md")
    
    manuscript = [
        "# THE MAKER'S BIBLE OF ELECTROMECHANICAL SALVAGE & REPURPOSING",
        "## The Complete 15-Volume Technical Handbook, Kinematics Manual & 50-Blueprint Compendium",
        f"**Compiled:** {datetime.now().strftime('%B %Y')} | **Edition:** 2.0 Master Collection (15 Volumes • 36 Chapters • 100 Donors • 50 Blueprints)\n",
        "> *\"Nothing is truly waste; it is merely raw engineering potential waiting for the right circuit, coupling, and imagination.\"*\n",
        "---\n",
        "## Table of Contents\n"
    ]
    
    chapter_num = 1
    for vol_title, chapters in CHAPTER_VOLUMES:
        manuscript.append(f"### {vol_title}")
        for rel_path, chap_title in chapters:
            anchor = f"chapter-{chapter_num}"
            manuscript.append(f"- [{chap_title}](#{anchor})")
            chapter_num += 1
        manuscript.append("")

    manuscript.append("\n---\n")

    chapter_num = 1
    for vol_title, chapters in CHAPTER_VOLUMES:
        manuscript.append(f"\n\n# ============================================================")
        manuscript.append(f"# {vol_title.upper()}")
        manuscript.append(f"# ============================================================\n")
        
        for rel_path, chap_title in chapters:
            full_path = find_chapter_path(rel_path)
            anchor = f"chapter-{chapter_num}"
            if full_path and os.path.exists(full_path):
                with open(full_path, "r", encoding="utf-8") as f:
                    content = f.read()
                manuscript.append(f"\n<a id=\"{anchor}\"></a>\n")
                manuscript.append(f"<!-- START CHAPTER {chapter_num}: {chap_title} -->\n")
                manuscript.append(content)
                manuscript.append(f"\n<!-- END CHAPTER {chapter_num} -->\n\n---\n")
            chapter_num += 1

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(manuscript))

    print(f"[OK] Master Markdown manuscript created: {output_path} ({os.path.getsize(output_path)} bytes)")
    return output_path


def build_standalone_html():
    """Builds a beautiful, self-contained standalone HTML eBook with sidebar and print CSS."""
    output_path = os.path.join(WORKSPACE, "THE_MAKERS_BIBLE_OF_ELECTROMECHANICAL_SALVAGE.html")
    
    toc_html = []
    content_html = []
    
    chapter_num = 1
    for vol_title, chapters in CHAPTER_VOLUMES:
        vol_id = f"vol-{chapter_num}"
        toc_html.append(f'<div class="nav-volume"><div class="nav-volume-title">{html.escape(vol_title)}</div><ul>')
        
        content_html.append(f'<div class="volume-cover-page" id="{vol_id}"><div class="vol-label">VOLUME</div><h1 class="vol-heading">{html.escape(vol_title)}</h1></div>')
        
        for rel_path, chap_title in chapters:
            chap_id = f"chap-{chapter_num}"
            toc_html.append(f'<li><a href="#{chap_id}"><span class="chap-badge">{chapter_num}</span> {html.escape(chap_title.split(": ")[-1])}</a></li>')
            
            full_path = find_chapter_path(rel_path)
            if full_path and os.path.exists(full_path):
                with open(full_path, "r", encoding="utf-8") as f:
                    md_text = f.read()
                
                chap_body = markdown_to_html(md_text, chap_id)
                content_html.append(f'<section class="chapter-container" id="{chap_id}">')
                content_html.append(f'<div class="chapter-header-badge">Chapter {chapter_num}</div>')
                content_html.append(chap_body)
                content_html.append('</section>')
                content_html.append('<div class="page-break"></div>')
            chapter_num += 1
            
        toc_html.append('</ul></div>')

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The Maker's Bible of Electromechanical Salvage &amp; Repurposing</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@300;400;500;600;700&family=Merriweather:ital,wght@0,300;0,400;0,700;1,300&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>

<style>
:root {{
  --bg-primary: #ffffff;
  --bg-secondary: #f8fafc;
  --bg-sidebar: #0f172a;
  --sidebar-text: #94a3b8;
  --sidebar-active: #38bdf8;
  --text-main: #1e293b;
  --text-muted: #64748b;
  --border: #e2e8f0;
  --accent: #2563eb;
  --code-bg: #1e293b;
  --code-text: #e2e8f0;
  --callout-note: #eff6ff;
  --callout-note-border: #3b82f6;
  --callout-warn: #fef2f2;
  --callout-warn-border: #ef4444;
  --callout-tip: #f0fdf4;
  --callout-tip-border: #22c55e;
}}

body.dark-mode {{
  --bg-primary: #0f172a;
  --bg-secondary: #1e293b;
  --text-main: #f1f5f9;
  --text-muted: #94a3b8;
  --border: #334155;
  --callout-note: #1e293b;
  --callout-note-border: #38bdf8;
  --callout-warn: #2d1515;
  --callout-warn-border: #f87171;
  --callout-tip: #132e1f;
  --callout-tip-border: #4ade80;
}}

* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  font-family: 'Merriweather', Georgia, serif;
  color: var(--text-main);
  background: var(--bg-primary);
  line-height: 1.8;
  font-size: 16px;
  display: flex;
}}

/* Sidebar navigation */
#sidebar {{
  width: 340px;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  background: var(--bg-sidebar);
  color: var(--sidebar-text);
  overflow-y: auto;
  font-family: 'Inter', sans-serif;
  padding: 24px 16px;
  z-index: 1000;
  border-right: 1px solid #1e293b;
}}

#sidebar-header {{
  padding-bottom: 20px;
  border-bottom: 1px solid #334155;
  margin-bottom: 20px;
}}
#sidebar-header h2 {{
  color: #f8fafc;
  font-size: 18px;
  font-weight: 700;
  line-height: 1.3;
}}
#sidebar-header p {{
  font-size: 12px;
  color: #64748b;
  margin-top: 6px;
}}

#search-box {{
  width: 100%;
  padding: 8px 12px;
  background: #1e293b;
  border: 1px solid #334155;
  border-radius: 6px;
  color: #f1f5f9;
  font-size: 13px;
  margin-bottom: 20px;
  outline: none;
}}
#search-box:focus {{ border-color: var(--sidebar-active); }}

.nav-volume {{
  margin-bottom: 20px;
}}
.nav-volume-title {{
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-weight: 700;
  color: #cbd5e1;
  margin-bottom: 8px;
}}
.nav-volume ul {{
  list-style: none;
}}
.nav-volume li a {{
  display: flex;
  align-items: center;
  padding: 6px 8px;
  color: var(--sidebar-text);
  text-decoration: none;
  font-size: 13px;
  border-radius: 4px;
  transition: all 0.15s ease;
  line-height: 1.4;
}}
.nav-volume li a:hover {{
  background: #1e293b;
  color: #f8fafc;
}}
.chap-badge {{
  display: inline-block;
  min-width: 20px;
  height: 20px;
  background: #334155;
  color: #94a3b8;
  border-radius: 3px;
  font-size: 10px;
  font-weight: 600;
  text-align: center;
  line-height: 20px;
  margin-right: 8px;
  flex-shrink: 0;
}}

/* Main Reading Content */
#main-content {{
  margin-left: 340px;
  flex: 1;
  max-width: 900px;
  padding: 60px 80px;
}}

/* Top reading bar */
#reading-bar {{
  display: flex;
  justify-content: flex-end;
  gap: 12px;
  margin-bottom: 40px;
  font-family: 'Inter', sans-serif;
}}
.btn {{
  padding: 6px 14px;
  background: var(--bg-secondary);
  border: 1px solid var(--border);
  border-radius: 6px;
  color: var(--text-main);
  font-size: 13px;
  cursor: pointer;
  font-weight: 500;
}}
.btn:hover {{ background: var(--border); }}

/* Book Title Page */
.book-cover {{
  text-align: center;
  padding: 80px 20px 100px;
  border-bottom: 2px solid var(--border);
  margin-bottom: 80px;
}}
.book-badge {{
  display: inline-block;
  padding: 6px 16px;
  background: #dbeafe;
  color: #1e40af;
  font-family: 'Inter', sans-serif;
  font-weight: 700;
  font-size: 12px;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  border-radius: 9999px;
  margin-bottom: 24px;
}}
.book-title {{
  font-family: 'Inter', sans-serif;
  font-size: 42px;
  font-weight: 800;
  line-height: 1.2;
  color: var(--text-main);
  margin-bottom: 16px;
}}
.book-subtitle {{
  font-size: 20px;
  color: var(--text-muted);
  font-style: italic;
  margin-bottom: 32px;
}}
.book-meta {{
  font-family: 'Inter', sans-serif;
  font-size: 14px;
  color: var(--text-muted);
}}

/* Volume divider cover page */
.volume-cover-page {{
  padding: 60px 0 30px;
  border-bottom: 3px solid var(--border);
  margin-top: 60px;
  margin-bottom: 50px;
}}
.vol-label {{
  font-family: 'Inter', sans-serif;
  font-size: 13px;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: var(--accent);
  font-weight: 700;
}}
.vol-heading {{
  font-family: 'Inter', sans-serif;
  font-size: 32px;
  font-weight: 700;
  color: var(--text-main);
  margin-top: 6px;
}}

/* Chapter Styling */
.chapter-container {{
  margin-bottom: 80px;
}}
.chapter-header-badge {{
  display: inline-block;
  font-family: 'Inter', sans-serif;
  font-size: 12px;
  font-weight: 700;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-bottom: 10px;
}}
.chapter-title {{
  font-family: 'Inter', sans-serif;
  font-size: 28px;
  font-weight: 700;
  line-height: 1.3;
  margin-bottom: 24px;
  color: var(--text-main);
}}
.section-title {{
  font-family: 'Inter', sans-serif;
  font-size: 22px;
  font-weight: 600;
  margin-top: 40px;
  margin-bottom: 16px;
  color: var(--text-main);
}}
.subsection-title {{
  font-family: 'Inter', sans-serif;
  font-size: 18px;
  font-weight: 600;
  margin-top: 28px;
  margin-bottom: 12px;
}}
.subsubsection-title {{
  font-family: 'Inter', sans-serif;
  font-size: 15px;
  font-weight: 600;
  margin-top: 20px;
  margin-bottom: 8px;
}}

p {{ margin-bottom: 20px; text-align: justify; }}
ul, ol {{ margin-bottom: 24px; padding-left: 28px; }}
li {{ margin-bottom: 8px; }}

pre {{
  background: var(--code-bg);
  color: var(--code-text);
  font-family: 'Fira Code', monospace;
  font-size: 13px;
  padding: 18px;
  border-radius: 8px;
  overflow-x: auto;
  margin-bottom: 24px;
  line-height: 1.6;
}}
code {{
  font-family: 'Fira Code', monospace;
  font-size: 0.9em;
  background: var(--bg-secondary);
  padding: 2px 6px;
  border-radius: 4px;
  border: 1px solid var(--border);
}}
pre code {{
  background: transparent;
  padding: 0;
  border: none;
}}

/* Tables */
.table-container {{
  width: 100%;
  overflow-x: auto;
  margin-bottom: 30px;
}}
table {{
  width: 100%;
  border-collapse: collapse;
  font-family: 'Inter', sans-serif;
  font-size: 13px;
}}
th, td {{
  padding: 10px 14px;
  border: 1px solid var(--border);
  text-align: left;
}}
th {{
  background: var(--bg-secondary);
  font-weight: 600;
}}

/* Callouts / Alerts */
.callout {{
  padding: 16px 20px;
  border-left: 4px solid;
  border-radius: 0 6px 6px 0;
  margin-bottom: 24px;
  font-size: 14.5px;
  font-family: 'Inter', sans-serif;
}}
.callout-note {{ background: var(--callout-note); border-color: var(--callout-note-border); }}
.callout-warning {{ background: var(--callout-warn); border-color: var(--callout-warn-border); }}
.callout-tip {{ background: var(--callout-tip); border-color: var(--callout-tip-border); }}
.callout-important {{ background: #fffbeb; border-color: #f59e0b; }}

.divider {{
  border: none;
  border-top: 1px solid var(--border);
  margin: 40px 0;
}}

/* Print stylesheet for instant high-res PDF generation */
@media print {{
  #sidebar, #reading-bar {{ display: none !important; }}
  #main-content {{ margin-left: 0 !important; padding: 0 !important; max-width: 100% !important; }}
  body {{ font-size: 11pt; color: #000; background: #fff; }}
  .page-break {{ page-break-after: always; break-after: page; }}
  .chapter-container {{ page-break-before: always; break-before: page; }}
  pre, table, .callout {{ page-break-inside: avoid; }}
}}
</style>
</head>
<body>

<nav id="sidebar">
  <div id="sidebar-header">
    <h2>The Maker's Bible</h2>
    <p>Electromechanical Salvage &amp; Repurposing</p>
  </div>
  <input type="text" id="search-box" placeholder="Filter chapters &amp; topics..." onkeyup="filterNav()">
  <div id="nav-tree">
    {''.join(toc_html)}
  </div>
</nav>

<main id="main-content">
  <div id="reading-bar">
    <button class="btn" onclick="toggleTheme()">Toggle Theme</button>
    <button class="btn" onclick="window.print()">Print to PDF</button>
  </div>

  <div class="book-cover">
    <div class="book-badge">The Complete Handbook</div>
    <h1 class="book-title">THE MAKER'S BIBLE OF ELECTROMECHANICAL SALVAGE &amp; REPURPOSING</h1>
    <div class="book-subtitle">A Comprehensive Engineering Manual for Harvesting, Kinematic Design, Power Electronics, and Hardware Hacking</div>
    <div class="book-meta">
      <strong>15 Volumes (Vol 00–14) &bull; 36 Comprehensive Chapters &bull; 50 Engineering Blueprints (Builds 1–50) &bull; 88 Master Donor Streams</strong><br>
      Published {datetime.now().strftime('%B %Y')} &bull; Open-Source Maker Edition
    </div>
  </div>

  {''.join(content_html)}
</main>

<script>
function toggleTheme() {{
  document.body.classList.toggle('dark-mode');
}}

function filterNav() {{
  const query = document.getElementById('search-box').value.toLowerCase();
  const items = document.querySelectorAll('.nav-volume li');
  items.forEach(li => {{
    const text = li.innerText.toLowerCase();
    li.style.display = text.includes(query) ? '' : 'none';
  }});
}}
</script>

</body>
</html>
"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"[OK] Standalone HTML eBook created: {output_path} ({os.path.getsize(output_path)} bytes)")
    return output_path


def build_epub():
    """Compiles a standards-compliant EPUB 3 digital book."""
    epub_path = os.path.join(WORKSPACE, "THE_MAKERS_BIBLE_OF_ELECTROMECHANICAL_SALVAGE.epub")
    
    # We will build files into an in-memory or temporary structure then zip
    epub_id = str(uuid.uuid4())
    
    # 1. Mimetype (must be uncompressed and the first entry in zip)
    # We'll use ZipFile
    with zipfile.ZipFile(epub_path, "w", zipfile.ZIP_DEFLATED) as z:
        # Write mimetype uncompressed
        z.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        
        # 2. META-INF/container.xml
        container_xml = """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>"""
        z.writestr("META-INF/container.xml", container_xml)
        
        # 3. Stylesheet
        css = """
body { font-family: serif; line-height: 1.6; margin: 5%; color: #111; }
h1, h2, h3 { font-family: sans-serif; color: #0f172a; }
pre { background: #f1f5f9; padding: 10px; border-radius: 5px; font-family: monospace; font-size: 0.85em; }
code { font-family: monospace; background: #e2e8f0; padding: 2px 4px; }
table { width: 100%; border-collapse: collapse; margin: 15px 0; font-size: 0.85em; font-family: sans-serif; }
th, td { border: 1px solid #cbd5e1; padding: 6px 10px; text-align: left; }
th { background: #f8fafc; font-weight: bold; }
.callout { border-left: 4px solid #3b82f6; background: #eff6ff; padding: 10px 14px; margin: 15px 0; }
"""
        z.writestr("OEBPS/styles.css", css)
        
        manifest_items = []
        spine_items = []
        ncx_points = []
        
        manifest_items.append('<item id="css" href="styles.css" media-type="text/css"/>')
        manifest_items.append('<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>')
        manifest_items.append('<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>')
        manifest_items.append('<item id="cover" href="cover.xhtml" media-type="application/xhtml+xml"/>')
        spine_items.append('<itemref idref="cover"/>')
        
        # Cover XHTML
        cover_xhtml = f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Cover</title>
<link rel="stylesheet" type="text/css" href="styles.css"/>
</head>
<body style="text-align: center; margin-top: 20%;">
  <h1 style="font-size: 2em;">THE MAKER'S BIBLE OF ELECTROMECHANICAL SALVAGE &amp; REPURPOSING</h1>
  <p style="font-size: 1.2em; color: #475569; font-style: italic;">The Complete 15-Volume Technical Handbook &amp; 50 Engineering Blueprints</p>
  <p style="margin-top: 40px; font-size: 0.9em; color: #64748b;">Edition 2.0 &bull; 100 Donors &bull; {datetime.now().strftime('%B %Y')}</p>
</body>
</html>"""
        z.writestr("OEBPS/cover.xhtml", cover_xhtml)
        
        chapter_num = 1
        nav_li = []
        
        for vol_title, chapters in CHAPTER_VOLUMES:
            for rel_path, chap_title in chapters:
                chap_id = f"chap_{chapter_num}"
                file_name = f"{chap_id}.xhtml"
                
                full_path = find_chapter_path(rel_path)
                if full_path and os.path.exists(full_path):
                    with open(full_path, "r", encoding="utf-8") as f:
                        md_text = f.read()
                    
                    chap_html = markdown_to_html(md_text, chap_id)
                    
                    xhtml_content = f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>{html.escape(chap_title)}</title>
<link rel="stylesheet" type="text/css" href="styles.css"/>
</head>
<body>
<div class="volume-header" style="color: #64748b; font-size: 0.85em; font-family: sans-serif; text-transform: uppercase;">{html.escape(vol_title)}</div>
{chap_html}
</body>
</html>"""
                    z.writestr(f"OEBPS/{file_name}", xhtml_content)
                    
                    manifest_items.append(f'<item id="{chap_id}" href="{file_name}" media-type="application/xhtml+xml"/>')
                    spine_items.append(f'<itemref idref="{chap_id}"/>')
                    
                    nav_li.append(f'<li><a href="{file_name}">{html.escape(chap_title)}</a></li>')
                    ncx_points.append(f"""  <navPoint id="navPoint-{chapter_num}" playOrder="{chapter_num}">
    <navLabel><text>{html.escape(chap_title)}</text></navLabel>
    <content src="{file_name}"/>
  </navPoint>""")
                    
                chapter_num += 1

        # Nav XHTML (EPUB 3)
        nav_xhtml = f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head>
<title>Table of Contents</title>
<link rel="stylesheet" type="text/css" href="styles.css"/>
</head>
<body>
<nav epub:type="toc" id="toc">
  <h1>Table of Contents</h1>
  <ol>
    {''.join(nav_li)}
  </ol>
</nav>
</body>
</html>"""
        z.writestr("OEBPS/nav.xhtml", nav_xhtml)
        
        # NCX (EPUB 2 compatibility)
        toc_ncx = f"""<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head>
    <meta name="dtb:uid" content="urn:uuid:{epub_id}"/>
    <meta name="dtb:depth" content="1"/>
    <meta name="dtb:totalPageCount" content="0"/>
    <meta name="dtb:maxPageNumber" content="0"/>
  </head>
  <docTitle>
    <text>The Maker's Bible of Electromechanical Salvage</text>
  </docTitle>
  <navMap>
{''.join(ncx_points)}
  </navMap>
</ncx>"""
        z.writestr("OEBPS/toc.ncx", toc_ncx)

        # content.opf
        content_opf = f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="BookID" version="3.0">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:title>The Maker's Bible of Electromechanical Salvage &amp; Repurposing</dc:title>
    <dc:creator>Open-Source Maker Community &amp; Antigravity</dc:creator>
    <dc:identifier id="BookID">urn:uuid:{epub_id}</dc:identifier>
    <dc:language>en</dc:language>
    <meta property="dcterms:modified">{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}</meta>
  </metadata>
  <manifest>
    {''.join(manifest_items)}
  </manifest>
  <spine toc="ncx">
    {''.join(spine_items)}
  </spine>
</package>"""
        z.writestr("OEBPS/content.opf", content_opf)

    print(f"[OK] Compliant EPUB eBook created: {epub_path} ({os.path.getsize(epub_path)} bytes)")
    return epub_path


if __name__ == "__main__":
    print("=== BUILDING EBOOK EDITIONS ===")
    md_file = build_consolidated_markdown()
    html_file = build_standalone_html()
    epub_file = build_epub()
    print("=== ALL EDITIONS COMPILED SUCCESSFULLY ===")
