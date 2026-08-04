import fitz
import sys

doc = fitz.open('main.pdf')
page = doc[18]  # 第19页，0-indexed
print(f"Page size: {page.rect.width:.2f} x {page.rect.height:.2f} pt")
print(f"Total drawings: {len(page.get_drawings())}")

words = page.get_text('words')
print(f"Total words: {len(words)}")

# Find H_x labels
print("\n=== H_x LABELS ===")
for w in words:
    x0, y0, x1, y1, text, bn, bt, ln = w
    if 'H' in text or '完整' in text or '截断' in text:
        print(f"  text='{text}' x=[{x0:.2f},{x1:.2f}] y=[{y0:.2f},{y1:.2f}]")

# Find dashed elements
drawings = page.get_drawings()
print("\n=== DASHED ELEMENTS ===")
for i, d in enumerate(drawings):
    dashes = d.get('dashes', '')
    if dashes and str(dashes) != '[]':
        items = d.get('items', [])
        pts = []
        for item in items:
            if isinstance(item, (list, tuple)):
                for p in item[1:]:
                    if hasattr(p, 'x') and hasattr(p, 'y'):
                        pts.append(p)
        if pts:
            xs = [p.x for p in pts]
            ys = [p.y for p in pts]
            print(f"  #{i}: dashes={dashes} x=[{min(xs):.2f},{max(xs):.2f}] y=[{min(ys):.2f},{max(ys):.2f}] w={max(xs)-min(xs):.2f} h={max(ys)-min(ys):.2f}")

# Find rectangles (panel borders)
print("\n=== RECTANGLES ===")
for i, d in enumerate(drawings):
    for item in d.get('items', []):
        if isinstance(item, (list, tuple)) and item[0] == 're':
            r = item[1]
            if hasattr(r, 'x0'):
                print(f"  #{i}: ({r.x0:.2f},{r.y0:.2f})-({r.x1:.2f},{r.y1:.2f}) w={r.width:.2f} h={r.height:.2f}")

doc.close()
