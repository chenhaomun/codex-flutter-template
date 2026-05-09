# Codex Project Template

Minimal Flutter-first Codex setup.

Keep this template minimal: `README.md` is for humans; the rest is for Codex.

Copy into a project root:

```sh
cp AGENTS.md /path/to/project/AGENTS.md
cp -R .codex /path/to/project/.codex
cp -R .agents /path/to/project/.agents
cp -R subagents /path/to/project/subagents
cp skills-lock.json /path/to/project/skills-lock.json
```

Use env files as `.env.dev.json`, `.env.prod.json`, and optional `.env.staging.json`.

Use subagents only when needed:

```text
Use subagents: business analyst, team lead, flutter developer, and QA.
```

Default replies use `$caveman lite`. Say `normal mode` to turn it off. Use `$caveman-compress <file>` for memory docs.
