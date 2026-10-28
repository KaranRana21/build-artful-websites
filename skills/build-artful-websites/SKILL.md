---
name: build-artful-websites
description: Build or redesign premium websites that feel authored rather than AI-generated. This is the house orchestration skill: it combines anti-slop art direction from design-taste-frontend with Emil-style design engineering, motion restraint, performance, accessibility, security, SEO, responsive craft, honest content, and production QA. The reference quality bar is authored design, never a reusable visual template.
---

# Build Artful Websites

## Mission

Build websites that feel designed by people with taste and engineered by people who care about the invisible details.

The goal is not to make every website look alike. Every project must develop its own visual language from its audience, brand, content, constraints, and references. Treat exceptional composition, interaction craft, performance, responsiveness, and production discipline as a quality benchmark, never as a visual template.

This skill orchestrates new websites and redesigns. It works independently; optional companion skills deepen specialized decisions.

## Integrated design engines

When available, read and apply these optional companion skills in this order:

1. `design-taste-frontend`
2. `emil-design-eng`
3. `find-animation-opportunities`
4. `animate`
5. `improve-animations`
6. `review-animations`

Do not merely name them. Use them as separate responsibilities.

### Authority split

- **Build Artful Websites** owns the complete product outcome and resolves conflicts.
- **Taste / anti-slop discipline** owns design read, art direction, composition, typography, hierarchy, visual density, brand distinctiveness, and removal of template patterns.
- **Emil design engineering** owns interaction feel, motion decisions, easing, timing, interruptibility, press/hover/focus behavior, perceived responsiveness, and animation restraint.
- **Project requirements** override aesthetics whenever usability, accessibility, regulation, trust, or business functionality demands it.

If upstream skills are unavailable, follow the embedded rules below. The house standard must not disappear because an external dependency is missing.

---

# 1. Read the room before touching code

Inspect everything the user supplied:

- website brief
- business type and audience
- desired tone
- logo and brand assets
- reference sites or screenshots
- existing repository and stack
- content and claims
- required integrations
- deployment target
- accessibility, performance, security, SEO, or legal constraints

For redesigns, inspect the live site and source before proposing changes. Preserve what is already strong.

State a concise design read before implementation:

`Reading this as: <site type> for <audience>, with a <visual language>, leaning toward <design family / implementation direction>.`

Ask at most one clarifying question only if two materially different directions remain plausible. If the context is enough, infer and execute.

---

# 2. Set the design dials

Set these intentionally for every project:

- `DESIGN_VARIANCE` — symmetry/predictability to expressive/asymmetric
- `MOTION_INTENSITY` — static to cinematic
- `VISUAL_DENSITY` — gallery-like to information-dense

Typical starting points:

- premium consumer / luxury brand: `8 / 6 / 3`
- creative agency / experimental portfolio: `9 / 8 / 3`
- mainstream marketing site: `7 / 5 / 4`
- local service business: `7 / 4 / 4`
- trust-first / regulated / accessibility-critical: `4 / 2 / 5`

These are starting points, not aesthetic presets.

---

# 3. Write the creative thesis

Before coding, define:

- one memorable truth
- three adjectives
- one productive visual tension
- what the website must never feel like
- the primary user action
- the emotional first impression

Example structure:

- **Truth:** what the visitor should remember
- **Tension:** precision vs warmth, heritage vs modernity, calm vs energy, etc.
- **Adjectives:** three project-specific words
- **Never:** explicit anti-goals

Create or update `DESIGN.md` so future work inherits the actual brand logic instead of reverse-engineering screenshots.

---

# 4. Anti-AI-slop rules

Never default to these because they are easy for a model to generate:

- centered hero + centered paragraph + two centered buttons
- dark mesh gradient behind enormous generic headline
- purple/blue AI glow
- three identical feature cards
- generic bento grids with no content reason
- glassmorphism everywhere
- floating gradient blobs
- excessive rounded cards
- random serif font just to signal premium
- Inter + slate as an automatic default
- tiny uppercase microcopy everywhere
- fake logos, clients, reviews, numbers, awards, or testimonials
- stock startup copy such as "unlock", "reimagine", "seamless", "next-generation" without concrete meaning
- animations on every viewport entry
- parallax because the page feels empty
- custom cursor without a brand/function reason
- hover effects that hide essential information from touch users

A premium site should feel more authored, not more decorated.

---

# 5. Static design before motion

The website must look exceptional with animation disabled.

Build quality in this order:

1. content truth
2. information architecture
3. composition
4. typography
5. spacing and rhythm
6. imagery and material
7. interaction states
8. motion

Never use motion to rescue weak composition.

Each major section needs a clear compositional idea. Avoid repeating the same two-column layout, card shape, heading formula, or spacing interval across the entire page.

Alternate density and quiet. Negative space is an active design material.

---

# 6. Typography discipline

Typography should carry more of the premium feeling than decoration.

Rules:

- choose fonts because they fit the brand, not because they are fashionable
- do not default to serif for creative or premium work
- mixed families require a real reason
- do not inject a random serif word inside a sans headline for visual interest
- hand-tune display line breaks on desktop and mobile
- preserve descender clearance on italics
- small text must remain readable and authoritative
- avoid exaggerated tracking on every uppercase label
- body copy should have comfortable measure and leading
- use type scale contrast intentionally rather than making every heading huge

Use self-hosted fonts / framework font tooling when practical and preserve `font-display` behavior.

---

# 7. Color and material

Prefer a restrained palette derived from the brand.

- one dominant accent is usually enough
- neutral colors should be project-specific rather than default Tailwind gray
- gradients require a material or lighting reason
- blur, grain, borders, shadows, texture, and transparency are seasoning, not the visual system
- avoid neon glow unless the brand genuinely calls for it
- maintain accessible text/control contrast

---

# 8. Imagery and art direction

Use real brand imagery when available.

If imagery is limited, create variety through:

- crop
- scale
- framing
- detail views
- negative space
- sequencing
- masks
- lighting treatment

Do not pretend repeated crops are different products/projects.
Do not invent evidence.
Do not use scraped imagery as if it belongs to the client.

Responsive images, dimensions, loading priority, decoding, and alt text are part of art direction.

---

# 9. Interaction craft

Every pressable surface must be reviewed for:

- default
- hover when hover exists
- active / pressed
- focus-visible
- selected
- disabled when relevant
- loading when relevant
- success/error where relevant
- touch behavior
- keyboard behavior

Frequent interactions should feel immediate.

A subtle press response around `scale(.97)` is a useful default where the geometry supports it, but never apply it mechanically.

Directional icons move in the direction they imply.

Do not use `transition: all`.

Popover/menu/dropdown motion should feel connected to its trigger. Modals are centered surfaces and do not need fake trigger-origin behavior.

---

# 10. Motion decision gate

Before implementing an animation, answer four questions:

### Frequency

- 100+ times/day / keyboard-driven: no decorative animation
- tens/day: near-imperceptible or none
- occasional: standard motion allowed
- rare/first-time: delight budget exists

### Purpose

Motion must serve at least one:

- feedback
- spatial consistency
- state indication
- explanation
- preventing a jarring change
- rare delight

`It looks cool` is not enough.

### Speed

Useful defaults:

- press feedback: `100–160ms`
- tooltip/small popover: `125–200ms`
- dropdown/select: `150–250ms`
- modal/drawer: `200–500ms`
- editorial/marketing reveal: longer only when frequency is low and the composition earns it

Most UI motion should stay below 300ms.

### Function

Do not make information move while the user is trying to read, compare, enter, or act on it.

---

# 11. Motion implementation standard

Preferred curves:

```css
--ease-out: cubic-bezier(.23,1,.32,1);
--ease-in-out: cubic-bezier(.77,0,.175,1);
--ease-drawer: cubic-bezier(.32,.72,0,1);
```

Rules:

- entering/exiting UI → strong ease-out
- moving/morphing on screen → ease-in-out
- constant marquee/progress → linear
- avoid ease-in on responsive UI
- never animate from `scale(0)`; use a subtle initial scale plus opacity if scale is needed
- prefer transforms and opacity
- use transitions for rapidly retargeted states
- use springs for gesture/momentum/interruptible physics, not as a generic UI personality
- stagger only when it improves hierarchy; keep it tight
- gate hover-only motion behind fine-pointer/hover capability
- reduced motion ships with the feature, not later

Use the cheapest capable tool. Do not install a motion library for a basic fade or press state.

---

# 12. Loader standard

A loader is allowed only when it is a deliberate brand ceremony or unavoidable wait state.

For branded opening sequences:

- the underlying first frame should still be complete
- set a hard maximum duration
- never use fake excessive loading time
- provide reduced-motion and constrained-data fallback
- ensure it cannot trap the visitor if JS/assets fail
- use a decisive exit into the hero
- prevent stale asset combinations in production

No loader is better than a weak loader.

---

# 13. Responsive composition

Mobile is not desktop collapsed into one column.

Audit at minimum:

- 320
- 360
- 390
- 430
- 768
- 1024
- 1440
- 1920

Requirements:

- zero horizontal overflow
- hand-tuned hero line breaks
- no clipped display type
- no overlapping fixed elements
- touch targets remain usable
- pointer-only effects disappear or degrade safely
- navigation is intentionally composed for touch
- the hierarchy remains clear when grids collapse
- imagery crops are re-art-directed for mobile

Use `dvh`-aware viewport units for full-height mobile compositions when supported by the stack.

---

# 14. Stack decisions

Do not rewrite a working project into the skill author's favorite stack.

For existing sites: preserve the existing architecture unless a change has concrete value.

For new sites: pick the lowest-complexity stack that supports the desired experience.

React/Next.js/Tailwind are appropriate defaults for many interactive builds, but static HTML/CSS/JS can be the better premium engineering choice for a small, dependency-light site.

Before importing any library, verify it exists in the project. Avoid dependency inflation.

---

# 15. Performance standard

Premium is invalid if the website feels slow.

Protect:

- LCP
- CLS
- INP
- first paint
- scroll smoothness
- mobile battery/CPU

Rules:

- responsive images and explicit dimensions
- preload only genuinely critical assets
- isolate client-side interactivity
- avoid layout-thrashing scroll handlers
- avoid expensive continuous blur/filter effects
- prefer CSS for predetermined motion and JS only where dynamic behavior needs it
- avoid rerendering component trees on continuous pointer/scroll values
- lazy-load below-fold noncritical media

Target where realistic:

- 90+ Lighthouse Performance
- 95+ Accessibility / Best Practices / SEO

Do not manipulate the test. Improve the site.

---

# 16. Accessibility standard

Target WCAG-minded production quality.

Required:

- semantic regions and headings
- one meaningful H1
- keyboard-safe navigation and controls
- visible focus
- sufficient contrast
- meaningful form labels
- status/error announcements where needed
- reduced-motion support
- alt text based on image purpose
- large enough touch targets
- no essential information encoded only in motion, hover, color, or sound

Reduced motion means a composed gentler alternative, not a broken static afterthought.

---

# 17. Security standard

Design work must not weaken security.

Preserve or implement as appropriate:

- secrets server-side only
- environment variables
- input validation
- output escaping
- origin checks for mutations
- rate limiting for public forms/actions
- least-privilege data access
- CSP and security headers
- safe external links
- minimal logs without unnecessary personal data

Never expose keys to make a frontend demo work.

---

# 18. Content, proof, and honesty

Never invent:

- customers
- testimonials
- awards
- rankings
- revenue
- metrics
- review counts
- certifications
- capabilities that are not implemented

When imagery is concept art, label it honestly if the context requires it.

Write human copy that is specific to the business. Avoid AI filler and inflated superlatives.

---

# 19. SEO and production basics

Every public site should consider:

- unique page titles/descriptions
- canonical URLs
- robots/sitemap
- semantic content structure
- Open Graph metadata
- structured data only for facts actually known
- crawlable text
- descriptive link labels
- sensible redirects and clean URLs

SEO cannot override clarity or brand voice.

---

# 20. The permanent build workflow

## Phase 0 — Recon

Inspect repository, live site if one exists, assets, integrations, constraints, and references.

## Phase 1 — Design Read

Define audience, page kind, creative thesis, design dials, primary action, anti-goals, and evidence boundaries.

## Phase 2 — DESIGN.md

Create/update the project design doctrine before substantial implementation.

## Phase 3 — Static composition

Build information hierarchy, section rhythm, typography, imagery, and responsive layout. No decorative motion yet.

## Phase 4 — Anti-slop review

Ask:

- Does this resemble a common AI landing-page pattern?
- Are there unnecessary cards/containers?
- Is the composition too symmetrical/predictable for the brief?
- Does each section have a reason for its layout?
- Could the design belong to a random company if the logo were removed?

Fix those first.

## Phase 5 — Interaction pass

Implement press, hover, focus, menus, forms, tabs, accordions, selected states, feedback, and perceived responsiveness.

## Phase 6 — Animation opportunity filter

Identify only the high-leverage moments that genuinely benefit from motion. Reject the rest.

## Phase 7 — Motion implementation

Implement the selected moments with exact purpose, timing, easing, interruption, reduced-motion, and pointer behavior.

## Phase 8 — Animation review

Run the review with a deletion bias. Remove anything slow, repetitive, generic, distracting, physically wrong, or unnecessary.

## Phase 9 — Responsive recomposition

Audit all target widths. Mobile receives art direction, not cleanup.

## Phase 10 — Performance / accessibility / security / SEO

Audit the complete system, not only the pretty homepage.

## Phase 11 — Functional QA

Test important user journeys, forms, navigation, error states, integrations, 404s, external links, and production headers.

## Phase 12 — Production verification

Deploy only with authorization. Verify the live domain serves the intended commit, assets, interactions, forms, security behavior, and responsive experience.

---

# 21. Required review format

When auditing an existing site or completed pass, use:

| Before | After | Why |
| --- | --- | --- |
| current issue | proposed/final behavior | design/engineering reason |

Prioritize by leverage. Do not pad the review with cosmetic suggestions.

---

# 22. Final quality gates

Do not call a website finished until all are true:

- the brand is identifiable without relying only on its logo
- the static page looks excellent before animation
- the layout does not read as an AI template
- typography feels chosen, not defaulted
- every major section has an intentional composition
- motion has purpose and appropriate frequency
- interactions feel immediate
- mobile feels equally designed
- no horizontal overflow at target widths
- keyboard and reduced-motion experiences work
- content/claims are honest
- performance remains strong
- security was not weakened
- critical journeys work in production

Final test:

**Would a strong designer say this feels authored, and would a strong engineer trust it in production?**

If either answer is no, continue refining.

---

# 23. Advanced component integration

For premium interaction patterns, 3D/WebGL scenes, complex galleries, spatial project indexes, and GSAP sequences, read [ADVANCED-COMPONENT-INTEGRATION.md](ADVANCED-COMPONENT-INTEGRATION.md). Its principles are optional by project fit, mandatory when implementing an advanced component. Do not force demonstration effects into unrelated products.
