# pggllc.org domain cutover

Prepared November 26, 2026. No DNS, registration, nameserver, or custom-domain changes have been made.

## Observed hosting

- Repository: https://github.com/pggLLC/pggllc.github.io
- GitHub Pages: public, legacy branch build, main /, HTTPS enforced, no custom domain.
- Preview: https://pggllc.github.io/
- Current pggllc.org appears hosted by GoDaddy Website Builder.
- Observed apex A: 13.248.243.5 and 76.223.105.230. No AAAA response.
- www CNAME: pggllc.org.
- MX: priority 0 pggllc-org.mail.protection.outlook.com.
- TXT observed: NETORGFT8364526.onmicrosoft.com and v=spf1 include:secureserver.net -all.
- These are an observed subset, not a full zone export. Obtain an authoritative zone export before cutover, including DKIM, DMARC, CAA, verification, and all subdomains.

## Prerequisites

1. Approve the live GitHub Pages preview and complete the direct business email and FirstPass destination configuration.
2. Export and securely save the entire existing DNS zone, TTLs and current website content. Keep the existing GoDaddy site/hosting available for rollback.
3. Confirm control of the domain DNS and GitHub organization. Verify pggllc.org ownership in organization Settings > Pages using GitHub's exact generated TXT name/value. Do not guess that token.
4. Lower only the web-record TTLs to 300 seconds at least one old TTL before cutover.
5. Verify the current values in GitHub's documentation immediately before use: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site

## Cutover (requires separate authorization)

1. In repository Settings > Pages, set custom domain to pggllc.org. For this branch-based deployment, GitHub saves a CNAME file containing pggllc.org. Pull that commit locally. Do not add the CNAME before the planned cutover: it may redirect the preview to the old site.
2. Replace ONLY apex website A records with GitHub Pages addresses:
   - 185.199.108.153
   - 185.199.109.153
   - 185.199.110.153
   - 185.199.111.153
3. Set www CNAME to pggllc.github.io (no protocol or path). Remove conflicting www address records. If using AAAA, use only current GitHub-documented IPv6 addresses; do not leave stale AAAA pointing at the old host.
4. Do not change nameservers or registration. Preserve MX, SPF, DKIM, DMARC, verification TXT, and unrelated subdomains. Check existing CAA permits GitHub's certificate issuer; do not broadly remove security records.
5. Wait for GitHub Pages DNS check and certificate issuance. Enable/confirm Enforce HTTPS when available. Certificate issuance can take time; monitor rather than repeatedly changing DNS.
6. Verify HTTPS on apex and www, redirects to the selected canonical apex, homepage and every internal page, CSS/favicon, the contact path, /about-us, /services, /contact-us and the preserved /housing-insights.html.
7. Test inbound/outbound business mail separately. Compare mail records with the export. Check sitemap.xml and robots.txt; submit the new sitemap through the owner's search-console account if used.
8. Retain the previous site through a stable observation period. Restore normal web TTLs after verification.

## Rollback

1. Restore the exact prior apex A and www CNAME values and TTLs from the authoritative export. Preserve all mail records.
2. Keep the old hosting active and verify pggllc.org returns the previous site after resolver caches expire.
3. Remove the GitHub Pages custom-domain setting/CNAME if abandoning the setup. Keep GitHub domain verification until DNS no longer points to Pages to avoid domain takeover exposure.
4. If reverting only site content, use a new git revert commit rather than resetting shared history. Baseline original commit: 7eecc4e (full SHA available in git history).

## Remaining launch inputs

The current website provides a contact form but publishes no pggLLC business email or telephone. The new site currently links to Paul's verified LinkedIn profile, with no simulated form submission. A direct business email is required to complete the requested email fallback. FirstPass's public destination could not be verified; its inquiry link is internal until supplied. These are launch-quality blockers for a domain switch, not reasons to invent contact details.
