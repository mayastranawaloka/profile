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

def get_pulse_sidebar(active_name="Articles &amp; Posts"):
    items = [
        ("Dashboard", 0),
        ("Articles &amp; Posts", 46),
        ("Media Library", 92),
        ("Categories &amp; Tags", 138),
        ("Editorial Calendar", 184),
        ("SEO Diagnostics", 230),
        ("Team &amp; Roles", 276),
        ("System Settings", 322)
    ]
    menu_svg = ""
    for name, offset in items:
        raw_name = name.replace("&amp;", "&")
        if raw_name == active_name or name == active_name:
            menu_svg += f"""    <rect x="0" y="{offset}" width="202" height="38" rx="6" fill="#ffffff" fill-opacity="0.08"/>
    <rect x="16" y="{offset+14}" width="10" height="10" fill="#ffffff"/>
    <text x="38" y="{offset+24}" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">{name}</text>\n"""
        else:
            menu_svg += f"""    <rect x="16" y="{offset+14}" width="10" height="10" fill="#52525b"/>
    <text x="38" y="{offset+24}" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">{name}</text>\n"""

    return f"""  <!-- Sidebar -->
  <rect x="0" y="52" width="250" height="948" fill="#0c0c0e" stroke="#27272a" stroke-width="1"/>
  <rect x="28" y="82" width="18" height="18" rx="4" fill="#ef4444"/>
  <circle cx="37" cy="91" r="3" fill="#fefefe"/>
  <text x="56" y="96" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="15" font-weight="800" letter-spacing="2">PULSE CMS</text>

  <g transform="translate(24, 140)">
{menu_svg}  </g>"""

def get_pulse_top_bar(breadcrumb, btn1="Save Draft", btn2="Publish Live"):
    return f"""  <!-- Editorial Top Bar -->
  <g transform="translate(280, 80)">
    <text x="0" y="24" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">{breadcrumb}</text>
    <rect x="850" y="4" width="110" height="34" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
    <text x="905" y="26" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="middle">{btn1}</text>

    <rect x="975" y="4" width="110" height="34" rx="4" fill="#ef4444"/>
    <text x="1030" y="26" fill="#fefefe" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" text-anchor="middle">{btn2}</text>
  </g>"""

def build_cms_svg(url, active_nav, breadcrumb, btn1, btn2, content_svg):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 1000" width="1600" height="1000" fill="none">
  <!-- Background -->
  <rect width="1600" height="1000" fill="#09090b"/>

{get_browser_header(url)}

{get_pulse_sidebar(active_nav)}

{get_pulse_top_bar(breadcrumb, btn1, btn2)}

{content_svg}
</svg>"""

cms_screens = {}

# -------------------------------------------------------------
# Screen 1: Editorial Markdown Workspace (100% Home Master Parity)
# -------------------------------------------------------------
with open("assets/projects/showcases/project-cms.svg", "r", encoding="utf-8") as f:
    cms_screens["01-editorial-workspace.svg"] = f.read()

# -------------------------------------------------------------
# Screen 2: Unified Content Repository
# -------------------------------------------------------------
cms_screens["02-content-repository.svg"] = build_cms_svg(
    url="https://cms.mayastranawaloka.com/articles",
    active_nav="Articles &amp; Posts",
    breadcrumb="Content Repository / All Articles (1,248 entries)",
    btn1="Export CSV",
    btn2="+ New Article",
    content_svg="""  <!-- Content Repository Area -->
  <g transform="translate(280, 140)">
    <!-- Top Filter Bar -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="400" height="42" rx="4" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="16" y="26" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Search articles by title, author, slug...</text>

      <!-- Filter tabs -->
      <g transform="translate(430, 0)">
        <rect x="0" y="0" width="90" height="42" rx="4" fill="#ffffff"/>
        <text x="45" y="26" fill="#09090b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" text-anchor="middle">All (1,248)</text>

        <rect x="100" y="0" width="115" height="42" rx="4" fill="#111114" stroke="#27272a" stroke-width="1"/>
        <text x="157" y="26" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="middle">Published (824)</text>

        <rect x="225" y="0" width="95" height="42" rx="4" fill="#111114" stroke="#27272a" stroke-width="1"/>
        <text x="272" y="26" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="middle">Drafts (312)</text>

        <rect x="330" y="0" width="115" height="42" rx="4" fill="#111114" stroke="#27272a" stroke-width="1"/>
        <text x="387" y="26" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="middle">In Review (112)</text>

        <rect x="455" y="0" width="140" height="42" rx="4" fill="#111114" stroke="#27272a" stroke-width="1"/>
        <text x="525" y="26" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="middle">Desk: All Desks v</text>
      </g>
    </g>

    <!-- Table Container -->
    <rect x="0" y="60" width="1280" height="760" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>

    <!-- Table Header -->
    <rect x="0" y="60" width="1280" height="44" fill="#151518" stroke="#27272a" stroke-width="1"/>
    <text x="24" y="88" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700">TITLE &amp; SLUG</text>
    <text x="500" y="88" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700">CATEGORY</text>
    <text x="700" y="88" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700">AUTHOR</text>
    <text x="860" y="88" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700">READ TIME</text>
    <text x="960" y="88" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700">VIEWS</text>
    <text x="1080" y="88" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700">STATUS</text>
    <text x="1200" y="88" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700">ACTIONS</text>

    <!-- Row 1 -->
    <g transform="translate(0, 104)">
      <line x1="0" y1="84" x2="1280" y2="84" stroke="#1f1f23" stroke-width="1"/>
      <text x="24" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Architectural Minimalist Systems for Mid-Market Enterprise 2026</text>
      <text x="24" y="54" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">/insights/architectural-minimalist-systems</text>
      <text x="500" y="44" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Enterprise Architecture</text>
      <text x="700" y="44" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Editorial Board</text>
      <text x="860" y="44" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">6 min</text>
      <text x="960" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">24,910</text>
      <rect x="1080" y="28" width="80" height="24" rx="4" fill="#ffffff" fill-opacity="0.12"/>
      <text x="1120" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Published</text>
      <text x="1200" y="44" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Edit | View</text>
    </g>

    <!-- Row 2 -->
    <g transform="translate(0, 188)">
      <line x1="0" y1="84" x2="1280" y2="84" stroke="#1f1f23" stroke-width="1"/>
      <text x="24" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Zero-Latency State Management in Modern Frontends</text>
      <text x="24" y="54" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">/insights/zero-latency-state-management</text>
      <text x="500" y="44" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Software Engineering</text>
      <text x="700" y="44" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Lead Engineer</text>
      <text x="860" y="44" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">8 min</text>
      <text x="960" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">18,420</text>
      <rect x="1080" y="28" width="80" height="24" rx="4" fill="#ffffff" fill-opacity="0.12"/>
      <text x="1120" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Published</text>
      <text x="1200" y="44" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Edit | View</text>
    </g>

    <!-- Row 3 -->
    <g transform="translate(0, 272)">
      <line x1="0" y1="84" x2="1280" y2="84" stroke="#1f1f23" stroke-width="1"/>
      <text x="24" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Multi-Region PostgreSQL Sharding: A Practical Field Guide</text>
      <text x="24" y="54" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">/insights/multi-region-postgres-sharding</text>
      <text x="500" y="44" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Cloud Infrastructure</text>
      <text x="700" y="44" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">DevOps Lead</text>
      <text x="860" y="44" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">11 min</text>
      <text x="960" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">32,150</text>
      <rect x="1080" y="28" width="80" height="24" rx="4" fill="#ffffff" fill-opacity="0.12"/>
      <text x="1120" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Published</text>
      <text x="1200" y="44" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Edit | View</text>
    </g>

    <!-- Row 4 -->
    <g transform="translate(0, 356)">
      <line x1="0" y1="84" x2="1280" y2="84" stroke="#1f1f23" stroke-width="1"/>
      <text x="24" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Microservices vs Modular Monolith: The 2026 Verdict</text>
      <text x="24" y="54" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">/drafts/microservices-vs-modular-monolith</text>
      <text x="500" y="44" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Enterprise Architecture</text>
      <text x="700" y="44" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Chief Architect</text>
      <text x="860" y="44" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">9 min</text>
      <text x="960" y="44" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">-</text>
      <rect x="1080" y="28" width="80" height="24" rx="4" fill="#27272a"/>
      <text x="1120" y="44" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="middle">In Review</text>
      <text x="1200" y="44" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Review</text>
    </g>

    <!-- Row 5 -->
    <g transform="translate(0, 440)">
      <line x1="0" y1="84" x2="1280" y2="84" stroke="#1f1f23" stroke-width="1"/>
      <text x="24" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Secure Supply Chain Hygiene for Node &amp; Rust Projects</text>
      <text x="24" y="54" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">/drafts/secure-supply-chain-hygiene</text>
      <text x="500" y="44" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Security &amp; Governance</text>
      <text x="700" y="44" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">SecOps Specialist</text>
      <text x="860" y="44" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">5 min</text>
      <text x="960" y="44" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">-</text>
      <rect x="1080" y="28" width="80" height="24" rx="4" fill="#18181c" stroke="#27272a" stroke-width="1"/>
      <text x="1120" y="44" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">Draft</text>
      <text x="1200" y="44" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Edit</text>
    </g>

    <!-- Row 6 -->
    <g transform="translate(0, 524)">
      <line x1="0" y1="84" x2="1280" y2="84" stroke="#1f1f23" stroke-width="1"/>
      <text x="24" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Design Token Architecture for Cross-Platform Teams</text>
      <text x="24" y="54" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">/insights/design-token-architecture</text>
      <text x="500" y="44" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Design Systems</text>
      <text x="700" y="44" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">UI/UX Principal</text>
      <text x="860" y="44" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">7 min</text>
      <text x="960" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">14,830</text>
      <rect x="1080" y="28" width="80" height="24" rx="4" fill="#ffffff" fill-opacity="0.12"/>
      <text x="1120" y="44" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Published</text>
      <text x="1200" y="44" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Edit | View</text>
    </g>

    <!-- Pagination Footer -->
    <g transform="translate(24, 715)">
      <text x="0" y="24" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Showing 1-6 of 1,248 entries</text>
      <g transform="translate(1000, 0)">
        <rect x="0" y="0" width="32" height="32" rx="4" fill="#ffffff"/>
        <text x="16" y="21" fill="#09090b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1</text>
        <rect x="40" y="0" width="32" height="32" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
        <text x="56" y="21" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="middle">2</text>
        <rect x="80" y="0" width="32" height="32" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
        <text x="96" y="21" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="middle">3</text>
        <rect x="120" y="0" width="60" height="32" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
        <text x="150" y="21" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="middle">Next</text>
      </g>
    </g>
  </g>"""
)

# -------------------------------------------------------------
# Screen 3: Real-Time SEO & Meta Engine
# -------------------------------------------------------------
cms_screens["03-seo-optimizer.svg"] = build_cms_svg(
    url="https://cms.mayastranawaloka.com/seo/diagnostics/8901",
    active_nav="SEO Diagnostics",
    breadcrumb="SEO Diagnostics / Automated Audit / Post #8901",
    btn1="Re-run Audit",
    btn2="Apply Changes",
    content_svg="""  <!-- SEO Area -->
  <g transform="translate(280, 140)">
    <!-- 4 Metric Cards -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="300" height="96" rx="4" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="24" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">OVERALL SEO INDEX</text>
      <text x="24" y="66" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="800">98 / 100</text>
      <text x="200" y="66" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">GRADE A+</text>

      <rect x="326" y="0" width="300" height="96" rx="4" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="350" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">READABILITY SCORE</text>
      <text x="350" y="66" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="26" font-weight="800">68.4 Flesch</text>
      <text x="510" y="66" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Standard Flow</text>

      <rect x="652" y="0" width="300" height="96" rx="4" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="676" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">KEYWORD DENSITY</text>
      <text x="676" y="66" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="26" font-weight="800">2.4% Focus</text>
      <text x="830" y="66" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">14 Mentions</text>

      <rect x="978" y="0" width="302" height="96" rx="4" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="1002" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">CORE WEB VITALS</text>
      <text x="1002" y="66" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="24" font-weight="800">LCP 0.8s</text>
      <text x="1140" y="66" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">CLS 0.01 Fast</text>
    </g>

    <!-- Split Panels -->
    <!-- Left: SERP Preview & Open Graph -->
    <g transform="translate(0, 116)">
      <rect x="0" y="0" width="760" height="704" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="24" y="36" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="700">SEARCH ENGINE &amp; SOCIAL PREVIEW</text>
      <line x1="24" y1="52" x2="736" y2="52" stroke="#27272a" stroke-width="1"/>

      <!-- SERP Snippet Box -->
      <text x="24" y="85" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Google Desktop SERP Snippet Preview</text>
      <rect x="24" y="100" width="712" height="150" rx="4" fill="#18181c" stroke="#27272a" stroke-width="1"/>
      <text x="44" y="132" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">https://mayastranawaloka.com &gt; insights &gt; architectural-minimalist-systems</text>
      <text x="44" y="160" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="18" font-weight="700">Architectural Minimalist Systems for Mid-Market Enterprise 2026</text>
      <text x="44" y="190" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Explore production-grade minimalist systems design for mid-market businesses. Discover zero-latency content delivery, deterministic state, and enterprise architecture.</text>
      <text x="44" y="230" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Title: 58 / 60 chars (Optimal) | Description: 152 / 160 chars (Optimal)</text>

      <!-- Social Card Preview -->
      <text x="24" y="285" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Open Graph Social Meta Card (Twitter/X &amp; LinkedIn)</text>
      <rect x="24" y="300" width="712" height="360" rx="4" fill="#18181c" stroke="#27272a" stroke-width="1"/>
      <rect x="44" y="320" width="672" height="200" rx="4" fill="#121215" stroke="#ef4444" stroke-opacity="0.4" stroke-width="1"/>
      <circle cx="380" cy="400" r="30" fill="#ef4444" fill-opacity="0.25" stroke="#ef4444" stroke-width="1.5"/>
      <text x="380" y="450" fill="#ef4444" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600" text-anchor="middle">og:image [1200x630 High Density Asset Verified]</text>
      <text x="44" y="555" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="16" font-weight="700">Architectural Minimalist Systems for Mid-Market Enterprise 2026</text>
      <text x="44" y="585" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">mayastranawaloka.com - 6 min read - PT Mayastra Nawaloka Nusantara</text>
      <text x="44" y="630" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Twitter Card: summary_large_image | og:type: article | twitter:site: @mayastranawaloka</text>
    </g>

    <!-- Right: Heuristics Checklist -->
    <g transform="translate(786, 116)">
      <rect x="0" y="0" width="494" height="704" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="24" y="36" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="700">HEURISTICS AUDIT (10 / 10 PASS)</text>
      <line x1="24" y1="52" x2="470" y2="52" stroke="#27272a" stroke-width="1"/>

      <!-- Checklist Items -->
      <g transform="translate(24, 75)">
        <rect x="0" y="0" width="54" height="24" rx="4" fill="#ffffff" fill-opacity="0.12"/>
        <text x="27" y="16" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" text-anchor="middle">PASS</text>
        <text x="68" y="16" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Primary keyword in Title and H1 tag</text>

        <rect x="0" y="48" width="54" height="24" rx="4" fill="#ffffff" fill-opacity="0.12"/>
        <text x="27" y="64" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" text-anchor="middle">PASS</text>
        <text x="68" y="64" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Keyword appears in first 100 words</text>

        <rect x="0" y="96" width="54" height="24" rx="4" fill="#ffffff" fill-opacity="0.12"/>
        <text x="27" y="112" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" text-anchor="middle">PASS</text>
        <text x="68" y="112" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">All 4 images possess descriptive alt text</text>

        <rect x="0" y="144" width="54" height="24" rx="4" fill="#ffffff" fill-opacity="0.12"/>
        <text x="27" y="160" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" text-anchor="middle">PASS</text>
        <text x="68" y="160" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Internal links ratio optimal (6 verified links)</text>

        <rect x="0" y="192" width="54" height="24" rx="4" fill="#ffffff" fill-opacity="0.12"/>
        <text x="27" y="208" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" text-anchor="middle">PASS</text>
        <text x="68" y="208" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Outbound authority reference cited</text>

        <rect x="0" y="240" width="54" height="24" rx="4" fill="#ffffff" fill-opacity="0.12"/>
        <text x="27" y="256" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" text-anchor="middle">PASS</text>
        <text x="68" y="256" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Canonical URL tag configured correctly</text>

        <rect x="0" y="288" width="54" height="24" rx="4" fill="#ffffff" fill-opacity="0.12"/>
        <text x="27" y="304" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" text-anchor="middle">PASS</text>
        <text x="68" y="304" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Structured JSON-LD TechArticle valid</text>

        <rect x="0" y="336" width="54" height="24" rx="4" fill="#ffffff" fill-opacity="0.12"/>
        <text x="27" y="352" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" text-anchor="middle">PASS</text>
        <text x="68" y="352" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Mobile touch targets meet 48px baseline</text>

        <rect x="0" y="384" width="54" height="24" rx="4" fill="#ffffff" fill-opacity="0.12"/>
        <text x="27" y="400" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" text-anchor="middle">PASS</text>
        <text x="68" y="400" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Zero broken hyperlinks or redirect loops</text>

        <rect x="0" y="432" width="54" height="24" rx="4" fill="#ffffff" fill-opacity="0.12"/>
        <text x="27" y="448" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" text-anchor="middle">PASS</text>
        <text x="68" y="448" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Flesch-Kincaid readability grade 11.2</text>
      </g>
    </g>
  </g>"""
)

# -------------------------------------------------------------
# Screen 4: Digital Asset & Media Library
# -------------------------------------------------------------
cms_screens["04-media-library.svg"] = build_cms_svg(
    url="https://cms.mayastranawaloka.com/media",
    active_nav="Media Library",
    breadcrumb="Media Library / Global Assets (4,892 files - 18.4 GB)",
    btn1="Batch Optimize",
    btn2="+ Upload Media",
    content_svg="""  <!-- Media Library Area -->
  <g transform="translate(280, 140)">
    <!-- Top Filter & Storage Row -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="360" height="42" rx="4" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="16" y="26" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Search media by filename, alt text...</text>

      <g transform="translate(390, 0)">
        <rect x="0" y="0" width="90" height="42" rx="4" fill="#ffffff"/>
        <text x="45" y="26" fill="#09090b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" text-anchor="middle">All Assets</text>

        <rect x="100" y="0" width="120" height="42" rx="4" fill="#111114" stroke="#27272a" stroke-width="1"/>
        <text x="160" y="26" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="middle">Images (3,840)</text>

        <rect x="230" y="0" width="110" height="42" rx="4" fill="#111114" stroke="#27272a" stroke-width="1"/>
        <text x="285" y="26" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="middle">Vectors (820)</text>

        <rect x="350" y="0" width="110" height="42" rx="4" fill="#111114" stroke="#27272a" stroke-width="1"/>
        <text x="405" y="26" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="middle">Docs (232)</text>
      </g>

      <!-- Storage Meter -->
      <g transform="translate(940, 0)">
        <rect x="0" y="0" width="340" height="42" rx="4" fill="#111114" stroke="#27272a" stroke-width="1"/>
        <text x="16" y="26" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Storage: 18.4 / 50 GB (36%)</text>
        <rect x="180" y="16" width="140" height="10" rx="5" fill="#27272a"/>
        <rect x="180" y="16" width="50" height="10" rx="5" fill="#ffffff"/>
      </g>
    </g>

    <!-- Main Grid (Left) -->
    <g transform="translate(0, 60)">
      <rect x="0" y="0" width="870" height="760" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>

      <!-- Asset Card 1 (Selected) -->
      <g transform="translate(24, 24)">
        <rect x="0" y="0" width="258" height="220" rx="4" fill="#18181c" stroke="#ef4444" stroke-width="2"/>
        <rect x="12" y="12" width="234" height="130" rx="3" fill="#121215"/>
        <circle cx="129" cy="77" r="28" fill="#ef4444" fill-opacity="0.85"/>
        <text x="12" y="170" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">hero-architecture-2026.webp</text>
        <text x="12" y="195" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">1920x1080 - 148.6 KB - WebP</text>
      </g>

      <!-- Asset Card 2 -->
      <g transform="translate(306, 24)">
        <rect x="0" y="0" width="258" height="220" rx="4" fill="#18181c" stroke="#27272a" stroke-width="1"/>
        <rect x="12" y="12" width="234" height="130" rx="3" fill="#121215"/>
        <rect x="110" y="58" width="38" height="38" fill="#ef4444" fill-opacity="0.85"/>
        <text x="12" y="170" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">diagram-kubernetes-mesh.svg</text>
        <text x="12" y="195" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Vector Scalable - 42.1 KB</text>
      </g>

      <!-- Asset Card 3 -->
      <g transform="translate(588, 24)">
        <rect x="0" y="0" width="258" height="220" rx="4" fill="#18181c" stroke="#27272a" stroke-width="1"/>
        <rect x="12" y="12" width="234" height="130" rx="3" fill="#121215"/>
        <circle cx="129" cy="77" r="28" fill="#ef4444" fill-opacity="0.85"/>
        <text x="12" y="170" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">founder-keynote-tech.webp</text>
        <text x="12" y="195" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">2400x1600 - 320.4 KB - WebP</text>
      </g>

      <!-- Asset Card 4 -->
      <g transform="translate(24, 268)">
        <rect x="0" y="0" width="258" height="220" rx="4" fill="#18181c" stroke="#27272a" stroke-width="1"/>
        <rect x="12" y="12" width="234" height="130" rx="3" fill="#121215"/>
        <circle cx="129" cy="77" r="28" fill="#ef4444" fill-opacity="0.85"/>
        <text x="12" y="170" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">server-rack-datacenter.webp</text>
        <text x="12" y="195" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">1920x1080 - 210.8 KB - WebP</text>
      </g>

      <!-- Asset Card 5 -->
      <g transform="translate(306, 268)">
        <rect x="0" y="0" width="258" height="220" rx="4" fill="#18181c" stroke="#27272a" stroke-width="1"/>
        <rect x="12" y="12" width="234" height="130" rx="3" fill="#121215"/>
        <rect x="110" y="58" width="38" height="38" fill="#ef4444" fill-opacity="0.85"/>
        <text x="12" y="170" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">system-topology-v4.svg</text>
        <text x="12" y="195" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Vector Scalable - 64.2 KB</text>
      </g>

      <!-- Asset Card 6 -->
      <g transform="translate(588, 268)">
        <rect x="0" y="0" width="258" height="220" rx="4" fill="#18181c" stroke="#27272a" stroke-width="1"/>
        <rect x="12" y="12" width="234" height="130" rx="3" fill="#121215"/>
        <text x="129" y="82" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="16" font-weight="700" text-anchor="middle">PDF</text>
        <text x="12" y="170" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">brand-guidelines-v2.pdf</text>
        <text x="12" y="195" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">Document - 1.8 MB</text>
      </g>
    </g>

    <!-- Right Inspector Panel -->
    <g transform="translate(896, 60)">
      <rect x="0" y="0" width="384" height="760" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="24" y="36" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="700">SELECTED ASSET INSPECTOR</text>
      <line x1="24" y1="52" x2="360" y2="52" stroke="#27272a" stroke-width="1"/>

      <!-- Large Preview Box -->
      <rect x="24" y="70" width="336" height="180" rx="4" fill="#18181c" stroke="#27272a" stroke-width="1"/>
      <circle cx="192" cy="160" r="40" fill="#ef4444" fill-opacity="0.85"/>

      <!-- Metadata Fields -->
      <text x="24" y="285" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">FILE NAME</text>
      <text x="24" y="308" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">hero-architecture-2026.webp</text>

      <text x="24" y="345" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">SPECIFICATIONS</text>
      <text x="24" y="368" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">1920 x 1080 px | 148.6 KB | WebP 92Q</text>
      <text x="24" y="390" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Compressed from 3.2 MB raw master</text>

      <text x="24" y="430" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">ACCESSIBILITY ALT TEXT</text>
      <rect x="24" y="445" width="336" height="60" rx="4" fill="#18181c" stroke="#27272a" stroke-width="1"/>
      <text x="36" y="470" fill="#e4e4e7" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Enterprise server architecture blueprint with</text>
      <text x="36" y="490" fill="#e4e4e7" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">high-availability edge cluster topology.</text>

      <text x="24" y="535" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">GLOBAL CDN PERMALINK</text>
      <rect x="24" y="550" width="336" height="36" rx="4" fill="#18181c" stroke="#27272a" stroke-width="1"/>
      <text x="36" y="573" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">https://cdn.mayastra.id/media/hero-arch.webp</text>

      <!-- Action Buttons -->
      <rect x="24" y="615" width="336" height="40" rx="4" fill="#ffffff"/>
      <text x="192" y="640" fill="#09090b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Copy CDN URL to Clipboard</text>

      <rect x="24" y="665" width="336" height="40" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
      <text x="192" y="690" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="middle">Replace Asset &amp; Invalidate Cache</text>
    </g>
  </g>"""
)

# -------------------------------------------------------------
# Screen 5: Multi-Stage Editorial Workflow (Kanban)
# -------------------------------------------------------------
cms_screens["05-publishing-workflow.svg"] = build_cms_svg(
    url="https://cms.mayastranawaloka.com/workflow/kanban",
    active_nav="Editorial Calendar",
    breadcrumb="Editorial Workflow / Kanban Production Pipeline",
    btn1="Filter: All Desks",
    btn2="+ Add Assignment",
    content_svg="""  <!-- Kanban Area -->
  <g transform="translate(280, 140)">
    <!-- Column 1: Ideation -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="305" height="820" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <rect x="0" y="0" width="305" height="44" fill="#151518" stroke="#27272a" stroke-width="1"/>
      <text x="20" y="27" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">1. IDEATION &amp; PITCH</text>
      <rect x="255" y="10" width="32" height="24" rx="4" fill="#27272a"/>
      <text x="271" y="26" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="middle">5</text>

      <!-- Card 1 -->
      <g transform="translate(16, 60)">
        <rect x="0" y="0" width="273" height="150" rx="4" fill="#18181c" stroke="#27272a" stroke-width="1"/>
        <rect x="16" y="16" width="60" height="20" rx="3" fill="#ffffff" fill-opacity="0.1"/>
        <text x="46" y="30" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="700" text-anchor="middle">AI / DATA</text>
        <text x="16" y="60" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Vector DB Indexing at</text>
        <text x="16" y="80" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Enterprise Scale</text>
        <text x="16" y="125" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Lead: R. Kusuma - Due Nov 18</text>
      </g>

      <!-- Card 2 -->
      <g transform="translate(16, 226)">
        <rect x="0" y="0" width="273" height="150" rx="4" fill="#18181c" stroke="#27272a" stroke-width="1"/>
        <rect x="16" y="16" width="70" height="20" rx="3" fill="#ffffff" fill-opacity="0.1"/>
        <text x="51" y="30" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="700" text-anchor="middle">SECURITY</text>
        <text x="16" y="60" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Zero-Trust Network</text>
        <text x="16" y="80" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Access in Hybrid Cloud</text>
        <text x="16" y="125" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Lead: A. Dimas - Due Nov 20</text>
      </g>
    </g>

    <!-- Column 2: Drafting -->
    <g transform="translate(325, 0)">
      <rect x="0" y="0" width="305" height="820" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <rect x="0" y="0" width="305" height="44" fill="#151518" stroke="#27272a" stroke-width="1"/>
      <text x="20" y="27" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">2. WRITING &amp; DRAFT</text>
      <rect x="255" y="10" width="32" height="24" rx="4" fill="#27272a"/>
      <text x="271" y="26" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="middle">8</text>

      <!-- Card 1 -->
      <g transform="translate(16, 60)">
        <rect x="0" y="0" width="273" height="150" rx="4" fill="#18181c" stroke="#27272a" stroke-width="1"/>
        <rect x="16" y="16" width="90" height="20" rx="3" fill="#ffffff" fill-opacity="0.1"/>
        <text x="61" y="30" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="700" text-anchor="middle">ARCHITECTURE</text>
        <text x="16" y="60" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Microservices vs Modular</text>
        <text x="16" y="80" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Monolith 2026</text>
        <text x="16" y="125" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">1,200 words - Author: C. Arch</text>
      </g>

      <!-- Card 2 -->
      <g transform="translate(16, 226)">
        <rect x="0" y="0" width="273" height="150" rx="4" fill="#18181c" stroke="#27272a" stroke-width="1"/>
        <rect x="16" y="16" width="60" height="20" rx="3" fill="#ffffff" fill-opacity="0.1"/>
        <text x="46" y="30" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="700" text-anchor="middle">DEVOPS</text>
        <text x="16" y="60" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">High-Throughput Logging</text>
        <text x="16" y="80" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">with Rust &amp; Vector</text>
        <text x="16" y="125" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">850 words - Author: Lead Eng</text>
      </g>
    </g>

    <!-- Column 3: Review -->
    <g transform="translate(650, 0)">
      <rect x="0" y="0" width="305" height="820" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <rect x="0" y="0" width="305" height="44" fill="#151518" stroke="#27272a" stroke-width="1"/>
      <text x="20" y="27" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">3. EDITORIAL REVIEW</text>
      <rect x="255" y="10" width="32" height="24" rx="4" fill="#27272a"/>
      <text x="271" y="26" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="middle">4</text>

      <!-- Card 1 -->
      <g transform="translate(16, 60)">
        <rect x="0" y="0" width="273" height="150" rx="4" fill="#18181c" stroke="#27272a" stroke-width="1"/>
        <rect x="16" y="16" width="70" height="20" rx="3" fill="#ffffff" fill-opacity="0.1"/>
        <text x="51" y="30" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="700" text-anchor="middle">SECURITY</text>
        <text x="16" y="60" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Secure Supply Chain</text>
        <text x="16" y="80" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Hygiene for Node &amp; Rust</text>
        <text x="16" y="125" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Reviewer: Managing Editor</text>
      </g>

      <!-- Card 2 -->
      <g transform="translate(16, 226)">
        <rect x="0" y="0" width="273" height="150" rx="4" fill="#18181c" stroke="#27272a" stroke-width="1"/>
        <rect x="16" y="16" width="60" height="20" rx="3" fill="#ffffff" fill-opacity="0.1"/>
        <text x="46" y="30" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="700" text-anchor="middle">DESIGN</text>
        <text x="16" y="60" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Design Token Architecture</text>
        <text x="16" y="80" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">for Multi-Platform</text>
        <text x="16" y="125" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Reviewer: Tech Principal</text>
      </g>
    </g>

    <!-- Column 4: Scheduled -->
    <g transform="translate(975, 0)">
      <rect x="0" y="0" width="305" height="820" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <rect x="0" y="0" width="305" height="44" fill="#151518" stroke="#27272a" stroke-width="1"/>
      <text x="20" y="27" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">4. SCHEDULED LIVE</text>
      <rect x="255" y="10" width="32" height="24" rx="4" fill="#ffffff"/>
      <text x="271" y="26" fill="#09090b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" text-anchor="middle">6</text>

      <!-- Card 1 -->
      <g transform="translate(16, 60)">
        <rect x="0" y="0" width="273" height="150" rx="4" fill="#18181c" stroke="#ffffff" stroke-width="1"/>
        <rect x="16" y="16" width="90" height="20" rx="3" fill="#ffffff"/>
        <text x="61" y="30" fill="#09090b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="700" text-anchor="middle">ARMED AUTO</text>
        <text x="16" y="60" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Architectural Minimalist</text>
        <text x="16" y="80" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Systems Enterprise</text>
        <text x="16" y="125" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Today, 14:00 UTC+7</text>
      </g>

      <!-- Card 2 -->
      <g transform="translate(16, 226)">
        <rect x="0" y="0" width="273" height="150" rx="4" fill="#18181c" stroke="#27272a" stroke-width="1"/>
        <rect x="16" y="16" width="90" height="20" rx="3" fill="#ffffff" fill-opacity="0.1"/>
        <text x="61" y="30" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="700" text-anchor="middle">SCHEDULED</text>
        <text x="16" y="60" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Zero-Latency State</text>
        <text x="16" y="80" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Management Frontends</text>
        <text x="16" y="125" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Tomorrow, 09:00 UTC+7</text>
      </g>
    </g>
  </g>"""
)

# -------------------------------------------------------------
# Screen 6: Granular Revision History & Diff
# -------------------------------------------------------------
cms_screens["06-revision-history.svg"] = build_cms_svg(
    url="https://cms.mayastranawaloka.com/articles/8901/revisions",
    active_nav="Articles &amp; Posts",
    breadcrumb="Articles / #8901 / Revisions / Compare Rev #42 vs Rev #41",
    btn1="Revert to #41",
    btn2="Confirm #42",
    content_svg="""  <!-- Revision Diff Area -->
  <g transform="translate(280, 140)">
    <!-- Comparison Banner -->
    <rect x="0" y="0" width="1280" height="64" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
    <text x="24" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="700">COMPARING REVISION #41 WITH REVISION #42</text>
    <text x="24" y="48" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Rev #41 (Managing Editor - Yesterday 18:20) vs Rev #42 (Lead Engineer - Today 00:32)</text>
    <rect x="1000" y="18" width="115" height="28" rx="4" fill="#ffffff" fill-opacity="0.1"/>
    <text x="1057" y="36" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" text-anchor="middle">+142 Additions</text>
    <rect x="1130" y="18" width="125" height="28" rx="4" fill="#27272a"/>
    <text x="1192" y="36" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" text-anchor="middle">-38 Deletions</text>

    <!-- Side-by-Side Diff Windows -->
    <g transform="translate(0, 80)">
      <!-- Left Column: Base #41 -->
      <rect x="0" y="0" width="628" height="520" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <rect x="0" y="0" width="628" height="40" fill="#151518" stroke="#27272a" stroke-width="1"/>
      <text x="20" y="25" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700">REVISION #41 (PREVIOUS BASE)</text>

      <g transform="translate(20, 60)">
        <text x="0" y="24" fill="#52525b" font-family="monospace" font-size="12">14</text>
        <text x="36" y="24" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Modern enterprise systems require efficient data layouts.</text>

        <!-- Deleted lines highlighted in dark red tint -->
        <rect x="30" y="42" width="550" height="46" rx="2" fill="#ef4444" fill-opacity="0.1" stroke="#ef4444" stroke-opacity="0.3" stroke-width="1"/>
        <text x="0" y="62" fill="#52525b" font-family="monospace" font-size="12">15</text>
        <text x="36" y="62" fill="#ef4444" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">- Conventional UI frameworks introduce excessive render overhead</text>
        <text x="36" y="80" fill="#ef4444" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">  and noticeable user perceptible latency.</text>

        <text x="0" y="112" fill="#52525b" font-family="monospace" font-size="12">16</text>
        <text x="36" y="112" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">By utilizing strict monochromatic typography, digital operations</text>
        <text x="36" y="130" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">achieve instantaneous user comprehension.</text>

        <rect x="30" y="148" width="550" height="30" rx="2" fill="#ef4444" fill-opacity="0.1" stroke="#ef4444" stroke-opacity="0.3" stroke-width="1"/>
        <text x="0" y="168" fill="#52525b" font-family="monospace" font-size="12">17</text>
        <text x="36" y="168" fill="#ef4444" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">- We suggest limiting visual components to simple basic tables.</text>

        <text x="0" y="208" fill="#52525b" font-family="monospace" font-size="12">18</text>
        <text x="36" y="208" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Core Infrastructure Deliverables:</text>
        <text x="0" y="232" fill="#52525b" font-family="monospace" font-size="12">19</text>
        <text x="36" y="232" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">1. Autonomous CMS synchronization with edge caching layers.</text>
      </g>

      <!-- Right Column: Amended #42 -->
      <g transform="translate(652, 0)">
        <rect x="0" y="0" width="628" height="520" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
        <rect x="0" y="0" width="628" height="40" fill="#151518" stroke="#27272a" stroke-width="1"/>
        <text x="20" y="25" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700">REVISION #42 (LATEST AMENDMENT)</text>

        <g transform="translate(20, 60)">
          <text x="0" y="24" fill="#52525b" font-family="monospace" font-size="12">14</text>
          <text x="36" y="24" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Modern enterprise systems require efficient data layouts.</text>

          <!-- Added lines highlighted in subtle surface tint -->
          <rect x="30" y="42" width="550" height="46" rx="2" fill="#ffffff" fill-opacity="0.06" stroke="#27272a" stroke-width="1"/>
          <text x="0" y="62" fill="#52525b" font-family="monospace" font-size="12">15</text>
          <text x="36" y="62" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">+ Modern enterprise applications require high-precision information</text>
          <text x="36" y="80" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">  density without perceptual clutter and distraction.</text>

          <text x="0" y="112" fill="#52525b" font-family="monospace" font-size="12">16</text>
          <text x="36" y="112" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">By utilizing strict monochromatic typography, digital operations</text>
          <text x="36" y="130" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">achieve instantaneous user comprehension.</text>

          <rect x="30" y="148" width="550" height="30" rx="2" fill="#ffffff" fill-opacity="0.06" stroke="#27272a" stroke-width="1"/>
          <text x="0" y="168" fill="#52525b" font-family="monospace" font-size="12">17</text>
          <text x="36" y="168" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">+ Edge architecture guarantees sub-80ms global document propagation.</text>

          <text x="0" y="208" fill="#52525b" font-family="monospace" font-size="12">18</text>
          <text x="36" y="208" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Core Infrastructure Deliverables:</text>
          <text x="0" y="232" fill="#52525b" font-family="monospace" font-size="12">19</text>
          <text x="36" y="232" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">1. Autonomous CMS synchronization with edge caching layers.</text>
        </g>
      </g>
    </g>

    <!-- Version Timeline Log -->
    <g transform="translate(0, 620)">
      <rect x="0" y="0" width="1280" height="200" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="24" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">VERSION COMMIT TIMELINE</text>
      <line x1="24" y1="46" x2="1256" y2="46" stroke="#27272a" stroke-width="1"/>

      <g transform="translate(24, 60)">
        <text x="0" y="24" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">Rev #42 (Current Active)</text>
        <text x="240" y="24" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Updated layout schematics &amp; edge synchronization details</text>
        <text x="800" y="24" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Lead Engineer</text>
        <text x="1000" y="24" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Today, 00:32 UTC+7</text>

        <text x="0" y="64" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Rev #41</text>
        <text x="240" y="64" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Added executive summary &amp; Jonathan Ive industrial quote</text>
        <text x="800" y="64" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Managing Editor</text>
        <text x="1000" y="64" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Yesterday, 18:20 UTC+7</text>

        <text x="0" y="104" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Rev #40</text>
        <text x="240" y="104" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Initial draft submission for architectural peer review</text>
        <text x="800" y="104" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Staff Writer</text>
        <text x="1000" y="104" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Nov 12, 11:15 UTC+7</text>
      </g>
    </g>
  </g>"""
)

# -------------------------------------------------------------
# Screen 7: Dynamic Taxonomy & Tag Manager
# -------------------------------------------------------------
cms_screens["07-taxonomy-manager.svg"] = build_cms_svg(
    url="https://cms.mayastranawaloka.com/taxonomy",
    active_nav="Categories &amp; Tags",
    breadcrumb="Taxonomy Manager / Hierarchical Categories &amp; Redirect Graph",
    btn1="Rebuild Cache",
    btn2="+ Create Taxonomy",
    content_svg="""  <!-- Taxonomy Area -->
  <g transform="translate(280, 140)">
    <!-- Left: Hierarchy Tree -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="580" height="820" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <rect x="0" y="0" width="580" height="44" fill="#151518" stroke="#27272a" stroke-width="1"/>
      <text x="24" y="27" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">HIERARCHICAL CATEGORY STRUCTURE</text>

      <g transform="translate(24, 70)">
        <!-- Node 1 -->
        <rect x="0" y="0" width="532" height="48" rx="4" fill="#18181c" stroke="#27272a" stroke-width="1"/>
        <text x="16" y="29" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">[-] Enterprise Architecture (342 posts)</text>
        <text x="360" y="29" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">/insights/architecture</text>

        <!-- Subnode 1.1 -->
        <line x1="20" y1="48" x2="20" y2="180" stroke="#27272a" stroke-width="1"/>
        <rect x="40" y="60" width="492" height="40" rx="4" fill="#141418" stroke="#27272a" stroke-width="1"/>
        <text x="56" y="85" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">|-- Cloud Infrastructure (128 posts)</text>
        <text x="360" y="85" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">/insights/architecture/cloud</text>

        <!-- Subnode 1.2 -->
        <rect x="40" y="112" width="492" height="40" rx="4" fill="#141418" stroke="#27272a" stroke-width="1"/>
        <text x="56" y="137" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">|-- Microservices &amp; Edge (86 posts)</text>
        <text x="360" y="137" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">/insights/architecture/edge</text>

        <!-- Subnode 1.3 -->
        <rect x="40" y="164" width="492" height="40" rx="4" fill="#141418" stroke="#27272a" stroke-width="1"/>
        <text x="56" y="189" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">\\-- Legacy Migration (44 posts)</text>
        <text x="360" y="189" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">/insights/architecture/migration</text>

        <!-- Node 2 -->
        <rect x="0" y="226" width="532" height="48" rx="4" fill="#18181c" stroke="#27272a" stroke-width="1"/>
        <text x="16" y="255" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">[-] Software Engineering (412 posts)</text>
        <text x="360" y="255" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">/insights/engineering</text>

        <!-- Subnode 2.1 -->
        <line x1="20" y1="274" x2="20" y2="350" stroke="#27272a" stroke-width="1"/>
        <rect x="40" y="286" width="492" height="40" rx="4" fill="#141418" stroke="#27272a" stroke-width="1"/>
        <text x="56" y="311" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">|-- Systems &amp; Low-Level (94 posts)</text>
        <text x="360" y="311" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">/insights/engineering/systems</text>

        <!-- Subnode 2.2 -->
        <rect x="40" y="338" width="492" height="40" rx="4" fill="#141418" stroke="#27272a" stroke-width="1"/>
        <text x="56" y="363" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">\\-- Security &amp; Governance (110 posts)</text>
        <text x="360" y="363" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">/insights/engineering/security</text>

        <!-- Node 3 -->
        <rect x="0" y="400" width="532" height="48" rx="4" fill="#18181c" stroke="#27272a" stroke-width="1"/>
        <text x="16" y="429" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">[+] Design Systems (184 posts)</text>
        <text x="360" y="429" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">/insights/design-systems</text>

        <!-- Node 4 -->
        <rect x="0" y="460" width="532" height="48" rx="4" fill="#18181c" stroke="#27272a" stroke-width="1"/>
        <text x="16" y="489" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">[+] Data Platforms &amp; AI (310 posts)</text>
        <text x="360" y="489" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">/insights/data-ai</text>
      </g>
    </g>

    <!-- Right: Tag Registry & URL Redirection -->
    <g transform="translate(604, 0)">
      <!-- Top: Tag Registry -->
      <rect x="0" y="0" width="676" height="390" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <rect x="0" y="0" width="676" height="44" fill="#151518" stroke="#27272a" stroke-width="1"/>
      <text x="24" y="27" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">TOPIC TAG REGISTRY (148 ACTIVE TAGS)</text>

      <g transform="translate(24, 65)">
        <!-- Tag Pills -->
        <rect x="0" y="0" width="115" height="32" rx="16" fill="#ffffff" fill-opacity="0.1"/>
        <text x="57" y="21" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="middle">#ERP (182)</text>

        <rect x="125" y="0" width="150" height="32" rx="16" fill="#ffffff" fill-opacity="0.1"/>
        <text x="200" y="21" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="middle">#Kubernetes (140)</text>

        <rect x="285" y="0" width="165" height="32" rx="16" fill="#ffffff" fill-opacity="0.1"/>
        <text x="367" y="21" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="middle">#Microservices (112)</text>

        <rect x="460" y="0" width="145" height="32" rx="16" fill="#ffffff" fill-opacity="0.1"/>
        <text x="532" y="21" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="middle">#PostgreSQL (98)</text>

        <rect x="0" y="44" width="145" height="32" rx="16" fill="#ffffff" fill-opacity="0.1"/>
        <text x="72" y="65" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="middle">#Performance (87)</text>

        <rect x="155" y="44" width="125" height="32" rx="16" fill="#ffffff" fill-opacity="0.1"/>
        <text x="217" y="65" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="middle">#Security (76)</text>

        <rect x="290" y="44" width="110" height="32" rx="16" fill="#ffffff" fill-opacity="0.1"/>
        <text x="345" y="65" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="middle">#Rust (64)</text>

        <rect x="410" y="44" width="115" height="32" rx="16" fill="#ffffff" fill-opacity="0.1"/>
        <text x="467" y="65" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="middle">#Kafka (58)</text>

        <rect x="535" y="44" width="90" height="32" rx="16" fill="#ffffff" fill-opacity="0.1"/>
        <text x="580" y="65" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="middle">#Go (52)</text>

        <rect x="0" y="88" width="120" height="32" rx="16" fill="#ffffff" fill-opacity="0.1"/>
        <text x="60" y="109" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="middle">#GraphQL (46)</text>

        <rect x="130" y="88" width="135" height="32" rx="16" fill="#ffffff" fill-opacity="0.1"/>
        <text x="197" y="109" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="middle">#TypeScript (41)</text>

        <rect x="275" y="88" width="110" height="32" rx="16" fill="#ffffff" fill-opacity="0.1"/>
        <text x="330" y="109" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="middle">#Redis (39)</text>

        <rect x="395" y="88" width="125" height="32" rx="16" fill="#ffffff" fill-opacity="0.1"/>
        <text x="457" y="109" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="middle">#DevOps (34)</text>

        <text x="0" y="170" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Tag rules: Automatic canonical lowercase slugging with strict hyphen separator.</text>
      </g>

      <!-- Bottom: URL Redirect Manager -->
      <g transform="translate(0, 410)">
        <rect x="0" y="0" width="676" height="410" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
        <rect x="0" y="0" width="676" height="44" fill="#151518" stroke="#27272a" stroke-width="1"/>
        <text x="24" y="27" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">URL 301 / 302 REDIRECT MANAGER</text>

        <g transform="translate(24, 60)">
          <!-- Row 1 -->
          <text x="0" y="24" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">/blog/old-erp-guide</text>
          <text x="170" y="24" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">-&gt;</text>
          <text x="200" y="24" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">/insights/enterprise-erp-systems</text>
          <rect x="520" y="8" width="40" height="22" rx="3" fill="#ffffff" fill-opacity="0.1"/>
          <text x="540" y="24" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" text-anchor="middle">301</text>
          <text x="580" y="24" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">14,820 Hits</text>

          <!-- Row 2 -->
          <text x="0" y="68" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">/articles/docker-setup</text>
          <text x="170" y="68" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">-&gt;</text>
          <text x="200" y="68" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">/insights/containerized-infrastructure</text>
          <rect x="520" y="52" width="40" height="22" rx="3" fill="#ffffff" fill-opacity="0.1"/>
          <text x="540" y="68" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" text-anchor="middle">301</text>
          <text x="580" y="68" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">9,340 Hits</text>

          <!-- Row 3 -->
          <text x="0" y="112" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">/docs/api-v1-deprecation</text>
          <text x="170" y="112" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">-&gt;</text>
          <text x="200" y="112" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">/developers/graphql</text>
          <rect x="520" y="96" width="40" height="22" rx="3" fill="#ffffff" fill-opacity="0.1"/>
          <text x="540" y="112" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" text-anchor="middle">301</text>
          <text x="580" y="112" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">5,120 Hits</text>

          <!-- Row 4 -->
          <text x="0" y="156" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">/news/q3-roundup</text>
          <text x="170" y="156" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">-&gt;</text>
          <text x="200" y="156" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">/insights/q3-financial-architecture</text>
          <rect x="520" y="140" width="40" height="22" rx="3" fill="#ffffff" fill-opacity="0.1"/>
          <text x="540" y="156" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" text-anchor="middle">301</text>
          <text x="580" y="156" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">3,490 Hits</text>
        </g>
      </g>
    </g>
  </g>"""
)

# -------------------------------------------------------------
# Screen 8: Audience & Engagement Analytics
# -------------------------------------------------------------
cms_screens["08-audience-analytics.svg"] = build_cms_svg(
    url="https://cms.mayastranawaloka.com/analytics/audience",
    active_nav="Dashboard",
    breadcrumb="Audience Analytics / Global Reader Metrics (Last 30 Days)",
    btn1="Filter: 30D",
    btn2="Export CSV",
    content_svg="""  <!-- Audience Analytics Area -->
  <g transform="translate(280, 140)">
    <!-- 4 KPI Cards -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="300" height="96" rx="4" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="24" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">TOTAL UNIQUE READERS</text>
      <text x="24" y="66" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="800">248,910</text>
      <text x="200" y="66" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">+18.4% MoM</text>

      <rect x="326" y="0" width="300" height="96" rx="4" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="350" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">AVG TIME ON PAGE</text>
      <text x="350" y="66" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="800">4m 32s</text>
      <text x="490" y="66" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Benchmark 2m 10s</text>

      <rect x="652" y="0" width="300" height="96" rx="4" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="676" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">AVG SCROLL DEPTH</text>
      <text x="676" y="66" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="800">78.6%</text>
      <text x="820" y="66" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">92% to Conclusion</text>

      <rect x="978" y="0" width="302" height="96" rx="4" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="1002" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">TOTAL ARTICLE SHARES</text>
      <text x="1002" y="66" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="800">14,290</text>
      <text x="1140" y="66" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">LinkedIn 58% / X 42%</text>
    </g>

    <!-- Split Panels: Large Chart (Left) + Referrals/Geo (Right) -->
    <g transform="translate(0, 116)">
      <!-- Left Chart Panel -->
      <rect x="0" y="0" width="840" height="704" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <rect x="0" y="0" width="840" height="44" fill="#151518" stroke="#27272a" stroke-width="1"/>
      <text x="24" y="27" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">READER ENGAGEMENT &amp; DAILY TRAFFIC VOLUME</text>
      <text x="620" y="27" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Red: Uniques | Dotted: Returns</text>

      <!-- Chart Graphics -->
      <g transform="translate(30, 80)">
        <!-- Gridlines -->
        <line x1="40" y1="50" x2="780" y2="50" stroke="#1f1f23" stroke-width="1"/>
        <line x1="40" y1="130" x2="780" y2="130" stroke="#1f1f23" stroke-width="1"/>
        <line x1="40" y1="210" x2="780" y2="210" stroke="#1f1f23" stroke-width="1"/>
        <line x1="40" y1="290" x2="780" y2="290" stroke="#1f1f23" stroke-width="1"/>
        <line x1="40" y1="370" x2="780" y2="370" stroke="#1f1f23" stroke-width="1"/>

        <!-- Y Axis labels -->
        <text x="30" y="55" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="end">12K</text>
        <text x="30" y="135" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="end">9K</text>
        <text x="30" y="215" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="end">6K</text>
        <text x="30" y="295" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="end">3K</text>
        <text x="30" y="375" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="end">0</text>

        <!-- Area Curve Underneath -->
        <path d="M 50 340 Q 150 280 250 300 T 450 180 T 650 100 T 770 120 L 770 370 L 50 370 Z" fill="#ef4444" fill-opacity="0.12"/>

        <!-- Primary Trend Line -->
        <path d="M 50 340 Q 150 280 250 300 T 450 180 T 650 100 T 770 120" stroke="#ef4444" stroke-width="3" fill="none"/>

        <!-- Return Readers Dotted Line -->
        <path d="M 50 360 Q 150 330 250 340 T 450 270 T 650 210 T 770 230" stroke="#71717a" stroke-width="2" stroke-dasharray="4 4" fill="none"/>

        <!-- Peak Indicator Point -->
        <circle cx="650" cy="100" r="5" fill="#ef4444"/>
        <rect x="600" y="50" width="100" height="30" rx="4" fill="#ffffff"/>
        <text x="650" y="70" fill="#09090b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Peak: 11,480</text>

        <!-- X Axis labels -->
        <text x="50" y="405" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">Oct 15</text>
        <text x="170" y="405" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">Oct 22</text>
        <text x="290" y="405" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">Oct 29</text>
        <text x="410" y="405" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">Nov 05</text>
        <text x="530" y="405" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">Nov 12</text>
        <text x="650" y="405" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">Nov 14</text>
        <text x="770" y="405" fill="#52525b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">Today</text>
      </g>
    </g>

    <!-- Right Panels: Referral & Geo -->
    <g transform="translate(864, 116)">
      <!-- Top: Referral Sources -->
      <rect x="0" y="0" width="416" height="340" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <rect x="0" y="0" width="416" height="44" fill="#151518" stroke="#27272a" stroke-width="1"/>
      <text x="24" y="27" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">TOP REFERRAL SOURCES</text>

      <g transform="translate(24, 64)">
        <text x="0" y="20" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Google Organic Search</text>
        <text x="368" y="20" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" text-anchor="end">54% (134K)</text>
        <rect x="0" y="32" width="368" height="6" rx="3" fill="#27272a"/>
        <rect x="0" y="32" width="198" height="6" rx="3" fill="#ffffff"/>

        <text x="0" y="70" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Direct Navigation &amp; Bookmarks</text>
        <text x="368" y="70" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" text-anchor="end">22% (54K)</text>
        <rect x="0" y="82" width="368" height="6" rx="3" fill="#27272a"/>
        <rect x="0" y="82" width="81" height="6" rx="3" fill="#ffffff"/>

        <text x="0" y="120" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">LinkedIn Technical Posts</text>
        <text x="368" y="120" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" text-anchor="end">14% (34K)</text>
        <rect x="0" y="132" width="368" height="6" rx="3" fill="#27272a"/>
        <rect x="0" y="132" width="51" height="6" rx="3" fill="#ffffff"/>

        <text x="0" y="170" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">GitHub Repositories</text>
        <text x="368" y="170" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" text-anchor="end">6% (15K)</text>
        <rect x="0" y="182" width="368" height="6" rx="3" fill="#27272a"/>
        <rect x="0" y="182" width="22" height="6" rx="3" fill="#ffffff"/>

        <text x="0" y="220" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Hacker News &amp; Tech Forums</text>
        <text x="368" y="220" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" text-anchor="end">4% (10K)</text>
        <rect x="0" y="232" width="368" height="6" rx="3" fill="#27272a"/>
        <rect x="0" y="232" width="15" height="6" rx="3" fill="#ffffff"/>
      </g>

      <!-- Bottom: Geographic Distribution -->
      <g transform="translate(0, 364)">
        <rect x="0" y="0" width="416" height="340" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
        <rect x="0" y="0" width="416" height="44" fill="#151518" stroke="#27272a" stroke-width="1"/>
        <text x="24" y="27" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">GEOGRAPHIC DISTRIBUTION</text>

        <g transform="translate(24, 70)">
          <text x="0" y="24" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Indonesia (Jakarta, Surabaya, Bandung)</text>
          <text x="368" y="24" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" text-anchor="end">68%</text>

          <text x="0" y="70" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Singapore (APAC Tech Hub)</text>
          <text x="368" y="70" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" text-anchor="end">14%</text>

          <text x="0" y="116" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">United States (West Coast &amp; NYC)</text>
          <text x="368" y="116" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" text-anchor="end">10%</text>

          <text x="0" y="162" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">European Union &amp; Other</text>
          <text x="368" y="162" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" text-anchor="end">8%</text>
        </g>
      </g>
    </g>
  </g>"""
)

# -------------------------------------------------------------
# Screen 9: Headless GraphQL & REST Distribution
# -------------------------------------------------------------
cms_screens["09-api-distribution.svg"] = build_cms_svg(
    url="https://cms.mayastranawaloka.com/developers/graphql",
    active_nav="System Settings",
    breadcrumb="Developer Platform / GraphQL Schema Playground &amp; Edge API",
    btn1="Schema Docs",
    btn2="Run Query [Ctrl+Enter]",
    content_svg="""  <!-- API Playground Area -->
  <g transform="translate(280, 140)">
    <!-- API Status Bar -->
    <rect x="0" y="0" width="1280" height="42" rx="4" fill="#111114" stroke="#27272a" stroke-width="1"/>
    <text x="20" y="26" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Endpoint: https://api.mayastranawaloka.com/graphql</text>
    <text x="560" y="26" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Edge POP: SIN-01 (Singapore)</text>
    <rect x="1140" y="8" width="120" height="26" rx="4" fill="#ffffff" fill-opacity="0.1"/>
    <text x="1200" y="25" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Cache HIT (18ms)</text>

    <!-- Side-by-Side: GraphQL Editor (Left) & JSON Response (Right) -->
    <g transform="translate(0, 58)">
      <!-- Editor -->
      <rect x="0" y="0" width="628" height="670" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <rect x="0" y="0" width="628" height="40" fill="#151518" stroke="#27272a" stroke-width="1"/>
      <text x="20" y="25" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700">GRAPHQL QUERY INPUT</text>

      <g transform="translate(20, 60)">
        <text x="0" y="24" fill="#52525b" font-family="monospace" font-size="12">01</text>
        <text x="36" y="24" fill="#ffffff" font-family="monospace" font-size="13">query GetArticleBySlug($slug: String!) {{</text>

        <text x="0" y="52" fill="#52525b" font-family="monospace" font-size="12">02</text>
        <text x="36" y="52" fill="#ffffff" font-family="monospace" font-size="13">  article(slug: $slug) {{</text>

        <text x="0" y="80" fill="#52525b" font-family="monospace" font-size="12">03</text>
        <text x="36" y="80" fill="#d4d4d8" font-family="monospace" font-size="13">    id</text>

        <text x="0" y="108" fill="#52525b" font-family="monospace" font-size="12">04</text>
        <text x="36" y="108" fill="#d4d4d8" font-family="monospace" font-size="13">    title</text>

        <text x="0" y="136" fill="#52525b" font-family="monospace" font-size="12">05</text>
        <text x="36" y="136" fill="#d4d4d8" font-family="monospace" font-size="13">    excerpt</text>

        <text x="0" y="164" fill="#52525b" font-family="monospace" font-size="12">06</text>
        <text x="36" y="164" fill="#d4d4d8" font-family="monospace" font-size="13">    contentHtml</text>

        <text x="0" y="192" fill="#52525b" font-family="monospace" font-size="12">07</text>
        <text x="36" y="192" fill="#d4d4d8" font-family="monospace" font-size="13">    readingTimeMinutes</text>

        <text x="0" y="220" fill="#52525b" font-family="monospace" font-size="12">08</text>
        <text x="36" y="220" fill="#d4d4d8" font-family="monospace" font-size="13">    publishedAt</text>

        <text x="0" y="248" fill="#52525b" font-family="monospace" font-size="12">09</text>
        <text x="36" y="248" fill="#ffffff" font-family="monospace" font-size="13">    author {{</text>

        <text x="0" y="276" fill="#52525b" font-family="monospace" font-size="12">10</text>
        <text x="36" y="276" fill="#d4d4d8" font-family="monospace" font-size="13">      name</text>

        <text x="0" y="304" fill="#52525b" font-family="monospace" font-size="12">11</text>
        <text x="36" y="304" fill="#d4d4d8" font-family="monospace" font-size="13">      title</text>

        <text x="0" y="332" fill="#52525b" font-family="monospace" font-size="12">12</text>
        <text x="36" y="332" fill="#ffffff" font-family="monospace" font-size="13">    }}</text>

        <text x="0" y="360" fill="#52525b" font-family="monospace" font-size="12">13</text>
        <text x="36" y="360" fill="#d4d4d8" font-family="monospace" font-size="13">    tags</text>

        <text x="0" y="388" fill="#52525b" font-family="monospace" font-size="12">14</text>
        <text x="36" y="388" fill="#ffffff" font-family="monospace" font-size="13">  }}</text>

        <text x="0" y="416" fill="#52525b" font-family="monospace" font-size="12">15</text>
        <text x="36" y="416" fill="#ffffff" font-family="monospace" font-size="13">}}</text>
      </g>

      <!-- Query Variables Box -->
      <g transform="translate(20, 520)">
        <rect x="0" y="0" width="588" height="120" rx="4" fill="#18181c" stroke="#27272a" stroke-width="1"/>
        <text x="16" y="25" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700">QUERY VARIABLES (JSON)</text>
        <text x="16" y="55" fill="#d4d4d8" font-family="monospace" font-size="12">{{</text>
        <text x="32" y="80" fill="#ffffff" font-family="monospace" font-size="12">"slug": "architectural-minimalist-systems"</text>
        <text x="16" y="105" fill="#d4d4d8" font-family="monospace" font-size="12">}}</text>
      </g>
    </g>

    <!-- Response Window -->
    <g transform="translate(652, 58)">
      <rect x="0" y="0" width="628" height="670" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <rect x="0" y="0" width="628" height="40" fill="#151518" stroke="#27272a" stroke-width="1"/>
      <text x="20" y="25" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700">JSON RESPONSE (200 OK - 18ms - 1.2 KB)</text>

      <g transform="translate(20, 60)">
        <text x="0" y="24" fill="#d4d4d8" font-family="monospace" font-size="12">{{</text>
        <text x="20" y="50" fill="#d4d4d8" font-family="monospace" font-size="12">  "data": {{</text>
        <text x="40" y="76" fill="#d4d4d8" font-family="monospace" font-size="12">    "article": {{</text>
        <text x="60" y="102" fill="#ffffff" font-family="monospace" font-size="12">      "id": "8901",</text>
        <text x="60" y="128" fill="#ffffff" font-family="monospace" font-size="12">      "title": "Architectural Minimalist Systems",</text>
        <text x="60" y="154" fill="#ffffff" font-family="monospace" font-size="12">      "excerpt": "Modern enterprise applications require high precision...",</text>
        <text x="60" y="180" fill="#ffffff" font-family="monospace" font-size="12">      "readingTimeMinutes": 6,</text>
        <text x="60" y="206" fill="#ffffff" font-family="monospace" font-size="12">      "publishedAt": "2026-11-14T00:32:00Z",</text>
        <text x="60" y="232" fill="#d4d4d8" font-family="monospace" font-size="12">      "author": {{</text>
        <text x="80" y="258" fill="#ffffff" font-family="monospace" font-size="12">        "name": "Editorial Board",</text>
        <text x="80" y="284" fill="#ffffff" font-family="monospace" font-size="12">        "title": "Principal Systems Architect"</text>
        <text x="60" y="310" fill="#d4d4d8" font-family="monospace" font-size="12">      }},</text>
        <text x="60" y="336" fill="#ffffff" font-family="monospace" font-size="12">      "tags": ["ERP", "Design", "Cloud"]</text>
        <text x="40" y="362" fill="#d4d4d8" font-family="monospace" font-size="12">    }}</text>
        <text x="20" y="388" fill="#d4d4d8" font-family="monospace" font-size="12">  }}</text>
        <text x="0" y="414" fill="#d4d4d8" font-family="monospace" font-size="12">}}</text>
      </g>
    </g>

    <!-- Bottom Edge Delivery Bar -->
    <g transform="translate(0, 742)">
      <rect x="0" y="0" width="1280" height="78" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="24" y="30" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">EDGE CDN DISTRIBUTION NETWORK</text>
      <text x="24" y="55" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">24 Global Edge POPs Active | 99.98% Cache Hit Ratio | Global Propagation &lt; 80ms</text>
      <rect x="1120" y="20" width="136" height="38" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1"/>
      <text x="1188" y="44" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" text-anchor="middle">Purge Edge Cache</text>
    </g>
  </g>"""
)

# -------------------------------------------------------------
# Screen 10: Enterprise Access & RBAC Control
# -------------------------------------------------------------
cms_screens["10-access-governance.svg"] = build_cms_svg(
    url="https://cms.mayastranawaloka.com/governance/rbac",
    active_nav="Team &amp; Roles",
    breadcrumb="Enterprise Access Governance / Role-Based Access Control",
    btn1="Audit Export",
    btn2="+ Invite Member",
    content_svg="""  <!-- RBAC Area -->
  <g transform="translate(280, 140)">
    <!-- 3 Metrics Cards -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="408" height="96" rx="4" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="24" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">ACTIVE EDITORIAL USERS</text>
      <text x="24" y="66" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="800">28 Active</text>
      <text x="260" y="66" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">0 Suspended</text>

      <rect x="436" y="0" width="408" height="96" rx="4" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="460" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">2-FACTOR ENFORCEMENT</text>
      <text x="460" y="66" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="800">100% Policy</text>
      <text x="690" y="66" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">FIDO2 / TOTP</text>

      <rect x="872" y="0" width="408" height="96" rx="4" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="896" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">ACTIVE CONCURRENT SESSIONS</text>
      <text x="896" y="66" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="800">34 Sessions</text>
      <text x="1140" y="66" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Across 4 Desks</text>
    </g>

    <!-- Team Members & RBAC Table -->
    <g transform="translate(0, 116)">
      <rect x="0" y="0" width="1280" height="570" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <rect x="0" y="0" width="1280" height="44" fill="#151518" stroke="#27272a" stroke-width="1"/>
      <text x="24" y="27" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700">USER &amp; EMAIL</text>
      <text x="360" y="27" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700">EDITORIAL DESK</text>
      <text x="560" y="27" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700">ASSIGNED ROLE</text>
      <text x="800" y="27" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700">AUTHENTICATION</text>
      <text x="980" y="27" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700">LAST ACTIVE</text>
      <text x="1180" y="27" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700">ACTION</text>

      <!-- Row 1 -->
      <g transform="translate(0, 44)">
        <line x1="0" y1="80" x2="1280" y2="80" stroke="#1f1f23" stroke-width="1"/>
        <text x="24" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Arya Pratama</text>
        <text x="24" y="52" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">arya@mayastranawaloka.com</text>
        <text x="360" y="42" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Executive Board</text>
        <rect x="560" y="26" width="165" height="24" rx="4" fill="#ffffff" fill-opacity="0.12"/>
        <text x="642" y="42" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Editor-in-Chief (Full)</text>
        <text x="800" y="42" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">FIDO2 Hardware Key</text>
        <text x="980" y="42" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="600">Active Now</text>
        <text x="1180" y="42" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Manage</text>
      </g>

      <!-- Row 2 -->
      <g transform="translate(0, 124)">
        <line x1="0" y1="80" x2="1280" y2="80" stroke="#1f1f23" stroke-width="1"/>
        <text x="24" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Siti Rahmawati</text>
        <text x="24" y="52" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">siti.r@mayastranawaloka.com</text>
        <text x="360" y="42" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Architecture Desk</text>
        <rect x="560" y="26" width="155" height="24" rx="4" fill="#27272a"/>
        <text x="637" y="42" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Senior Tech Editor</text>
        <text x="800" y="42" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">TOTP Authenticator</text>
        <text x="980" y="42" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">12 mins ago</text>
        <text x="1180" y="42" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Manage</text>
      </g>

      <!-- Row 3 -->
      <g transform="translate(0, 204)">
        <line x1="0" y1="80" x2="1280" y2="80" stroke="#1f1f23" stroke-width="1"/>
        <text x="24" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Budi Santoso</text>
        <text x="24" y="52" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">budi.s@mayastranawaloka.com</text>
        <text x="360" y="42" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Software Engineering</text>
        <rect x="560" y="26" width="115" height="24" rx="4" fill="#18181c" stroke="#27272a" stroke-width="1"/>
        <text x="617" y="42" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">Staff Writer</text>
        <text x="800" y="42" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">TOTP Authenticator</text>
        <text x="980" y="42" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">1 hour ago</text>
        <text x="1180" y="42" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Manage</text>
      </g>

      <!-- Row 4 -->
      <g transform="translate(0, 284)">
        <line x1="0" y1="80" x2="1280" y2="80" stroke="#1f1f23" stroke-width="1"/>
        <text x="24" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Dian Kusuma</text>
        <text x="24" y="52" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">dian.k@mayastranawaloka.com</text>
        <text x="360" y="42" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Design Systems</text>
        <rect x="560" y="26" width="165" height="24" rx="4" fill="#18181c" stroke="#27272a" stroke-width="1"/>
        <text x="642" y="42" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">Copy &amp; Layout Review</text>
        <text x="800" y="42" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">FIDO2 Hardware Key</text>
        <text x="980" y="42" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">3 hours ago</text>
        <text x="1180" y="42" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Manage</text>
      </g>

      <!-- Row 5 -->
      <g transform="translate(0, 364)">
        <text x="24" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">External Contributor</text>
        <text x="24" y="52" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">guest.contributor@partner.org</text>
        <text x="360" y="42" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Guest Column</text>
        <rect x="560" y="26" width="145" height="24" rx="4" fill="#18181c" stroke="#27272a" stroke-width="1"/>
        <text x="632" y="42" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">Sandboxed Author</text>
        <text x="800" y="42" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Email Magic Link + OTP</text>
        <text x="980" y="42" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13">Nov 12, 16:30</text>
        <text x="1180" y="42" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Manage</text>
      </g>
    </g>

    <!-- Bottom Governance Rules -->
    <g transform="translate(0, 700)">
      <rect x="0" y="0" width="1280" height="120" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="24" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">NEWSROOM GOVERNANCE &amp; SECURITY POLICIES</text>
      <line x1="24" y1="46" x2="1256" y2="46" stroke="#27272a" stroke-width="1"/>
      <text x="24" y="72" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">1. Session Idle Timeout: 12 Hours with mandatory re-auth on publishing live actions.</text>
      <text x="24" y="94" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">2. IP Whitelisting: Enforced for administrative role modification and bulk taxonomy deletions.</text>
    </g>
  </g>"""
)

# -------------------------------------------------------------
# Screen 11: Edge Invalidation Webhooks & Omnichannel Pipeline
# -------------------------------------------------------------
cms_screens["11-webhook-integrations.svg"] = build_cms_svg(
    url="https://cms.mayastranawaloka.com/settings/webhooks",
    active_nav="System Settings",
    breadcrumb="System Settings / Event Webhooks &amp; Edge Invalidation Pipeline",
    btn1="Test All Webhooks",
    btn2="+ Register Endpoint",
    content_svg="""  <!-- Webhook Pipeline Area -->
  <g transform="translate(280, 140)">
    <!-- 4 KPI Cards -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="300" height="96" rx="4" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="24" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">REGISTERED ENDPOINTS</text>
      <text x="24" y="66" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="800">8 Active</text>
      <text x="180" y="66" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">0 Failing</text>

      <rect x="326" y="0" width="300" height="96" rx="4" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="350" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">AVG DISPATCH LATENCY</text>
      <text x="350" y="66" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="800">14.2 ms</text>
      <text x="500" y="66" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Async Queue</text>

      <rect x="652" y="0" width="300" height="96" rx="4" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="676" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">GLOBAL PURGE TIME</text>
      <text x="676" y="66" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="800">&lt; 50 ms</text>
      <text x="820" y="66" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Edge Propagation</text>

      <rect x="978" y="0" width="302" height="96" rx="4" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="1002" y="28" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600">DELIVERY RETRY SLA</text>
      <text x="1002" y="66" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="28" font-weight="800">99.99 %</text>
      <text x="1140" y="66" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Exponential DLQ</text>
    </g>

    <!-- Webhook Table -->
    <g transform="translate(0, 116)">
      <rect x="0" y="0" width="1280" height="570" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <rect x="0" y="0" width="1280" height="44" fill="#151518" stroke="#27272a" stroke-width="1"/>
      <text x="24" y="27" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700">INTEGRATION &amp; TARGET URL</text>
      <text x="440" y="27" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700">SUBSCRIBED EVENTS</text>
      <text x="740" y="27" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700">HMAC SIGNATURE</text>
      <text x="960" y="27" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700">LAST DELIVERY</text>
      <text x="1150" y="27" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700">STATUS</text>

      <!-- Row 1 -->
      <g transform="translate(0, 44)">
        <line x1="0" y1="80" x2="1280" y2="80" stroke="#1f1f23" stroke-width="1"/>
        <text x="24" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Cloudflare Edge Cache Purge</text>
        <text x="24" y="52" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">https://api.cloudflare.com/client/v4/zones/.../purge_cache</text>
        <rect x="440" y="26" width="150" height="24" rx="4" fill="#18181c" stroke="#27272a" stroke-width="1"/>
        <text x="515" y="42" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">article.published, article.rev</text>
        <text x="740" y="42" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">SHA256 (Enforced)</text>
        <text x="960" y="42" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Today 00:32 (18ms)</text>
        <rect x="1150" y="26" width="90" height="24" rx="4" fill="#ffffff" fill-opacity="0.12"/>
        <text x="1195" y="42" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="middle">200 OK</text>
      </g>

      <!-- Row 2 -->
      <g transform="translate(0, 124)">
        <line x1="0" y1="80" x2="1280" y2="80" stroke="#1f1f23" stroke-width="1"/>
        <text x="24" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Mobile Newsstand Push Notification</text>
        <text x="24" y="52" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">https://fcm.googleapis.com/v1/projects/mayastra-news/messages:send</text>
        <rect x="440" y="26" width="160" height="24" rx="4" fill="#18181c" stroke="#27272a" stroke-width="1"/>
        <text x="520" y="42" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">article.breaking_news</text>
        <text x="740" y="42" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">OAuth 2.0 Token</text>
        <text x="960" y="42" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Yesterday 18:20 (32ms)</text>
        <rect x="1150" y="26" width="90" height="24" rx="4" fill="#ffffff" fill-opacity="0.12"/>
        <text x="1195" y="42" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="middle">200 OK</text>
      </g>

      <!-- Row 3 -->
      <g transform="translate(0, 204)">
        <line x1="0" y1="80" x2="1280" y2="80" stroke="#1f1f23" stroke-width="1"/>
        <text x="24" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Search Engine IndexNow Broadcaster</text>
        <text x="24" y="52" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">https://api.indexnow.org/indexnow</text>
        <rect x="440" y="26" width="140" height="24" rx="4" fill="#18181c" stroke="#27272a" stroke-width="1"/>
        <text x="510" y="42" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">article.url_published</text>
        <text x="740" y="42" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">API Key Header</text>
        <text x="960" y="42" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Today 00:32 (45ms)</text>
        <rect x="1150" y="26" width="90" height="24" rx="4" fill="#ffffff" fill-opacity="0.12"/>
        <text x="1195" y="42" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="middle">200 OK</text>
      </g>

      <!-- Row 4 -->
      <g transform="translate(0, 284)">
        <text x="24" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="600">Static RSS / Atom XML Feed Builder</text>
        <text x="24" y="52" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11">https://cdn.mayastranawaloka.com/hooks/rebuild-rss</text>
        <rect x="440" y="26" width="130" height="24" rx="4" fill="#18181c" stroke="#27272a" stroke-width="1"/>
        <text x="505" y="42" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" text-anchor="middle">article.all_events</text>
        <text x="740" y="42" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">HMAC-SHA256</text>
        <text x="960" y="42" fill="#d4d4d8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">Nov 12 11:15 (8ms)</text>
        <rect x="1150" y="26" width="90" height="24" rx="4" fill="#ffffff" fill-opacity="0.12"/>
        <text x="1195" y="42" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="middle">200 OK</text>
      </g>
    </g>

    <!-- Bottom Security Policy -->
    <g transform="translate(0, 700)">
      <rect x="0" y="0" width="1280" height="120" rx="6" fill="#111114" stroke="#27272a" stroke-width="1"/>
      <text x="24" y="32" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700">WEBHOOK SECURITY &amp; RETRY CONFIGURATION</text>
      <line x1="24" y1="46" x2="1256" y2="46" stroke="#27272a" stroke-width="1"/>
      <text x="24" y="72" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">1. Cryptographic HMAC-SHA256 signature calculated over timestamp + JSON body to eliminate replay attacks.</text>
      <text x="24" y="94" fill="#a1a1aa" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12">2. Exponential backoff retry: 5 attempts (1s, 5s, 30s, 5m, 1h) before moving payload to Dead Letter Queue (DLQ).</text>
    </g>
  </g>"""
)

# Output directory
out_dir = "assets/projects/cms"
os.makedirs(out_dir, exist_ok=True)

for filename, content in cms_screens.items():
    filepath = os.path.join(out_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    # Validate XML
    ET.fromstring(content)
    print(f"Generated and validated {filepath}")

print("All 10 CMS screens generated and verified successfully.")
