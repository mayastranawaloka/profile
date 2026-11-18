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
        ("Mission Control", 0),
        ("Multi-Agent DAG", 46),
        ("Vector RAG Index", 92),
        ("Sandbox Runner", 138),
        ("Tool Registry", 184),
        ("Memory Graph", 230),
        ("Safety &amp; Gates", 276),
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
  <!-- Brand in Agentic Ops -->
  <rect x="28" y="80" width="24" height="24" rx="4" fill="#ef4444"/>
  <circle cx="40" cy="92" r="3.5" fill="#fefefe"/>
  <text x="64" y="97" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="700" letter-spacing="1.5">AGENTIC OPS</text>

  <!-- Nav items -->
  <g transform="translate(24, 140)">
{menu_svg}  </g>

  <!-- Swarm Status at bottom sidebar -->
  <rect x="24" y="930" width="212" height="42" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
  <circle cx="48" cy="951" r="10" fill="#ef4444" fill-opacity="0.15"/>
  <circle cx="48" cy="951" r="4" fill="#ef4444"/>
  <text x="64" y="948" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Autonomous Swarm #04</text>
  <text x="64" y="961" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">34 Active Agent Threads</text>"""

# Helper to render monochrome top bar
def get_top_bar(title, subtitle, btn1_label="Export DAG", btn2_label="Deploy Agent"):
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
def wrap_svg(inner_content, active_name, title, subtitle, url="https://agentic.internal.mayastranawaloka.com/control"):
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
        badge_bg = "#27272a" if row['status'] in ["ACTIVE", "HEALTHY", "OPTIMAL", "PASSED", "VERIFIED", "CACHED", "MOUNTED", "COMPLETED", "NORMAL", "RUNNING", "APPROVED"] else "#1f1f23"
        badge_color = "#ffffff" if row['status'] in ["ACTIVE", "HEALTHY", "OPTIMAL", "PASSED", "VERIFIED", "CACHED", "MOUNTED", "COMPLETED", "NORMAL", "RUNNING", "APPROVED"] else "#a1a1aa"

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
      <text x="596" y="44" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Filter agent swarms...</text>

      <!-- Table Separator -->
      <line x1="24" y1="78" x2="796" y2="78" stroke="#27272a" stroke-width="1"/>

      <!-- Table Headers -->
{headers_svg}
      <line x1="24" y1="108" x2="796" y2="108" stroke="#1f1f23" stroke-width="1"/>

      <!-- Rows -->
{rows_svg}
      <!-- Table Pagination / Status Footer -->
      <line x1="24" y1="620" x2="796" y2="620" stroke="#27272a" stroke-width="1"/>
      <text x="24" y="646" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Showing 1 to 5 of active agent swarms</text>
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

# Define all 11 Agentic Ops screens with rich UI/UX features
screens = {
    "01-agentic-mission-control.svg": {
        "title": "Autonomous Swarm Mission Control",
        "subtitle": "Real-Time Multi-Agent Task Orchestration, Swarm Telemetry & Consensus Engine",
        "active": "Mission Control",
        "url": "https://agentic.internal.mayastranawaloka.com/control",
        "kpi": [
            {"label": "ACTIVE AUTONOMOUS SWARMS", "val": "34", "badge": "100% HEALTH", "sub": "Multi-Agent Parallel Execution"},
            {"label": "TOOL INVOCATION ACCURACY", "val": "99.4%", "badge": "0.01% FAIL", "sub": "Schema-Validated Function Calls"},
            {"label": "VECTOR KNOWLEDGE NODES", "val": "18.2M", "badge": "1536D NODES", "sub": "Sub-15ms Hybrid Dense Retrieval"},
            {"label": "CONCURRENT WORKFLOW RUNS", "val": "142", "badge": "ACTIVE DAG", "sub": "Zero Memory Leaks or Rogue Loops"},
        ],
        "table_title": "Active Autonomous Swarms & DAG Fleet",
        "table_sub": "Inspect live worker hierarchies, task status, tool invocation counts, and latency",
        "headers": ["SWARM ID", "PRIMARY OBJECTIVE", "AGENT SPECIALISTS", "TOOL CALLS", "LATENCY", "STATUS"],
        "rows": [
            {"c1": "SWARM-ALPHA-01", "c2": "End-to-End Financial Audit", "c3": "Planner + Coder + Critic", "c4": "42 tools", "c5": "4.2 s", "status": "RUNNING"},
            {"c1": "SWARM-BETA-04", "c2": "Warehouse Inventory Sync", "c3": "Ingestion + Verifier", "c4": "18 tools", "c5": "1.8 s", "status": "HEALTHY"},
            {"c1": "SWARM-GAMMA-02", "c2": "Automated Tax Reconciliation", "c3": "Legal Analyst + Auditor", "c4": "31 tools", "c5": "3.1 s", "status": "HEALTHY"},
            {"c1": "SWARM-DELTA-08", "c2": "Multi-Document OCR Parse", "c3": "Layout Parser + Tokenizer", "c4": "64 tools", "c5": "6.2 s", "status": "OPTIMAL"},
            {"c1": "SWARM-EPSILON-03", "c2": "Microservice Health Probe", "c3": "Sentinel Daemon", "c4": "12 tools", "c5": "0.9 s", "status": "HEALTHY"},
        ],
        "right_title": "Swarm Execution Topology & Tool Activity",
        "right_content": """        <!-- Swarm throughput sparkline -->
        <rect x="24" y="80" width="392" height="150" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
        <text x="40" y="104" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">SWARM EXECUTION VELOCITY</text>
        <text x="40" y="122" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Active tasks per minute across all nodes</text>
        <path d="M 40 195 L 80 180 L 120 185 L 160 165 L 200 172 L 240 155 L 280 160 L 320 140 L 360 148 L 400 130 L 400 215 L 40 215 Z" fill="url(#monoGrad)"/>
        <path d="M 40 195 L 80 180 L 120 185 L 160 165 L 200 172 L 240 155 L 280 160 L 320 140 L 360 148 L 400 130" fill="none" stroke="#ffffff" stroke-width="2"/>

        <!-- Capability boundary status -->
        <g transform="translate(24, 250)">
          <rect width="392" height="110" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <text x="16" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">CAPABILITY ACCESS BOUNDARY</text>
          <text x="16" y="52" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="20" font-weight="700">0 Egress Violations</text>
          <text x="16" y="74" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Zero trust network proxy / Local isolation active</text>
          <rect x="16" y="88" width="360" height="6" rx="3" fill="#27272a"/>
          <rect x="16" y="88" width="360" height="6" rx="3" fill="#ffffff"/>
        </g>

        <!-- Sandbox Runner Status -->
        <g transform="translate(24, 380)">
          <rect width="392" height="120" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <text x="16" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">GVISOR SANDBOX ISOLATION</text>
          <text x="16" y="48" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Ephemeral MicroVM Kernel Sandboxing</text>
          <text x="16" y="74" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">64 Sandboxes Sealed</text>
          <text x="16" y="94" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Zero root escapes / Strict 128MB RAM limit</text>
        </g>

        <!-- Human In The Loop Gate -->
        <g transform="translate(24, 520)">
          <rect width="392" height="120" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <text x="16" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">HUMAN-IN-THE-LOOP STATUS</text>
          <text x="16" y="48" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Threshold Approval Governance</text>
          <text x="16" y="74" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">3 Pending Review</text>
          <text x="16" y="94" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">High-stakes actions paused for manual signoff</text>
        </g>"""
    },
    "02-rag-vector-pipeline.svg": {
        "title": "Enterprise Vector RAG Pipeline",
        "subtitle": "HNSW Dense Embedding Index, Sparse BM25 Lexical Match & Reciprocal Rank Fusion",
        "active": "Vector RAG Index",
        "url": "https://agentic.internal.mayastranawaloka.com/rag",
        "kpi": [
            {"label": "INDEXED KNOWLEDGE CHUNKS", "val": "18.2M", "badge": "1536D CHUNKS", "sub": "Hierarchical Context Partitioning"},
            {"label": "RECALL PRECISION @ 10", "val": "99.8%", "badge": "HYBRID RRF", "sub": "Dense Semantic + BM25 Lexical Score"},
            {"label": "RETRIEVAL LATENCY", "val": "14ms", "badge": "HNSW INDEX", "sub": "In-Memory Cosine Similarity Match"},
            {"label": "VECTOR REFRESH CADENCE", "val": "CDC SYNC", "badge": "REAL-TIME", "sub": "Automated PostgreSQL CDC Pipeline"},
        ],
        "table_title": "Vector Knowledge Bases & Embedding Indexes",
        "table_sub": "Synchronizes millions of enterprise records into high-dimensional searchable vector embeddings",
        "headers": ["COLLECTION NAME", "DIMENSION", "TOTAL CHUNKS", "INDEX ENGINE", "p95 LATENCY", "STATUS"],
        "rows": [
            {"c1": "KB-Financial-Statements", "c2": "1536D Dense", "c3": "4.8M Chunks", "c4": "HNSW Cosine", "c5": "12 ms", "status": "ACTIVE"},
            {"c1": "KB-Warehouse-Manifests", "c2": "1536D Dense", "c3": "6.2M Chunks", "c4": "HNSW Cosine", "c5": "14 ms", "status": "ACTIVE"},
            {"c1": "KB-Legal-Contracts", "c2": "1536D Dense", "c3": "2.4M Chunks", "c4": "HNSW Cosine", "c5": "11 ms", "status": "ACTIVE"},
            {"c1": "KB-Technical-Manuals", "c2": "1536D Dense", "c3": "3.1M Chunks", "c4": "HNSW Cosine", "c5": "15 ms", "status": "ACTIVE"},
            {"c1": "KB-Product-Catalog", "c2": "1536D Dense", "c3": "1.7M Chunks", "c4": "HNSW Cosine", "c5": "9 ms", "status": "OPTIMAL"},
        ],
        "right_title": "Hybrid Search Engine & Reciprocal Rank Fusion",
        "right_content": """        <g transform="translate(24, 80)">
          <rect width="392" height="540" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <text x="20" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">RAG RETRIEVAL ARCHITECTURE</text>

          <text x="20" y="70" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Dense Vector Semantic Match (60%)</text>
          <text x="330" y="70" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">0.962</text>
          <rect x="20" y="80" width="352" height="6" rx="3" fill="#27272a"/>
          <rect x="20" y="80" width="338" height="6" rx="3" fill="#ffffff"/>

          <text x="20" y="114" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Sparse BM25 Lexical Keyword (40%)</text>
          <text x="330" y="114" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">0.948</text>
          <rect x="20" y="124" width="352" height="6" rx="3" fill="#27272a"/>
          <rect x="20" y="124" width="333" height="6" rx="3" fill="#ffffff"/>

          <line x1="20" y1="150" x2="372" y2="150" stroke="#27272a" stroke-width="1"/>

          <text x="20" y="180" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">CHUNK PARTITIONING STRATEGY</text>
          <text x="20" y="204" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Chunk Size: 512 Tokens | Overlap: 64 Tokens</text>
          <text x="20" y="224" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Preserves table structure and markdown headings</text>

          <g transform="translate(20, 250)">
            <rect width="352" height="150" rx="6" fill="#121215" stroke="#27272a" stroke-width="1"/>
            <text x="16" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">CROSS-ENCODER RERANKER</text>
            <text x="16" y="50" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Reranks top 50 candidates into top 5</text>
            <text x="16" y="74" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Precision Uplift: +14.2% Context Relevance</text>
            <text x="16" y="94" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Zero hallucinated context fed into prompt</text>
            <text x="16" y="114" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Sub-15ms reranker inference on local GPU</text>
          </g>
        </g>"""
    },
    "03-sandbox-code-runner.svg": {
        "title": "gVisor Secure Isolated Code Sandbox",
        "subtitle": "Ephemeral Container Runtimes, Memory Caps & Zero-Egress Network Blackhole",
        "active": "Sandbox Runner",
        "url": "https://agentic.internal.mayastranawaloka.com/sandbox",
        "kpi": [
            {"label": "ACTIVE EPHEMERAL RUNNERS", "val": "64", "badge": "MICRO-VM", "sub": "Isolated Kernel Space Architecture"},
            {"label": "HOST ESCAPE INCIDENTS", "val": "0", "badge": "ZERO ESCAPE", "sub": "100% Kernel Intercept Enforced"},
            {"label": "STRICT MEMORY CEILING", "val": "128MB", "badge": "CGROUPS", "sub": "OOM-Kill Enforced Instantly"},
            {"label": "NETWORK EGRESS STATE", "val": "BLACKHOLE", "badge": "OFFLINE", "sub": "Zero Host Socket Exposure Allowed"},
        ],
        "table_title": "Active Sandbox Runner Sessions & Isolation Metrics",
        "table_sub": "Dynamically executes agent-compiled code without risking host operating system integrity",
        "headers": ["RUNNER ID", "AGENT WORKER", "RUNTIME LANG", "CPU QUOTA", "MEMORY USED", "STATUS"],
        "rows": [
            {"c1": "RUN-0x882", "c2": "Python Data Analyzer", "c3": "Python 3.11", "c4": "0.5 Cores", "c5": "42 MB / 128MB", "status": "RUNNING"},
            {"c1": "RUN-0x771", "c2": "SQL Transformation Worker", "c3": "Go 1.22 Runtime", "c4": "0.2 Cores", "c5": "18 MB / 128MB", "status": "COMPLETED"},
            {"c1": "RUN-0x650", "c2": "Spreadsheet Formula Parser", "c3": "Node 20 Runtime", "c4": "0.4 Cores", "c5": "54 MB / 128MB", "status": "RUNNING"},
            {"c1": "RUN-0x529", "c2": "Financial Metric Compiler", "c3": "Rust Fast Runner", "c4": "0.1 Cores", "c5": "12 MB / 128MB", "status": "COMPLETED"},
            {"c1": "RUN-0x418", "c2": "Shell Safe Automation", "c3": "BusyBox Sandbox", "c4": "0.1 Cores", "c5": "8 MB / 128MB", "status": "COMPLETED"},
        ],
        "right_title": "Live Terminal Execution & Syscall Logs",
        "right_content": """        <g transform="translate(24, 80)">
          <rect width="392" height="540" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <text x="20" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">TERMINAL OUTPUT (STDOUT / STDERR)</text>

          <g transform="translate(20, 50)">
            <rect width="352" height="220" rx="4" fill="#111113" stroke="#27272a" stroke-width="1"/>
            <text x="16" y="26" fill="#71717a" font-family="monospace" font-size="11">$ python3 reconcile_variance.py</text>
            <text x="16" y="48" fill="#d4d4d8" font-family="monospace" font-size="11">[+] Loading 14,290 ledger records...</text>
            <text x="16" y="70" fill="#d4d4d8" font-family="monospace" font-size="11">[+] Validating double-entry balance: 0.00</text>
            <text x="16" y="92" fill="#ffffff" font-family="monospace" font-size="11">[OK] Variance checked: Zero anomalies.</text>
            <text x="16" y="114" fill="#a1a1aa" font-family="monospace" font-size="11">[+] Memory footprint: 42.1 MB</text>
            <text x="16" y="136" fill="#71717a" font-family="monospace" font-size="11">[+] Execution completed in 0.42s</text>
            <text x="16" y="160" fill="#ffffff" font-family="monospace" font-size="11">[+] Return code: 0 (Clean Exit)</text>
          </g>

          <g transform="translate(20, 290)">
            <rect width="352" height="150" rx="6" fill="#121215" stroke="#27272a" stroke-width="1"/>
            <text x="16" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">EPHEMERAL RUNNER LIFECYCLE</text>
            <text x="16" y="50" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">MicroVM Provisioning Time: 45 ms</text>
            <text x="16" y="74" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Destruction: Automatic on Process End</text>
            <text x="16" y="94" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Ephemeral storage purged; zero artifacts kept</text>
            <text x="16" y="114" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Host file system mounted read-only or blackholed</text>
          </g>
        </g>"""
    },
    "04-human-in-the-loop.svg": {
        "title": "Human-in-the-Loop Approval & Intervention Gate",
        "subtitle": "High-Stakes Transaction Verification, Risk Threshold Routing & Manual Override Telemetry",
        "active": "Safety & Gates",
        "url": "https://agentic.internal.mayastranawaloka.com/hitl",
        "kpi": [
            {"label": "PENDING INTERVENTIONS", "val": "3", "badge": "AWAITING", "sub": "High-Impact System Operations"},
            {"label": "AUTO-PASSED TRANSACTIONS", "val": "1,420", "badge": "99.8%", "sub": "Confidence Score Above Threshold"},
            {"label": "RISK THRESHOLD LIMIT", "val": "$25,000", "badge": "MANDATORY", "sub": "Requires Multi-Signature Approval"},
            {"label": "MEDIAN OPERATOR RESPONSE", "val": "4.2m", "badge": "SLA FAST", "sub": "Automated Escalation Dispatch"},
        ],
        "table_title": "Pending Intervention Queue & High-Stakes Operations",
        "table_sub": "Stops autonomous execution and requests verified supervisor approval for risky system actions",
        "headers": ["APPROVAL ID", "INITIATING SWARM", "TARGET OPERATION", "ESTIMATED VALUE", "RISK SCORE", "STATUS"],
        "rows": [
            {"c1": "HITL-0x9942", "c2": "Swarm-Fin-Reconcile", "c3": "Disburse Settlement Wire", "c4": "$42,500", "c5": "0.94 High Risk", "status": "PENDING"},
            {"c1": "HITL-0x9941", "c2": "Swarm-DB-Migrate", "c3": "Drop Deprecated Column", "c4": "Non-Monetary", "c5": "0.88 Med Risk", "status": "PENDING"},
            {"c1": "HITL-0x9940", "c2": "Swarm-Procurement", "c3": "Issue Auto PO #8812", "c4": "$18,900", "c5": "0.82 Med Risk", "status": "PENDING"},
            {"c1": "HITL-0x9939", "c2": "Swarm-Logistics-Hub", "c3": "Re-Route Fleet to Hub #02", "c4": "$4,200", "c5": "0.42 Low Risk", "status": "APPROVED"},
            {"c1": "HITL-0x9938", "c2": "Swarm-User-RBAC", "c3": "Grant Finance Lead Access", "c4": "Non-Monetary", "c5": "0.55 Low Risk", "status": "APPROVED"},
        ],
        "right_title": "Operator Action Drawer & Payload Inspector",
        "right_content": """        <g transform="translate(24, 80)">
          <rect width="392" height="540" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <text x="20" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">INSPECT SELECTED OPERATION</text>

          <g transform="translate(20, 50)">
            <rect width="352" height="150" rx="4" fill="#121215" stroke="#27272a" stroke-width="1"/>
            <text x="16" y="24" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">HITL-0x9942: Settlement Wire Disbursal</text>
            <text x="16" y="44" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Target: PT Mitra Logistik Utama (IDR 672.4M)</text>
            <text x="16" y="64" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Verification: 3-Way Invoice Match Verified 100%</text>
            <text x="16" y="84" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Agent Reasoning: Within approved budget quota</text>
            <text x="16" y="104" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Requires Officer Signoff (&gt; $25,000 threshold)</text>
          </g>

          <g transform="translate(20, 220)">
            <!-- Approve Button -->
            <rect width="352" height="38" rx="4" fill="#ffffff"/>
            <text x="176" y="24" fill="#09090b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600" text-anchor="middle">APPROVE &amp; DISPATCH OPERATION</text>

            <!-- Revise Button -->
            <rect y="48" width="352" height="36" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
            <text x="176" y="70" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">Revise Parameters with Agent</text>

            <!-- Reject Button -->
            <rect y="94" width="352" height="36" rx="4" fill="#27272a" stroke="#3f3f46" stroke-width="1"/>
            <text x="176" y="116" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="middle">REJECT &amp; HALT SWARM WORKFLOW</text>
          </g>

          <g transform="translate(20, 370)">
            <rect width="352" height="120" rx="6" fill="#121215" stroke="#27272a" stroke-width="1"/>
            <text x="16" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">AUDIT TRAIL LOGGING</text>
            <text x="16" y="50" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Operator Identity: Gilang Teja Krishna (CEO)</text>
            <text x="16" y="74" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Immutable Signature: Hardware Key Signed</text>
            <text x="16" y="94" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Recorded permanently in cryptographic ledger</text>
          </g>
        </g>"""
    },
    "05-agent-tool-registry.svg": {
        "title": "Dynamic Tool Definition & Capability Catalog",
        "subtitle": "OpenAPI Spec Function Calling, Runtime Schema Validation & Concurrency Throttling",
        "active": "Tool Registry",
        "url": "https://agentic.internal.mayastranawaloka.com/tools",
        "kpi": [
            {"label": "REGISTERED TOOLS", "val": "84", "badge": "OPENAPI SPEC", "sub": "Callable Microservice Endpoints"},
            {"label": "SCHEMA VALIDITY", "val": "99.7%", "badge": "STRICT JSON", "sub": "AST Syntactic Schema Verification"},
            {"label": "CONCURRENCY THROTTLE", "val": "10 req/s", "badge": "PER-SWARM", "sub": "Prevents Internal Service Floods"},
            {"label": "UNSCOPED CALLS", "val": "0", "badge": "ZERO LEAK", "sub": "Mandatory Scoped Token Boundary"},
        ],
        "table_title": "Enterprise Capability Catalog & Microservice Tools",
        "table_sub": "Exposes vetted backend endpoints as structured function definitions with parameter constraints",
        "headers": ["TOOL IDENTIFIER", "TARGET SERVICE", "FUNCTION SIGNATURE", "TIMEOUT", "PERMISSION", "STATUS"],
        "rows": [
            {"c1": "tool_query_stock", "c2": "Svc-Warehouse", "c3": "query_stock(sku: str)", "c4": "2.0 s", "c5": "Warehouse:Read", "status": "ACTIVE"},
            {"c1": "tool_post_journal", "c2": "Svc-Finance", "c3": "post_journal(data: obj)", "c4": "3.0 s", "c5": "Finance:Write", "status": "ACTIVE"},
            {"c1": "tool_issue_po", "c2": "Svc-Procurement", "c3": "create_po(po: obj)", "c4": "5.0 s", "c5": "Procurement:Write", "status": "ACTIVE"},
            {"c1": "tool_search_vector", "c2": "Svc-RAG-Engine", "c3": "search_db(q: str)", "c4": "1.0 s", "c5": "Vector:Read", "status": "ACTIVE"},
            {"c1": "tool_dispatch_email", "c2": "Svc-Notification", "c3": "send_alert(msg: str)", "c4": "2.5 s", "c5": "Notify:Write", "status": "ACTIVE"},
        ],
        "right_title": "OpenAPI Schema & Payload Definition",
        "right_content": """        <g transform="translate(24, 80)">
          <rect width="392" height="540" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <text x="20" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">FUNCTION SCHEMA SPECIFICATION</text>

          <g transform="translate(20, 50)">
            <rect width="352" height="230" rx="4" fill="#111113" stroke="#27272a" stroke-width="1"/>
            <text x="14" y="24" fill="#71717a" font-family="monospace" font-size="10">"name": "tool_post_journal",</text>
            <text x="14" y="44" fill="#ffffff" font-family="monospace" font-size="10">"description": "Post double-entry journal",</text>
            <text x="14" y="64" fill="#71717a" font-family="monospace" font-size="10">"parameters": {{</text>
            <text x="26" y="84" fill="#a1a1aa" font-family="monospace" font-size="10">"debit_account": {{ "type": "string" }},</text>
            <text x="26" y="104" fill="#a1a1aa" font-family="monospace" font-size="10">"credit_account": {{ "type": "string" }},</text>
            <text x="26" y="124" fill="#a1a1aa" font-family="monospace" font-size="10">"amount": {{ "type": "number" }},</text>
            <text x="26" y="144" fill="#a1a1aa" font-family="monospace" font-size="10">"reference_id": {{ "type": "string" }}</text>
            <text x="14" y="164" fill="#71717a" font-family="monospace" font-size="10">}},</text>
            <text x="14" y="184" fill="#ffffff" font-family="monospace" font-size="10">"required": ["debit", "credit", "amount"]</text>
          </g>

          <g transform="translate(20, 300)">
            <rect width="352" height="150" rx="6" fill="#121215" stroke="#27272a" stroke-width="1"/>
            <text x="16" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">INPUT VALIDATION PIPELINE</text>
            <text x="16" y="50" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">AST Type Validation: Enforced via Rust</text>
            <text x="16" y="74" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">100% Deterministic Parsing</text>
            <text x="16" y="94" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Rejects malformed JSON arguments before API dispatch</text>
            <text x="16" y="114" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Automatic retry hint generation for LLM recovery</text>
          </g>
        </g>"""
    },
    "06-long-term-memory-store.svg": {
        "title": "Episodic & Semantic Long-Term Memory Store",
        "subtitle": "Knowledge Graph Entity Resolution, Dynamic Working Memory & Cross-Session Persistence",
        "active": "Memory Graph",
        "url": "https://agentic.internal.mayastranawaloka.com/memory",
        "kpi": [
            {"label": "KNOWLEDGE GRAPH NODES", "val": "1.24M", "badge": "TRIPLES", "sub": "Entity-Relationship Graph Elements"},
            {"label": "EPISODIC SESSIONS", "val": "42,000", "badge": "INDEXED", "sub": "Multi-Day Workflow Context Kept"},
            {"label": "CONTEXT RECALL RELEVANCE", "val": "98.9%", "badge": "RELEVANT", "sub": "Zero Context Hallucinations"},
            {"label": "CROSS-SESSION TTL", "val": "PERMANENT", "badge": "PERSISTENT", "sub": "PostgreSQL Directed Property Graph"},
        ],
        "table_title": "Memory Graph Entity Triples & Episodic Records",
        "table_sub": "Maintains persistent operational understanding across discontinuous agent workflows",
        "headers": ["ENTITY ID", "CONCEPT TYPE", "RELATIONSHIP TARGET", "CONFIDENCE", "ACCESS COUNT", "STATUS"],
        "rows": [
            {"c1": "ENT-0x992", "c2": "Corporate Vendor", "c3": "PT Nusantara Distribusi", "c4": "99.8%", "c5": "1,420 hits", "status": "ACTIVE"},
            {"c1": "ENT-0x884", "c2": "Warehouse Facility", "c3": "Cikarang Central Hub #01", "c4": "99.5%", "c5": "2,890 hits", "status": "ACTIVE"},
            {"c1": "ENT-0x771", "c2": "Financial Account", "c3": "1100 Operational Cash", "c4": "100.0%", "c5": "4,120 hits", "status": "ACTIVE"},
            {"c1": "ENT-0x650", "c2": "Tax Classification", "c3": "PPN 11% Article 4 Law", "c4": "99.2%", "c5": "890 hits", "status": "ACTIVE"},
            {"c1": "ENT-0x529", "c2": "Procurement Policy", "c3": "Approval Threshold &gt; $25k", "c4": "100.0%", "c5": "3,450 hits", "status": "OPTIMAL"},
        ],
        "right_title": "Graph Traversal & Working Memory Topology",
        "right_content": """        <g transform="translate(24, 80)">
          <rect width="392" height="540" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <text x="20" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">DIRECTED PROPERTY GRAPH STATS</text>

          <text x="20" y="70" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Active Entity Nodes:</text>
          <text x="20" y="94" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="22" font-weight="700">1,240,892 Nodes</text>

          <text x="20" y="130" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Total Directed Edges:</text>
          <text x="20" y="154" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="22" font-weight="700">4,812,040 Edges</text>

          <line x1="20" y1="180" x2="372" y2="180" stroke="#27272a" stroke-width="1"/>

          <text x="20" y="210" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">WORKING MEMORY DECAY ENGINE</text>
          <text x="20" y="234" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Importance Weighting: Exponential Decay</text>
          <text x="20" y="254" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Critical policies retain 1.0 importance factor</text>

          <g transform="translate(20, 280)">
            <rect width="352" height="150" rx="6" fill="#121215" stroke="#27272a" stroke-width="1"/>
            <text x="16" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">CROSS-SESSION SYNC ENGINE</text>
            <text x="16" y="50" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Synchronizes state across days and weeks</text>
            <text x="16" y="74" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Immutable Postgres Property Store</text>
            <text x="16" y="94" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Agents resume long-horizon jobs seamlessly</text>
            <text x="16" y="114" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Zero cross-tenant memory leakage guaranteed</text>
          </g>
        </g>"""
    },
    "07-multi-agent-consensus.svg": {
        "title": "Multi-Agent Consensus & Majority Voting",
        "subtitle": "Swarm Cross-Examination, Self-Correction Loops & Adversarial Debate Synthesis",
        "active": "Multi-Agent DAG",
        "url": "https://agentic.internal.mayastranawaloka.com/consensus",
        "kpi": [
            {"label": "SYNTHESIS CONSENSUS", "val": "99.8%", "badge": "AGREED", "sub": "Cross-Agent Consensus Rate"},
            {"label": "MEDIAN DEBATE ROUNDS", "val": "3.2", "badge": "REFINED", "sub": "Refinement Cycles Before Decision"},
            {"label": "SPECIALIST WORKERS", "val": "4", "badge": "SWARM FLEET", "sub": "Planner, Coder, Critic, Judge"},
            {"label": "HALLUCINATIONS CAUGHT", "val": "148", "badge": "REFUTED", "sub": "Filtered by Adversarial Critic Agent"},
        ],
        "table_title": "Deliberation Sessions & Multi-Agent Verdicts",
        "table_sub": "Independent agents formulate hypotheses and cross-examine facts before committing actions",
        "headers": ["SESSION ID", "TASK OBJECTIVE", "PRIMARY HYPOTHESIS", "CRITIC VERDICT", "CONFIDENCE", "STATUS"],
        "rows": [
            {"c1": "DEBATE-0x994", "c2": "Reconcile Q3 Variance", "c3": "Allocation Misplaced", "c4": "REFUTED &gt; Corrected", "c5": "100.0%", "status": "VERIFIED"},
            {"c1": "DEBATE-0x993", "c2": "Optimize Delivery Route", "c3": "Hub Consolidation", "c4": "CONCURRED", "c5": "98.2%", "status": "VERIFIED"},
            {"c1": "DEBATE-0x992", "c2": "Validate PO Discount", "c3": "2% Early Payment", "c4": "CONCURRED", "c5": "100.0%", "status": "VERIFIED"},
            {"c1": "DEBATE-0x991", "c2": "Assess Credit Risk Ratio", "c3": "1.8x Working Capital", "c4": "REFUTED &gt; 1.4x", "c5": "96.4%", "status": "VERIFIED"},
            {"c1": "DEBATE-0x990", "c2": "Audit Code Patch Security", "c3": "Zero Memory Leak", "c4": "CONCURRED", "c5": "100.0%", "status": "VERIFIED"},
        ],
        "right_title": "Consensus Voting Weights & Debate Tree",
        "right_content": """        <g transform="translate(24, 80)">
          <rect width="392" height="540" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <text x="20" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">SWARM VOTING QUORUM WEIGHTS</text>

          <text x="20" y="70" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">1. Proposer Agent (Hypothesis)</text>
          <text x="330" y="70" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">1.0x</text>
          <rect x="20" y="80" width="352" height="6" rx="3" fill="#27272a"/>
          <rect x="20" y="80" width="176" height="6" rx="3" fill="#ffffff"/>

          <text x="20" y="114" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">2. Adversarial Critic (Cross-Exam)</text>
          <text x="330" y="114" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">1.5x</text>
          <rect x="20" y="124" width="352" height="6" rx="3" fill="#27272a"/>
          <rect x="20" y="124" width="264" height="6" rx="3" fill="#ffffff"/>

          <text x="20" y="158" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">3. Chief Judge (Synthesis Verdict)</text>
          <text x="330" y="158" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">2.0x</text>
          <rect x="20" y="168" width="352" height="6" rx="3" fill="#27272a"/>
          <rect x="20" y="168" width="352" height="6" rx="3" fill="#ffffff"/>

          <line x1="20" y1="196" x2="372" y2="196" stroke="#27272a" stroke-width="1"/>

          <text x="20" y="226" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">SELF-CORRECTION CONVERGENCE</text>
          <text x="20" y="250" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Requires 80% weighted agreement before committing</text>

          <g transform="translate(20, 270)">
            <rect width="352" height="150" rx="6" fill="#121215" stroke="#27272a" stroke-width="1"/>
            <text x="16" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">DEBATE ARTIFACT AUDIT</text>
            <text x="16" y="50" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Full debate transcripts preserved in audit trail</text>
            <text x="16" y="74" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Zero Black-Box Decisions</text>
            <text x="16" y="94" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Every deduction is traceable to concrete source files</text>
            <text x="16" y="114" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Adversarial testing eliminates ungrounded assumptions</text>
          </g>
        </g>"""
    },
    "08-document-ingestion-grid.svg": {
        "title": "Multi-Modal Document Parsing & Tokenizer Grid",
        "subtitle": "OCR Table Extraction, Financial Report Chunking & Markdown Structure Preservation",
        "active": "Vector RAG Index",
        "url": "https://agentic.internal.mayastranawaloka.com/ingestion",
        "kpi": [
            {"label": "INGESTION VELOCITY", "val": "14,800", "badge": "PAGES / HOUR", "sub": "Distributed Parallel Workers"},
            {"label": "TABLE CELL ACCURACY", "val": "99.4%", "badge": "OCR SPATIAL", "sub": "Exact Coordinate Preservation"},
            {"label": "SUPPORTED FORMATS", "val": "18", "badge": "MULTI-MODAL", "sub": "PDF, XLSX, DOCX, TIFF Scans"},
            {"label": "MARKDOWN STRUCTURE", "val": "100%", "badge": "SYNTAX VALID", "sub": "Preserves Hierarchy &amp; Headers"},
        ],
        "table_title": "Enterprise Ingestion Queue & Extraction Diagnostics",
        "table_sub": "Transforms unstructured PDFs, financial statements, and spreadsheets into structured knowledge",
        "headers": ["DOCUMENT NAME", "SOURCE TYPE", "PAGE COUNT", "EXTRACTED TABLES", "CHUNKS", "STATUS"],
        "rows": [
            {"c1": "Financial_Audit_Q3.pdf", "c2": "PDF (300 DPI)", "c3": "142 pages", "c4": "38 tables", "c5": "1,420 chunks", "status": "COMPLETED"},
            {"c1": "Warehouse_Manifest_Nov.xlsx", "c2": "Excel Workbook", "c3": "45 sheets", "c4": "45 tables", "c5": "2,890 chunks", "status": "COMPLETED"},
            {"c1": "Vendor_Procurement.pdf", "c2": "Scanned Contract", "c3": "88 pages", "c4": "14 tables", "c5": "890 chunks", "status": "COMPLETED"},
            {"c1": "Corporate_Tax_Filing.pdf", "c2": "Vector PDF", "c3": "210 pages", "c4": "62 tables", "c5": "3,120 chunks", "status": "COMPLETED"},
            {"c1": "Logistics_Fleet_Logs.csv", "c2": "Raw Data Feed", "c3": "1,200 rows", "c4": "1 table", "c5": "650 chunks", "status": "OPTIMAL"},
        ],
        "right_title": "Spatial Coordinate Grid & OCR Confidence",
        "right_content": """        <g transform="translate(24, 80)">
          <rect width="392" height="540" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <text x="20" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">SPATIAL TABLE PARSER METRICS</text>

          <text x="20" y="70" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Numeric Extraction Accuracy:</text>
          <text x="20" y="94" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="22" font-weight="700">99.8% Precision</text>

          <text x="20" y="130" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Header-Row Relationship Index:</text>
          <text x="20" y="154" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="22" font-weight="700">100% Retained</text>

          <line x1="20" y1="180" x2="372" y2="180" stroke="#27272a" stroke-width="1"/>

          <text x="20" y="210" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">BOUNDING BOX RESOLUTION</text>
          <text x="20" y="234" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Preserves spatial bounding box per cell</text>
          <text x="20" y="254" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Enables exact visual grounding in citation preview</text>

          <g transform="translate(20, 280)">
            <rect width="352" height="150" rx="6" fill="#121215" stroke="#27272a" stroke-width="1"/>
            <text x="16" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">VECTOR STORE EMBEDDING PIPELINE</text>
            <text x="16" y="50" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Embeds chunks immediately upon parsing</text>
            <text x="16" y="74" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">1536D Vectors Ingested into HNSW Index</text>
            <text x="16" y="94" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Available for swarm query in &lt; 500 ms</text>
            <text x="16" y="114" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Automated deduplication purges duplicate scans</text>
          </g>
        </g>"""
    },
    "09-agent-observability-traces.svg": {
        "title": "OpenTelemetry Distributed Trace Spans",
        "subtitle": "Step-by-Step Reasoning Latencies, Sub-Call Trees & Token Consumption Graphs",
        "active": "Mission Control",
        "url": "https://agentic.internal.mayastranawaloka.com/traces",
        "kpi": [
            {"label": "DISTRIBUTED TRACE COVERAGE", "val": "100%", "badge": "OTEL NATIVE", "sub": "Every Agent Step Captured"},
            {"label": "SPAN RESOLUTION", "val": "0.1ms", "badge": "SUB-MILLI", "sub": "Granular Execution Micro-Spans"},
            {"label": "AVERAGE SPANS PER TASK", "val": "14", "badge": "CALL TREE", "sub": "Root Goal to Terminal Conclusion"},
            {"label": "TOKEN USAGE ATTRIBUTION", "val": "100%", "badge": "TRACKED", "sub": "Cost Allocated Per Sub-Call"},
        ],
        "table_title": "Active Execution Traces & Hierarchical Spans",
        "table_sub": "Deep distributed trace trees capturing latency, token spend, and outcome for every reasoning step",
        "headers": ["TRACE ID", "ROOT GOAL", "EXECUTION HIERARCHY", "TOTAL TIME", "TOKEN SPEND", "STATUS"],
        "rows": [
            {"c1": "TRACE-0x992", "c2": "Quarterly Financial Close", "c3": "Plan &gt; Tool &gt; Eval", "c4": "2.6 s", "c5": "8,420 tokens", "status": "COMPLETED"},
            {"c1": "TRACE-0x884", "c2": "Stock Discrepancy Audit", "c3": "Plan &gt; Tool &gt; Conclude", "c4": "1.6 s", "c5": "3,890 tokens", "status": "COMPLETED"},
            {"c1": "TRACE-0x771", "c2": "Tax Compliance Check", "c3": "Plan &gt; Tool &gt; Eval", "c4": "3.7 s", "c5": "11,200 tokens", "status": "COMPLETED"},
            {"c1": "TRACE-0x650", "c2": "Automated Code Patch", "c3": "Plan &gt; Runner &gt; Test", "c4": "3.9 s", "c5": "14,800 tokens", "status": "COMPLETED"},
            {"c1": "TRACE-0x529", "c2": "Vendor Scoring Pipeline", "c3": "Plan &gt; Tool &gt; Conclude", "c4": "1.1 s", "c5": "2,450 tokens", "status": "OPTIMAL"},
        ],
        "right_title": "Interactive Trace Waterfall & Span Hierarchy",
        "right_content": """        <g transform="translate(24, 80)">
          <rect width="392" height="540" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <text x="20" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">REASONING SPAN TIMELINE (GANTT)</text>

          <text x="20" y="70" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">1. Root Task Decomp (Plan)</text>
          <text x="330" y="70" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">420 ms</text>
          <rect x="20" y="80" width="352" height="6" rx="3" fill="#27272a"/>
          <rect x="20" y="80" width="80" height="6" rx="3" fill="#ffffff"/>

          <text x="20" y="114" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">2. Tool Call: query_ledger()</text>
          <text x="330" y="114" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">840 ms</text>
          <rect x="20" y="124" width="352" height="6" rx="3" fill="#27272a"/>
          <rect x="100" y="124" width="160" height="6" rx="3" fill="#ffffff"/>

          <text x="20" y="158" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">3. Sandbox Code Verify</text>
          <text x="330" y="158" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">510 ms</text>
          <rect x="20" y="168" width="352" height="6" rx="3" fill="#27272a"/>
          <rect x="260" y="168" width="90" height="6" rx="3" fill="#ffffff"/>

          <line x1="20" y1="196" x2="372" y2="196" stroke="#27272a" stroke-width="1"/>

          <text x="20" y="226" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">CONTEXT MEMORY ALLOCATION</text>
          <text x="20" y="250" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Used: 8,420 Tokens / 128,000 Window (6.5%)</text>

          <g transform="translate(20, 270)">
            <rect width="352" height="150" rx="6" fill="#121215" stroke="#27272a" stroke-width="1"/>
            <text x="16" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">OPENTELEMETRY JAEGER COMPLIANT</text>
            <text x="16" y="50" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Exports to standard corporate observability stacks</text>
            <text x="16" y="74" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Trace Context W3C Header Propagation</text>
            <text x="16" y="94" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Pinpoints slow tools or runaway sub-agents instantly</text>
            <text x="16" y="114" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Zero unlogged execution branches in production</text>
          </g>
        </g>"""
    },
    "10-agent-security-boundary.svg": {
        "title": "Capability-Based Access Control (CapBAC)",
        "subtitle": "Zero-Trust Tool Isolation, Network Blackhole & Anti-Egress Boundary Enforcer",
        "active": "Safety & Gates",
        "url": "https://agentic.internal.mayastranawaloka.com/security",
        "kpi": [
            {"label": "PRIVILEGE ESCALATIONS", "val": "0", "badge": "ZERO ESCAPE", "sub": "Strict Boundary Intercept Enforced"},
            {"label": "CAPABILITY SCOPING", "val": "100%", "badge": "POLICIES ACTIVE", "sub": "Least Privilege Per Agent Role"},
            {"label": "ISOLATION RINGS", "val": "4", "badge": "RING 0-3", "sub": "Hardware Enforced Kernel Boundaries"},
            {"label": "NETWORK EGRESS", "val": "BLOCKED", "badge": "LOCAL ONLY", "sub": "Anti-Exfiltration Shield Active"},
        ],
        "table_title": "Security Ring Policies & Capability Scopes",
        "table_sub": "Enforces mathematically provable capability bounds; agents cannot exceed granted permissions",
        "headers": ["RING LEVEL", "AGENT FLEET GROUP", "PERMITTED SCOPES", "RESTRICTED OPS", "ENFORCER", "STATUS"],
        "rows": [
            {"c1": "Ring 0: Kernel", "c2": "Core Orchestrator", "c3": "Internal Memory", "c4": "All Host Calls Blocked", "c5": "STRICT", "status": "ACTIVE"},
            {"c1": "Ring 1: Planner", "c2": "Planner &amp; Critic", "c3": "Read-Only DB", "c4": "Zero Shell / WAN", "c5": "STRICT", "status": "ACTIVE"},
            {"c1": "Ring 2: Worker", "c2": "Microservice Caller", "c3": "Scoped REST APIs", "c4": "Raw DB Bypass Blocked", "c5": "STRICT", "status": "ACTIVE"},
            {"c1": "Ring 3: Sandbox", "c2": "Python Runner", "c3": "Ephemeral RAM", "c4": "Network Blackhole", "c5": "STRICT", "status": "ACTIVE"},
            {"c1": "Ring 3: Parser", "c2": "Document OCR", "c3": "Local Files Only", "c4": "Network Sockets Denied", "c5": "STRICT", "status": "OPTIMAL"},
        ],
        "right_title": "Zero-Trust Syscall Filter & Violation Monitor",
        "right_content": """        <g transform="translate(24, 80)">
          <rect width="392" height="540" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <text x="20" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">SECCOMP SYSCALL FILTER STATUS</text>

          <text x="20" y="70" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Allowed Syscalls (Read/Write Only)</text>
          <text x="330" y="70" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">100%</text>
          <rect x="20" y="80" width="352" height="6" rx="3" fill="#27272a"/>
          <rect x="20" y="80" width="352" height="6" rx="3" fill="#ffffff"/>

          <text x="20" y="114" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Restricted Syscalls (Socket/Execve)</text>
          <text x="330" y="114" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">BLOCKED</text>
          <rect x="20" y="124" width="352" height="6" rx="3" fill="#27272a"/>
          <rect x="20" y="124" width="352" height="6" rx="3" fill="#ffffff"/>

          <line x1="20" y1="150" x2="372" y2="150" stroke="#27272a" stroke-width="1"/>

          <text x="20" y="180" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">ANTI-EXFILTRATION NETWORK SHIELD</text>
          <text x="20" y="204" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Outbound Connections: Strictly Filtered</text>
          <text x="20" y="224" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Agents cannot initiate arbitrary external web requests</text>

          <g transform="translate(20, 250)">
            <rect width="352" height="150" rx="6" fill="#121215" stroke="#27272a" stroke-width="1"/>
            <text x="16" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">VIOLATION ENFORCEMENT ACTION</text>
            <text x="16" y="50" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Behavioral anomaly detection</text>
            <text x="16" y="74" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Instant SIGKILL on Unscoped Call</text>
            <text x="16" y="94" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Dispatches high-priority alert to corporate SOC</text>
            <text x="16" y="114" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Automated session freeze protects internal database</text>
          </g>
        </g>"""
    },
    "11-autonomous-scheduler.svg": {
        "title": "Autonomous Scheduled Swarms & Daemon Watchers",
        "subtitle": "Cron Event-Driven Agent Triggers, Exponential Backoff Retries & System Health Monitoring",
        "active": "Mission Control",
        "url": "https://agentic.internal.mayastranawaloka.com/scheduler",
        "kpi": [
            {"label": "SCHEDULED DAEMONS", "val": "24", "badge": "ACTIVE CRON", "sub": "Recurring Automated Swarms"},
            {"label": "SCHEDULE RELIABILITY", "val": "99.99%", "badge": "ZERO MISS", "sub": "On-Time Dispatch Guarantee"},
            {"label": "SELF-HEALING RETRIES", "val": "3 MAX", "badge": "EXP-BACKOFF", "sub": "Automated Fault Recovery Loop"},
            {"label": "DISTRIBUTED HEARTBEAT", "val": "100%", "badge": "HEALTHY", "sub": "Active Across All 4 Worker Nodes"},
        ],
        "table_title": "Scheduled Autonomous Jobs & Daemon Fleet",
        "table_sub": "Executes recurring system audits, inventory reconciliation, and background maintenance",
        "headers": ["JOB IDENTIFIER", "CRON SCHEDULE", "TARGET SWARM", "LAST RUN TIME", "DURATION", "STATUS"],
        "rows": [
            {"c1": "JOB-NIGHTLY-AUDIT", "c2": "00:00 Daily", "c3": "Swarm-Fin-Reconcile", "c4": "Today 00:00", "c5": "14m 28s", "status": "COMPLETED"},
            {"c1": "JOB-WAREHOUSE-SYNC", "c2": "*/15 * * * *", "c3": "Swarm-Logistics-Sync", "c4": "6 mins ago", "c5": "1m 12s", "status": "HEALTHY"},
            {"c1": "JOB-DB-INDEX-DEFRAG", "c2": "03:00 Sunday", "c3": "Swarm-DevOps-Sentinel", "c4": "Nov 10 03:00", "c5": "28m 40s", "status": "COMPLETED"},
            {"c1": "JOB-VECTOR-REFRESH", "c2": "01:00 Daily", "c3": "Swarm-RAG-Ingest", "c4": "Today 01:00", "c5": "42m 15s", "status": "COMPLETED"},
            {"c1": "JOB-HEALTH-HEARTBEAT", "c2": "*/1 * * * *", "c3": "Swarm-Health-Probe", "c4": "32 secs ago", "c5": "0m 04s", "status": "HEALTHY"},
        ],
        "right_title": "Daemon Execution Heartbeat & Consensus Engine",
        "right_content": """        <g transform="translate(24, 80)">
          <rect width="392" height="540" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
          <text x="20" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">SCHEDULER RAFT CONSENSUS</text>

          <text x="20" y="70" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Raft Leader Node:</text>
          <text x="20" y="94" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="20" font-weight="700">Cluster Node #01 (Active)</text>

          <text x="20" y="130" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Missed Heartbeats (90 Days):</text>
          <text x="20" y="154" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="20" font-weight="700">0 Missed Events</text>

          <line x1="20" y1="180" x2="372" y2="180" stroke="#27272a" stroke-width="1"/>

          <text x="20" y="210" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">UPCOMING SCHEDULED DISPATCHES</text>
          <text x="20" y="234" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">JOB-WAREHOUSE-SYNC: Next in 9 minutes</text>
          <text x="20" y="254" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">JOB-NIGHTLY-AUDIT: Next in 12 hours 25 mins</text>

          <g transform="translate(20, 280)">
            <rect width="352" height="150" rx="6" fill="#121215" stroke="#27272a" stroke-width="1"/>
            <text x="16" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">DAEMON WATCHDOG AGENT</text>
            <text x="16" y="50" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Self-monitoring supervisor process</text>
            <text x="16" y="74" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Automatic Failover to Node #02</text>
            <text x="16" y="94" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Heartbeat checked every 100 milliseconds</text>
            <text x="16" y="114" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Guarantees zero interrupted background audits</text>
          </g>
        </g>"""
    }
}

out_dir = "assets/projects/agentic-ops"
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
master_path = "assets/projects/showcases/project-agentic-ops.svg"
with open(os.path.join(out_dir, "01-agentic-mission-control.svg"), "r", encoding="utf-8") as f:
    master_content = f.read()

with open(master_path, "w", encoding="utf-8") as f:
    f.write(master_content)

print(f"Master {master_path} written byte-for-byte identical to 01-agentic-mission-control.svg")
