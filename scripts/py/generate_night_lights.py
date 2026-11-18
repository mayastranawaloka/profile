#!/usr/bin/env python3
"""
Generate realistic Indonesian population density night lights for assets/indonesia-map.svg.
Based on real demographic distribution (BPS Indonesia):
- Java (~56% of population): Dense continuous chains (Jabodetabek, Bandung Raya, Pantura, Joglosemar, Gerbangkertosusilo, Malang Raya)
- Sumatra (~21%): Medan-Deli, Palembang, Lampung, Pekanbaru, Batam, Padang
- Bali & Nusa Tenggara: Denpasar-Badung-Gianyar, Mataram, Kupang
- Kalimantan: Balikpapan-Samarinda-IKN, Banjarmasin-Banjarbaru, Pontianak
- Sulawesi: Makassar-Gowa-Maros, Manado-Bitung, Palu, Kendari
- Maluku & Papua: Ambon, Ternate, Jayapura, Sorong, Timika, Merauke
"""
import random
import re
import xml.etree.ElementTree as ET

# Canvas & projection parameters matching generate_indonesia_map.py
width = 1200
height = 500
pad_x = 60
pad_y = 65
map_w = width - (pad_x * 2)  # 1080
map_h = height - (pad_y * 2) # 370

lon_min = 95.0
lon_max = 141.0
lat_min = -11.0
lat_max = 6.0

def project(lon, lat):
    x = pad_x + ((lon - lon_min) / 46.0) * 1080
    y = pad_y + ((6.0 - lat) / 17.0) * 370
    return round(x, 2), round(y, 2)

# Major Population Hubs & Clusters (lon, lat, weight/density, radius_spread_deg, cluster_count)
# High density hubs get more clustered points with varying jitter
HUBS = [
    # --- JABODETABEK & BANTEN (Massive density ~35M people) ---
    ("Jakarta Pusat", 106.83, -6.18, 5, 0.08, 14),
    ("Jakarta Selatan", 106.81, -6.26, 4, 0.06, 10),
    ("Jakarta Barat", 106.74, -6.16, 4, 0.06, 10),
    ("Jakarta Timur", 106.89, -6.23, 4, 0.06, 10),
    ("Jakarta Utara/Tanjung Priok", 106.88, -6.12, 4, 0.06, 8),
    ("Tangerang Kota", 106.63, -6.18, 4, 0.06, 8),
    ("Tangerang Selatan/BSD", 106.69, -6.30, 4, 0.06, 8),
    ("Depok", 106.83, -6.40, 4, 0.06, 8),
    ("Bekasi Kota", 106.99, -6.24, 4, 0.07, 10),
    ("Cikarang/Bekasi Industri", 107.15, -6.31, 3, 0.07, 7),
    ("Karawang Kota", 107.31, -6.30, 3, 0.07, 6),
    ("Bogor Kota", 106.80, -6.59, 4, 0.06, 8),
    ("Cibinong", 106.85, -6.48, 3, 0.05, 5),
    ("Serang", 106.16, -6.11, 3, 0.06, 6),
    ("Cilegon/Merak", 106.03, -6.01, 3, 0.06, 6),
    ("Pandeglang", 106.11, -6.31, 2, 0.05, 3),
    ("Rangkasbitung", 106.25, -6.35, 2, 0.05, 3),

    # --- BANDUNG RAYA & PRIANGAN ---
    ("Bandung Kota", 107.61, -6.91, 5, 0.08, 12),
    ("Cimahi", 107.54, -6.88, 3, 0.04, 5),
    ("Padalarang", 107.48, -6.84, 2, 0.04, 4),
    ("Jatinangor/Sumedang Barat", 107.77, -6.93, 2, 0.04, 4),
    ("Soreang/Banjaran", 107.53, -7.03, 3, 0.05, 5),
    ("Purwakarta", 107.44, -6.55, 3, 0.05, 5),
    ("Subang", 107.76, -6.57, 2, 0.05, 4),
    ("Sukabumi", 106.93, -6.92, 3, 0.06, 5),
    ("Cianjur", 107.14, -6.82, 3, 0.05, 5),
    ("Garut", 107.90, -7.21, 3, 0.05, 5),
    ("Tasikmalaya", 108.22, -7.33, 3, 0.06, 6),
    ("Ciamis", 108.35, -7.33, 2, 0.04, 3),
    ("Banjar", 108.53, -7.37, 2, 0.04, 3),

    # --- CIREBON & PANTURA JAWA BARAT - TENGAH ---
    ("Cirebon Kota", 108.56, -6.72, 4, 0.06, 8),
    ("Indramayu", 108.32, -6.33, 2, 0.06, 4),
    ("Kuningan", 108.48, -6.98, 2, 0.04, 3),
    ("Brebes", 109.04, -6.87, 2, 0.05, 4),
    ("Tegal Kota", 109.13, -6.87, 3, 0.06, 6),
    ("Pemalang", 109.38, -6.89, 2, 0.05, 4),
    ("Pekalongan Kota", 109.67, -6.89, 3, 0.06, 6),
    ("Batang", 109.73, -6.91, 2, 0.04, 3),

    # --- SEMARANG & KUDUS PATI ---
    ("Semarang Kota", 110.42, -6.99, 5, 0.08, 12),
    ("Ungaran", 110.40, -7.14, 2, 0.04, 3),
    ("Kendal", 110.20, -6.92, 2, 0.05, 4),
    ("Demak", 110.64, -6.89, 2, 0.05, 4),
    ("Kudus", 110.84, -6.81, 3, 0.05, 6),
    ("Pati", 111.04, -6.75, 2, 0.05, 4),
    ("Jepara", 110.67, -6.59, 2, 0.05, 4),
    ("Rembang", 111.34, -6.71, 2, 0.04, 3),
    ("Salatiga", 110.50, -7.33, 3, 0.04, 4),

    # --- DI YOGYAKARTA & SOLO RAYA ---
    ("Yogyakarta Kota", 110.37, -7.80, 5, 0.07, 10),
    ("Sleman", 110.35, -7.72, 4, 0.05, 6),
    ("Bantul", 110.34, -7.89, 3, 0.05, 5),
    ("Klaten", 110.60, -7.70, 3, 0.05, 5),
    ("Surakarta / Solo", 110.83, -7.57, 5, 0.07, 10),
    ("Sukoharjo", 110.84, -7.68, 3, 0.04, 4),
    ("Karanganyar", 110.95, -7.60, 2, 0.04, 3),
    ("Boyolali", 110.59, -7.53, 2, 0.04, 3),
    ("Sragen", 111.02, -7.43, 2, 0.04, 3),
    ("Magelang Kota", 110.22, -7.48, 3, 0.04, 5),

    # --- BANYUMAS & JATENG SELATAN ---
    ("Purwokerto", 109.24, -7.42, 3, 0.06, 6),
    ("Cilacap", 109.01, -7.72, 3, 0.06, 5),
    ("Purbalingga", 109.36, -7.39, 2, 0.04, 3),
    ("Kebumen", 109.67, -7.67, 2, 0.05, 4),
    ("Purworejo", 110.01, -7.71, 2, 0.04, 3),
    ("Wonosobo", 109.90, -7.36, 2, 0.04, 3),

    # --- GERBANGKERTOSUSILO & SURABAYA METROPOLITAN (~12M people) ---
    ("Surabaya Pusat", 112.75, -7.26, 5, 0.08, 14),
    ("Surabaya Barat", 112.68, -7.27, 4, 0.06, 8),
    ("Surabaya Timur/Rungkut", 112.78, -7.32, 4, 0.06, 8),
    ("Sidoarjo", 112.72, -7.45, 4, 0.06, 9),
    ("Gresik", 112.65, -7.16, 4, 0.06, 8),
    ("Mojokerto", 112.43, -7.47, 3, 0.05, 5),
    ("Lamongan", 112.41, -7.12, 2, 0.05, 4),
    ("Tuban", 112.06, -6.90, 2, 0.05, 4),
    ("Bojonegoro", 111.88, -7.15, 2, 0.05, 4),

    # --- MALANG RAYA & JATIM SELATAN ---
    ("Malang Kota", 112.63, -7.98, 4, 0.07, 9),
    ("Batu", 112.53, -7.87, 3, 0.04, 4),
    ("Kepanjen/Malang Selatan", 112.57, -8.13, 2, 0.04, 3),
    ("Pasuruan Kota", 112.91, -7.64, 3, 0.05, 5),
    ("Probolinggo Kota", 113.22, -7.75, 3, 0.05, 5),
    ("Kediri Kota", 112.01, -7.82, 3, 0.06, 6),
    ("Blitar Kota", 112.17, -8.10, 2, 0.05, 4),
    ("Tulungagung", 111.90, -8.07, 2, 0.05, 4),
    ("Madiun Kota", 111.52, -7.63, 3, 0.05, 5),
    ("Jombang", 112.23, -7.55, 2, 0.05, 4),

    # --- TAPAL KUDA & MADURA ---
    ("Jember", 113.70, -8.17, 3, 0.06, 6),
    ("Lumajang", 113.22, -8.13, 2, 0.04, 3),
    ("Bondowoso", 113.82, -7.91, 2, 0.04, 3),
    ("Situbondo", 114.01, -7.71, 2, 0.04, 3),
    ("Banyuwangi Kota", 114.37, -8.22, 3, 0.06, 6),
    ("Ketapang/Banyuwangi Pelabuhan", 114.39, -8.15, 2, 0.03, 3),
    ("Bangkalan", 112.75, -7.03, 2, 0.05, 4),
    ("Sampang", 113.24, -7.19, 2, 0.04, 3),
    ("Pamekasan", 113.48, -7.16, 2, 0.04, 3),
    ("Sumenep", 113.86, -7.01, 2, 0.04, 3),

    # --- SUMATRA UTARA & ACEH ---
    ("Medan Metropolitan", 98.67, 3.59, 5, 0.08, 14),
    ("Binjai", 98.49, 3.60, 3, 0.04, 4),
    ("Deli Serdang/Lubuk Pakam", 98.88, 3.56, 3, 0.05, 5),
    ("Tebing Tinggi", 99.16, 3.33, 2, 0.04, 3),
    ("Pematang Siantar", 99.07, 2.96, 3, 0.05, 5),
    ("Kisaran", 99.63, 2.98, 2, 0.04, 3),
    ("Rantau Prapat", 99.83, 2.10, 2, 0.04, 3),
    ("Banda Aceh", 95.32, 5.55, 3, 0.06, 6),
    ("Lhokseumawe", 97.14, 5.18, 3, 0.05, 5),
    ("Langsa", 97.97, 4.47, 2, 0.04, 3),
    ("Meulaboh", 96.13, 4.14, 2, 0.04, 3),
    ("Sibolga", 98.78, 1.74, 2, 0.04, 3),
    ("Padang Sidempuan", 99.27, 1.37, 2, 0.04, 3),

    # --- RIAU, KEPRI & SUMATRA BARAT ---
    ("Pekanbaru", 101.45, 0.53, 4, 0.07, 9),
    ("Dumai", 101.45, 1.67, 3, 0.05, 5),
    ("Duri", 101.21, 1.28, 2, 0.04, 3),
    ("Batam Kota", 104.03, 1.13, 4, 0.07, 10),
    ("Tanjung Pinang", 104.45, 0.92, 3, 0.05, 5),
    ("Tanjung Balai Karimun", 103.43, 1.00, 2, 0.04, 3),
    ("Padang Kota", 100.35, -0.95, 4, 0.07, 8),
    ("Bukittinggi", 100.37, -0.31, 3, 0.04, 4),
    ("Payakumbuh", 100.63, -0.23, 2, 0.04, 3),
    ("Solok", 100.66, -0.80, 2, 0.04, 3),

    # --- SUMATRA SELATAN, JAMBI, LAMPUNG, BABEL ---
    ("Palembang Metropolitan", 104.75, -2.99, 4, 0.08, 10),
    ("Prabumulih", 104.23, -3.43, 2, 0.04, 3),
    ("Lubuklinggau", 102.86, -3.30, 2, 0.04, 3),
    ("Baturaja", 104.18, -4.13, 2, 0.04, 3),
    ("Jambi Kota", 103.62, -1.61, 3, 0.06, 6),
    ("Muara Bungo", 102.13, -1.50, 2, 0.04, 3),
    ("Bengkulu Kota", 102.27, -3.80, 3, 0.05, 5),
    ("Bandar Lampung", 105.26, -5.43, 4, 0.07, 9),
    ("Metro Lampung", 105.31, -5.11, 2, 0.04, 4),
    ("Kotabumi", 104.88, -4.83, 2, 0.04, 3),
    ("Bakauheni", 105.75, -5.87, 2, 0.03, 3),
    ("Pangkal Pinang", 106.11, -2.13, 3, 0.05, 4),
    ("Tanjung Pandan (Belitung)", 107.64, -2.74, 2, 0.04, 3),

    # --- BALI & NUSA TENGGARA ---
    ("Denpasar Metropolitan", 115.22, -8.65, 4, 0.07, 10),
    ("Kuta / Seminyak", 115.17, -8.72, 3, 0.04, 5),
    ("Nusa Dua / Jimbaran", 115.19, -8.79, 3, 0.04, 4),
    ("Ubud / Gianyar", 115.26, -8.51, 3, 0.05, 5),
    ("Singaraja", 115.09, -8.11, 2, 0.05, 4),
    ("Mataram / Lombok Barat", 116.12, -8.58, 3, 0.06, 6),
    ("Praya Lombok", 116.27, -8.71, 2, 0.04, 3),
    ("Sumbawa Besar", 117.43, -8.50, 2, 0.04, 3),
    ("Bima Kota", 118.73, -8.46, 2, 0.04, 3),
    ("Labuan Bajo", 119.89, -8.50, 2, 0.03, 3),
    ("Ende Flores", 121.65, -8.84, 2, 0.04, 3),
    ("Maumere", 122.21, -8.62, 2, 0.04, 3),
    ("Kupang Kota", 123.61, -10.17, 3, 0.06, 6),

    # --- KALIMANTAN ---
    ("Balikpapan Kota", 116.83, -1.26, 4, 0.06, 8),
    ("IKN Nusantara Hub", 116.98, -0.97, 4, 0.05, 7),
    ("Samarinda Kota", 117.15, -0.50, 4, 0.06, 8),
    ("Bontang", 117.48, 0.13, 2, 0.04, 4),
    ("Sangatta", 117.58, 0.49, 2, 0.04, 3),
    ("Banjarmasin Metropolitan", 114.59, -3.32, 4, 0.06, 8),
    ("Banjarbaru / Martapura", 114.83, -3.44, 3, 0.05, 5),
    ("Palangka Raya", 113.92, -2.21, 3, 0.05, 5),
    ("Sampit", 112.95, -2.53, 2, 0.04, 3),
    ("Pangkalan Bun", 111.62, -2.68, 2, 0.04, 3),
    ("Pontianak Kota", 109.34, -0.03, 4, 0.06, 8),
    ("Singkawang", 108.98, 0.91, 3, 0.05, 4),
    ("Ketapang Kalbar", 109.97, -1.84, 2, 0.04, 3),
    ("Tarakan Kota", 117.60, 3.32, 3, 0.05, 4),
    ("Tanjung Selor", 117.37, 2.84, 2, 0.03, 3),

    # --- SULAWESI ---
    ("Makassar Metropolitan", 119.42, -5.14, 5, 0.08, 12),
    ("Sungguminasa / Gowa", 119.45, -5.20, 3, 0.04, 4),
    ("Maros", 119.57, -5.00, 2, 0.04, 4),
    ("Parepare", 119.63, -4.01, 3, 0.04, 4),
    ("Palopo", 120.20, -2.99, 2, 0.04, 3),
    ("Manado Metropolitan", 124.84, 1.47, 4, 0.07, 8),
    ("Bitung", 125.19, 1.44, 3, 0.04, 4),
    ("Tomohon", 124.84, 1.33, 2, 0.04, 3),
    ("Gorontalo Kota", 123.06, 0.54, 3, 0.05, 4),
    ("Palu Kota", 119.87, -0.90, 3, 0.06, 5),
    ("Kendari Kota", 122.51, -3.99, 3, 0.06, 5),
    ("Bau-Bau Buton", 122.61, -5.46, 2, 0.04, 3),
    ("Mamuju", 118.89, -2.67, 2, 0.04, 3),

    # --- MALUKU & PAPUA ---
    ("Ambon Kota", 128.18, -3.70, 3, 0.05, 5),
    ("Ternate Kota", 127.38, 0.79, 3, 0.04, 4),
    ("Tidore", 127.40, 0.68, 2, 0.03, 3),
    ("Jayapura Kota", 140.71, -2.53, 3, 0.06, 6),
    ("Abepura / Sentani", 140.54, -2.58, 2, 0.05, 4),
    ("Sorong Kota", 131.25, -0.88, 3, 0.05, 5),
    ("Manokwari", 134.06, -0.86, 2, 0.04, 3),
    ("Timika Kota", 136.89, -4.55, 2, 0.05, 4),
    ("Merauke Kota", 140.34, -8.49, 2, 0.05, 4),
    ("Biak", 136.08, -1.18, 2, 0.04, 3),
]

def generate_lights():
    random.seed(2026)  # Deterministic seed for repeatable build

    # Animation class pools
    anim_classes = ["tw-a", "tw-b", "tw-c", "tw-d", "tw-e", "tw-f", "tw-g", "tw-h"]
    
    # Palette of night city lights (Strict Monochrome: pure whites, zinc highlights, soft greys)
    light_colors = [
        ("#ffffff", 0.95),  # Pure bright LED core
        ("#f4f4f5", 0.90),  # Pure crisp white city light
        ("#e4e4e7", 0.85),  # High intensity light
        ("#d4d4d8", 0.75),  # Mid intensity cluster
        ("#a1a1aa", 0.60),  # Subtle distant city light
        ("#71717a", 0.40),  # Faint outskirts light
    ]

    elements = []
    
    # 1. Macro City Glow Halos for the 6 biggest metropolitan areas (Jakarta, Surabaya, Bandung, Medan, Semarang, Makassar)
    major_glows = [
        ("Jakarta Mega-Halo", 106.84, -6.22, 10.0, 0.22),
        ("Surabaya Mega-Halo", 112.75, -7.28, 7.5, 0.20),
        ("Bandung Mega-Halo", 107.61, -6.91, 6.0, 0.18),
        ("Medan Mega-Halo", 98.67, 3.59, 5.5, 0.18),
        ("Semarang Halo", 110.42, -6.99, 5.0, 0.16),
        ("Solo-Jogja Corridor", 110.60, -7.68, 6.5, 0.16),
        ("Makassar Halo", 119.42, -5.14, 5.0, 0.16),
        ("Denpasar-Badung Halo", 115.20, -8.68, 5.0, 0.16),
        ("Balikpapan-IKN Corridor", 116.90, -1.10, 5.0, 0.15),
    ]

    elements.append('  <!-- Metropolitan Night Glow Bloom (Delicate Radial Halos) -->')
    elements.append('  <g class="city-blooms" style="mix-blend-mode: screen;">')
    for label, g_lon, g_lat, radius, base_op in major_glows:
        gx, gy = project(g_lon, g_lat)
        elements.append(f'    <circle cx="{gx}" cy="{gy}" r="{radius}" fill="url(#cityBloomGrad)" opacity="{base_op}" class="bloom-pulse" />')
    elements.append('  </g>')

    # 2. Discrete Point Night Lights
    elements.append('  <!-- Indonesian Population Density Night Lights (Kelap-Kelip City Constellation) -->')
    elements.append('  <g class="population-night-lights" style="mix-blend-mode: screen;">')

    total_points = 0
    for name, base_lon, base_lat, weight, spread, count in HUBS:
        # Hub core point
        cx, cy = project(base_lon, base_lat)
        core_r = 0.85 if weight >= 4 else (0.65 if weight >= 3 else 0.5)
        core_anim = random.choice(anim_classes)
        elements.append(f'    <!-- {name} Core -->')
        elements.append(f'    <circle cx="{cx}" cy="{cy}" r="{core_r}" fill="#ffffff" opacity="0.95" class="{core_anim}" />')
        total_points += 1

        # Satellite cluster points representing urban sprawl / surrounding population
        for i in range(count - 1):
            # Gaussian-like jitter around the center
            j_lon = base_lon + random.gauss(0, spread * 0.45)
            j_lat = base_lat + random.gauss(0, spread * 0.45)
            px, py = project(j_lon, j_lat)
            
            # Vary radius between 0.4 and 0.85 (ultra tiny)
            r = round(random.uniform(0.40, 0.75), 2)
            color, op = random.choice(light_colors)
            anim = random.choice(anim_classes)

            elements.append(f'    <circle cx="{px}" cy="{py}" r="{r}" fill="{color}" opacity="{op}" class="{anim}" />')
            total_points += 1

    elements.append('  </g>')

    print(f"Generated {total_points} realistic Indonesian population density night light points across {len(HUBS)} hubs.")
    return "\n".join(elements)

def inject_night_lights():
    with open("assets/indonesia-map.svg", "r", encoding="utf-8") as f:
        svg_content = f.read()

    # 1. Check if <defs> exists and inject bloom gradient + animation CSS
    defs_inject = '''    <!-- Realistic City Night Light Radial Bloom Gradient (Strict Monochrome) -->
    <radialGradient id="cityBloomGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.75" />
      <stop offset="40%" stop-color="#f4f4f5" stop-opacity="0.30" />
      <stop offset="80%" stop-color="#e4e4e7" stop-opacity="0.08" />
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0" />
    </radialGradient>
    <style>
      @keyframes cityTwinkleA {
        0%, 100% { opacity: 0.35; transform: scale(0.85); }
        50% { opacity: 1.0; transform: scale(1.2); }
      }
      @keyframes cityTwinkleB {
        0%, 100% { opacity: 0.90; transform: scale(1.15); }
        50% { opacity: 0.25; transform: scale(0.8); }
      }
      @keyframes cityTwinkleC {
        0%, 100% { opacity: 0.4; }
        35% { opacity: 0.95; }
        75% { opacity: 0.3; }
      }
      @keyframes cityTwinkleD {
        0%, 100% { opacity: 0.85; }
        60% { opacity: 0.35; }
      }
      @keyframes cityBloomPulse {
        0%, 100% { opacity: 0.15; transform: scale(0.92); }
        50% { opacity: 0.35; transform: scale(1.08); }
      }
      .tw-a { animation: cityTwinkleA 2.2s ease-in-out infinite; transform-origin: center; transform-box: fill-box; }
      .tw-b { animation: cityTwinkleB 3.1s ease-in-out infinite; transform-origin: center; transform-box: fill-box; }
      .tw-c { animation: cityTwinkleC 1.8s ease-in-out infinite; transform-origin: center; transform-box: fill-box; }
      .tw-d { animation: cityTwinkleD 2.7s ease-in-out infinite; transform-origin: center; transform-box: fill-box; }
      .tw-e { animation: cityTwinkleA 3.5s ease-in-out infinite 0.7s; transform-origin: center; transform-box: fill-box; }
      .tw-f { animation: cityTwinkleB 2.4s ease-in-out infinite 1.1s; transform-origin: center; transform-box: fill-box; }
      .tw-g { animation: cityTwinkleC 2.9s ease-in-out infinite 0.4s; transform-origin: center; transform-box: fill-box; }
      .tw-h { animation: cityTwinkleD 3.3s ease-in-out infinite 1.5s; transform-origin: center; transform-box: fill-box; }
      .bloom-pulse { animation: cityBloomPulse 4.2s ease-in-out infinite; transform-origin: center; transform-box: fill-box; }
    </style>'''

    # If already injected, remove previous injection
    if '<radialGradient id="cityBloomGrad"' in svg_content:
        svg_content = re.sub(r'\s*<!-- Realistic City Night Light Radial Bloom Gradient -->[\s\S]*?</style>', '', svg_content)
    if 'class="population-night-lights"' in svg_content:
        svg_content = re.sub(r'\s*<!-- Metropolitan Night Glow Bloom[\s\S]*?<!-- Strategic Geopolitical Blueprint Reference Markers', '  <!-- Strategic Geopolitical Blueprint Reference Markers', svg_content)
        svg_content = re.sub(r'\s*<!-- Indonesian Archipelago Landmasses -->[\s\S]*?<!-- Strategic Geopolitical Blueprint Reference Markers', lambda m: m.group(0), svg_content)

    # Insert into <defs>
    svg_content = svg_content.replace('</defs>', defs_inject + '\n  </defs>')

    # Generate lights SVG
    lights_svg = generate_lights()

    # Insert right before '<!-- Blueprint Geodetic Markers -->' or '<!-- Strategic Geopolitical Blueprint Reference Markers -->'
    marker_target = '  <!-- Blueprint Geodetic Markers -->'
    if marker_target not in svg_content:
        marker_target = '  <g class="markers">'

    svg_content = svg_content.replace(marker_target, lights_svg + '\n' + marker_target)

    with open("assets/indonesia-map.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)

    # Validate XML
    ET.fromstring(svg_content)
    print("[OK] assets/indonesia-map.svg successfully updated and validated cleanly as valid XML!")

if __name__ == "__main__":
    inject_night_lights()
