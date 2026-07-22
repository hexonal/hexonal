#!/usr/bin/env python3
"""Regenerate the merged/open PR lists in README.md from live GitHub data.

Only touches the text between the MERGED/OPEN marker comments - everything
else in README.md is left untouched.
"""
import json
import re
import subprocess
import sys

USERNAME = "hexonal"

# Repos/owners we don't want showing up in the "look at my OSS work" list -
# our own repos, and anything that isn't a real external-project fix.
EXCLUDE_OWNERS = {"hexonal", "algorithm004-05"}


def gh_search_prs(limit=100):
    out = subprocess.run(
        [
            "gh", "search", "prs",
            f"--author={USERNAME}",
            f"--limit={limit}",
            "--json", "repository,number,title,url,state,updatedAt",
        ],
        capture_output=True, text=True, check=True,
    )
    return json.loads(out.stdout)


def relevant(pr):
    owner = pr["repository"]["nameWithOwner"].split("/")[0]
    return owner not in EXCLUDE_OWNERS


def format_block(prs, prefix, count):
    prs = sorted(prs, key=lambda p: p["updatedAt"], reverse=True)[:count]
    if not prs:
        return "(none right now)"
    labels = [f"{p['repository']['nameWithOwner']}#{p['number']}" for p in prs]
    width = max(len(label) for label in labels)
    lines = []
    for label, pr in zip(labels, prs):
        lines.append(f"{prefix} {label.ljust(width)}  {pr['title']}")
    return "\n".join(lines)


def replace_block(text, marker, block):
    pattern = re.compile(
        rf"(<!-- {marker}:START -->\n```diff\n).*?(\n```\n<!-- {marker}:END -->)",
        re.DOTALL,
    )
    if not pattern.search(text):
        print(f"warning: markers for {marker} not found, skipping", file=sys.stderr)
        return text
    return pattern.sub(lambda m: m.group(1) + block + m.group(2), text)


def main():
    prs = [p for p in gh_search_prs() if relevant(p)]
    merged = [p for p in prs if p["state"] == "merged"]
    open_prs = [p for p in prs if p["state"] == "open"]

    merged_block = format_block(merged, "+", 3)
    open_block = format_block(open_prs, "?", 4)

    with open("README.md", encoding="utf-8") as f:
        readme = f.read()

    readme = replace_block(readme, "MERGED", merged_block)
    readme = replace_block(readme, "OPEN", open_block)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme)


if __name__ == "__main__":
    main()
