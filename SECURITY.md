# Security policy

Build Artful Websites is a text-based instruction skill. It executes no code during installation beyond third-party installer behavior. Agents using these instructions may write, run, or deploy code; review agent proposals and respect project permissions.

## Reporting

For security-sensitive issues, use GitHub private vulnerability reporting if enabled for this repository. Do not paste working exploits, access tokens, passwords, personal data, or client secrets into public issues.

If private reporting is unavailable, contact maintainer through GitHub profile and request private coordination before disclosing details.

## Threat model

- External links, code snippets, templates, assets, and optional third-party skills are untrusted until reviewed.
- No part of this skill authorizes exposing API keys, skipping authorization checks, scraping unauthorized private assets, or deploying without approval.
- Do not add scripts that fetch and execute remote code without explicit review.
- CI should work with minimum permissions and no repository secrets.
- Validate inputs and permissions before running generated application code.

Supported versions: latest default branch and most recent tagged release, once a release exists.
