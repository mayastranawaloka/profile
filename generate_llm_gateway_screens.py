import os
import xml.etree.ElementTree as ET

# Helper to render standard monochrome browser header
def get_browser_header(url):
    return f"""  <!-- Browser Header Bar -->
  <rect width="1600" height="52" fill="#111113" stroke="#27272a" stroke-width="1"/>
  <circle cx="36" cy="26" r="6" fill="#27272a"/>
  <circle cx="56" cy="26" r="6" fill="#27272a"/>
  <circle cx="76" cy="26" r="6" fill="#27272a"/>
  <rect x="520" y="14" width="560" height="24" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
  <text x="800" y="30" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle" letter-spacing="1">{url}</text>"""

# Helper to render standard monochrome sidebar
def get_sidebar(active_name):
    items = [
        ("Gateway Telemetry", 0),
        ("Key Vault &amp; RBAC", 46),
        ("Model Router", 92),
        ("Prompt Eval Harness", 138),
        ("Semantic Cache", 184),
        ("Security &amp; Firewall", 230),
        ("Audit Logs", 276),
    ]
    menu_svg = ""
    for name, offset in items:
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
  <!-- Brand in Gateway -->
  <rect x="28" y="80" width="24" height="24" rx="4" fill="#ffffff"/>
  <text x="64" y="97" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="700" letter-spacing="1.5">AI GATEWAY</text>

  <!-- Nav items -->
  <g transform="translate(24, 140)">
{menu_svg}  </g>

  <!-- Cluster status at bottom sidebar -->
  <rect x="24" y="930" width="212" height="42" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
  <circle cx="48" cy="951" r="5" fill="#ffffff"/>
  <text x="64" y="948" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Enterprise Vault #01</text>
  <text x="64" y="961" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">HSM Encrypted / FIPS-140</text>"""

# Helper to render monochrome top bar
def get_top_bar(title, subtitle, btn1_label="Export Traces", btn2_label="Deploy Key"):
    safe_title = title.replace("&amp;", "&").replace("&", "&amp;")
    safe_subtitle = subtitle.replace("&amp;", "&").replace("&", "&amp;")
    return f"""  <!-- Top bar inside main content -->
  <g transform="translate(290, 80)">
    <text x="0" y="26" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="24" font-weight="600" letter-spacing="-0.5">{safe_title}</text>
    <text x="0" y="48" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">{safe_subtitle}</text>

    <!-- Action buttons -->
    <rect x="1070" y="8" width="110" height="34" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
    <text x="1125" y="30" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">{btn1_label}</text>

    <rect x="1190" y="8" width="90" height="34" rx="4" fill="#ffffff"/>
    <text x="1235" y="30" fill="#09090b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="middle">{btn2_label}</text>
  </g>"""

# Wrap SVG with pure monochrome styling
def wrap_svg(inner_content, active_name, title, subtitle, url="https://gateway.internal.mayastranawaloka.com/telemetry"):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 1000" width="1600" height="1000">
  <defs>
    <linearGradient id="bgGlow" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#09090b"/>
      <stop offset="100%" stop-color="#121215"/>
    </linearGradient>
    <linearGradient id="monoGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0.0"/>
    </linearGradient>
  </defs>

  <rect width="1600" height="1000" fill="url(#bgGlow)"/>

{get_browser_header(url)}
{get_sidebar(active_name)}
{get_top_bar(title, subtitle)}

  <!-- Main Content Body -->
  <g transform="translate(290, 150)">
{inner_content}
  </g>
</svg>"""

# Helper to build 4 KPI cards in monochrome
def build_kpi_cards(c1, c2, c3, c4):
    cards = [c1, c2, c3, c4]
    svg = "    <!-- 4 KPI Cards -->\n    <g transform=\"translate(0, 0)\">\n"
    for i, c in enumerate(cards):
        x = i * 325
        safe_label = c['label'].replace("&amp;", "&").replace("&", "&amp;")
        safe_val = c['val'].replace("&amp;", "&").replace("&", "&amp;")
        safe_badge = c['badge'].replace("&amp;", "&").replace("&", "&amp;")
        safe_sub = c['sub'].replace("&amp;", "&").replace("&", "&amp;")
        svg += f"""      <rect x="{x}" y="0" width="300" height="96" rx="6" fill="#121215" stroke="#27272a" stroke-width="1"/>
      <text x="{x+20}" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="500">{safe_label}</text>
      <text x="{x+20}" y="64" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="700">{safe_val}</text>
      <text x="{x+180}" y="64" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">{safe_badge}</text>
      <text x="{x+20}" y="82" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">{safe_sub}</text>\n"""
    svg += "    </g>\n"
    return svg

# Helper to build split layout with left table and right inspector
def build_split_layout(table_title, table_sub, table_headers, table_rows, right_box_title, right_box_content):
    safe_table_title = table_title.replace("&amp;", "&").replace("&", "&amp;")
    safe_table_sub = table_sub.replace("&amp;", "&").replace("&", "&amp;")
    safe_right_box_title = right_box_title.replace("&amp;", "&").replace("&", "&amp;")

    headers_svg = ""
    for idx, (h, x) in enumerate(zip(table_headers, [24, 210, 390, 520, 640, 720])):
        safe_h = h.replace("&amp;", "&").replace("&", "&amp;")
        headers_svg += f'        <text x="{x}" y="98" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">{safe_h}</text>\n'

    rows_svg = ""
    for r_idx, row in enumerate(table_rows):
        y = 132 + (r_idx * 54)
        bg = "#18181b" if r_idx % 2 == 1 else "#121215"
        badge_bg = "#27272a" if row['status'] in ["ACTIVE", "HEALTHY", "OPTIMAL", "PASSED", "VERIFIED", "CACHED", "MOUNTED", "COMPLETED", "NORMAL"] else "#1f1f23"
        badge_color = "#ffffff" if row['status'] in ["ACTIVE", "HEALTHY", "OPTIMAL", "PASSED", "VERIFIED", "CACHED", "MOUNTED", "COMPLETED", "NORMAL"] else "#a1a1aa"

        safe_c1 = row['c1'].replace("&amp;", "&").replace("&", "&amp;")
        safe_c2 = row['c2'].replace("&amp;", "&").replace("&", "&amp;")
        safe_c3 = row['c3'].replace("&amp;", "&").replace("&", "&amp;")
        safe_c4 = row['c4'].replace("&amp;", "&").replace("&", "&amp;")
        safe_c5 = row['c5'].replace("&amp;", "&").replace("&", "&amp;")

        rows_svg += f"""      <!-- Row {r_idx+1} -->
      <rect x="12" y="{y-18}" width="796" height="46" rx="4" fill="{bg}"/>
      <text x="24" y="{y+10}" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">{safe_c1}</text>
      <text x="210" y="{y+10}" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">{safe_c2}</text>
      <text x="390" y="{y+10}" fill="#ffffff" font-family="monospace" font-size="12">{safe_c3}</text>
      <text x="520" y="{y+10}" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">{safe_c4}</text>
      <text x="640" y="{y+10}" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">{safe_c5}</text>
      <rect x="716" y="{y-6}" width="76" height="22" rx="3" fill="{badge_bg}" stroke="#3f3f46" stroke-width="1"/>
      <text x="754" y="{y+9}" fill="{badge_color}" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="600" text-anchor="middle">{row['status']}</text>\n"""

    return f"""    <!-- Main Split Panels -->
    <g transform="translate(0, 114)">
      <!-- Left Panel: High Density Table -->
      <rect width="820" height="666" rx="6" fill="#121215" stroke="#27272a" stroke-width="1"/>
      <text x="24" y="38" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="16" font-weight="600">{safe_table_title}</text>
      <text x="24" y="58" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">{safe_table_sub}</text>

      <!-- Search / Filter Pill -->
      <rect x="580" y="24" width="216" height="30" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
      <text x="596" y="44" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Filter records...</text>

      <!-- Table Separator -->
      <line x1="24" y1="78" x2="796" y2="78" stroke="#27272a" stroke-width="1"/>

      <!-- Table Headers -->
{headers_svg}
      <line x1="24" y1="108" x2="796" y2="108" stroke="#1f1f23" stroke-width="1"/>

      <!-- Rows -->
{rows_svg}
      <!-- Table Pagination / Status Footer -->
      <line x1="24" y1="620" x2="796" y2="620" stroke="#27272a" stroke-width="1"/>
      <text x="24" y="646" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Showing 1 to 5 of active records</text>
      <rect x="710" y="632" width="86" height="24" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
      <text x="753" y="648" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" text-anchor="middle">Page 1 / 1</text>

      <!-- Right Panel: Telemetry / Inspector Drawer -->
      <g transform="translate(840, 0)">
        <rect width="440" height="666" rx="6" fill="#121215" stroke="#27272a" stroke-width="1"/>
        <text x="24" y="38" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="16" font-weight="600">{safe_right_box_title}</text>
        <line x1="24" y1="58" x2="416" y2="58" stroke="#27272a" stroke-width="1"/>
{right_box_content}
      </g>
    </g>"""

# Define all 11 screens with deep UI/UX features
screens = {
    "01-gateway-telemetry.svg": {
        "title": "Multi-Model Telemetry & Token Throughput",
        "subtitle": "Real-time dispatch latency, token burn rate, and cross-provider failover",
        "active": "Gateway Telemetry",
        "url": "https://gateway.internal.mayastranawaloka.com/telemetry",
        "kpi": [
            {"label": "ACTIVE MODEL CLUSTERS", "val": "12 / 12", "badge": "100% HEALTH", "sub": "Zero Downtime SLA Guaranteed"},
            {"label": "GLOBAL THROUGHPUT", "val": "14,820", "badge": "REQ / SEC", "sub": "p99 Latency 38ms Global Mean"},
            {"label": "SEMANTIC CACHE RATIO", "val": "42.4%", "badge": "+42% SAVED", "sub": "Sub-millisecond Vector Match"},
            {"label": "AGGREGATE TOKEN VELOCITY", "val": "1.42M", "badge": "TOKENS / MIN", "sub": "Blended Yield $0.0018 / 1k"},
        ],
        "table_title": "Active Foundation Model Pools & Health Matrix",
        "table_sub": "Live inference routing, token yield, and latency benchmarks across 12 clusters",
        "headers": ["CLUSTER POOL", "BASE ARCHITECTURE", "p99 LATENCY", "TOKEN YIELD", "ERROR RATE", "STATUS"],
        "rows": [
            {"c1": "Deep Reasoning Pool", "c2": "32B Speculative Cluster", "c3": "42 ms", "c4": "480k / min", "c5": "0.00%", "status": "HEALTHY"},
            {"c2": "70B Dense Pool", "c1": "High-Throughput Pool", "c3": "28 ms", "c4": "620k / min", "c5": "0.01%", "status": "HEALTHY"},
            {"c1": "Code Synthesis Pool", "c2": "34B Instruct Weights", "c3": "34 ms", "c4": "190k / min", "c5": "0.00%", "status": "HEALTHY"},
            {"c1": "Semantic Vector Pool", "c2": "1536D Dense Embedding", "c3": "8 ms", "c4": "130k / min", "c5": "0.00%", "status": "OPTIMAL"},
            {"c1": "Edge Low-Latency Pool", "c2": "8B Quantized Weights", "c3": "12 ms", "c4": "95k / min", "c5": "0.00%", "status": "HEALTHY"},
        ],
        "right_title": "Real-Time Telemetry & Buffer Dynamics",
        "right_content": """        <!-- Telemetry sparkline graph -->
        <rect x="24" y="80" width="392" height="150" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
        <text x="40" y="104" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">INFERENCE VELOCITY CURVE</text>
        <text x="40" y="122" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Window: Last 60 Minutes (req/sec)</text>
        <path d="M 40 200 L 80 185 L 120 190 L 160 170 L 200 178 L 240 160 L 280 165 L 320 145 L 360 150 L 400 135 L 400 215 L 40 215 Z" fill="url(#monoGrad)"/>
        <path d="M 40 200 L 80 185 L 120 190 L 160 170 L 200 178 L 240 160 L 280 165 L 320 145 L 360 150 L 400 135" fill="none" stroke="#ffffff" stroke-width="2"/>

        <!-- Stream status box -->
        <g transform="translate(24, 250)">
          <rect width="392" height="110" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <text x="16" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">DUPLEX STREAMING BUFFER</text>
          <text x="16" y="52" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="20" font-weight="700">1,240 Channels</text>
          <text x="16" y="74" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Zero buffer drop / Backpressure safe</text>
          <rect x="16" y="88" width="360" height="6" rx="3" fill="#27272a"/>
          <rect x="16" y="88" width="280" height="6" rx="3" fill="#ffffff"/>
        </g>

        <!-- Key Vault Security Badge -->
        <g transform="translate(24, 380)">
          <rect width="392" height="120" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <text x="16" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">HSM KEY VAULT ENCLAVE</text>
          <text x="16" y="48" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Hardware Level Security Isolation</text>
          <text x="16" y="74" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">16 Vaults Sealed</text>
          <text x="16" y="94" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">AES-256 Envelope Encryption Active</text>
        </g>

        <!-- Guardrail Status -->
        <g transform="translate(24, 520)">
          <rect width="392" height="120" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <text x="16" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">PII SCRUBBING FIREWALL</text>
          <text x="16" y="48" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Zero-Leakage Real-Time Filter</text>
          <text x="16" y="74" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">0 Secrets Outbound</text>
          <text x="16" y="94" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Automated Masking at Ingestion</text>
        </g>"""
    },
    "02-key-vault-governance.svg": {
        "title": "Hardware Security Module (HSM) Key Vault",
        "subtitle": "FIPS 140-2 Level 3 Hardware Isolation, Envelope Encryption & Key Rotation",
        "active": "Key Vault & RBAC",
        "url": "https://gateway.internal.mayastranawaloka.com/keys",
        "kpi": [
            {"label": "HARDWARE ISOLATED KEYS", "val": "16", "badge": "SEALED", "sub": "Zero Plaintext Exposure to Host OS"},
            {"label": "ENVELOPE ENCRYPTION", "val": "AES-256", "badge": "GCM CIPHER", "sub": "Root Key in Hardware Secure Enclave"},
            {"label": "KEY ROTATION CADENCE", "val": "24h", "badge": "AUTOMATED", "sub": "Zero-Downtime Key Transitioning"},
            {"label": "AUTHORIZED SERVICE TOKENS", "val": "142", "badge": "mTLS ROLES", "sub": "Role-Based Token Boundary Enforced"},
        ],
        "table_title": "Hardware-Backed Key Inventory & Cryptographic Enclaves",
        "table_sub": "Tamper-resistant cryptographic boundaries with zero developer exposure to raw secrets",
        "headers": ["KEY IDENTIFIER", "TARGET POOL", "ENCLAVE ID", "ROTATION CADENCE", "ACCESS SCOPE", "STATUS"],
        "rows": [
            {"c1": "KEY-HSM-9021", "c2": "Deep Reasoning Pool", "c3": "ENCLAVE-ALPHA-01", "c4": "Daily (Next: 04h)", "c5": "Inference:Write", "status": "ACTIVE"},
            {"c1": "KEY-HSM-8842", "c2": "High-Throughput Pool", "c3": "ENCLAVE-ALPHA-02", "c4": "Daily (Next: 11h)", "c5": "Inference:Write", "status": "ACTIVE"},
            {"c1": "KEY-HSM-7719", "c2": "Code Synthesis Pool", "c3": "ENCLAVE-BETA-01", "c4": "Daily (Next: 18h)", "c5": "CodeGen:Write", "status": "ACTIVE"},
            {"c1": "KEY-HSM-6540", "c2": "Vector Embedding Pool", "c3": "ENCLAVE-GAMMA-01", "c4": "Weekly (Next: 3d)", "c5": "Embed:ReadOnly", "status": "ACTIVE"},
            {"c1": "KEY-HSM-5102", "c2": "Backup Failover Pool", "c3": "ENCLAVE-DELTA-01", "c4": "On-Demand", "c5": "Failover:Standby", "status": "OPTIMAL"},
        ],
        "right_title": "Enclave Security Inspector & PCR Validation",
        "right_content": """        <g transform="translate(24, 80)">
          <rect width="392" height="150" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <text x="20" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">HARDWARE ATTESTATION</text>
          <text x="20" y="54" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">PCR0 Measurement Hash (SHA-256):</text>
          <text x="20" y="78" fill="#d4d4d8" font-family="monospace" font-size="10">e3b0c44298fc1c149afbf4c8996fb92427</text>
          <text x="20" y="104" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Integrity Status: VERIFIED</text>
          <text x="20" y="124" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Kernel memory dump protection armed</text>
        </g>

        <g transform="translate(24, 250)">
          <rect width="392" height="170" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <text x="20" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">DECRYPTION PERFORMANCE</text>
          <text x="20" y="60" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="24" font-weight="700">0.12 ms</text>
          <text x="140" y="60" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Hardware Overhead</text>
          <text x="20" y="86" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Peak Decryption Calls: 14,820 req/sec</text>
          <line x1="20" y1="104" x2="372" y2="104" stroke="#27272a" stroke-width="1"/>
          <text x="20" y="126" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Envelope Protocol: AES-256-GCM Ephemeral</text>
          <text x="20" y="146" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Rotated in memory without socket tear-down</text>
        </g>

        <g transform="translate(24, 440)">
          <rect width="392" height="180" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <text x="20" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">EMERGENCY KILLSWITCH</text>
          <text x="20" y="54" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Global API Key Revocation Gateway</text>
          <rect x="20" y="74" width="352" height="38" rx="4" fill="#27272a"/>
          <text x="196" y="98" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600" text-anchor="middle">KILLSWITCH ARMED (STANDBY)</text>
          <text x="20" y="134" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Single-action zeroization revokes all 16 enclaves</text>
          <text x="20" y="154" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Requires quorum approval from 2 executive officers</text>
        </g>"""
    },
    "03-model-router-matrix.svg": {
        "title": "Semantic Multi-Model Dynamic Router",
        "subtitle": "Intent Classification, Latency Optimization & Algorithmic SLA Failover",
        "active": "Model Router",
        "url": "https://gateway.internal.mayastranawaloka.com/router",
        "kpi": [
            {"label": "ACTIVE ROUTING TIERS", "val": "5", "badge": "ENFORCED", "sub": "Zero Conflicting Policy Directives"},
            {"label": "CLASSIFIER OVERHEAD", "val": "1.8ms", "badge": "EMBED MATCH", "sub": "Semantic Intent Embedding Engine"},
            {"label": "COST YIELD SAVINGS", "val": "38.6%", "badge": "+38.6% SAVE", "sub": "Dynamic Context Allocator Enabled"},
            {"label": "SLA FAILOVER READY", "val": "100%", "badge": "SUB-50ms", "sub": "Automatic Secondary Pool Handoff"},
        ],
        "table_title": "Dynamic Routing Matrix & Algorithmic Rules",
        "table_sub": "Analyzes token payload semantics and routes to the optimal price-to-performance cluster",
        "headers": ["RULE ID", "INTENT CLASSIFICATION", "PRIMARY CLUSTER", "FALLBACK ROUTE", "MAX LATENCY", "STATUS"],
        "rows": [
            {"c1": "ROUTE-01", "c2": "Complex Reasoning & Math", "c3": "Deep Reasoning 32B", "c4": "High-Throughput 70B", "c5": "150 ms", "status": "ACTIVE"},
            {"c1": "ROUTE-02", "c2": "Code Synthesis & Debug", "c3": "Code Synthesis 34B", "c4": "Deep Reasoning 32B", "c5": "120 ms", "status": "ACTIVE"},
            {"c1": "ROUTE-03", "c2": "Document Extraction", "c3": "High-Throughput 70B", "c4": "Edge Fast 8B", "c5": "60 ms", "status": "ACTIVE"},
            {"c1": "ROUTE-04", "c2": "Semantic Similarity Search", "c3": "Vector Matrix 1536D", "c4": "Local HNSW Cache", "c5": "15 ms", "status": "ACTIVE"},
            {"c1": "ROUTE-05", "c2": "Fast Interactive Dialogue", "c3": "Edge Fast 8B", "c4": "High-Throughput 70B", "c5": "25 ms", "status": "ACTIVE"},
        ],
        "right_title": "Live Routing Decision Stream",
        "right_content": """        <g transform="translate(24, 80)">
          <rect width="392" height="540" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <text x="20" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">REAL-TIME DISPATCH TRACES</text>
          
          <!-- Trace Item 1 -->
          <g transform="translate(16, 50)">
            <rect width="360" height="74" rx="4" fill="#121215" stroke="#27272a" stroke-width="1"/>
            <text x="14" y="22" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">REQ-0x9942 - Financial Ledger</text>
            <text x="14" y="42" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Matched ROUTE-01 (Confidence 99.2%)</text>
            <text x="14" y="60" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Dispatched: Deep Reasoning 32B in 1.4ms</text>
          </g>

          <!-- Trace Item 2 -->
          <g transform="translate(16, 134)">
            <rect width="360" height="74" rx="4" fill="#121215" stroke="#27272a" stroke-width="1"/>
            <text x="14" y="22" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">REQ-0x9941 - Markdown Table Format</text>
            <text x="14" y="42" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Matched ROUTE-05 (Confidence 98.7%)</text>
            <text x="14" y="60" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Dispatched: Edge Fast 8B in 0.9ms</text>
          </g>

          <!-- Trace Item 3 -->
          <g transform="translate(16, 218)">
            <rect width="360" height="74" rx="4" fill="#121215" stroke="#27272a" stroke-width="1"/>
            <text x="14" y="22" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">REQ-0x9940 - SQL Schema Migration</text>
            <text x="14" y="42" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Matched ROUTE-02 (Confidence 99.5%)</text>
            <text x="14" y="60" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Dispatched: Code Synthesis 34B in 1.2ms</text>
          </g>

          <!-- Trace Item 4 -->
          <g transform="translate(16, 302)">
            <rect width="360" height="74" rx="4" fill="#121215" stroke="#27272a" stroke-width="1"/>
            <text x="14" y="22" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">REQ-0x9939 - Legal Term Extraction</text>
            <text x="14" y="42" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Matched ROUTE-03 (Confidence 97.4%)</text>
            <text x="14" y="60" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Dispatched: High-Throughput 70B in 1.1ms</text>
          </g>

          <text x="20" y="410" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">AVERAGE ROUTING OVERHEAD</text>
          <text x="20" y="434" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="20" font-weight="700">1.15 ms</text>
          <text x="20" y="456" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Fast embedding classification across all 5 tiers</text>
        </g>"""
    },
    "04-prompt-eval-harness.svg": {
        "title": "Prompt Evaluation & Regression Testing Harness",
        "subtitle": "Multi-Judge Benchmark Scoring, Semantic Drift Detection & Automated CI/CD Gates",
        "active": "Prompt Eval Harness",
        "url": "https://gateway.internal.mayastranawaloka.com/eval",
        "kpi": [
            {"label": "BENCHMARK SUITES", "val": "48", "badge": "1,480 TESTS", "sub": "Regression Test Scenarios Automated"},
            {"label": "EVALUATION ACCURACY", "val": "98.4%", "badge": "0.96 SCORE", "sub": "Cross-Judge Agreement Consensus"},
            {"label": "SEMANTIC DRIFT", "val": "0.02%", "badge": "GATE PASSED", "sub": "Strict Drift Threshold &lt; 1.5%"},
            {"label": "EVAL CADENCE", "val": "CI/CD", "badge": "AUTOMATED", "sub": "Zero Production Prompt Regressions"},
        ],
        "table_title": "Prompt Regression Test Runs & Quality Gates",
        "table_sub": "Evaluates prompt iterations against golden test sets using LLM-as-a-judge consensus",
        "headers": ["SUITE NAME", "PROMPT VERSION", "EVAL JUDGE POOL", "ROUGE-L", "FACTUALITY", "RESULT"],
        "rows": [
            {"c1": "Enterprise ERP Parser", "c2": "v3.4.2-prod", "c3": "Dual Specialist Cluster", "c4": "0.942", "c5": "99.8%", "status": "PASSED"},
            {"c1": "Financial Reconciliation", "c2": "v4.1.0-prod", "c3": "Deep Reasoning Cluster", "c4": "0.985", "c5": "100.0%", "status": "PASSED"},
            {"c1": "Customer Support Terminal", "c2": "v2.8.0-prod", "c3": "High-Throughput Pool", "c4": "0.918", "c5": "98.6%", "status": "PASSED"},
            {"c1": "Security Policy Validator", "c2": "v1.9.4-prod", "c3": "Multi-Agent Critic", "c4": "0.962", "c5": "99.4%", "status": "PASSED"},
            {"c1": "Multilingual Translator", "c2": "v2.3.1-prod", "c3": "Specialist Cluster", "c4": "0.925", "c5": "98.9%", "status": "PASSED"},
        ],
        "right_title": "Evaluation Quality Dimension Gauge",
        "right_content": """        <g transform="translate(24, 80)">
          <rect width="392" height="540" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <text x="20" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">QUALITY BENCHMARK SCORES</text>

          <!-- Gauge 1 -->
          <text x="20" y="70" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Factuality &amp; Grounding</text>
          <text x="330" y="70" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">99.4%</text>
          <rect x="20" y="80" width="352" height="8" rx="4" fill="#27272a"/>
          <rect x="20" y="80" width="350" height="8" rx="4" fill="#ffffff"/>

          <!-- Gauge 2 -->
          <text x="20" y="120" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Schema Conformance (JSON/SQL)</text>
          <text x="330" y="120" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">100.0%</text>
          <rect x="20" y="130" width="352" height="8" rx="4" fill="#27272a"/>
          <rect x="20" y="130" width="352" height="8" rx="4" fill="#ffffff"/>

          <!-- Gauge 3 -->
          <text x="20" y="170" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Safety &amp; Guardrail Adherence</text>
          <text x="330" y="170" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">100.0%</text>
          <rect x="20" y="180" width="352" height="8" rx="4" fill="#27272a"/>
          <rect x="20" y="180" width="352" height="8" rx="4" fill="#ffffff"/>

          <!-- Gauge 4 -->
          <text x="20" y="220" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Tone &amp; Stylistic Consistency</text>
          <text x="330" y="220" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">97.8%</text>
          <rect x="20" y="230" width="352" height="8" rx="4" fill="#27272a"/>
          <rect x="20" y="230" width="344" height="8" rx="4" fill="#ffffff"/>

          <!-- CI/CD Deployment Gate -->
          <g transform="translate(20, 270)">
            <rect width="352" height="110" rx="6" fill="#121215" stroke="#27272a" stroke-width="1"/>
            <text x="16" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">CI/CD DEPLOYMENT GATE</text>
            <text x="16" y="52" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="16" font-weight="700">STATUS: APPROVED FOR PROD</text>
            <text x="16" y="74" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Automated gate release: Commit 0x88f2b1</text>
            <text x="16" y="94" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Zero regressions across 1,480 scenarios</text>
          </g>
        </g>"""
    },
    "05-semantic-caching.svg": {
        "title": "Vector Semantic Caching Matrix",
        "subtitle": "Sub-Millisecond Cosine Similarity Lookup, Exact & Fuzzy Match Deduplication",
        "active": "Semantic Cache",
        "url": "https://gateway.internal.mayastranawaloka.com/cache",
        "kpi": [
            {"label": "CACHE HIT RATIO", "val": "42.4%", "badge": "+42.4%", "sub": "14,820 req/s Evaluated Continuously"},
            {"label": "LOOKUP LATENCY", "val": "0.8ms", "badge": "SUB-MILLI", "sub": "HNSW In-Memory Vector Index"},
            {"label": "MONTHLY COST AVOIDED", "val": "$14,280", "badge": "SAVED", "sub": "42% Incurred API Cost Reduction"},
            {"label": "CACHED VECTOR ENTRIES", "val": "480,000", "badge": "HNSW INDEX", "sub": "Cosine Threshold >= 0.92"},
        ],
        "table_title": "Active Vector Cache Registry & Similarity Matches",
        "table_sub": "Bypasses costly foundation model calls when incoming prompt semantics match existing vectors",
        "headers": ["VECTOR HASH", "NORMALIZED PROMPT", "DISTANCE", "TTL REMAINING", "HIT COUNT", "STATUS"],
        "rows": [
            {"c1": "VEC-0x89A4F2", "c2": "Calculate monthly EBITDA margin", "c3": "0.982 Cos", "c4": "18h 42m", "c5": "1,420 hits", "status": "CACHED"},
            {"c1": "VEC-0x77C1B9", "c2": "Explain double entry ledger rules", "c3": "0.954 Cos", "c4": "12h 15m", "c5": "892 hits", "status": "CACHED"},
            {"c1": "VEC-0x66E3A0", "c2": "Generate quarterly inventory report", "c3": "0.941 Cos", "c4": "22h 08m", "c5": "654 hits", "status": "CACHED"},
            {"c1": "VEC-0x55F8D3", "c2": "Verify procurement PO tax formula", "c3": "0.978 Cos", "c4": "06h 30m", "c5": "421 hits", "status": "CACHED"},
            {"c1": "VEC-0x44D2E1", "c2": "List active fulfillment warehouses", "c3": "0.991 Cos", "c4": "23h 50m", "c5": "2,140 hits", "status": "CACHED"},
        ],
        "right_title": "Cache Eviction & Cluster Health",
        "right_content": """        <g transform="translate(24, 80)">
          <rect width="392" height="540" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <text x="20" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">SEMANTIC THRESHOLD SPECS</text>

          <text x="20" y="66" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Cosine Similarity Cutoff:</text>
          <text x="20" y="88" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="16" font-weight="700">0.920 (Strict Enterprise Mode)</text>

          <text x="20" y="124" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Total RAM Consumption:</text>
          <text x="20" y="146" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="16" font-weight="700">2.42 GB (Distributed In-Memory)</text>

          <line x1="20" y1="168" x2="372" y2="168" stroke="#27272a" stroke-width="1"/>

          <text x="20" y="196" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">QUERY DOMAIN DISTRIBUTION</text>
          <text x="20" y="222" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Financial Analysis</text>
          <text x="340" y="222" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">38%</text>
          <rect x="20" y="230" width="352" height="6" rx="3" fill="#27272a"/>
          <rect x="20" y="230" width="134" height="6" rx="3" fill="#ffffff"/>

          <text x="20" y="262" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Supply Chain &amp; Logistics</text>
          <text x="340" y="262" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">33%</text>
          <rect x="20" y="270" width="352" height="6" rx="3" fill="#27272a"/>
          <rect x="20" y="270" width="116" height="6" rx="3" fill="#ffffff"/>

          <text x="20" y="302" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Executive System Reports</text>
          <text x="340" y="302" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">29%</text>
          <rect x="20" y="310" width="352" height="6" rx="3" fill="#27272a"/>
          <rect x="20" y="310" width="102" height="6" rx="3" fill="#ffffff"/>

          <g transform="translate(20, 340)">
            <rect width="352" height="120" rx="6" fill="#121215" stroke="#27272a" stroke-width="1"/>
            <text x="16" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">AUTOMATED INVALIDATION HOOK</text>
            <text x="16" y="50" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Database Event Mutation Listener</text>
            <text x="16" y="74" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Status: Synced with PostgreSQL CDC</text>
            <text x="16" y="94" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Flushes stale vectors upon balance updates</text>
          </g>
        </g>"""
    },
    "06-guardrails-firewall.svg": {
        "title": "Real-Time AI Firewall & PII Redaction",
        "subtitle": "Zero-Leakage In-Stream Masking, Prompt Injection Defense & Toxicity Blocker",
        "active": "Security & Firewall",
        "url": "https://gateway.internal.mayastranawaloka.com/firewall",
        "kpi": [
            {"label": "PII LEAK INCIDENTS", "val": "0", "badge": "CLEAN", "sub": "100% In-Stream Scrubbing Enforced"},
            {"label": "INJECTIONS BLOCKED", "val": "324", "badge": "DEFENDED", "sub": "Past 24 Hours Heuristic Filter"},
            {"label": "INSPECTION TIME", "val": "1.4ms", "badge": "OVERHEAD", "sub": "Sub-2ms Token Pipeline Delay"},
            {"label": "COMPLIANCE SCORE", "val": "100%", "badge": "ISO27001", "sub": "Strict Corporate Boundary Enforced"},
        ],
        "table_title": "Firewall Intercept Log & Sanitization Events",
        "table_sub": "Proactive protection against prompt injection, data exfiltration, and toxic payload injection",
        "headers": ["EVENT ID", "TIMESTAMP", "THREAT TAXONOMY", "CONFIDENCE", "ACTION TAKEN", "AUDIT REF"],
        "rows": [
            {"c1": "SEC-0x9942", "c2": "11:28:14", "c3": "PII: Bank Account Number", "c4": "99.8%", "c5": "SHA-256 Masked", "status": "VERIFIED"},
            {"c1": "SEC-0x9941", "c2": "11:24:02", "c3": "Adversarial Prompt Injection", "c4": "98.2%", "c5": "Dropped HTTP 403", "status": "VERIFIED"},
            {"c1": "SEC-0x9940", "c2": "11:19:48", "c3": "System Prompt Extraction", "c4": "97.6%", "c5": "Halted &amp; Logged", "status": "VERIFIED"},
            {"c1": "SEC-0x9939", "c2": "11:15:22", "c3": "PII: Employee Tax ID Number", "c4": "99.9%", "c5": "Synthetic Replaced", "status": "VERIFIED"},
            {"c1": "SEC-0x9938", "c2": "11:10:05", "c3": "Unauthorized API Exfiltration", "c4": "96.5%", "c5": "Blocked at Gateway", "status": "VERIFIED"},
        ],
        "right_title": "Active Firewall Rules & Regex Guardrails",
        "right_content": """        <g transform="translate(24, 80)">
          <rect width="392" height="540" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <text x="20" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">IN-STREAM SANITIZATION RULES</text>

          <g transform="translate(20, 60)">
            <rect width="352" height="74" rx="4" fill="#121215" stroke="#27272a" stroke-width="1"/>
            <text x="14" y="24" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">RULE-01: Financial Data Masking</text>
            <text x="14" y="44" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Detects Bank Account, IBAN, Credit Cards</text>
            <text x="14" y="62" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Action: Cryptographic Token Replacement</text>
          </g>

          <g transform="translate(20, 146)">
            <rect width="352" height="74" rx="4" fill="#121215" stroke="#27272a" stroke-width="1"/>
            <text x="14" y="24" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">RULE-02: Adversarial Jailbreak Defense</text>
            <text x="14" y="44" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Filters context escaping and token manipulation</text>
            <text x="14" y="62" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Action: Immediate Rejection HTTP 403</text>
          </g>

          <g transform="translate(20, 232)">
            <rect width="352" height="74" rx="4" fill="#121215" stroke="#27272a" stroke-width="1"/>
            <text x="14" y="24" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">RULE-03: Credential Exfiltration Blocker</text>
            <text x="14" y="44" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Intercepts RSA keys, SSH certs, JWT secrets</text>
            <text x="14" y="62" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Action: Instant Drop &amp; Security Alert</text>
          </g>

          <text x="20" y="340" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">SANITIZATION LATENCY IMPACT</text>
          <text x="20" y="364" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="18" font-weight="700">1.42 ms Mean Latency</text>
          <text x="20" y="386" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Zero measurable impact on time-to-first-token</text>
        </g>"""
    },
    "07-streaming-orchestrator.svg": {
        "title": "Ultra Low-Latency Token Streaming Orchestrator",
        "subtitle": "Server-Sent Events (SSE), gRPC Duplex Pipelines & Speculative Token Pre-Warming",
        "active": "Gateway Telemetry",
        "url": "https://gateway.internal.mayastranawaloka.com/stream",
        "kpi": [
            {"label": "TIME-TO-FIRST-TOKEN", "val": "82ms", "badge": "MEDIAN", "sub": "Speculative Token Pre-Warming Active"},
            {"label": "ACTIVE STREAM CHANNELS", "val": "1,240", "badge": "DUPLEX", "sub": "Real-Time SSE and gRPC Connections"},
            {"label": "BACKPRESSURE SPILL", "val": "0.00%", "badge": "ZERO LOSS", "sub": "Adaptive Flow Control Buffering"},
            {"label": "TOKEN VELOCITY", "val": "64.2k", "badge": "TOKENS / SEC", "sub": "Multi-Threaded Socket Multiplexing"},
        ],
        "table_title": "Active Streaming Channels & Connection Telemetry",
        "table_sub": "Inspect real-time token dispatch velocity, socket buffer depth, and client latency",
        "headers": ["CHANNEL ID", "CONSUMING CLIENT", "PROTOCOL", "STREAM VELOCITY", "BUFFER DEPTH", "STATUS"],
        "rows": [
            {"c1": "STRM-0x992", "c2": "ERP Executive Analytics", "c3": "SSE Duplex", "c4": "84 tokens/s", "c5": "16 KB Buffer", "status": "ACTIVE"},
            {"c1": "STRM-0x884", "c2": "Financial Ledger Assistant", "c3": "gRPC Bi-Di", "c4": "112 tokens/s", "c5": "32 KB Buffer", "status": "ACTIVE"},
            {"c1": "STRM-0x771", "c2": "Customer Service Terminal", "c3": "SSE Stream", "c4": "68 tokens/s", "c5": "8 KB Buffer", "status": "ACTIVE"},
            {"c1": "STRM-0x650", "c2": "Automated Report Generator", "c3": "gRPC Bi-Di", "c4": "140 tokens/s", "c5": "64 KB Buffer", "status": "ACTIVE"},
            {"c1": "STRM-0x529", "c2": "Code Synthesis Sandbox", "c3": "SSE Duplex", "c4": "96 tokens/s", "c5": "24 KB Buffer", "status": "ACTIVE"},
        ],
        "right_title": "Streaming Latency Waterfall & Pipeline",
        "right_content": """        <g transform="translate(24, 80)">
          <rect width="392" height="540" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <text x="20" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">END-TO-END LATENCY BREAKDOWN</text>

          <text x="20" y="70" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">1. Client TLS Handshake</text>
          <text x="330" y="70" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">14 ms</text>
          <rect x="20" y="80" width="352" height="8" rx="4" fill="#27272a"/>
          <rect x="20" y="80" width="48" height="8" rx="4" fill="#ffffff"/>

          <text x="20" y="120" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">2. Semantic Intent Router</text>
          <text x="330" y="120" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">2 ms</text>
          <rect x="20" y="130" width="352" height="8" rx="4" fill="#27272a"/>
          <rect x="20" y="130" width="16" height="8" rx="4" fill="#ffffff"/>

          <text x="20" y="170" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">3. Model First-Token Synthesis</text>
          <text x="330" y="170" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">56 ms</text>
          <rect x="20" y="180" width="352" height="8" rx="4" fill="#27272a"/>
          <rect x="20" y="180" width="220" height="8" rx="4" fill="#ffffff"/>

          <text x="20" y="220" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">4. Firewall In-Stream Scrubbing</text>
          <text x="330" y="220" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">1 ms</text>
          <rect x="20" y="230" width="352" height="8" rx="4" fill="#27272a"/>
          <rect x="20" y="230" width="10" height="8" rx="4" fill="#ffffff"/>

          <text x="20" y="270" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">5. gRPC Chunk Serialization</text>
          <text x="330" y="270" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">9 ms</text>
          <rect x="20" y="280" width="352" height="8" rx="4" fill="#27272a"/>
          <rect x="20" y="280" width="36" height="8" rx="4" fill="#ffffff"/>

          <line x1="20" y1="310" x2="372" y2="310" stroke="#27272a" stroke-width="1"/>

          <text x="20" y="340" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">AGGREGATE TTFT MEDIAN</text>
          <text x="20" y="370" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="700">82 ms</text>
          <text x="20" y="394" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Speculative decoding pre-warms context window</text>
        </g>"""
    },
    "08-finetune-lora-registry.svg": {
        "title": "LoRA Adapter & Fine-Tuning Registry",
        "subtitle": "Enterprise Custom Weights Repository, Parameter-Efficient Adaptation & Zero-Downtime Hot-Swap",
        "active": "Model Router",
        "url": "https://gateway.internal.mayastranawaloka.com/lora",
        "kpi": [
            {"label": "PRODUCTION ADAPTERS", "val": "8", "badge": "MOUNTED", "sub": "Custom Domain Specific Weights"},
            {"label": "HOT-SWAP DOWNTIME", "val": "0ms", "badge": "IN-VRAM", "sub": "Zero Process Restarts or Latency Spikes"},
            {"label": "VRAM PER ADAPTER", "val": "380MB", "badge": "EFFICIENT", "sub": "Base Model Parameters Shared"},
            {"label": "VALIDATION LOSS", "val": "0.042", "badge": "CONVERGED", "sub": "Zero Catastrophic Forgetting Detected"},
        ],
        "table_title": "Enterprise Adapter Registry & VRAM Allocations",
        "table_sub": "Dynamically attaches low-rank adaptation weights to base foundation clusters",
        "headers": ["ADAPTER ID", "DOMAIN APPLICATION", "BASE ARCHITECTURE", "RANK SPECS", "VAL LOSS", "STATUS"],
        "rows": [
            {"c1": "LORA-FIN-01", "c2": "Corporate Accounting &amp; Tax", "c3": "Deep Reasoning 32B", "c4": "r=64 a=128", "c5": "0.038", "status": "MOUNTED"},
            {"c1": "LORA-SCM-02", "c2": "Supply Chain &amp; Logistics", "c3": "High-Throughput 70B", "c4": "r=64 a=128", "c5": "0.041", "status": "MOUNTED"},
            {"c1": "LORA-LEG-03", "c2": "Procurement Contract Law", "c3": "Deep Reasoning 32B", "c4": "r=32 a=64", "c5": "0.044", "status": "MOUNTED"},
            {"c1": "LORA-OPS-04", "c2": "DevOps Incident Recovery", "c3": "Code Synthesis 34B", "c4": "r=64 a=128", "c5": "0.039", "status": "MOUNTED"},
            {"c1": "LORA-MED-05", "c2": "Indonesian-EN Domain Parity", "c3": "High-Throughput 70B", "c4": "r=32 a=64", "c5": "0.049", "status": "MOUNTED"},
        ],
        "right_title": "VRAM Memory Management & Checkpoints",
        "right_content": """        <g transform="translate(24, 80)">
          <rect width="392" height="540" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <text x="20" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">IN-MEMORY ADAPTER CACHE</text>

          <text x="20" y="66" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Base Model Memory Map:</text>
          <text x="20" y="88" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="16" font-weight="700">70B Dense FP16 (140 GB Shared)</text>

          <text x="20" y="124" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Total LoRA Adapter Overhead:</text>
          <text x="20" y="146" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="16" font-weight="700">3.04 GB (8 Mounted Adapters)</text>

          <line x1="20" y1="168" x2="372" y2="168" stroke="#27272a" stroke-width="1"/>

          <text x="20" y="196" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">ADAPTER SWAP LATENCY</text>
          <text x="20" y="222" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Hot-Swap Overhead</text>
          <text x="330" y="222" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">12 ms</text>
          <rect x="20" y="230" width="352" height="6" rx="3" fill="#27272a"/>
          <rect x="20" y="230" width="48" height="6" rx="3" fill="#ffffff"/>

          <g transform="translate(20, 270)">
            <rect width="352" height="150" rx="6" fill="#121215" stroke="#27272a" stroke-width="1"/>
            <text x="16" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">WEIGHTS CRYPTOGRAPHIC PROVENANCE</text>
            <text x="16" y="50" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Checkpoint Signature: SHA-256 Verified</text>
            <text x="16" y="74" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">100% In-House Weights Ownership</text>
            <text x="16" y="94" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Trained on air-gapped secure cluster</text>
            <text x="16" y="114" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Zero external weight leak or transmission</text>
          </g>
        </g>"""
    },
    "09-quota-cost-allocation.svg": {
        "title": "Multi-Tenant Quota & Departmental Cost Allocation",
        "subtitle": "Departmental Token Budgets, Tiered Rate Limits & Automatic Financial Chargebacks",
        "active": "Audit Logs",
        "url": "https://gateway.internal.mayastranawaloka.com/billing",
        "kpi": [
            {"label": "MONTHLY BUDGET CEILING", "val": "$48,000", "badge": "HARD CAP", "sub": "Zero Overdrafts or Bill Surprises"},
            {"label": "CURRENT MONTH BURN", "val": "$28,490", "badge": "59.3% USED", "sub": "18 Days Remaining in Billing Cycle"},
            {"label": "BUSINESS UNITS TRACKED", "val": "12", "badge": "TENANTS", "sub": "Granular Header-Based Attribution"},
            {"label": "BLENDED COST / 1M TOKENS", "val": "$1.80", "badge": "-42% YIELD", "sub": "Optimized by Semantic Router Matrix"},
        ],
        "table_title": "Departmental Token Quotas & Utilization Matrix",
        "table_sub": "Enforces strict financial governance and automated departmental cost chargebacks",
        "headers": ["BUSINESS UNIT", "TOKEN CEILING", "CONSUMED TOKENS", "PROJECTED COST", "RATE LIMIT", "STATUS"],
        "rows": [
            {"c1": "Operations &amp; Logistics", "c2": "150M Tokens", "c3": "98.4M Tokens", "c4": "$11,800", "c5": "200 req/s", "status": "NORMAL"},
            {"c1": "Finance &amp; Accounting", "c2": "80M Tokens", "c3": "46.2M Tokens", "c4": "$5,540", "c5": "100 req/s", "status": "NORMAL"},
            {"c1": "Customer Success", "c2": "60M Tokens", "c3": "38.9M Tokens", "c4": "$4,660", "c5": "150 req/s", "status": "NORMAL"},
            {"c1": "Engineering &amp; DevOps", "c2": "100M Tokens", "c3": "54.1M Tokens", "c4": "$6,490", "c5": "250 req/s", "status": "NORMAL"},
            {"c1": "Legal &amp; Compliance", "c2": "20M Tokens", "c3": "8.4M Tokens", "c4": "$1,000", "c5": "50 req/s", "status": "NORMAL"},
        ],
        "right_title": "Spend Trajectory & Chargeback Integration",
        "right_content": """        <g transform="translate(24, 80)">
          <rect width="392" height="540" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <text x="20" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">BUDGET ENFORCEMENT ENGINE</text>

          <text x="20" y="70" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Current Month Burn Rate:</text>
          <text x="20" y="94" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="22" font-weight="700">$1,582 / Day Average</text>

          <text x="20" y="130" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Projected End-of-Month Total:</text>
          <text x="20" y="154" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="22" font-weight="700">$43,200 (Under $48k Cap)</text>

          <line x1="20" y1="180" x2="372" y2="180" stroke="#27272a" stroke-width="1"/>

          <text x="20" y="210" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">ERP GENERAL LEDGER SYNC</text>
          <text x="20" y="234" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Journal Entry: Accrual Debit 5100 (IT Cloud)</text>
          <text x="20" y="254" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Credit: 2100 Accounts Payable</text>

          <g transform="translate(20, 280)">
            <rect width="352" height="150" rx="6" fill="#121215" stroke="#27272a" stroke-width="1"/>
            <text x="16" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">AUTOMATIC RATE LIMIT THROTTLE</text>
            <text x="16" y="50" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Tiered Soft / Hard Warning Limits</text>
            <text x="16" y="74" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">80% Threshold: Warning Dispatch</text>
            <text x="16" y="94" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">100% Threshold: Graceful Rate Throttling</text>
            <text x="16" y="114" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Prevents rogue loops from draining corporate funds</text>
          </g>
        </g>"""
    },
    "10-audit-compliance-trail.svg": {
        "title": "Enterprise Compliance & Immutable Prompt Audit Trail",
        "subtitle": "SHA-256 Chained Event Logs, SOC2 Type II Readiness & Cryptographic Verification",
        "active": "Audit Logs",
        "url": "https://gateway.internal.mayastranawaloka.com/audit",
        "kpi": [
            {"label": "LOGGED TRANSACTIONS", "val": "14.2M", "badge": "100% COVER", "sub": "Zero Missing Records or Log Gaps"},
            {"label": "MERKLE ROOT STATUS", "val": "VALID", "badge": "SHA-256", "sub": "Cryptographic Proof Tamper-Proof"},
            {"label": "COMPLIANCE READINESS", "val": "SOC2 / ISO", "badge": "TYPE II", "sub": "Enterprise Financial Grade Audit"},
            {"label": "IMMUTABLE RETENTION", "val": "7 Years", "badge": "WORM LOCK", "sub": "Write-Once Read-Many Sealed Storage"},
        ],
        "table_title": "Cryptographic Audit Ledger & Chain of Custody",
        "table_sub": "Every prompt dispatch, response hash, and token usage event is immutably hashed and verifiable",
        "headers": ["AUDIT HASH", "TIMESTAMP", "SERVICE ORIGIN", "MODEL CLUSTER", "POLICY RESULT", "STATUS"],
        "rows": [
            {"c1": "0x8F90A1..D2", "c2": "11:29:40", "c3": "Svc-ERP-Operations", "c4": "Deep Reasoning 32B", "c5": "PII Masked Clean", "status": "VERIFIED"},
            {"c1": "0x7E8B42..91", "c2": "11:29:38", "c3": "Svc-Fin-Ledger", "c4": "High-Throughput 70B", "c5": "Guardrail Passed", "status": "VERIFIED"},
            {"c1": "0x6D4A19..3C", "c2": "11:29:35", "c3": "Svc-Logistics-Hub", "c4": "Edge Fast 8B", "c5": "Rate Limit OK", "status": "VERIFIED"},
            {"c1": "0x5C1277..88", "c2": "11:29:31", "c3": "Svc-DevOps-Pipeline", "c4": "Code Synthesis 34B", "c5": "Sandboxed Verified", "status": "VERIFIED"},
            {"c1": "0x4B9954..10", "c2": "11:29:28", "c3": "Svc-Customer-API", "c4": "High-Throughput 70B", "c5": "DLP Scrubbed", "status": "VERIFIED"},
        ],
        "right_title": "Merkle Tree Proof & Non-Repudiation",
        "right_content": """        <g transform="translate(24, 80)">
          <rect width="392" height="540" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <text x="20" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">CRYPTOGRAPHIC PROOF VERIFIER</text>

          <text x="20" y="70" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Current Block Height:</text>
          <text x="20" y="94" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="20" font-weight="700">Block #1,842,910</text>

          <text x="20" y="130" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Merkle Root Hash:</text>
          <text x="20" y="152" fill="#d4d4d8" font-family="monospace" font-size="10">0x992bf441a7c0932810e4a7812bc8819</text>

          <line x1="20" y1="180" x2="372" y2="180" stroke="#27272a" stroke-width="1"/>

          <text x="20" y="210" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">INSPECTOR BUNDLE EXPORT</text>
          <text x="20" y="234" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Export complete cryptographically signed evidence</text>
          <rect x="20" y="250" width="352" height="36" rx="4" fill="#27272a"/>
          <text x="196" y="272" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="middle">DOWNLOAD AUDIT ARCHIVE (ZIP)</text>

          <g transform="translate(20, 310)">
            <rect width="352" height="140" rx="6" fill="#121215" stroke="#27272a" stroke-width="1"/>
            <text x="16" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">NON-REPUDIATION GUARANTEE</text>
            <text x="16" y="50" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Signed with Enterprise HSM Private Key</text>
            <text x="16" y="74" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Integrity: 100% Tamper Evident</text>
            <text x="16" y="94" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Acceptable for external legal &amp; tax discovery</text>
          </g>
        </g>"""
    },
    "11-synthetic-dataset-factory.svg": {
        "title": "Synthetic Dataset Generation & Curation Pipeline",
        "subtitle": "Domain Calibration Sets, Semantic Deduplication & Human-Aligned Curation",
        "active": "Prompt Eval Harness",
        "url": "https://gateway.internal.mayastranawaloka.com/datasets",
        "kpi": [
            {"label": "CURATED TRAINING PAIRS", "val": "250,000", "badge": "CURATED", "sub": "High-Diversity Instruction Sets"},
            {"label": "DEDUPLICATION RATE", "val": "99.8%", "badge": "UNIQUE", "sub": "Cosine Distance Filter >= 0.15"},
            {"label": "SCHEMA VALIDITY", "val": "100%", "badge": "JSON SCHEMA", "sub": "Automated AST Syntactic Validator"},
            {"label": "ACCURACY UPLIFT", "val": "+18.4%", "badge": "BENCHMARK", "sub": "Measurable Domain Knowledge Gain"},
        ],
        "table_title": "Synthetic Generation Batches & Curation Status",
        "table_sub": "Produces fine-tuning and evaluation datasets to calibrate internal foundation models",
        "headers": ["BATCH ID", "DOMAIN TAXONOMY", "GENERATION RECIPE", "SAMPLE COUNT", "PASS RATE", "STATUS"],
        "rows": [
            {"c1": "SYNTH-014", "c2": "Double-Entry Ledger Rules", "c3": "Evol-Instruct Multi-Turn", "c4": "50,000 pairs", "c5": "99.4%", "status": "COMPLETED"},
            {"c1": "SYNTH-015", "c2": "Warehouse Logistics Edges", "c3": "Self-Consistency Debate", "c4": "40,000 pairs", "c5": "99.1%", "status": "COMPLETED"},
            {"c1": "SYNTH-016", "c2": "Indonesian Corporate Tax", "c3": "Constitutional Grounding", "c4": "35,000 pairs", "c5": "99.8%", "status": "COMPLETED"},
            {"c1": "SYNTH-017", "c2": "Microservice Error Scenarios", "c3": "Failure Perturbation", "c4": "45,000 pairs", "c5": "98.9%", "status": "COMPLETED"},
            {"c1": "SYNTH-018", "c2": "Contract Clause Variations", "c3": "Counterfactual Synthesis", "c4": "30,000 pairs", "c5": "99.2%", "status": "OPTIMAL"},
        ],
        "right_title": "Dataset Quality Filters & Distribution",
        "right_content": """        <g transform="translate(24, 80)">
          <rect width="392" height="540" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <text x="20" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">QUALITY CONTROL FILTERS</text>

          <text x="20" y="70" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">1. Syntactic Schema Conformance</text>
          <text x="330" y="70" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">100%</text>
          <rect x="20" y="80" width="352" height="6" rx="3" fill="#27272a"/>
          <rect x="20" y="80" width="352" height="6" rx="3" fill="#ffffff"/>

          <text x="20" y="114" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">2. Semantic Deduplication</text>
          <text x="330" y="114" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">99.8%</text>
          <rect x="20" y="124" width="352" height="6" rx="3" fill="#27272a"/>
          <rect x="20" y="124" width="350" height="6" rx="3" fill="#ffffff"/>

          <text x="20" y="158" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">3. Factuality Verification</text>
          <text x="330" y="158" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">99.2%</text>
          <rect x="20" y="168" width="352" height="6" rx="3" fill="#27272a"/>
          <rect x="20" y="168" width="348" height="6" rx="3" fill="#ffffff"/>

          <line x1="20" y1="196" x2="372" y2="196" stroke="#27272a" stroke-width="1"/>

          <text x="20" y="226" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">TOKEN LENGTH HISTOGRAM</text>
          <text x="20" y="250" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Short (512 tokens): 25% | Medium (1024): 50% | Long (4096): 25%</text>

          <g transform="translate(20, 270)">
            <rect width="352" height="150" rx="6" fill="#121215" stroke="#27272a" stroke-width="1"/>
            <text x="16" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">DATASET EXPORT FORMATS</text>
            <text x="16" y="50" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Pre-formatted for local model training</text>
            <text x="16" y="74" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Formats: JSONL, Arrow, Parquet</text>
            <text x="16" y="94" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Grounded against verified internal databases</text>
            <text x="16" y="114" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Zero external telemetry or web leakage</text>
          </g>
        </g>"""
    }
}

out_dir = "assets/projects/llm-gateway"
os.makedirs(out_dir, exist_ok=True)

for fname, d in screens.items():
    kpi_svg = build_kpi_cards(d['kpi'][0], d['kpi'][1], d['kpi'][2], d['kpi'][3])
    split_svg = build_split_layout(d['table_title'], d['table_sub'], d['headers'], d['rows'], d['right_title'], d['right_content'])
    content = kpi_svg + split_svg
    svg_out = wrap_svg(content, d['active'], d['title'], d['subtitle'], d['url'])

    # Validate XML
    ET.fromstring(svg_out)
    for b in ["—", "–", "&#8212;", "&mdash;"]:
        assert b not in svg_out, f"Banned dash in {fname}"

    path = os.path.join(out_dir, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg_out)
    print(f"Generated {path}")

# Write master SVG byte-for-byte identical to Screen 01
master_path = "assets/project-llm-gateway.svg"
with open(os.path.join(out_dir, "01-gateway-telemetry.svg"), "r", encoding="utf-8") as f:
    master_content = f.read()

with open(master_path, "w", encoding="utf-8") as f:
    f.write(master_content)

print(f"Master {master_path} written byte-for-byte identical to 01-gateway-telemetry.svg")
