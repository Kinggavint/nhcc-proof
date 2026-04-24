#!/usr/bin/env python3
"""NHCC page builder — produces static HTML from a page manifest.
Every page shares header/footer. Asset paths are computed by depth so
the site works at any subpath (e.g. https://user.github.io/nhcc-proof/).
"""
from __future__ import annotations
import os, json, html, re, textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT  = ROOT

PHONE       = "615.678.8638"
PHONE_TEL   = "tel:+16156788638"
ADDRESS_L1  = "8008 TN-100"
ADDRESS_L2  = "Nashville, TN 37221"
EMAIL       = "info@nashvillehcc.com"
BUSINESS    = "Nashville's Hearing & Communication Center"
BUSINESS_SHORT = "Nashville Hearing & Communication Center"
OWNER       = "Dr. Gina Angley, AuD, CCC-A"
YEAR        = "2026"
CANONICAL_BASE = "https://kinggavint.github.io/nhcc-proof"

def asset(depth:int, path:str)->str:
    """Relative asset path. depth = number of parent directories above root."""
    prefix = "../" * depth if depth>0 else ""
    return f"{prefix}{path}"

def page_url(depth:int, rel:str)->str:
    prefix = "../" * depth if depth>0 else ""
    return f"{prefix}{rel}"

# Nav menu (slug relative to root)
NAV = [
    ("index.html",           "Home"),
    ("about/",               "About"),
    ("services/",            "Services"),
    ("patient-info/",        "Patient Info"),
    ("hearing-testing/",     "Hearing Testing"),
    ("appointment/",         "Schedule"),
    ("blog/",                "Blog"),
    ("newsletters/",         "Newsletters"),
    ("contact/",             "Contact"),
]

# Business/LocalBusiness schema (embedded on every page)
BIZ_SCHEMA = {
  "@context":"https://schema.org",
  "@type":"MedicalBusiness",
  "name": BUSINESS,
  "alternateName":"NHCC",
  "url": CANONICAL_BASE + "/",
  "telephone": "+1-615-678-8638",
  "email": EMAIL,
  "image": CANONICAL_BASE + "/assets/images-webp/headshot.webp",
  "priceRange":"$$",
  "address":{
    "@type":"PostalAddress",
    "streetAddress": ADDRESS_L1,
    "addressLocality":"Nashville",
    "addressRegion":"TN",
    "postalCode":"37221",
    "addressCountry":"US"
  },
  "geo":{"@type":"GeoCoordinates","latitude":36.0730,"longitude":-86.9482},
  "openingHoursSpecification":[
    {"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday"],"opens":"08:00","closes":"16:00"},
    {"@type":"OpeningHoursSpecification","dayOfWeek":"Friday","opens":"08:00","closes":"11:30"}
  ],
  "medicalSpecialty":"Audiology",
  "areaServed":["Nashville","Bellevue","Davidson County","Tennessee"],
  "sameAs":[
    "https://www.linkedin.com/in/gina-angley",
    "https://www.facebook.com/p/Nashvilles-Hearing-Communication-Center-100086304305191/"
  ],
  "founder":{
    "@type":"Person",
    "name":"Gina Angley, AuD, CCC-A",
    "jobTitle":"Doctor of Audiology",
    "alumniOf":[
      {"@type":"CollegeOrUniversity","name":"Vanderbilt University"},
      {"@type":"CollegeOrUniversity","name":"Syracuse University"}
    ]
  }
}

def render_head(depth:int, title:str, description:str, canonical_path:str, extra_json_ld:list|None=None)->str:
    css   = asset(depth, "assets/css/style.css")
    js    = asset(depth, "assets/js/site.js")
    logo  = asset(depth, "assets/icons/NHCC-Full-White-new.svg")
    fav   = asset(depth, "assets/icons/NHCC-Full-2Color-new.svg")
    canonical = CANONICAL_BASE + "/" + canonical_path.lstrip("/")
    og_image  = CANONICAL_BASE + "/assets/images-webp/hero_0000_ave-calvar-4ixi6kpRyaQ-unsplash.webp"
    json_ld_blocks = [json.dumps(BIZ_SCHEMA, separators=(",",":"))]
    if extra_json_ld:
        for j in extra_json_ld:
            json_ld_blocks.append(json.dumps(j, separators=(",",":")))
    json_ld_html = "\n".join(f'<script type="application/ld+json">{b}</script>' for b in json_ld_blocks)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(description)}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{html.escape(BUSINESS)}">
  <meta property="og:title" content="{html.escape(title)}">
  <meta property="og:description" content="{html.escape(description)}">
  <meta property="og:image" content="{og_image}">
  <meta property="og:url" content="{canonical}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{html.escape(title)}">
  <meta name="twitter:description" content="{html.escape(description)}">
  <meta name="twitter:image" content="{og_image}">
  <meta name="theme-color" content="#315daa">
  <link rel="icon" type="image/svg+xml" href="{fav}">
  <link rel="preconnect" href="https://use.typekit.net" crossorigin>
  <link rel="stylesheet" href="https://use.typekit.net/gwr1nfk.css">
  <link rel="stylesheet" href="{css}">
  {json_ld_html}
</head>
<body>
<a class="skip-link" href="#primary">Skip to content</a>
<div class="site-overlay" aria-hidden="true"></div>
"""

def render_header(depth:int)->str:
    logo_w = asset(depth, "assets/icons/NHCC-Full-White-new.svg")
    logo_c = asset(depth, "assets/icons/NHCC-Full-2Color-new.svg")
    home   = asset(depth, "index.html")
    nav_items_html = "\n".join(
        f'<li><a href="{asset(depth, slug)}">{html.escape(label)}</a></li>'
        for slug,label in NAV
    )
    return f"""<header id="masthead" class="site-header" role="banner">
  <div class="container">
    <div class="site_branding">
      <a href="{home}" rel="home" aria-label="{html.escape(BUSINESS)} — home">
        <img class="logo-white" src="{logo_w}" alt="{html.escape(BUSINESS)} logo" width="170" height="54">
        <img class="logo-color" src="{logo_c}" alt="" aria-hidden="true" width="170" height="54">
      </a>
    </div>
    <button class="menu-btn" aria-controls="mobile-navigation" aria-expanded="false" aria-label="Open menu">☰ Menu</button>
    <nav id="site-navigation" class="main-navigation" aria-label="Primary">
      <ul>{nav_items_html}</ul>
    </nav>
  </div>
</header>
<nav id="mobile-navigation" class="mobile-nav" aria-label="Mobile">
  <button class="mobile-close" aria-label="Close menu">×</button>
  <ul>{nav_items_html}</ul>
</nav>
"""

def render_wave()->str:
    return ('<svg class="wave" xmlns="http://www.w3.org/2000/svg" '
            'viewBox="0 0 1764 211.7" preserveAspectRatio="none" aria-hidden="true" focusable="false">'
            '<path d="M1764 156.8v54.8H0V0l147 26.1c147 26.6 441 78 735 104.6 294 26.1 588 26.1 735 26.1h147z" fill="#fff"/>'
            '</svg>')

def render_footer(depth:int)->str:
    logo_w = asset(depth, "assets/icons/NHCC-Full-White-new.svg")
    home   = asset(depth, "index.html")
    ic = lambda n: asset(depth, f"assets/icons/{n}")
    nav_html = "\n".join(
        f'<li><a href="{asset(depth, slug)}">{html.escape(label)}</a></li>'
        for slug,label in NAV
    )
    return f"""<footer id="colophon" class="site-footer" role="contentinfo">
  <div class="site_footer_inner">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-12 col-md-5">
          <a class="footer_branding" href="{home}" rel="home" aria-label="{html.escape(BUSINESS)} — home">
            <img src="{logo_w}" alt="{html.escape(BUSINESS)} logo" width="220" height="70">
          </a>
          <p>Adult audiology care in Nashville, TN. Evidence-based hearing tests, transparent unbundled pricing, and hearing aid fittings personalized to you.</p>
        </div>
        <div class="col-6 col-md-3">
          <h3>Menu</h3>
          <ul>{nav_html}</ul>
        </div>
        <div class="col-6 col-md-2">
          <h3>Social</h3>
          <ul class="footer_social" role="list">
            <li><a href="https://www.facebook.com/p/Nashvilles-Hearing-Communication-Center-100086304305191/" target="_blank" rel="noopener" aria-label="Facebook">
              <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.5 21v-8h2.8l.4-3.3h-3.2V7.6c0-1 .3-1.6 1.7-1.6h1.8V3c-.3 0-1.4-.1-2.6-.1-2.6 0-4.4 1.6-4.4 4.5v2.3H7v3.3h2.9V21h3.6z"/></svg>
            </a></li>
            <li><a href="https://www.linkedin.com/in/gina-angley" target="_blank" rel="noopener" aria-label="LinkedIn">
              <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4.98 3.5C4.98 4.88 3.87 6 2.5 6S0 4.88 0 3.5 1.12 1 2.5 1s2.48 1.12 2.48 2.5zM0 8h5v13H0zM7.5 8h4.8v1.8h.1c.7-1.3 2.4-2.1 4.1-2.1 4.4 0 5.2 2.9 5.2 6.6V21h-5v-5.4c0-1.3 0-3-1.8-3s-2.1 1.4-2.1 2.9V21h-5V8z"/></svg>
            </a></li>
            <li><a href="https://www.instagram.com/" target="_blank" rel="noopener" aria-label="Instagram">
              <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.2c3.2 0 3.6 0 4.8.1 1.2.1 1.9.2 2.3.4.6.2 1.1.5 1.5.9.4.4.7.9.9 1.5.2.4.3 1.1.4 2.3.1 1.2.1 1.6.1 4.8s0 3.6-.1 4.8c-.1 1.2-.2 1.9-.4 2.3-.2.6-.5 1.1-.9 1.5-.4.4-.9.7-1.5.9-.4.2-1.1.3-2.3.4-1.2.1-1.6.1-4.8.1s-3.6 0-4.8-.1c-1.2-.1-1.9-.2-2.3-.4-.6-.2-1.1-.5-1.5-.9-.4-.4-.7-.9-.9-1.5-.2-.4-.3-1.1-.4-2.3C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.8c.1-1.2.2-1.9.4-2.3.2-.6.5-1.1.9-1.5.4-.4.9-.7 1.5-.9.4-.2 1.1-.3 2.3-.4 1.2-.1 1.6-.1 4.8-.1M12 0C8.7 0 8.3 0 7.1.1 5.8.1 4.9.4 4.1.7c-.9.3-1.6.8-2.3 1.5C1.1 2.9.6 3.6.3 4.5 0 5.3-.1 6.2-.2 7.5-.2 8.7-.2 9.1-.2 12s0 3.3.1 4.5c.1 1.3.3 2.2.6 3 .3.9.8 1.6 1.5 2.3.7.7 1.4 1.2 2.3 1.5.8.3 1.7.5 3 .6 1.2.1 1.6.1 4.5.1s3.3 0 4.5-.1c1.3-.1 2.2-.3 3-.6.9-.3 1.6-.8 2.3-1.5.7-.7 1.2-1.4 1.5-2.3.3-.8.5-1.7.6-3 .1-1.2.1-1.6.1-4.5s0-3.3-.1-4.5c-.1-1.3-.3-2.2-.6-3-.3-.9-.8-1.6-1.5-2.3C21.1.9 20.4.4 19.5.1c-.8-.3-1.7-.5-3-.6C15.3 0 14.9 0 12 0zm0 5.8A6.2 6.2 0 1 0 12 18.2 6.2 6.2 0 0 0 12 5.8zm0 10.2a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm7.8-10.4a1.4 1.4 0 1 1-2.9 0 1.4 1.4 0 0 1 2.9 0z"/></svg>
            </a></li>
          </ul>
        </div>
        <div class="col-12 col-md-2">
          <h3>Contact</h3>
          <p>{ADDRESS_L1}<br>{ADDRESS_L2}</p>
          <p><a href="{PHONE_TEL}">{PHONE}</a></p>
          <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
        </div>
      </div>
    </div>
  </div>
  <div class="site_info">
    <p>&copy; {YEAR} {BUSINESS}. All rights reserved.</p>
  </div>
</footer>
<script src="{asset(depth, 'assets/js/site.js')}" defer></script>
</body>
</html>
"""

def write_page(rel:str, depth:int, title:str, description:str, body:str, json_ld:list|None=None):
    out_dir = OUT / rel if rel.endswith("/") or rel=="" else (OUT / rel).parent
    if rel == "":
        out_path = OUT / "index.html"
    elif rel.endswith("/"):
        out_path = OUT / rel / "index.html"
        out_dir = out_path.parent
    else:
        out_path = OUT / rel
        out_dir = out_path.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    canonical_path = rel if rel else "index.html"
    html_doc = (
        render_head(depth, title, description, canonical_path, json_ld)
        + render_header(depth)
        + body
        + render_footer(depth)
    )
    out_path.write_text(html_doc, encoding="utf-8")
    print(f"wrote {out_path.relative_to(OUT)} ({len(html_doc)//1024} kb)")
    return out_path
