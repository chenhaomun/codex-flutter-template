# Codex Project Template

Minimal Flutter-first Codex setup.

Keep this template minimal: `README.md` is for humans; the rest is for Codex.

Copy into a project root:

```sh
cp AGENTS.md /path/to/project/AGENTS.md
cp -R .agents /path/to/project/.agents
cp -R subagents /path/to/project/subagents
cp skills-lock.json /path/to/project/skills-lock.json
```

Use subagents for larger work:

```text
Use subagents: business analyst, team lead, flutter developer, and QA.

Task:
<what to build or fix>

Requirements:
- <requirement 1>
- <requirement 2>
- <requirement 3>

Verify:
- <command or expected check>
```

Skip subagents for small edits like typos, formatting, copy changes, or one-file fixes. They add coordination cost and can be slower than a direct change.

Subagent runs write reports under `reports/subagents/<task-slug>/`.

Ask Codex to generate `.agents/project-map.md` after copying so project terms map to the right paths.

Default replies use `$caveman lite`. Say `normal mode` to turn it off. Use `$caveman-compress <file>` for memory docs.
