# AGENTS.md

Flutter-first coding rules for Codex.

## Repo Layout

- `AGENTS.md`: repo instructions for Codex.
- `.agents/project-map.md`: folder-level map from product/code areas to repo directories.
- `subagents/`: reusable subagent prompt templates.
- `reports/subagents/`: generated subagent reports, grouped by task slug.
- App source, tests, scripts, and platform folders vary by copied project; inspect the root before work.

## Commands

- Discover project type: inspect root files such as `pubspec.yaml`, `analysis_options.yaml`, package files, and scripts.
- Run Flutter app: `flutter run --dart-define-from-file=.env.dev.json`.
- Analyze: `flutter analyze`.
- Test: `flutter test`.
- Build Android: `flutter build apk --dart-define-from-file=.env.prod.json`.
- Build iOS: `flutter build ios --dart-define-from-file=.env.prod.json`.
- Use existing project scripts when present; do not invent new commands before checking the repo.

## Command Output

- Protect context usage: byte/char-cap commands with unknown or potentially large output.
- Known-small commands like `git status --short` do not need caps.
- macOS/Linux: `COMMAND 2>&1 | head -c 4000`.
- Windows PowerShell: `$out = COMMAND 2>&1 | Out-String; $out.Substring(0, [Math]::Min(4000, $out.Length))`.

## Work Rules

- Read nearby code first.
- Check `.agents/project-map.md` before broad searches; if missing or stale, infer areas from repo structure and update it.
- Follow existing architecture, naming, formatting, and test style.
- Adapt workflow patterns only when they fit the current repo; existing project conventions win.
- Keep changes small and scoped.
- Always prefer the minimal-token approach.
- Keep Codex guidance minimal and scoped to the active repo.
- Avoid adding extra docs, checklists, templates, or verbose guidance unless clearly needed.
- Preserve user changes; never reset unrelated work.
- Add/update tests when behavior changes.
- Run the narrowest useful verification.
- Stop suspicious commands and report command plus elapsed time, e.g. `flutter analyze` around 20s or `flutter test` with no output around 30s.
- Keep secrets out of source control.
- Ask before installing packages, plugins, tools, or global dependencies.
- Do not introduce new frameworks, state managers, databases, or services without clear need.
- Do not force external defaults such as new packages, Riverpod, Clean Architecture, or test generation.
- Default to `$caveman lite`; use normal mode only when user asks or detail is necessary.
- Keep responses short and precise. Do not explain further unless asked or needed for safety/blockers.

## Flutter Rules

- Check `analysis_options.yaml` before coding to follow lint rules early.
- Follow SOLID principles and prefer clear OOP structure.
- Use the project's state management; prefer Bloc/Cubit only when already used or requested.
- Keep code minimal, production-level, and low-boilerplate.
- Keep widgets small and business logic out of large widget trees.
- Split large files into focused units; avoid many-line files.
- Use concise Dart syntax, including expression-bodied members, when it stays readable.
- Use existing state, routing, theme, localization, API, and generator patterns.
- If the project already uses layered/Clean Architecture, keep changes in the existing layer order: domain contract first, data implementation second, presentation last.
- Ask before adding dependencies.
- Use existing routing, design system, component, asset/theme/token conventions unless change is needed.
- If localization exists, do not add raw user-facing strings.
- For platform features, update Android/iOS permissions and fallbacks together.
- Avoid unnecessary rebuilds; use `const`, selectors, and scoped rebuilds where useful.
- Avoid hardcoded values; allow only justified edge cases.
- Do not modify generated files manually.
- Cover loading, success, empty, error, disabled, and permission states when relevant.
- User-facing errors must be clear and actionable.
- Flutter Developer defines production retry/logging pattern for failure states.
- New Bloc/Cubit logic needs unit tests when practical.
- Always ensure responsive behavior; add accessibility quality when scenario or request needs it.
- Configure flavors for `dev` and `prod`; add `staging` when requested.
- Use `--dart-define-from-file` with `.env.dev.json`, `.env.prod.json`, and optional `.env.staging.json`.

## Full-Stack Rules

- Treat client, API, database, and infrastructure changes as one contract.
- Update DTOs, generated clients, fixtures, mocks, migrations, and tests together.
- Do not silently change public API behavior.

## PR Expectations

- Keep PRs scoped to one user goal.
- Include behavior change, files touched, verification run, and known gaps.
- Mention migrations, API changes, env changes, permissions, or release notes when relevant.
- Do not mix unrelated refactors with feature or bug work.

## Subagents

Core: `business-analyst`, `team-lead`, `flutter-developer`, `qa`.

Optional specialists: `backend-api-developer`, `devops-release-engineer`, `security-privacy-reviewer`, `ux-product-reviewer`.

Do not use subagents for trivial edits, formatting, copy changes, or one-file fixes.

Use subagents for medium, large, risky, or unclear work. Use `.agents/skills/subagent-workflow` for routing, model choice, planning, reports, review loops, QA behavior, and compaction timing.

Default flow: `business-analyst` business scope -> `team-lead` technical direction -> developer -> `team-lead` review loop -> `qa`.

Subagents must plan before operations, stay within role permissions, write reports under `reports/subagents/<task-slug>/`, and link reports in the final response.

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
