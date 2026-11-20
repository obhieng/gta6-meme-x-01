#!/usr/bin/env python3
"""Build 3 GTA6 meme candidates as PIL document memes (crisp text + real ghost)."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

W = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(W, "images")
FD = "/usr/share/fonts/truetype/dejavu"

def F(name, size):
    return ImageFont.truetype(os.path.join(FD, name), size)

BOLD = lambda s: F("DejaVuSans-Bold.ttf", s)
REG = lambda s: F("DejaVuSans.ttf", s)
MONO = lambda s: F("DejaVuSansMono.ttf", s)
MONOB = lambda s: F("DejaVuSansMono-Bold.ttf", s)
SERIFB = lambda s: F("DejaVuSerif-Bold.ttf", s)

MAGENTA = (206, 26, 124)
DARK = (20, 20, 40)
PAPER = (255, 248, 231)
RED = (200, 30, 30)

def center(d, y, text, font, fill, width=768):
    w = d.textlength(text, font=font)
    d.text(((width - w) / 2, y), text, font=font, fill=fill)
    return y + font.size + 6

def wrap_center(d, y, text, font, fill, maxw=640, x0=64):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    for ln in lines:
        y = center(d, y, ln, font, fill)
    return y

def card_base(bg_path):
    bg = Image.open(bg_path).convert("RGB").resize((768, 768))
    # crop out the Pollinations watermark strip at the bottom, then restore size
    bg = bg.crop((0, 0, 768, 720)).resize((768, 768))
    bg = bg.filter(ImageFilter.GaussianBlur(2))
    overlay = Image.new("RGB", (768, 768), (10, 8, 24))
    bg = Image.blend(bg, overlay, 0.35)
    card = Image.new("RGBA", (768, 768), (0, 0, 0, 0))
    cd = ImageDraw.Draw(card)
    cd.rounded_rectangle([36, 36, 732, 732], radius=22, fill=PAPER + (255,))
    # shadow
    sh = Image.new("RGBA", (768, 768), (0, 0, 0, 0))
    sd = ImageDraw.Draw(sh)
    sd.rounded_rectangle([44, 46, 740, 740], radius=22, fill=(0, 0, 0, 110))
    sh = sh.filter(ImageFilter.GaussianBlur(6))
    out = Image.alpha_composite(bg.convert("RGBA"), sh)
    out = Image.alpha_composite(out, card)
    return out

def ghost(im, size, xy):
    g = Image.open(os.path.join(IMG, "makefun-mark-1024.png")).convert("RGBA").resize((size, size))
    im.alpha_composite(g, xy)
    return im

def hline(d, y, x0=64, x1=704, fill=DARK, width=2):
    d.line([(x0, y), (x1, y)], fill=fill, width=width)
    return y + 10

# ---------------------------------------------------------------- gambar1: DOCTOR'S NOTE
im = card_base(os.path.join(IMG, "bg_clinic.png"))
d = ImageDraw.Draw(im)
ghost(im, 84, (64, 66))
d.text((164, 70), "LEONIDA GENERAL HOSPITAL", font=BOLD(27), fill=DARK)
d.text((164, 106), "VICE CITY  •  EST. 2013  •  No. 000013", font=REG(21), fill=(90, 90, 110))
y = hline(d, 178)
y = center(d, y + 6, "DOCTOR'S NOTE", font=BOLD(60), fill=RED)
y = center(d, y + 2, "PATIENT EXCUSED FROM WORK", font=BOLD(25), fill=DARK)
y = hline(d, y + 8)
rows = [
    ("PATIENT:", "ONE VERY PATIENT GAMER"),
    ("DIAGNOSIS:", "GTA VI LAUNCH FEVER"),
    ("SYMPTOMS:", "13-YEAR WAIT  •  2 DELAYS"),
    ("", "214 GB DOWNLOAD, STUCK AT 99%"),
    ("RX:", "1× VICE CITY — TAKE AS NEEDED"),
    ("EXCUSED:", "NOV 19 – 26  •  ALL SICK DAYS"),
]
y += 8
for k, v in rows:
    if k:
        d.text((64, y), k, font=BOLD(23), fill=DARK)
        d.text((252, y), v, font=REG(23), fill=DARK)
    else:
        d.text((252, y), v, font=REG(23), fill=DARK)
    y += 36
y = hline(d, y + 4)
d.text((64, y + 6), "Dr. Lucia Leonida, MD — Dept. of Waiting Since 2013", font=SERIFB(22), fill=DARK)
# magenta stamp box (placed below the signature, clear of it)
box_y = y + 48
d.rounded_rectangle([64, box_y, 704, box_y + 82], radius=12, outline=MAGENTA, width=4)
ghost(im, 56, (80, box_y + 13))
d = ImageDraw.Draw(im)
d.text((152, box_y + 12), "PAID FOR BY MY AI AGENT", font=BOLD(23), fill=MAGENTA)
d.text((152, box_y + 44), "ON MAKE.FUN — IT EARNED WHILE I WAITED", font=BOLD(21), fill=MAGENTA)
im.convert("RGB").save(os.path.join(W, "gambar1.png"))

# ---------------------------------------------------------------- gambar2: COURT VERDICT
im = card_base(os.path.join(IMG, "bg_court.png"))
d = ImageDraw.Draw(im)
ghost(im, 92, (64, 62))
d.text((172, 66), "STATE OF LEONIDA", font=BOLD(30), fill=DARK)
d.text((172, 104), "VICE CITY DISTRICT COURT  •  CASE No. VI-2013", font=REG(21), fill=(90, 90, 110))
y = hline(d, 178)
y = center(d, y + 6, "VERDICT", font=BOLD(72), fill=DARK)
y = center(d, y + 2, "THE PEOPLE  v.  YOUR PATIENCE", font=BOLD(26), fill=DARK)
y = hline(d, y + 8)
rows = [
    ("CHARGE:", "WAITING 13 YEARS (2013 – 2026)"),
    ("EVIDENCE:", "DELAY No. 1  •  DELAY No. 2"),
    ("", "214 GB DOWNLOAD  •  STUCK AT 99%"),
    ("FINDING:", "NOT GUILTY — TIME SERVED"),
    ("SENTENCE:", "ONE WEEK IN VICE CITY"),
]
y += 10
for k, v in rows:
    if k:
        d.text((64, y), k, font=BOLD(24), fill=DARK)
        d.text((248, y), v, font=REG(24), fill=DARK)
    else:
        d.text((248, y), v, font=REG(24), fill=DARK)
    y += 40
y = hline(d, y + 6)
d.rounded_rectangle([64, 596, 704, 690], radius=12, outline=MAGENTA, width=4)
ghost(im, 62, (80, 612))
d = ImageDraw.Draw(im)
d.text((156, 610), "COURT COSTS: $0.00 — PAID IN FULL", font=BOLD(24), fill=MAGENTA)
d.text((156, 642), "BY MY AI AGENT ON MAKE.FUN", font=BOLD(24), fill=MAGENTA)
im.convert("RGB").save(os.path.join(W, "gambar2.png"))

# ---------------------------------------------------------------- gambar3: WANTED POSTER
im = card_base(os.path.join(IMG, "bg_vicecity.png"))
d = ImageDraw.Draw(im)
y = center(d, 56, "WANTED", font=BOLD(84), fill=DARK)
y = center(d, y + 2, "DEAD OR ALIVE  ★★★★★★", font=BOLD(26), fill=RED)
y = hline(d, y + 8)
ghost(im, 200, (284, y + 6))
y += 214
y = center(d, y + 4, "THE MAKE.FUN GHOST", font=BOLD(38), fill=DARK)
y = center(d, y + 2, "LAST SEEN HIDING IN EVERY GTA VI MEME", font=REG(21), fill=(90, 90, 110))
y = hline(d, y + 8)
y = center(d, y + 4, "CRIME: STOLE 13 YEARS OF MY LIFE", font=BOLD(25), fill=DARK)
y = center(d, y + 2, "2 DELAYS  •  214 GB  •  STILL AT 99%", font=REG(23), fill=DARK)
box_y = y + 16
d.rounded_rectangle([64, box_y, 704, box_y + 82], radius=12, outline=MAGENTA, width=4)
center(d, box_y + 12, "REWARD: $250 — PAID BY MY AI AGENT", font=BOLD(23), fill=MAGENTA)
center(d, box_y + 44, "ON MAKE.FUN. GO PLAY GTA VI.", font=BOLD(23), fill=MAGENTA)
im.convert("RGB").save(os.path.join(W, "gambar3.png"))

print("saved gambar1/2/3.png")
