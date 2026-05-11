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

## Work Rules

- Read nearby code first.
- Check `.agents/project-map.md` before broad searches; if missing or stale, infer areas from repo structure and update it.
- Follow existing architecture, naming, formatting, and test style.
- Keep changes small and scoped.
- Always prefer the minimal-token approach.
- Keep Codex guidance minimal and scoped to the active repo.
- Avoid adding extra docs, checklists, templates, or verbose guidance unless clearly needed.
- Preserve user changes; never reset unrelated work.
- Add/update tests when behavior changes.
- Run the narrowest useful verification.
- Stop suspicious commands and report command plus elapsed time, e.g. `flutter analyze` around 60s or `flutter test` with no output around 120s.
- Keep secrets out of source control.
- Ask before installing packages, plugins, tools, or global dependencies.
- Do not introduce new frameworks, state managers, databases, or services without clear need.
- Default to `$caveman lite`; use normal mode only when user asks or detail is necessary.

## Flutter Rules

- Check `analysis_options.yaml` before coding to follow lint rules early.
- Follow SOLID principles and prefer clear OOP structure.
- Use the project's state management; prefer Bloc/Cubit only when already used or requested.
- Keep code minimal, production-level, and low-boilerplate.
- Keep widgets small and business logic out of large widget trees.
- Split large files into focused units; avoid many-line files.
- Use concise Dart syntax, including expression-bodied members, when it stays readable.
- Use existing state, routing, theme, localization, API, and generator patterns.
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

Model selection: use the best available model for the role and task.

- `team-lead`: strongest reasoning model available.
- `flutter-developer`: best coding-optimized model available.
- `qa`: strong reasoning model with good code/test analysis.
- Other specialists: fast capable model; upgrade when complexity or risk requires it.
- If a newer model supersedes these choices, prefer the newer capable model.
- Record chosen model and fallback reason in the role report.

Do not use subagents for trivial edits, formatting, copy changes, or one-file fixes.

When subagents are used, always write reports under `reports/subagents/<task-slug>/`.

- Pass relevant `.agents/project-map.md` areas and folders into each subagent prompt.
- Ask `team-lead` or the first relevant developer subagent to update `.agents/project-map.md` when task terms do not map to known areas.
- Maintain `timeline.md` as a short event log: time/order, role, action, decision, outcome.
- Write each role report as `<role>.md`.
- If the same role runs again, append a new `## Run N - <short reason>` section instead of rewriting prior runs.
- Use this report shape only:
  - `Task`: one sentence.
  - `Result`: done, partial, blocked, or rejected.
  - `Changed`: files changed, or `None`.
  - `Read`: key folders/files only, max 6.
  - `Findings`: max 5 bullets, severity/order first.
  - `Verification`: commands/checks and result.
  - `Next`: one concrete next step, or `None`.
- Keep each run report under 80 lines unless a blocker needs evidence.
- Use `$caveman full`: precise fragments, no filler.
- Link reports in the final response.
- Close subagents after their report is written and their result is integrated.

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
