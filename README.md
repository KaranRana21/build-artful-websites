# Build Artful Websites

**Open-source design-engineering skill for websites that feel authored—not AI-templated.**

Most AI website prompts ask for polish. Build Artful Websites specifies **how to make design decisions and verify them**: brand-specific creative direction, strong static composition, purposeful interaction/motion, mobile art direction, accessibility, performance, security, SEO, and production QA.

This is an [Agent Skill](https://agentskills.io/), not a site theme, component library, or guarantee of a particular design award. Works standalone; optional specialized design and GSAP skills can extend it.

## Install

Requires Node.js/npm for the installer. Use an agent supported by the [Skills CLI](https://skills.sh/).

```bash
npx skills add KaranRana21/build-artful-websites
```

To select this skill explicitly:

```bash
npx skills add KaranRana21/build-artful-websites --skill build-artful-websites
```

Follow CLI prompts to choose project/global scope and agent. No OpenAI key required to **install** this instruction-only skill.

**Compatibility note:** Installation is via external Skills CLI; instructions are agent-agnostic. Exact installation behavior depends on CLI version and available agent adapters. Other named companion skills are **not** bundled.

## Use

Start any new website or redesign with:

> Use the `build-artful-websites` skill. Inspect existing repository, real brand assets, audience, and business goals. Define a creative thesis and write `DESIGN.md`. Make the static composition exceptional before adding motion. Reject generic landing-page patterns. Implement useful interaction states, accessibility, honest content, responsive art direction, and production QA.

Want a complete fill-in brief? Copy [NEW-WEBSITE-PROMPT.md](NEW-WEBSITE-PROMPT.md).

## What changes in practice?

| Generic AI website | Artful website |
| --- | --- |
| Identical centered hero + gradient + feature cards | Layout emerges from brand, content, and audience |
| Animation on every scroll event | Motion earns its place through frequency and purpose |
| Desktop design shrunk for mobile | Mobile composition and image crops art-directed separately |
| Placeholder reviews and invented metrics | Verifiable copy and genuine proof only |
| Production as afterthought | Performance, accessibility, security, SEO, and functional QA |

## Workflow

1. **Recon:** read brief, codebase, real assets, integrations, constraints, references.
2. **Creative thesis:** audience, primary action, design dials, brand tension, anti-goals.
3. **Design doctrine:** write `DESIGN.md` for project-specific decisions.
4. **Static design:** content hierarchy, rhythm, typography, material, intentional mobile layout.
5. **Anti-template review:** delete generic composition and unearned decoration.
6. **Interaction:** hover, active, focus, keyboard, touch, selected, error/loading.
7. **Motion gate:** animate only when it improves feedback, spatial continuity, explanation, or rare delight.
8. **Production check:** accessibility, reduced motion, Core Web Vitals, security, SEO, real conversion journeys.
9. **Verify:** tests, live behavior if deployed, cleanup, and content honesty.

Read full rules in [SKILL.md](skills/build-artful-websites/SKILL.md).

## Included

```text
skills/build-artful-websites/
  SKILL.md
  ADVANCED-COMPONENT-INTEGRATION.md
NEW-WEBSITE-PROMPT.md
LICENSE
README.md
```

[Advanced Component Integration](skills/build-artful-websites/ADVANCED-COMPONENT-INTEGRATION.md) covers when to adapt spatial galleries, GSAP timelines, Three.js/WebGL effects, and complex UI components—and how to provide keyboard, touch, reduced-motion, performance, and failure fallbacks.

## Example briefs

- **[Local business](examples/local-business.md):** build with real menu, reservation links, contact info, and review integrity.
- **[Creative portfolio](examples/creative-portfolio.md):** distinctive spatial navigation, credible case studies, restrained motion.
- **[Product site](examples/product-site.md):** conversion-led clarity, accessible interactions, fast product journeys.

Examples are prompts and quality criteria, **not deployed client work or fabricated adoption evidence**.

## Optional companion skills

When present, skill coordinates `design-taste-frontend`, `emil-design-eng`, `find-animation-opportunities`, `animate`, `improve-animations`, `review-animations`, and applicable `gsap-*` skills. They are separate projects/tools; installation is optional and not implied.

## Maintain and contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for changes, validation, and PR expectations. Report vulnerabilities via [SECURITY.md](SECURITY.md). Review releases/changelog for evolution.

Current project is early-stage. We do **not** claim usage numbers, stars, endorsements, award wins, client deployments, or official OpenAI affiliation.

**Quality gate:** *Would a strong designer call this authored, and a strong engineer trust it in production?*

Maintainer: [KaranRana21](https://github.com/KaranRana21) · License: [MIT](LICENSE)
