# Release checklist

Use real versioned releases to communicate concrete changes, not to fabricate activity.

1. Validate package locally: `python3 scripts/validate_skill.py`.
2. Review new/updated guidance, example links, frontmatter, permissions, and security implications.
3. Test install on an independent local project with current Skills CLI:
   `npx skills add KaranRana21/build-artful-websites --skill build-artful-websites`.
4. Ask agent to read SKILL.md and advanced protocol, and test a bounded sample task.
5. Review `CHANGELOG.md` against merged commit history. Avoid claiming untested compatibility.
6. Commit release notes, then create annotated Git tag on verified main commit:
   `git tag -a v1.0.0 -m "Build Artful Websites v1.0.0"`
   `git push origin v1.0.0`
7. Publish GitHub Release from tag with changes, compatibility limitations, and links.
8. Monitor real install reports, issues, and PRs; record factual impact only.

No GitHub release exists merely because this document or CHANGELOG mentions a version.
