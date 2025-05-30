from _cdolphin import gui

def add_osd_message(message: str, duration_ms: int = 2000, color_argb: int = 0xFFFFFF30):
    return gui._add_osd_message(message, duration_ms, color_argb)

def draw_line(a, b, color, thickness = 1):
    gui._draw_line(a[0], a[1], b[0], b[1], color, thickness)

def draw_rect(a, b, color, rounding = 0, thickness = 1):
    gui._draw_rect(a[0], a[1], b[0], b[1], color, rounding, thickness)

def draw_rect_filled(a, b, color, rounding= 0):
    gui._draw_rect_filled(a[0], a[1], b[0], b[1], color, rounding)

def draw_quad(a, b, c, d, color, thickness = 1):
    gui._draw_quad(a[0], a[1], b[0], b[1], c[0], c[1], d[0], d[1], color, thickness)

def draw_quad_filled(a, b, c, d, color):
    gui._draw_quad_filled(a[0], a[1], b[0], b[1], c[0], c[1], d[0], d[1], color)

def draw_triangle(a, b, c, color, thickness = 1):
    gui._draw_triangle(a[0], a[1], b[0], b[1], c[0], c[1], color, thickness)

def draw_triangle_filled(a, b, c, color):
    gui._draw_triangle_filled(a[0], a[1], b[0], b[1], c[0], c[1], color)

def draw_circle(center, radius, color, num_segments = None, thickness = 1):
    if num_segments is None:
        num_segments = 8 + int(radius // 50)
    gui._draw_circle(center[0], center[1], radius, color, num_segments, thickness)

def draw_circle_filled(center, radius, color, num_segments = None):
    if num_segments is None:
        num_segments = 8 + int(radius // 50)
    gui._draw_circle_filled(center[0], center[1], radius, color, num_segments)

def draw_text(pos, color, text):
    gui._draw_text(pos[0], pos[1], color, text)

def draw_polyline(points, color, closed = False, thickness = 1):
    gui._draw_polyline(points, color, closed, thickness)

def draw_convex_poly_filled(points, color):
    gui._draw_convex_poly_filled(points, color)