import math
import os
from PIL import Image, ImageFilter

def create_panoramic_banner():
    logo_path = 'assets/logo.png'
    output_path = 'assets/logo-banner.png'

    if not os.path.exists(logo_path):
        raise FileNotFoundError(f"Missing {logo_path}")

    orig = Image.open(logo_path).convert('RGB')
    ow, oh = orig.size

    # Ultra-high-resolution widescreen canvas: 2400 x 850
    bw, bh = 2400, 850
    cx, cy = bw / 2.0, bh / 2.0

    # Scale original logo so the flower is sized gracefully
    # Target flower height ~320px
    # Original flower is 273px -> scale = 320 / 273 = 1.172
    scale = 1.172
    nw, nh = int(ow * scale), int(oh * scale) # 539 x 539
    scaled_orig = orig.resize((nw, nh), Image.Resampling.LANCZOS)

    # Ambient blurred background to span 2400px edge-to-edge
    ambient_bg = orig.resize((bw, bh), Image.Resampling.BILINEAR).filter(ImageFilter.GaussianBlur(radius=100))

    # Center composite with smooth radial blend
    center_composite = ambient_bg.copy()
    ox = int(cx - nw / 2)
    oy = int(cy - nh / 2)

    center_mask = Image.new('L', (nw, nh), 0)
    for y in range(nh):
        dy = y - nh / 2.0
        for x in range(nw):
            dx = x - nw / 2.0
            r = math.sqrt(dx*dx + dy*dy)
            if r <= 215.0:
                val = 255
            elif r < 265.0:
                # Smooth cosine transition
                f = 0.5 * (1.0 + math.cos(math.pi * (r - 215.0) / 50.0))
                val = int(f * 255)
            else:
                val = 0
            center_mask.putpixel((x, y), val)

    center_mask = center_mask.filter(ImageFilter.GaussianBlur(radius=4))
    center_composite.paste(scaled_orig, (ox, oy), center_mask)

    # Master elliptical Quartic window to fade seamlessly into pure black (#000000)
    # Rx = 1080px (wide horizontal spread spanning the viewport)
    # Ry = 390px (vertical spread reaching top and bottom with zero cutoff)
    Rx = 1080.0
    Ry = 390.0

    final_img = Image.new('RGB', (bw, bh), (0, 0, 0))
    comp_pixels = center_composite.load()
    final_pixels = final_img.load()

    for y in range(bh):
        dy = (y - cy) / Ry
        for x in range(bw):
            dx = (x - cx) / Rx
            d2 = dx*dx + dy*dy
            if d2 < 1.0:
                # Quartic smooth decay: (1 - d2)^2.2
                weight = (1.0 - d2) ** 2.2
                r, g, b = comp_pixels[x, y]
                final_pixels[x, y] = (int(r * weight), int(g * weight), int(b * weight))
            else:
                final_pixels[x, y] = (0, 0, 0)

    final_img.save(output_path, 'PNG')
    print(f"[OK] Generated {output_path} successfully!")

if __name__ == '__main__':
    create_panoramic_banner()
