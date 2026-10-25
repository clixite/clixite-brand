"""Text to SVG path helpers: shaping with HarfBuzz, outlines with fontTools."""
import os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
import uharfbuzz as hb

ROOT = os.path.dirname(os.path.abspath(__file__))
FS = os.path.join(ROOT, "node_modules", "@fontsource")

FONT_FILES = {
    ("space", 400): "space-grotesk/files/space-grotesk-latin-400-normal.woff2",
    ("space", 500): "space-grotesk/files/space-grotesk-latin-500-normal.woff2",
    ("space", 600): "space-grotesk/files/space-grotesk-latin-600-normal.woff2",
    ("space", 700): "space-grotesk/files/space-grotesk-latin-700-normal.woff2",
    ("inter", 400): "inter/files/inter-latin-400-normal.woff2",
    ("inter", 500): "inter/files/inter-latin-500-normal.woff2",
    ("inter", 600): "inter/files/inter-latin-600-normal.woff2",
    ("inter", 700): "inter/files/inter-latin-700-normal.woff2",
    ("sora", 400): "sora/files/sora-latin-400-normal.woff2",
    ("sora", 500): "sora/files/sora-latin-500-normal.woff2",
    ("sora", 600): "sora/files/sora-latin-600-normal.woff2",
    ("sora", 700): "sora/files/sora-latin-700-normal.woff2",
    ("mono", 500): "jetbrains-mono/files/jetbrains-mono-latin-500-normal.woff2",
    ("instr-it", 400): "instrument-serif/files/instrument-serif-latin-400-italic.woff2",
    ("dmserif-it", 400): "dm-serif-display/files/dm-serif-display-latin-400-italic.woff2",
    ("fraunces-it", 500): "fraunces/files/fraunces-latin-500-italic.woff2",
    ("fraunces-it", 600): "fraunces/files/fraunces-latin-600-italic.woff2",
    ("mono", 700): "jetbrains-mono/files/jetbrains-mono-latin-700-normal.woff2",
}

_cache = {}


def load(family, weight):
    key = (family, weight)
    if key in _cache:
        return _cache[key]
    path = os.path.join(FS, FONT_FILES[key])
    tt = TTFont(path)
    # HarfBuzz needs a raw sfnt: decompress the woff2 into a .ttf once
    ttf_path = os.path.join(ROOT, "fonts", f"{family}-{weight}.ttf")
    os.makedirs(os.path.dirname(ttf_path), exist_ok=True)
    if not os.path.exists(ttf_path):
        tt.flavor = None
        tt.save(ttf_path)
    with open(ttf_path, "rb") as f:
        blob = hb.Blob(f.read())
    face = hb.Face(blob)
    font = hb.Font(face)
    upem = tt["head"].unitsPerEm
    font.scale = (upem, upem)
    _cache[key] = (tt, font, upem)
    return _cache[key]


def shape(family, weight, text, tracking=0.0, features=None):
    """Return list of (glyphname, x_offset_units, y_offset_units, advance) in font units.
    tracking is extra space in units per em fraction (e.g. 0.05 = 5% of em)."""
    tt, font, upem = load(family, weight)
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf, features or {"kern": True, "liga": True})
    glyph_order = tt.getGlyphOrder()
    x = 0.0
    out = []
    track = tracking * upem
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        gname = glyph_order[info.codepoint]
        out.append((gname, x + pos.x_offset, pos.y_offset, pos.x_advance))
        x += pos.x_advance + track
    width = x - track if out else 0
    return out, width, upem


def glyph_path(tt, gname, scale, dx, dy):
    """SVG path data for a glyph at scale, translated to (dx, dy); y flipped."""
    gs = tt.getGlyphSet()
    pen = SVGPathPen(gs)
    tpen = TransformPen(pen, (scale, 0, 0, -scale, dx, dy))
    gs[gname].draw(tpen)
    return pen.getCommands()


def glyph_bounds(tt, gname):
    gs = tt.getGlyphSet()
    bp = BoundsPen(gs)
    gs[gname].draw(bp)
    return bp.bounds  # (xMin, yMin, xMax, yMax) in units or None


def text_paths(family, weight, text, size, x, baseline, tracking=0.0, skip=None):
    """Return (list of dict(char, d, x0, adv), total_width_px).
    size = font size in px (em). skip: set of glyph names to omit (path not drawn but space kept)."""
    tt, font, upem = load(family, weight)
    glyphs, width, _ = shape(family, weight, text, tracking)
    s = size / upem
    items = []
    for gname, gx, gy, adv in glyphs:
        d = "" if (skip and gname in skip) else glyph_path(tt, gname, s, x + gx * s, baseline - gy * s)
        b = glyph_bounds(tt, gname)
        bb = None
        if b:
            bb = (x + (gx + b[0]) * s, baseline - (gy + b[3]) * s, x + (gx + b[2]) * s, baseline - (gy + b[1]) * s)
        items.append(dict(g=gname, d=d, x=x + gx * s, adv=adv * s, bbox=bb))
    return items, width * s


def metrics(family, weight):
    tt, font, upem = load(family, weight)
    os2 = tt["OS/2"]
    return dict(upem=upem, xh=os2.sxHeight, cap=os2.sCapHeight, asc=tt["hhea"].ascent, desc=tt["hhea"].descent)


def stem_width(family, weight, char="l"):
    """Approximate vertical stem width from the glyph 'l' bbox width (units)."""
    tt, font, upem = load(family, weight)
    cmap = tt.getBestCmap()
    g = tt.getGlyphOrder()[0]
    gname = cmap[ord(char)]
    b = glyph_bounds(tt, gname)
    return b[2] - b[0]


if __name__ == "__main__":
    for fam, w in [("space", 500), ("space", 600), ("space", 700), ("sora", 600), ("inter", 600)]:
        m = metrics(fam, w)
        print(fam, w, m, "stem l:", stem_width(fam, w), "x width:", glyph_bounds(load(fam, w)[0], load(fam, w)[0].getBestCmap()[ord('x')]))
