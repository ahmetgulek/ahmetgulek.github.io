import os, re, sys, html
sys.path.insert(0, os.path.dirname(__file__))
from content2 import *
# Run from anywhere: ~/.jobtracker-venv/bin/python tools/buildA.py writes index.html, research.html, style.css at the repo root.
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = {p["id"]: p for p in PAPERS}
e = html.escape
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

SVG_NETWORK = f'''<svg viewBox="0 0 620 300" class="schematic" role="img" aria-label="Four-firm network">{ARROW}<g font-family="inherit" fill="currentColor">
{node(130,80,"i₁")}{node(430,80,"i₂","var(--accent)",26,"#fff")}{node(430,230,"i₃")}{node(130,230,"i₄")}
{arrow(158,80,402,80)}{arrow(430,108,430,202)}{arrow(158,230,402,230)}
{arrow(560,30,460,64,True,"var(--accent)")}{txt(575,24,"Immigration",14,"end",'fill="var(--accent)" font-weight="600"')}
{txt(280,66,"Downstream-2 exposure",13)}{txt(445,160,"Upstream exposure",13,"start")}{txt(280,252,"Downstream-1 exposure",13)}
{txt(130,128,"supplier of i₂",12,"middle",'opacity=".7"')}{txt(430,30,"host-region firm",12,"middle",'opacity=".7"')}{txt(430,278,"buyer of i₂ and i₄",12,"middle",'opacity=".7"')}{txt(130,278,"other supplier of i₃",12,"middle",'opacity=".7"')}
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
{chain(100,"A labor-supply shock travels both ways (Gulek, 2025)","#dcefdc","#dcefdc","sales ↑, wage ↑","wage ↓, price ↓","input cheaper, wage ↑","forward +","backward +","#2e7d32")}
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
def head(title, active):
    nav = "".join(f'<a href="{h}"{" class=active" if a==active else ""}{" target=_blank" if a=="cv" else ""}>{t}</a>' for t,h,a in
                  [("About","index.html#about","about"),("Research","research.html","research"),("Press","index.html#press","press"),("CV","CV.pdf","cv"),("Contact","index.html#contact","contact")])
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
{GA}
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,400;0,600;1,400&family=Source+Sans+3:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css"></head><body>
<header class="top"><div class="wrap"><a class="brand" href="index.html">{e(NAME)}</a><nav>{nav}</nav></div></header>
<main class="wrap">"""
FOOT = '</main><footer class="wrap"><p>© 2026 Ahmet Gulek · Last updated November 2026</p></footer></body></html>'

def status_html(p):
    parts = []
    if p["tag"]: parts.append(f'<span class="tag">{e(p["tag"])}</span>')
    if p["status"]: parts.append(f'<span class="status">{e(p["status"])}</span>')
    return " ".join(parts)
def links_html(p, readmore=True):
    out = [f'<a href="{e(u)}" target="_blank">{e(t)}</a>' for t,u in p["links"]]
    if readmore: out.append(f'<a href="research.html#{p["id"]}">Read more</a>')
    return f'<span class="links">{" ".join(out)}</span>'

# ---------- index ----------
def index():
    h = head(NAME, "about")
    h += f"""<section id="about" class="hero"><img src="assets/profile.jpg" alt="Ahmet Gulek" class="photo">
<div><h1>{e(NAME)}</h1><p class="role">{e(TITLE)}</p><p class="affil">{e(AFFIL)}</p><p class="bio">{e(BIO)}</p>
<p class="linkrow">{' · '.join(f'<a href="{e(u)}"{"" if u.startswith("mailto:") else " target=_blank"}>{e(t)}</a>' for t,u in LINKS)}</p></div></section>
<section id="research"><h2>Research <a class="more" href="research.html">Research overview with figures →</a></h2>"""
    for sid, stitle in SECTIONS:
        h += f'<h3>{stitle}</h3><ul class="papers">'
        for p in [p for p in PAPERS if p["sec"]==sid]:
            h += f'<li id="{p["id"]}"><div class="ptitle">{e(p["title"])}</div>'
            if p["coauthors"]: h += f'<div class="coauth">{e(p["coauthors"])}</div>'
            h += f'<div class="meta">{status_html(p)} {links_html(p)}</div>'
            if p["abstract"]: h += f'<details><summary>Abstract</summary><p class="abs">{e(p["abstract"])}</p></details>'
            h += '</li>'
        h += '</ul>'
    h += '</section><section id="press"><h2>In the Press and Policy</h2><ul class="press">'
    for outlet, what, url, yr, kind in PRESS:
        title = f'<a href="{e(url)}" target="_blank">{e(what)}</a>' if url else e(what)
        label = f"Referenced by {outlet}" if kind == "referenced" else outlet
        h += f'<li><span class="outlet">{e(label)} · {e(yr)}</span> {title}</li>'
    h += '</ul></section><section id="contact"><h2>Contact</h2><p><a href="mailto:agulek@stanford.edu">agulek@stanford.edu</a> · <a href="mailto:agulek@mit.edu">agulek@mit.edu</a><br>Stanford Immigration Policy Lab, 616 Jane Stanford Way, Stanford, CA 94305</p></section>'
    return h + FOOT

# ---------- research ----------
def exhibit(ex):
    src, headline, note = ex
    if src.startswith("svg:"):
        fig = SVGS[src[4:]]
    elif src == "text:restriction":
        rows = "".join(f'<tr><td>{e(a)}</td><td class="num">{e(b)}</td></tr>' for a,b in RESTRICTION)
        return (f'<figure class="ex"><figcaption class="above"><strong>{e(headline)}</strong></figcaption>'
                f'<div class="exfig textfig"><table class="cf">{rows}</table><p class="takeaway">{e(TAKEAWAY[0])}</p><p class="takeaway2">{e(TAKEAWAY[1])}</p></div></figure>')
    else:
        fig = f'<img src="assets/img/{src}" alt="{e(headline)}" loading="lazy">'
    return f'<figure class="ex"><div class="exfig">{fig}</div><figcaption><strong>{e(headline)}</strong> <span>{rich(note)}</span></figcaption></figure>'

def research():
    h = head("Research · " + NAME, "research")
    h += f'<h1 class="pagetitle">Research</h1><p class="lede">{e(OPENING)}</p>'
    h += '<nav class="toc">' + " · ".join(f'<a href="#{i}">{e(t)}</a>' for k,i,t in [b for b in RESEARCH if b[0]=="h2"]) + '</nav>'
    for b in RESEARCH:
        if b[0] == "h2":
            h += f'<h2 id="{b[1]}">{e(b[2])}</h2>'
        elif b[0] == "p":
            h += f'<p>{e(b[1])}</p>'
        elif b[0] == "paper":
            p = P[b[1]]
            parts = [x for x in [e(p["coauthors"]), status_html(p), links_html(p, readmore=False) if p["links"] else ""] if x]
            h += f'<h3 id="{p["id"]}">{e(p["title"])}</h3><p class="meta">' + " · ".join(parts) + '</p>'
        elif b[0] == "exhibits":
            h += '<div class="exhibits">' + "".join(exhibit(ex) for ex in EXHIBITS[b[1]]) + '</div>'
    return h + FOOT

CSS = """
:root{--ink:#1c1c1c;--muted:#5f5f5f;--rule:#dcd8d0;--bg:#fcfbf8;--accent:#7a1f1f}
*{box-sizing:border-box}html{scroll-padding-top:70px}
body{margin:0;background:var(--bg);color:var(--ink);font-family:"Crimson Pro",Georgia,serif;font-size:19px;line-height:1.55}
.wrap{max-width:780px;margin:0 auto;padding:0 20px}
header.top{border-bottom:1px solid var(--rule);background:var(--bg);position:sticky;top:0;z-index:5}
header.top .wrap{display:flex;justify-content:space-between;align-items:center;height:56px}
.brand{font-weight:600;text-decoration:none;color:var(--ink);font-size:21px;border:0}
nav a{font-family:"Source Sans 3",system-ui,sans-serif;font-size:14.5px;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);text-decoration:none;margin-left:20px}
nav a.active,nav a:hover{color:var(--accent)}
a{color:var(--accent);text-decoration:none;border-bottom:1px solid rgba(122,31,31,.3)}a:hover{border-bottom-color:var(--accent)}
nav a,.linkrow a,.toc a,.links a,h2 .more{border:0}
.toc a{margin-left:0}
.pagetitle{margin-top:40px}
p.meta .status{margin-right:0}
h1{font-size:40px;font-weight:600;margin:0 0 4px;line-height:1.1}
h2{font-size:28px;font-weight:600;margin:48px 0 10px;padding-bottom:6px;border-bottom:1px solid var(--rule)}
h2 .more{font-family:"Source Sans 3",sans-serif;font-size:14px;font-weight:400;text-transform:uppercase;letter-spacing:.06em;float:right;margin-top:12px}
h3{font-size:22px;font-weight:600;margin:28px 0 6px;line-height:1.25}
.hero{display:flex;gap:32px;align-items:flex-start;margin-top:40px}
.photo{width:170px;height:170px;border-radius:50%;object-fit:cover;object-position:top center;flex:none}
.role{margin:0;font-size:20px}.affil{margin:2px 0 12px;color:var(--muted);font-style:italic}
.bio{margin:0 0 10px}
.linkrow{font-family:"Source Sans 3",sans-serif;font-size:15px;color:var(--muted);margin:0}
.papers{list-style:none;padding:0;margin:0}.papers li{padding:14px 0;border-bottom:1px dotted var(--rule)}
.ptitle{font-weight:600;font-size:20px;line-height:1.3}.coauth{color:var(--muted);font-style:italic}
.meta{font-family:"Source Sans 3",sans-serif;font-size:14px;margin:5px 0 4px;color:var(--muted)}
.tag{display:inline-block;border:1px solid var(--accent);border-radius:3px;padding:1px 7px;font-size:12.5px;text-transform:uppercase;letter-spacing:.06em;color:var(--accent);background:#fff;margin-right:6px}
.status{font-style:italic;margin-right:8px}
.links a{margin-right:10px;font-weight:600;white-space:nowrap}
details{margin-top:4px}summary{font-family:"Source Sans 3",sans-serif;font-size:14px;color:var(--muted);cursor:pointer}
.abs{color:#444;font-size:17px;margin:6px 0 0}
.press{list-style:none;padding:0}.press li{padding:8px 0;border-bottom:1px dotted var(--rule)}
.outlet{font-family:"Source Sans 3",sans-serif;font-size:13px;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);display:block}
.yr{color:var(--muted);font-size:15px;margin-left:8px}
footer{margin:60px auto 30px;color:var(--muted);font-size:15px;border-top:1px solid var(--rule);padding-top:14px}
/* research page */
.lede{font-size:21px;color:var(--muted);margin-top:4px}
.toc{font-family:"Source Sans 3",sans-serif;font-size:14px;color:var(--muted);margin-bottom:10px}
.exhibits{margin:22px 0 30px;padding:24px 0 4px;border-top:1px solid var(--rule);border-bottom:1px solid var(--rule)}
.ex{margin:0 0 34px}.exfig{background:#fff;border:1px solid var(--rule);padding:16px;text-align:center}
.exfig img,.exfig svg{max-width:100%;height:auto;max-height:440px}
.schematic{width:100%;max-width:620px;color:var(--ink)}
figcaption{font-family:"Source Sans 3",sans-serif;font-size:15px;line-height:1.45;margin-top:10px;color:var(--muted)}
figcaption strong{color:var(--ink);font-weight:600;display:block;font-size:17px;margin-bottom:3px}
figcaption.above{margin:0 0 8px}
.textfig{text-align:left;padding:18px 22px}
.cf{border-collapse:collapse;width:100%;font-size:17px}.cf td{padding:5px 0;border-bottom:1px dotted var(--rule)}.cf td.num{text-align:right;color:var(--accent);font-weight:600;white-space:nowrap}
.takeaway{font-size:22px;font-weight:600;margin:18px 0 4px;text-align:center}.takeaway2{text-align:center;color:var(--muted);margin:0;font-style:italic}
@media(max-width:640px){.hero{flex-direction:column;align-items:center;text-align:center}.photo{width:140px;height:140px}h2 .more{float:none;display:block;margin:4px 0 0}header.top .wrap{height:auto;flex-direction:column;padding:10px 20px}header.top nav a{margin:0 7px;font-size:13px;letter-spacing:.05em}.toc a{margin:0;display:inline}html{scroll-padding-top:110px}.bio,.linkrow{text-align:left}.cf td.num{white-space:normal;padding-left:12px}.exfig{padding:8px}.textfig{padding:12px}body{font-size:18px}}
"""

os.makedirs(OUT, exist_ok=True)
open(os.path.join(OUT,"index.html"),"w").write(index())
open(os.path.join(OUT,"research.html"),"w").write(research())
open(os.path.join(OUT,"style.css"),"w").write(CSS)
print("built", OUT)
