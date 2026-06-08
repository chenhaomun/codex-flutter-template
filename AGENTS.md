# AGENTS.md

Flutter-first Codex rules.

## Repo Layout

- `.agents/`: map, skills, subagents, tools.
- `reports/subagents/`: generated reports. Inspect app root before work.

## Commands

- Prefer project scripts. Common: `flutter analyze`, `flutter test`, `flutter run --dart-define-from-file=.env.dev.json`, `flutter build <target> --dart-define-from-file=.env.prod.json`.
- Cap potentially large command output at 4,000 chars.

## Work Rules

- Read nearby code; follow existing architecture, naming, state, routing, theme, l10n, API, generator, platform, and test patterns.
- Check `.agents/project-map.md` before broad search; if missing/stale, preview `<python> .agents/tools/generate_project_map.py`, then update via `apply_patch`.
- Use relevant `.agents/skills/<skill>/SKILL.md`; project conventions beat generic examples.
- Auto-use `grill-requirements` when acceptance, scope, target flow/state, or contradictions may cause rework. Ask max 3 blocking questions; else state assumptions and proceed.
- Prefer Dart/Flutter MCP for analyzer, symbols, fixes, format, tests, pub.dev, dependencies, and running-app/widget inspection.
- For refactor/rename/architecture/unclear bug/API contract/cross-module/dead code/risky cleanup: use CodeGraph if `.codegraph/` exists; ask before generating for large/risky work; else use `rg`.
- Keep changes scoped. Preserve user changes. Never reset unrelated work or edit generated files.
- Follow SOLID/DRY/KISS. Ask before packages/tools/global deps or architecture/state/routing/l10n/generator changes.
- No forced packages, services, patterns, or broad test suites.
- Use `test-driven-development` only when clear behavior + regression risk justify it; skip trivial/low-risk edits.
- Keep secrets out. Stop suspicious/long commands; report command + elapsed.
- Add/update tests when requested, useful for TDD, or matching project practice. Run narrow verification.
- Tiered review: small = self-check; medium single-owner = `production-code-review` + max one specialist; large/risky/multi-agent = full review.
- Default `$caveman lite`; expand only for safety, blockers, or user request.

## Flutter

- Check `analysis_options.yaml` and `.agents/flutter-dependencies.md`.
- Prefer composition, immutable widgets, `const`, pure/fast `build()`, lazy lists, and off-UI-thread expensive work.
- Keep null safety; avoid `!` unless guaranteed. Use project logging, not `print`.
- Reuse design assets/theme/tokens. Preserve l10n, responsive/a11y, platform parity, permissions, entitlements, fallbacks.
- Cover loading, success, empty, error, disabled, and permission states. Keep errors actionable.
- Use configured flavors and `--dart-define-from-file`.

## Contracts

- Do not silently change public APIs. Update consumers, mocks/fixtures, migrations, and verification together.
- Keep PRs single-goal; report behavior, files, verification, gaps, and release/API/env/permission impact.

## Subagents

For medium/large/risky/unclear work, use `.agents/skills/subagent-workflow`. Skip trivial edits. Default: BA -> TL -> dev -> TL review -> QA.

## Git

Branch: `<type>/<ticket-title-summary>`, e.g. `feature/add-login`.

For commit messages from staged changes, use `git-staged-commit-message`.

Commit with ticket:

```text
<ticket> - <summary>

- <point A>
- <point B>
```

Without ticket, omit `<ticket> - `.

## Done

- Changed Dart is formatted; relevant code compiles/type-checks.
- Relevant tests/checks pass, or failures/blockers are reported.
- Medium+ work has review level matched to risk, or a clear skipped reason.
- Final response states changes and verification.
