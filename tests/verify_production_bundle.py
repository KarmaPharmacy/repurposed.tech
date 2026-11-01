"""
Verification suite for the repurposed.tech production distribution bundle.
Validates the complete integrity of dist/ before cloud deployment.
"""

import os
import sys
import json
import xml.etree.ElementTree as ET

WORKSPACE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DIST_DIR = os.path.join(WORKSPACE, "dist")

def test_production_bundle():
    print("=== STARTING REPURPOSED.TECH PRODUCTION BUNDLE VERIFICATION ===")
    assert os.path.exists(DIST_DIR), f"Dist directory does not exist: {DIST_DIR}"

    # 1. dist/index.html checks
    index_path = os.path.join(DIST_DIR, "index.html")
    assert os.path.exists(index_path), "dist/index.html is missing"
    with open(index_path, "r", encoding="utf-8") as f:
        index_content = f.read()

    size_mb = len(index_content.encode("utf-8")) / (1024 * 1024)
    print(f"[OK] dist/index.html exists ({size_mb:.2f} MB)")
    assert size_mb > 0.8, f"index.html unexpectedly small: {size_mb} MB"

    assert "REPURPOSED &bull; The Maker's Bible" in index_content, "Custom domain title missing"
    assert '<link rel="canonical" href="https://repurposed.tech/">' in index_content, "Canonical link missing"
    assert 'property="og:site_name" content="repurposed.tech"' in index_content, "OG site_name missing"
    assert 'content="https://repurposed.tech/assets/og-card.png"' in index_content, "OG card image missing"
    assert 'name="twitter:domain" content="repurposed.tech"' in index_content, "Twitter domain missing"
    assert 'href="/manifest.json"' in index_content, "Manifest link missing"
    assert 'href="/favicon.svg"' in index_content, "Favicon SVG missing"
    assert 'href="/favicon.ico"' in index_content, "Favicon ICO missing"
    assert 'const BLUEPRINTS = [' in index_content and 'const DONORS = [' in index_content, "Embedded datasets missing"
    assert 'id="view-compendium"' in index_content and 'id="view-blueprints"' in index_content and 'id="view-atlas"' in index_content, "Core 3 modern views missing"
    assert 'id="view-lab"' not in index_content and 'id="view-mindmaze"' not in index_content and 'id="view-xray"' not in index_content, "Stripped chaff still present"
    print("[OK] dist/index.html modern UI, metadata, canonical, OpenGraph, and datasets verified")

    # 2. dist/ebook.html checks
    ebook_path = os.path.join(DIST_DIR, "ebook.html")
    assert os.path.exists(ebook_path), "dist/ebook.html is missing"
    with open(ebook_path, "r", encoding="utf-8") as f:
        ebook_content = f.read()
    assert '<link rel="canonical" href="https://repurposed.tech/ebook.html">' in ebook_content, "eBook canonical missing"
    assert "RETURN TO REPURPOSED.TECH TERMINAL" in ebook_content or "Return to REPURPOSED.TECH" in ebook_content, "Back button missing in eBook"
    print(f"[OK] dist/ebook.html verified ({len(ebook_content) / 1024:.1f} KB)")

    # 3. Downloads directory checks
    downloads_dir = os.path.join(DIST_DIR, "downloads")
    epub_file = os.path.join(downloads_dir, "the-makers-bible-of-electromechanical-salvage.epub")
    md_file = os.path.join(downloads_dir, "the-makers-bible-of-electromechanical-salvage.md")
    comp_file = os.path.join(downloads_dir, "salvage-compendium.md")

    assert os.path.exists(epub_file) and os.path.getsize(epub_file) > 200000, "EPUB download missing or small"
    assert os.path.exists(md_file) and os.path.getsize(md_file) > 500000, "Markdown manuscript download missing or small"
    assert os.path.exists(comp_file) and os.path.getsize(comp_file) > 50000, "Compendium download missing or small"
    print(f"[OK] dist/downloads/ verified (EPUB: {os.path.getsize(epub_file)/1024:.1f} KB, MD: {os.path.getsize(md_file)/1024:.1f} KB, Compendium: {os.path.getsize(comp_file)/1024:.1f} KB)")

    # 4. Branding assets checks
    fav_svg = os.path.join(DIST_DIR, "favicon.svg")
    fav_ico = os.path.join(DIST_DIR, "favicon.ico")
    touch_png = os.path.join(DIST_DIR, "assets", "apple-touch-icon.png")
    og_png = os.path.join(DIST_DIR, "assets", "og-card.png")
    og_svg = os.path.join(DIST_DIR, "assets", "og-card.svg")

    assert os.path.exists(fav_svg), "favicon.svg missing"
    assert os.path.exists(fav_ico), "favicon.ico missing"
    with open(fav_ico, "rb") as f:
        ico_head = f.read(4)
        assert ico_head == b"\x00\x00\x01\x00", "favicon.ico header invalid"

    assert os.path.exists(touch_png), "apple-touch-icon.png missing"
    with open(touch_png, "rb") as f:
        png_sig = f.read(8)
        assert png_sig == b"\x89PNG\r\n\x1a\n", "apple-touch-icon.png invalid PNG signature"

    assert os.path.exists(og_png), "og-card.png missing"
    with open(og_png, "rb") as f:
        png_sig = f.read(8)
        assert png_sig == b"\x89PNG\r\n\x1a\n", "og-card.png invalid PNG signature"

    assert os.path.exists(og_svg), "og-card.svg missing"
    print("[OK] Branding assets verified (SVG, ICO, Apple Touch PNG, OpenGraph banner)")

    # 5. PWA Manifest & Robots & Sitemap checks
    manifest_path = os.path.join(DIST_DIR, "manifest.json")
    assert os.path.exists(manifest_path), "manifest.json missing"
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest_data = json.load(f)
    assert "REPURPOSED" in manifest_data.get("name"), "Manifest name mismatch"
    assert "ENCARTA" not in manifest_data.get("name"), "Legacy Encarta in manifest name"
    assert manifest_data.get("display") == "standalone", "Manifest display mismatch"
    print("[OK] PWA manifest.json valid JSON and schema verified")

    robots_path = os.path.join(DIST_DIR, "robots.txt")
    with open(robots_path, "r", encoding="utf-8") as f:
        robots_txt = f.read()
    assert "https://repurposed.tech/sitemap.xml" in robots_txt, "Robots.txt missing sitemap URL"
    print("[OK] dist/robots.txt verified")

    sitemap_path = os.path.join(DIST_DIR, "sitemap.xml")
    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    urls = [elem.text for elem in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
    assert "https://repurposed.tech/" in urls, "Sitemap root missing"
    assert "https://repurposed.tech/ebook.html" in urls, "Sitemap ebook missing"
    print(f"[OK] dist/sitemap.xml parsed and verified ({len(urls)} URLs mapped)")

    # 6. 404 & Hosting Configurations
    assert os.path.exists(os.path.join(DIST_DIR, "404.html")), "404.html missing"
    
    cname_path = os.path.join(DIST_DIR, "CNAME")
    assert os.path.exists(cname_path), "CNAME file missing"
    with open(cname_path, "r", encoding="utf-8") as f:
        assert f.read().strip() == "repurposed.tech", "CNAME content mismatch"

    assert os.path.exists(os.path.join(DIST_DIR, "_headers")), "_headers missing"
    assert os.path.exists(os.path.join(DIST_DIR, "_redirects")), "_redirects missing"
    
    vercel_path = os.path.join(DIST_DIR, "vercel.json")
    with open(vercel_path, "r", encoding="utf-8") as f:
        v_data = json.load(f)
    assert v_data.get("cleanUrls") is True, "vercel.json cleanUrls missing"

    firebase_path = os.path.join(WORKSPACE, "firebase.json")
    with open(firebase_path, "r", encoding="utf-8") as f:
        fb_data = json.load(f)
    assert fb_data.get("hosting", {}).get("public") == "dist", "firebase.json public directory mismatch"

    print("[OK] Host configs verified (CNAME, _headers, _redirects, vercel.json, firebase.json)")
    print("=== ALL PRODUCTION BUNDLE VERIFICATION CHECKS PASSED ===")

if __name__ == "__main__":
    test_production_bundle()
