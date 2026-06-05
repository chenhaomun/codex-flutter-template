# AGENTS.md

Flutter-first Codex rules.

## Repo Layout

- `.agents/`: map, skills, subagents, tools.
- `reports/subagents/`: generated reports. Inspect app root before work.

## Commands

- Prefer project scripts. Common: `flutter analyze`, `flutter test`, `flutter run --dart-define-from-file=.env.dev.json`, `flutter build <target> --dart-define-from-file=.env.prod.json`.
- Cap potentially large command output at 4,000 chars.

## Work Rules

- Read nearby code and follow existing architecture, naming, formatting, state, routing, theme, localization, API, generator, platform, and test patterns.
- Check `.agents/project-map.md` before broad searches; if missing/empty/stale, preview with `python3 .agents/tools/generate_project_map.py`, then update via `apply_patch`.
- Use only relevant `.agents/skills/<skill>/SKILL.md`; project conventions override generic examples.
- Prefer Dart/Flutter MCP for analyzer, symbols, fixes, format, tests, pub.dev, dependencies, and running-app/widget inspection.
- Use CodeGraph MCP when `.codegraph/` exists for semantic search and impact.
- Keep changes scoped. Preserve user changes; never reset unrelated work or edit generated files.
- Ask before packages/plugins/tools/global dependencies or architecture/state/routing/localization/generator changes.
- Do not force new packages, services, patterns, or tests.
- Keep secrets out of source control. Stop suspicious/long commands; report command and elapsed time.
- Add/update tests for behavior changes when requested or consistent with project practice. Run narrow verification.
- For non-trivial changes, self-review with `production-code-review`; add `architecture-review`, `solid-oop-review`, `security-review`, or `performance-review` when relevant.
- Default `$caveman lite`; expand only for safety, blockers, or user request.

## Flutter

- Check `analysis_options.yaml` and `.agents/flutter-dependencies.md`.
- Prefer composition, immutable widgets, and `const`; keep `build()` pure/fast and business logic outside widgets.
- Use lazy builders for long lists; move expensive work off UI thread when needed.
- Keep null safety; avoid `!` unless guaranteed. Use project logging, not `print`.
- Reuse design components, assets, themes, and tokens.
- Preserve localization, responsive/accessibility behavior, platform parity, permissions, entitlements, and fallbacks.
- Cover relevant loading, success, empty, error, disabled, and permission states. Keep errors actionable.
- Use configured flavors and `--dart-define-from-file`.

## Contracts

- Do not silently change public APIs. Update consumers, mocks/fixtures, migrations, and verification together.
- Keep PRs single-goal; report behavior, files, verification, gaps, and release/API/env/permission impact.

## Subagents

For medium/large/risky/unclear work, use `.agents/skills/subagent-workflow`. Skip trivial edits. Default: BA -> TL -> developer -> TL review loop -> QA.

## Git

Branch: `<type>/<ticket-title-summary>`, e.g. `feature/add-login`.

Commit with ticket:

```text
<ticket> - <summary>

- <point A>
- <point B>
```

Without ticket, omit `<ticket> - `.

## Done

- Changed Dart formatted; relevant code compiles/type-checks.
- Relevant tests/checks pass, or failures/blockers are reported.
- Final response states changes and verification.
