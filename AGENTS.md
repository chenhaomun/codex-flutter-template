# AGENTS.md

Flutter-first coding rules for Codex.

## Repo Layout

- `AGENTS.md`: repo instructions for Codex.
- `.agents/`: project map, subagents, skills, tools, token report, AI/tooling docs.
- `.agents/flutter-dependencies.md`: preferred Flutter packages.
- `.agents/skill-maintenance.md`: skill refresh workflow and review checklist.
- `reports/subagents/`: subagent reports.
- App layout varies; inspect root before work.

## Commands

- Discover project type from root markers and scripts.
- Run Flutter app: `flutter run --dart-define-from-file=.env.dev.json`.
- Analyze: `flutter analyze`.
- Test: `flutter test`.
- Build: use project target, e.g. `flutter build <target> --dart-define-from-file=.env.prod.json`.
- Prefer existing project scripts.

## Command Output

- Byte/char-cap unknown or potentially large output.
- Known-small commands like `git status --short` do not need caps.
- macOS/Linux: `COMMAND 2>&1 | head -c 4000`.
- Windows PowerShell: `$out = COMMAND 2>&1 | Out-String; $out.Substring(0, [Math]::Min(4000, $out.Length))`.

## Work Rules

- Read nearby code first.
- Check `.agents/project-map.md` before broad searches; if missing/empty/stale, run `python .agents/tools/generate_project_map.py --write`.
- Use matching project skills from `.agents/skills`; read only the relevant `SKILL.md`.
- Prefer official Flutter/Dart skills for matching tasks; follow repo architecture over generic skill examples.
- Prefer Dart/Flutter MCP for analyzer, symbols, fixes, format, tests, pub.dev, dependencies, and running-app/widget inspection.
- Prefer CodeGraph MCP when `.codegraph/` exists for semantic search, callers/callees, impact, and architecture discovery.
- Follow existing architecture, naming, formatting, and test style.
- Keep changes small, scoped, and low-token.
- Preserve user changes; never reset unrelated work.
- Add/update tests for behavior changes; run the narrowest useful verification.
- Stop suspicious commands and report command plus elapsed time, e.g. `flutter analyze` around 20s or `flutter test` with no output around 30s.
- Keep secrets out of source control.
- Ask before installing packages/plugins/tools/global deps or using skills that change dependencies/package choices.
- Existing conventions win; do not force new packages, state managers, architecture, services, or test generation.
- Default to `$caveman lite`; use normal mode only when user asks or detail is necessary.
- Keep responses short and precise. Do not explain further unless asked or needed for safety/blockers.

## Flutter Guardrails

- Check `analysis_options.yaml` before coding.
- Use official skills for routing, localization, responsive layout, JSON, analysis, coverage, widget/integration tests, and package conflicts.
- Follow existing state, routing, theme, localization, API, generator, platform, and test patterns.
- Keep widgets small; keep business logic out of large widget trees.
- If layered/Clean Architecture exists, implement in existing layer order.
- Follow `.agents/flutter-dependencies.md`; ask before changing dependencies, architecture, routing, localization, or generators.
- Use existing design/component/asset/theme/token conventions.
- Preserve localization, platform parity, permissions/entitlements/fallbacks, and performance-sensitive UI.
- Do not modify generated files manually.
- Cover relevant loading, success, empty, error, disabled, permission, responsive, and accessibility states.
- User-facing errors must be clear and actionable.
- Use configured flavors and `--dart-define-from-file` env files.

## Contracts and PRs

- Do not silently change public API behavior.
- When touching API/backend/data contracts, update connected client, mocks/fixtures, migrations, and verification together.
- Keep PRs scoped to one goal; mention behavior change, files touched, verification, known gaps, and any migrations/API/env/permission/release-note impact.

## Subagents

Core: `business-analyst`, `team-lead`, `flutter-developer`, `qa`.
Optional: `backend-api-developer`, `devops-release-engineer`, `security-privacy-reviewer`, `ux-product-reviewer`.
Skip subagents for trivial edits, formatting, copy changes, or one-file fixes.
Use `.agents/skills/subagent-workflow` for medium/large/risky/unclear work.
Default flow: BA -> TL -> developer -> TL review loop -> QA.

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

- Relevant code compiles or type-checks.
- Relevant tests pass, or failures are reported.
- Final response states what changed and what was verified.
