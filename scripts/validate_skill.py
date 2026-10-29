#!/usr/bin/env python3
"""Validate Build Artful Websites skill package without external dependencies."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "build-artful-websites"
SKILL_FILE = SKILL_DIR / "SKILL.md"
REQUIRED = [
    SKILL_FILE,
    SKILL_DIR / "ADVANCED-COMPONENT-INTEGRATION.md",
    ROOT / "NEW-WEBSITE-PROMPT.md",
    ROOT / "README.md",
    ROOT / "LICENSE",
    ROOT / "SECURITY.md",
    ROOT / "CONTRIBUTING.md",
]

LINK_RE = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")


def check_frontmatter(text: str) -> list[str]:
    issues: list[str] = []
    if not text.startswith("---\n"):
        return ["SKILL.md missing YAML frontmatter"]
    end = text.find("\n---\n", 4)
    if end == -1:
        return ["SKILL.md missing closing YAML frontmatter delimiter"]
    header = text[4:end]
    metadata: dict[str, str] = {}
    for line in header.splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            key, value = line.split(":", 1)
            metadata[key.strip()] = value.strip().strip('"').strip("'")
    if metadata.get("name") != "build-artful-websites":
        issues.append("SKILL.md name must be build-artful-websites")
    if not metadata.get("description") or len(metadata["description"]) < 30:
        issues.append("SKILL.md description missing or too short")
    if len(header) > 1300:
        issues.append("SKILL.md frontmatter too long for concise discovery")
    return issues


def check_markdown_links(path: Path) -> list[str]:
    issues: list[str] = []
    content = path.read_text(encoding="utf-8")
    for raw in LINK_RE.findall(content):
        link = raw.strip().split(" ", 1)[0].strip("<>")
        if not link or link.startswith(("https://", "http://", "mailto:", "#", "data:")):
            continue
        link = link.split("#", 1)[0].split("?", 1)[0]
        if not link:
            continue
        if link.startswith("/"):
            issues.append(f"{path.relative_to(ROOT)}: absolute local link {raw}")
            continue
        target = (path.parent / link).resolve()
        if not target.is_relative_to(ROOT.resolve()) or not target.exists():
            issues.append(f"{path.relative_to(ROOT)}: broken local link {raw}")
    return issues


def validate() -> list[str]:
    issues: list[str] = []
    for path in REQUIRED:
        if not path.is_file():
            issues.append(f"Missing: {path.relative_to(ROOT)}")
    if issues:
        return issues
    skill = SKILL_FILE.read_text(encoding="utf-8")
    issues += check_frontmatter(skill)
    if len(skill.splitlines()) > 500:
        issues.append("SKILL.md exceeds recommended 500-line limit; move references out")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        issues += check_markdown_links(path)
    return issues


if __name__ == "__main__":
    failures = validate()
    if failures:
        print("Skill package validation FAILED:")
        for failure in failures:
            print(f" - {failure}")
        sys.exit(1)
    print("Skill package validation PASSED: required files, frontmatter, local links.")
