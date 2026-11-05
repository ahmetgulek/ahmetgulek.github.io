import os, re, sys, html
sys.path.insert(0, os.path.dirname(__file__))
from content2 import *
# Run from anywhere: ~/.jobtracker-venv/bin/python tools/buildA.py writes index.html, research.html, style.css at the repo root.
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = {p["id"]: p for p in PAPERS}
e = html.escape
def emph(s): return re.sub(r"\*([^*]+)\*", r"<em>\1</em>", e(s))
def rich(s): return re.sub(r"_\{([^}]*)\}", r"<sub>\1</sub>", e(s))
GA = """<script async src="https://www.googletagmanager.com/gtag/js?id=G-97FFQFKGC9"></script>
<script>window.dataLayer = window.dataLayer || []; function gtag(){dataLayer.push(arguments);} gtag('js', new Date()); gtag('config', 'G-97FFQFKGC9');</script>"""

# ---------- schematics (inline SVG, currentColor + --accent) ----------
ARROW = '<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="currentColor"/></marker></defs>'
def node(x,y,label,fill="none",r=26,tc="currentColor"):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="currentColor" stroke-width="1.5"/><text x="{x}" y="{y+6}" text-anchor="middle" font-size="18" font-style="italic" fill="{tc}">{label}</text>'
def arrow(x1,y1,x2,y2,dash=False,color="currentColor"):
    d = ' stroke-dasharray="6 5"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="1.6"{d} marker-end="url(#ah)"/>'
def txt(x,y,s,size=14,anchor="middle",extra=""):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" {extra}>{s}</text>'

SVG_NETWORK = f'''<svg viewBox="0 0 560 290" class="schematic" role="img" aria-label="Four-firm network">{ARROW}<g font-family="inherit" fill="currentColor">
{node(120,80,"i₁","#bfe3bf")}{node(400,80,"i₂","#b9cbe6")}{node(400,230,"i₃","#f0b9b9")}{node(120,230,"i₄","#dcc2e3")}
{arrow(148,80,372,80)}{arrow(400,108,400,202)}{arrow(148,230,372,230)}
{arrow(520,26,428,62,True,"#b23b3b")}{txt(548,20,"Immigration",14,"end",'fill="#b23b3b" font-weight="600"')}
{txt(260,66,"Downstream-2",13)}{txt(414,160,"Upstream",13,"start")}{txt(260,256,"Downstream-1",13)}
</g></svg>'''

def chain(y, title, s_fill, c_fill, s_lab, j_lab, c_lab, f_lab, b_lab, b_color, extra=""):
    BOLD='font-weight="600"'; DIM='opacity=".75"'
    FL='fill="#2e7d32" font-weight="600"'; BL='fill="'+b_color+'" font-weight="600"'
    return (txt(20,y-48,title,15,"start",BOLD)
            + node(90,y,"S",s_fill) + node(300,y,"J","var(--accent)",26,"#fff") + node(510,y,"C",c_fill)
            + arrow(118,y,272,y) + arrow(328,y,482,y)
            + txt(90,y+44,"supplier",12) + txt(300,y+44,"exposed industry",12) + txt(510,y+44,"customer",12)
            + txt(90,y+62,s_lab,12,"middle",DIM) + txt(300,y+62,j_lab,12,"middle",DIM) + txt(510,y+62,c_lab,12,"middle",DIM)
            + txt(405,y-12,f_lab,13,"middle",FL) + txt(195,y-12,b_lab,13,"middle",BL) + extra)
SVG_CHAINS = f'''<svg viewBox="0 0 620 400" class="schematic" role="img" aria-label="Two propagation chains">{ARROW}<g font-family="inherit" fill="currentColor">
{chain(100,"A labor-supply shock travels both ways (JMP-1)","#dcefdc","#dcefdc","sales ↑, wage ↑","wage ↓, price ↓","input cheaper, wage ↑","forward +","backward +","#2e7d32")}
{chain(290,"A productivity shock travels forward, and hurts suppliers","#f6dcdc","#dcefdc","sales ↓, wage ↓","price ↓, wage 0","input cheaper, wage ↑","forward +","direct backward 0","#777")}
<path d="M500 316 C 420 380, 180 380, 100 316" fill="none" stroke="#b23b3b" stroke-width="1.4" stroke-dasharray="5 4" marker-end="url(#ah)"/>
{txt(300,392,"C cuts its whole input bill, including S; J sells less, so J buys less from S",12,"middle",'fill="#b23b3b"')}
</g></svg>'''

SVG_TWOSIDES = f'''<svg viewBox="0 0 680 230" class="schematic" role="img" aria-label="Immigration and minimum wage as two sides of one chain">{ARROW}<g font-family="inherit" fill="currentColor">
<rect x="210" y="20" width="260" height="190" rx="8" fill="none" stroke="currentColor" stroke-width="1.2" opacity=".6"/>
{txt(340,52,"Local wage shock",15,"middle",'font-weight="600"')}{txt(340,74,"↓",14)}{txt(340,94,"costs and prices of local firms",13)}{txt(340,116,"↓",14)}{txt(340,136,"their buyers and suppliers",13)}{txt(340,158,"↓",14)}{txt(340,178,"labor demand and sales elsewhere",13)}
<rect x="10" y="60" width="160" height="90" rx="8" fill="var(--accent)" opacity=".9"/>{txt(90,90,"Immigration",15,"middle",'fill="#fff" font-weight="600"')}{txt(90,112,"labor supply ↑",13,"middle",'fill="#fff"')}{txt(90,132,"wages ↓",13,"middle",'fill="#fff"')}
{txt(90,172,"JMP-1",12,"middle",'opacity=".7"')}
<rect x="510" y="60" width="160" height="90" rx="8" fill="#2b4a6f" opacity=".9"/>{txt(590,90,"Minimum wage",15,"middle",'fill="#fff" font-weight="600"')}{txt(590,112,"set by law",13,"middle",'fill="#fff"')}{txt(590,132,"wages ↑",13,"middle",'fill="#fff"')}
{txt(590,172,"in progress",12,"middle",'opacity=".7"')}
{arrow(172,105,206,105)}{arrow(508,105,474,105)}
{txt(340,224,"Same forces, opposite sign",13,"middle",'fill="var(--accent)" font-weight="600"')}
</g></svg>'''
SVGS = {"network": SVG_NETWORK, "chains": SVG_CHAINS, "twosides": SVG_TWOSIDES}

# ---------- helpers ----------
def md(s):
    """Escape, then [text](url) -> link and *x* -> italics."""
    s = e(s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2" target="_blank">\1</a>', s)
    return re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)

def head(title, active):
    items = [("About", "index.html#about", "about"), ("Research", "research.html", "research"),
             ("Press", "index.html#press", "press"), ("CV", "CV.pdf", "cv"), ("Contact", "index.html#contact", "contact")]
    nav = "".join(f'<li><a href="{h}"{" class=active" if a == active else ""}{" target=_blank" if a == "cv" else ""}>{t}</a></li>'
                  for t, h, a in items)
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
{GA}
<link rel="stylesheet" href="style.css"></head><body>
<nav><div class="container"><a class="nav-name" href="index.html">{e(NAME)}</a><ul>{nav}</ul></div></nav>
"""
FOOT = '<footer><p>© 2026 Ahmet Gulek · Last updated November 2026</p></footer></body></html>'

def meta_line(p):
    """Old-site italic line: 'Job Market Paper 2, with A and B. Status.'"""
    first = ", ".join(x for x in [p["tag"], p["coauthors"]] if x)
    if first and not p["tag"]: first = first[0].upper() + first[1:]
    out = first + (". " if first and p["status"] else "") + p["status"]
    return e(out + ("." if out and not out.endswith(".") else ""))

def paper_box(p, readmore=False):
    links = [f'<a href="{e(u)}" target="_blank">[{e(t)}]</a>' for t, u in p["links"]]
    if readmore: links.append(f'<a href="research.html#{p["id"]}">[Read more]</a>')
    head_ = f'<b>{e(p["title"])}</b><br><i>{meta_line(p)}</i> {" ".join(links)}'
    if p["abstract"]:
        return f'<details id="{p["id"]}-box"><summary>{head_}</summary><p class="abstract">{e(p["abstract"])}</p></details>'
    return f'<div class="wip-item" id="{p["id"]}-box">{head_}</div>'

# ---------- index ----------
def index():
    h = head(NAME, "about")
    links = ' · '.join(f'<a href="{e(u)}"{"" if u.startswith("mailto:") else " target=_blank"}>{e(t)}</a>' for t, u in LINKS)
    h += f"""<header class="container" id="about"><img src="assets/profile.jpg" alt="Ahmet Gulek" class="profile-pic">
<div><h1>{e(NAME)}</h1>{f'<p class="title">{e(TITLE)}</p>' if TITLE else ""}<p class="institution">{e(AFFIL)}</p>
<p class="bio">{emph(BIO)}</p><p class="linkrow">{links}</p></div></header>
<main class="container"><section id="research"><h2>Research <a class="more" href="research.html">Research overview</a></h2>"""
    for sid, stitle in SECTIONS:
        h += f'<h3>{stitle}</h3>'
        for p in [p for p in PAPERS if p["sec"] == sid]:
            h += paper_box(p, readmore=(sid == "jmp"))
    h += '</section><section id="press"><h2>In the Press and Policy</h2><ul class="press">'
    for outlet, what, url, yr, kind in PRESS:
        title = f'<a href="{e(url)}" target="_blank">{e(what)}</a>' if url else e(what)
        label = f"Referenced by {outlet}" if kind == "referenced" else outlet
        h += f'<li><b>{e(label)}</b>, {e(yr)}: {title}</li>'
    h += ('</ul></section><section id="contact"><h2>Contact</h2><p><a href="mailto:agulek@stanford.edu">agulek@stanford.edu</a> · '
          '<a href="mailto:agulek@mit.edu">agulek@mit.edu</a><br>Stanford Immigration Policy Lab, 616 Jane Stanford Way, Stanford, CA 94305</p></section></main>')
    return h + FOOT

# ---------- research ----------
def figure(src, title, note):
    if src.startswith("svg:"):
        fig = SVGS[src[4:]]
    else:
        fig = f'<a href="assets/img/{src}" target="_blank"><img src="assets/img/{src}" alt="{e(title)}" loading="lazy"></a>'
    cap = f'<b>{e(title)}</b>' + (f' {rich(note)}' if note else "")
    return f'<figure class="ex"><div class="exfig">{fig}</div><figcaption>{cap}</figcaption></figure>'

def restriction_box():
    rows = "".join(f'<tr><td>{e(a)}</td><td class="num">{e(b)}</td></tr>' for a, b in RESTRICTION)
    return (f'<div class="cfbox"><p class="cftitle">{e(RESTRICTION_TITLE)}</p><table class="cf">{rows}</table>'
            f'<p class="takeaway">{e(TAKEAWAY[0])}</p><p class="takeaway2">{e(TAKEAWAY[1])}</p></div>')

def banner(p):
    links = " ".join(f'<a href="{e(u)}" target="_blank">[{e(t)}]</a>' for t, u in p["links"])
    co = f'<p class="bco">{e(p["coauthors"][0].upper() + p["coauthors"][1:])}</p>' if p["coauthors"] else ""
    return (f'<div class="banner" id="{p["id"]}"><p class="blabel">{e(p["tag"])}</p><h2>{e(p["title"])}</h2>{co}'
            f'<p class="bstatus">{e(p["status"])} {links}</p></div>')

def research():
    h = head("Research · " + NAME, "research")
    h += f'<main class="container"><h1 class="pagetitle">Research</h1><p class="lede">{e(OPENING)}</p>'
    h += '<p class="toc">' + "".join(f'<a href="#{i}">{e(t)}</a>' for i, t in TOC) + '</p>'
    for b in RESEARCH:
        k = b[0]
        if k == "banner":    h += banner(P[b[1]])
        elif k == "section": h += f'<h2 class="section" id="{b[1]}">{e(b[2])}</h2>'
        elif k == "h3":      h += f'<h3>{e(b[1])}</h3>'
        elif k == "p":       h += f'<p>{md(b[1])}</p>'
        elif k == "list":    h += '<ul class="forces">' + "".join(f'<li>{e(x)}</li>' for x in b[1]) + '</ul>'
        elif k == "fig":     h += figure(*b[1:])
        elif k == "row":     h += f'<div class="figrow n{len(b[1])}">' + "".join(figure(*x) for x in b[1]) + '</div>'
        elif k == "box":     h += restriction_box()
        elif k == "papers":
            h += (f'<h3>{e(b[1])}</h3>' if b[1] else "") + "".join(paper_box(P[i]) for i in b[2])
    return h + '</main>' + FOOT

# Old-site look (main branch style.css + its inline <style>), extended for the research page.
CSS = """
:root{--accent:#003366}
body{font-family:'Georgia',serif;line-height:1.6;color:#333;margin:0;padding:0;background:#fdfdfd;text-align:justify}
html{scroll-padding-top:20px}
.container{width:85%;max-width:900px;margin:0 auto;padding:20px 0}
a{color:blue;text-decoration:underline}
nav{background:#003366;color:white;padding:10px 0;box-shadow:0 2px 5px rgba(0,0,0,0.1)}
nav .container{display:flex;justify-content:space-between;align-items:center;padding:10px 0}
.nav-name{font-size:24px;font-weight:bold;margin-left:10px;color:white;text-decoration:none}
nav ul{list-style:none;display:flex;margin:0 10px 0 0;padding:0}
nav ul li{margin-left:20px}
nav ul li a{color:white;text-decoration:none;font-weight:500}
nav ul li a:hover,nav ul li a.active{text-decoration:underline}
header{display:flex;flex-wrap:wrap;align-items:center;margin-top:30px;border-bottom:1px solid #ddd;padding-bottom:20px}
.profile-pic{width:300px;height:300px;object-fit:cover;object-position:top center;border-radius:50%;margin-right:30px}
h1{font-size:32px;margin-bottom:10px}
.title{font-size:20px;font-weight:500}
.institution{font-style:italic;margin-bottom:10px}
.bio{margin-top:10px}
.linkrow{text-align:left}
section{margin-bottom:40px}
h2{font-size:26px;color:#003366;margin-bottom:10px;border-bottom:1px solid #ccc;padding-bottom:5px}
h2 .more{font-size:16px;font-weight:normal;float:right;margin-top:8px}
h3{font-size:22px;margin-top:20px;color:#333}
details{margin-bottom:15px;padding:10px;border:1px solid #ccc;border-radius:5px;background-color:#f9f9f9}
summary{cursor:pointer;font-size:16px}
summary::marker{color:#003366}
.abstract{font-size:15px;color:#555;margin-top:10px;line-height:1.4}
.wip-item{margin-bottom:15px;padding:10px;border:1px solid #ccc;border-radius:5px;background-color:#f9f9f9;font-size:16px}
.press{padding-left:20px;text-align:left}.press li{margin-bottom:8px}
footer{background:#f2f2f2;text-align:center;padding:10px 0;border-top:1px solid #ddd;font-size:14px;color:#777}
/* research page */
.pagetitle{margin-top:20px}
.lede{font-size:18px}
.toc{display:flex;flex-wrap:wrap;gap:10px;margin:20px 0 30px}
.toc a{display:inline-block;padding:6px 14px;border:1px solid #003366;border-radius:5px;color:#003366;text-decoration:none;font-size:16px;background:#fff}
.toc a:hover{background:#003366;color:#fff}
.banner{background:#003366;color:#fff;border-radius:5px;padding:22px 26px;margin:50px 0 24px;text-align:left}
.banner .blabel{margin:0;font-size:14px;letter-spacing:.12em;text-transform:uppercase;opacity:.85}
.banner h2{color:#fff;border:0;margin:6px 0 6px;padding:0;font-size:26px;line-height:1.3}
.banner .bco{margin:0;font-style:italic}
.banner .bstatus{margin:6px 0 0;font-size:15px}
.banner a{color:#fff}
h2.section{margin-top:50px}
.forces{margin-top:0}.forces li{margin-bottom:6px}
.ex{margin:16px 0 24px}
.exfig{background:#fff;border:1px solid #ccc;border-radius:5px;padding:12px;text-align:center}
.exfig img,.exfig svg{max-width:100%;height:auto;max-height:400px}.exfig a{display:block}
.schematic{width:100%;max-width:560px;color:#333}.schematic[aria-label='Four-firm network']{max-width:400px}
figcaption{font-size:15px;color:#555;line-height:1.4;margin-top:8px;text-align:left}figcaption b{display:block;color:#333}
.figrow{display:grid;gap:14px;margin:16px 0 8px}
.figrow.n2{grid-template-columns:1fr 1fr}.figrow.n3{grid-template-columns:1fr 1fr 1fr}
.figrow .ex{margin:0}.figrow .exfig{padding:6px}
.cfbox{border:1px solid #ccc;border-radius:5px;background:#f9f9f9;padding:16px 22px;margin:16px 0 24px;text-align:left}
.cftitle{font-weight:bold;margin:0 0 8px;color:#003366}
.cf{border-collapse:collapse;width:100%;font-size:16px}.cf td{padding:5px 0;border-bottom:1px dotted #ccc}
.cf td.num{text-align:right;color:#003366;font-weight:bold;white-space:nowrap;padding-left:12px}
.takeaway{font-size:20px;font-weight:bold;margin:18px 0 4px;text-align:center}
.takeaway2{text-align:center;color:#555;margin:0;font-style:italic}
@media (max-width:700px){.figrow.n2,.figrow.n3{grid-template-columns:1fr}}
@media (max-width:600px){
  body{text-align:left}
  header{flex-direction:column;text-align:center}
  .profile-pic{width:200px;height:200px;margin:0 auto 20px}
  header .bio{text-align:left}
  nav .container{flex-direction:column}
  nav ul{flex-wrap:wrap;justify-content:center;margin:8px 0 0}
  nav ul li{margin:4px 10px}
  h2 .more{float:none;display:block;margin:4px 0 0}
  .banner{padding:16px 18px}.banner h2{font-size:22px}
  .cf td.num{white-space:normal}
  .cfbox{padding:12px 14px}
}
"""

os.makedirs(OUT, exist_ok=True)
open(os.path.join(OUT, "index.html"), "w").write(index())
open(os.path.join(OUT, "research.html"), "w").write(research())
open(os.path.join(OUT, "style.css"), "w").write(CSS)
print("built", OUT)
