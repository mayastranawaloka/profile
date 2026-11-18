import os

os.makedirs("assets", exist_ok=True)

# 1. ERP Mockup SVG
erp_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 1000" width="1600" height="1000" fill="none">
  <defs>
    <linearGradient id="erpGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0.02"/>
    </linearGradient>
    <linearGradient id="chartGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0.0"/>
    </linearGradient>
  </defs>

  <!-- Background -->
  <rect width="1600" height="1000" fill="#09090b"/>

  <!-- Browser Header Bar -->
  <rect width="1600" height="52" fill="#111113" stroke="#27272a" stroke-width="1"/>
  <circle cx="36" cy="26" r="6" fill="#27272a"/>
  <circle cx="56" cy="26" r="6" fill="#27272a"/>
  <circle cx="76" cy="26" r="6" fill="#27272a"/>
  <rect x="520" y="14" width="560" height="24" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
  <text x="800" y="30" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle" letter-spacing="1">https://erp.mayastranawaloka.com/dashboard</text>

  <!-- Sidebar -->
  <rect x="0" y="52" width="260" height="948" fill="#0d0d10" stroke="#27272a" stroke-width="1"/>
  <!-- Logo / Brand in ERP -->
  <rect x="28" y="80" width="24" height="24" rx="4" fill="#ef4444"/>
  <circle cx="40" cy="92" r="3.5" fill="#fefefe"/>
  <text x="64" y="97" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="700" letter-spacing="1.5">MAYA ERP</text>

  <!-- Nav items -->
  <g transform="translate(24, 140)">
    <rect x="0" y="0" width="212" height="38" rx="6" fill="#ffffff" fill-opacity="0.08"/>
    <rect x="16" y="14" width="10" height="10" fill="#ffffff"/>
    <text x="38" y="24" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="500">Overview</text>

    <text x="38" y="70" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Inventory &amp; Stock</text>
    <rect x="16" y="60" width="10" height="10" fill="#52525b"/>

    <text x="38" y="116" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Orders &amp; Sales</text>
    <rect x="16" y="106" width="10" height="10" fill="#52525b"/>

    <text x="38" y="162" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Procurement</text>
    <rect x="16" y="152" width="10" height="10" fill="#52525b"/>

    <text x="38" y="208" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Finance &amp; Ledger</text>
    <rect x="16" y="198" width="10" height="10" fill="#52525b"/>

    <text x="38" y="254" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Warehouse Hub</text>
    <rect x="16" y="244" width="10" height="10" fill="#52525b"/>

    <text x="38" y="300" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Settings</text>
    <rect x="16" y="290" width="10" height="10" fill="#52525b"/>
  </g>

  <!-- User info at bottom sidebar -->
  <rect x="24" y="930" width="212" height="42" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
  <circle cx="48" cy="951" r="10" fill="#ef4444" fill-opacity="0.15"/>
  <circle cx="48" cy="951" r="4" fill="#ef4444"/>
  <text x="70" y="948" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Admin Operations</text>
  <text x="70" y="961" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Branch #04 - Jakarta</text>

  <!-- Top bar inside main content -->
  <g transform="translate(290, 80)">
    <text x="0" y="26" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="24" font-weight="600" letter-spacing="-0.5">Enterprise Resource Dashboard</text>
    <text x="0" y="48" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Multi-Warehouse Inventory &amp; Revenue Consolidation</text>

    <!-- Date selector & export button -->
    <rect x="1090" y="8" width="90" height="34" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
    <text x="1135" y="30" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">Export Data</text>

    <rect x="1195" y="8" width="75" height="34" rx="4" fill="#ffffff"/>
    <text x="1232" y="30" fill="#09090b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="middle">New Order</text>
  </g>

  <!-- KPI Cards -->
  <g transform="translate(290, 160)">
    <!-- Card 1 -->
    <rect x="0" y="0" width="298" height="120" rx="8" fill="#121215" stroke="#27272a" stroke-width="1"/>
    <text x="24" y="34" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="500">MONTHLY REVENUE</text>
    <text x="24" y="74" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="700">Rp 842.500.000</text>
    <text x="24" y="100" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">+18.4% from last period</text>

    <!-- Card 2 -->
    <rect x="324" y="0" width="298" height="120" rx="8" fill="#121215" stroke="#27272a" stroke-width="1"/>
    <text x="348" y="34" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="500">ACTIVE INVENTORY SKU</text>
    <text x="348" y="74" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="700">14,290 Units</text>
    <text x="348" y="100" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">99.2% in stock health</text>

    <!-- Card 3 -->
    <rect x="648" y="0" width="298" height="120" rx="8" fill="#121215" stroke="#27272a" stroke-width="1"/>
    <text x="672" y="34" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="500">PENDING FULFILLMENT</text>
    <text x="672" y="74" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="700">328 Orders</text>
    <text x="672" y="100" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">4 hubs processing</text>

    <!-- Card 4 -->
    <rect x="972" y="0" width="298" height="120" rx="8" fill="#121215" stroke="#27272a" stroke-width="1"/>
    <text x="996" y="34" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="500">OPERATIONAL MARGIN</text>
    <text x="996" y="74" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="700">34.8 %</text>
    <text x="996" y="100" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Automated cost reconciliation</text>
  </g>

  <!-- Large Chart Area -->
  <g transform="translate(290, 310)">
    <rect x="0" y="0" width="810" height="340" rx="8" fill="#121215" stroke="#27272a" stroke-width="1"/>
    <text x="24" y="34" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="15" font-weight="600">Production &amp; Cash Flow Forecast</text>
    <text x="24" y="52" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Rolling 12-month automated ledger sync</text>

    <!-- Chart Grid Lines -->
    <line x1="24" y1="90" x2="786" y2="90" stroke="#1f1f23" stroke-width="1"/>
    <line x1="24" y1="150" x2="786" y2="150" stroke="#1f1f23" stroke-width="1"/>
    <line x1="24" y1="210" x2="786" y2="210" stroke="#1f1f23" stroke-width="1"/>
    <line x1="24" y1="270" x2="786" y2="270" stroke="#1f1f23" stroke-width="1"/>

    <!-- Chart Polygon & Line -->
    <polygon points="24,250 100,230 180,240 260,190 340,170 420,200 500,140 580,120 660,130 740,90 786,85 786,270 24,270" fill="url(#chartGrad)"/>
    <polyline points="24,250 100,230 180,240 260,190 340,170 420,200 500,140 580,120 660,130 740,90 786,85" fill="none" stroke="#ffffff" stroke-width="2.5"/>

    <!-- Dots -->
    <circle cx="500" cy="140" r="4" fill="#ffffff"/>
    <circle cx="740" cy="90" r="4" fill="#ffffff"/>
    <circle cx="786" cy="85" r="5" fill="#ef4444"/>

    <!-- Months labels -->
    <text x="24" y="300" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Jan</text>
    <text x="180" y="300" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Apr</text>
    <text x="340" y="300" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Jul</text>
    <text x="500" y="300" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Oct</text>
    <text x="660" y="300" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Dec</text>
    <text x="760" y="300" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Forecast</text>
  </g>

  <!-- Side Warehouse Status -->
  <g transform="translate(1124, 310)">
    <rect x="0" y="0" width="436" height="340" rx="8" fill="#121215" stroke="#27272a" stroke-width="1"/>
    <text x="24" y="34" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="15" font-weight="600">Distribution Nodes</text>

    <!-- Node 1 -->
    <rect x="24" y="60" width="388" height="52" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
    <text x="40" y="85" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Warehouse Central (Cikarang)</text>
    <text x="40" y="100" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Capacity: 92% | Automated Dispatch</text>
    <text x="360" y="91" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="end">Optimal</text>

    <!-- Node 2 -->
    <rect x="24" y="124" width="388" height="52" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
    <text x="40" y="149" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Hub Surabaya Timur</text>
    <text x="40" y="164" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Capacity: 74% | Cross-Docking</text>
    <text x="360" y="155" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="end">Active</text>

    <!-- Node 3 -->
    <rect x="24" y="188" width="388" height="52" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
    <text x="40" y="213" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Hub Medan Belawan</text>
    <text x="40" y="228" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Capacity: 58% | Maritime Delivery</text>
    <text x="360" y="219" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="end">Active</text>

    <!-- Node 4 -->
    <rect x="24" y="252" width="388" height="52" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
    <text x="40" y="277" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Makassar Gateway</text>
    <text x="40" y="292" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Capacity: 45% | Eastern Feeder</text>
    <text x="360" y="283" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="end">Standby</text>
  </g>

  <!-- Data Table -->
  <g transform="translate(290, 675)">
    <rect x="0" y="0" width="1270" height="280" rx="8" fill="#121215" stroke="#27272a" stroke-width="1"/>
    <text x="24" y="34" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="15" font-weight="600">Recent Supply Chain Transactions</text>

    <!-- Table Header -->
    <line x1="24" y1="55" x2="1246" y2="55" stroke="#27272a" stroke-width="1"/>
    <text x="24" y="74" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">INVOICE #</text>
    <text x="180" y="74" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">CLIENT / DISTRIBUTOR</text>
    <text x="480" y="74" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">CATEGORY</text>
    <text x="700" y="74" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">TOTAL VALUE</text>
    <text x="960" y="74" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">STATUS</text>

    <!-- Row 1 -->
    <line x1="24" y1="92" x2="1246" y2="92" stroke="#1f1f23" stroke-width="1"/>
    <text x="24" y="118" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">TRX-2026-8812</text>
    <text x="180" y="118" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">PT Sinar Makmur Sentosa</text>
    <text x="480" y="118" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Raw Material Bulk</text>
    <text x="700" y="118" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Rp 128.450.000</text>
    <rect x="960" y="104" width="76" height="20" rx="3" fill="#ffffff" fill-opacity="0.12"/>
    <text x="998" y="118" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Dispatched</text>

    <!-- Row 2 -->
    <line x1="24" y1="140" x2="1246" y2="140" stroke="#1f1f23" stroke-width="1"/>
    <text x="24" y="166" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">TRX-2026-8813</text>
    <text x="180" y="166" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">CV Indo Niaga Logistik</text>
    <text x="480" y="166" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">FMCG Retail Pack</text>
    <text x="700" y="166" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Rp 64.200.000</text>
    <rect x="960" y="152" width="76" height="20" rx="3" fill="#ffffff" fill-opacity="0.12"/>
    <text x="998" y="166" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="600" text-anchor="middle">In Transit</text>

    <!-- Row 3 -->
    <line x1="24" y1="188" x2="1246" y2="188" stroke="#1f1f23" stroke-width="1"/>
    <text x="24" y="214" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">TRX-2026-8814</text>
    <text x="180" y="214" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">PT Prima Baja Lestari</text>
    <text x="480" y="214" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Component Fabrication</text>
    <text x="700" y="214" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Rp 312.900.000</text>
    <rect x="960" y="200" width="76" height="20" rx="3" fill="#ffffff" fill-opacity="0.12"/>
    <text x="998" y="214" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Settled</text>
  </g>
</svg>'''

with open("assets/projects/showcases/project-erp.svg", "w") as f:
    f.write(erp_svg.strip())
print("[OK] generated assets/projects/showcases/project-erp.svg")

# 2. Toko Online / E-Commerce Mockup SVG
ecommerce_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 1000" width="1600" height="1000" fill="none">
  <!-- Background -->
  <rect width="1600" height="1000" fill="#0a0a0c"/>

  <!-- Browser Header Bar -->
  <rect width="1600" height="52" fill="#121215" stroke="#27272a" stroke-width="1"/>
  <circle cx="36" cy="26" r="6" fill="#27272a"/>
  <circle cx="56" cy="26" r="6" fill="#27272a"/>
  <circle cx="76" cy="26" r="6" fill="#27272a"/>
  <rect x="520" y="14" width="560" height="24" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
  <text x="800" y="30" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle" letter-spacing="1">https://store.mayastranawaloka.com/curated-edition</text>

  <!-- Store Navigation Bar -->
  <rect y="52" width="1600" height="70" fill="#0d0d10" stroke="#1f1f23" stroke-width="1"/>
  <rect x="52" y="81" width="16" height="16" rx="3" fill="#ef4444"/>
  <circle cx="60" cy="89" r="3" fill="#fefefe"/>
  <text x="80" y="94" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="16" font-weight="800" letter-spacing="3">KRONIK COMMERCE</text>

  <g transform="translate(480, 94)">
    <text x="0" y="0" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600" letter-spacing="1.5">ALL OBJECTS</text>
    <text x="140" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" letter-spacing="1.5">LIVING</text>
    <text x="240" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" letter-spacing="1.5">HARDWARE</text>
    <text x="360" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" letter-spacing="1.5">ARCHIVES</text>
    <text x="480" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" letter-spacing="1.5">EDITORIAL</text>
  </g>

  <!-- Currency & Cart -->
  <g transform="translate(1380, 94)">
    <text x="0" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" letter-spacing="1">IDR / EN</text>
    <rect x="80" y="-16" width="68" height="26" rx="13" fill="#ffffff"/>
    <text x="114" y="1" fill="#0a0a0c" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" text-anchor="middle">BAG (3)</text>
    <circle cx="152" cy="-14" r="4.5" fill="#ef4444"/>
  </g>

  <!-- Hero Feature Banner -->
  <g transform="translate(80, 150)">
    <rect x="0" y="0" width="1020" height="380" rx="6" fill="#141418" stroke="#27272a" stroke-width="1"/>
    
    <!-- Geometric artwork inside hero -->
    <rect x="620" y="40" width="350" height="300" rx="4" fill="#1c1c22" stroke="#323238" stroke-width="1"/>
    <circle cx="795" cy="190" r="100" fill="#26262e"/>
    <circle cx="795" cy="190" r="60" fill="#0d0d10"/>
    <line x1="620" y1="190" x2="970" y2="190" stroke="#323238" stroke-width="1"/>
    <line x1="795" y1="40" x2="795" y2="340" stroke="#323238" stroke-width="1"/>

    <text x="50" y="90" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" letter-spacing="3" font-weight="600">SERIES 04 / EDITION 2026</text>
    <text x="50" y="150" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="44" font-weight="700" letter-spacing="-1">MONOCHROME</text>
    <text x="50" y="200" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="44" font-weight="700" letter-spacing="-1">STUDIO OBJECTS</text>
    <text x="50" y="240" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" max-width="480">Direct-to-consumer artisanal home and studio instruments.</text>
    <text x="50" y="260" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14">Engineered for commercial spaces and boutique environments.</text>

    <rect x="50" y="295" width="150" height="42" rx="4" fill="#ef4444"/>
    <text x="125" y="321" fill="#fefefe" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" letter-spacing="1" text-anchor="middle">EXPLORE DROP</text>
  </g>

  <!-- Cart / Checkout Preview Drawer on the Right -->
  <g transform="translate(1130, 150)">
    <rect x="0" y="0" width="390" height="800" rx="6" fill="#121216" stroke="#27272a" stroke-width="1"/>
    <text x="30" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="16" font-weight="700">SHOPPING BAG</text>
    <text x="330" y="44" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">3 ITEMS</text>
    <line x1="30" y1="65" x2="360" y2="65" stroke="#27272a" stroke-width="1"/>

    <!-- Cart Item 1 -->
    <rect x="30" y="85" width="60" height="60" rx="4" fill="#1e1e24"/>
    <circle cx="60" cy="115" r="15" fill="#323238"/>
    <text x="105" y="105" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">Matte Ceramic Carafe</text>
    <text x="105" y="125" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Qty: 1 | Midnight Black</text>
    <text x="105" y="142" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700">Rp 480.000</text>

    <!-- Cart Item 2 -->
    <rect x="30" y="170" width="60" height="60" rx="4" fill="#1e1e24"/>
    <rect x="45" y="185" width="30" height="30" rx="2" fill="#323238"/>
    <text x="105" y="190" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">Linear Anodized Tray</text>
    <text x="105" y="210" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Qty: 2 | Raw Silver</text>
    <text x="105" y="227" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700">Rp 650.000</text>

    <!-- Cart Item 3 -->
    <rect x="30" y="255" width="60" height="60" rx="4" fill="#1e1e24"/>
    <circle cx="60" cy="285" r="18" fill="#323238"/>
    <text x="105" y="275" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">Solid Cast Iron Desk Lamp</text>
    <text x="105" y="295" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Qty: 1 | Carbon Edition</text>
    <text x="105" y="312" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700">Rp 1.250.000</text>

    <line x1="30" y1="340" x2="360" y2="340" stroke="#27272a" stroke-width="1"/>

    <!-- Summary -->
    <text x="30" y="375" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Subtotal</text>
    <text x="360" y="375" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600" text-anchor="end">Rp 2.380.000</text>

    <text x="30" y="405" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Insured Courier (JNE/SiCepat)</text>
    <text x="360" y="405" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="end">FREE</text>

    <line x1="30" y1="430" x2="360" y2="430" stroke="#27272a" stroke-width="1"/>

    <text x="30" y="465" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="700">TOTAL</text>
    <text x="360" y="465" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="18" font-weight="800" text-anchor="end">Rp 2.380.000</text>

    <!-- Payment Gateway Badges -->
    <rect x="30" y="495" width="330" height="48" rx="4" fill="#ffffff"/>
    <text x="195" y="525" fill="#09090b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" letter-spacing="1" text-anchor="middle">INSTANT CHECKOUT (QRIS / VA)</text>

    <text x="195" y="570" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" text-anchor="middle">Encrypted 256-bit automated payment sync</text>
  </g>

  <!-- Product Catalog Grid -->
  <g transform="translate(80, 560)">
    <text x="0" y="24" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="18" font-weight="700" letter-spacing="1">CURATED INVENTORY</text>
    <text x="960" y="24" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">VIEW COMPLETE COLLECTION &#8594;</text>

    <!-- Product 1 -->
    <rect x="0" y="50" width="320" height="340" rx="4" fill="#121215" stroke="#27272a" stroke-width="1"/>
    <rect x="20" y="70" width="280" height="200" rx="2" fill="#18181e"/>
    <circle cx="160" cy="170" r="50" fill="#24242c"/>
    <text x="20" y="300" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Matte Obsidian Vessel</text>
    <text x="20" y="322" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Handcrafted Studio Stoneware</text>
    <text x="300" y="315" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="700" text-anchor="end">Rp 520.000</text>

    <!-- Product 2 -->
    <rect x="350" y="50" width="320" height="340" rx="4" fill="#121215" stroke="#27272a" stroke-width="1"/>
    <rect x="370" y="70" width="280" height="200" rx="2" fill="#18181e"/>
    <rect x="470" y="120" width="80" height="100" rx="4" fill="#24242c"/>
    <text x="370" y="300" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Acoustic Wool Desk Mat</text>
    <text x="370" y="322" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Organic Felt Surface 900x400</text>
    <text x="650" y="315" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="700" text-anchor="end">Rp 390.000</text>

    <!-- Product 3 -->
    <rect x="700" y="50" width="320" height="340" rx="4" fill="#121215" stroke="#27272a" stroke-width="1"/>
    <rect x="720" y="70" width="280" height="200" rx="2" fill="#18181e"/>
    <polygon points="860,110 810,210 910,210" fill="#24242c"/>
    <text x="720" y="300" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Brass Geometric Bookend</text>
    <text x="720" y="322" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Solid Milled Metal Pair</text>
    <text x="1000" y="315" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="700" text-anchor="end">Rp 890.000</text>
  </g>
</svg>'''

with open("assets/projects/showcases/project-ecommerce.svg", "w") as f:
    f.write(ecommerce_svg.strip())
print("[OK] generated assets/projects/showcases/project-ecommerce.svg")

# 3. CMS Mockup SVG
cms_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 1000" width="1600" height="1000" fill="none">
  <!-- Background -->
  <rect width="1600" height="1000" fill="#09090b"/>

  <!-- Browser Header Bar -->
  <rect width="1600" height="52" fill="#121215" stroke="#27272a" stroke-width="1"/>
  <circle cx="36" cy="26" r="6" fill="#27272a"/>
  <circle cx="56" cy="26" r="6" fill="#27272a"/>
  <circle cx="76" cy="26" r="6" fill="#27272a"/>
  <rect x="520" y="14" width="560" height="24" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
  <text x="800" y="30" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle" letter-spacing="1">https://cms.mayastranawaloka.com/editor/articles/8901</text>

  <!-- Sidebar -->
  <rect x="0" y="52" width="250" height="948" fill="#0c0c0e" stroke="#27272a" stroke-width="1"/>
  <rect x="28" y="82" width="18" height="18" rx="4" fill="#ef4444"/>
  <circle cx="37" cy="91" r="3" fill="#fefefe"/>
  <text x="56" y="96" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="15" font-weight="800" letter-spacing="2">PULSE CMS</text>

  <g transform="translate(24, 140)">
    <text x="38" y="24" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Dashboard</text>
    <rect x="16" y="14" width="10" height="10" fill="#52525b"/>

    <rect x="0" y="46" width="202" height="38" rx="6" fill="#ffffff" fill-opacity="0.08"/>
    <text x="38" y="70" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">Articles &amp; Posts</text>
    <rect x="16" y="60" width="10" height="10" fill="#ffffff"/>

    <text x="38" y="116" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Media Library</text>
    <rect x="16" y="106" width="10" height="10" fill="#52525b"/>

    <text x="38" y="162" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Categories &amp; Tags</text>
    <rect x="16" y="152" width="10" height="10" fill="#52525b"/>

    <text x="38" y="208" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Editorial Calendar</text>
    <rect x="16" y="198" width="10" height="10" fill="#52525b"/>

    <text x="38" y="254" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">SEO Diagnostics</text>
    <rect x="16" y="244" width="10" height="10" fill="#52525b"/>

    <text x="38" y="300" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Team &amp; Roles</text>
    <rect x="16" y="290" width="10" height="10" fill="#52525b"/>

    <text x="38" y="346" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">System Settings</text>
    <rect x="16" y="336" width="10" height="10" fill="#52525b"/>
  </g>

  <!-- Editorial Top Bar -->
  <g transform="translate(280, 80)">
    <text x="0" y="24" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Articles / Enterprise Architecture / Edit Post</text>
    <rect x="850" y="4" width="110" height="34" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
    <text x="905" y="26" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="middle">Save Draft</text>

    <rect x="975" y="4" width="110" height="34" rx="4" fill="#ef4444"/>
    <text x="1030" y="26" fill="#fefefe" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Publish Live</text>
  </g>

  <!-- Editor Main Area -->
  <g transform="translate(280, 140)">
    <rect x="0" y="0" width="880" height="820" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>

    <!-- Document Toolbar -->
    <rect x="0" y="0" width="880" height="50" fill="#151518" stroke="#27272a" stroke-width="1"/>
    <text x="30" y="30" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">H1</text>
    <text x="70" y="30" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">H2</text>
    <text x="110" y="30" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">B</text>
    <text x="140" y="30" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-style="italic">I</text>
    <text x="170" y="30" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">&lt;/&gt;</text>
    <text x="210" y="30" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Media</text>
    <text x="270" y="30" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Quote</text>
    <text x="840" y="30" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="end">1,480 Words | 6 min read</text>

    <!-- Post Title -->
    <text x="40" y="110" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="32" font-weight="800" letter-spacing="-0.5">Architectural Minimalist Systems</text>
    <text x="40" y="150" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="32" font-weight="800" letter-spacing="-0.5">for Mid-Market Enterprise 2026</text>

    <!-- Meta Subtitle -->
    <text x="40" y="190" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14">Published by Editorial Board &#8226; Updated 14 minutes ago &#8226; Public Visibility</text>

    <!-- Featured Header Visual inside editor -->
    <rect x="40" y="220" width="800" height="220" rx="4" fill="#1b1b20" stroke="#2d2d34" stroke-width="1"/>
    <circle cx="440" cy="330" r="50" fill="#292932"/>
    <text x="440" y="335" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="middle">Featured Hero Cover Image [1920x1080]</text>

    <!-- Content Paragraphs -->
    <text x="40" y="480" fill="#e4e4e7" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="15" line-height="24">Modern enterprise applications require high-precision information density without perceptual</text>
    <text x="40" y="508" fill="#e4e4e7" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="15">clutter. By utilizing strict monochromatic typography, intentional whitespace, and zero superfluous</text>
    <text x="40" y="536" fill="#e4e4e7" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="15">embellishments, digital operations achieve instantaneous user comprehension.</text>

    <!-- Quote Block -->
    <rect x="40" y="570" width="4" height="60" fill="#ffffff"/>
    <text x="60" y="595" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="15" font-style="italic">"Simplicity is not the absence of clutter, that's a consequence of simplicity."</text>
    <text x="60" y="620" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Jonathan Ive, Industrial Architecture</text>

    <!-- Structured Data Subheader -->
    <text x="40" y="675" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="18" font-weight="700">Core Infrastructure Deliverables</text>
    <text x="40" y="710" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14">1. Autonomous CMS synchronization with edge caching layers.</text>
    <text x="40" y="735" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14">2. Zero latency content delivery network with automated asset compression.</text>
    <text x="40" y="760" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14">3. Granular RBAC permissions for enterprise editorial departments.</text>
  </g>

  <!-- Sidebar Inspector on the Right -->
  <g transform="translate(1190, 140)">
    <rect x="0" y="0" width="370" height="820" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
    <text x="24" y="36" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="700">DOCUMENT METRICS</text>
    <line x1="24" y1="52" x2="346" y2="52" stroke="#27272a" stroke-width="1"/>

    <!-- SEO Score Card -->
    <rect x="24" y="70" width="322" height="90" rx="4" fill="#18181c" stroke="#27272a" stroke-width="1"/>
    <text x="44" y="100" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">SEARCH OPTIMIZATION INDEX</text>
    <text x="44" y="136" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="800">98 / 100</text>
    <text x="240" y="136" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">GRADE A+</text>

    <!-- Fields -->
    <text x="24" y="195" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Permalink Slug</text>
    <rect x="24" y="208" width="322" height="36" rx="4" fill="#18181c" stroke="#27272a" stroke-width="1"/>
    <text x="36" y="231" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">/insights/architectural-minimalist-systems</text>

    <text x="24" y="275" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Primary Category</text>
    <rect x="24" y="288" width="322" height="36" rx="4" fill="#18181c" stroke="#27272a" stroke-width="1"/>
    <text x="36" y="311" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Enterprise Technology</text>

    <text x="24" y="355" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Tags</text>
    <rect x="24" y="370" width="80" height="26" rx="13" fill="#ffffff" fill-opacity="0.1"/>
    <text x="64" y="387" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">#ERP</text>
    <rect x="114" y="370" width="80" height="26" rx="13" fill="#ffffff" fill-opacity="0.1"/>
    <text x="154" y="387" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">#Design</text>
    <rect x="204" y="370" width="80" height="26" rx="13" fill="#ffffff" fill-opacity="0.1"/>
    <text x="244" y="387" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">#Cloud</text>

    <line x1="24" y1="425" x2="346" y2="425" stroke="#27272a" stroke-width="1"/>

    <!-- Revision log -->
    <text x="24" y="455" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">AUDIT TRAIL</text>
    <text x="24" y="485" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Rev #42: Updated layout schematics</text>
    <text x="24" y="502" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Today, 00:32 &#8226; Lead Engineer</text>

    <text x="24" y="535" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Rev #41: Added executive summary</text>
    <text x="24" y="552" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Yesterday, 18:20 &#8226; Managing Editor</text>
  </g>
</svg>'''

with open("assets/projects/showcases/project-cms.svg", "w") as f:
    f.write(cms_svg.strip())
print("[OK] generated assets/projects/showcases/project-cms.svg")
