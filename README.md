# Mix Wizard for Ableton

Mixing and mastering skills for Ableton Live, from the Wizard of Om.

These are Claude Skills: short instruction files that teach an AI assistant how to mix like an engineer instead of guessing. Each one covers a single job, with real numbers and a clear order of steps.

## The skills

| Skill | What it does |
| --- | --- |
| [`clean-eq`](skills/clean-eq/SKILL.md) | Gentle 250 Hz dip across the session, and broad curves instead of narrow ones |
| [`level-first-mix`](skills/level-first-mix/SKILL.md) | Static balance from RMS meters before any processing |
| [`depth-with-limiters`](skills/depth-with-limiters/SKILL.md) | Light limiting on tracks and buses to place sounds front to back |
| [`low-end-handoff`](skills/low-end-handoff/SKILL.md) | Staggered gentle high-pass filters so guitars, drums, and bass share the low end |
| [`vocal-guitar-pocket`](skills/vocal-guitar-pocket/SKILL.md) | Complementary EQ so vocals stay clear against guitars and keys |
| [`compression-math`](skills/compression-math/SKILL.md) | Ratio, threshold, and makeup gain in plain arithmetic |
| [`master-polish`](skills/master-polish/SKILL.md) | Master-bus exciter and a light mastering chain built around a loud chorus |
| [`vocal-tracking`](skills/vocal-tracking/SKILL.md) | Mic choice, mic position as EQ, and performance level for home recording |

## Suggested order

1. `vocal-tracking` while recording
2. `level-first-mix` to set the balance
3. `clean-eq`, `low-end-handoff`, `vocal-guitar-pocket` to shape tone
4. `compression-math` and `depth-with-limiters` for control and depth
5. `master-polish` to finish

## Install

Claude Code:

```bash
git clone https://github.com/WizardofOm/mix-wizard-ableton ~/.claude/skills/mix-wizard
```

Claude app: open a skill's `SKILL.md`, copy it, and ask Claude to save it as a skill.

## Using them

Ask in plain language:

- "My mix sounds muddy. Clean it up."
- "Help me balance this session before I add any plugins."
- "The vocal is getting lost behind the guitars."
- "Get this track ready for release."

The skills work as advice on their own. To let the assistant operate Live directly (add devices, set parameters), connect an Ableton MCP server such as [`uisato/ableton-mcp-extended`](https://github.com/uisato/ableton-mcp-extended).

Every skill uses stock Ableton devices first. All frequencies and amounts are starting points. Trust your ears last.

## About

Made by [Wizard of Om](https://www.instagram.com/b_parker_333/) (B Parker): producer, multi-instrumentalist, DJ and VJ.

The techniques here are widely used engineering practice, collected and written up in original wording for Ableton Live.

## License

[MIT](LICENSE)
