# NHCC Rebuild — Research Notes

## Current nashvillehcc.com (Onspire build) — fact sheet
| Item | Current site | Rebuild (this project) |
|---|---|---|
| Address | 8008 TN-100, Nashville, TN 37221 (Bellevue) | 8008 TN-100, Nashville, TN 37221 ([Helping Me Hear listing](https://www.helpingmehear.com/find-an-expert/nashvilles-hearing-communication-center/), [nashvillehcc.com/location-contact](https://www.nashvillehcc.com/location-contact/)) |
| Phone | 615-237-7701 (Onspire contact page) | **615.678.8638** per Erik's hard rule and REAL_CONTENT ACF field `cta_button_one` (the line also still printed in nashvillehcc.com/appointment metadata) |
| Hours | Mon–Thu 8a–4p, Fri 8a–11:30a, closed weekends | Same (verified via [Helping Me Hear](https://www.helpingmehear.com/find-an-expert/nashvilles-hearing-communication-center/) and [Yelp](https://www.yelp.com/biz/nashvilles-hearing-and-communication-center-nashville-2)) |
| Email | Not publicly listed | Placeholder `info@nashvillehcc.com` — flagged for Gina to confirm |

The phone-number discrepancy is called out in [current-site-notes.md](./current-site-notes.md) and in NOTES_FOR_CLIENT.md so Gina can confirm which line she wants.

## Nashville / Davidson County audiology demographic snapshot

**Population & seniors**
- Davidson County population is roughly 715,000 as of the latest census estimates; the Nashville metro (MSA) is about 2.1 million ([U.S. Census QuickFacts — Davidson County, TN](https://www.census.gov/quickfacts/fact/table/davidsoncountytennessee/POP010220)).
- Residents aged 65+ are roughly **13–14%** of Davidson County and growing, with Williamson, Wilson, and Sumner suburbs skewing older — the core audiology referral geography for Bellevue practices like NHCC.
- Tennessee as a whole has about **1 in 5** adults over 65 reporting some hearing loss, matching national averages cited in NHCC's own patient education copy ([NIH / NIDCD — Age-Related Hearing Loss](https://www.nidcd.nih.gov/health/age-related-hearing-loss)).

**Insurance landscape**
- Medicare Advantage penetration in Middle Tennessee is high and most Advantage plans offer a hearing benefit or allowance — patients routinely ask if NHCC accepts their plan.
- Traditional Medicare still does NOT cover routine hearing aids; NHCC's unbundled pricing + CareCredit/Cherry financing directly addresses this gap.
- BlueCross BlueShield of Tennessee, Cigna, Aetna, and UnitedHealthcare are the dominant commercial carriers. Audiology benefit coverage varies; NHCC handles verification on a per-plan basis.

**Competitor landscape (Nashville / Bellevue / Brentwood)**
- Chain/retail: Miracle-Ear (several locations), Beltone Middle Tennessee, Costco Hearing Aid Center.
- Hospital-affiliated: Vanderbilt Bill Wilkerson Center (Green Hills & main campus), Saint Thomas ENT partners.
- Independent Doctors of Audiology: Audiology of Nashville, Hearing Services of Nashville, Summit Hearing, Hearing Associates of Nashville. Roughly **15–25** independent audiology / hearing-aid dispensing locations serve the metro area depending on how the search is scoped.

**NHCC positioning**
- Unique pitch: independent, audiologist-owned, **unbundled/at-cost** device pricing with real-ear measurement on every fitting. Dr. Angley trained at Vanderbilt Bill Wilkerson, so credibility with existing Vanderbilt patients is strong.
- Bellevue location captures west Nashville / Belle Meade / Cheatham & Dickson county patients who would otherwise drive into Green Hills or Cool Springs.
- AEO-friendly content strategy on this rebuild emphasizes "Nashville audiologist," "Nashville hearing test," "Bellevue hearing aids," and specific procedure schema to win voice-assistant and AI-search queries.

## Design reference
Original 2022 Paris Mountain Marketing theme files live in `/reference-theme/`. Color palette, type scale, and component structure were ported directly from `compiled-style.css` and `scss/_var.scss`. The hero wave SVG in `front-page.php` (viewBox 0 0 1764 211.7) is preserved inline on every hero section.

## Image inventory
- 42 real photos from WordPress media library, all optimized to WebP at 80% quality.
- Originals preserved in `assets/images-original/` for archival.
- Usage distribution: 5 heroes, 5 landscape backdrops, 8 square lifestyle portraits, 1 Dr. Angley headshot, 10 supporting photos, remaining are post illustrations.

## AEO notes
Every page ships with:
- MedicalBusiness JSON-LD including address, phone, hours, geo coordinates, owner bio, and sameAs links.
- Page-specific schema (FAQPage on About, MedicalProcedure on Hearing Testing, BlogPosting on articles, OfferCatalog on Services).
- First-sentence direct answers under every H2 (the pattern that AI answer-engines copy verbatim).
- H1s anchor on location + role triples: "Adult Audiologist in Nashville, TN," "Audiology Services in Nashville, TN," "Hearing Testing in Nashville, TN."
