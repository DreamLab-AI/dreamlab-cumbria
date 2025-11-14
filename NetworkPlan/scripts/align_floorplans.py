#!/usr/bin/env python3
"""
Utility to create a vertically stacked composite of the three Fairfield floorplans.

- Reads PNG images in FairfieldSpatial/
- Optionally rescales so widths match.
- Allows manual x/y offsets per floor.
- Outputs FairfieldSpatial/composite_floorplans.png
"""

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
IMG_DIR = ROOT / "FairfieldSpatial"

FLOOR_FILES = [
    ("ground", "Screenshot_20251113_130628.png"),
    ("first", "Screenshot_20251113_130650.png"),
    ("second", "Screenshot_20251113_130721.png"),
]

# User-tweakable parameters: target composite width and per-floor x/y offsets
TARGET_WIDTH = 2000  # pixels
OFFSETS = {
    "ground": (0, 0),
    "first": (0, 50),
    "second": (0, 100),
}


def load_and_normalise(path: Path, target_width: int) -> Image.Image:
    """
    Load a floorplan image, convert to RGBA, and scale it to target_width
    while preserving aspect ratio.
    """
    img = Image.open(path).convert("RGBA")
    w, h = img.size
    if w == target_width:
        return img
    scale = target_width / w
    new_size = (target_width, int(h * scale))
    return img.resize(new_size, Image.LANCZOS)


def build_composite(target_width: int = TARGET_WIDTH) -> Image.Image:
    """
    Stack the normalised floorplan images vertically into a single composite.

    The OFFSETS dict allows manual alignment of structural features (stairs,
    risers, etc.) between floors by shifting each floorplan left/right and
    up/down within its slot.
    """
    layers = []
    for name, fname in FLOOR_FILES:
        img = load_and_normalise(IMG_DIR / fname, target_width)
        dx, dy = OFFSETS.get(name, (0, 0))
        layers.append((name, img, dx, dy))

    total_height = sum(img.height for _, img, _, _ in layers) + max(
        dy for _, _, _, dy in layers
    )
    composite = Image.new("RGBA", (target_width, total_height), (255, 255, 255, 0))

    y_cursor = 0
    for name, img, dx, dy in layers:
        composite.alpha_composite(img, (dx, y_cursor + dy))
        y_cursor += img.height

    return composite


def main() -> None:
    composite = build_composite()
    out_path = IMG_DIR / "composite_floorplans.png"
    composite.convert("RGB").save(out_path, "PNG")
    print(f"Saved composite to {out_path}")


if __name__ == "__main__":
    main()