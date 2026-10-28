# Purplease.com: full website audit

Audited 28 Oct 2026. Every published page was checked on desktop (1440px) and mobile (390px): Home, About us, Digital Transformation, Contact, Service enquiry, Pricing, Hello world!

**Stack found:** WordPress 7.1.3 on PHP 8.1, Hostinger (LiteSpeed cache + Hostinger CDN), Astra 4.14.1 + Astra child theme + Astra Pro add-on, Spectra (Ultimate Addons for Gutenberg), Contact Form 7 + country phone field, Rank Math SEO, Google Analytics 4 (G-55W17SR2X9), Google reCAPTCHA. SSL from Let's Encrypt, renews 25 Nov 2026. Email on Hostinger mail.

## Scorecard

| Area | Rating | Headline issue |
|---|---|---|
| Content and trust | 🔴 Poor | Template and placeholder content is live (coworking pricing page, fake testimonials, "Hello world!" post) |
| Conversion (leads) | 🔴 Poor | Hero buttons go nowhere, phone link dials the wrong number, "Free Trial" CTA doesn't fit a services company |
| SEO | 🟠 Weak | One meta description shared by every page, missing or duplicated H1s, only 6 pages, no service pages or blog |
| Design and UX | 🟠 Dated | Blue (not purple) generic template, stock photos, slider hero, tiny grey body text |
| Performance | 🟡 OK | Caching works; about 2 MB and 50–64 requests per page, reCAPTCHA loaded 3 times on every page |
| Accessibility | 🟠 Weak | No alt text on most images, form fields without labels, low-contrast text |
| Security | 🟡 OK | Username "admin" publicly listed, XML-RPC open, no security headers |
| Email domain | 🟡 OK | SPF set, DMARC at `p=none` (no protection against spoofing) |

---

## 1. Content and trust (fix first)

| # | Issue | Where | Fix |
|---|---|---|---|
| 1.1 | Pricing page is a coworking template: "$29/mo grab any desk", "Dedicated Office $228/mo", "Free Coffee and Beer", "People Who Love Our Place", placeholder paragraphs | `/pricing/` | Unpublish now; rebuild later as engagement models |
| 1.2 | Default WordPress post and sample comment, listed under "Blog" | `/hello-world/`, `/category/blog/`, `/author/admin/` | Delete the post; noindex author archive |
| 1.3 | Placeholder testimonials ("Jane Smith, Sosvertigo", "Derik van, Innovite") | Contact | Real quotes with name, role, company, photo, or remove |
| 1.4 | FAQ intro is template placeholder ("A descriptive paragraph that tells clients how good you are…"); FAQs are about website building on a Golang/DevOps page | Digital Transformation | Rewrite FAQs for Golang, cloud and DevOps buyers |
| 1.5 | "Over a decade of experience" vs "Established in 2023" | Home vs About | Pick one true statement (e.g. "Founded 2023 by engineers with 10+ years at MNCs and startups") |
| 1.6 | Typos in headlines and titles: "Techonologies", "Deveops", "Free Trail", "Maintainence", "We am committed", "We hired skilled developers" | Home, Service enquiry, Digital Transformation | Proofread every page |
| 1.7 | Service copy mismatched: DevOps card describes security; on Service enquiry, Maintenance has DevOps text and DevOps has Cloud Migration text | Home, Service enquiry | Rewrite each service blurb |
| 1.8 | First-person singular copy pasted from a CV ("As a passionate and experienced Golang developer… We am committed…") | Digital Transformation | Rewrite as company copy |
| 1.9 | Contact form request types (Cloud, Consulting, Digital Engineering, Enterprise Applications, Platform Operations, RPA, Testing) don't match the services you list | Contact | Use your real service list |
| 1.10 | Generic stock photos (living-room armchair, meeting rooms, 2020 template uploads) | Home, About, Digital Transformation | Real team photos, office, screenshots of work, architecture diagrams |
| 1.11 | No case studies, team, founders, certifications or client results anywhere | Site-wide | Add Case Studies and a Team section (see §8) |
| 1.12 | Footer "Let's Connect! Connect with entrepreneurs, build your network" is coworking template copy; no address, phone, email or social links | Footer | Contact details, LinkedIn, Clutch/GoodFirms, short company line |
| 1.13 | Logo file is `LogoAi-Purpl-ease-Watermark…png` (720px wide, shown at 183px) | Header | Clean SVG logo from the source design |

## 2. Conversion and lead capture

| # | Issue | Fix |
|---|---|---|
| 2.1 | Home hero slider buttons "Know More" and "Contact Us" link to `#` (go nowhere) | Link to the service page and Contact, or replace the slider with one static hero |
| 2.2 | The India phone number on Contact shows **+91 903 9003932**, but the link dials **9039343396** (different digits, no country code) | Confirm the right number; use `tel:+91…` format |
| 2.3 | Canada number is not clickable | Add `tel:+12267906396` |
| 2.4 | Main CTA "Get Your Free Trial" sounds like a SaaS product | "Book a free consultation" or "Get a free test project" |
| 2.5 | No phone, email, WhatsApp or booking link in header or footer | Add a header phone/WhatsApp, a footer contact block, and a Calendly or Cal.com booking link |
| 2.6 | Contact form fields have no visible labels (placeholder only); 7 fields is long for a first touch | Add labels; cut to name, email, service, budget range, message |
| 2.7 | Phone field defaults to +1 for every visitor | Default by visitor country or make phone optional |
| 2.8 | No confirmation that leads are stored (Contact Form 7 only emails) | Use Fluent Forms or Flamingo to store entries; send to CRM; add a thank-you page and a GA4 conversion event |
| 2.9 | Nothing proves results: no numbers, no logos with context, no reviews | Stat bar (projects, engineers, years, retention), Clutch badge, 2–3 case-study cards on Home |

## 3. SEO

| # | Issue | Fix |
|---|---|---|
| 3.1 | Every page has the same meta description ("Stand out in the digital landscape…") | Unique description per page, 140–155 characters |
| 3.2 | Titles are thin: "About us - Purplease", "Contact - Purplease", "Free Trail - Purplease" | e.g. "About Purplease: Golang & Cloud Engineering Team in India and Canada" |
| 3.3 | Home has 4 H1s (slider duplicates); About, Digital Transformation, Contact and Service enquiry have no H1 | Exactly one H1 per page |
| 3.4 | Only 6 indexable pages; one page ("Digital Transformation") tries to rank for Golang, DevOps, cloud and QA at once | One page per service and per "hire" intent (see §8) |
| 3.5 | No Open Graph image on Home, Contact and Service enquiry; others use 2020 stock photos | Branded 1200×630 share image |
| 3.6 | Schema marks Home as an "Article" with a "Person" author | In Rank Math set Home to WebPage, pages to WebPage/Service, keep Organization; add LocalBusiness for both offices, FAQPage on FAQs |
| 3.7 | Blog last updated May 2024 with only "Hello world!" | Content plan: 2 articles a month on Go, cloud migration, DevOps costs and hiring |
| 3.8 | Site tagline empty in WordPress settings; timezone not set | Settings → General |
| 3.9 | No Google Business Profile or location pages for India and Canada (not visible on site) | Create profiles; add addresses to Contact and footer |
| 3.10 | 404 and redirects: `www` → apex works, `/sitemap.xml` works, robots.txt OK | Keep; add 301s when page URLs change in the revamp |

## 4. Design and user experience

- The brand is called **Purplease** but the site is blue (#3b4fe0) with a navy footer; the purple only shows in the logo arrow. Move to a purple-led palette (deep violet + one bright accent).
- Rotating image slider hero: low engagement, hides the second message, adds weight. Use one static hero: headline, one sentence, one main button, proof line.
- Body text is light grey (#6e7180) on white at 16px in Poppins, which reads faint. Use darker text (#3f3f46 or darker) and a sharper font (Inter, Geist or Satoshi).
- Menu has only Home, Digital Transformation, About, Contact. "Digital Transformation" doesn't tell visitors what you sell. Add Services (mega-menu), Hire Developers, Case Studies, Blog.
- Tools & Technologies on Digital Transformation is 7 rows of logo tiles. Group them as one compact, filterable grid.
- Heavy scroll-reveal animations hide content until scrolled; keep them subtle and short.
- The Digital Transformation page is 6,857px tall on desktop with long text blocks; break it into separate service pages.
- On mobile the Digital Transformation slider overflows the screen width (content runs to 750px on a 390px screen), causing sideways scrolling.

## 5. Performance

Measured in a lab run (desktop/mobile, cached CDN):

| Page | Largest content paint (desktop / mobile) | Page weight | Requests |
|---|---|---|---|
| Home | 3.1s / 1.9s | 2.1 MB | 60 |
| About us | 2.4s / 2.5s | 2.1 MB | 58 |
| Digital Transformation | 2.4s / 2.6s | 2.6 MB | 64 |
| Contact | 1.6s / 1.9s | 1.9 MB | 56 |

Layout shift is low everywhere (under 0.1). Main fixes:

- **reCAPTCHA is loaded 3 times on every page** (≈350 KB each, about 1 MB total) even where there's no form. Load it only on form pages, once; or switch to Cloudflare Turnstile / Fluent Forms' built-in spam protection.
- Images are served far larger than shown (client logos 1077px shown at 232px, icons 512px at 164px, logo 720px at 183px). Resize and convert to WebP/AVIF; use SVG for logos and icons.
- Font Awesome solid font (153 KB) loads for a few icons; use inline SVG icons.
- The slider library (Swiper) loads on every page; it disappears with a static hero.
- Target after revamp: under 1 MB and under 35 requests per page, LCP under 2.0s on mobile.

## 6. Accessibility

- Images without alt text: Home 12 of 14, About 7 of 9, Digital Transformation 39 of 41, Pricing 14 of 14.
- Form inputs have no labels (placeholders only); screen readers can't name them.
- 2 empty links per page (icon-only links with no label) and 7+ tap targets under 24px tall on mobile.
- Grey body text and white text on mid-grey (#6d7080) sections are below comfortable contrast.
- Target: WCAG 2.2 AA.

## 7. Security and maintenance

| # | Issue | Fix |
|---|---|---|
| 7.1 | `/wp-json/wp/v2/users` publicly lists the login username **admin** | Rename the admin account (new admin user, delete old, reassign content); block the users endpoint for visitors |
| 7.2 | `xmlrpc.php` is open (brute-force and pingback abuse) | Disable XML-RPC unless the Jetpack/mobile app needs it |
| 7.3 | `/wp-login.php` is public at the default URL | Two-factor login, login rate limiting, optionally a custom login URL |
| 7.4 | `readme.html` and `license.txt` public; PHP version shown in `x-powered-by` header | Remove or block; hide header |
| 7.5 | No security headers (HSTS, X-Frame-Options, X-Content-Type-Options, Referrer-Policy) | Add via Hostinger/LiteSpeed `.htaccess` or a headers plugin |
| 7.6 | PHP 8.1 is end of life (security support ended Dec 2025) | Upgrade to PHP 8.3+ in Hostinger hPanel after testing on staging |
| 7.7 | Comments open on posts (sample comment visible) | Disable comments site-wide unless the blog needs them |
| 7.8 | DMARC is `p=none` (domain can be spoofed in phishing emails) | Add DKIM for Hostinger and Google, then move DMARC to `p=quarantine` with reporting |
| 7.9 | No visible backups or staging | Daily off-site backups (UpdraftPlus to Google Drive/S3), Hostinger staging for every change |
| 7.10 | No Privacy Policy, Terms or cookie notice, yet GA4 and reCAPTCHA set cookies and the form collects personal data (GDPR, Canada PIPEDA, India DPDP Act) | Add Privacy Policy, Terms, cookie consent (Complianz or CookieYes), consent checkbox on forms |

## 8. Recommended new site structure

| Page | Status | Purpose |
|---|---|---|
| Home | Rebuild | Clear positioning, proof, services, case studies, process, testimonials, CTA |
| Services hub + Golang Development, Cloud Migration (AWS/GCP), DevOps & CI/CD, Web App Development, Mobile App Development, QA & Test Automation, Maintenance & Support | New | One page each: problem, approach, tech, case study, FAQ, CTA (ranks for each search intent) |
| Hire Developers (Golang, DevOps, Full-stack) | New | Engagement models, vetting, time-zone overlap, free test project, rates "from" |
| Case Studies | New | Problem → architecture → results with numbers |
| Industries (SaaS, FinTech, Healthcare, eCommerce) | New | Optional, for SEO and relevance |
| How We Work | New | Discovery → sprints → CI/CD → support; tools; communication |
| Pricing / Engagement Models | Replace | Fixed price, dedicated team, hourly; "starting from" |
| About | Rewrite | Founders, team photos, offices in India and Canada, values with evidence |
| Blog / Insights | New | 2 posts a month |
| Careers | New | Optional |
| Contact / Book a Call | Rebuild | Short form, booking calendar, WhatsApp, both offices |
| Privacy Policy, Terms, Cookie Policy | New | Legal requirement |

Old URLs to redirect: `/digital-transformation/` → `/services/golang-development/` (or the Services hub), `/service-enquiry/` → `/contact/`, `/pricing/` → `/engagement-models/`, `/hello-world/` → `/blog/`.

## 9. Plugin and theme changes

Keep: Astra + child theme, Spectra, Rank Math, LiteSpeed Cache (already active via Hostinger).

Add: ACF (Case Study, Service, Team, Testimonial content types), Fluent Forms (replaces Contact Form 7, stores leads), Complianz or CookieYes, a security plugin (Wordfence or Solid Security) with 2FA, UpdraftPlus, a WebP/AVIF image optimiser (LiteSpeed image optimisation or ShortPixel), Microsoft Clarity for heatmaps.

Remove: Contact Form 7 + country phone field (after migrating forms), unused Spectra blocks, Font Awesome if icons move to SVG.

## 10. Priority plan

**This week (1–2 hours, no redesign needed):**
1. Unpublish Pricing; delete "Hello world!"; remove fake testimonials.
2. Fix the hero buttons, the India phone link and the Canada link.
3. Fix typos and the swapped service descriptions.
4. Unique titles and meta descriptions on all pages; one H1 per page.
5. Rename the `admin` user, disable XML-RPC, turn on 2FA and backups.

**Next 2 weeks:**
6. Privacy Policy, Terms, cookie consent.
7. Load reCAPTCHA only on form pages; resize and convert images; add alt text.
8. PHP 8.3 upgrade on staging, then live; DKIM and DMARC.

**Weeks 3–8 (revamp):**
9. Positioning and sitemap (§8) → wireframes → purple design system in Figma.
10. Build on staging: child theme styles, new Home, service pages, Hire Developers, Case Studies, Contact.
11. Content: 3 case studies, team photos, real testimonials, first 4 blog posts.
12. Launch with 301 redirects, GA4 conversion events, Search Console, Clarity.

## Questions for the owner

- Which India number is correct: +91 903 9003932 (shown) or 903 934 3396 (linked)?
- Founding year and team size to state publicly.
- Can we name clients (Innowhyte, Cite, SOS Vertigo, Telmio) with project results?
- Office addresses for India and Canada.
- Main buyer: startups needing a dev team, or enterprises migrating to cloud?
