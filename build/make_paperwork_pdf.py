#!/usr/bin/env python3
"""Generate a blank, HIPAA-compliant new patient paperwork PDF.

All fields are BLANK. No pre-filled patient info. Intended to be printed
and completed by hand, OR filled in a PDF reader before a first visit.
"""
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, black, white
from pathlib import Path
import textwrap

OUT = Path(__file__).resolve().parents[1] / "downloads" / "nhcc-new-patient-paperwork.pdf"
OUT.parent.mkdir(parents=True, exist_ok=True)

PRIMARY = HexColor("#315daa")
SECONDARY = HexColor("#607083")
LIGHT = HexColor("#f0f1f3")

BUSINESS  = "Nashville's Hearing & Communication Center"
PHONE     = "615.678.8638"
ADDR1     = "8008 TN-100"
ADDR2     = "Nashville, TN 37221"

page_w, page_h = LETTER
MARGIN = 0.65 * inch
content_w = page_w - 2*MARGIN

def header(c, title):
    c.setFillColor(PRIMARY)
    c.rect(0, page_h - 0.7*inch, page_w, 0.7*inch, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(MARGIN, page_h - 0.32*inch, BUSINESS.upper())
    c.setFont("Helvetica", 9)
    c.drawString(MARGIN, page_h - 0.52*inch, f"{ADDR1}  ·  {ADDR2}  ·  {PHONE}")
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 11)
    c.drawRightString(page_w - MARGIN, page_h - 0.32*inch, title)

def footer(c, page_num):
    c.setStrokeColor(SECONDARY)
    c.setLineWidth(0.5)
    c.line(MARGIN, 0.6*inch, page_w - MARGIN, 0.6*inch)
    c.setFillColor(SECONDARY)
    c.setFont("Helvetica", 8)
    c.drawString(MARGIN, 0.38*inch, f"{BUSINESS} — {ADDR1}, {ADDR2} — {PHONE}")
    c.drawRightString(page_w - MARGIN, 0.38*inch, f"Page {page_num}")

def section_title(c, y, title):
    c.setFillColor(PRIMARY)
    c.rect(MARGIN, y-2, content_w, 18, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(MARGIN + 6, y+4, title.upper())
    return y - 26

def field_line(c, y, label, width_frac=1.0, with_underline=True):
    c.setFillColor(black)
    c.setFont("Helvetica", 9)
    c.drawString(MARGIN, y, label)
    if with_underline:
        c.setStrokeColor(SECONDARY)
        c.setLineWidth(0.5)
        # underline below the label, leaving space for writing
        w = content_w * width_frac
        c.line(MARGIN + 0, y - 14, MARGIN + w, y - 14)
    return y - 28

def two_field_row(c, y, label1, label2, split=0.5):
    c.setFillColor(black)
    c.setFont("Helvetica", 9)
    c.drawString(MARGIN, y, label1)
    x2 = MARGIN + content_w * split + 10
    c.drawString(x2, y, label2)
    c.setStrokeColor(SECONDARY)
    c.setLineWidth(0.5)
    c.line(MARGIN, y-14, MARGIN + content_w*split - 5, y-14)
    c.line(x2, y-14, MARGIN + content_w, y-14)
    return y - 28

def three_field_row(c, y, l1, l2, l3):
    c.setFillColor(black)
    c.setFont("Helvetica", 9)
    third = content_w / 3
    c.drawString(MARGIN, y, l1)
    c.drawString(MARGIN + third + 6, y, l2)
    c.drawString(MARGIN + 2*third + 6, y, l3)
    c.setStrokeColor(SECONDARY)
    c.setLineWidth(0.5)
    c.line(MARGIN, y-14, MARGIN + third - 6, y-14)
    c.line(MARGIN + third + 6, y-14, MARGIN + 2*third - 6, y-14)
    c.line(MARGIN + 2*third + 6, y-14, MARGIN + content_w, y-14)
    return y - 28

def checkbox_row(c, y, items, per_row=4):
    c.setFillColor(black)
    c.setFont("Helvetica", 9)
    col_w = content_w / per_row
    i = 0
    for item in items:
        col = i % per_row
        row = i // per_row
        x = MARGIN + col * col_w
        cy = y - row * 18
        c.rect(x, cy-1, 10, 10, fill=0, stroke=1)
        c.drawString(x+15, cy, item)
        i += 1
    rows_used = (len(items) + per_row - 1)//per_row
    return y - rows_used*18 - 12

def paragraph(c, y, text, size=9, leading=12, max_width=None):
    max_width = max_width or content_w
    c.setFillColor(black)
    c.setFont("Helvetica", size)
    # crude wrapping
    words = text.split()
    lines = []
    cur = ""
    for w in words:
        test = (cur + " " + w).strip()
        if c.stringWidth(test, "Helvetica", size) <= max_width:
            cur = test
        else:
            lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    for ln in lines:
        c.drawString(MARGIN, y, ln)
        y -= leading
    return y - 4

def signature_row(c, y):
    c.setFillColor(black)
    c.setFont("Helvetica", 9)
    c.drawString(MARGIN, y, "Patient or Guardian Signature")
    c.drawString(MARGIN + content_w*0.6, y, "Date")
    c.setStrokeColor(SECONDARY)
    c.setLineWidth(0.7)
    c.line(MARGIN, y-14, MARGIN + content_w*0.55, y-14)
    c.line(MARGIN + content_w*0.6, y-14, MARGIN + content_w, y-14)
    return y - 30

# ---------- build ----------
c = canvas.Canvas(str(OUT), pagesize=LETTER, pageCompression=1)
c.setTitle("New Patient Paperwork — Nashville's Hearing & Communication Center")
c.setAuthor(BUSINESS)
c.setSubject("HIPAA-compliant blank new patient intake form")
c.setKeywords("NHCC, audiology, intake, HIPAA, new patient")

# ---- PAGE 1: Patient demographics & insurance ----
header(c, "New Patient Paperwork")
y = page_h - 1.15*inch
c.setFillColor(black)
c.setFont("Helvetica", 9.5)
y = paragraph(c, y,
    "Please complete all sections below before your first visit. Bring the signed pages with you, "
    "or ask our office about a secure email link. All information is kept confidential in accordance "
    "with HIPAA and our Notice of Privacy Practices.", size=9, leading=12)
y -= 4

y = section_title(c, y, "1. Patient Information")
y = two_field_row(c, y, "Last name", "First name")
y = two_field_row(c, y, "Middle initial", "Preferred name")
y = three_field_row(c, y, "Date of birth (MM/DD/YYYY)", "Sex", "Gender identity")
y = two_field_row(c, y, "Mailing address", "Apt / Unit", split=0.7)
y = three_field_row(c, y, "City", "State", "ZIP")
y = two_field_row(c, y, "Mobile phone", "Home phone")
y = two_field_row(c, y, "Email", "Preferred contact method (call / text / email)")
y = two_field_row(c, y, "Occupation", "Employer")
y = three_field_row(c, y, "Marital status", "Language preference", "Ethnicity (optional)")

y = section_title(c, y, "2. Emergency Contact")
y = two_field_row(c, y, "Full name", "Relationship to patient")
y = two_field_row(c, y, "Phone", "Alternate phone")

y = section_title(c, y, "3. Insurance Information")
y = two_field_row(c, y, "Primary insurance carrier", "Member ID")
y = two_field_row(c, y, "Group #", "Plan / Product")
y = two_field_row(c, y, "Policyholder name (if not patient)", "Policyholder DOB")
y = two_field_row(c, y, "Secondary insurance (if any)", "Secondary Member ID")

footer(c, 1)
c.showPage()

# ---- PAGE 2: Medical history ----
header(c, "New Patient Paperwork")
y = page_h - 1.15*inch

y = section_title(c, y, "4. Hearing & Ear Concerns")
y = paragraph(c, y, "Please describe your main hearing concerns and when you first noticed them.", size=9)
# 4 blank lines for free text
for _ in range(4):
    c.line(MARGIN, y, MARGIN + content_w, y); y -= 18

y = paragraph(c, y, "Do you experience any of the following? (Check all that apply)", size=9)
y = checkbox_row(c, y, [
    "Hearing loss (L)", "Hearing loss (R)", "Ringing/tinnitus (L)", "Ringing/tinnitus (R)",
    "Dizziness/vertigo", "Ear pain", "Ear drainage", "Fullness/pressure",
    "Sudden hearing change", "Difficulty in noise", "Noise exposure", "Family history",
])

y = section_title(c, y, "5. Current Hearing Devices")
y = two_field_row(c, y, "Do you currently wear hearing aids? (Yes / No)", "Brand & model")
y = two_field_row(c, y, "Approximate date first fit", "Date of last professional cleaning")
y = two_field_row(c, y, "Are you satisfied with current devices? (Yes / No)", "If not, why?")

y = section_title(c, y, "6. Medical & Family History")
y = paragraph(c, y, "Check any conditions that apply to you:", size=9)
y = checkbox_row(c, y, [
    "Diabetes", "High blood pressure", "Heart disease", "Stroke",
    "Kidney disease", "Autoimmune disease", "Cancer", "Head/neck injury",
    "Ear surgery", "Thyroid disease", "Depression/anxiety", "None",
])

y = paragraph(c, y, "Family members with hearing loss (who, at what age):", size=9)
for _ in range(2):
    c.line(MARGIN, y, MARGIN + content_w, y); y -= 18

y = section_title(c, y, "7. Medications & Allergies")
y = paragraph(c, y, "Current medications (name, dose, frequency):", size=9)
for _ in range(3):
    c.line(MARGIN, y, MARGIN + content_w, y); y -= 18
y = paragraph(c, y, "Known drug or latex allergies:", size=9)
for _ in range(2):
    c.line(MARGIN, y, MARGIN + content_w, y); y -= 18

footer(c, 2)
c.showPage()

# ---- PAGE 3: HIPAA / consent / release ----
header(c, "Consent & HIPAA")
y = page_h - 1.15*inch

y = section_title(c, y, "8. Consent for Care")
y = paragraph(c, y,
    "I voluntarily consent to audiological evaluation, diagnostic testing, and treatment services provided by "
    f"{BUSINESS} (NHCC). I understand that results will be reviewed with me and that I may ask questions at "
    "any time. I may decline any recommended service without penalty.", size=9, leading=12)
y = signature_row(c, y)

y = section_title(c, y, "9. HIPAA Acknowledgment — Notice of Privacy Practices")
y = paragraph(c, y,
    "I acknowledge that I have been given the opportunity to review NHCC's Notice of Privacy Practices, which "
    "describes how my protected health information (PHI) may be used and disclosed for treatment, payment, and "
    "healthcare operations, and my rights regarding that information. A printed or electronic copy is available "
    "on request.", size=9, leading=12)
y = signature_row(c, y)

y = section_title(c, y, "10. Authorization for Release of Information")
y = paragraph(c, y,
    "I authorize NHCC to release my protected health information to the following individuals or entities (e.g., "
    "referring physician, family member, primary care provider):", size=9, leading=12)
y = two_field_row(c, y, "Name", "Relationship / organization")
y = two_field_row(c, y, "Phone", "Email or fax")
y = paragraph(c, y, "Information that may be released:", size=9)
y = checkbox_row(c, y, [
    "Test results", "Diagnoses", "Treatment plan", "Billing info",
    "Progress notes", "Correspondence", "All of the above", "None",
])
y = signature_row(c, y)

y = section_title(c, y, "11. Financial Responsibility")
y = paragraph(c, y,
    "I understand NHCC operates on an unbundled pricing model. I will receive an itemized invoice before payment. "
    "I am financially responsible for any services not covered by my insurance. I agree to pay balances due at the "
    "time of service, or per arranged financing plan (CareCredit, Cherry, or similar).", size=9, leading=12)
y = signature_row(c, y)

footer(c, 3)

c.save()
print(f"wrote {OUT} ({OUT.stat().st_size//1024} KB)")
