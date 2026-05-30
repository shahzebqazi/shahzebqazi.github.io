#!/usr/bin/env python3
"""Inline logo.svg into hero.svg so README <img> renders on GitHub (no external refs)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

IMAGE_RE = re.compile(
    r"<image\b[^>]*\bxlink:href=\"([^\"]+)\"[^>]*/>",
    re.IGNORECASE,
)
VIEWBOX_RE = re.compile(r'viewBox="([^"]+)"', re.IGNORECASE)
SVG_INNER_RE = re.compile(r"<svg[^>]*>(.*)</svg>", re.DOTALL | re.IGNORECASE)
ID_RE = re.compile(r'\bid="([^"]+)"')


def extract_svg_inner(svg_text: str) -> str:
    match = SVG_INNER_RE.search(svg_text)
    if not match:
        raise ValueError("No <svg> root found")
    return match.group(1).strip()


def prefix_ids(fragment: str, prefix: str = "logo") -> str:
    ids = ID_RE.findall(fragment)
    for id_ in sorted(ids, key=len, reverse=True):
        fragment = fragment.replace(f'id="{id_}"', f'id="{prefix}-{id_}"')
        fragment = fragment.replace(f"url(#{id_})", f"url(#{prefix}-{id_})")
        fragment = fragment.replace(f'href="#{id_}"', f'href="#{prefix}-{id_}"')
    return fragment


def parse_image_attrs(image_tag: str) -> tuple[str, str, str, str]:
    def attr(name: str, default: str) -> str:
        m = re.search(rf'\b{name}="([^"]+)"', image_tag)
        return m.group(1) if m else default

    return attr("x", "480"), attr("y", "40"), attr("width", "240"), attr("height", "240")


def inline_hero(hero_path: Path, logo_path: Path | None = None) -> bool:
    hero_text = hero_path.read_text(encoding="utf-8")
    match = IMAGE_RE.search(hero_text)
    if not match:
        return False

    href = match.group(1)
    logo_file = logo_path or hero_path.parent / href
    if not logo_file.is_file():
        raise FileNotFoundError(f"{hero_path}: logo not found at {logo_file}")

    logo_text = logo_file.read_text(encoding="utf-8")
    viewbox = VIEWBOX_RE.search(logo_text)
    viewbox_val = viewbox.group(1) if viewbox else "0 0 128 128"
    logo_inner = prefix_ids(extract_svg_inner(logo_text))
    x, y, w, h = parse_image_attrs(match.group(0))

    nested = (
        f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="{viewbox_val}" aria-hidden="true">\n'
        f"{logo_inner}\n"
        f"</svg>"
    )
    hero_new = IMAGE_RE.sub(nested, hero_text, count=1)
    hero_new = re.sub(r'\s*xmlns:xlink="[^"]*"\s*', " ", hero_new, count=1)
    hero_path.write_text(hero_new, encoding="utf-8")
    return True


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: inline-hero-logo.py <hero.svg> [logo.svg] ...", file=sys.stderr)
        return 1
    status = 0
    for hero_arg in argv[1:]:
        hero = Path(hero_arg)
        if hero.suffix.lower() != ".svg" or "hero" not in hero.name:
            print(f"skip (not a hero path): {hero}", file=sys.stderr)
            status = 2
            continue
        if not inline_hero(hero):
            print(f"skip (no <image>): {hero}", file=sys.stderr)
            status = 2
            continue
        print(f"ok: {hero}")
    return status


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
