---
name: fullstack-flutter-engineering
description: Use when working on Flutter-first full-stack software engineering tasks, including feature implementation, bug fixing, architecture review, API integration, database-backed changes, testing, release readiness, or code review across mobile, web, backend, and infrastructure.
---

# Full-Stack Flutter Engineering

## Rules

- Read the repo before changing code.
- Make the smallest coherent change that solves the request.
- Prefer the minimal-token approach.
- Check `analysis_options.yaml` before coding to follow lint rules early.
- Follow existing architecture, state, routing, API, error, logging, and test patterns.
- Follow SOLID, prefer OOP structure, and keep code production-level with minimal boilerplate.
- Use the project's state management; prefer Bloc/Cubit only when already used or requested.
- Keep UI, state, domain, and data responsibilities separated.
- Split large files into focused units and use concise Dart syntax when readable.
- Ask before adding dependencies.
- Use existing routing, design system, component, asset/theme/token conventions unless change is needed.
- If localization exists, do not add raw user-facing strings.
- For platform features, update Android/iOS permissions and fallbacks together.
- Avoid unnecessary rebuilds; use `const`, selectors, and scoped rebuilds where useful.
- Avoid hardcoded values unless justified by edge case.
- Do not modify generated files manually.
- Cover loading, error, empty, disabled, and permission states when relevant.
- User-facing errors must be clear and actionable.
- Define production retry/logging pattern for failure states.
- New Bloc/Cubit logic needs unit tests when practical.
- Always ensure responsive behavior; add accessibility quality when scenario or request needs it.
- Use flavors for `dev` and `prod`; add `staging` when requested.
- Use `--dart-define-from-file` with `.env.dev.json`, `.env.prod.json`, and optional `.env.staging.json`.
- Keep API changes contract-safe; update validation, generated clients, fixtures, and tests together.
- Use migrations for schema changes and preserve existing data compatibility.
- Include authorization checks near protected operations.

## Verification

Run the most relevant available command:

```sh
flutter analyze
flutter test
npm test
npm run lint
go test ./...
```

Stop suspicious commands and report command plus elapsed time, such as `flutter analyze` around 60s or `flutter test` with no output around 120s. If verification cannot run, state why.
