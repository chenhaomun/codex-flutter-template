# Guidance Token Report

Live report. Approximate with words/chars.

## Baseline

| Area | Approx size | Token risk | Note |
|---|---:|---|---|
| `AGENTS.md` before workflow split | 1,346 words | High | Subagents section was largest. |
| `AGENTS.md` after workflow split | 807 words | Medium | Detailed subagent rules moved to skill. |
| `.agents/subagents/*.md` before cleanup | 658 words | Medium | QA, TL, Flutter prompts were biggest. |

## Live Run Log

| Task | Source | Approx size | Risk | Action |
|---|---|---:|---|---|
| baseline | guidance files | see baseline | Medium | Track during real subagent runs. |
| harness-tools | guidance+reports | 2869 words / 20692 chars | Medium | Review if growing. |

## Track

| Source | What to count | Reduce by |
|---|---|---|
| Visible updates | UI progress/thinking text | Use `$caveman full`; skip nonessential narration. |
| Command output | Terminal output returned to context | Cap unknown/large output at 4,000 chars. |
| Subagent prompts | Handoff text sent to subagents | Pass only task, ownership, relevant folders, constraints. |
| Subagent reports | Report markdown | Keep table format under 80 lines. |
| Timeline | `timeline.md` entries | Keep one-line event entries. |
| Final response | User-facing summary | Link reports; avoid repeating report contents. |

## Harness Tools

| Tool | Purpose |
|---|---|
| `.agents/tools/detect_project.py` | Detect repo type with short JSON output. |
| `.agents/tools/check_project_map.py` | Check mapped folders still exist. |
| `.agents/tools/count_tokens.py` | Count guidance/report words and optionally append a live log row. |

## Update

After each subagent run, command output over 2,000 chars, before compaction, and final handoff.

## Notes

- Visible status text consumes context.
- Hidden model reasoning is not repo-controllable.
- Reports carry decisions/outcomes; live thinking stays minimal.
