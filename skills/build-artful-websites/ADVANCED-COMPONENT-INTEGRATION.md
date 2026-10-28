# Advanced Component Integration Protocol

This protocol is part of Build Artful Websites and applies to every new website.

Its job is not to force the same showpiece component into every project. Its job is to ensure that when a premium interaction, gallery, portfolio index, carousel, spatial navigation pattern, 3D/WebGL surface, or motion-heavy section is appropriate, it is integrated with the same rigor as the rest of the site instead of being dropped in as a demo.

## Available reference patterns

Two high-craft component prompts were added as reference patterns:

1. **Works Wheel** — a portfolio/project index that begins as a ring and unfolds into a perspective drum controlled by wheel, drag, keyboard, and direct selection.
2. **Liquid Glass Carousel** — a GSAP + Three.js infinite carousel with WebGL lens/refraction behavior, pointer/drag interaction, focus mode, entry choreography, keyboard support, reduced-motion handling, WebGL fallback, and lifecycle cleanup.

These are references and reusable interaction patterns, not mandatory visual motifs.

## Permanent pre-integration checklist

Before integrating any advanced component:

1. Inspect the current stack and component conventions.
2. Confirm framework, TypeScript, Tailwind, shadcn/ui structure, aliases, utility helpers, styles path, and existing animation libraries.
3. If the supplied component assumes shadcn/Tailwind/TypeScript but the project does not use them, do **not** blindly convert the whole project. Choose between:
   - adapting the component to the existing stack, or
   - adding the missing foundation only when it is clearly the better project-level decision.
4. Determine the correct local component path. For shadcn projects, prefer `/components/ui` unless the repository has an established equivalent.
5. Analyze imports and install only missing dependencies.
6. Inspect props, state, refs, event listeners, context providers, hooks, browser APIs, WebGL requirements, and cleanup behavior.
7. Resolve what real data, images, links, labels, and actions the component receives.
8. Define responsive behavior before implementation, not after desktop is finished.
9. Decide where the component belongs in the information architecture and why it improves that section.
10. Verify keyboard, touch, reduced-motion, fallback, loading, error, and teardown behavior.

## Questions the implementation must answer internally

Do not ask the user all of these if the repository/brief already answers them. Resolve them from context whenever possible:

- What data/props drive the component?
- Is local state enough, or is shared state required?
- What project assets should replace demo imagery?
- Which interaction modes must work: wheel, touch drag, pointer, keyboard, buttons?
- What should happen on narrow/mobile layouts?
- What is the best placement for this component in the page narrative?
- Is this interaction worth its bundle, GPU, memory, and complexity cost?
- What is the static/reduced-motion/WebGL-unavailable fallback?

## Asset rule

Demo prompts may contain Unsplash, CDN, placeholder, or generated artwork so the demo runs immediately. Production builds must replace those with:

1. real client/project assets when available;
2. approved generated assets when explicitly part of the project;
3. clearly temporary placeholders only while prototyping.

Never let demo art become accidental brand art.

## Icon rule

Use the project's existing icon family. Do not switch the entire project to a library merely because a pasted component prompt names one. Avoid hand-rolled SVG paths when a maintained project icon already exists, but preserve bespoke SVG when it is genuinely part of the component's visual identity.

## GSAP integration

When the installed GreenSock skill pack is available, use the relevant skill(s) for motion-heavy implementations:

- `gsap-core`
- `gsap-frameworks`
- `gsap-performance`
- `gsap-plugins`
- `gsap-react`
- `gsap-scrolltrigger`
- `gsap-timeline`
- `gsap-utils`

Build Artful Websites remains the orchestrator. Emil-style motion judgment decides **whether** an effect should exist and how it should feel. GSAP skills decide **how to implement** complex choreography correctly when GSAP is the right tool.

Use GSAP when it materially improves timeline coordination, ScrollTrigger scenes, sequencing, complex transforms, FLIP-like choreography, plugin-driven effects, or imperative high-performance animation. Do not use GSAP for a simple hover, opacity fade, or press state that CSS handles better.

## Works Wheel integration rules

When the Works Wheel pattern fits the project:

- preserve the core ring-to-drum spatial concept rather than flattening it into a generic carousel;
- keep wheel scrolling cancellable only while the component can still advance so page scroll is not trapped at boundaries;
- preserve drag/pointer capture behavior;
- preserve keyboard navigation and active descendant semantics;
- keep animation work out of React render loops where possible;
- use actual project titles, links, and artwork;
- provide a simpler mobile/reduced-motion variant when the full perspective treatment becomes unusable;
- test perspective, culling, z-index, card scaling, and title/index readability across viewport sizes.

## Liquid Glass Carousel integration rules

When the Liquid Glass Carousel pattern fits the project:

- treat GSAP and Three.js as real dependencies with bundle/performance cost;
- preserve WebGL failure handling and a useful fallback;
- cap device pixel ratio and GPU work appropriately;
- stop rendering when offscreen or when the document is hidden;
- dispose renderer, render targets, geometry, materials, textures, observers, listeners, timelines, and tweens during teardown;
- preserve pointer, wheel, touch, keyboard, and focus behavior;
- honor reduced motion by removing or simplifying entry choreography and movement-heavy effects;
- replace demo imagery with real project assets;
- validate color-space, image loading, cross-origin behavior, texture memory, and fallback behavior;
- keep the lens/glass effect subordinate to project art direction rather than letting the demo's blue-ring look become the site identity by accident.

## Integration sequence

For every advanced component:

1. **Analyze** — structure, dependencies, props, state, assets, APIs, and cost.
2. **Adapt** — fit the project's component conventions, design tokens, icon family, type system, and responsive strategy.
3. **Install** — add only missing dependencies.
4. **Integrate** — place in the page narrative with real project data/assets.
5. **Art-direct** — restyle from demo appearance into the project's own visual language.
6. **Motion-review** — apply Build Artful Websites + Emil judgment; delete unjustified motion.
7. **GSAP-review** — if GSAP is used, apply the installed GSAP skill(s) for framework setup, timelines/plugins/ScrollTrigger, and performance.
8. **Accessibility** — keyboard, focus, reduced motion, semantic labeling, fallbacks.
9. **Performance** — measure bundle, rendering cost, scroll smoothness, memory, mobile behavior, and lifecycle cleanup.
10. **Responsive QA** — test the component as a composition at target widths, not only whether it technically fits.
11. **Production QA** — verify real assets, links, errors, fallbacks, cleanup, and console/runtime behavior.

## Mandatory anti-demo rule

Never ship an advanced component because it looked impressive in its demo.

It must pass all four checks:

- **Brand fit** — does this interaction belong to this brand?
- **Narrative fit** — does it improve this point in the page?
- **Usability fit** — does it remain understandable and operable across input methods?
- **Performance fit** — is the visual payoff worth the runtime cost?

If not, adapt it heavily or do not use it.
