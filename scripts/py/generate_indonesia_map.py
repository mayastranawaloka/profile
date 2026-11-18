#!/usr/bin/env python3
"""
Generate a strict monochrome, high-precision architectural blueprint SVG map
of the Indonesian archipelago for the Hero underlay.
"""
import json
import xml.etree.ElementTree as ET

def generate_svg():
    with open("scratch_idn.json", "r") as f:
        data = json.load(f)

    # Canvas dimensions
    width = 1200
    height = 500

    # Margins and map bounds
    pad_x = 60
    pad_y = 65
    map_w = width - (pad_x * 2)
    map_h = height - (pad_y * 2)

    # Geo bounding box for Indonesia
    lon_min = 95.0
    lon_max = 141.0
    lat_min = -11.0
    lat_max = 6.0

    lon_span = lon_max - lon_min
    lat_span = lat_max - lat_min

    def project(lon, lat):
        x = pad_x + ((lon - lon_min) / lon_span) * map_w
        # Invert y because SVG y goes downwards while latitude goes upwards
        y = pad_y + ((lat_max - lat) / lat_span) * map_h
        return round(x, 2), round(y, 2)

    svg_parts = []
    svg_parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" fill="none" preserveAspectRatio="xMidYMid meet">')
    
    # 1. Defs for gradients, patterns, and filters (Strict Monochrome)
    svg_parts.append('''  <defs>
    <!-- Blueprint micro-dot grid pattern -->
    <pattern id="geoGrid" width="32" height="32" patternUnits="userSpaceOnUse">
      <circle cx="16" cy="16" r="0.8" fill="#333333" />
    </pattern>
    <!-- Island fill gradient (pure neutral dark zinc) -->
    <linearGradient id="islandGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2a2a2d" />
      <stop offset="100%" stop-color="#18181b" />
    </linearGradient>
  </defs>''')

    # 2. Background container & subtle grid
    svg_parts.append(f'  <rect width="{width}" height="{height}" fill="transparent" />')
    svg_parts.append(f'  <rect width="{width}" height="{height}" fill="url(#geoGrid)" opacity="0.45" />')

    # 3. Graticule / Blueprint Lat-Lon Grid Lines
    svg_parts.append('  <!-- Graticule Lines -->')
    svg_parts.append('  <g class="graticule" stroke="#262626" stroke-width="0.8" stroke-dasharray="3 4">')
    for lon in [100, 110, 120, 130, 140]:
        gx, _ = project(lon, 0)
        svg_parts.append(f'    <line x1="{gx}" y1="{pad_y - 20}" x2="{gx}" y2="{height - pad_y + 20}" />')
    for lat in [5, -5, -10]:
        _, gy = project(0, lat)
        svg_parts.append(f'    <line x1="{pad_x - 30}" y1="{gy}" x2="{width - pad_x + 30}" y2="{gy}" />')
    svg_parts.append('  </g>')

    # Equator line (Solid, slightly accentuated)
    _, eq_y = project(0, 0)
    svg_parts.append(f'  <!-- Equator Line (0° Latitude) -->')
    svg_parts.append(f'  <line x1="{pad_x - 40}" y1="{eq_y}" x2="{width - pad_x + 40}" y2="{eq_y}" stroke="#3f3f46" stroke-width="1.2" stroke-dasharray="8 6" />')
    svg_parts.append(f'  <text x="{pad_x - 35}" y="{eq_y - 6}" font-family="monospace" font-size="9" fill="#52525b" letter-spacing="1">00° 00\' 00" EQUATOR</text>')

    # Graticule Labels
    svg_parts.append('  <!-- Graticule Labels -->')
    svg_parts.append('  <g font-family="monospace" font-size="9" fill="#52525b">')
    for lon in [100, 110, 120, 130, 140]:
        gx, _ = project(lon, 0)
        svg_parts.append(f'    <text x="{gx}" y="{pad_y - 26}" text-anchor="middle">{lon}°E</text>')
        svg_parts.append(f'    <text x="{gx}" y="{height - pad_y + 34}" text-anchor="middle">{lon}°E</text>')
    for lat in [5, -5, -10]:
        _, gy = project(0, lat)
        label = f"{lat}°N" if lat > 0 else f"{abs(lat)}°S"
        svg_parts.append(f'    <text x="{width - pad_x + 36}" y="{gy + 3}" text-anchor="start">{label}</text>')
    svg_parts.append('  </g>')

    # 4. Island Polygons
    svg_parts.append('  <!-- Indonesian Archipelago Landmasses -->')
    svg_parts.append('  <g id="landmasses" fill="url(#islandGrad)" stroke="#444448" stroke-width="0.9" stroke-linejoin="round">')

    coords_list = data["geometry"]["coordinates"]
    for poly in coords_list:
        path_data = []
        for ring in poly:
            if not ring:
                continue
            first_pt = ring[0]
            sx, sy = project(first_pt[0], first_pt[1])
            ring_cmds = [f"M {sx} {sy}"]
            for pt in ring[1:]:
                px, py = project(pt[0], pt[1])
                ring_cmds.append(f"L {px} {py}")
            ring_cmds.append("Z")
            path_data.append(" ".join(ring_cmds))
        if path_data:
            svg_parts.append(f'    <path d="{" ".join(path_data)}" />')
    svg_parts.append('  </g>')

    # 5. Strategic Geopolitical Blueprint Reference Markers (Crosshairs & Coordinates)
    markers = [
        ("SABANG", 95.31, 5.89, "05°53'N 95°18'E", 0, -12),
        ("JAKARTA", 106.84, -6.20, "06°12'S 106°50'E", 0, 16),
        ("NUSANTARA", 116.98, -0.97, "00°58'S 116°59'E // IKN", 0, -12),
        ("MAKASSAR", 119.42, -5.14, "05°08'S 119°25'E", 0, 16),
        ("MIANGAS", 126.58, 5.55, "05°33'N 126°35'E", 0, -12),
        ("ROTE", 123.13, -10.82, "10°49'S 123°08'E", 0, 16),
        ("JAYAPURA", 140.71, -2.53, "02°32'S 140°42'E", 0, -12),
        ("MERAUKE", 140.34, -8.49, "08°29'S 140°20'E", 0, 16),
    ]

    svg_parts.append('  <!-- Blueprint Geodetic Markers -->')
    svg_parts.append('  <g class="markers">')
    for name, m_lon, m_lat, coord_str, off_x, off_y in markers:
        mx, my = project(m_lon, m_lat)
        # Crosshair '+'
        svg_parts.append(f'    <path d="M {mx - 4} {my} L {mx + 4} {my} M {mx} {my - 4} L {mx} {my + 4}" stroke="#71717a" stroke-width="1.2" />')
        # Pin dot
        svg_parts.append(f'    <circle cx="{mx}" cy="{my}" r="1.5" fill="#ffffff" />')
        # Text
        anchor = "middle"
        if mx < pad_x + 80:
            anchor = "start"
        elif mx > width - pad_x - 80:
            anchor = "end"
        svg_parts.append(f'    <text x="{mx + off_x}" y="{my + off_y}" font-family="monospace" font-size="8.5" fill="#a1a1aa" text-anchor="{anchor}" font-weight="600" letter-spacing="0.5">{name}</text>')
        svg_parts.append(f'    <text x="{mx + off_x}" y="{my + off_y + (8 if off_y > 0 else -8)}" font-family="monospace" font-size="7" fill="#52525b" text-anchor="{anchor}">{coord_str}</text>')
    svg_parts.append('  </g>')

    # 6. Technical Blueprint Framing & Metadata Annotations
    svg_parts.append('  <!-- Architectural CAD Metadata Block -->')
    svg_parts.append(f'  <g font-family="monospace" font-size="8" fill="#52525b" letter-spacing="1">')
    svg_parts.append(f'    <text x="{pad_x - 35}" y="{height - 18}">DATUM: WGS-84 // ARCHIPELAGIC TERRITORY OF THE REPUBLIC OF INDONESIA</text>')
    svg_parts.append(f'    <text x="{width - pad_x + 35}" y="{height - 18}" text-anchor="end">COORD: 95°00\'00"E - 141°00\'00"E // 06°00\'00"N - 11°00\'00"S</text>')
    svg_parts.append('  </g>')

    svg_parts.append('</svg>')

    full_svg = "\n".join(svg_parts)
    output_path = "assets/indonesia-map.svg"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_svg)
    print(f"Generated {output_path} successfully ({len(full_svg)} bytes).")

    # Validate XML
    ET.fromstring(full_svg)
    print("XML validation passed cleanly!")

if __name__ == "__main__":
    generate_svg()
