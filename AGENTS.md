# AGENTS.md

Flutter-first coding rules for Codex.

## Repo Layout

- `.agents/`: map, subagents, skills, tools, AI/tooling docs.
- `reports/subagents/`: generated reports.
- App layout varies; inspect root before work.

## Commands

- Prefer existing scripts. Common: `flutter analyze`, `flutter test`, `flutter run --dart-define-from-file=.env.dev.json`, `flutter build <target> --dart-define-from-file=.env.prod.json`.
- Cap potentially large command output at 4,000 chars.

## Work Rules

- Read nearby code first.
- Check `.agents/project-map.md` before broad searches; if missing/empty/stale, preview with `python3 .agents/tools/generate_project_map.py`, then update via `apply_patch`.
- Use only relevant `.agents/skills/<skill>/SKILL.md`; repo architecture wins over generic examples.
- Prefer Dart/Flutter MCP for analyzer, symbols, fixes, format, tests, pub.dev, dependencies, and running-app/widget inspection.
- Prefer CodeGraph MCP when `.codegraph/` exists for semantic search, callers/callees, impact, and architecture discovery.
- Follow existing architecture, naming, formatting, and test style.
- Keep changes small, scoped, and low-token.
- Preserve user changes; never reset unrelated work.
- Add/update tests for behavior changes; run the narrowest useful verification.
- Stop suspicious commands; report command and elapsed time.
- Keep secrets out of source control.
- Ask before installing packages/plugins/tools/global deps or changing package choices.
- Existing conventions win; do not force new packages, state managers, architecture, services, or test generation.
- Default `$caveman lite`: short, precise; expand only when asked or needed for safety/blockers.

## Flutter Guardrails

- Check `analysis_options.yaml`; use matching official skills.
- Follow existing state, routing, theme, localization, API, generator, platform, and test patterns.
- Prefer composition, immutable widgets, and `const`; keep `build()` pure/fast and business logic outside widget trees.
- Use lazy builders for long lists; move expensive work off the UI thread when needed.
- Keep Dart null-safe; avoid `!` unless guaranteed. Do not use `print`; follow project logging.
- Respect existing layers. Follow `.agents/flutter-dependencies.md`; ask before dependency, architecture, routing, localization, or generator changes.
- Use existing design/component/asset/theme/token conventions.
- Preserve localization, platform parity, and permissions/entitlements/fallbacks.
- Do not modify generated files manually.
- Cover relevant loading, success, empty, error, disabled, permission, responsive, and accessibility states.
- Keep user errors actionable. Use configured flavors and `--dart-define-from-file`.

## Contracts and PRs

- Do not silently change public APIs. Update connected client, mocks/fixtures, migrations, and verification together.
- Keep PRs single-goal; mention behavior, files, verification, gaps, and relevant migration/API/env/permission/release impact.

## Subagents

For medium/large/risky/unclear work, use `.agents/skills/subagent-workflow`. Skip trivial edits. Default: BA -> TL -> developer -> TL review loop -> QA.

## Git

Branch format: `<type>/<ticket-title-summary>`, e.g. `feature/add-login`, `bugfix/fix-login-error`, `task/update-env`.

Commit format with ticket:

```text
<ticket> - <summary>

- <point A>
- <point B>
```

Commit format without ticket:

```text
<summary>

- <point A>
- <point B>
```

## Done

- Changed Dart code is formatted.
- Relevant code compiles or type-checks.
- Relevant tests pass, or failures are reported.
- Final response states what changed and what was verified.
