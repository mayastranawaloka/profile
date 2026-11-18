import os
import xml.etree.ElementTree as ET

def get_browser_header(url):
    return f"""  <!-- Browser Header Bar -->
  <rect width="1600" height="52" fill="#121215" stroke="#27272a" stroke-width="1"/>
  <circle cx="36" cy="26" r="6" fill="#27272a"/>
  <circle cx="56" cy="26" r="6" fill="#27272a"/>
  <circle cx="76" cy="26" r="6" fill="#27272a"/>
  <rect x="520" y="14" width="560" height="24" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
  <text x="800" y="30" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle" letter-spacing="1">{url}</text>"""

def get_store_nav(active_cat="ALL OBJECTS", bag_count=3):
    cats = ["ALL OBJECTS", "LIVING", "HARDWARE", "ARCHIVES", "EDITORIAL"]
    cat_svg = ""
    x_pos = 0
    for c in cats:
        is_active = (c == active_cat)
        color = "#ffffff" if is_active else "#71717a"
        weight = 'font-weight="600"' if is_active else ""
        cat_svg += f'<text x="{x_pos}" y="0" fill="{color}" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" {weight} letter-spacing="1.5">{c}</text>\n    '
        x_pos += 120

    return f"""  <!-- Store Navigation Bar -->
  <rect y="52" width="1600" height="70" fill="#0d0d10" stroke="#1f1f23" stroke-width="1"/>
  <text x="80" y="94" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="16" font-weight="800" letter-spacing="3">KRONIK COMMERCE</text>

  <g transform="translate(480, 94)">
    {cat_svg}
  </g>

  <!-- Currency & Cart -->
  <g transform="translate(1380, 94)">
    <text x="0" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" letter-spacing="1">IDR / EN</text>
    <rect x="80" y="-16" width="68" height="26" rx="13" fill="#ffffff"/>
    <text x="114" y="1" fill="#0a0a0c" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" text-anchor="middle">BAG ({bag_count})</text>
  </g>"""

def build_ecommerce_svg(url, active_cat, bag_count, content_svg):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 1000" width="1600" height="1000" fill="none">
  <!-- Background -->
  <rect width="1600" height="1000" fill="#0a0a0c"/>

{get_browser_header(url)}

{get_store_nav(active_cat, bag_count)}

{content_svg}
</svg>"""

print("E-commerce base generator defined.")

def generate_all_ecommerce():
    os.makedirs("assets/projects/ecommerce", exist_ok=True)

    # -------------------------------------------------------------
    # Screen 01: Curated Storefront (100% Home Master Parity)
    # -------------------------------------------------------------
    with open("assets/project-ecommerce.svg", "r", encoding="utf-8") as f:
        svg_01 = f.read()
    with open("assets/projects/ecommerce/01-curated-storefront.svg", "w", encoding="utf-8") as f:
        f.write(svg_01)

    # -------------------------------------------------------------
    # Screen 02: Product Detail Page (PDP)
    # -------------------------------------------------------------
    content_02 = """  <!-- Product Detail Section -->
  <g transform="translate(80, 150)">
    <!-- Breadcrumbs -->
    <text x="0" y="16" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">CATALOG / LIVING OBJECTS / CERAMICS / MATTE OBSIDIAN VESSEL</text>

    <!-- Left: Large Product Visual Showcase -->
    <g transform="translate(0, 40)">
      <rect x="0" y="0" width="860" height="740" rx="6" fill="#141418" stroke="#27272a" stroke-width="1"/>
      <rect x="40" y="40" width="780" height="520" rx="4" fill="#18181e"/>
      <circle cx="430" cy="300" r="160" fill="#22222a"/>
      <circle cx="430" cy="300" r="100" fill="#0d0d10"/>
      <circle cx="430" cy="300" r="50" fill="#1c1c24"/>
      
      <!-- Multi-Angle Thumbnails -->
      <g transform="translate(40, 580)">
        <rect x="0" y="0" width="120" height="120" rx="4" fill="#18181e" stroke="#ffffff" stroke-width="2"/>
        <circle cx="60" cy="60" r="25" fill="#24242c"/>

        <rect x="140" y="0" width="120" height="120" rx="4" fill="#18181e" stroke="#27272a" stroke-width="1"/>
        <rect x="175" y="35" width="50" height="50" rx="2" fill="#24242c"/>

        <rect x="280" y="0" width="120" height="120" rx="4" fill="#18181e" stroke="#27272a" stroke-width="1"/>
        <polygon points="340,35 315,85 365,85" fill="#24242c"/>
      </g>
    </g>

    <!-- Right: Buy Box & Product Specifications -->
    <g transform="translate(900, 40)">
      <rect x="0" y="0" width="540" height="740" rx="6" fill="#121216" stroke="#27272a" stroke-width="1"/>
      <g transform="translate(40, 40)">
        <text x="0" y="20" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" letter-spacing="2" font-weight="700">LIMITED STUDIO RUN // 100 PIECES</text>
        <text x="0" y="60" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="700">Matte Obsidian Vessel</text>
        <text x="0" y="96" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="22" font-weight="800">Rp 520.000</text>
        <text x="460" y="96" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600" text-anchor="end">IN STOCK (42 LEFT)</text>

        <line x1="0" y1="120" x2="460" y2="120" stroke="#27272a" stroke-width="1"/>

        <!-- Description -->
        <text x="0" y="150" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" line-height="22">Meticulously thrown stoneware vessel finished in a tactile matte obsidian</text>
        <text x="0" y="172" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">glaze. Fired at 1280&#176;C for maximum structural density and watertight seal.</text>

        <!-- Variant Selector -->
        <text x="0" y="220" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" letter-spacing="1">SELECT FINISH</text>
        <rect x="0" y="235" width="140" height="38" rx="4" fill="#ffffff" fill-opacity="0.08" stroke="#ffffff" stroke-width="1"/>
        <text x="70" y="259" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="middle">MIDNIGHT OBSIDIAN</text>

        <rect x="155" y="235" width="140" height="38" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
        <text x="225" y="259" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">RAW CARBON</text>

        <rect x="310" y="235" width="140" height="38" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
        <text x="380" y="259" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">SANDSTONE GREY</text>

        <!-- Quantity & Add to Cart -->
        <text x="0" y="315" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" letter-spacing="1">QUANTITY</text>
        <rect x="0" y="330" width="100" height="44" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
        <text x="20" y="357" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="16">-</text>
        <text x="50" y="357" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="700" text-anchor="middle">1</text>
        <text x="80" y="357" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="16">+</text>

        <rect x="120" y="330" width="340" height="44" rx="4" fill="#ffffff"/>
        <text x="290" y="357" fill="#09090b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" letter-spacing="1" text-anchor="middle">ADD TO SHOPPING BAG</text>

        <!-- Shipping & Warranty Perks -->
        <g transform="translate(0, 420)">
          <rect x="0" y="0" width="460" height="180" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <text x="24" y="34" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Direct Courier Guarantee</text>
          <text x="24" y="56" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Same-day dispatch from Jakarta fulfillment hub before 16:00 WIB</text>

          <text x="24" y="94" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Breakage Transit Insurance</text>
          <text x="24" y="116" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">100% replacement guarantee if damaged during shipping transit</text>

          <text x="24" y="150" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Authentic Studio Provenance</text>
          <text x="24" y="168" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Serialized edition stamp stamped on base</text>
        </g>
      </g>
    </g>
  </g>"""

    svg_02 = build_ecommerce_svg(
        url="https://store.mayastranawaloka.com/products/matte-obsidian-vessel",
        active_cat="ALL OBJECTS",
        bag_count=3,
        content_svg=content_02
    )
    with open("assets/projects/ecommerce/02-product-detail.svg", "w", encoding="utf-8") as f:
        f.write(svg_02)

    # -------------------------------------------------------------
    # Screen 03: Instant Search & Faceted Filtering
    # -------------------------------------------------------------
    content_03 = """  <!-- Search & Filter Layout -->
  <g transform="translate(80, 150)">
    <!-- Search Bar Top Input -->
    <rect x="0" y="0" width="1440" height="60" rx="6" fill="#141418" stroke="#27272a" stroke-width="1"/>
    <text x="32" y="36" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="16" font-weight="500">search: "studio objects"</text>
    <text x="1400" y="36" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="end">Sub-42ms latency &#8226; 24 Matches Found</text>

    <!-- Left: Filter Facets -->
    <g transform="translate(0, 80)">
      <rect x="0" y="0" width="300" height="700" rx="6" fill="#121216" stroke="#27272a" stroke-width="1"/>
      <g transform="translate(24, 30)">
        <text x="0" y="16" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" letter-spacing="1">FACET FILTERS</text>

        <!-- Category -->
        <text x="0" y="54" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700">COLLECTION</text>
        <rect x="0" y="70" width="14" height="14" rx="2" fill="#ffffff"/>
        <text x="24" y="82" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Studio Hardware (14)</text>
        
        <rect x="0" y="100" width="14" height="14" rx="2" fill="#1f1f23"/>
        <text x="24" y="112" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Living Ceramics (8)</text>

        <rect x="0" y="130" width="14" height="14" rx="2" fill="#1f1f23"/>
        <text x="24" y="142" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Desk Accessories (12)</text>

        <!-- Price Slider -->
        <text x="0" y="190" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700">PRICE RANGE (IDR)</text>
        <rect x="0" y="210" width="252" height="6" rx="3" fill="#1f1f23"/>
        <rect x="0" y="210" width="180" height="6" rx="3" fill="#ffffff"/>
        <circle cx="180" cy="213" r="8" fill="#ffffff"/>
        <text x="0" y="240" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Rp 100.000 - Rp 2.500.000</text>

        <!-- Material Filter -->
        <text x="0" y="280" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700">PRIMARY MATERIAL</text>
        <text x="0" y="306" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">&#8226; Anodized Aluminum</text>
        <text x="0" y="330" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">&#8226; Solid Cast Iron</text>
        <text x="0" y="354" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">&#8226; Tactile Stoneware</text>
        <text x="0" y="378" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">&#8226; Organic Wool Felt</text>
      </g>
    </g>

    <!-- Right: Matched Product Results -->
    <g transform="translate(330, 80)">
      <!-- Item 1 -->
      <rect x="0" y="0" width="345" height="330" rx="4" fill="#121215" stroke="#27272a" stroke-width="1"/>
      <rect x="20" y="20" width="305" height="190" rx="2" fill="#18181e"/>
      <circle cx="172" cy="115" r="45" fill="#24242c"/>
      <text x="20" y="245" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Matte Ceramic Carafe</text>
      <text x="20" y="268" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Kitchen / Stoneware</text>
      <text x="325" y="260" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="700" text-anchor="end">Rp 480.000</text>

      <!-- Item 2 -->
      <rect x="375" y="0" width="345" height="330" rx="4" fill="#121215" stroke="#27272a" stroke-width="1"/>
      <rect x="395" y="20" width="305" height="190" rx="2" fill="#18181e"/>
      <rect x="510" y="70" width="75" height="90" rx="4" fill="#24242c"/>
      <text x="395" y="245" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Linear Anodized Tray</text>
      <text x="395" y="268" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Hardware / Silver</text>
      <text x="700" y="260" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="700" text-anchor="end">Rp 650.000</text>

      <!-- Item 3 -->
      <rect x="750" y="0" width="345" height="330" rx="4" fill="#121215" stroke="#27272a" stroke-width="1"/>
      <rect x="770" y="20" width="305" height="190" rx="2" fill="#18181e"/>
      <polygon points="942,65 895,165 990,165" fill="#24242c"/>
      <text x="770" y="245" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Cast Iron Desk Lamp</text>
      <text x="770" y="268" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Lighting / Carbon</text>
      <text x="1075" y="260" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="700" text-anchor="end">Rp 1.250.000</text>

      <!-- Second Row of Items -->
      <g transform="translate(0, 360)">
        <rect x="0" y="0" width="345" height="330" rx="4" fill="#121215" stroke="#27272a" stroke-width="1"/>
        <rect x="20" y="20" width="305" height="190" rx="2" fill="#18181e"/>
        <circle cx="172" cy="115" r="45" fill="#24242c"/>
        <text x="20" y="245" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Acoustic Desk Pad</text>
        <text x="20" y="268" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Desk / Felt Surface</text>
        <text x="325" y="260" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="700" text-anchor="end">Rp 390.000</text>

        <rect x="375" y="0" width="345" height="330" rx="4" fill="#121215" stroke="#27272a" stroke-width="1"/>
        <rect x="395" y="20" width="305" height="190" rx="2" fill="#18181e"/>
        <rect x="510" y="70" width="75" height="90" rx="4" fill="#24242c"/>
        <text x="395" y="245" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Brass Bookend Pair</text>
        <text x="395" y="268" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Living / Milled Brass</text>
        <text x="700" y="260" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="700" text-anchor="end">Rp 890.000</text>

        <rect x="750" y="0" width="345" height="330" rx="4" fill="#121215" stroke="#27272a" stroke-width="1"/>
        <rect x="770" y="20" width="305" height="190" rx="2" fill="#18181e"/>
        <polygon points="942,65 895,165 990,165" fill="#24242c"/>
        <text x="770" y="245" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Minimalist Timer</text>
        <text x="770" y="268" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Studio / Analog</text>
        <text x="1075" y="260" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="700" text-anchor="end">Rp 320.000</text>
      </g>
    </g>
  </g>"""

    svg_03 = build_ecommerce_svg(
        url="https://store.mayastranawaloka.com/search?q=studio",
        active_cat="HARDWARE",
        bag_count=3,
        content_svg=content_03
    )
    with open("assets/projects/ecommerce/03-instant-search-filters.svg", "w", encoding="utf-8") as f:
        f.write(svg_03)

    # -------------------------------------------------------------
    # Screen 04: Slide Cart Ledger
    # -------------------------------------------------------------
    content_04 = """  <!-- Slide Cart Expanded Layout -->
  <g transform="translate(80, 150)">
    <!-- Main Store Background (dimmed) -->
    <rect x="0" y="0" width="940" height="780" rx="6" fill="#101013" stroke="#27272a" stroke-width="1"/>
    <text x="40" y="50" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">ACTIVE BROWSING SESSION // STORE CATALOG IN BACKGROUND</text>
    <rect x="40" y="80" width="400" height="300" rx="4" fill="#16161c"/>
    <rect x="470" y="80" width="430" height="300" rx="4" fill="#16161c"/>

    <!-- High-Fidelity Slide Cart Drawer (Prominent on Right) -->
    <g transform="translate(970, 0)">
      <rect x="0" y="0" width="550" height="780" rx="6" fill="#121216" stroke="#ffffff" stroke-width="1.5"/>
      <g transform="translate(36, 40)">
        <text x="0" y="20" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="20" font-weight="700">SHOPPING BAG</text>
        <text x="470" y="20" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" text-anchor="end">[CLOSE &#10005;]</text>

        <!-- Free shipping meter -->
        <rect x="0" y="45" width="478" height="32" rx="4" fill="#18181b"/>
        <text x="16" y="66" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">You have unlocked FREE Insured Courier Shipping!</text>

        <!-- Cart Item 1 -->
        <g transform="translate(0, 105)">
          <rect x="0" y="0" width="80" height="80" rx="4" fill="#1c1c24"/>
          <circle cx="40" cy="40" r="22" fill="#292934"/>
          <text x="96" y="24" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Matte Ceramic Carafe</text>
          <text x="96" y="46" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Midnight Obsidian Edition</text>
          <text x="96" y="70" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">Rp 480.000</text>
          <text x="478" y="70" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" text-anchor="end">Qty: 1 &#8226; Remove</text>
        </g>
        <line x1="0" y1="205" x2="478" y2="205" stroke="#27272a"/>

        <!-- Cart Item 2 -->
        <g transform="translate(0, 225)">
          <rect x="0" y="0" width="80" height="80" rx="4" fill="#1c1c24"/>
          <rect x="25" y="25" width="30" height="30" rx="2" fill="#292934"/>
          <text x="96" y="24" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Linear Anodized Tray</text>
          <text x="96" y="46" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Raw Silver / 400x200</text>
          <text x="96" y="70" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">Rp 650.000</text>
          <text x="478" y="70" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" text-anchor="end">Qty: 2 &#8226; Remove</text>
        </g>
        <line x1="0" y1="325" x2="478" y2="325" stroke="#27272a"/>

        <!-- Promo Code Input -->
        <g transform="translate(0, 350)">
          <rect x="0" y="0" width="350" height="40" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <text x="16" y="25" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">ENTER VOUCHER CODE</text>
          <rect x="360" y="0" width="118" height="40" rx="4" fill="#ffffff" fill-opacity="0.08"/>
          <text x="419" y="25" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" text-anchor="middle">APPLY</text>
        </g>

        <!-- Ledger Summary -->
        <g transform="translate(0, 420)">
          <text x="0" y="20" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Bag Subtotal</text>
          <text x="478" y="20" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600" text-anchor="end">Rp 2.380.000</text>

          <text x="0" y="50" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Shipping (JNE / SiCepat Express)</text>
          <text x="478" y="50" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600" text-anchor="end">Rp 0 (FREE)</text>

          <text x="0" y="80" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Tax / PPN 11% Included</text>
          <text x="478" y="80" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" text-anchor="end">Rp 235.856</text>

          <line x1="0" y1="105" x2="478" y2="105" stroke="#27272a"/>

          <text x="0" y="140" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="16" font-weight="700">TOTAL AMOUNT</text>
          <text x="478" y="140" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="22" font-weight="800" text-anchor="end">Rp 2.380.000</text>

          <!-- Checkout Action -->
          <rect x="0" y="165" width="478" height="52" rx="4" fill="#ffffff"/>
          <text x="239" y="198" fill="#09090b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="800" letter-spacing="1" text-anchor="middle">PROCEED TO SECURE CHECKOUT</text>
        </g>
      </g>
    </g>
  </g>"""

    svg_04 = build_ecommerce_svg(
        url="https://store.mayastranawaloka.com/cart",
        active_cat="ALL OBJECTS",
        bag_count=3,
        content_svg=content_04
    )
    with open("assets/projects/ecommerce/04-slide-cart-ledger.svg", "w", encoding="utf-8") as f:
        f.write(svg_04)

    # -------------------------------------------------------------
    # Screen 05: Streamlined One-Page Checkout
    # -------------------------------------------------------------
    content_05 = """  <!-- One-Page Checkout Layout -->
  <g transform="translate(80, 150)">
    <!-- Left Column: Shipping Address & Details -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="880" height="780" rx="6" fill="#121216" stroke="#27272a" stroke-width="1"/>
      <g transform="translate(40, 40)">
        <text x="0" y="20" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" letter-spacing="1">STEP 01 OF 02</text>
        <text x="0" y="55" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="24" font-weight="700">Shipping &amp; Delivery Details</text>

        <!-- Email & Phone -->
        <text x="0" y="105" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">EMAIL ADDRESS FOR ORDER TRACKING</text>
        <rect x="0" y="120" width="800" height="42" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
        <text x="16" y="146" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">arief.wicaksono@enterprise.id</text>

        <!-- Name Inputs -->
        <g transform="translate(0, 185)">
          <text x="0" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">FIRST NAME</text>
          <rect x="0" y="12" width="385" height="42" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <text x="16" y="38" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Arief</text>

          <text x="415" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">LAST NAME</text>
          <rect x="415" y="12" width="385" height="42" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <text x="431" y="38" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Wicaksono</text>
        </g>

        <!-- Street Address -->
        <g transform="translate(0, 265)">
          <text x="0" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">STREET ADDRESS &amp; BUILDING</text>
          <rect x="0" y="12" width="800" height="42" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <text x="16" y="38" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Jl. Senopati No. 82, Kebayoran Baru, Jakarta Selatan, DKI Jakarta 12190</text>
        </g>

        <!-- Courier Selector -->
        <g transform="translate(0, 345)">
          <text x="0" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700">SELECT COURIER SERVICE</text>
          
          <rect x="0" y="18" width="800" height="60" rx="4" fill="#ffffff" fill-opacity="0.06" stroke="#ffffff" stroke-width="1"/>
          <circle cx="28" cy="48" r="6" fill="#ffffff"/>
          <text x="50" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">SiCepat Cargo Express (Next Day Delivery)</text>
          <text x="50" y="62" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Estimated arrival: Tomorrow before 14:00 WIB</text>
          <text x="770" y="52" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" text-anchor="end">FREE</text>

          <rect x="0" y="90" width="800" height="60" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <circle cx="28" cy="120" r="6" fill="#27272a"/>
          <text x="50" y="116" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">JNE Trucking Heavy Freight (2-3 Days)</text>
          <text x="50" y="134" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Palletized insured delivery</text>
          <text x="770" y="124" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" text-anchor="end">Rp 45.000</text>
        </g>

        <!-- Continue Button -->
        <rect x="0" y="540" width="800" height="52" rx="4" fill="#ffffff"/>
        <text x="400" y="572" fill="#09090b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="800" letter-spacing="1" text-anchor="middle">CONTINUE TO PAYMENT GATEWAY</text>
      </g>
    </g>

    <!-- Right Column: Order Ledger Preview -->
    <g transform="translate(910, 0)">
      <rect x="0" y="0" width="530" height="780" rx="6" fill="#121216" stroke="#27272a" stroke-width="1"/>
      <g transform="translate(36, 40)">
        <text x="0" y="20" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="16" font-weight="700">ORDER SUMMARY (3 ITEMS)</text>
        
        <g transform="translate(0, 50)">
          <text x="0" y="24" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Matte Ceramic Carafe x 1</text>
          <text x="458" y="24" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" text-anchor="end">Rp 480.000</text>

          <text x="0" y="60" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Linear Anodized Tray x 2</text>
          <text x="458" y="60" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" text-anchor="end">Rp 650.000</text>

          <text x="0" y="96" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Cast Iron Desk Lamp x 1</text>
          <text x="458" y="96" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" text-anchor="end">Rp 1.250.000</text>
        </g>
        <line x1="0" y1="180" x2="458" y2="180" stroke="#27272a"/>

        <text x="0" y="220" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="16" font-weight="700">TOTAL DUE</text>
        <text x="458" y="220" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="20" font-weight="800" text-anchor="end">Rp 2.380.000</text>
      </g>
    </g>
  </g>"""

    svg_05 = build_ecommerce_svg(
        url="https://store.mayastranawaloka.com/checkout/step-1",
        active_cat="ALL OBJECTS",
        bag_count=3,
        content_svg=content_05
    )
    with open("assets/projects/ecommerce/05-streamlined-checkout.svg", "w", encoding="utf-8") as f:
        f.write(svg_05)

    # -------------------------------------------------------------
    # Screen 06: Payment Gateway Hub
    # -------------------------------------------------------------
    content_06 = """  <!-- Payment Gateway Layout -->
  <g transform="translate(80, 150)">
    <!-- Center Terminal Card -->
    <rect x="220" y="0" width="1000" height="780" rx="8" fill="#121216" stroke="#27272a" stroke-width="1"/>
    
    <g transform="translate(280, 40)">
      <text x="440" y="24" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="22" font-weight="700" text-anchor="middle">PAYMENT GATEWAY</text>
      <text x="440" y="48" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="middle">ORDER #KRN-88201 &#8226; TOTAL Rp 2.380.000</text>

      <!-- Countdown timer -->
      <rect x="270" y="70" width="340" height="34" rx="17" fill="#18181b" stroke="#27272a" stroke-width="1"/>
      <text x="440" y="92" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600" text-anchor="middle">RESERVATION EXPIRES IN 14:52</text>

      <!-- Dynamic QRIS Block -->
      <g transform="translate(260, 130)">
        <rect x="0" y="0" width="360" height="360" rx="6" fill="#ffffff"/>
        
        <!-- Synthetic QRIS matrix pattern -->
        <rect x="24" y="24" width="70" height="70" fill="#09090b"/>
        <rect x="36" y="36" width="46" height="46" fill="#ffffff"/>
        <rect x="46" y="46" width="26" height="26" fill="#09090b"/>

        <rect x="266" y="24" width="70" height="70" fill="#09090b"/>
        <rect x="278" y="36" width="46" height="46" fill="#ffffff"/>
        <rect x="288" y="46" width="26" height="26" fill="#09090b"/>

        <rect x="24" y="266" width="70" height="70" fill="#09090b"/>
        <rect x="36" y="278" width="46" height="46" fill="#ffffff"/>
        <rect x="46" y="288" width="26" height="26" fill="#09090b"/>

        <!-- QR dense grid dots -->
        <g fill="#09090b">
          <rect x="120" y="40" width="20" height="20"/>
          <rect x="160" y="40" width="40" height="20"/>
          <rect x="220" y="40" width="20" height="20"/>
          <rect x="120" y="80" width="60" height="20"/>
          <rect x="200" y="80" width="40" height="20"/>
          
          <rect x="40" y="120" width="280" height="20"/>
          <rect x="60" y="160" width="80" height="40"/>
          <rect x="160" y="160" width="80" height="40"/>
          <rect x="260" y="160" width="60" height="40"/>
          
          <rect x="40" y="220" width="40" height="30"/>
          <rect x="120" y="220" width="80" height="30"/>
          <rect x="220" y="220" width="100" height="30"/>
        </g>
        <text x="180" y="335" fill="#09090b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="800" text-anchor="middle" letter-spacing="2">QRIS STANDAR NASIONAL</text>
      </g>

      <!-- Multi-Bank Virtual Accounts -->
      <g transform="translate(60, 520)">
        <rect x="0" y="0" width="760" height="150" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
        <text x="24" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">TRANSFER VIRTUAL ACCOUNT ALTERNATIVE</text>
        
        <text x="24" y="65" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">BCA Virtual Account: <tspan fill="#ffffff" font-weight="700">8902 1290 8820 1991</tspan></text>
        <text x="24" y="95" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Mandiri Bill Payment: <tspan fill="#ffffff" font-weight="700">7001 4410 8820 1991</tspan></text>
        <text x="24" y="125" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">BNI / BRI Virtual Account: <tspan fill="#ffffff" font-weight="700">9881 0022 8820 1991</tspan></text>
      </g>
    </g>
  </g>"""

    svg_06 = build_ecommerce_svg(
        url="https://store.mayastranawaloka.com/checkout/payment",
        active_cat="ALL OBJECTS",
        bag_count=3,
        content_svg=content_06
    )
    with open("assets/projects/ecommerce/06-payment-gateway.svg", "w", encoding="utf-8") as f:
        f.write(svg_06)

    # -------------------------------------------------------------
    # Screen 07: Real-Time Order Tracking & Milestones
    # -------------------------------------------------------------
    content_07 = """  <!-- Order Milestone Tracker -->
  <g transform="translate(80, 150)">
    <rect x="0" y="0" width="1440" height="780" rx="6" fill="#121216" stroke="#27272a" stroke-width="1"/>
    
    <g transform="translate(48, 40)">
      <text x="0" y="24" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="22" font-weight="700">ORDER TRACKING #KRN-88201</text>
      <text x="0" y="50" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Carrier: SiCepat Cargo Express &#8226; Waybill: 0041-9982-1092-JKT</text>

      <!-- Milestone Timeline Progress Bar -->
      <g transform="translate(0, 90)">
        <rect x="0" y="20" width="1344" height="6" rx="3" fill="#1f1f23"/>
        <rect x="0" y="20" width="1000" height="6" rx="3" fill="#ffffff"/>

        <!-- Milestone 1 -->
        <circle cx="0" cy="23" r="10" fill="#ffffff"/>
        <text x="0" y="55" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Order Placed</text>
        <text x="0" y="74" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">14 Nov 08:30 WIB</text>

        <!-- Milestone 2 -->
        <circle cx="336" cy="23" r="10" fill="#ffffff"/>
        <text x="336" y="55" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Payment Verified</text>
        <text x="336" y="74" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">14 Nov 08:32 WIB</text>

        <!-- Milestone 3 -->
        <circle cx="672" cy="23" r="10" fill="#ffffff"/>
        <text x="672" y="55" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Staged &amp; Packed</text>
        <text x="672" y="74" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">14 Nov 11:15 WIB</text>

        <!-- Milestone 4 (Active) -->
        <circle cx="1008" cy="23" r="12" fill="#ffffff" stroke="#000000" stroke-width="3"/>
        <text x="1008" y="55" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700">Out for Delivery</text>
        <text x="1008" y="74" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Courier En Route (South JKT)</text>

        <!-- Milestone 5 -->
        <circle cx="1344" cy="23" r="10" fill="#1f1f23"/>
        <text x="1344" y="55" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="end">Delivered</text>
        <text x="1344" y="74" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="end">Est. Today 15:00</text>
      </g>

      <!-- Live GPS Dispatch Log -->
      <g transform="translate(0, 220)">
        <rect x="0" y="0" width="1344" height="420" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
        <text x="32" y="36" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="700">REAL-TIME COURIER TELEMETRY DISPATCHES</text>

        <g transform="translate(32, 60)">
          <line x1="0" y1="20" x2="1280" y2="20" stroke="#27272a"/>
          <text x="0" y="46" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">14 Nov 13:42 WIB</text>
          <text x="180" y="46" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Courier [Hendra] is 1.8 km from destination address (Jl. Senopati, Kebayoran Baru)</text>

          <line x1="0" y1="70" x2="1280" y2="70" stroke="#27272a"/>
          <text x="0" y="96" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">14 Nov 12:10 WIB</text>
          <text x="180" y="96" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Package departed South Jakarta Delivery Station (Duren Tiga Hub)</text>

          <line x1="0" y1="120" x2="1280" y2="120" stroke="#27272a"/>
          <text x="0" y="146" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">14 Nov 10:20 WIB</text>
          <text x="180" y="146" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Consignment scanned at Central Sorting Facility (Halim Logistics Hub)</text>
        </g>
      </g>
    </g>
  </g>"""

    svg_07 = build_ecommerce_svg(
        url="https://store.mayastranawaloka.com/orders/track/KRN-88201",
        active_cat="ALL OBJECTS",
        bag_count=3,
        content_svg=content_07
    )
    with open("assets/projects/ecommerce/07-order-tracking.svg", "w", encoding="utf-8") as f:
        f.write(svg_07)

    # -------------------------------------------------------------
    # Screen 08: Merchant Dashboard
    # -------------------------------------------------------------
    content_08 = """  <!-- Merchant Analytics Dashboard -->
  <g transform="translate(80, 150)">
    <rect x="0" y="0" width="1440" height="780" rx="6" fill="#121216" stroke="#27272a" stroke-width="1"/>
    
    <g transform="translate(40, 40)">
      <text x="0" y="24" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="22" font-weight="700">MERCHANT INTELLIGENCE &amp; CONVERSION FUNNEL</text>
      <text x="0" y="48" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Real-time revenue telemetry, conversion cohorts, and average order value metrics</text>

      <!-- 4 Top Cards -->
      <g transform="translate(0, 80)">
        <rect x="0" y="0" width="320" height="110" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
        <text x="24" y="32" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">DAILY GMV</text>
        <text x="24" y="68" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="24" font-weight="800">Rp 48.250.000</text>
        <text x="24" y="92" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">+24.2% vs yesterday</text>

        <rect x="345" y="0" width="320" height="110" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
        <text x="369" y="32" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">CONVERSION RATE</text>
        <text x="369" y="68" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="24" font-weight="800">4.82 %</text>
        <text x="369" y="92" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Benchmark: 2.1%</text>

        <rect x="690" y="0" width="320" height="110" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
        <text x="714" y="32" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">AVG ORDER VALUE (AOV)</text>
        <text x="714" y="68" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="24" font-weight="800">Rp 820.000</text>
        <text x="714" y="92" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Bundling engine active</text>

        <rect x="1035" y="0" width="325" height="110" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
        <text x="1059" y="32" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">CHECKOUT SPEED</text>
        <text x="1059" y="68" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="24" font-weight="800">84 ms TTFB</text>
        <text x="1059" y="92" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Sub-second transaction commit</text>
      </g>

      <!-- Funnel Chart -->
      <g transform="translate(0, 220)">
        <rect x="0" y="0" width="1360" height="460" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
        <text x="32" y="36" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="700">CONVERSION FUNNEL DROP-OFF AUDIT</text>

        <!-- Funnel bars -->
        <g transform="translate(32, 70)">
          <text x="0" y="24" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">1. Storefront Visits: 142,000 Sessions</text>
          <rect x="0" y="36" width="1290" height="30" rx="4" fill="#ffffff"/>

          <text x="0" y="104" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">2. Product Detail Views: 64,800 Users (45.6%)</text>
          <rect x="0" y="116" width="588" height="30" rx="4" fill="#ffffff" fill-opacity="0.8"/>

          <text x="0" y="184" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">3. Added to Shopping Bag: 14,200 Carts (21.9%)</text>
          <rect x="0" y="196" width="282" height="30" rx="4" fill="#ffffff" fill-opacity="0.6"/>

          <text x="0" y="264" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">4. Completed Payment: 6,840 Transactions (48.1% of checkout)</text>
          <rect x="0" y="276" width="136" height="30" rx="4" fill="#ffffff" fill-opacity="0.4"/>
        </g>
      </g>
    </g>
  </g>"""

    svg_08 = build_ecommerce_svg(
        url="https://store.mayastranawaloka.com/admin/analytics",
        active_cat="EDITORIAL",
        bag_count=3,
        content_svg=content_08
    )
    with open("assets/projects/ecommerce/08-merchant-dashboard.svg", "w", encoding="utf-8") as f:
        f.write(svg_08)

    # -------------------------------------------------------------
    # Screen 09: Omnichannel Inventory Sync
    # -------------------------------------------------------------
    content_09 = """  <!-- Omnichannel Inventory Sync Matrix -->
  <g transform="translate(80, 150)">
    <rect x="0" y="0" width="1440" height="780" rx="6" fill="#121216" stroke="#27272a" stroke-width="1"/>
    
    <g transform="translate(40, 40)">
      <text x="0" y="24" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="22" font-weight="700">OMNICHANNEL INVENTORY BALANCING MATRIX</text>
      <text x="0" y="48" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Atomic stock reservation across Direct Web, Tokopedia, Shopee, and TikTok Shop</text>

      <!-- Channel status pills -->
      <g transform="translate(0, 80)">
        <rect x="0" y="0" width="320" height="80" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
        <text x="20" y="30" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">KRONIK STOREFRONT (WEB)</text>
        <text x="20" y="55" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Priority Allocation: 60% &#8226; 0 ms Latency</text>

        <rect x="345" y="0" width="320" height="80" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
        <text x="365" y="30" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">TOKOPEDIA OFFICIAL</text>
        <text x="365" y="55" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Allocation: 20% &#8226; Webhook Synced</text>

        <rect x="690" y="0" width="320" height="80" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
        <text x="710" y="30" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">SHOPEE MALL</text>
        <text x="710" y="55" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Allocation: 15% &#8226; Webhook Synced</text>

        <rect x="1035" y="0" width="325" height="80" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
        <text x="1055" y="30" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">TIKTOK SHOP</text>
        <text x="1055" y="55" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Allocation: 5% &#8226; Live Stock Lock</text>
      </g>

      <!-- Inventory Table -->
      <g transform="translate(0, 190)">
        <rect x="0" y="0" width="1360" height="490" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
        
        <g transform="translate(32, 40)">
          <text x="0" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">PRODUCT TITLE</text>
          <text x="360" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">STORE STOCK</text>
          <text x="560" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">MARKETPLACE</text>
          <text x="780" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">RESERVED (IN CART)</text>
          <text x="1040" y="0" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">STATUS</text>

          <line x1="0" y1="20" x2="1290" y2="20" stroke="#27272a"/>
          <text x="0" y="50" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">Matte Ceramic Carafe</text>
          <text x="360" y="50" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">240 units</text>
          <text x="560" y="50" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">160 units</text>
          <text x="780" y="50" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">18 units (Locked)</text>
          <text x="1040" y="50" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700">100% IN SYNC</text>

          <line x1="0" y1="75" x2="1290" y2="75" stroke="#27272a"/>
          <text x="0" y="105" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">Linear Anodized Tray</text>
          <text x="360" y="105" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">180 units</text>
          <text x="560" y="105" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">120 units</text>
          <text x="780" y="105" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">12 units (Locked)</text>
          <text x="1040" y="105" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700">100% IN SYNC</text>
        </g>
      </g>
    </g>
  </g>"""

    svg_09 = build_ecommerce_svg(
        url="https://store.mayastranawaloka.com/admin/inventory-matrix",
        active_cat="HARDWARE",
        bag_count=3,
        content_svg=content_09
    )
    with open("assets/projects/ecommerce/09-inventory-sync.svg", "w", encoding="utf-8") as f:
        f.write(svg_09)

    # -------------------------------------------------------------
    # Screen 10: Customer Loyalty & Retention Engine
    # -------------------------------------------------------------
    content_10 = """  <!-- Customer Loyalty Engine Layout -->
  <g transform="translate(80, 150)">
    <rect x="0" y="0" width="1440" height="780" rx="6" fill="#121216" stroke="#27272a" stroke-width="1"/>
    
    <g transform="translate(40, 40)">
      <text x="0" y="24" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="22" font-weight="700">KRONIK MEMBER PRIVILEGE CLUB</text>
      <text x="0" y="48" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Tiered rewards, point balance redemption, and private studio drop access</text>

      <!-- Member Tier Card -->
      <g transform="translate(0, 80)">
        <rect x="0" y="0" width="600" height="280" rx="8" fill="#18181f" stroke="#ffffff" stroke-width="1.5"/>
        <text x="36" y="50" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" letter-spacing="2" font-weight="700">TIER 03 // VIP PRIVILEGE</text>
        <text x="36" y="90" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="32" font-weight="800">OBSIDIAN BLACK TIER</text>
        
        <text x="36" y="140" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">AVAILABLE REWARD POINTS</text>
        <text x="36" y="175" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="26" font-weight="700">4,250 PTS</text>
        <text x="36" y="200" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Equivalent to Rp 425.000 in checkout redemption</text>

        <!-- Progress to next tier -->
        <rect x="36" y="235" width="528" height="6" rx="3" fill="#27272a"/>
        <rect x="36" y="235" width="450" height="6" rx="3" fill="#ffffff"/>
      </g>

      <!-- Member Privileges List -->
      <g transform="translate(640, 80)">
        <rect x="0" y="0" width="720" height="280" rx="8" fill="#18181b" stroke="#27272a" stroke-width="1"/>
        <text x="36" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="16" font-weight="700">TIER BENEFITS ACTIVE</text>
        
        <g transform="translate(36, 65)">
          <text x="0" y="25" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">&#10003; 10% Flat Member Voucher on All Studio Drops</text>
          <text x="0" y="60" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">&#10003; Free Same-Day Courier Delivery (No Minimum Purchase)</text>
          <text x="0" y="95" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">&#10003; 24-Hour Early Access to Limited Edition Hardware Drops</text>
          <text x="0" y="130" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">&#10003; Dedicated Private Concierge Support</text>
        </g>
      </g>
    </g>
  </g>"""

    svg_10 = build_ecommerce_svg(
        url="https://store.mayastranawaloka.com/account/loyalty-rewards",
        active_cat="ALL OBJECTS",
        bag_count=3,
        content_svg=content_10
    )
    with open("assets/projects/ecommerce/10-customer-loyalty.svg", "w", encoding="utf-8") as f:
        f.write(svg_10)

    # -------------------------------------------------------------
    # Screen 11: Automated Promotions & Flash-Sale Rules Matrix
    # -------------------------------------------------------------
    content_11 = """  <!-- Promotions Matrix Content -->
  <g transform="translate(80, 150)">
    <text x="0" y="24" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="20" font-weight="700">PROMOTIONS &amp; FLASH-SALE RULES ENGINE</text>
    <text x="0" y="48" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Automated discount matrix, bundle logic, coupon thresholds, and margin protections</text>

    <!-- Top 4 Metrics -->
    <g transform="translate(0, 70)">
      <rect x="0" y="0" width="340" height="96" rx="6" fill="#141418" stroke="#27272a" stroke-width="1"/>
      <text x="24" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">ACTIVE CAMPAIGNS</text>
      <text x="24" y="66" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="800">4 Running</text>
      <text x="220" y="66" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">0 Expired</text>

      <rect x="366" y="0" width="340" height="96" rx="6" fill="#141418" stroke="#27272a" stroke-width="1"/>
      <text x="390" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">AVG BASKET UPLIFT</text>
      <text x="390" y="66" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="800">+32.4%</text>
      <text x="560" y="66" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Tiered Bundles</text>

      <rect x="732" y="0" width="340" height="96" rx="6" fill="#141418" stroke="#27272a" stroke-width="1"/>
      <text x="756" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">COUPON REDEMPTION</text>
      <text x="756" y="66" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="800">18.6%</text>
      <text x="910" y="66" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">1 User Limit</text>

      <rect x="1098" y="0" width="342" height="96" rx="6" fill="#141418" stroke="#27272a" stroke-width="1"/>
      <text x="1122" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">MARGIN PROTECTION</text>
      <text x="1122" y="66" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="800">28.5% Min</text>
      <text x="1300" y="66" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Guaranteed</text>
    </g>

    <!-- Rules Table -->
    <g transform="translate(0, 190)">
      <rect x="0" y="0" width="1440" height="520" rx="8" fill="#121216" stroke="#27272a" stroke-width="1"/>
      <rect x="0" y="0" width="1440" height="44" fill="#18181c" rx="8"/>
      <text x="24" y="27" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700">PROMO TITLE &amp; CODE</text>
      <text x="360" y="27" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700">DISCOUNT LOGIC</text>
      <text x="600" y="27" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700">MINIMUM SPEND</text>
      <text x="800" y="27" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700">REDEMPTIONS</text>
      <text x="1000" y="27" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700">CAMPAIGN WINDOW</text>
      <text x="1200" y="27" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700">STATUS</text>
      <text x="1340" y="27" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700">ACTIONS</text>

      <!-- Row 1 -->
      <g transform="translate(0, 44)">
        <text x="24" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">Studio Opening Drop - CODE: MONO15</text>
        <text x="24" y="52" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Applies to All Studio Instruments &amp; Desk Objects</text>
        <text x="360" y="42" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">15% Instant Cart Discount</text>
        <text x="600" y="42" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Rp 1.000.000</text>
        <text x="800" y="42" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">420 / 500 Used</text>
        <text x="1000" y="42" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Nov 10 - Nov 20, 2026</text>
        <rect x="1200" y="26" width="90" height="24" rx="4" fill="#ffffff" fill-opacity="0.12"/>
        <text x="1245" y="42" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Active</text>
        <text x="1340" y="42" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Edit</text>
        <line x1="24" y1="74" x2="1416" y2="74" stroke="#1f1f23"/>
      </g>

      <!-- Row 2 -->
      <g transform="translate(0, 118)">
        <text x="24" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">Hardware Bundle Set - AUTO APPLIED</text>
        <text x="24" y="52" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Buy Desk Lamp + Aluminum Tray together</text>
        <text x="360" y="42" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Rp 250.000 Bundle Rebate</text>
        <text x="600" y="42" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Bundle Match</text>
        <text x="800" y="42" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">184 Bundles</text>
        <text x="1000" y="42" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Permanent Promotion</text>
        <rect x="1200" y="26" width="90" height="24" rx="4" fill="#ffffff" fill-opacity="0.12"/>
        <text x="1245" y="42" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Active</text>
        <text x="1340" y="42" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Edit</text>
        <line x1="24" y1="74" x2="1416" y2="74" stroke="#1f1f23"/>
      </g>

      <!-- Row 3 -->
      <g transform="translate(0, 192)">
        <text x="24" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">VIP Founding Tier Free Logistics</text>
        <text x="24" y="52" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Automated 100% courier shipping absorption</text>
        <text x="360" y="42" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Free Insured Courier</text>
        <text x="600" y="42" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">No Minimum</text>
        <text x="800" y="42" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">892 Shipments</text>
        <text x="1000" y="42" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Indefinite (VIP)</text>
        <rect x="1200" y="26" width="90" height="24" rx="4" fill="#ffffff" fill-opacity="0.12"/>
        <text x="1245" y="42" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Active</text>
        <text x="1340" y="42" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Edit</text>
      </g>
    </g>
  </g>"""

    svg_11 = build_ecommerce_svg(
        url="https://store.mayastranawaloka.com/admin/promotions-matrix",
        active_cat="ALL OBJECTS",
        bag_count=3,
        content_svg=content_11
    )
    with open("assets/projects/ecommerce/11-promotions-engine.svg", "w", encoding="utf-8") as f:
        f.write(svg_11)

    print("[*] Generated all 11 E-Commerce SVGs successfully.")

if __name__ == "__main__":
    generate_all_ecommerce()
