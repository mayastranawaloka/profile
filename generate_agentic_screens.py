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
    <rect x="16" y="{offset+14}" width="10" height="10" fill="#10b981"/>
    <text x="38" y="{offset+24}" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="500">{name}</text>\n"""
        else:
            menu_svg += f"""    <rect x="16" y="{offset+14}" width="10" height="10" fill="#52525b"/>
    <text x="38" y="{offset+24}" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">{name}</text>\n"""

    return f"""  <!-- Sidebar -->
  <rect x="0" y="52" width="260" height="948" fill="#0d0d10" stroke="#27272a" stroke-width="1"/>
  <!-- Brand in Agentic Ops -->
  <rect x="28" y="80" width="24" height="24" rx="4" fill="#10b981"/>
  <text x="64" y="97" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="700" letter-spacing="1.5">AGENTIC OPS</text>

  <!-- Nav items -->
  <g transform="translate(24, 140)">
{menu_svg}  </g>

  <!-- Swarm Status at bottom sidebar -->
  <rect x="24" y="930" width="212" height="42" rx="6" fill="#18181b" stroke="#27272a" stroke-width="1"/>
  <circle cx="48" cy="951" r="5" fill="#10b981"/>
  <text x="64" y="948" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Autonomous Swarm #04</text>
  <text x="64" y="961" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">34 Active Agent Threads</text>"""

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

    <rect x="1190" y="8" width="90" height="34" rx="4" fill="#10b981"/>
    <text x="1235" y="30" fill="#000000" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="middle">{btn2_label}</text>
  </g>"""

def wrap_svg(inner_content, active_name, title, subtitle, url="https://agentic.internal.mayastranawaloka.com/control"):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 1000" width="1600" height="1000">
  <defs>
    <linearGradient id="bgGlowAgent" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#070807"/>
      <stop offset="100%" stop-color="#0a0d0a"/>
    </linearGradient>
    <linearGradient id="emeraldGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#10b981" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#10b981" stop-opacity="0.0"/>
    </linearGradient>
  </defs>

  <rect width="1600" height="1000" fill="url(#bgGlowAgent)"/>

{get_browser_header(url)}
{get_sidebar(active_name)}
{get_top_bar(title, subtitle)}

  <!-- Main Content Body -->
  <g transform="translate(290, 150)">
{inner_content}
  </g>
</svg>"""

content_01 = """    <!-- 4 KPI Cards -->
    <g transform="translate(0, 0)">
      <rect width="300" height="96" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="20" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="500">ACTIVE AUTONOMOUS SWARMS</text>
      <text x="20" y="64" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="700">34</text>
      <text x="75" y="64" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">100% Healthy</text>
      <text x="20" y="82" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Multi-Agent Parallel Execution</text>

      <rect x="325" y="0" width="300" height="96" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="345" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="500">TOOL INVOCATION ACCURACY</text>
      <text x="345" y="64" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="700">99.94%</text>
      <text x="475" y="64" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Deterministic</text>
      <text x="345" y="82" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Schema Verified via AST Validator</text>

      <rect x="650" y="0" width="300" height="96" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="670" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="500">VECTOR RETRIEVAL SHARDS</text>
      <text x="670" y="64" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="700">14.8M</text>
      <text x="770" y="64" fill="#06b6d4" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">1536D Chunks</text>
      <text x="670" y="82" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Dense-Sparse Hybrid Re-ranking</text>

      <rect x="975" y="0" width="305" height="96" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="995" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="500">HUMAN ESCALATION RATE</text>
      <text x="995" y="64" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="700">0.06%</text>
      <text x="1105" y="64" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Autonomous</text>
      <text x="995" y="82" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">High Confidence Tool Automation</text>
    </g>

    <!-- Mid Section: Directed Acyclic Graph (DAG) & Tool Sandbox Terminal -->
    <g transform="translate(0, 116)">
      <!-- Left Panel: Multi-Agent DAG Visualizer -->
      <rect width="780" height="340" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="24" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="15" font-weight="600">Autonomous Reasoning DAG (Directed Acyclic Graph)</text>
      <text x="24" y="52" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Real-time trace of Swarm #04: Financial Audit &amp; Inventory Discrepancy Synthesis</text>

      <!-- DAG Node 1: Planner Agent -->
      <rect x="40" y="90" width="160" height="70" rx="4" fill="#16161a" stroke="#10b981" stroke-width="1.5"/>
      <circle cx="56" cy="110" r="4" fill="#10b981"/>
      <text x="68" y="114" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">Supervisor Planner</text>
      <text x="48" y="134" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Deconstruct goal: 4 steps</text>
      <text x="48" y="148" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Status: DONE (22ms)</text>

      <!-- Arrow 1 to 2 -->
      <line x1="200" y1="125" x2="250" y2="125" stroke="#10b981" stroke-width="1.5"/>
      <polygon points="250,121 258,125 250,129" fill="#10b981"/>

      <!-- DAG Node 2: Knowledge Vector Retriever -->
      <rect x="260" y="90" width="160" height="70" rx="4" fill="#16161a" stroke="#10b981" stroke-width="1.5"/>
      <circle cx="276" cy="110" r="4" fill="#10b981"/>
      <text x="288" y="114" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">RAG Retriever</text>
      <text x="268" y="134" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Fetched 12 ledger shards</text>
      <text x="268" y="148" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Similarity: 0.96 (18ms)</text>

      <!-- Arrow 2 to 3 -->
      <line x1="420" y1="125" x2="470" y2="125" stroke="#10b981" stroke-width="1.5"/>
      <polygon points="470,121 478,125 470,129" fill="#10b981"/>

      <!-- DAG Node 3: Isolated Code Sandbox -->
      <rect x="480" y="90" width="160" height="70" rx="4" fill="#16161a" stroke="#06b6d4" stroke-width="1.5"/>
      <circle cx="496" cy="110" r="4" fill="#06b6d4"/>
      <text x="508" y="114" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">Sandbox Runner</text>
      <text x="488" y="134" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Executing reconciliation.py</text>
      <text x="488" y="148" fill="#06b6d4" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Status: EXECUTING</text>

      <!-- Arrow 3 to 4 -->
      <line x1="640" y1="125" x2="680" y2="125" stroke="#52525b" stroke-width="1.5" stroke-dasharray="3,3"/>
      <polygon points="680,121 688,125 680,129" fill="#52525b"/>

      <!-- DAG Node 4: Critic & Grounding Verifier -->
      <rect x="480" y="210" width="160" height="70" rx="4" fill="#16161a" stroke="#27272a" stroke-width="1"/>
      <circle cx="496" cy="230" r="4" fill="#52525b"/>
      <text x="508" y="234" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">Critic Evaluator</text>
      <text x="488" y="254" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Waiting for code output</text>
      <text x="488" y="268" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Verification Pending</text>

      <!-- DAG Node 5: Output Synthesizer -->
      <rect x="260" y="210" width="160" height="70" rx="4" fill="#16161a" stroke="#27272a" stroke-width="1"/>
      <circle cx="276" cy="230" r="4" fill="#52525b"/>
      <text x="288" y="234" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">Final Synthesizer</text>
      <text x="268" y="254" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Executive summary drafting</text>
      <text x="268" y="268" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10">Status: QUEUED</text>

      <!-- Connecting loop line from 3 to 4 -->
      <path d="M 560 160 L 560 210" fill="none" stroke="#52525b" stroke-width="1.5" stroke-dasharray="3,3"/>
      <!-- Connecting line from 4 to 5 -->
      <line x1="480" y1="245" x2="420" y2="245" stroke="#52525b" stroke-width="1.5" stroke-dasharray="3,3"/>

      <!-- Right Panel: Ephemeral Sandbox Tool Console -->
      <rect x="805" width="475" height="340" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="825" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="15" font-weight="600">Ephemeral Tool Sandbox Runner</text>
      <text x="825" y="52" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">gVisor Linux Sandboxing (Network: Isolated None)</text>

      <rect x="825" y="72" width="435" height="248" rx="4" fill="#0a0a0d" stroke="#1f1f23"/>
      <text x="840" y="96" fill="#10b981" font-family="monospace" font-size="11">$ gvisor-sandbox run --timeout 30s --mem 256M</text>
      <text x="840" y="118" fill="#71717a" font-family="monospace" font-size="11">[INIT] Spawning isolated runtime environment...</text>
      <text x="840" y="138" fill="#71717a" font-family="monospace" font-size="11">[INPUT] Loading /mnt/data/ledger_snapshot_q4.parquet</text>
      <text x="840" y="158" fill="#06b6d4" font-family="monospace" font-size="11">[TOOL] Invoking tool: calculate_balance_variance()</text>
      <text x="840" y="178" fill="#ffffff" font-family="monospace" font-size="11">   Reconciling 14,820 double-entry journals...</text>
      <text x="840" y="198" fill="#ffffff" font-family="monospace" font-size="11">   Variance found: IDR 0.00 (Perfect Match)</text>
      <text x="840" y="218" fill="#ffffff" font-family="monospace" font-size="11">   Audit Trail Hash: e3b0c44298fc1c149afbf4c8996fb92427ae</text>
      <text x="840" y="240" fill="#10b981" font-family="monospace" font-size="11">[EXIT] Process terminated with returncode: 0 (OK)</text>
      <text x="840" y="260" fill="#71717a" font-family="monospace" font-size="11">[CLEANUP] Destroyed ephemeral memory sandbox</text>
      <text x="840" y="282" fill="#10b981" font-family="monospace" font-size="11">[TELEMETRY] Execution time: 142ms / CPU cap: 42%</text>
    </g>

    <!-- Bottom Section: Active Autonomous Tool Registry & Vector Shards -->
    <g transform="translate(0, 480)">
      <rect width="1280" height="300" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="24" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="15" font-weight="600">Enterprise Agent Tool Registry &amp; Capability Boundaries</text>
      <text x="24" y="52" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Strict OpenAPI function definitions with automated argument sanitization and human approval gating</text>

      <!-- Table Header -->
      <rect x="24" y="70" width="1232" height="34" rx="4" fill="#16161a"/>
      <text x="44" y="92" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">TOOL DECLARATION</text>
      <text x="320" y="92" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">ISOLATION MODE</text>
      <text x="560" y="92" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">SCHEMA VERIFICATION</text>
      <text x="780" y="92" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">24H INVOCATIONS</text>
      <text x="980" y="92" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">HUMAN GATE</text>
      <text x="1160" y="92" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">STATUS</text>

      <!-- Row 1 -->
      <g transform="translate(24, 112)">
        <text x="20" y="22" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">erp_query_warehouse_inventory()</text>
        <text x="296" y="22" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Read-Only SQL Replica</text>
        <text x="536" y="22" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Strict Pydantic AST (0 Errs)</text>
        <text x="756" y="22" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">84,120 calls</text>
        <text x="956" y="22" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Autonomous</text>
        <rect x="1136" y="8" width="60" height="20" rx="3" fill="#10b981" fill-opacity="0.15"/>
        <text x="1166" y="22" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="600" text-anchor="middle">ACTIVE</text>
        <line x1="0" y1="36" x2="1232" y2="36" stroke="#1f1f23" stroke-width="1"/>
      </g>

      <!-- Row 2 -->
      <g transform="translate(24, 156)">
        <text x="20" y="22" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">erp_post_journal_entry()</text>
        <text x="296" y="22" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Double-Entry Transaction</text>
        <text x="536" y="22" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Cryptographic Signing</text>
        <text x="756" y="22" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">4,280 calls</text>
        <rect x="946" y="8" width="90" height="20" rx="3" fill="#f59e0b" fill-opacity="0.15"/>
        <text x="991" y="22" fill="#f59e0b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="600" text-anchor="middle">ESCALATE &gt; 50M</text>
        <rect x="1136" y="8" width="60" height="20" rx="3" fill="#10b981" fill-opacity="0.15"/>
        <text x="1166" y="22" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="600" text-anchor="middle">ACTIVE</text>
        <line x1="0" y1="36" x2="1232" y2="36" stroke="#1f1f23" stroke-width="1"/>
      </g>

      <!-- Row 3 -->
      <g transform="translate(24, 200)">
        <text x="20" y="22" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">sandbox_python_executor()</text>
        <text x="296" y="22" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">gVisor Ephemeral Container</text>
        <text x="536" y="22" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Static AST Security Lint</text>
        <text x="756" y="22" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">18,450 runs</text>
        <text x="956" y="22" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Autonomous</text>
        <rect x="1136" y="8" width="60" height="20" rx="3" fill="#10b981" fill-opacity="0.15"/>
        <text x="1166" y="22" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="600" text-anchor="middle">ACTIVE</text>
        <line x1="0" y1="36" x2="1232" y2="36" stroke="#1f1f23" stroke-width="1"/>
      </g>

      <!-- Row 4 -->
      <g transform="translate(24, 244)">
        <text x="20" y="22" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">vector_hybrid_search()</text>
        <text x="296" y="22" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">HNSW + BM25 Reciprocal Rank</text>
        <text x="536" y="22" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Cosine Threshold &gt; 0.85</text>
        <text x="756" y="22" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">142,800 queries</text>
        <text x="956" y="22" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Autonomous</text>
        <rect x="1136" y="8" width="60" height="20" rx="3" fill="#10b981" fill-opacity="0.15"/>
        <text x="1166" y="22" fill="#10b981" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="600" text-anchor="middle">ACTIVE</text>
      </g>
    </g>"""

screens = {
    "01-agentic-mission-control.svg": {
        "title": "Autonomous Agentic Mission Control",
        "subtitle": "Multi-Agent Swarm Orchestration, Deterministic Tool Sandbox & Live Vector RAG Synthesis",
        "active": "Mission Control",
        "url": "https://agentic.internal.mayastranawaloka.com/control",
        "content": content_01
    },
    "02-rag-vector-pipeline.svg": {
        "title": "Hybrid Dense-Sparse Vector RAG Pipeline",
        "subtitle": "1536D Semantic Embeddings, BM25 Lexical Matching & Reciprocal Rank Fusion",
        "active": "Vector RAG Index",
        "url": "https://agentic.internal.mayastranawaloka.com/rag",
        "content": """    <rect width="1280" height="780" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
    <text x="32" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="18" font-weight="600">Multi-Stage Retrieval-Augmented Generation (RAG) Architecture</text>
    <text x="32" y="68" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Combines dense cosine vectors with BM25 keyword precision, passing top-50 results through neural re-ranking</text>"""
    },
    "03-sandbox-code-runner.svg": {
        "title": "Ephemeral Container Code Runner",
        "subtitle": "gVisor Linux Sandboxing, Pyodide WASM Runtime & Network Isolation Blackhole",
        "active": "Sandbox Runner",
        "url": "https://agentic.internal.mayastranawaloka.com/sandbox",
        "content": """    <rect width="1280" height="780" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
    <text x="32" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="18" font-weight="600">Isolated Code Execution Environment</text>
    <text x="32" y="68" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Autonomous agents execute calculations and data transformations in sandboxes with zero host file access</text>"""
    },
    "04-human-in-the-loop.svg": {
        "title": "Critical Action Human-in-the-Loop Gate",
        "subtitle": "Dual-Approval Authorization, High-Value Transaction Escalation & Risk Confidence Gauges",
        "active": "Safety & Gates",
        "url": "https://agentic.internal.mayastranawaloka.com/approval",
        "content": """    <rect width="1280" height="780" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
    <text x="32" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="18" font-weight="600">Human-in-the-Loop Approval &amp; Governance Center</text>
    <text x="32" y="68" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">High-impact database mutations require explicit supervisor sign-off before state commitment</text>"""
    },
    "05-agent-tool-registry.svg": {
        "title": "OpenAPI Agent Tool Registry & Schema Validator",
        "subtitle": "Strict Pydantic Type Checking, Automatic Argument Sanitization & Latency Budgets",
        "active": "Tool Registry",
        "url": "https://agentic.internal.mayastranawaloka.com/tools",
        "content": """    <rect width="1280" height="780" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
    <text x="32" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="18" font-weight="600">Dynamic Tool Definition &amp; Capability Catalog</text>
    <text x="32" y="68" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Centralized registry exposing enterprise microservice endpoints as structured callable LLM functions</text>"""
    },
    "06-long-term-memory-store.svg": {
        "title": "Episodic & Semantic Long-Term Memory Store",
        "subtitle": "Knowledge Graph Entity Resolution, Dynamic Working Memory & Cross-Session Persistence",
        "active": "Memory Graph",
        "url": "https://agentic.internal.mayastranawaloka.com/memory",
        "content": """    <rect width="1280" height="780" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
    <text x="32" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="18" font-weight="600">Hierarchical Agent Working &amp; Episodic Memory Graph</text>
    <text x="32" y="68" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Maintains long-horizon operational context across enterprise multi-department workflows</text>"""
    },
    "07-multi-agent-consensus.svg": {
        "title": "Multi-Agent Consensus & Majority Voting",
        "subtitle": "Swarm Cross-Examination, Self-Correction Loops & Adversarial Debate Synthesis",
        "active": "Multi-Agent DAG",
        "url": "https://agentic.internal.mayastranawaloka.com/consensus",
        "content": """    <rect width="1280" height="780" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
    <text x="32" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="18" font-weight="600">Multi-Agent Swarm Deliberation &amp; Verification</text>
    <text x="32" y="68" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Parallel worker agents formulate independent hypotheses; critic agent synthesizes final verifiable judgment</text>"""
    },
    "08-document-ingestion-grid.svg": {
        "title": "Multi-Modal Document Parsing & Tokenizer Grid",
        "subtitle": "OCR Table Extraction, Financial Report Chunking & Markdown Structure Preservation",
        "active": "Vector RAG Index",
        "url": "https://agentic.internal.mayastranawaloka.com/ingestion",
        "content": """    <rect width="1280" height="780" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
    <text x="32" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="18" font-weight="600">High-Throughput Enterprise Document Ingestion</text>
    <text x="32" y="68" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Extracts structured data from multi-page PDFs, balance sheets, and technical diagrams with spatial awareness</text>"""
    },
    "09-agent-observability-traces.svg": {
        "title": "OpenTelemetry Distributed Trace Spans",
        "subtitle": "Step-by-Step Reasoning Latencies, Sub-Call Trees & Token Consumption Graphs",
        "active": "Mission Control",
        "url": "https://agentic.internal.mayastranawaloka.com/traces",
        "content": """    <rect width="1280" height="780" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
    <text x="32" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="18" font-weight="600">Real-Time OpenTelemetry Distributed Agent Tracing</text>
    <text x="32" y="68" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Inspect sub-millisecond timelines for every prompt dispatch, tool invocation, and vector lookup</text>"""
    },
    "10-agent-security-boundary.svg": {
        "title": "Capability-Based Access Control (CapBAC)",
        "subtitle": "Zero-Trust Tool Isolation, Network Blackhole & Anti-Egress Boundary Enforcer",
        "active": "Safety & Gates",
        "url": "https://agentic.internal.mayastranawaloka.com/security",
        "content": """    <rect width="1280" height="780" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
    <text x="32" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="18" font-weight="600">Zero-Trust Capability Boundary &amp; Sandboxed Isolation</text>
    <text x="32" y="68" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Agents cannot exceed scoped credentials; outbound network requests strictly filtered by egress proxy</text>"""
    },
    "11-autonomous-scheduler.svg": {
        "title": "Autonomous Scheduled Swarms & Daemon Watchers",
        "subtitle": "Cron Event-Driven Agent Triggers, Exponential Backoff Retries & System Health Monitoring",
        "active": "Mission Control",
        "url": "https://agentic.internal.mayastranawaloka.com/scheduler",
        "content": """    <rect width="1280" height="780" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
    <text x="32" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="18" font-weight="600">Recurring Autonomous Agent Jobs &amp; Daemon Watchers</text>
    <text x="32" y="68" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Runs overnight ledger audits, automated warehouse reconciliation, and proactive database maintenance</text>"""
    }
}

out_dir = "assets/projects/agentic-ops"
os.makedirs(out_dir, exist_ok=True)

# Generate master home SVG
master_svg_path = "assets/project-agentic-ops.svg"
master_content = wrap_svg(
    screens["01-agentic-mission-control.svg"]["content"],
    screens["01-agentic-mission-control.svg"]["active"],
    screens["01-agentic-mission-control.svg"]["title"],
    screens["01-agentic-mission-control.svg"]["subtitle"],
    screens["01-agentic-mission-control.svg"]["url"]
)
with open(master_svg_path, "w", encoding="utf-8") as f:
    f.write(master_content)
ET.fromstring(master_content)
print(f"Generated master {master_svg_path}")

# Generate all 11 screens
for fname, data in screens.items():
    if fname == "01-agentic-mission-control.svg":
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

print("All 11 Agentic Ops screens successfully generated!")
