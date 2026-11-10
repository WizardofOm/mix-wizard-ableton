# Mix Wizard for Ableton

Mixing and mastering skills for Ableton Live, from the Wizard of Om.

These are Claude Skills: short instruction files that teach an AI assistant how to mix like an engineer instead of guessing. Each one covers a single job, with real numbers and a clear order of steps.

## The skills

| Skill | What it does |
| --- | --- |
| [`perception-first-engineer`](skills/perception-first-engineer/SKILL.md) | Engineer mode: blunt diagnosis of the perceptual problem, then an exact stock-device chain |
| [`clean-eq`](skills/clean-eq/SKILL.md) | Gentle 250 Hz dip across the session, and broad curves instead of narrow ones |
| [`level-first-mix`](skills/level-first-mix/SKILL.md) | Static balance from RMS meters before any processing |
| [`depth-with-limiters`](skills/depth-with-limiters/SKILL.md) | Light limiting on tracks and buses to place sounds front to back |
| [`low-end-handoff`](skills/low-end-handoff/SKILL.md) | Staggered gentle high-pass filters so guitars, drums, and bass share the low end |
| [`vocal-guitar-pocket`](skills/vocal-guitar-pocket/SKILL.md) | Complementary EQ so vocals stay clear against guitars and keys |
| [`compression-math`](skills/compression-math/SKILL.md) | Ratio, threshold, and makeup gain in plain arithmetic |
| [`parallel-bus`](skills/parallel-bus/SKILL.md) | One heavily compressed return blended under the mix for glue and density |
| [`reference-check`](skills/reference-check/SKILL.md) | Comparing a bounce to commercial tracks outside the session at matched loudness |
| [`master-polish`](skills/master-polish/SKILL.md) | Master-bus exciter and a light mastering chain built around a loud chorus |
| [`vocal-tracking`](skills/vocal-tracking/SKILL.md) | Mic choice, mic position as EQ, and performance level for home recording |
| [`mix-master-reference`](skills/mix-master-reference/SKILL.md) | Quick reference: gain staging, typical settings, chain order, loudness targets, common mistakes |
| [`dance-arrangement-architect`](skills/dance-arrangement-architect/SKILL.md) | Arrangement mode for dance music: energy flow and layout in 8, 16, and 32 bar blocks |

## Suggested order

1. `vocal-tracking` while recording
2. `level-first-mix` to set the balance
3. `clean-eq`, `low-end-handoff`, `vocal-guitar-pocket` to shape tone
4. `compression-math`, `depth-with-limiters`, and `parallel-bus` for control, depth, and glue
5. `reference-check` against records you trust
6. `master-polish` to finish

## Works with

The skills use the open Agent Skills format (`SKILL.md`), so the same files work in Claude, OpenAI Codex, Cursor, Gemini CLI, and other tools that read it. Nothing needs converting.

## Install

Get the files once:

```bash
git clone https://github.com/WizardofOm/mix-wizard-ableton
```

Then copy the skill folders to where your tool looks for them:

| Tool | Command |
| --- | --- |
| Claude Code | `mkdir -p ~/.claude/skills && cp -r mix-wizard-ableton/skills/* ~/.claude/skills/` |
| OpenAI Codex | `mkdir -p ~/.agents/skills && cp -r mix-wizard-ableton/skills/* ~/.agents/skills/` |
| Cursor | `mkdir -p ~/.cursor/skills && cp -r mix-wizard-ableton/skills/* ~/.cursor/skills/` |
| Gemini CLI | `mkdir -p ~/.gemini/skills && cp -r mix-wizard-ableton/skills/* ~/.gemini/skills/` |

Restart the tool afterward so it picks up the new skills.

Other options:

- **One-line installer:** `npx skills add WizardofOm/mix-wizard-ableton` detects your installed tools and places the skills for you.
- **Claude app:** open a skill's `SKILL.md`, copy it, and ask Claude to save it as a skill.
- **ChatGPT or any chat assistant:** paste a skill's `SKILL.md` into the conversation, or into a custom GPT's or project's instructions, and ask your question.
- **Tools without skill support:** open this folder as your project. [`AGENTS.md`](AGENTS.md) indexes every skill and tells the assistant when to read each one.

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
