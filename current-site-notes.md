# Notes from current Onspire-built nashvillehcc.com (for reference)

Pulled via public web search on 2026 build date.

## Address (verified, used on our rebuild)
**8008 TN-100, Nashville, TN 37221** (Bellevue)

Sources: [Helping Me Hear listing](https://www.helpingmehear.com/find-an-expert/nashvilles-hearing-communication-center/), [Gina Angley LinkedIn](https://www.linkedin.com/in/gina-angley), [nashvillehcc.com/location-contact](https://www.nashvillehcc.com/location-contact/), [Yelp](https://www.yelp.com/biz/nashvilles-hearing-and-communication-center-nashville-2).

## Office hours
- Monday – Thursday: 8:00am – 4:00pm
- Friday: 8:00am – 11:30am
- Saturday & Sunday: Closed

## Phone numbers — conflict
- Task / REAL_CONTENT.md ACF `cta_button_one`: **615.678.8638** ← Erik's hard rule: use this.
- Current Onspire Contact page: 615-237-7701
- nashvillehcc.com/appointment page still lists 615-678-8638 in description metadata.

**Action:** Rebuild uses 615.678.8638 everywhere (primary practice line per original WordPress ACF).
Note in NOTES_FOR_CLIENT.md that Gina should confirm which line is active and whether a forwarding/text line needs separate treatment.

## Widgets visible on current Onspire site
- "Call or Text Us" button — vendor not named publicly, likely Podium/Birdeye style text-messaging widget. Needs Gina's vendor confirmation.
- "See What Patients Think" reviews section — Review Manager embed (matches the `review_html` placeholder in the original 2022 theme).
- No financing widget visible on current site (Gina wants Cherry added).
- No online booking widget visible; current site uses a request form.

## Email
Not publicly listed on current site. The original WordPress had no public email ACF field. Added a placeholder `info@nashvillehcc.com` — flagged in NOTES_FOR_CLIENT.md for Gina to confirm / replace.
