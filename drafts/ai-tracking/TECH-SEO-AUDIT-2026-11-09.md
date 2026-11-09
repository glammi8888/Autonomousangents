# Technical SEO audit: glammi.ai + issue11.app (Nov 9, 2026)
Evidence: live HTTP captures with a Googlebot user agent, 2.5 s apart (fast bursts got a 12-word shell back, a rate-limit artifact, not a site defect; re-tested slowly, every page served full HTML).

## Healthy (no action)
- Both: HTTPS, http -> https 308, robots.txt allows all + lists the sitemap, real 404s, self-canonicals on every page, `max-image-preview:large`, one title + meta description per page, FAQPage JSON-LD valid on every article.
- Both sitemaps list every live page (glammi 19 URLs, issue11 7).

## Fixed today (Framer main, goes live on the next Glammi publish)
| Finding | Evidence | Fix |
|---|---|---|
| glammi.ai showed Framer's default favicon in Google results | `<link rel="icon" href=".../default-favicon-light.v1.png">` | New Glammi favicon (black circle + white hexagon, same as the homepage mark), 96x96, set for light/dark/apple-touch |
| 6 extra H1s on every Glammi page | footer buttons ("Book a Discovery Call", "Tell Us…", "Follow on LinkedIn") used the H1 tag | Tag set to p (look unchanged) |
| Case study pages titled "…Deliver — Framer Design and Development Agency" | /projects/* `<title>` (template leftover) | "{{Title}}: AEO and AI Search Case Study \| Glammi Studio" |
| /404 in the sitemap | sitemap.xml lists https://glammi.ai/404 | 404 page set to noindex |
| Weak blog index title/description | "Blog — Glammi Studio" | "AEO and AI Search Blog for Beauty and Jewelry Brands \| Glammi Studio" + new description |
| Article titles 75 to 92 chars with an em dash | "{{Title}} — Glammi Studio" | Uses each post's SEO Title field (shorter, "\| Glammi Studio") |

## Open (owner)
| Priority | Finding | Owner |
|---|---|---|
| 1 | Google Search Console + Bing Webmaster not confirmed for either site (can't see indexing without it) | Megan (her Google login) |
| 2 | issue11.app: homepage FAQPage code is site-wide, so privacy, terms, blog index and every article carry it (articles have 2 FAQPage blocks) | Megan: move the Custom Code from Site Settings to the Home page |
| 3 | issue11.app/llms.txt returns 404 (file ready: drafts/issue11-site/llms.txt) | Megan uploads |
| 4 | Internal links: posts link to only 1 or 2 other posts | Agent: daily run now adds 2 to 3 per new post; backfill live posts |
| 5 | glammi.ai has no og:image (no preview picture when shared) | Agent next pass (needs one brand image) |
| 6 | 11 images without alt on the glammi.ai homepage, 15 on issue11.app (many are template phone screens due to be replaced) | Agent with the screen swap |
| 7 | www.glammi.ai / www.issue11.app could not be tested from here (host not reachable through this sandbox) | Megan: check both open and redirect to the bare domain |
| 8 | glammi.ai homepage schema names "Megan Nancy Scott" | Megan: Custom Code find/replace |
