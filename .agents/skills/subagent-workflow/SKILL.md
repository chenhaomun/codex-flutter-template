---
name: subagent-workflow
description: >
  Subagent workflow rules. Use when asked to use subagents, route BA/TL/dev/QA,
  choose models, write reports, track token-heavy output, compact context, or manage
  multi-agent work.
---

Use only for medium, large, risky, or unclear work. Auto-use `grill-requirements` before planning when requirements are unclear, missing acceptance criteria, missing target flow/state, contradictory, or likely to cause rework.

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
- Developers may add/update scoped tests when behavior is clear and regression risk justifies TDD.

## Plan Before Operations

Every subagent starts with a short plan: goal, scope, max 3 steps, verification.

## Execution

- Use one stable kebab-case `task-slug` for `reports/subagents/<task-slug>/` during the whole task.
- Flow: choose tier first. Medium single-owner may use TL -> developer -> quick TL review. Large/risky uses BA -> TL -> developer -> developer self-check -> TL review -> developer revision -> QA.
- TL review: spec compliance first, code quality/architecture second.
- Repeat TL loop until accepted; stop after 3 rounds.
- Parallelize only independent work; prefer isolated/forked context.

## Production Bar

Developer cannot report `done` unless behavior matches requirements, diff is scoped, project conventions hold, relevant states are handled, verification ran or blocker is stated, and no debug/dead/TODO/generated-file churn remains.

Use focused skills for deeper checks: `test-driven-development`, `production-code-review`, `architecture-review`, `solid-oop-review`, `dry-review`, `kiss-review`, `security-review`, `performance-review`.

For large/risky or multi-agent work, TL runs final review before acceptance: accumulated changes, unresolved assumptions, verification, and relevant review-skill findings.

## Gate Lite

Stop and route instead of guessing.

Gates: `USER_DECISION` stop/ask; `CLARIFICATION` route to BA/TL; `REVIEW_CHANGES` send exact revision; `PRODUCTION_GAP` reject/revise; `BLOCKED` stop/report; `ACCEPTED` continue.

Clarifications include owner, question, why blocked, options/default only when useful and safe.

## Task Breakdown

For larger work, TL may create task rows with: task, dependency, owner, requirement, verification.

Prefer vertical slices that deliver reviewable behavior end-to-end. Use horizontal layer tasks only when dependency order requires it. Parallelize only non-overlapping ownership.

## Quality Tiers

| Tier | Use |
|---|---|
| Trivial | No subagent, no TDD/review skill |
| Small | Direct work + quick self-check |
| Medium single-owner | One developer, `production-code-review` only, max one specialist skill |
| Medium behavior risk | Add TDD only when focused test fits existing project |
| Large/risky/multi-agent | Full TL/dev/TL/QA loop and relevant specialist skills |

## Review Skills

| Skill | Use for |
|---|---|
| `production-code-review` | medium+ review |
| `grill-requirements` | unclear scope, missing acceptance, likely rework |
| `test-driven-development` | clear behavior changes with meaningful regression risk |
| `architecture-review` | boundaries, contracts, ownership, integration risk |
| `solid-oop-review` | class/refactor design, responsibility, coupling |
| `dry-review` | duplicated rules, mappings, setup, or drift-prone copy/paste |
| `kiss-review` | over-engineering, avoidable indirection, unnecessary abstraction |
| `security-review` | auth, privacy, permissions, secrets, network, dependency risk |
| `performance-review` | UI rebuilds, async work, rendering, memory, scaling |

Developer owns one bounded module or concern, reads nearby code/tests, states intended files before editing, and runs narrow verification after each slice. TL reviews actual diff, not reports only. Integrate after tier-matched review passes.

Typical Flutter slices: domain/contracts -> repository/API -> Bloc/Cubit -> UI -> routing/platform -> tests/regression.

## Harness Tools

Use `.agents/tools/` at checkpoints, not every turn. Use the available Python command for the local OS (`python`, `python3`, or bundled runtime).

| Checkpoint | Tool |
|---|---|
| Task start, project type unclear | `<python> .agents/tools/detect_project.py` |
| Project map missing/empty/stale | Preview with `<python> .agents/tools/generate_project_map.py`; update via `apply_patch` |
| Before broad search or after map edits | `<python> .agents/tools/check_project_map.py` |
| After medium/large subagent run | `<python> .agents/tools/count_tokens.py --update --task "<task-slug>"` |
| Before compaction | `<python> .agents/tools/count_tokens.py --update --task "<task-slug>"` |

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
