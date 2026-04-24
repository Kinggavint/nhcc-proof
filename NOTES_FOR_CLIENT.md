# Notes for Dr. Angley — wiring-up items

The rebuild is **fully functional static HTML** and uses only NHCC branding — no third-party credits anywhere. A handful of integrations need a credential, vendor choice, or account ID from you before we flip them fully live.

## 1. Phone number — which line is primary?
- REAL_CONTENT.md lists `615.678.8638` as the primary CTA phone (this is what the rebuild uses everywhere).
- Your current Onspire site lists `615-237-7701` as call/text.
- Tell us which number is the **real, monitored** line (and whether text-messaging is on that same line or a separate Podium/Birdeye-style number). We'll flip the site instantly.

## 2. Text-messaging widget
The current site has "Call or Text Us" language — vendor is unknown from the public site. Typical options:
- **Podium** — most common for healthcare, has a floating widget + analytics.
- **Birdeye** — similar; also bundles review requests.
- **Weave** — popular for smaller practices, ties into phone/scheduling.
- Or a simple **click-to-text SMS link** using your carrier's SMS-to-short-code.

Once you pick one, we paste their embed snippet into `/assets/js/site.js` or the footer partial.

## 3. Cherry Financing widget
The rebuild includes a styled Cherry card on Patient Info with a "call us" CTA. To activate the real flow:
- Provide your **Cherry Merchant ID** (or practice login) and we'll embed the live Cherry application widget/QR as their docs specify.
- Typical placement: Patient Info page payment grid + a small "Apply with Cherry" badge near pricing conversations.

## 4. Review Manager embed (patient reviews)
The original 2022 theme used a `reviewmgr` embed that pulled from `results.medpb.com/nsv/`. The rebuild has a **Reviews** placeholder on the About page reserved for this widget.
- Confirm Review Manager is still your review-collection vendor.
- Send us the current embed snippet or account ID and we'll drop it in. Alternative: switch to Google Reviews carousel, Birdeye, or Endorsal — happy to recommend.

## 5. Appointment & Contact forms
Both forms are real HTML forms with proper fields, but they currently POST to static "thanks" confirmation pages. To collect submissions by email you have three easy options:
- **Formspree** (fastest — a 5-minute setup, we add your endpoint and you get email notifications).
- **Netlify Forms** (if we move hosting to Netlify).
- **HearingHealthPortal booking iframe** — your original site used `hearinghealthportal.com/scheduling/schedule.aspx?key=104511-8369&embed=true`. If you still have that key we can re-embed the exact widget.

Pick one and we'll wire it in under 10 minutes.

## 6. Google Maps
The Contact page embeds a Maps iframe pointing at `8008 TN-100, Nashville, TN 37221`. If you want a **Google Maps Embed API key** for custom styling/tracking, we'll swap in the keyed URL. Otherwise the current embed works out of the box.

## 7. Photos
- The rebuild uses your original 42 WordPress photos (optimized to WebP).
- Your team headshot (`headshot.jpg`) is featured on Home and About — **confirm this is still the headshot you want**, or send a newer one.
- Many of the hero/landscape photos are Adobe Stock + Unsplash. If you now own newer, branded photography of the Bellevue office, send it over and we'll swap.

## 8. Email address
The site currently shows `info@nashvillehcc.com` in the footer and on the Contact page. This is a **placeholder** — give us the real address (or a dedicated inbox like `hello@` or `gina@`) and we'll update everywhere in one pass.

## 9. HIPAA-compliant new patient paperwork PDF
The rebuild ships a **blank, HIPAA-compliant, 3-page intake form** at `/downloads/nhcc-new-patient-paperwork.pdf`. It covers demographics, insurance, hearing history, medical history, HIPAA acknowledgment, release authorization, and financial responsibility. Review it on your end — if you want additional fields (e.g., referring physician, how you heard about us, preferred pronouns) we can add them.

## 10. Content that may need refreshing
Pulled directly from the old 2022 WordPress site and used verbatim:
- Home hero, success boxes, services, steps, team bio.
- About section, values (5), what-to-expect (3), FAQ (8 questions), review placeholder.
- Services ACF copy (hearing care personalized, verification, unbundled pricing, brands list).
- Patient Info payment boxes + privacy-practices mention.
- Hearing Testing full article (`/hearing-testing/`).
- Two blog posts (preserve-your-hearing + clean-your-hearing-aid) — both use your exact prose.
- Three newsletter entries (January 2025, February 2025 × 2).

If any of this is **out of date** (e.g., pricing language, insurance acceptance, FAQ answers), send edits and we'll update.

## 11. SEO / AEO enhancements baked in
- MedicalBusiness schema with address, hours, geo, and owner credentials on every page.
- FAQPage schema on About.
- MedicalProcedure schema on Hearing Testing.
- BlogPosting schema on each article.
- OfferCatalog schema enumerating your six main services.
- Sitemap.xml and robots.txt generated for GoogleBot / ChatGPT / Perplexity crawlers.
- Clean H1/H2 hierarchy so answer-engines can quote individual sections.
- Relative asset paths so the site runs on any domain (e.g., `kinggavint.github.io/nhcc-proof/` or your custom domain) without rewrites.

## 12. Branding confirmation
- Zero "Created with Perplexity," "Lovable," "Computer," or "Paris Mountain Marketing" branding anywhere. Footer is NHCC-only.
- Real NHCC logos (`NHCC-Full-White-new.svg` and `NHCC-Full-2Color-new.svg`) used in header, footer, and favicon. No generated/substitute logos.

## Checklist to go fully live
- [ ] Confirm primary phone number + text line
- [ ] Choose text-messaging vendor and share embed
- [ ] Share Cherry merchant ID
- [ ] Share Review Manager embed or pick alternative
- [ ] Pick form backend (Formspree / HearingHealthPortal / other)
- [ ] Confirm email address
- [ ] Point your domain (nashvillehcc.com) DNS to the rebuild when ready
