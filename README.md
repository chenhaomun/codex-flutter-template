# Codex Project Template

Minimal Flutter-first Codex setup.

Keep this template minimal: `README.md` is for humans; the rest is for Codex.

Copy into a project root.

macOS/Linux:

```sh
cp AGENTS.md /path/to/project/AGENTS.md
cp -R .agents /path/to/project/.agents
cp skills-lock.json /path/to/project/skills-lock.json
```

Windows PowerShell:

```powershell
Copy-Item AGENTS.md C:\path\to\project\AGENTS.md
Copy-Item .agents C:\path\to\project\.agents -Recurse
Copy-Item skills-lock.json C:\path\to\project\skills-lock.json
```

Use subagents for larger work:

```text
Use subagents: business analyst, team lead, flutter developer, and QA.

Task:
Add a loading and empty state to the profile screen.

Requirements:
- Show a spinner while profile data loads.
- Show a clear empty state when no profile data exists.
- Keep the existing theme, routing, and state management.

Verify:
- flutter analyze
- flutter test
```

For messy requirements, ask Codex to format them first:

```text
/subagent-task
I need profile to feel better. It should not look broken when data is loading,
and if no profile exists it should tell the user what to do next.
```

Skip subagents for small edits like typos, formatting, copy changes, or one-file fixes. They add coordination cost and can be slower than a direct change.

Subagent runs write reports under `reports/subagents/<task-slug>/`.

Codex will generate `.agents/project-map.md` when it first works in the copied project.

Refresh vendored Flutter/Dart skills using `.agents/skill-maintenance.md`.

For current OpenAI/Codex docs, Codex can install the docs MCP on demand when needed. It will ask permission before running:

```sh
codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp
```

Restart Codex if the MCP tools do not appear after install. This is local Codex config, not copied by the template.

Optional shared Codex device setup lives in `.codex/`. Preview with:

```sh
python .codex/install.py --dry-run
```

Default replies use `$caveman lite`. Say `normal mode` to turn it off. Use `$caveman-compress <file>` for memory docs.
