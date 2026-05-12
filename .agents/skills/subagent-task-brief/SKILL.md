---
name: subagent-task-brief
description: >
  Turn raw or messy requirements into a subagent-ready task brief. Use when the user invokes
  /subagent-task, /taskbrief, asks to split requirements into Task/Requirements/Verify, or
  wants help preparing work for subagents.
---

Create a concise subagent task brief from raw requirements.

Rules:
- Keep business requirements separate from technical direction.
- Make `Task` one clear outcome.
- Make `Requirements` business/product-focused bullets.
- Make `Verify` include useful commands and manual checks.
- Add `Suggested subagents` based on AGENTS.md routing.
- Add `Ambiguities` only when a decision is blocked.
- Do not invent technical implementation details.
- Use `$caveman lite`.

Output:

```text
Use subagents: <roles>.

Task:
<one clear outcome>

Requirements:
- <business/product requirement>
- <business/product requirement>

Verify:
- <command or manual check>
- <command or manual check>

Ambiguities:
- <question or assumption, or None>
```
