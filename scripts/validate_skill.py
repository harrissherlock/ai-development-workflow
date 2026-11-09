#!/usr/bin/env python3
"""Check the reusable skill package's required files and local links."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = (
    "SKILL.md", "README.md", "LICENSE", "docs/guide.html",
    "references/development-process.md", "references/testing-and-ci.md",
    "references/vercel-previews.md", "references/agent-compatibility.md",
    "references/security.md", "templates/AGENTS.md",
    "templates/ISSUE_TEMPLATE.md", "templates/PULL_REQUEST_TEMPLATE.md",
    "templates/node-ci.yml",
)
errors = []
for entry in REQUIRED:
    if not (ROOT / entry).is_file():
        errors.append(f"Missing required file: {entry}")

for path in ROOT.rglob("*.md"):
    data = path.read_text(encoding="utf-8")
    for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", data):
        if not target or target.startswith(("http:", "https:", "#", "mailto:")):
            continue
        relative = target.split("#", 1)[0]
        if relative and not (path.parent / relative).exists():
            errors.append(f"Broken link: {path.relative_to(ROOT)} -> {target}")

skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
if not re.match(r"\A---\nname: ai-development-workflow\ndescription: .+\n---\n", skill):
    errors.append("SKILL.md requires valid name and description frontmatter")
if "<html" not in (ROOT / "docs/guide.html").read_text(encoding="utf-8").lower():
    errors.append("docs/guide.html does not contain an HTML document")
if errors:
    print("\n".join(errors), file=sys.stderr)
    raise SystemExit(1)
print(f"Skill package validated ({len(REQUIRED)} required files, Markdown links checked).")
