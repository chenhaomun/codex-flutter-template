# AGENTS.md

Flutter-first coding rules for Codex.

## Repo Layout

- `AGENTS.md`: repo instructions for Codex.
- `.agents/`: project map, subagents, skills, tools, token report.
- `reports/subagents/`: subagent reports.
- App layout varies; inspect root before work.

## Commands

- Discover project type from root markers and scripts.
- Run Flutter app: `flutter run --dart-define-from-file=.env.dev.json`.
- Analyze: `flutter analyze`.
- Test: `flutter test`.
- Build: use project target, e.g. `flutter build <target> --dart-define-from-file=.env.prod.json`.
- Use existing project scripts when present; do not invent new commands before checking the repo.

## Command Output

- Byte/char-cap unknown or potentially large output.
- Known-small commands like `git status --short` do not need caps.
- macOS/Linux: `COMMAND 2>&1 | head -c 4000`.
- Windows PowerShell: `$out = COMMAND 2>&1 | Out-String; $out.Substring(0, [Math]::Min(4000, $out.Length))`.

## Work Rules

- Read nearby code first.
- Check `.agents/project-map.md` before broad searches; if missing/empty/stale, run `python .agents/tools/generate_project_map.py --write`.
- Follow existing architecture, naming, formatting, and test style.
- Keep changes small and scoped.
- Prefer minimal-token guidance and output.
- Preserve user changes; never reset unrelated work.
- Add/update tests when behavior changes.
- Run the narrowest useful verification.
- Stop suspicious commands and report command plus elapsed time, e.g. `flutter analyze` around 20s or `flutter test` with no output around 30s.
- Keep secrets out of source control.
- Ask before installing packages, plugins, tools, or global dependencies.
- Existing conventions win; do not force new packages, state managers, architecture, services, or test generation.
- Default to `$caveman lite`; use normal mode only when user asks or detail is necessary.
- Visible thinking/status updates consume context; use `$caveman full` for progress updates during long tasks.
- Keep responses short and precise. Do not explain further unless asked or needed for safety/blockers.

## Flutter Rules

- Check `analysis_options.yaml` before coding to follow lint rules early.
- Follow SOLID/OOP and existing state/routing/theme/localization/API/generator patterns.
- Keep widgets small; keep business logic out of large widget trees.
- Keep code minimal, production-level, low-boilerplate, and split when files grow.
- Use concise Dart syntax when readable.
- If layered/Clean Architecture exists, follow existing layer order.
- Ask before adding dependencies.
- Use existing design/component/asset/theme/token conventions.
- If localization exists, do not add raw user-facing strings.
- For platform features, update target permissions, entitlements, and fallbacks together.
- Avoid unnecessary rebuilds; use `const`, selectors, and scoped rebuilds where useful.
- Watch performance-sensitive UI: scrolling, image loading/caching, rebuild scope, startup, and memory.
- Avoid hardcoded values; allow only justified edge cases.
- Do not modify generated files manually.
- Cover loading/success/empty/error/disabled/permission states when relevant.
- User-facing errors must be clear and actionable.
- New Bloc/Cubit logic needs unit tests when practical.
- Ensure responsive behavior and needed accessibility.
- Maintain target-platform parity/adaptation and state restoration when relevant.
- Use configured flavors and `--dart-define-from-file` env files.

## Contract Rules

- When work touches API/backend/data contracts, update connected client, mocks/fixtures, migrations, and verification together.
- Do not silently change public API behavior.

## PR Expectations

- Keep PRs scoped to one user goal.
- Include behavior change, files touched, verification run, and known gaps.
- Mention migrations, API changes, env changes, permissions, or release notes when relevant.
- Do not mix unrelated refactors with feature or bug work.

## Subagents

Core: `business-analyst`, `team-lead`, `flutter-developer`, `qa`.
Optional: `backend-api-developer`, `devops-release-engineer`, `security-privacy-reviewer`, `ux-product-reviewer`.
Skip subagents for trivial edits, formatting, copy changes, or one-file fixes.
Use `.agents/skills/subagent-workflow` for medium/large/risky/unclear work.
Default flow: BA scope -> TL direction -> developer -> TL review loop -> QA.

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
