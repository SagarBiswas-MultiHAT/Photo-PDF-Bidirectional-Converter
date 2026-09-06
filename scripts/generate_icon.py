"""Generate the app icon (assets/icon.ico) for the Photo-PDF converter.

Draws a simple, clean mark: a rounded document shape with a photo mountain
motif on top and a PDF arrow motif below, hinting at the two-way conversion.
Run once; the output is committed to the repo.
"""

from pathlib import Path

from PIL import Image, ImageDraw

OUTPUT = Path(__file__).resolve().parent.parent / "assets" / "icon.ico"


def rounded_rect(draw, xy, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def draw_icon(size: int) -> Image.Image:
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    s = size / 256.0  # scale factor, design in a 256 grid

    # Background: rounded square with a soft blue gradient feel (two tones).
    rounded_rect(
        draw,
        (8 * s, 8 * s, 248 * s, 248 * s),
        radius=48 * s,
        fill=(37, 99, 235, 255),
    )
    rounded_rect(
        draw,
        (8 * s, 8 * s, 248 * s, 120 * s),
        radius=48 * s,
        fill=(59, 130, 246, 255),
    )

    # Top half: a "photo" card with a mountain and sun.
    card = (44 * s, 36 * s, 212 * s, 118 * s)
    rounded_rect(draw, card, radius=14 * s, fill=(255, 255, 255, 255))

    # Sun
    sun_r = 12 * s
    sun_c = (178 * s, 62 * s)
    draw.ellipse(
        (sun_c[0] - sun_r, sun_c[1] - sun_r, sun_c[0] + sun_r, sun_c[1] + sun_r),
        fill=(250, 204, 21, 255),
    )

    # Mountains
    draw.polygon(
        [
            (56 * s, 106 * s),
            (96 * s, 58 * s),
            (128 * s, 96 * s),
            (150 * s, 74 * s),
            (200 * s, 106 * s),
        ],
        fill=(16, 122, 87, 255),
    )

    # Bottom half: a "PDF" page with the two-way arrows.
    page = (60 * s, 136 * s, 196 * s, 224 * s)
    rounded_rect(draw, page, radius=10 * s, fill=(255, 255, 255, 255))

    # Two-way arrow between photo and PDF.
    arrow_y = 180 * s
    # Right arrow (photo -> PDF)
    draw.polygon(
        [
            (78 * s, arrow_y - 10 * s),
            (78 * s, arrow_y + 10 * s),
            (106 * s, arrow_y + 10 * s),
            (106 * s, arrow_y + 20 * s),
            (126 * s, arrow_y),
            (106 * s, arrow_y - 20 * s),
            (106 * s, arrow_y - 10 * s),
        ],
        fill=(37, 99, 235, 255),
    )
    # Left arrow (PDF -> photo)
    draw.polygon(
        [
            (178 * s, arrow_y - 10 * s),
            (178 * s, arrow_y + 10 * s),
            (150 * s, arrow_y + 10 * s),
            (150 * s, arrow_y + 20 * s),
            (130 * s, arrow_y),
            (150 * s, arrow_y - 20 * s),
            (150 * s, arrow_y - 10 * s),
        ],
        fill=(16, 122, 87, 255),
    )

    return img


def main() -> None:
    sizes = [16, 24, 32, 48, 64, 128, 256]
    base = draw_icon(256)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    base.save(OUTPUT, format="ICO", sizes=[(s, s) for s in sizes])
    print(f"Written: {OUTPUT}")


if __name__ == "__main__":
    main()
