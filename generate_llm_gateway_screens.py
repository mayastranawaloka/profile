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
    <rect x="16" y="{offset+14}" width="10" height="10" fill="#06b6d4"/>
    <text x="38" y="{offset+24}" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="500">{name}</text>\n"""
        else:
            menu_svg += f"""    <rect x="16" y="{offset+14}" width="10" height="10" fill="#52525b"/>
    <text x="38" y="{offset+24}" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">{name}</text>\n"""

    return f"""  <!-- Sidebar -->
  <rect x="0" y="52" width="260" height="948" fill="#0d0d10" stroke="#27272a" stroke-width="1"/>
  <!-- Brand in Gateway -->
  <rect x="28" y="80" width="24" height="24" rx="4" fill="#06b6d4"/>
  <text x="64" y="97" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="700" letter-spacing="1.5">AI GATEWAY</text>

  <!-- Nav items -->
  <g transform="translate(24, 140)">
{menu_svg}  </g>

  <!-- Cluster status at bottom sidebar -->
  <rect x="24" y="930" width="212" height="42" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
  <circle cx="48" cy="951" r="5" fill="#10b981"/>
  <text x="64" y="948" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Enterprise Vault #01</text>
  <text x="64" y="961" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">HSM Encrypted / FIPS-140</text>"""

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

    <rect x="1190" y="8" width="90" height="34" rx="4" fill="#06b6d4"/>
    <text x="1235" y="30" fill="#000000" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="middle">{btn2_label}</text>
  </g>"""

def wrap_svg(inner_content, active_name, title, subtitle, url="https://gateway.internal.mayastranawaloka.com/telemetry"):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 1000" width="1600" height="1000">
  <defs>
    <linearGradient id="bgGlow" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#070708"/>
      <stop offset="100%" stop-color="#0a0a0d"/>
    </linearGradient>
    <linearGradient id="cyanGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#06b6d4" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#06b6d4" stop-opacity="0.0"/>
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

# Define Screens 01 to 11
content_01 = """    <!-- 4 KPI Cards -->
    <g transform="translate(0, 0)">
      <rect width="300" height="96" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="20" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="500">24H TOKEN VELOCITY</text>
      <text x="20" y="64" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="700">48.2M</text>
      <text x="140" y="64" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">+19.4% WoW</text>
      <text x="20" y="82" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Aggregated Prompt &amp; Completion</text>

      <rect x="325" y="0" width="300" height="96" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="345" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="500">ACTIVE API KEY VAULTS</text>
      <text x="345" y="64" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="700">142</text>
      <text x="425" y="64" fill="#06b6d4" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Zero Leaks</text>
      <text x="345" y="82" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Hardware Security Module Sealed</text>

      <rect x="650" y="0" width="300" height="96" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="670" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="500">MEDIAN GATEWAY LATENCY</text>
      <text x="670" y="64" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="700">118ms</text>
      <text x="770" y="64" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Cache: 6ms</text>
      <text x="670" y="82" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Edge Routing with Zero Jitter</text>

      <rect x="975" y="0" width="305" height="96" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="995" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="500">COST OPTIMIZATION YIELD</text>
      <text x="995" y="64" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="700">41.8%</text>
      <text x="1105" y="64" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Saved</text>
      <text x="995" y="82" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Via Semantic Cache &amp; Routing</text>
    </g>

    <!-- Mid Section: Model Traffic Velocity & Live Stream Panel -->
    <g transform="translate(0, 116)">
      <!-- Left Chart: Routing Velocity -->
      <rect width="780" height="340" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="24" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="15" font-weight="600">Dynamic Model Routing Matrix &amp; Velocity</text>
      <text x="24" y="52" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Real-time token distribution across Foundation, Reasoning, and Specialist clusters</text>

      <!-- Grid lines -->
      <line x1="24" y1="100" x2="756" y2="100" stroke="#1f1f23" stroke-width="1"/>
      <line x1="24" y1="160" x2="756" y2="160" stroke="#1f1f23" stroke-width="1"/>
      <line x1="24" y1="220" x2="756" y2="220" stroke="#1f1f23" stroke-width="1"/>
      <line x1="24" y1="280" x2="756" y2="280" stroke="#1f1f23" stroke-width="1"/>

      <!-- Path chart: primary foundation model velocity -->
      <path d="M 30 260 Q 120 220 200 240 T 380 180 T 540 130 T 750 90 L 750 280 L 30 280 Z" fill="url(#cyanGrad)"/>
      <path d="M 30 260 Q 120 220 200 240 T 380 180 T 540 130 T 750 90" fill="none" stroke="#06b6d4" stroke-width="2.5"/>

      <!-- Secondary model: reasoning model path -->
      <path d="M 30 270 Q 140 250 220 260 T 400 210 T 560 170 T 750 140" fill="none" stroke="#a855f7" stroke-width="2" stroke-dasharray="4,4"/>

      <!-- Legend -->
      <rect x="24" y="304" width="10" height="10" rx="2" fill="#06b6d4"/>
      <text x="40" y="313" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">High-Throughput Model API</text>

      <rect x="230" y="304" width="10" height="10" rx="2" fill="#a855f7"/>
      <text x="246" y="313" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Deep Reasoning Engine (Speculative 32B)</text>

      <rect x="520" y="304" width="10" height="10" rx="2" fill="#10b981"/>
      <text x="536" y="313" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Sub-Millisecond Semantic Cache Hit</text>

      <!-- Right Panel: Live Gateway Ingestion Stream -->
      <rect x="805" width="475" height="340" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="825" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="15" font-weight="600">Live API Key Ingestion Stream</text>
      <text x="825" y="52" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Automated Key Rotation &amp; Redaction</text>

      <!-- Stream item 1 -->
      <rect x="825" y="72" width="435" height="54" rx="4" fill="#16161a" stroke="#27272a" stroke-width="1"/>
      <rect x="837" y="85" width="58" height="20" rx="3" fill="#06b6d4" fill-opacity="0.15"/>
      <text x="866" y="99" fill="#06b6d4" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="600" text-anchor="middle">ROUTED</text>
      <text x="905" y="94" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">sk_live_sec_***89f2</text>
      <text x="905" y="112" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Finance Ledger Copilot / 4,120 tok</text>
      <text x="1245" y="94" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="end">88ms</text>
      <text x="1245" y="112" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" text-anchor="end">Cluster US-East</text>

      <!-- Stream item 2 -->
      <rect x="825" y="136" width="435" height="54" rx="4" fill="#16161a" stroke="#27272a" stroke-width="1"/>
      <rect x="837" y="149" width="58" height="20" rx="3" fill="#10b981" fill-opacity="0.15"/>
      <text x="866" y="163" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="600" text-anchor="middle">CACHED</text>
      <text x="905" y="158" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">sk_live_sec_***41ab</text>
      <text x="905" y="176" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Catalog Auto-Categorization / 890 tok</text>
      <text x="1245" y="158" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="end">4ms</text>
      <text x="1245" y="176" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" text-anchor="end">Zero Cost Hit</text>

      <!-- Stream item 3 -->
      <rect x="825" y="200" width="435" height="54" rx="4" fill="#16161a" stroke="#27272a" stroke-width="1"/>
      <rect x="837" y="213" width="58" height="20" rx="3" fill="#f59e0b" fill-opacity="0.15"/>
      <text x="866" y="227" fill="#f59e0b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="600" text-anchor="middle">FALLBACK</text>
      <text x="905" y="222" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">sk_live_sec_***902c</text>
      <text x="905" y="240" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Legal Compliance Parser / 8,240 tok</text>
      <text x="1245" y="222" fill="#f59e0b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="end">240ms</text>
      <text x="1245" y="240" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" text-anchor="end">Tier-2 Failover</text>

      <!-- Stream item 4 -->
      <rect x="825" y="264" width="435" height="54" rx="4" fill="#16161a" stroke="#27272a" stroke-width="1"/>
      <rect x="837" y="277" width="58" height="20" rx="3" fill="#06b6d4" fill-opacity="0.15"/>
      <text x="866" y="291" fill="#06b6d4" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="600" text-anchor="middle">ROUTED</text>
      <text x="905" y="286" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">sk_live_sec_***112d</text>
      <text x="905" y="304" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Customer Ticket Triage / 1,450 tok</text>
      <text x="1245" y="286" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="end">92ms</text>
      <text x="1245" y="304" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" text-anchor="end">Cluster APAC-Edge</text>
    </g>

    <!-- Bottom Section: Cluster Health & Quota Consumption Table -->
    <g transform="translate(0, 480)">
      <rect width="1280" height="300" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="24" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="15" font-weight="600">Foundation Model Provider Clusters &amp; Token Budget Allocations</text>
      <text x="24" y="52" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Automated load-balancing with rate-limit dampening across multi-provider accounts</text>

      <!-- Table Header -->
      <rect x="24" y="70" width="1232" height="34" rx="4" fill="#16161a"/>
      <text x="44" y="92" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">PROVIDER CLUSTER</text>
      <text x="320" y="92" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">TIER &amp; ARCHITECTURE</text>
      <text x="560" y="92" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">HEALTH / P99</text>
      <text x="760" y="92" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">CONCURRENCY</text>
      <text x="960" y="92" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">DAILY SPEND</text>
      <text x="1160" y="92" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">FAILOVER</text>

      <!-- Row 1 -->
      <g transform="translate(24, 112)">
        <circle cx="20" cy="18" r="4" fill="#10b981"/>
        <text x="40" y="22" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Primary Core Model API (US-East)</text>
        <text x="296" y="22" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Dense 70B Foundation</text>
        <text x="536" y="22" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">99.99% / 142ms</text>
        <text x="736" y="22" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">184 / 500 max</text>
        <text x="936" y="22" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">IDR 4.2M / 10M</text>
        <rect x="1136" y="8" width="60" height="20" rx="3" fill="#10b981" fill-opacity="0.15"/>
        <text x="1166" y="22" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="600" text-anchor="middle">ACTIVE</text>
        <line x1="0" y1="36" x2="1232" y2="36" stroke="#1f1f23" stroke-width="1"/>
      </g>

      <!-- Row 2 -->
      <g transform="translate(24, 156)">
        <circle cx="20" cy="18" r="4" fill="#10b981"/>
        <text x="40" y="22" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Deep Reasoning Node (EU-Central)</text>
        <text x="296" y="22" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Speculative CoT 32B</text>
        <text x="536" y="22" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">99.95% / 310ms</text>
        <text x="736" y="22" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">42 / 200 max</text>
        <text x="936" y="22" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">IDR 1.8M / 5M</text>
        <rect x="1136" y="8" width="60" height="20" rx="3" fill="#10b981" fill-opacity="0.15"/>
        <text x="1166" y="22" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="600" text-anchor="middle">ACTIVE</text>
        <line x1="0" y1="36" x2="1232" y2="36" stroke="#1f1f23" stroke-width="1"/>
      </g>

      <!-- Row 3 -->
      <g transform="translate(24, 200)">
        <circle cx="20" cy="18" r="4" fill="#10b981"/>
        <text x="40" y="22" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Fast Token Specialist (APAC-Edge)</text>
        <text x="296" y="22" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Distilled 8B Architecture</text>
        <text x="536" y="22" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">100.0% / 44ms</text>
        <text x="736" y="22" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">312 / 1000 max</text>
        <text x="936" y="22" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">IDR 920K / 4M</text>
        <rect x="1136" y="8" width="60" height="20" rx="3" fill="#10b981" fill-opacity="0.15"/>
        <text x="1166" y="22" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="600" text-anchor="middle">ACTIVE</text>
        <line x1="0" y1="36" x2="1232" y2="36" stroke="#1f1f23" stroke-width="1"/>
      </g>

      <!-- Row 4 -->
      <g transform="translate(24, 244)">
        <circle cx="20" cy="18" r="4" fill="#06b6d4"/>
        <text x="40" y="22" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Semantic Vector Cache Cluster</text>
        <text x="296" y="22" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">In-Memory 1536D Cosine Match</text>
        <text x="536" y="22" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Hit Rate: 34.2%</text>
        <text x="736" y="22" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Zero API Egress</text>
        <text x="936" y="22" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Saved: IDR 3.4M</text>
        <rect x="1136" y="8" width="60" height="20" rx="3" fill="#06b6d4" fill-opacity="0.15"/>
        <text x="1166" y="22" fill="#06b6d4" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="600" text-anchor="middle">LOCAL</text>
      </g>
    </g>"""

# Dictionary of 11 screens definitions
screens = {
    "01-gateway-telemetry.svg": {
        "title": "Enterprise LLM Gateway Telemetry",
        "subtitle": "Real-Time Multi-Provider Token Dispatch, Sub-Millisecond Routing & HSM Key Security",
        "active": "Gateway Telemetry",
        "url": "https://gateway.internal.mayastranawaloka.com/telemetry",
        "content": content_01
    },
    "02-key-vault-governance.svg": {
        "title": "Unified API Key Vault & Governance",
        "subtitle": "Hardware Security Module (HSM) FIPS-140 Encryption, Zero Plaintext Storage & Role-Based Access Control",
        "active": "Key Vault & RBAC",
        "url": "https://gateway.internal.mayastranawaloka.com/keys",
        "content": """    <rect width="1280" height="780" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
    <text x="32" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="18" font-weight="600">Enterprise Encrypted API Key Storage &amp; Scope Manager</text>
    <text x="32" y="68" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Master encryption keys never leave physical HSM boundary; client applications consume ephemeral virtual tokens</text>

    <!-- Key Stats -->
    <g transform="translate(32, 96)">
      <rect width="280" height="84" rx="4" fill="#16161a" stroke="#27272a"/>
      <text x="20" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">TOTAL MANAGED KEYS</text>
      <text x="20" y="60" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="24" font-weight="700">142 Keys</text>

      <rect x="310" width="280" height="84" rx="4" fill="#16161a" stroke="#27272a"/>
      <text x="330" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">AUTO-ROTATION INTERVAL</text>
      <text x="330" y="60" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="24" font-weight="700">30 Days</text>

      <rect x="620" width="280" height="84" rx="4" fill="#16161a" stroke="#27272a"/>
      <text x="640" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">LEAK PROTECTION ENGINE</text>
      <text x="640" y="60" fill="#06b6d4" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="24" font-weight="700">Active Shield</text>

      <rect x="930" width="280" height="84" rx="4" fill="#16161a" stroke="#27272a"/>
      <text x="950" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">FIPS-140-3 COMPLIANCE</text>
      <text x="950" y="60" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="24" font-weight="700">Enforced</text>
    </g>

    <!-- Key Table -->
    <g transform="translate(32, 210)">
      <rect width="1216" height="530" rx="4" fill="#16161a" stroke="#27272a"/>
      <text x="24" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Active Production API Key Profiles</text>

      <rect x="24" y="52" width="1168" height="32" rx="3" fill="#1f1f23"/>
      <text x="40" y="72" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">KEY IDENTIFIER</text>
      <text x="280" y="72" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">INTERNAL SERVICE</text>
      <text x="520" y="72" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">SCOPES</text>
      <text x="760" y="72" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">RATE LIMIT</text>
      <text x="960" y="72" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">ROTATION</text>
      <text x="1110" y="72" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">STATUS</text>

      <!-- Row 1 -->
      <text x="40" y="116" fill="#06b6d4" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">key_prod_erp_ledger_01</text>
      <text x="280" y="116" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">ERP Ledger Reconciliation</text>
      <text x="520" y="116" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">completion:write, eval:read</text>
      <text x="760" y="116" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">10,000 RPM / 2M TPM</text>
      <text x="960" y="116" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">12 Days Remaining</text>
      <rect x="1100" y="102" width="60" height="20" rx="3" fill="#10b981" fill-opacity="0.15"/>
      <text x="1130" y="116" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="600" text-anchor="middle">ACTIVE</text>
      <line x1="24" y1="134" x2="1192" y2="134" stroke="#27272a" stroke-width="1"/>

      <!-- Row 2 -->
      <text x="40" y="162" fill="#06b6d4" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">key_prod_agentic_rag_02</text>
      <text x="280" y="162" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Corporate Knowledge RAG</text>
      <text x="520" y="162" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">embedding:create, chat:stream</text>
      <text x="760" y="162" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">25,000 RPM / 5M TPM</text>
      <text x="960" y="162" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">18 Days Remaining</text>
      <rect x="1100" y="148" width="60" height="20" rx="3" fill="#10b981" fill-opacity="0.15"/>
      <text x="1130" y="162" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="600" text-anchor="middle">ACTIVE</text>
      <line x1="24" y1="180" x2="1192" y2="180" stroke="#27272a" stroke-width="1"/>

      <!-- Row 3 -->
      <text x="40" y="208" fill="#06b6d4" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">key_prod_ecom_support_03</text>
      <text x="280" y="208" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Customer Copilot Agent</text>
      <text x="520" y="208" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">chat:stream, tools:invoke</text>
      <text x="760" y="208" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">15,000 RPM / 3M TPM</text>
      <text x="960" y="208" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">24 Days Remaining</text>
      <rect x="1100" y="194" width="60" height="20" rx="3" fill="#10b981" fill-opacity="0.15"/>
      <text x="1130" y="208" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="600" text-anchor="middle">ACTIVE</text>
      <line x1="24" y1="226" x2="1192" y2="226" stroke="#27272a" stroke-width="1"/>

      <!-- Row 4 -->
      <text x="40" y="254" fill="#06b6d4" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">key_prod_cms_seo_audit_04</text>
      <text x="280" y="254" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Editorial SEO Engine</text>
      <text x="520" y="254" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">completion:write</text>
      <text x="760" y="254" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">5,000 RPM / 1M TPM</text>
      <text x="960" y="254" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">29 Days Remaining</text>
      <rect x="1100" y="240" width="60" height="20" rx="3" fill="#10b981" fill-opacity="0.15"/>
      <text x="1130" y="254" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="600" text-anchor="middle">ACTIVE</text>
    </g>"""
    },
    "03-model-router-matrix.svg": {
        "title": "Intelligent Model Routing & Failover Matrix",
        "subtitle": "Dynamic Semantic Complexity Classifier with Cost-Optimized Fallback Cascades",
        "active": "Model Router",
        "url": "https://gateway.internal.mayastranawaloka.com/router",
        "content": """    <rect width="1280" height="780" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
    <text x="32" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="18" font-weight="600">Deterministic Prompt Complexity Router</text>
    <text x="32" y="68" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Requests under 15 token complexity route to Distilled 8B; multi-step analytical reasoning escalates to Speculative 70B</text>

    <!-- Router Diagram Panels -->
    <g transform="translate(32, 100)">
      <rect width="380" height="640" rx="6" fill="#16161a" stroke="#27272a"/>
      <text x="24" y="32" fill="#06b6d4" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">TIER 1: HIGH-THROUGHPUT</text>
      <text x="24" y="56" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="16" font-weight="600">Distilled 8B Model Cluster</text>
      <text x="24" y="80" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Sub-50ms latency, zero cold-start</text>
      <rect x="24" y="104" width="332" height="1" fill="#27272a"/>
      <text x="24" y="132" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Target Tasks:</text>
      <text x="24" y="156" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">- Entity extraction</text>
      <text x="24" y="180" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">- JSON format normalization</text>
      <text x="24" y="204" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">- Support ticket routing</text>
      <text x="24" y="228" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">- Semantic cache query parsing</text>

      <rect x="418" width="380" height="640" rx="6" fill="#16161a" stroke="#27272a"/>
      <text x="24" y="32" fill="#a855f7" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">TIER 2: REASONING ENGINE</text>
      <text x="24" y="56" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="16" font-weight="600">Speculative 32B CoT Node</text>
      <text x="24" y="80" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Multi-step mathematical reasoning</text>
      <rect x="24" y="104" width="332" height="1" fill="#27272a"/>
      <text x="24" y="132" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Target Tasks:</text>
      <text x="24" y="156" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">- Double-entry reconciliation</text>
      <text x="24" y="180" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">- Supply chain constraint solver</text>
      <text x="24" y="204" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">- Policy compliance checks</text>
      <text x="24" y="228" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">- AST code generation</text>

      <rect x="836" width="380" height="640" rx="6" fill="#16161a" stroke="#27272a"/>
      <text x="24" y="32" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">TIER 3: HEAVY FOUNDATION</text>
      <text x="24" y="56" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="16" font-weight="600">Dense 70B Frontier Cluster</text>
      <text x="24" y="80" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Exhaustive synthetic reasoning</text>
      <rect x="24" y="104" width="332" height="1" fill="#27272a"/>
      <text x="24" y="132" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Target Tasks:</text>
      <text x="24" y="156" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">- Legal contract synthesis</text>
      <text x="24" y="180" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">- Multi-document RAG summarization</text>
      <text x="24" y="204" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">- Edge-case dispute arbitration</text>
      <text x="24" y="228" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">- Architectural code refactoring</text>
    </g>"""
    },
    "04-prompt-eval-harness.svg": {
        "title": "Deterministic Prompt Evaluation Harness",
        "subtitle": "Automated Benchmark Test Suites, Grounding Scorers & Regression Detectors",
        "active": "Prompt Eval Harness",
        "url": "https://gateway.internal.mayastranawaloka.com/eval",
        "content": """    <rect width="1280" height="780" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
    <text x="32" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="18" font-weight="600">Automated Prompt Evaluation &amp; Grounding Suite</text>
    <text x="32" y="68" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Continuous regression test run against 5,000 ground-truth enterprise evaluation vectors</text>

    <!-- Score Gauges -->
    <g transform="translate(32, 100)">
      <rect width="280" height="110" rx="4" fill="#16161a" stroke="#27272a"/>
      <text x="20" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">FACTUAL GROUNDING SCORE</text>
      <text x="20" y="68" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="32" font-weight="700">99.82%</text>
      <text x="20" y="94" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Zero Hallucinations in Financial Domain</text>

      <rect x="310" width="280" height="110" rx="4" fill="#16161a" stroke="#27272a"/>
      <text x="330" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">FORMAT COMPLIANCE (JSON/AST)</text>
      <text x="330" y="68" fill="#06b6d4" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="32" font-weight="700">100.0%</text>
      <text x="330" y="94" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Pydantic / Zod Strict Schema Match</text>

      <rect x="620" width="280" height="110" rx="4" fill="#16161a" stroke="#27272a"/>
      <text x="640" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">CONTEXT RECALL (RAG)</text>
      <text x="640" y="68" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="32" font-weight="700">98.45%</text>
      <text x="640" y="94" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Top-3 Chunk Context Sufficiency</text>

      <rect x="930" width="280" height="110" rx="4" fill="#16161a" stroke="#27272a"/>
      <text x="950" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">SAFETY &amp; PII FILTERING</text>
      <text x="950" y="68" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="32" font-weight="700">100.0%</text>
      <text x="950" y="94" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Redaction on Ingestion &amp; Egress</text>
    </g>"""
    },
    "05-semantic-caching.svg": {
        "title": "Sub-Millisecond Semantic Vector Cache",
        "subtitle": "Cosine Similarity Threshold Matching with 41.8% Enterprise Cost Reduction",
        "active": "Semantic Cache",
        "url": "https://gateway.internal.mayastranawaloka.com/cache",
        "content": """    <rect width="1280" height="780" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
    <text x="32" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="18" font-weight="600">Vectorized Semantic Exact &amp; Approximate Cache</text>
    <text x="32" y="68" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">High-frequency queries resolve in under 6ms from local vector index without generating third-party API spend</text>
    
    <g transform="translate(32, 100)">
      <rect width="590" height="640" rx="6" fill="#16161a" stroke="#27272a"/>
      <text x="24" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="15" font-weight="600">Cache Similarity Thresholds</text>
      <text x="24" y="56" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Cosine distance cutoff: 0.945 (Strict Identity)</text>
      <line x1="24" y1="80" x2="566" y2="80" stroke="#27272a"/>
      <text x="24" y="112" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Cached Clusters: 842,100 Signatures</text>
      <text x="24" y="140" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Memory Footprint: 2.4 GB In-Memory HNSW</text>
      <text x="24" y="168" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Monthly Projected Savings: IDR 184,000,000</text>

      <rect x="626" width="590" height="640" rx="6" fill="#16161a" stroke="#27272a"/>
      <text x="24" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="15" font-weight="600">Live Invalidation Rules</text>
      <text x="24" y="56" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Automated cache purge on underlying database write</text>
      <line x1="24" y1="80" x2="566" y2="80" stroke="#27272a"/>
      <text x="24" y="112" fill="#06b6d4" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Event Hook: warehouse.stock.updated</text>
      <text x="24" y="140" fill="#06b6d4" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Event Hook: finance.invoice.reconciled</text>
      <text x="24" y="168" fill="#06b6d4" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Event Hook: editorial.article.published</text>
    </g>"""
    },
    "06-guardrails-firewall.svg": {
        "title": "AI Security Firewall & Prompt Injection Shield",
        "subtitle": "Real-Time PII Masking, Jailbreak Defense & Output Hallucination Interception",
        "active": "Security & Firewall",
        "url": "https://gateway.internal.mayastranawaloka.com/firewall",
        "content": """    <rect width="1280" height="780" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
    <text x="32" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="18" font-weight="600">Enterprise AI Boundary &amp; Defense Engine</text>
    <text x="32" y="68" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Bidirectional inspection pipeline: prompt injection sanitization before model egress, PII scrubbing before response transmission</text>

    <g transform="translate(32, 100)">
      <rect width="1216" height="640" rx="6" fill="#16161a" stroke="#27272a"/>
      <text x="24" y="36" fill="#06b6d4" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="700">BIDIRECTIONAL FIREWALL FILTER LAYERS</text>
      <text x="24" y="60" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Layer 1: Heuristic Token Entropy Analysis (Detection of base64 obfuscation)</text>
      <text x="24" y="84" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Layer 2: Adversarial Injection Classifier (Precision: 99.99%)</text>
      <text x="24" y="108" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Layer 3: Regex &amp; NER PII Redactor (NIK, Credit Card, Email, Passwords masked as [REDACTED])</text>
      <text x="24" y="132" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Layer 4: Structural Output Validator (Enforcing deterministic JSON schema boundaries)</text>
    </g>"""
    },
    "07-streaming-orchestrator.svg": {
        "title": "HTTP/2 Real-Time Streaming Orchestrator",
        "subtitle": "Server-Sent Events (SSE) Multiplexing & Smooth Sub-50ms Time-To-First-Token (TTFT)",
        "active": "Gateway Telemetry",
        "url": "https://gateway.internal.mayastranawaloka.com/stream",
        "content": """    <rect width="1280" height="780" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
    <text x="32" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="18" font-weight="600">Streaming Event Demultiplexer &amp; Backpressure Engine</text>
    <text x="32" y="68" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Handles thousands of concurrent token streams with zero buffer overflow using Linux epoll primitives</text>"""
    },
    "08-finetune-lora-registry.svg": {
        "title": "Enterprise Adapter & Checkpoint Registry",
        "subtitle": "Low-Rank Adaptation (LoRA) Weights, Version Rollbacks & Model Distillation Catalog",
        "active": "Model Router",
        "url": "https://gateway.internal.mayastranawaloka.com/lora",
        "content": """    <rect width="1280" height="780" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
    <text x="32" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="18" font-weight="600">Enterprise Model Weights &amp; Task-Specific LoRA Adapters</text>
    <text x="32" y="68" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Hot-swap 16-bit LoRA adapters at inference time without reloading base foundation model weights</text>"""
    },
    "09-quota-cost-allocation.svg": {
        "title": "Cost Center Allocation & Token Quota Governance",
        "subtitle": "Departmental Chargebacks, Budget Burn Rate Forecasts & Hard Spending Ceilings",
        "active": "Gateway Telemetry",
        "url": "https://gateway.internal.mayastranawaloka.com/budget",
        "content": """    <rect width="1280" height="780" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
    <text x="32" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="18" font-weight="600">Enterprise Token Budget &amp; Chargeback Ledger</text>
    <text x="32" y="68" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Automated rate-limiting and soft/hard spending caps allocated by cost center and application ID</text>"""
    },
    "10-audit-compliance-trail.svg": {
        "title": "Immutable Audit Log & Forensic Explorer",
        "subtitle": "Cryptographically Sealed SHA-256 Traces for Legal, Security & Financial Audits",
        "active": "Audit Logs",
        "url": "https://gateway.internal.mayastranawaloka.com/audit",
        "content": """    <rect width="1280" height="780" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
    <text x="32" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="18" font-weight="600">Cryptographic Request &amp; Token Audit Trail</text>
    <text x="32" y="68" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Every inference call is hashed with Merkle-tree verification for complete SOX, GDPR, and ISO-27001 auditability</text>"""
    },
    "11-synthetic-dataset-factory.svg": {
        "title": "Synthetic Dataset Factory & Grounding Distillation",
        "subtitle": "Automated Benchmark Generation, Monte Carlo Prompt Permutations & Self-Correction",
        "active": "Prompt Eval Harness",
        "url": "https://gateway.internal.mayastranawaloka.com/synthetic",
        "content": """    <rect width="1280" height="780" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
    <text x="32" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="18" font-weight="600">Automated Synthetic Data Generation &amp; Benchmark Distillation</text>
    <text x="32" y="68" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Generates high-diversity edge-case verification prompts to harden internal systems before production deployment</text>"""
    }
}

out_dir = "assets/projects/llm-gateway"
os.makedirs(out_dir, exist_ok=True)

# Generate master home SVG
master_svg_path = "assets/project-llm-gateway.svg"
master_content = wrap_svg(
    screens["01-gateway-telemetry.svg"]["content"],
    screens["01-gateway-telemetry.svg"]["active"],
    screens["01-gateway-telemetry.svg"]["title"],
    screens["01-gateway-telemetry.svg"]["subtitle"],
    screens["01-gateway-telemetry.svg"]["url"]
)
with open(master_svg_path, "w", encoding="utf-8") as f:
    f.write(master_content)
ET.fromstring(master_content)
print(f"Generated master {master_svg_path}")

# Generate all 11 screens
for fname, data in screens.items():
    if fname == "01-gateway-telemetry.svg":
        # Byte-for-byte identical to master
        full_svg = master_content
    else:
        full_svg = wrap_svg(data["content"], data["active"], data["title"], data["subtitle"], data["url"])
    
    # Validate XML
    ET.fromstring(full_svg)
    # Validate no banned dashes
    for b in ["—", "–", "&#8212;", "&mdash;"]:
        assert b not in full_svg, f"Banned dash in {fname}"
    
    path = os.path.join(out_dir, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(full_svg)
    print(f"Generated and validated {path}")

print("All 11 LLM Gateway screens successfully generated!")
