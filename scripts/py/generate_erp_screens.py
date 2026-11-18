import os
import xml.etree.ElementTree as ET

def get_browser_header(url):
    return f"""  <!-- Browser Header Bar -->
  <rect width="1600" height="52" fill="#111113" stroke="#27272a" stroke-width="1"/>
  <circle cx="36" cy="26" r="6" fill="#27272a"/>
  <circle cx="56" cy="26" r="6" fill="#27272a"/>
  <circle cx="76" cy="26" r="6" fill="#27272a"/>
  <rect x="520" y="14" width="560" height="24" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
  <text x="800" y="30" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle" letter-spacing="1">{url}</text>"""

def get_maya_sidebar(active_name):
    items = [
        ("Overview", 0),
        ("Inventory &amp; Stock", 46),
        ("Orders &amp; Sales", 92),
        ("Procurement", 138),
        ("Finance &amp; Ledger", 184),
        ("Warehouse Hub", 230),
        ("Settings", 276),
    ]
    menu_svg = ""
    for name, offset in items:
        # Match active state
        raw_name = name.replace("&amp;", "&")
        if raw_name == active_name or name == active_name:
            menu_svg += f"""    <rect x="0" y="{offset}" width="212" height="38" rx="6" fill="#ffffff" fill-opacity="0.08"/>
    <rect x="16" y="{offset+14}" width="10" height="10" fill="#ffffff"/>
    <text x="38" y="{offset+24}" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="500">{name}</text>\n"""
        else:
            menu_svg += f"""    <rect x="16" y="{offset+14}" width="10" height="10" fill="#52525b"/>
    <text x="38" y="{offset+24}" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">{name}</text>\n"""

    return f"""  <!-- Sidebar -->
  <rect x="0" y="52" width="260" height="948" fill="#0d0d10" stroke="#27272a" stroke-width="1"/>
  <!-- Logo / Brand in ERP -->
  <rect x="28" y="80" width="24" height="24" rx="4" fill="#ef4444"/>
  <circle cx="40" cy="92" r="3.5" fill="#fefefe"/>
  <text x="64" y="97" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="700" letter-spacing="1.5">MAYA ERP</text>

  <!-- Nav items -->
  <g transform="translate(24, 140)">
{menu_svg}  </g>

  <!-- User info at bottom sidebar -->
  <rect x="24" y="930" width="212" height="42" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
  <circle cx="48" cy="951" r="10" fill="#ef4444" fill-opacity="0.15"/>
  <circle cx="48" cy="951" r="4" fill="#ef4444"/>
  <text x="70" y="948" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Admin Operations</text>
  <text x="70" y="961" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Branch #04 - Jakarta</text>"""

def get_top_bar(title, subtitle, btn1_label="Export Data", btn2_label="Primary Action"):
    return f"""  <!-- Top bar inside main content -->
  <g transform="translate(290, 80)">
    <text x="0" y="26" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="24" font-weight="600" letter-spacing="-0.5">{title}</text>
    <text x="0" y="48" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">{subtitle}</text>

    <!-- Date selector & export button -->
    <rect x="1070" y="8" width="110" height="34" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
    <text x="1125" y="30" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">{btn1_label}</text>

    <rect x="1195" y="8" width="105" height="34" rx="4" fill="#ffffff"/>
    <text x="1247" y="30" fill="#09090b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="middle">{btn2_label}</text>
  </g>"""

def get_kpi_cards(cards):
    res = '  <!-- KPI Cards -->\n  <g transform="translate(290, 160)">\n'
    x_positions = [0, 324, 648, 972]
    for idx, (label, val, note) in enumerate(cards):
        x = x_positions[idx]
        res += f"""    <!-- Card {idx+1} -->
    <rect x="{x}" y="0" width="298" height="120" rx="8" fill="#121215" stroke="#27272a" stroke-width="1"/>
    <text x="{x+24}" y="34" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="500">{label}</text>
    <text x="{x+24}" y="74" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="700">{val}</text>
    <text x="{x+24}" y="100" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">{note}</text>\n"""
    res += '  </g>\n'
    return res

def build_erp_svg(url, active_nav, title, subtitle, btn1, btn2, kpis, content_svg):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 1000" width="1600" height="1000" fill="none">
  <defs>
    <linearGradient id="chartGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#ef4444" stop-opacity="0.28"/>
      <stop offset="100%" stop-color="#ef4444" stop-opacity="0.0"/>
    </linearGradient>
    <linearGradient id="meterGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0.2"/>
    </linearGradient>
  </defs>

  <!-- Background -->
  <rect width="1600" height="1000" fill="#09090b"/>

{get_browser_header(url)}

{get_maya_sidebar(active_nav)}

{get_top_bar(title, subtitle, btn1, btn2)}

{get_kpi_cards(kpis)}

{content_svg}
</svg>"""

print("ERP Helper module defined.")

def generate_all_erp():
    os.makedirs("assets/projects/erp", exist_ok=True)

    # -------------------------------------------------------------
    # Screen 01: Executive Overview (100% Home Master Parity)
    # -------------------------------------------------------------
    with open("assets/projects/showcases/project-erp.svg", "r", encoding="utf-8") as f:
        svg_01 = f.read()
    with open("assets/projects/erp/01-executive-overview.svg", "w", encoding="utf-8") as f:
        f.write(svg_01)

    # -------------------------------------------------------------
    # Screen 02: Warehouse Inventory Matrix
    # -------------------------------------------------------------
    rows_02 = [
        ("SKU-99201", "Precision Linear Ball Bearing 12mm", "Industrial Hardware", "Jakarta Central", "4,200", "300", "500", "HEALTHY"),
        ("SKU-99202", "Brushless DC Motor 48V 750W", "Electric Drive", "Surabaya Hub", "1,850", "120", "250", "HEALTHY"),
        ("SKU-99203", "Anodized Aluminum Extrusion 4040", "Raw Structural", "Medan Depot", "820", "40", "150", "HEALTHY"),
        ("SKU-99204", "Solid Carbide End Mill 4-Flute", "Tooling Consumable", "Jakarta Central", "290", "85", "300", "LOW STOCK"),
        ("SKU-99205", "Micro-Controller Industrial Gateway", "Electronics", "Makassar Hub", "640", "15", "100", "HEALTHY"),
        ("SKU-99206", "High-Torque Planetary Gearbox 10:1", "Transmission", "Surabaya Hub", "410", "30", "80", "HEALTHY"),
        ("SKU-99207", "Heavy Duty Hydraulic Cylinder 100mm", "Pneumatics", "Jakarta Central", "180", "25", "50", "HEALTHY"),
        ("SKU-99208", "Silicone Thermal Conductive Pad 2mm", "Consumables", "Medan Depot", "3,100", "200", "400", "HEALTHY")
    ]
    table_rows_02 = ""
    y_pos = 110
    for sku, desc, cat, hub, qty, res, min_th, status in rows_02:
        badge_fill = "#ffffff" if status == "HEALTHY" else "#a1a1aa"
        table_rows_02 += f"""    <g transform="translate(32, {y_pos})">
      <line x1="0" y1="0" x2="1206" y2="0" stroke="#1f1f23" stroke-width="1"/>
      <text x="10" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">{sku}</text>
      <text x="130" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">{desc}</text>
      <text x="490" y="28" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">{cat}</text>
      <text x="670" y="28" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">{hub}</text>
      <text x="820" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">{qty}</text>
      <text x="910" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">{res}</text>
      <text x="990" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">{min_th}</text>
      <rect x="1080" y="12" width="100" height="24" rx="4" fill="#ffffff" fill-opacity="0.08"/>
      <text x="1130" y="28" fill="{badge_fill}" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="700" text-anchor="middle">{status}</text>
    </g>\n"""
        y_pos += 48

    content_02 = f"""  <!-- Main Content Grid -->
  <g transform="translate(290, 304)">
    <rect x="0" y="0" width="1270" height="660" rx="8" fill="#121215" stroke="#27272a" stroke-width="1"/>
    
    <!-- Table Header Controls -->
    <text x="32" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="16" font-weight="600">Master Stock &amp; Inventory Ledger</text>
    <text x="32" y="66" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">14,290 verified SKUs across 4 nationwide fulfillment facilities</text>

    <!-- Search input inside table -->
    <rect x="940" y="24" width="298" height="34" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
    <text x="960" y="45" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Search by SKU or description...</text>

    <!-- Column Headers -->
    <g transform="translate(32, 90)">
      <text x="10" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">SKU CODE</text>
      <text x="130" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">ITEM DESCRIPTION</text>
      <text x="490" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">CATEGORY</text>
      <text x="670" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">WAREHOUSE HUB</text>
      <text x="820" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">ON HAND</text>
      <text x="910" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">RESERVED</text>
      <text x="990" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">MIN ALERT</text>
      <text x="1080" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="middle">STATUS</text>
    </g>

{table_rows_02}

    <!-- Pagination Footer -->
    <g transform="translate(32, 590)">
      <line x1="0" y1="0" x2="1206" y2="0" stroke="#1f1f23" stroke-width="1"/>
      <text x="10" y="34" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Showing 1 - 8 of 14,290 verified stock SKUs</text>
      <rect x="1050" y="16" width="70" height="28" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
      <text x="1085" y="34" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">Previous</text>
      <rect x="1136" y="16" width="70" height="28" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
      <text x="1171" y="34" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">Next</text>
    </g>
  </g>"""

    svg_02 = build_erp_svg(
        url="https://erp.mayastranawaloka.com/inventory",
        active_nav="Inventory & Stock",
        title="Warehouse Inventory Matrix",
        subtitle="SKU Stock Levels, Multi-Location Distribution &amp; Reorder Automation",
        btn1="Batch Import",
        btn2="Add SKU",
        kpis=[
            ("TOTAL WAREHOUSED UNITS", "14,290 SKUs", "Distributed across 4 hubs"),
            ("LOW STOCK ALERTS", "14 Items", "Triggered automated reorder"),
            ("INVENTORY VALUATION", "Rp 18.62 B", "Calculated on FIFO basis"),
            ("TURNOVER RATIO", "8.4x / Year", "Above sector median")
        ],
        content_svg=content_02
    )
    with open("assets/projects/erp/02-warehouse-inventory.svg", "w", encoding="utf-8") as f:
        f.write(svg_02)

    # -------------------------------------------------------------
    # Screen 03: Procurement Pipeline
    # -------------------------------------------------------------
    content_03 = """  <!-- Main Content Grid -->
  <g transform="translate(290, 304)">
    <!-- Top 4 Stage Process Banner -->
    <rect x="0" y="0" width="1270" height="110" rx="8" fill="#121215" stroke="#27272a" stroke-width="1"/>
    <g transform="translate(32, 24)">
      <!-- Stage 1 -->
      <rect x="0" y="0" width="280" height="62" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
      <text x="20" y="26" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="700">STAGE 01 // DRAFT RFQ</text>
      <text x="20" y="48" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">12 Pending RFQs</text>

      <!-- Stage 2 -->
      <rect x="306" y="0" width="280" height="62" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
      <text x="326" y="26" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="700">STAGE 02 // MANAGEMENT REVIEW</text>
      <text x="326" y="48" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">5 Awaiting Approval</text>

      <!-- Stage 3 (Active) -->
      <rect x="612" y="0" width="280" height="62" rx="6" fill="#ef4444" fill-opacity="0.12" stroke="#ef4444" stroke-opacity="0.8" stroke-width="1.5"/>
      <text x="632" y="26" fill="#ef4444" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="700">STAGE 03 // DISPATCHED TO VENDOR</text>
      <text x="632" y="48" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">38 In Transit Orders</text>

      <!-- Stage 4 -->
      <rect x="918" y="0" width="288" height="62" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
      <text x="938" y="26" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="700">STAGE 04 // 3-WAY RECONCILED</text>
      <text x="938" y="48" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">142 Closed This Month</text>
    </g>

    <!-- Bottom Purchase Order Table -->
    <g transform="translate(0, 134)">
      <rect x="0" y="0" width="1270" height="526" rx="8" fill="#121215" stroke="#27272a" stroke-width="1"/>
      <text x="32" y="40" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="16" font-weight="600">Active Vendor Purchase Order Matrix</text>
      <text x="32" y="62" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Automated 3-way matching between PO, receiving slip, and tax invoice</text>

      <!-- Table Header -->
      <g transform="translate(32, 95)">
        <text x="10" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">PO NUMBER</text>
        <text x="140" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">PRIMARY SUPPLIER</text>
        <text x="440" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">COMMITTED VALUE</text>
        <text x="640" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">ISSUE DATE</text>
        <text x="780" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">EST. ARRIVAL</text>
        <text x="930" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">3-WAY MATCH</text>
        <text x="1100" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">ACTION</text>
      </g>

      <!-- Rows -->
      <g transform="translate(32, 115)">
        <line x1="0" y1="0" x2="1206" y2="0" stroke="#1f1f23"/>
        <text x="10" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">PO-2026-0891</text>
        <text x="140" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">PT Mitra Steel Industri</text>
        <text x="440" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Rp 480.000.000</text>
        <text x="640" y="28" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">10 Nov 2026</text>
        <text x="780" y="28" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">18 Nov 2026</text>
        <rect x="930" y="12" width="110" height="24" rx="4" fill="#ffffff" fill-opacity="0.08"/>
        <text x="985" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="700" text-anchor="middle">VERIFIED 100%</text>
        <text x="1100" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Release</text>

        <line x1="0" y1="48" x2="1206" y2="48" stroke="#1f1f23"/>
        <text x="10" y="76" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">PO-2026-0892</text>
        <text x="140" y="76" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Nusantara Electric Components</text>
        <text x="440" y="76" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Rp 215.400.000</text>
        <text x="640" y="76" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">11 Nov 2026</text>
        <text x="780" y="76" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">15 Nov 2026</text>
        <rect x="930" y="60" width="110" height="24" rx="4" fill="#ffffff" fill-opacity="0.08"/>
        <text x="985" y="76" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="700" text-anchor="middle">VERIFIED 100%</text>
        <text x="1100" y="76" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Release</text>

        <line x1="0" y1="96" x2="1206" y2="96" stroke="#1f1f23"/>
        <text x="10" y="124" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">PO-2026-0893</text>
        <text x="140" y="124" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Global Precision Tools Ltd</text>
        <text x="440" y="124" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Rp 92.500.000</text>
        <text x="640" y="124" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">12 Nov 2026</text>
        <text x="780" y="124" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">20 Nov 2026</text>
        <rect x="930" y="108" width="110" height="24" rx="4" fill="#ffffff" fill-opacity="0.08"/>
        <text x="985" y="124" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="700" text-anchor="middle">AWAITING SLIP</text>
        <text x="1100" y="124" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Hold</text>
      </g>
    </g>
  </g>"""

    svg_03 = build_erp_svg(
        url="https://erp.mayastranawaloka.com/procurement",
        active_nav="Procurement",
        title="Procurement &amp; Vendor Pipeline",
        subtitle="Automated Purchase Orders, 3-Way Invoice Matching &amp; Supplier Analytics",
        btn1="Vendor List",
        btn2="Generate PO",
        kpis=[
            ("ACTIVE PURCHASE ORDERS", "38 Orders", "Total committed contracts"),
            ("PENDING APPROVALS", "5 POs", "Executive review queue"),
            ("COMMITTED SPEND", "Rp 3.42 B", "November procurement budget"),
            ("ON-TIME VENDOR RATE", "97.8 %", "Weighted supplier SLA score")
        ],
        content_svg=content_03
    )
    with open("assets/projects/erp/03-procurement-pipeline.svg", "w", encoding="utf-8") as f:
        f.write(svg_03)

    # -------------------------------------------------------------
    # Screen 04: Financial Ledger
    # -------------------------------------------------------------
    rows_04 = [
        ("TX-88019", "14 Nov 2026", "1101-01", "Cash at Bank (BCA Corporate)", "Rp 850.000.000", "-", "0x9f82...c102", "BALANCED"),
        ("TX-88019", "14 Nov 2026", "4101-02", "Commercial Revenue Account", "-", "Rp 850.000.000", "0x9f82...c103", "BALANCED"),
        ("TX-88020", "14 Nov 2026", "1301-04", "Warehouse Inventory Asset", "Rp 320.000.000", "-", "0x7a11...4401", "BALANCED"),
        ("TX-88020", "14 Nov 2026", "2101-01", "Accounts Payable (Trade)", "-", "Rp 320.000.000", "0x7a11...4402", "BALANCED"),
        ("TX-88021", "13 Nov 2026", "5102-01", "Freight &amp; Logistics Expense", "Rp 42.500.000", "-", "0x3b90...2190", "BALANCED"),
        ("TX-88021", "13 Nov 2026", "1101-02", "Cash at Bank (Mandiri Ops)", "-", "Rp 42.500.000", "0x3b90...2191", "BALANCED"),
        ("TX-88022", "13 Nov 2026", "1201-03", "Accounts Receivable Commercial", "Rp 640.000.000", "-", "0x12bb...8801", "BALANCED"),
        ("TX-88022", "13 Nov 2026", "4101-01", "Enterprise License Sales", "-", "Rp 640.000.000", "0x12bb...8802", "BALANCED")
    ]
    table_rows_04 = ""
    y_pos = 110
    for tx, dt, ac_code, ac_name, debit, credit, hash_val, st in rows_04:
        table_rows_04 += f"""    <g transform="translate(32, {y_pos})">
      <line x1="0" y1="0" x2="1206" y2="0" stroke="#1f1f23" stroke-width="1"/>
      <text x="10" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">{tx}</text>
      <text x="130" y="28" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">{dt}</text>
      <text x="250" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">{ac_code}</text>
      <text x="360" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">{ac_name}</text>
      <text x="680" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">{debit}</text>
      <text x="830" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">{credit}</text>
      <text x="980" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">{hash_val}</text>
      <rect x="1100" y="12" width="90" height="24" rx="4" fill="#ffffff" fill-opacity="0.08"/>
      <text x="1145" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="700" text-anchor="middle">{st}</text>
    </g>\n"""
        y_pos += 48

    content_04 = f"""  <!-- Main Content Grid -->
  <g transform="translate(290, 304)">
    <rect x="0" y="0" width="1270" height="660" rx="8" fill="#121215" stroke="#27272a" stroke-width="1"/>
    <text x="32" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="16" font-weight="600">Double-Entry Immutable General Ledger</text>
    <text x="32" y="66" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Cryptographically chained balance records with row-level transactional locking</text>

    <!-- Column Headers -->
    <g transform="translate(32, 90)">
      <text x="10" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">TX ID</text>
      <text x="130" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">DATE</text>
      <text x="250" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">GL CODE</text>
      <text x="360" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">ACCOUNT NAME</text>
      <text x="680" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">DEBIT (IDR)</text>
      <text x="830" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">CREDIT (IDR)</text>
      <text x="980" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">HASH CHECKSUM</text>
      <text x="1100" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="middle">STATUS</text>
    </g>

{table_rows_04}

    <!-- Total Reconciliation Banner -->
    <g transform="translate(32, 580)">
      <rect x="0" y="0" width="1206" height="50" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
      <text x="20" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">TOTAL RECONCILED LEDGER BALANCE</text>
      <text x="680" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">Rp 1.852.500.000</text>
      <text x="830" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">Rp 1.852.500.000</text>
      <text x="1170" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" text-anchor="end">PERFECT PARITY (0.00)</text>
    </g>
  </g>"""

    svg_04 = build_erp_svg(
        url="https://erp.mayastranawaloka.com/finance",
        active_nav="Finance &amp; Ledger",
        title="Double-Entry Financial Ledger",
        subtitle="Automated Journal Entries, Multi-Currency Reconciliations &amp; Balance Sheets",
        btn1="Audit Report",
        btn2="Manual Journal",
        kpis=[
            ("NET CASH POSITION", "Rp 4.28 B", "Liquid bank balances"),
            ("ACCOUNTS RECEIVABLE", "Rp 1.62 B", "Average aging 14.2 days"),
            ("ACCOUNTS PAYABLE", "Rp 940.0 M", "Upcoming vendor commitments"),
            ("UNRECONCILED TRANSACTIONS", "0 Items", "Zero discrepancies flagged")
        ],
        content_svg=content_04
    )
    with open("assets/projects/erp/04-financial-ledger.svg", "w", encoding="utf-8") as f:
        f.write(svg_04)

    # -------------------------------------------------------------
    # Screen 05: Sales Dispatch & Logistics Hub
    # -------------------------------------------------------------
    content_05 = """  <!-- Main Content Grid -->
  <g transform="translate(290, 304)">
    <rect x="0" y="0" width="830" height="660" rx="8" fill="#121215" stroke="#27272a" stroke-width="1"/>
    <text x="32" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="16" font-weight="600">Active Outbound Dispatch Queue</text>
    <text x="32" y="66" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Automated courier manifest sorting and shipment delivery SLA counters</text>

    <!-- Column Headers -->
    <g transform="translate(32, 95)">
      <text x="0" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">WAYBILL #</text>
      <text x="140" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">CLIENT / CONSIGNEE</text>
      <text x="380" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">DESTINATION</text>
      <text x="520" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">CARRIER</text>
      <text x="660" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">MANIFEST STATUS</text>
    </g>

    <g transform="translate(32, 115)">
      <line x1="0" y1="0" x2="766" y2="0" stroke="#1f1f23"/>
      <text x="0" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">WB-JKT-9901</text>
      <text x="140" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Karya Bangun Sentosa</text>
      <text x="380" y="28" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Bandung</text>
      <text x="520" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">JNE Trucking</text>
      <rect x="660" y="12" width="100" height="24" rx="4" fill="#ffffff" fill-opacity="0.08"/>
      <text x="710" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="700" text-anchor="middle">DISPATCHED</text>

      <line x1="0" y1="48" x2="766" y2="48" stroke="#1f1f23"/>
      <text x="0" y="76" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">WB-JKT-9902</text>
      <text x="140" y="76" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Sinarmas Indah Logistik</text>
      <text x="380" y="76" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Semarang</text>
      <text x="520" y="76" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">SiCepat Cargo</text>
      <rect x="660" y="60" width="100" height="24" rx="4" fill="#ffffff" fill-opacity="0.08"/>
      <text x="710" y="76" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="700" text-anchor="middle">IN TRANSIT</text>

      <line x1="0" y1="96" x2="766" y2="96" stroke="#1f1f23"/>
      <text x="0" y="124" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">WB-JKT-9903</text>
      <text x="140" y="124" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Bima Sakti Kontraktor</text>
      <text x="380" y="124" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Surabaya</text>
      <text x="520" y="124" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Fleet Internal #02</text>
      <rect x="660" y="108" width="100" height="24" rx="4" fill="#ffffff" fill-opacity="0.08"/>
      <text x="710" y="124" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="700" text-anchor="middle">DELIVERED</text>

      <line x1="0" y1="144" x2="766" y2="144" stroke="#1f1f23"/>
      <text x="0" y="172" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">WB-JKT-9904</text>
      <text x="140" y="172" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Pacific Indo Pratama</text>
      <text x="380" y="172" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Denpasar</text>
      <text x="520" y="172" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Baraka Express</text>
      <rect x="660" y="156" width="100" height="24" rx="4" fill="#ffffff" fill-opacity="0.08"/>
      <text x="710" y="172" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="700" text-anchor="middle">DISPATCHED</text>
    </g>

    <!-- Right Side: Fleet Performance -->
    <g transform="translate(850, 0)">
      <rect x="0" y="0" width="420" height="660" rx="8" fill="#121215" stroke="#27272a" stroke-width="1"/>
      <text x="32" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="16" font-weight="600">Carrier Breakdown &amp; SLA</text>
      <text x="32" y="66" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Fulfillment rate by logistics provider</text>

      <g transform="translate(32, 105)">
        <text x="0" y="16" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Internal Fleet Transport</text>
        <text x="350" y="16" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="end">99.4% On-Time</text>
        <rect x="0" y="28" width="350" height="8" rx="4" fill="#1f1f23"/>
        <rect x="0" y="28" width="345" height="8" rx="4" fill="#ffffff"/>

        <text x="0" y="80" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">JNE Freight Logistics</text>
        <text x="350" y="80" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="end">97.8% On-Time</text>
        <rect x="0" y="92" width="350" height="8" rx="4" fill="#1f1f23"/>
        <rect x="0" y="92" width="320" height="8" rx="4" fill="#ffffff"/>

        <text x="0" y="144" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">SiCepat Cargo</text>
        <text x="350" y="144" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="end">98.2% On-Time</text>
        <rect x="0" y="156" width="350" height="8" rx="4" fill="#1f1f23"/>
        <rect x="0" y="156" width="330" height="8" rx="4" fill="#ffffff"/>
      </g>
    </g>
  </g>"""

    svg_05 = build_erp_svg(
        url="https://erp.mayastranawaloka.com/orders/dispatch",
        active_nav="Orders &amp; Sales",
        title="Sales Dispatch &amp; Logistics Hub",
        subtitle="Outbound Order Queue, Courier Dispatch Manifests &amp; SLA Tracking",
        btn1="Daily Manifest",
        btn2="Dispatch Batch",
        kpis=[
            ("READY FOR DISPATCH", "42 Orders", "Staged at outbound bays"),
            ("DISPATCHED TODAY", "286 Consignments", "Jakarta central hub"),
            ("ON-TIME ARRIVAL RATE", "98.9 %", "Within guaranteed window"),
            ("AVERAGE TRANSIT", "18.4 Hours", "Direct line-haul delivery")
        ],
        content_svg=content_05
    )
    with open("assets/projects/erp/05-sales-dispatch.svg", "w", encoding="utf-8") as f:
        f.write(svg_05)

    # -------------------------------------------------------------
    # Screen 06: Supply Chain Flow
    # -------------------------------------------------------------
    content_06 = """  <!-- Main Content Grid -->
  <g transform="translate(290, 304)">
    <rect x="0" y="0" width="1270" height="660" rx="8" fill="#121215" stroke="#27272a" stroke-width="1"/>
    <text x="32" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="16" font-weight="600">Inter-Hub Supply Chain Network Flow</text>
    <text x="32" y="66" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Topology map of transit lines, transfer latency, and real-time inventory velocity</text>

    <!-- Network diagram -->
    <g transform="translate(50, 110)">
      <!-- Central Hub -->
      <rect x="450" y="80" width="220" height="100" rx="8" fill="#18181b" stroke="#ef4444" stroke-width="1.5"/>
      <circle cx="650" cy="100" r="4" fill="#ef4444"/>
      <text x="560" y="125" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="700" text-anchor="middle">JAKARTA CENTRAL HUB</text>
      <text x="560" y="150" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">12,400 Pallets &#8226; Master Router</text>

      <!-- West Node -->
      <rect x="60" y="240" width="200" height="90" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
      <text x="160" y="280" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600" text-anchor="middle">MEDAN DEPOT</text>
      <text x="160" y="302" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">Transit: 36h &#8226; 3,400 Units</text>

      <!-- East Node 1 -->
      <rect x="460" y="320" width="200" height="90" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
      <text x="560" y="360" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600" text-anchor="middle">SURABAYA HUB</text>
      <text x="560" y="382" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">Transit: 14h &#8226; 6,800 Units</text>

      <!-- East Node 2 -->
      <rect x="860" y="240" width="200" height="90" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
      <text x="960" y="280" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600" text-anchor="middle">MAKASSAR HUB</text>
      <text x="960" y="302" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">Transit: 48h &#8226; 4,200 Units</text>

      <!-- Connecting Lines -->
      <line x1="450" y1="140" x2="260" y2="280" stroke="#ef4444" stroke-width="2" stroke-dasharray="6,4"/>
      <line x1="560" y1="180" x2="560" y2="320" stroke="#ef4444" stroke-width="2"/>
      <line x1="670" y1="140" x2="860" y2="280" stroke="#ef4444" stroke-width="2" stroke-dasharray="6,4"/>
    </g>

    <!-- Bottom summary table -->
    <g transform="translate(32, 480)">
      <rect x="0" y="0" width="1206" height="150" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
      <text x="24" y="34" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Active Pipeline Bottlenecks: 0 Critical Alerts</text>
      <text x="24" y="58" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">All freight corridors running within optimal lead time tolerances</text>
      <text x="24" y="100" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Jakarta - Surabaya: 14 Line-Haul Trucks in Motion &#8226; Status: Clear</text>
      <text x="24" y="125" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Jakarta - Medan: Maritime Ferry Transit Node #03 &#8226; Status: Dispatched</text>
    </g>
  </g>"""

    svg_06 = build_erp_svg(
        url="https://erp.mayastranawaloka.com/warehouses/flow",
        active_nav="Warehouse Hub",
        title="Supply Chain Flow &amp; Bottlenecks",
        subtitle="Inter-Hub Transfer Logistics, Route Efficiency &amp; Lead Time Optimization",
        btn1="Route Map",
        btn2="Schedule Transfer",
        kpis=[
            ("ACTIVE TRANSIT NODES", "4 Facilities", "100% interconnected"),
            ("CONSIGNMENTS IN MOTION", "18 Shipments", "En route inter-hub"),
            ("BOTTLENECK INDEX", "0.02 / Low", "Minimal port congestion"),
            ("FLEET READINESS", "96.4 %", "24 vehicle inspections passed")
        ],
        content_svg=content_06
    )
    with open("assets/projects/erp/06-supply-chain-flow.svg", "w", encoding="utf-8") as f:
        f.write(svg_06)

    # -------------------------------------------------------------
    # Screen 07: Employee Directory & RBAC Control
    # -------------------------------------------------------------
    users_07 = [
        ("Budi Hartono, S.T.", "budi.hartono@mayastranawaloka.com", "Operations", "Chief Operations Officer", "Full Cluster Admin", "ENFORCED"),
        ("Siti Rahmawati, S.E.", "siti.rahma@mayastranawaloka.com", "Finance", "Senior Financial Controller", "General Ledger Audit", "ENFORCED"),
        ("Ahmad Fauzi", "ahmad.fauzi@mayastranawaloka.com", "Logistics", "Jakarta Warehouse Manager", "Inventory &amp; Outbound", "ENFORCED"),
        ("Dewi Kusuma", "dewi.k@mayastranawaloka.com", "Procurement", "Procurement Lead Specialist", "PO Creation &amp; Approval", "ENFORCED"),
        ("Reza Pratama", "reza.p@mayastranawaloka.com", "Logistics", "Fleet Dispatch Coordinator", "Dispatch Queue Only", "ENFORCED"),
        ("Linda Wijaya", "linda.w@mayastranawaloka.com", "Accounting", "Junior Tax &amp; Bookkeeper", "Read-Only Ledger", "ENFORCED"),
        ("Eko Saputra", "eko.s@mayastranawaloka.com", "Operations", "Safety &amp; Facility Auditor", "Maintenance Log Read", "ENFORCED")
    ]
    table_rows_07 = ""
    y_pos = 110
    for name, email, dept, role, scope, mfa in users_07:
        table_rows_07 += f"""    <g transform="translate(32, {y_pos})">
      <line x1="0" y1="0" x2="1206" y2="0" stroke="#1f1f23" stroke-width="1"/>
      <circle cx="20" cy="24" r="14" fill="#18181b" stroke="#27272a"/>
      <text x="20" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" text-anchor="middle">{name[0]}</text>
      <text x="50" y="22" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">{name}</text>
      <text x="50" y="36" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">{email}</text>
      <text x="380" y="28" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">{dept}</text>
      <text x="520" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">{role}</text>
      <text x="800" y="28" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">{scope}</text>
      <rect x="1080" y="12" width="100" height="24" rx="4" fill="#ffffff" fill-opacity="0.08"/>
      <text x="1130" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="700" text-anchor="middle">2FA ACTIVE</text>
    </g>\n"""
        y_pos += 52

    content_07 = f"""  <!-- Main Content Grid -->
  <g transform="translate(290, 304)">
    <rect x="0" y="0" width="1270" height="660" rx="8" fill="#121215" stroke="#27272a" stroke-width="1"/>
    <text x="32" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="16" font-weight="600">Enterprise Role-Based Access Control (RBAC)</text>
    <text x="32" y="66" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Cryptographic user sessions, permission policies, and hardware token enforcement</text>

    <!-- Column Headers -->
    <g transform="translate(32, 90)">
      <text x="50" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">EMPLOYEE NAME &amp; EMAIL</text>
      <text x="380" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">DEPARTMENT</text>
      <text x="520" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">ASSIGNED SECURITY ROLE</text>
      <text x="800" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">PERMISSION SCOPE</text>
      <text x="1130" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="middle">MFA STATUS</text>
    </g>

{table_rows_07}

    <!-- Bottom summary banner -->
    <g transform="translate(32, 580)">
      <rect x="0" y="0" width="1206" height="50" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
      <text x="20" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">MFA ENFORCEMENT: 100%</text>
      <text x="300" y="32" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Hardware WebAuthn / FIDO2 security keys mandatory for all privileged roles</text>
    </g>
  </g>"""

    svg_07 = build_erp_svg(
        url="https://erp.mayastranawaloka.com/settings/rbac",
        active_nav="Settings",
        title="Employee Directory &amp; RBAC Control",
        subtitle="Granular Security Roles, Department Policies &amp; Multi-Factor Access",
        btn1="Audit Roles",
        btn2="Add Employee",
        kpis=[
            ("ACTIVE OPERATORS", "84 Users", "Across all regional branches"),
            ("DEFINED ROLES", "12 Roles", "Strict least-privilege matrix"),
            ("PRIVILEGED ADMINS", "3 Accounts", "Root infrastructure operators"),
            ("MFA COMPLIANCE", "100 %", "Hardware security key enforced")
        ],
        content_svg=content_07
    )
    with open("assets/projects/erp/07-employee-rbac.svg", "w", encoding="utf-8") as f:
        f.write(svg_07)

    # -------------------------------------------------------------
    # Screen 08: Fixed Asset & Maintenance Schedule
    # -------------------------------------------------------------
    content_08 = """  <!-- Main Content Grid -->
  <g transform="translate(290, 304)">
    <rect x="0" y="0" width="1270" height="660" rx="8" fill="#121215" stroke="#27272a" stroke-width="1"/>
    <text x="32" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="16" font-weight="600">Fixed Assets &amp; Preventive Maintenance Diagnostics</text>
    <text x="32" y="66" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Machine health telemetry, operational run-hours, and scheduled maintenance service orders</text>

    <!-- Column Headers -->
    <g transform="translate(32, 90)">
      <text x="10" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">ASSET TAG</text>
      <text x="140" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">EQUIPMENT TYPE</text>
      <text x="400" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">FACILITY</text>
      <text x="560" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">RUN-HOURS</text>
      <text x="700" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">NEXT SERVICE</text>
      <text x="860" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">HEALTH SCORE</text>
      <text x="1080" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="middle">STATUS</text>
    </g>

    <g transform="translate(32, 115)">
      <line x1="0" y1="0" x2="1206" y2="0" stroke="#1f1f23"/>
      <text x="10" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">AST-FLT-01</text>
      <text x="140" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Toyota Electric Forklift 3.0T</text>
      <text x="400" y="28" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Jakarta Central Hub</text>
      <text x="560" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">2,410 hrs</text>
      <text x="700" y="28" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">28 Nov 2026</text>
      <text x="860" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">98 / 100</text>
      <rect x="1030" y="12" width="100" height="24" rx="4" fill="#ffffff" fill-opacity="0.08"/>
      <text x="1080" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="700" text-anchor="middle">OPTIMAL</text>

      <line x1="0" y1="48" x2="1206" y2="48" stroke="#1f1f23"/>
      <text x="10" y="76" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">AST-FLT-02</text>
      <text x="140" y="76" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Crown Reach Truck RR5700</text>
      <text x="400" y="76" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Surabaya Hub</text>
      <text x="560" y="76" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">1,980 hrs</text>
      <text x="700" y="76" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">04 Dec 2026</text>
      <text x="860" y="76" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">96 / 100</text>
      <rect x="1030" y="60" width="100" height="24" rx="4" fill="#ffffff" fill-opacity="0.08"/>
      <text x="1080" y="76" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="700" text-anchor="middle">OPTIMAL</text>

      <line x1="0" y1="96" x2="1206" y2="96" stroke="#1f1f23"/>
      <text x="10" y="124" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">AST-CONV-01</text>
      <text x="140" y="124" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Automated Sorting Conveyor 80m</text>
      <text x="400" y="124" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Jakarta Central Hub</text>
      <text x="560" y="124" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">8,720 hrs</text>
      <text x="700" y="124" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">20 Nov 2026</text>
      <text x="860" y="124" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">91 / 100</text>
      <rect x="1030" y="108" width="100" height="24" rx="4" fill="#ffffff" fill-opacity="0.08"/>
      <text x="1080" y="124" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="700" text-anchor="middle">OPTIMAL</text>
    </g>
  </g>"""

    svg_08 = build_erp_svg(
        url="https://erp.mayastranawaloka.com/warehouses/assets",
        active_nav="Warehouse Hub",
        title="Fixed Asset &amp; Maintenance Schedule",
        subtitle="Heavy Machinery Diagnostics, Service Cycles &amp; Depreciation Calculations",
        btn1="Asset Audit",
        btn2="Schedule Service",
        kpis=[
            ("TRACKED EQUIPMENT", "148 Assets", "Registered in asset registry"),
            ("SCHEDULED SERVICES", "4 Machines", "Preventative maintenance plan"),
            ("FLEET READINESS", "99.2 %", "Zero unscheduled downtime"),
            ("ASSET VALUATION", "Rp 6.84 B", "Straight-line depreciation")
        ],
        content_svg=content_08
    )
    with open("assets/projects/erp/08-asset-maintenance.svg", "w", encoding="utf-8") as f:
        f.write(svg_08)

    # -------------------------------------------------------------
    # Screen 09: Immutable Audit Trail
    # -------------------------------------------------------------
    logs_09 = [
        ("EV-009182", "14 Nov 2026 07:18:22.091", "Ahmad Fauzi (Ops)", "UPDATE", "inventory_balances", "sku_qty: 4200 -> 4180", "0xfa91...38a1"),
        ("EV-009181", "14 Nov 2026 07:14:08.412", "Siti Rahma (Finance)", "RECONCILE", "general_ledger_entries", "tx_balance: 0 diff verified", "0x882b...10c2"),
        ("EV-009180", "14 Nov 2026 06:58:49.190", "System Daemon", "AUTOMATED_SYNC", "redis_cart_reservations", "expired_ttl_purged: 14", "0x11ee...90a0"),
        ("EV-009179", "14 Nov 2026 06:40:12.871", "Dewi Kusuma (Procure)", "INSERT", "purchase_orders", "po_id: PO-2026-0894 approved", "0x33b1...7712"),
        ("EV-009178", "14 Nov 2026 05:30:00.002", "Cron Worker", "SNAPSHOT", "cluster_wal_backups", "s3_archive_sealed: 4.8 GB", "0xaa90...4421"),
        ("EV-009177", "14 Nov 2026 04:12:38.109", "Budi Hartono (Admin)", "CONFIG_CHANGE", "security_policies", "mfa_grace_period: 0s enforced", "0x00fa...5591")
    ]
    table_rows_09 = ""
    y_pos = 110
    for ev_id, ts, actor, action, tbl, diff, chk in logs_09:
        table_rows_09 += f"""    <g transform="translate(32, {y_pos})">
      <line x1="0" y1="0" x2="1206" y2="0" stroke="#1f1f23" stroke-width="1"/>
      <text x="10" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">{ev_id}</text>
      <text x="140" y="28" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">{ts}</text>
      <text x="360" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">{actor}</text>
      <text x="560" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700">{action}</text>
      <text x="700" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">{tbl}</text>
      <text x="890" y="28" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">{diff}</text>
      <text x="1100" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">{chk}</text>
    </g>\n"""
        y_pos += 48

    content_09 = f"""  <!-- Main Content Grid -->
  <g transform="translate(290, 304)">
    <rect x="0" y="0" width="1270" height="660" rx="8" fill="#121215" stroke="#27272a" stroke-width="1"/>
    <text x="32" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="16" font-weight="600">Cryptographically Chained Audit Stream</text>
    <text x="32" y="66" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Nano-precision timestamps, immutable Merkle proofs, and actor identity tracking</text>

    <!-- Column Headers -->
    <g transform="translate(32, 90)">
      <text x="10" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">EVENT ID</text>
      <text x="140" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">TIMESTAMP (UTC+7)</text>
      <text x="360" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">ACTOR IDENTITY</text>
      <text x="560" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">ACTION</text>
      <text x="700" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">TARGET TABLE</text>
      <text x="890" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">DIFF PAYLOAD</text>
      <text x="1100" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">HASH PROOF</text>
    </g>

{table_rows_09}
  </g>"""

    svg_09 = build_erp_svg(
        url="https://erp.mayastranawaloka.com/settings/audit-logs",
        active_nav="Settings",
        title="Immutable Audit Trail",
        subtitle="Cryptographic Mutation Logs, Operator Session Tracing &amp; State Diffing",
        btn1="Filter Logs",
        btn2="Export Merkle Proof",
        kpis=[
            ("TOTAL LOGGED MUTATIONS", "1,842,910 Events", "100% hash chain integrity"),
            ("VERIFIED CHECKSUMS", "Zero Tampering", "Merkle tree verified"),
            ("SECURITY INCIDENTS", "0 Flagged", "Automated anomaly shield"),
            ("LOG RETENTION", "7 Years", "Compliant with corporate law")
        ],
        content_svg=content_09
    )
    with open("assets/projects/erp/09-audit-logs.svg", "w", encoding="utf-8") as f:
        f.write(svg_09)

    # -------------------------------------------------------------
    # Screen 10: System Settings
    # -------------------------------------------------------------
    content_10 = """  <!-- Main Content Grid -->
  <g transform="translate(290, 304)">
    <rect x="0" y="0" width="1270" height="660" rx="8" fill="#121215" stroke="#27272a" stroke-width="1"/>
    <text x="32" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="16" font-weight="600">Cluster Parameters &amp; Database Configurations</text>
    <text x="32" y="66" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">PostgreSQL high-availability cluster topology, webhook consumers, and cryptographic keys</text>

    <!-- Cluster parameter cards -->
    <g transform="translate(32, 100)">
      <rect x="0" y="0" width="580" height="150" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
      <text x="24" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Primary Database Engine</text>
      <text x="24" y="56" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">PostgreSQL 16.4 Enterprise on High-Speed NVMe</text>
      <text x="24" y="90" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Active Connections: 48 / 500 &#8226; Max Pool Size: 1,000</text>
      <text x="24" y="115" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Write-Ahead Log (WAL) Streaming: 0.08ms Latency</text>

      <rect x="620" y="0" width="586" height="150" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
      <text x="644" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Automated Backup &amp; Disaster Recovery</text>
      <text x="644" y="56" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Encrypted S3 Multi-Region Geographic Replication</text>
      <text x="644" y="90" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Hourly Differential Snapshot &#8226; Daily Full Image</text>
      <text x="644" y="115" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">RTO Target: &lt; 5 Minutes &#8226; RPO Target: &lt; 30 Seconds</text>
    </g>

    <!-- Webhook settings -->
    <g transform="translate(32, 280)">
      <rect x="0" y="0" width="1206" height="240" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
      <text x="24" y="34" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Enterprise Integrations &amp; Webhook Endpoints</text>
      <text x="24" y="58" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Configured external event subscribers with HMAC-SHA256 signature verification</text>

      <line x1="24" y1="85" x2="1182" y2="85" stroke="#27272a"/>
      <text x="24" y="115" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Courier Line-Haul Dispatch Webhook</text>
      <text x="400" y="115" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">https://api.logistics-partner.co.id/v1/shipments/inbound</text>
      <text x="1100" y="115" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="end">ACTIVE (200 OK)</text>

      <line x1="24" y1="145" x2="1182" y2="145" stroke="#27272a"/>
      <text x="24" y="175" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Corporate Banking Mutasi Feed (BCA API)</text>
      <text x="400" y="175" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">https://api.mayastranawaloka.com/integrations/banking/bca/mutasi</text>
      <text x="1100" y="175" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="end">ACTIVE (200 OK)</text>
    </g>
  </g>"""

    svg_10 = build_erp_svg(
        url="https://erp.mayastranawaloka.com/settings/system",
        active_nav="Settings",
        title="Cluster Parameters &amp; Integrations",
        subtitle="Database Replication, Webhook Endpoints, Encrypted Backup &amp; Timezone Policies",
        btn1="Test Endpoints",
        btn2="Save Parameters",
        kpis=[
            ("DB REPLICATION LAG", "0.08 ms", "Synchronous replica active"),
            ("WEBHOOK DELIVERABILITY", "99.98 %", "Zero dropped callbacks"),
            ("BACKUP FREQUENCY", "Hourly WAL", "Encrypted multi-region S3"),
            ("UPTIME SLA", "99.99 %", "Continuous zero-downtime")
        ],
        content_svg=content_10
    )
    with open("assets/projects/erp/10-system-settings.svg", "w", encoding="utf-8") as f:
        f.write(svg_10)

    # -------------------------------------------------------------
    # Screen 11: Predictive Forecasting & Replenishment Model
    # -------------------------------------------------------------
    content_11 = """  <!-- Predictive Forecasting Content -->
  <g transform="translate(290, 300)">
    <!-- Forecast Chart Box -->
    <rect x="0" y="0" width="1230" height="340" rx="8" fill="#121215" stroke="#27272a" stroke-width="1"/>
    <text x="24" y="34" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">90-Day Predictive Demand Velocity vs Buffer Stock Simulation</text>
    <text x="24" y="56" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">ARIMA / Monte Carlo multi-warehouse replenishment algorithm - Jakarta Hub &amp; Regional DCs</text>
    <text x="1150" y="34" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600" text-anchor="end">Model Confidence: 99.4%</text>

    <!-- Forecast Curve Graphic -->
    <g transform="translate(24, 70)">
      <line x1="40" y1="30" x2="1140" y2="30" stroke="#1f1f23" stroke-width="1"/>
      <line x1="40" y1="90" x2="1140" y2="90" stroke="#1f1f23" stroke-width="1"/>
      <line x1="40" y1="150" x2="1140" y2="150" stroke="#1f1f23" stroke-width="1"/>
      <line x1="40" y1="210" x2="1140" y2="210" stroke="#1f1f23" stroke-width="1"/>

      <text x="30" y="34" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="end">40K</text>
      <text x="30" y="94" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="end">30K</text>
      <text x="30" y="154" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="end">20K</text>
      <text x="30" y="214" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="end">10K</text>

      <!-- Confidence band fill -->
      <path d="M 50 180 Q 250 160 450 120 T 850 70 T 1130 50 L 1130 90 Q 850 110 450 150 T 50 200 Z" fill="#ef4444" fill-opacity="0.12"/>
      <!-- Projected Mean Demand Line -->
      <path d="M 50 190 Q 250 170 450 135 T 850 90 T 1130 70" stroke="#ef4444" stroke-width="3" fill="none"/>
      <circle cx="1130" cy="70" r="5" fill="#ef4444"/>
      <!-- Safety Stock Threshold Line -->
      <line x1="50" y1="170" x2="1130" y2="170" stroke="#71717a" stroke-width="1.5" stroke-dasharray="6 4"/>
      <text x="1130" y="165" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" text-anchor="end">Safety Buffer Baseline (16,000 Units)</text>

      <!-- Timeline Axis -->
      <text x="50" y="235" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">Current</text>
      <text x="320" y="235" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">+15 Days</text>
      <text x="590" y="235" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">+30 Days</text>
      <text x="860" y="235" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">+60 Days</text>
      <text x="1130" y="235" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">+90 Days (Peak Q4)</text>
    </g>

    <!-- Replenishment Recommendations Table -->
    <g transform="translate(0, 360)">
      <rect x="0" y="0" width="1230" height="300" rx="8" fill="#121215" stroke="#27272a" stroke-width="1"/>
      <rect x="0" y="0" width="1230" height="42" fill="#18181b" rx="8"/>
      <text x="24" y="26" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">SKU CODE</text>
      <text x="180" y="26" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">PRODUCT NAME</text>
      <text x="500" y="26" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">CURRENT STOCK</text>
      <text x="660" y="26" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">30D VELOCITY</text>
      <text x="820" y="26" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">RE-ORDER ADVICE</text>
      <text x="1000" y="26" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">SUGGESTED VENDOR</text>
      <text x="1160" y="26" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">ACTION</text>

      <!-- Row 1 -->
      <g transform="translate(0, 42)">
        <text x="24" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">SKU-8921-JKT</text>
        <text x="180" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Precision Aluminum Chassis M4</text>
        <text x="500" y="32" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">840 Units</text>
        <text x="660" y="32" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">1,240 Units / mo</text>
        <rect x="820" y="16" width="120" height="24" rx="4" fill="#ffffff" fill-opacity="0.12"/>
        <text x="880" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="middle">+600 Units PO</text>
        <text x="1000" y="32" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">PT Metalindo Presisi</text>
        <text x="1160" y="32" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Order</text>
        <line x1="24" y1="48" x2="1206" y2="48" stroke="#1f1f23"/>
      </g>

      <!-- Row 2 -->
      <g transform="translate(0, 92)">
        <text x="24" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">SKU-7734-SBY</text>
        <text x="180" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Industrial Motherboard Micro-ATX</text>
        <text x="500" y="32" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">320 Units</text>
        <text x="660" y="32" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">450 Units / mo</text>
        <rect x="820" y="16" width="120" height="24" rx="4" fill="#ffffff" fill-opacity="0.12"/>
        <text x="880" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="middle">+300 Units PO</text>
        <text x="1000" y="32" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Global Components SG</text>
        <text x="1160" y="32" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Order</text>
        <line x1="24" y1="48" x2="1206" y2="48" stroke="#1f1f23"/>
      </g>

      <!-- Row 3 -->
      <g transform="translate(0, 142)">
        <text x="24" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">SKU-4410-BDG</text>
        <text x="180" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Copper Heat-Sink Assembly v2</text>
        <text x="500" y="32" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">2,100 Units</text>
        <text x="660" y="32" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">800 Units / mo</text>
        <rect x="820" y="16" width="120" height="24" rx="4" fill="#18181b" stroke="#27272a"/>
        <text x="880" y="32" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">Optimal Stock</text>
        <text x="1000" y="32" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">PT Thermal Nusantara</text>
        <text x="1160" y="32" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">View</text>
      </g>
    </g>
  </g>"""

    svg_11 = build_erp_svg(
        url="https://erp.mayastranawaloka.com/forecasting/predictive",
        active_nav="Warehouse Hub",
        title="Predictive Inventory &amp; Demand Forecasting",
        subtitle="Monte Carlo Replenishment Algorithm &amp; Auto PO Suggestions (Next 90 Days)",
        btn1="Run Simulation",
        btn2="Execute 2 POs",
        kpis=[
            ("FORECAST ACCURACY", "99.4 %", "Confidence interval verified"),
            ("SAFETY STOCK BUFFER", "16,000 Units", "Zero stockout risk"),
            ("ARMED RE-ORDERS", "Rp 420.000.000", "2 POs awaiting confirmation"),
            ("LEAD TIME VARIANCE", "-1.2 Days", "Multi-supplier optimization")
        ],
        content_svg=content_11
    )
    with open("assets/projects/erp/11-predictive-forecasting.svg", "w", encoding="utf-8") as f:
        f.write(svg_11)

    print("[*] Generated all 11 ERP SVGs successfully.")

if __name__ == "__main__":
    generate_all_erp()
