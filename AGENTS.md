# AGENTS.md

Flutter-first Codex rules.

## Commands / Verify

- Prefer project scripts. Common: `flutter analyze`, `flutter test`, `flutter run --dart-define-from-file=.env.dev.json`, `flutter build <target> --dart-define-from-file=.env.prod.json`.
- Cap potentially large command output at 4,000 chars.
- Final response states changes, verification, blockers/gaps, and API/env/permission impact if relevant.

## Work Rules

- Read nearby code; follow existing architecture, naming, state, routing, theme, l10n, API, generator, platform, and test patterns.
- Check `.agents/project-map.md` before broad search; if missing/stale, preview `<python> .agents/tools/generate_project_map.py`, then update via `apply_patch`.
- Use relevant `.agents/skills/<skill>/SKILL.md`; project conventions beat generic examples.
- Use `grill-requirements` when acceptance, scope, target flow/state, or contradictions may cause rework.
- Prefer Dart/Flutter MCP for analyzer, symbols, fixes, format, tests, pub.dev, dependencies, and running-app/widget inspection.
- Keep changes scoped. Preserve user changes. Never reset unrelated work or edit generated files.
- Follow SOLID/DRY/KISS. Ask before packages/tools/global deps or architecture/state/routing/l10n/generator changes.
- Native/FFI/binary downloads require explicit user approval and hash/offline fallback review.
- Use `test-driven-development` only when clear behavior + regression risk justify it; skip trivial/low-risk edits.
- Keep secrets out. Stop suspicious/long commands; report command + elapsed.
- Add/update tests when requested, useful for TDD, or matching project practice. Run narrow verification.
- Tiered review: small = self-check; medium single-owner = `production-code-review` + max one specialist; large/risky/multi-agent = full review.
- Default `$caveman lite`; expand only for safety, blockers, or user request.

## Flutter

- Check `analysis_options.yaml` and `.agents/flutter-dependencies.md`.
- Prefer composition, immutable widgets, `const`, pure/fast `build()`, lazy lists, and off-UI-thread expensive work.
- Keep null safety; avoid `!` unless guaranteed. Use project logging, theme/assets/tokens, l10n, responsive/a11y, platform parity, permissions, and fallbacks.
- Cover loading, success, empty, error, disabled, and permission states. Keep errors actionable.
- Use configured flavors and `--dart-define-from-file`.

## Contracts

- Do not silently change public APIs. Update consumers, mocks/fixtures, migrations, and verification together.
- Keep PRs single-goal.

## Subagents

For medium/large/risky/unclear work, use `.agents/skills/subagent-workflow`. Skip trivial edits.

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
