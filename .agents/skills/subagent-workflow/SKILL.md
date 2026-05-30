---
name: subagent-workflow
description: >
  Subagent workflow rules. Use when asked to use subagents, route BA/TL/dev/QA,
  choose models, write reports, track token-heavy output, compact context, or manage
  multi-agent work.
---

Use only for medium, large, risky, or unclear work.

## Routing

BA: business scope. TL: architecture/refactor/ownership/risk. Flutter dev: UI/state/routing/platform/implementation. Backend: API/DTO/migration/contract/database. DevOps: CI/build/release/env/signing. Security: privacy/auth/permissions/secrets/payments. UX: accessibility/copy/states. QA: functional verify/manual QA/regression/risk.

## Model Choice

Use these default overrides:

| Role | Model |
|---|---|
| BA | `gpt-5.4-mini` |
| TL | `gpt-5.5` |
| Flutter dev | `gpt-5.3-codex` |
| Backend/API | `gpt-5.3-codex` |
| DevOps | `gpt-5.4` |
| Security | `gpt-5.4` |
| UX | `gpt-5.4-mini` |
| QA | `gpt-5.4` |

Override only when task complexity clearly requires a stronger model. If listed model is unavailable, use nearest capable model. Record model and fallback in report.

## Permissions

- Read-only by default: BA, TL, QA, security, UX.
- Write-capable only with explicit ownership: Flutter, backend/API, DevOps.
- QA must not add test files unless the user asks for tests.
- Developers must not edit outside ownership without reporting why.

## Plan Before Operations

Every subagent starts with a short plan: goal, scope, max 3 steps, verification.

## Execution

- Use one stable kebab-case `task-slug` for `reports/subagents/<task-slug>/` during the whole task.
- Flow: BA -> TL -> developer -> developer self-check -> TL production review -> developer revision -> QA.
- TL review: spec compliance first, code quality/architecture second.
- Repeat TL loop until accepted; stop after 3 rounds.
- Parallelize only independent work; prefer isolated/forked context.

## Production Bar

Developer cannot report `done` unless these pass:

behavior matches requirements; diff is scoped; architecture fits; no unnecessary dependency/framework/service; relevant states are handled; performance-sensitive UI is considered; platform parity/adaptation is preserved; localization/responsive/accessibility conventions are followed; no debug/dead/TODO/generated-file edits; verification run or blocker stated.

If any item fails, return `done with concerns`, `blocked`, or `rejected`.

## Gate Lite

Stop and route instead of guessing.

Gates: `USER_DECISION` stop/ask; `CLARIFICATION` route to BA/TL; `REVIEW_CHANGES` send exact revision; `PRODUCTION_GAP` reject/revise; `BLOCKED` stop/report; `ACCEPTED` continue.

Clarifications include owner, question, why blocked, options/default only when useful and safe.

## Task Breakdown

For larger work, TL may create task rows with: task, dependency, owner, requirement, verification.

Keep slices reviewable. Parallelize only non-overlapping ownership.

## Code Quality

- TL must split medium/large implementation into small slices before coding.
- Each developer run owns one bounded module or concern. Avoid whole-feature prompts.
- Developer must read nearby code/tests and state intended files before editing.
- Developer runs narrow analysis/tests after each slice.
- TL reviews actual diff after each slice, not report only.
- TL rejects duplication, oversized files/widgets, mixed responsibilities, missing states/tests, or unrelated edits.
- Integrate only after each slice passes review.
- Use stronger model when a slice still needs broad cross-module reasoning.

Typical Flutter slices: domain/contracts -> repository/API -> Bloc/Cubit -> UI -> routing/platform -> tests/regression.

## Harness Tools

Use `.agents/tools/` at checkpoints, not every turn.

| Checkpoint | Tool |
|---|---|
| Task start, project type unclear | `python3 .agents/tools/detect_project.py` |
| Project map missing/empty/stale | Preview with `python3 .agents/tools/generate_project_map.py`; update via `apply_patch` |
| Before broad search or after map edits | `python3 .agents/tools/check_project_map.py` |
| After medium/large subagent run | `python3 .agents/tools/count_tokens.py --update --task "<task-slug>"` |
| Before compaction | `python3 .agents/tools/count_tokens.py --update --task "<task-slug>"` |

Keep output short. No install/network/destructive action without approval.

## Reports

Write reports under `reports/subagents/<task-slug>/`.

- `timeline.md`: time/order, role, action, decision, outcome.
- `<role>.md`; append `## Run N - <short reason>` for repeats.
- Table-based, under 80 lines.
- Omit files read unless essential evidence.
- Use `$caveman lite`.
- Use `$caveman full` for live progress/thinking updates; reports stay clear and table-based.

Report fields: run heading, `Field/Report`, `Decision/Reason/Outcome`, `Step/Critical thinking/Outcome`.

## QA Without Tests

If tests do not exist or are not requested, QA uses static checks, app/manual scenarios, state checks, and nearby regression checks.

## Compact Timing

Compact/summarize before context gets heavy:

- after 15 turns in one task;
- before more than 2 subagents;
- after each TL/dev review loop;
- when a report exceeds 120 lines;
- before QA handoff.

Before compacting, update `timeline.md`: decisions, changed files, blockers, next step.

## Token Tracking

Update `.agents/guidance-token-report.md` after subagent runs, command output over 2,000 chars, before compaction, and final handoff. Approximate with words/chars.
