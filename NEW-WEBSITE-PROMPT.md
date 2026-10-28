# Universal New Website Launcher

Use this prompt whenever starting a new website with the Build Artful Websites standard.

---

Use the **Build Artful Websites** house skill for this entire project.

Before you design or code anything:

1. Locate and read installed `build-artful-websites/SKILL.md`.
2. Locate and read `build-artful-websites/ADVANCED-COMPONENT-INTEGRATION.md`.
3. If the project also contains these installed skills, read and apply them in this exact order:
   - `design-taste-frontend`
   - `emil-design-eng`
   - `find-animation-opportunities`
   - `animate`
   - `improve-animations`
   - `review-animations`
4. If the GreenSock skill pack is installed, also use the relevant GSAP skills when complex choreography genuinely earns them:
   - `gsap-core`
   - `gsap-frameworks`
   - `gsap-performance`
   - `gsap-plugins`
   - `gsap-react`
   - `gsap-scrolltrigger`
   - `gsap-timeline`
   - `gsap-utils`
5. Treat `Build Artful Websites` as the orchestrator and final authority for the complete website outcome.
6. Taste owns art direction/composition. Emil-style rules own interaction/motion judgment. GSAP skills own complex implementation details when GSAP is the right tool. Project usability, accessibility, security, performance, and business requirements override aesthetics.

## Project brief

Build:
`[DESCRIBE THE WEBSITE / BUSINESS / PRODUCT]`

Audience:
`[WHO THIS IS FOR]`

Primary action:
`[WHAT THE VISITOR SHOULD DO]`

Brand assets / references:
`[LOGO, COLORS, EXISTING SITE, SCREENSHOTS, REFERENCES, OR NONE]`

Required features / integrations:
`[FORMS, CMS, AUTH, PAYMENTS, BOOKING, DATABASE, EMAIL, WHATSAPP, ETC.]`

Preferred stack / hosting if fixed:
`[STACK OR "choose appropriately"]`

## Operating requirement

Do not build a generic AI landing page.

The output must be authored, brand-specific, responsive, accessible, performant, secure, and production-ready. Use exceptional authored design and engineering as a **quality benchmark**, never a visual template. Do not copy any reference brand's colors, typography, layout, or motion language unless this project's own brief calls for them.

## Phase 1 — Read the room

Before coding, inspect all supplied material and produce a concise design read:

`Reading this as: <site type> for <audience>, with a <visual language>, leaning toward <design family / implementation direction>.`

Then define:

- `DESIGN_VARIANCE`
- `MOTION_INTENSITY`
- `VISUAL_DENSITY`
- one memorable truth
- three brand adjectives
- one productive visual tension
- primary action
- what this website must never feel like

If the brief is sufficiently clear, do not ask follow-up questions. Make strong design decisions and proceed.

## Phase 2 — Create the design doctrine

Create `DESIGN.md` before substantial implementation.

Document:

- creative thesis
- audience
- primary action
- design dials
- typography direction
- color/material system
- grid/composition approach
- image/art direction
- interaction vocabulary
- motion vocabulary
- accessibility constraints
- performance budget
- security constraints
- mobile behavior
- explicit anti-goals

This file becomes the project's permanent visual/product doctrine.

## Phase 3 — Static design first

Build the page so it looks exceptional with motion disabled.

Work in this order:

1. information architecture
2. content hierarchy
3. section composition
4. typography
5. spacing/rhythm
6. imagery/material
7. responsive composition

Do not add decorative animation yet.

Reject common AI patterns unless the brief specifically earns them:

- centered hero + paragraph + two buttons
- three equal cards
- purple/blue glow
- generic bento grid
- glassmorphism everywhere
- random blobs
- giant type with no compositional reason
- default Inter/slate styling
- serif simply to look premium
- excessive rounded containers
- fake testimonials/metrics/logos

Every major section must have its own compositional idea.

## Phase 4 — Anti-slop review

Before motion, audit the static build using:

| Before | After | Why |
| --- | --- | --- |

Ask:

- Could this belong to a random company if the logo disappeared?
- Does this resemble a common AI-generated landing page?
- Is any section using a card/grid because it was easy rather than correct?
- Is the typography actually brand-specific?
- Is mobile intentionally composed or merely stacked?

Fix all high-leverage issues before proceeding.

## Phase 5 — Interaction engineering

Apply Emil-style design engineering to every pressable or stateful element:

- default
- hover
- active
- focus-visible
- selected
- disabled
- loading
- error/success where relevant
- keyboard behavior
- touch behavior

Keep frequent interactions immediate.

Never use `transition: all`.
Never use `scale(0)` entrances.
Avoid `ease-in` on responsive UI.

Use strong shared easing tokens:

```css
--ease-out: cubic-bezier(.23,1,.32,1);
--ease-in-out: cubic-bezier(.77,0,.175,1);
--ease-drawer: cubic-bezier(.32,.72,0,1);
```

## Phase 6 — Advanced component fit check

Before adding any high-craft showpiece component, read and apply `build-artful-websites/ADVANCED-COMPONENT-INTEGRATION.md`.

The **Works Wheel** and **Liquid Glass Carousel** prompts are permanent reference patterns for future builds. Consider them when they improve a portfolio, gallery, project index, spatial navigation, 3D/WebGL surface, or premium motion section. Never force them into every website.

Before integration:

1. inspect the actual framework, component conventions, TypeScript, Tailwind, shadcn structure, aliases, and styles path;
2. analyze required dependencies, props, state, refs, context, browser APIs, assets, and cleanup;
3. install only missing dependencies;
4. adapt to the project's own component structure rather than rewriting the entire app just to match a demo;
5. replace demo/CDN/stock imagery with real project assets whenever available;
6. preserve keyboard, touch, reduced-motion, fallback, and responsive behavior;
7. decide where the component belongs in the page narrative and why;
8. verify the interaction is worth its bundle, GPU, memory, and complexity cost.

A component must pass **brand fit, narrative fit, usability fit, and performance fit** before shipping.

## Phase 7 — Find motion opportunities

Now use the animation-opportunity rules.

Do not animate everything.

For every candidate ask:

1. How often will the user see it?
2. What is its purpose?
3. Can it stay fast enough?
4. Does movement help or hinder the task?

Motion is valid for:

- feedback
- spatial consistency
- state indication
- explanation
- bridging a jarring change
- rare delight

`It looks cool` is not sufficient.

## Phase 8 — Implement motion

Use the cheapest appropriate tool.

General timing:

- press: 100–160ms
- tooltip/popover: 125–200ms
- dropdown/select: 150–250ms
- modal/drawer: 200–500ms
- editorial/marketing reveal: longer only when infrequent and justified

Prefer transform and opacity.
Use transitions for rapidly retargeted UI.
Use springs only for gestures/interruptible physics where appropriate.
Gate hover motion for fine pointers.
Ship reduced-motion behavior with every movement-heavy feature.

When complex sequencing, ScrollTrigger scenes, plugin-driven effects, advanced transforms, timelines, or imperative choreography genuinely require GSAP, use the installed GreenSock skill pack. Do not use GSAP for basic hover/press/fade/color transitions that CSS handles better.

## Phase 9 — Review and delete

Run a final animation review with a deletion bias.

Remove motion that is:

- repetitive
- slow
- generic
- decorative without purpose
- physically disconnected from its trigger
- bad for performance
- distracting from readable content
- unnecessary on high-frequency actions

The final website should feel alive because the right things move, not because everything moves.

## Phase 10 — Responsive art direction

Test at minimum:

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
- intentional mobile hero line breaks
- no clipped type
- no fixed-element collisions
- correct touch targets
- mobile navigation designed for touch
- safe degradation of pointer-only effects
- re-art-directed image crops

## Phase 11 — Engineering quality

Protect:

- LCP
- CLS
- INP
- scroll performance
- accessibility
- security
- SEO
- functional reliability

Do not expose secrets.
Validate public inputs.
Preserve origin/authorization checks.
Use rate limits where appropriate.
Use semantic markup, visible focus, labels, alt text, reduced motion, meaningful metadata, canonical URLs, sitemap/robots where appropriate, and structured data only for known facts.

Do not invent testimonials, clients, reviews, awards, metrics, prices, capabilities, or business facts.

## Phase 12 — QA before deployment

Test:

- all routes
- navigation
- forms
- primary conversion journey
- integrations
- success/error states
- 404
- external links
- mobile
- keyboard navigation
- reduced-motion mode
- console/runtime errors
- production assets
- security headers where applicable
- advanced component fallbacks and teardown behavior where used

Deploy only when authorized.

## Final quality bar

The site is not finished until:

- the static composition looks premium without animation
- the design cannot be mistaken for an AI template
- the brand is recognizable without relying solely on its logo
- advanced components are used only where they improve the experience
- motion is purposeful
- interactions feel immediate
- mobile feels equally designed
- performance remains strong
- accessibility is intact
- claims are honest
- security is not weakened
- production journeys work

Final question:

**Would a strong designer call this authored, and would a strong engineer trust it in production?**

If either answer is no, continue refining before calling the website complete.