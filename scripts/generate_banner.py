from PIL import Image, ImageFilter
import os

def create_panoramic_banner():
    logo_path = 'assets/logo.png'
    output_path = 'assets/logo-banner.png'
    
    if not os.path.exists(logo_path):
        raise FileNotFoundError(f"Missing {logo_path}")

    orig = Image.open(logo_path).convert('RGBA')
    ow, oh = orig.size

    # Panoramic dimensions
    bw, bh = 1920, 780
    banner = Image.new('RGBA', (bw, bh), (0, 0, 0, 255))

    # Ambient blurred background to span 1920px edge-to-edge
    bg = orig.resize((bw, bh), Image.Resampling.BILINEAR)
    bg = bg.filter(ImageFilter.GaussianBlur(radius=60))

    # Scaled center logo with complete flower preservation (356px flower in 780px canvas)
    nw, nh = 600, 600
    scaled_orig = orig.resize((nw, nh), Image.Resampling.LANCZOS)

    cx = (bw - nw) // 2
    cy = (bh - nh) // 2

    banner.paste(bg, (0, 0))

    # Smooth feathered circular mask for center logo
    mask = Image.new('L', (nw, nh), 0)
    for y in range(nh):
        for x in range(nw):
            dx = (x - nw/2) / (nw/2)
            dy = (y - nh/2) / (nh/2)
            dist = (dx**6 + dy**6)**0.5
            val = int(max(0, min(1, 1.0 - dist)) * 255)
            mask.putpixel((x, y), val)
    mask = mask.filter(ImageFilter.GaussianBlur(radius=15))

    banner.paste(scaled_orig, (cx, cy), mask)

    # Vertical gradient fade layer:
    # Pure black (#000000) at top (y < 0.22) fading smoothly into the blue aura
    # Bottom fade (y > 0.82) into black
    # Horizontal vignette at edges (x < 0.12 or x > 0.88)
    fade_layer = Image.new('RGBA', (bw, bh), (0, 0, 0, 0))
    for y in range(bh):
        y_norm = y / bh
        top_alpha = int((1.0 - (y_norm / 0.22)) * 255) if y_norm < 0.22 else 0
        bot_alpha = int(((y_norm - 0.82) / 0.18) * 255) if y_norm > 0.82 else 0
        alpha = max(top_alpha, bot_alpha)
        for x in range(bw):
            x_norm = x / bw
            side_alpha = 0
            if x_norm < 0.12:
                side_alpha = int((1.0 - (x_norm / 0.12)) * 255)
            elif x_norm > 0.88:
                side_alpha = int(((x_norm - 0.88) / 0.12) * 255)
            total_a = max(alpha, side_alpha)
            if total_a > 0:
                fade_layer.putpixel((x, y), (0, 0, 0, total_a))

    banner = Image.alpha_composite(banner, fade_layer)
    banner.save(output_path, 'PNG')
    print(f"[OK] Generated {output_path} successfully!")

if __name__ == '__main__':
    create_panoramic_banner()
