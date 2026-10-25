"""Geometry helpers: glyph outlines to shapely polygons and back to SVG paths."""
from fontTools.pens.basePen import BasePen
from shapely.geometry import Polygon, LineString, MultiPolygon, box
from shapely.ops import unary_union
from shapely import affinity


class FlattenPen(BasePen):
    """Collects contours as lists of points, flattening curves."""

    def __init__(self, glyphSet, steps=24):
        super().__init__(glyphSet)
        self.contours = []
        self._cur = None
        self.steps = steps

    def _moveTo(self, p):
        self._cur = [p]

    def _lineTo(self, p):
        self._cur.append(p)

    def _curveToOne(self, p1, p2, p3):
        p0 = self._cur[-1]
        n = self.steps
        for i in range(1, n + 1):
            t = i / n
            mt = 1 - t
            x = mt**3 * p0[0] + 3 * mt**2 * t * p1[0] + 3 * mt * t**2 * p2[0] + t**3 * p3[0]
            y = mt**3 * p0[1] + 3 * mt**2 * t * p1[1] + 3 * mt * t**2 * p2[1] + t**3 * p3[1]
            self._cur.append((x, y))

    def _closePath(self):
        if self._cur and len(self._cur) >= 3:
            self.contours.append(self._cur)
        self._cur = None

    def _endPath(self):
        self._closePath()


def glyph_polygon(tt, gname):
    """Shapely geometry of a glyph in font units (y up), even-odd filled."""
    gs = tt.getGlyphSet()
    pen = FlattenPen(gs)
    gs[gname].draw(pen)
    geom = None
    for c in pen.contours:
        poly = Polygon(c).buffer(0)
        geom = poly if geom is None else geom.symmetric_difference(poly)
    return geom if geom is not None else Polygon()


def _ring_to_d(coords, fmt):
    pts = list(coords)
    if not pts:
        return ""
    d = "M" + " L".join(fmt(x, y) for x, y in pts[:-1]) + " Z"
    return d


def geom_to_d(geom, scale=1.0, dx=0.0, dy=0.0, flip=True, prec=2):
    """Shapely geometry -> SVG path data. flip=True maps font y-up to svg y-down."""
    def fmt(x, y):
        X = dx + x * scale
        Y = dy - y * scale if flip else dy + y * scale
        return f"{X:.{prec}f} {Y:.{prec}f}"

    polys = []
    if geom.is_empty:
        return ""
    if isinstance(geom, Polygon):
        polys = [geom]
    elif isinstance(geom, MultiPolygon):
        polys = list(geom.geoms)
    else:
        try:
            polys = [g for g in geom.geoms if isinstance(g, Polygon)]
        except AttributeError:
            return ""
    parts = []
    for p in polys:
        parts.append(_ring_to_d(p.exterior.coords, fmt))
        for r in p.interiors:
            parts.append(_ring_to_d(r.coords, fmt))
    return " ".join(parts)


def band(p0, p1, half_width):
    """Rectangle band around the segment p0-p1 extended well beyond both ends."""
    ls = LineString([p0, p1])
    # extend the line by 50% each side so the band covers the terminals fully
    ext = affinity.scale(ls, xfact=2.0, yfact=2.0, origin="center")
    return ext.buffer(half_width, cap_style=2, join_style=2)


def chevron(points, half_width):
    """Mitred, flat-capped polyline as a polygon."""
    return LineString(points).buffer(half_width, cap_style=2, join_style=2, mitre_limit=10)


def rounded_rect(x, y, w, h, r):
    if r <= 0:
        return box(x, y, x + w, y + h)
    return box(x + r, y + r, x + w - r, y + h - r).buffer(r, join_style=1, quad_segs=12)
