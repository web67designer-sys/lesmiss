# LES MISS NYC — digital flagship redesign concept

An independent, unaffiliated design prototype. Run with `python3 server.py`, then open `http://localhost:8000`. The Python server provides a small read-only proxy to the store's public Shopify product JSON. The product edit reads current names, prices, availability and images directly from the official store; if the request fails, visitors see a link to the official shop instead. The rest of the site is static. Python 3 is the only server dependency. Google Fonts and product images require a network connection; the editorial images are optimized local copies.

## Important scope and integration status

This is **not a production-ready replacement** for the existing Shopify theme. The official store remains the source of truth. All collection, product, account, cart, search, booking and builder links navigate to lesmissnyc.com. The redesigned page does not contain a Shopify cart drawer, embedded charm builder, native product detail template, Shopify analytics, or a checkout integration. The current official Charm Builder uses Shopify/theme and bundle-app functionality; reproducing it safely, including variant IDs, inventory, pricing, discount rules and cart attributes, requires access to the actual theme and relevant app configuration. No simulated cart, fake checkout, or invented bundle-discount calculations are included.

Before publishing commercially: obtain written permission for the brand imagery and branding; integrate the design into an approved Shopify theme or authorized storefront architecture; preserve existing theme/app, SEO URLs, tracking, account and booking integrations; review policies and content; and test the builder, bundle discounts, cart, checkout, mobile, accessibility and analytics in a staging store with client approval. This demo does not alter the live store. Local business schema references the official store; add canonical and product structured data only when integrating on the authorized domain.

## Research notes

Official homepage, Charm Builder, charm and all-product collections, Shop IRL, Press and Charm Bar Events were inspected. `/pages/stories` returned 404 during research, so no link to that page is used. The live shop lists a $200 non-refundable styling deposit applied toward purchases; confirm all service information with the store before publication. Press references correspond to links displayed on the official homepage. The official account URL redirects to Shopify customer authentication; the redirect returned 406 to the automated test client and needs browser validation.

## Asset rights and provenance

Locally optimized images in `assets/lesmiss/` are derived from official Les Miss NYC Shopify-hosted images and are included only to demonstrate this redesign. Rights are not granted by this prototype; obtain permission before external or commercial reuse. See `ASSET-SOURCES.json` for original URLs. Empty press folder is intentional: publication names link to coverage referenced by the official homepage rather than assuming rights to third-party logos. Product cards load official images directly from Shopify.

## Checks performed

- Local server responded successfully and the product endpoint returned four current Shopify products.
- Official in-site shopping, builder, product, visit, event, policy and booking links responded HTTP 200 at review time. `/account` redirected to Shopify authentication, which responded 406 to the non-browser test client.
- Editorial assets were downloaded from official Shopify URLs and locally optimized.
- No end-to-end purchase, discount, builder, booking, visual-browser, mobile-device or assistive-technology testing has been performed. Those are required before launch.

## Editorial exploration update

The concept now includes a three-part, scroll-led Charm Bar field guide and a selectable charm-style discovery section (gold, silver, crystal, enamel and painted). Style selections change the editorial image and link to the corresponding official collection; they are not product filters or a replacement for the live Charm Builder. A paper-like texture and photograph captions support the analog direction. Motion continues to respect reduced-motion preferences. Browser and assistive-technology testing remain necessary.

## November 2026 — IRL and events update

The Shop IRL page supplied verified details for the Nolita flagship and Brooklyn atelier; additional images are sourced from that official page. The linked Partiful Jewellery Box Show took place on October 23, 2026 and is presented as a past event, not an upcoming ticket offer. Check current hours, availability, deposit terms and future events with the official store.

Browser checks were run locally in headless Chromium at desktop, tablet, and 390px/320px mobile sizes. Menu, search, charm-style selectors, local assets and live product feed were exercised. This does not verify an actual Vercel deployment, Shopify checkout, booking, discounts or assistive technologies.
