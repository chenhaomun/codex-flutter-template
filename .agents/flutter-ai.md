# Flutter AI Tooling

This template includes project-local skills for repeatable Flutter and Dart workflows. Agents should use them only when the task clearly matches the skill and should still inspect local code first.

## Installed Skills

Flutter skills:

- `flutter-add-integration-test`
- `flutter-add-widget-preview`
- `flutter-add-widget-test`
- `flutter-apply-architecture-best-practices`
- `flutter-build-responsive-layout`
- `flutter-fix-layout-issues`
- `flutter-implement-json-serialization`
- `flutter-setup-declarative-routing`
- `flutter-setup-localization`
- `flutter-use-http-package`

Dart skills:

- `dart-add-unit-test`
- `dart-build-cli-app`
- `dart-collect-coverage`
- `dart-fix-runtime-errors`
- `dart-generate-test-mocks`
- `dart-migrate-to-checks-package`
- `dart-resolve-package-conflicts`
- `dart-run-static-analysis`
- `dart-use-pattern-matching`

## Skill Rules

- Read the relevant `.agents/skills/<skill>/SKILL.md` before using a skill.
- Prefer repo conventions over generic examples from a skill.
- Do not add dependencies, change package choices, or migrate architecture without explicit user approval.
- Keep skill-driven changes scoped and verify with the narrowest useful Flutter/Dart command.

## Dart and Flutter MCP

Recommended local MCP setup for Codex:

```powershell
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

```powershell
npx.cmd @colbymchenry/codegraph
codegraph init -i
```

Use CodeGraph MCP when `.codegraph/` exists and the tools are available. Keep `.agents/project-map.md` as the lightweight human area map, and do not commit `.codegraph/`.
