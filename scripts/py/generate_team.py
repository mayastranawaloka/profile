import os

os.makedirs("assets/team", exist_ok=True)

for i, role in enumerate(["LEAD SYSTEM ARCHITECT", "PRINCIPAL SOFTWARE ENGINEER", "HEAD OF TECHNOLOGY &amp; OPERATIONS"], start=1):
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 800" width="600" height="800" fill="none">
  <!-- Background -->
  <rect width="600" height="800" fill="#0d0d10"/>
  <rect x="20" y="20" width="560" height="760" stroke="#222226" stroke-width="1" rx="4"/>
  
  <!-- Subtle geometric grid lines -->
  <line x1="20" y1="400" x2="580" y2="400" stroke="#16161a" stroke-width="1"/>
  <line x1="300" y1="20" x2="300" y2="780" stroke="#16161a" stroke-width="1"/>
  
  <!-- Abstract Minimalist Portrait Silhouette -->
  <circle cx="300" cy="280" r="100" fill="#18181f" stroke="#2e2e38" stroke-width="1.5"/>
  <path d="M160 560 C160 430, 440 430, 440 560 L440 640 L160 640 Z" fill="#18181f" stroke="#2e2e38" stroke-width="1.5"/>
  
  <!-- Hair / Feature accent -->
  <circle cx="300" cy="270" r="70" fill="#24242e"/>
  
  <!-- Index Tag -->
  <rect x="40" y="40" width="70" height="26" rx="2" fill="#141418" stroke="#27272a" stroke-width="1"/>
  <text x="75" y="57" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" text-anchor="middle" letter-spacing="1">0{i} / TEAM</text>
  
  <!-- Label at bottom -->
  <text x="300" y="690" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="700" text-anchor="middle" letter-spacing="2">KEY PERSONNEL 0{i}</text>
  <text x="300" y="718" fill="#71717a" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="500" text-anchor="middle" letter-spacing="1.5">{role}</text>
  <text x="300" y="740" fill="#3f3f46" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="9" text-anchor="middle" letter-spacing="1">PHOTO PLACEHOLDER</text>
</svg>'''
    with open(f"assets/team/person-{i}.svg", "w") as f:
        f.write(svg_content.strip())
    print(f"[OK] Generated assets/team/person-{i}.svg")
