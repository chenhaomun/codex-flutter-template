# Guidance Token Report

Word count is an approximate token-cost proxy, not exact tokenizer output.

## Current Hotspots

| Area | Approx size | Token risk | Note |
|---|---:|---|---|
| `AGENTS.md` before split | 1,346 words | High | Subagents section was the largest block. |
| `subagents/*.md` total | 658 words | Medium | Prompt files are small; QA, TL, Flutter are biggest. |
| `.agents/skills/*/SKILL.md` total | 337 words before new workflow | Low | Skills load only when triggered. |

## Action Taken

| Change | Outcome |
|---|---|
| Moved detailed subagent workflow into `.agents/skills/subagent-workflow` | Keeps `AGENTS.md` smaller during normal work. |
| Kept role prompts concise | Avoids duplicating full workflow in every subagent file. |
| Added compact timing rules | Reduces late-context degradation during long tasks. |

## Watch Next

| Section | Recommendation |
|---|---|
| `AGENTS.md` Flutter Rules | Keep for now; split only if it grows further. |
| `subagent-workflow` skill | Review after real subagent runs; shrink if reports still feel verbose. |
| `subagents/qa.md` | Keep manual QA rules concise; avoid test boilerplate. |
