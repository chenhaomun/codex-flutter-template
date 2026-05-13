---
name: subagent-workflow
description: >
  Subagent workflow rules for this repo. Use when the user asks to use subagents,
  run BA/TL/developer/QA, choose subagent models, produce subagent reports, compact
  context, or manage multi-agent Flutter work.
---

Use this workflow only for medium, large, risky, or unclear work.

## Routing

- Business scope: `business-analyst`.
- Architecture, refactor, SOLID, ownership, integration risk: `team-lead`.
- Flutter UI, widget, state, routing, platform, implementation: `flutter-developer`.
- API, DTO, migration, contract, database: `backend-api-developer`.
- CI, build, release, env, signing: `devops-release-engineer`.
- Security, privacy, auth, permissions, secrets, payments: `security-privacy-reviewer`.
- UX, accessibility, copy, empty/loading/error state: `ux-product-reviewer`.
- Functional verify, manual QA, regression, risk: `qa`.

## Model Choice

Choose by task complexity, not fixed role preference.

| Complexity | Use | Examples |
|---|---|---|
| Low | fast capable model | clear one-file inspection, simple QA checklist |
| Medium | strong coding/reasoning model | multi-file implementation, state/routing changes |
| High | strongest available model | architecture, risky refactor, cross-contract review |

Record chosen model and fallback reason in the role report only when useful.

## Permissions

- Read-only by default: BA, TL, QA, security, UX.
- Write-capable only with explicit ownership: Flutter, backend/API, DevOps.
- QA must not add test files unless the user asks for tests.
- Developers must not edit outside ownership without reporting why.

## Plan Before Operations

Every subagent starts with a short plan before commands or edits:

| Field | Plan |
|---|---|
| Goal | one sentence |
| Scope | owned folders/files or review area |
| Steps | max 3 |
| Verify | command/manual check |

## Execution

- Default flow: BA -> TL -> developer -> TL review -> developer revision -> QA.
- TL review has two gates: spec compliance first, then code quality/architecture.
- Repeat TL review -> developer revision until accepted; stop after 3 rounds and report blocker.
- Parallelize only independent work.
- Prefer isolated/forked context for research, review, verification, and independent implementation.

## Reports

Write reports under `reports/subagents/<task-slug>/`.

- Maintain `timeline.md`: time/order, role, action, decision, outcome.
- Write each role report as `<role>.md`.
- Append `## Run N - <short reason>` for repeat role runs.
- Keep reports table-based and under 80 lines.
- Do not include files read unless essential evidence.
- Use `$caveman lite`.

Report shape:

```text
## Run N - <short reason>

| Field | Report |
|---|---|
| Task | ... |
| Result | done / done with concerns / blocked / rejected |
| Changed | ... |
| Verification | ... |
| Next | ... |
| Final outcome | ... |

| Decision | Reason | Outcome |
|---|---|---|
| ... | ... | ... |

| Step | Critical thinking | Outcome |
|---|---|---|
| ... | ... | ... |
```

## QA Without Tests

If no tests exist or tests are not requested, QA verifies with:

- `flutter analyze` when available.
- app run or manual scenario checks.
- loading/success/empty/error/permission state checks.
- regression checks near the changed flow.

## Compact Timing

Main agent or subagents should compact/summarize before context gets heavy:

- after 15 user/assistant turns in one task;
- before spawning more than 2 subagents;
- after each TL/developer review loop;
- when a report file exceeds 120 lines;
- before switching from implementation to QA.

Before compacting, update `timeline.md` and add current decisions, changed files, blockers, and next step.
