#!/usr/bin/env python3
"""Build MIX-WIZARD.md, the single-file guide, from skills/*/SKILL.md.

Run from the repository root:  python3 tools/compile.py
"""
import os
import re

ORDER = [
    "perception-first-engineer",
    "level-first-mix",
    "clean-eq",
    "low-end-handoff",
    "vocal-guitar-pocket",
    "compression-math",
    "depth-with-limiters",
    "parallel-bus",
    "reference-check",
    "master-polish",
    "vocal-tracking",
    "mix-master-reference",
    "dance-arrangement-architect",
]


def main():
    names = ORDER + sorted(n for n in os.listdir("skills") if n not in ORDER)
    out = [
        "# Mix Wizard: the complete guide\n",
        "Every Mix Wizard skill in one file, for reading straight through or "
        "pasting into any AI assistant. Generated from the files in `skills/` "
        "by `tools/compile.py`; edit those, not this.\n",
        "## Contents\n",
    ]
    bodies = []
    for i, name in enumerate(names, 1):
        text = open(f"skills/{name}/SKILL.md", encoding="utf-8").read()
        match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
        front, body = match.group(1), match.group(2).strip()
        desc = re.search(r"^description:\s*(.*)$", front, re.M).group(1)
        title = re.search(r"^# (.*)$", body, re.M).group(1)
        body = re.sub(r"^# .*\n", "", body, count=1).strip()
        body = re.sub(r"^(#{2,5}) ", lambda m: "#" + m.group(1) + " ", body, flags=re.M)
        anchor = re.sub(r"[^a-z0-9 -]", "", f"{i}. {title}".lower()).replace(" ", "-")
        out.append(f"{i}. [{title}](#{anchor})")
        bodies.append(f"\n---\n\n## {i}. {title}\n\n*When to use: {desc}*\n\n{body}\n")
    with open("MIX-WIZARD.md", "w", encoding="utf-8") as handle:
        handle.write("\n".join(out) + "\n" + "".join(bodies))


if __name__ == "__main__":
    main()
