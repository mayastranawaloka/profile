#!/usr/bin/env python3
"""
Generate crisp, high-contrast Light Mode counterparts for all project SVGs and map SVG.
Strictly 100% monochrome. Maps every dark hex value cleanly to light mode.
"""
import os
import re
import glob
import xml.etree.ElementTree as ET

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(REPO_ROOT)

# Comprehensive color mapping for all 41 hex colors
COLOR_MAP = {
    # 1. Deepest canvas backgrounds -> Pure white canvas
    "#000000": "#ffffff",
    "#050505": "#ffffff",
    "#09090b": "#ffffff",
    "#0a0a0a": "#ffffff",
    "#0a0a0c": "#ffffff",

    # 2. Elevated panels, drawers, sidebars, headers, cards -> Crisp light surfaces
    "#0c0c0e": "#f4f4f5",
    "#0d0d10": "#fafafa",
    "#0f0f12": "#f4f4f5",
    "#101013": "#fafafa",
    "#111113": "#f4f4f5",
    "#111114": "#ffffff", # Editor / central document canvas
    "#121215": "#fafafa",
    "#121216": "#f4f4f5",
    "#141418": "#fafafa",
    "#151518": "#f4f4f5",
    "#16161a": "#f4f4f5",
    "#16161c": "#fafafa",
    "#18181b": "#f4f4f5",
    "#18181c": "#f4f4f5",
    "#18181e": "#f4f4f5",
    "#18181f": "#f4f4f5",
    "#1a1a1e": "#f4f4f5",
    "#1b1b20": "#f4f4f5",
    "#1c1c1f": "#f4f4f5",
    "#1c1c22": "#f4f4f5",
    "#1c1c24": "#f4f4f5",
    "#1e1e24": "#f4f4f5",
    "#1f1f23": "#f4f4f5",

    # 3. Borders, divider lines, strokes, subtle geometry
    "#222226": "#e4e4e7",
    "#22222a": "#e4e4e7",
    "#24242c": "#e4e4e7",
    "#262626": "#e4e4e7",
    "#26262e": "#e4e4e7",
    "#27272a": "#e4e4e7",
    "#292932": "#e4e4e7",
    "#292934": "#e4e4e7",
    "#2a2a2d": "#e4e4e7",
    "#2d2d34": "#e4e4e7",
    "#2e2e33": "#e4e4e7",
    "#323238": "#e4e4e7",
    "#333333": "#d4d4d8",
    "#3a3a40": "#d4d4d8",

    # 4. Muted icons, tertiary markers, inactive tags
    "#3f3f46": "#a1a1aa",
    "#444444": "#a1a1aa",
    "#444448": "#a1a1aa",
    "#4a4a52": "#71717a",
    "#52525b": "#71717a",
    "#666666": "#71717a",

    # 5. Metadata, captions, secondary labels
    "#71717a": "#71717a",
    "#888888": "#52525b",

    # 6. Body text, regular content
    "#999999": "#3f3f46",
    "#a1a1aa": "#27272a",

    # 7. Section titles, bold values, prices
    "#cccccc": "#18181b",
    "#d4d4d8": "#18181b",
    "#dddddd": "#111113",

    # 8. High-contrast titles, active items, action buttons -> Solid dark
    "#e4e4e7": "#09090b",
    "#f4f4f5": "#09090b",
    "#ffffff": "#09090b",

    # 9. Refined Brand Red Accents -> Crisp Ruby Carmine in Light Mode
    "#ef4444": "#dc2626",
    "#dc2626": "#dc2626",
    "#fefefe": "#ffffff",
}

def convert_svg_to_light(svg_text):
    def replace_color(match):
        hex_c = match.group(0).lower()
        return COLOR_MAP.get(hex_c, hex_c)

    # Replace all 6-digit hex colors in one pass
    converted = re.sub(r"#[0-9a-fA-F]{6}", replace_color, svg_text)

    # Gradients with stop-color adjustments
    converted = re.sub(r'stop-color="#09090b"', 'stop-color="#000000"', converted)

    return converted

def process_all_svgs():
    # 1. Project SVGs in assets/projects/ (both showcases and screen details)
    detail_svgs = glob.glob("assets/projects/**/*.svg", recursive=True)
    for d in detail_svgs:
        with open(d, "r", encoding="utf-8") as f:
            content = f.read()
        light_content = convert_svg_to_light(content)
        out_path = d.replace("assets/projects/", "assets/projects-light/")
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(light_content)
        ET.fromstring(light_content)
        print(f"Created {out_path}")

    # 2. Indonesia map SVG (Daytime mode: omit dark mode night lights)
    if os.path.exists("assets/maps/indonesia-map.svg"):
        with open("assets/maps/indonesia-map.svg", "r", encoding="utf-8") as f:
            map_content = f.read()
        # Strip dark-mode specific night lights and city blooms for clean daytime map
        clean_daytime_map = re.sub(r'\s*<!-- Metropolitan Night Glow Bloom[\s\S]*?<!-- Blueprint Geodetic Markers -->', '\n  <!-- Blueprint Geodetic Markers -->', map_content)
        clean_daytime_map = re.sub(r'\s*<!-- Realistic City Night Light Radial Bloom Gradient[\s\S]*?</style>', '', clean_daytime_map)
        light_map = convert_svg_to_light(clean_daytime_map)
        out_map = "assets/maps/indonesia-map-light.svg"
        with open(out_map, "w", encoding="utf-8") as f:
            f.write(light_map)
        ET.fromstring(light_map)
        print(f"Created {out_map}")

if __name__ == "__main__":
    process_all_svgs()
    print("All Light Mode SVGs created and validated successfully!")
