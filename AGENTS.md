# AGENTS.md

Flutter-first coding rules for Codex.

## Work Rules

- Read nearby code first.
- Follow existing architecture, naming, formatting, and test style.
- Keep changes small and scoped.
- Always prefer the minimal-token approach.
- Keep this template minimal: only `README.md` is user-facing; other files are for Codex use.
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

## Subagents

Core: `business-analyst`, `team-lead`, `flutter-developer`, `qa`.

Optional specialists: `backend-api-developer`, `devops-release-engineer`, `security-privacy-reviewer`, `ux-product-reviewer`.

Model preferences: `team-lead` GPT-5.5, `flutter-developer` GPT-5.3-Codex, `qa` GPT-5.4, all other roles GPT-5.4-Mini unless complexity requires stronger.

If a preferred model is unavailable, use the nearest capable model and state the fallback.

Do not use subagents for trivial edits, formatting, copy changes, or one-file fixes.

Subagent output returns as the subagent final response by default. Write files only when persistent artifacts are needed, under `reports/subagents/<task-slug>/<role>.md`.

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
