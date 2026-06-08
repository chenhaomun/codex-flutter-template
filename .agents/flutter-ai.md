# Flutter AI Tooling

This template includes project-local skills for repeatable Flutter and Dart workflows. Agents should use them only when the task clearly matches the skill and should still inspect local code first.

## Skill Rules

- Installed skills live under `.agents/skills/`.
- Read the relevant `.agents/skills/<skill>/SKILL.md` before using a skill.
- Prefer repo conventions over generic examples from a skill.
- Do not add dependencies, change package choices, or migrate architecture without explicit user approval.
- Keep skill-driven changes scoped and verify with the narrowest useful Flutter/Dart command.

## Dart and Flutter MCP

Recommended local MCP setup for Codex:

```sh
codex mcp add dart -- dart mcp-server --force-roots-fallback
```

Use the Dart/Flutter MCP server when available for:

- analyzer diagnostics and quick fixes
- symbol lookup and code navigation
- formatting
- running tests
- `pubspec.yaml` dependency operations
- pub.dev package lookup
- running-app or widget tree inspection

MCP setup is per developer machine. Keep this repository limited to instructions and project-local skills.

## Optional CodeGraph

CodeGraph can complement `.agents/project-map.md` with a local semantic index for larger codebases. It is useful for symbol search, callers/callees, impact analysis, and architecture discovery.

Recommended setup:

macOS/Linux:

```sh
npx @colbymchenry/codegraph
codegraph init -i
```

Windows PowerShell:

```powershell
npx.cmd @colbymchenry/codegraph
codegraph init -i
```

Use CodeGraph MCP when `.codegraph/` exists and tools are available for refactor, rename/move, architecture review, unclear bug, API/model contract change, cross-module feature, dead code, or risky cleanup. If missing and task is large/risky, ask before generating it. Otherwise use `rg`. Keep `.agents/project-map.md` as the lightweight Codex-maintained area map, and do not commit `.codegraph/`.
