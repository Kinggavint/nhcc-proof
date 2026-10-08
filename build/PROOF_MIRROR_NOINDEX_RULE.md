# Rule: never edit checked-in HTML output to change robots directives

## What happened (2026-08-30)

Commit `fd46cdb` changed `<meta name="robots">` from `index,follow` to
`noindex,follow` directly in all 18 checked-in `.html` output files, intending
to stop the GitHub Pages proof mirror (`kinggavint.github.io/nhcc-proof`) from
competing with the live site for indexing.

But this repo's checked-in HTML is the single source synced to **both**
destinations:
- GitHub Pages serves these files directly for the proof mirror.
- The SEO cron's S3 sync step (`aws s3 sync` / `aws s3 cp`) pushes the same
  files to the live bucket `nashville-hearing-center`.

There is no build-mode split. Editing the output files edited both targets
at once. The live domain nashvillehcc.com carried `noindex,follow` for four
consecutive cron cycles (2026-08-30 PM through 2026-09-01 AM) before this was
caught and fixed by direct S3 overwrite (see changelog entry
2026-09-XX "LIVE FIX" and rollback_snapshots/<timestamp>_noindex_regression/).

## The rule going forward

1. `render.py` line ~110 (`<meta name="robots" content="index,follow">`) is
   the single source of truth for the LIVE site. It must always read
   `index,follow`. Do not change it to serve the proof mirror.
2. If the proof mirror needs `noindex,follow` (it does, per Defect 1
   remediation — the mirror must not compete with the live domain for
   indexing), that value belongs ONLY in whatever copy of the HTML is
   actually pushed to GitHub Pages, produced as a separate, clearly-named
   build artifact (e.g. a `proof-mirror-build/` directory) that the S3 sync
   step never reads from and never touches.
3. The repo's own checked-in `.html` files (what `git status` tracks at the
   repo root) must always match what LIVE should serve. Never use them as a
   staging ground for a proof-only variant.
4. Before any commit that touches a `<meta name="robots">` line, run:
   `grep -c 'noindex' *.html */index.html */*/index.html` (or equivalent)
   and confirm the count matches expectations for the INTENDED target only.
   If the SEO cron's ship step is about to sync repo HTML to S3, that grep
   must return 0 for the live tree, always.
5. If a future change legitimately needs to touch the proof mirror's robots
   meta independent of live, do it as a post-render step against a copy in
   a directory the S3 deploy step is not configured to read (see
   `nhcc-proof-live-only/` used for the robots.txt/sitemap.xml split from
   Defect 1 — same pattern, now extended to page-level noindex).
