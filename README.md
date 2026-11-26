# pggLLC website

Static, dependency-free website deployed by GitHub Pages from `main` at repository root. No build step or external contact backend. `.nojekyll` keeps static delivery explicit.

## Local work

Clone this repository, then run `python3 -m http.server 8765` from its root. Open http://localhost:8765. Edit the HTML and assets/site.css directly. Run `python3 scripts/check_site.py` before publishing.

The original housing-insights.html is preserved unchanged. It is a legacy standalone analysis, not featured as current data on the new marketing site.

See docs/DOMAIN-CUTOVER.md for the separately authorized future domain switch. No CNAME file is intentionally included before cutover. Canonical metadata and sitemap already target the intended pggllc.org domain.

Contact currently uses the verified LinkedIn profile because no business email was published by the old site. Add the owner's verified direct email before domain launch. FirstPass also needs a verified external destination.

## Current practice and sample

The homepage presents all five original service lines, named career experience, and a COHO-backed memo preview. Supporting-page typography and navigation share the compact refinements in `assets/refinements.css`.

The sample memo uses actual public Fruita screening figures, with a fictional nonprofit and unspecified site. Its source register, definitions, vintages and exclusions are available in the memo and downloadable evidence JSON. The four-page PDF is in `downloads/`. No figure establishes parcel feasibility, project yield, a rent schedule, funding eligibility or an award. The 60% AMI gap is excluded because the current COHO rendered overview and digest differ. Preserve these distinctions when editing.
