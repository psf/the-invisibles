# Handoff: upstream candidates for hugo-theme-popular

Findings from porting pypodcats.live (a podcast site) onto the Popular theme.
The port lives on the `popular-theme-poc` branch of `psf/the-invisibles`; every
item below references a working site-level override there that can serve as the
starting implementation. Paths starting with `layouts/` or `content/` are in
that repo; paths starting with `theme:` are in `hugo-theme-popular`.

General rules that apply to every item (from the theme's AGENTS.md):

- Each change needs the mirrored Astro change in `astro-theme-popular`, updates
  to both `PARITY.md` files, and, for new front-matter or config keys, an update
  to Astro's `src/content.config.ts`. Use the same branch name in both repos so
  CI pairs them.
- New user-facing strings go through `i18n/en.toml` plus Astro's `STRINGS`.
- Config and front-matter keys must be descriptive words, no abbreviations.
- No em dashes in docs or demo copy.

Suggested implementation order: 1 (bug fix), then 3 and 4 (small knobs), then
6, then 5, then 7.

---

## 1. Date-less pages render "Jan 0001" in post cards

**Problem.** `theme: layouts/partials/post-card.html` always prints
`{{ .Date | time.Format "Jan 2006" }}`. The default section list
(`theme: layouts/_default/list.html`) renders child pages through this card, so
any section of static pages (about pages, policies) shows "Jan 0001" and, when
the pages have no `image`, an empty or fallback media slot.

**Proposal.**
- In `post-card.html`, wrap the date in `{{ if not .Date.IsZero }}`.
- When both the date and the author names are absent, omit the eyebrow line
  entirely instead of leaving a stray separator.
- Consider a plainer card variant for date-less pages in the default list, a
  title plus description card with no media block. See the reference override
  for the shape.

**Reference.** `layouts/about/list.html` (plain title and description cards),
written because of this exact defect.

**Parity.** Mirror in Astro's `PostCard` component. No new keys, no i18n.

**Acceptance.** A section of pages without `date` or `image` front matter shows
cards with no date, no empty media box, and no "Jan 0001" anywhere in the
built site. Existing demos render unchanged.

---

## 3. Configurable authors section (`authorsSection`)

**Problem.** The `/authors/` section prefix is hardcoded in three places:
`theme: layouts/partials/author-line.html`,
`theme: layouts/partials/post-card.html`, and the author-box resolution block
in `theme: layouts/blog/single.html`. Sites where the organizers write the
blog (PyPodcats: the hosts are the authors) must override all three files to
change one string, and end up maintaining a parallel authors section or
carrying the overrides forever.

**Proposal.** Add `params.authorsSection`, default `"authors"`. All three
lookups become `site.GetPage (print "/" site.Params.authorsSection "/" .)` (or
equivalent). Document it next to the authors content model with the organizers
use case as the example.

**Reference.** `layouts/partials/author-line.html`,
`layouts/partials/post-card.html`, `layouts/blog/single.html` on the PoC
branch: identical to the theme's files except `/authors/` became `/hosts/`.

**Parity.** Astro: the same three components resolve author slugs; the new key
goes in `src/config.ts` and both `PARITY.md` files. No i18n.

**Acceptance.** With the param unset, everything behaves as today. With
`authorsSection = "organizers"`, post bylines link to organizer pages and the
author bio boxes at the end of posts render from organizer entries.

---

## 4. Configurable team section for the homepage (`teamSection`)

**Problem.** `theme: layouts/index.html` hardcodes
`where site.RegularPages "Section" "organizers"` and the `organizers/` link in
the "All organizers" button. A site whose people live in a differently named
section (hosts, crew, committee) must override the whole homepage template for
two strings. The heading text is already configurable via the home page
`[team]` block, only the section name is not.

**Proposal.** Add `params.teamSection`, default `"organizers"`. Use it for the
section query and the button link. The `[team]` block already covers the copy.

**Reference.** `layouts/index.html` on the PoC branch, the `$orgs` line and the
button href are the only team-related edits.

**Parity.** Astro homepage pulls the same collection; add the key to
`src/config.ts` and both `PARITY.md` files. No i18n.

**Acceptance.** Default unchanged. With `teamSection = "hosts"`, the homepage
team grid and button use the hosts section.

---

## 5. Organizer profile pages and linkable organizer cards

**Problem.** `theme: layouts/partials/organizer-card.html` links nowhere, by
design, because the theme ships no `organizers/single.html`. But Hugo renders
single pages for organizer entries anyway (through `_default/single.html`, as
bare title plus prose), so the pages exist, just unreachable and underwhelming.
Any site that wants clickable people cards overrides the card and builds a
profile page from scratch.

**Proposal.**
- Add `theme: layouts/organizers/single.html`: page hero (eyebrow from `role`),
  `author-box.html` persona card, then `.Content` as prose. This mirrors what
  speakers and authors already get.
- Link the card's photo and name to `.RelPermalink` (keep `style="color:inherit"`
  on the name link so the card look does not change).
- If always-on linking is not wanted for existing demos, gate it behind
  `params.organizerPagesEnabled` (default true is recommended, the pages exist
  either way).

**Reference.** `layouts/partials/organizer-card.html` (linked card) and
`layouts/organizers/single.html` (profile page; ignore the stats strip and the
episodes/posts grids there, those are covered by item 7 and are otherwise
site-specific).

**Parity.** Astro needs the organizer detail route plus the card link. Update
both `PARITY.md` files; the eyebrow falls back to a plain string today, route
it through i18n (`eyebrowOrganizer`) in both repos.

**Acceptance.** Organizer cards on the list page and the homepage link to a
profile page showing the persona card and any page body. Demo organizer pages
render sensibly without extra front matter.

---

## 6. Back link to the parent section on plain pages

**Problem.** Pages nested in a section (about/conduct, about/financials) render
through `theme: layouts/_default/single.html` with no way back to their parent.
Blog posts and episodes have back links; plain section children are dead ends.

**Proposal.** In `_default/single.html`, when `.Parent` exists and is not the
home page, render a back link above the content, same style as the blog
single's "All posts" link. Label: the parent's title, preferring a new optional
parent front-matter key for long titles (the PoC used `menu_label`; a more
descriptive name like `shortTitle` fits the theme's naming rules better,
pick one and register it in the content model).

**Reference.** `layouts/_default/single.html` and the `menu_label` in
`content/english/about/_index.md` on the PoC branch.

**Parity.** Astro's plain page layout gets the same link; new front-matter key
goes in `src/content.config.ts` and both `PARITY.md` files. The link text is
content-derived, so no i18n string is strictly needed; if an aria-label is
added, use i18n.

**Acceptance.** A page at `about/x/` shows a back link to `/about/` with the
parent's short title; root-level pages (subscribe, contact) show none.

---

## 7. Generalize computed stat values (`@count:<section>`)

**Problem.** The home page stats support exactly one computed value,
`@pastEventCount`. Sites want other live numbers: PyPodcats needed episode and
blog-post counts on the homepage and again on host profile pages, and had to
hand-count or template them.

**Proposal.** Extend the stat value resolver in `theme: layouts/index.html`
(and factor it into a partial so other templates can reuse it):

- `@count:<section>` : number of regular pages in that section.
- Keep `@pastEventCount` as is for compatibility.
- Optional niceties, only if cheap: the same "70+" rounding once at ten or
  more, controlled by an explicit suffix such as `@count:episodes:rounded`,
  rather than always-on, so podcast-style exact counts stay exact.

Factoring it into a partial (for example `partials/stat-value.html`) lets
custom pages, like the PoC's host profiles with "episodes hosted" and "blog
posts" strips, reuse the resolver instead of reimplementing it.

**Reference.** The stats strip in `layouts/organizers/single.html` on the PoC
branch shows the demand; it computes per-person counts inline today.

**Parity.** Astro computes stats in the homepage component; mirror the
resolver, document the magic values in both `PARITY.md` files and the
configuration reference. No i18n.

**Acceptance.** `value = "@count:blog"` on a demo homepage renders the live
post count; `@pastEventCount` output is unchanged for all four demos.

---

## 8. `check-jsonld.py` silently passes on a minified build

**Problem.** `theme: scripts/check-jsonld.py` finds JSON-LD blocks with the
regex `<script[^>]*type="application/ld\+json"[^>]*>`, which requires the
`type` value to be double-quoted. Hugo's minifier (`--minify`, the normal
production build) strips those quotes, emitting `<script
type=application/ld+json>`. The regex then matches zero blocks and the script
prints `OK: 0 JSON-LD block(s) valid` and exits 0: a false pass. Since the
whole point of the 0.6.0 SEO work is the structured data, CI that runs the
checker against a minified build (or a site that minifies, like this podcast
port) gets green with nothing actually validated. Only a non-minified build
exercises the check today.

Found while adopting 0.6.0 on the PoC branch: `hugo --minify` produced valid
Organization / BlogPosting / FAQPage blocks that the checker reported as
"0 valid"; the same build unminified reported them all.

**Proposal.**
- Loosen the block regex to accept an optionally quoted (single or double)
  attribute value, e.g. `type\s*=\s*["']?application/ld\+json["']?`, keeping
  the existing `[^>]*` allowances for attribute order.
- Belt and suspenders: have the checker fail (non-zero) when it finds zero
  blocks in a directory that contains HTML, so "found nothing" can never read
  as "everything passed" again. Gate this behind a flag if any legitimately
  block-free build needs to pass.
- Point at least one CI invocation at the actual minified output, so the
  production artifact is what gets validated.

**Reference.** `scripts/check-jsonld.py` (the `BLOCK` regex) in the theme; no
site-level override, this is a theme-tooling fix. The PoC validated its own
blocks by building unminified into a scratch dir as a workaround.

**Parity.** The script ships byte-identical in both repos (PARITY.md Tier 1),
so the same regex fix lands in `astro-theme-popular`. Astro's HTML minifier
strips quotes the same way, so both are affected; keep the file identical. No
i18n, no config, no front-matter keys.

**Acceptance.** Running the checker against a `--minify` build of a demo with
Organization/BlogPosting/FAQPage blocks reports the real block count and
validates each; a build with zero blocks in HTML-bearing output fails loudly
rather than printing "OK: 0". Both repos' copies stay byte-identical.

---

## Not included, follow-ups discussed separately

- Item 2 (speaker bio duplicated in hero lead and persona card) needs a design
  decision about what the hero lead should show, raised separately.
- Docs candidates: migrating images from assets-pipeline themes (the
  `module.mounts` static trick and its "declaring a static mount removes the
  default" gotcha), and a "beyond meetups" case study based on this podcast
  port.
