# Contributing

Thanks for improving Build Artful Websites. This is an instruction-based, agent-agnostic skill. Changes should make real design and engineering decisions clearer—not add fashionable effects.

## Before opening a pull request

1. Read `skills/build-artful-websites/SKILL.md` and related protocol.
2. Open an issue for major changes to workflow or scope, or explain rationale directly in PR.
3. Keep changes vendor-neutral and executable by real agents. Do not add fictional benchmarks, references, installations, reviews, awards, or adoption.
4. Add or revise an example when introducing a new pattern.
5. Run the local validator: `python3 scripts/validate_skill.py`.
6. Explain *why* change improves design quality, reliability, or accessibility and what tradeoffs it introduces.

## Pull request checklist

- [ ] Design intent and affected workflow documented
- [ ] No generic template bias introduced
- [ ] Honest claims, lawful assets, accurate references
- [ ] Accessibility, mobile, performance, security considered
- [ ] Skill frontmatter and local references validate
- [ ] Example/prompt refreshed where behavior changes
- [ ] No private client materials, secrets, credentials, or unpublished project code

Small editorial corrections welcome. For changes to shared reference patterns, cite concrete scenarios and include fallback/cleanup guidance.

## Issue guidance

Report unclear instructions, broken links, failed installation, agent-specific interpretation issues, and missing accessibility/performance rules. Supply minimal reproducer and the agent/version used when possible.

## Development

No package manager required to change the skill. Skill metadata follows the Agent Skills `SKILL.md` convention, with `name` and `description` YAML frontmatter. Validator uses Python standard library only.

## Code of conduct

Be constructive. Review ideas on evidence and usability; avoid personal attacks and share private vulnerability reports privately through repository security contacts.

## License

By contributing, you agree contributions are distributed under repository MIT license.
