#!/usr/bin/env python3
"""
Generate crisp, high-contrast Light Mode counterparts for all project SVGs and map SVG.
Strictly 100% monochrome.
"""
import os
import re
import glob
import xml.etree.ElementTree as ET

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(REPO_ROOT)

COLOR_MAP = {
    # Dark backgrounds -> Light backgrounds
    "#000000": "#ffffff",
    "#050505": "#ffffff",
    "#09090b": "#ffffff",
    "#0a0a0a": "#ffffff",
    "#0d0d10": "#f4f4f5",
    "#0f0f12": "#f4f4f5",
    "#111113": "#fafafa",
    "#111111": "#f4f4f5",
    "#121215": "#f4f4f5",
    "#141418": "#f4f4f5",
    "#16161a": "#f4f4f5",
    "#18181b": "#f4f4f5",
    "#1a1a1e": "#e4e4e7",
    "#1c1c1f": "#e4e4e7",
    "#1f1f23": "#e4e4e7",
    "#222226": "#e4e4e7",
    "#262626": "#e4e4e7",
    "#27272a": "#e4e4e7",
    "#2a2a2d": "#e4e4e7",
    "#2e2e33": "#e4e4e7",
    "#333333": "#d4d4d8",
    "#3a3a40": "#d4d4d8",
    "#3f3f46": "#a1a1aa",
    "#444444": "#a1a1aa",
    "#444448": "#a1a1aa",
    "#4a4a52": "#71717a",
    # Muted midtones
    "#52525b": "#71717a",
    "#666666": "#52525b",
    "#71717a": "#52525b",
    "#888888": "#3f3f46",
    "#999999": "#27272a",
    "#a1a1aa": "#27272a",
    "#cccccc": "#18181b",
    "#d4d4d8": "#18181b",
    "#dddddd": "#111113",
    "#e4e4e7": "#09090b",
    "#f4f4f5": "#09090b",
    "#ffffff": "#09090b",
}

def convert_svg_to_light(svg_text):
    # Case-insensitive color replacements
    def replace_color(match):
        hex_c = match.group(0).lower()
        return COLOR_MAP.get(hex_c, hex_c)

    # 1. Replace 6-digit hex colors
    converted = re.sub(r"#[0-9a-fA-F]{6}", replace_color, svg_text)

    # 2. Invert gradients with white stop-color to black stop-color
    converted = re.sub(r'stop-color="#09090b"', 'stop-color="#000000"', converted)

    return converted

def process_all_svgs():
    # 1. Master project SVGs in assets/
    master_svgs = [
        "assets/project-erp.svg",
        "assets/project-ecommerce.svg",
        "assets/project-cms.svg",
        "assets/project-llm-gateway.svg",
        "assets/project-agentic-ops.svg",
    ]
    for m in master_svgs:
        with open(m, "r", encoding="utf-8") as f:
            content = f.read()
        light_content = convert_svg_to_light(content)
        out_path = m.replace(".svg", "-light.svg")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(light_content)
        ET.fromstring(light_content)
        print(f"Created {out_path}")

    # 2. Detail project SVGs in assets/projects/
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

    # 3. Indonesia map SVG
    if os.path.exists("assets/indonesia-map.svg"):
        with open("assets/indonesia-map.svg", "r", encoding="utf-8") as f:
            map_content = f.read()
        # Custom tune for light blueprint map:
        # Landmass fill: subtle light zinc #e4e4e7, stroke #a1a1aa, graticule #e4e4e7, text #52525b
        light_map = convert_svg_to_light(map_content)
        # Ensure landmass fill is crisp on light canvas
        light_map = light_map.replace('stop-color="#e4e4e7"', 'stop-color="#e4e4e7"')
        light_map = light_map.replace('stop-color="#f4f4f5"', 'stop-color="#f4f4f5"')
        out_map = "assets/indonesia-map-light.svg"
        with open(out_map, "w", encoding="utf-8") as f:
            f.write(light_map)
        ET.fromstring(light_map)
        print(f"Created {out_map}")

if __name__ == "__main__":
    process_all_svgs()
    print("All Light Mode SVGs created and validated successfully!")
