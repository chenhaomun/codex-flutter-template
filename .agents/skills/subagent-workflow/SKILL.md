---
name: subagent-workflow
description: >
  Subagent workflow rules. Use when asked to use subagents, route BA/TL/dev/QA,
  choose models, write reports, track token-heavy output, compact context, or manage
  multi-agent work.
---

Use only for medium, large, risky, or unclear work.

## Routing

- Business scope -> `business-analyst`.
- Architecture/refactor/ownership/risk -> `team-lead`.
- Flutter UI/state/routing/platform/implementation -> `flutter-developer`.
- API/DTO/migration/contract/database -> `backend-api-developer`.
- CI/build/release/env/signing -> `devops-release-engineer`.
- Security/privacy/auth/permissions/secrets/payments -> `security-privacy-reviewer`.
- UX/accessibility/copy/states -> `ux-product-reviewer`.
- Functional verify/manual QA/regression/risk -> `qa`.

## Model Choice

Choose by complexity: low -> fast capable; medium -> strong coding/reasoning; high -> strongest available. Record model/fallback only when useful.

## Permissions

- Read-only by default: BA, TL, QA, security, UX.
- Write-capable only with explicit ownership: Flutter, backend/API, DevOps.
- QA must not add test files unless the user asks for tests.
- Developers must not edit outside ownership without reporting why.

## Plan Before Operations

Every subagent starts with a short plan:

| Field | Plan |
|---|---|
| Goal | one sentence |
| Scope | owned files/folders or review area |
| Steps | max 3 |
| Verify | command/manual check |

## Execution

- Use one stable kebab-case `task-slug` for `reports/subagents/<task-slug>/` during the whole task.
- Flow: BA -> TL -> developer -> TL review -> developer revision -> QA.
- TL review: spec compliance first, code quality/architecture second.
- Repeat TL loop until accepted; stop after 3 rounds.
- Parallelize only independent work; prefer isolated/forked context.

## Gate Lite

Stop and route instead of guessing.

| Gate | Meaning | Action |
|---|---|---|
| `USER_DECISION` | User must choose direction/scope | Stop and ask. |
| `CLARIFICATION` | BA or TL can answer from existing context | Route to owner, then resume. |
| `REVIEW_CHANGES` | TL requires developer revision | Send exact changes to developer. |
| `BLOCKED` | Cannot proceed safely | Stop and report blocker. |
| `ACCEPTED` | Review passed | Continue to next step. |

Clarifications include owner, question, why blocked, options/default only when useful and safe.

## Task Breakdown

For larger work, TL may create:

| Task | Depends on | Owner | Requirement | Verification |
|---|---|---|---|---|
| T01 | none | role | R1 | command/manual check |

Keep slices reviewable. Parallelize only non-overlapping ownership.

## Harness Tools

Use `.agents/tools/` at checkpoints, not every turn.

| Checkpoint | Tool |
|---|---|
| Task start, project type unclear | `python .agents/tools/detect_project.py` |
| Before broad search or after map edits | `python .agents/tools/check_project_map.py` |
| After medium/large subagent run | `python .agents/tools/count_tokens.py --update --task "<task-slug>"` |
| Before compaction | `python .agents/tools/count_tokens.py --update --task "<task-slug>"` |

Keep output short. No install/network/destructive action without approval.

## Reports

Write reports under `reports/subagents/<task-slug>/`.

- `timeline.md`: time/order, role, action, decision, outcome.
- `<role>.md`; append `## Run N - <short reason>` for repeats.
- Table-based, under 80 lines.
- Omit files read unless essential evidence.
- Use `$caveman lite`.
- Use `$caveman full` for live progress/thinking updates; reports stay clear and table-based.

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
