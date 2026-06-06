---
name: kiss-review
description: Review code for KISS simplicity. Use for over-engineering, unnecessary abstraction, excessive indirection, clever code, avoidable complexity, broad patterns, or implementations larger than the requirement needs.
---

# KISS Review

Use project architecture first. Prefer the simplest implementation that satisfies the requirement, preserves correctness, and fits existing conventions.

## Check

| Principle | Reject when |
|---|---|
| Minimal abstraction | New layer, helper, base class, mixin, service, package, or pattern adds no clear current value |
| Straight control flow | Async flow, state transitions, or branching are harder to follow than the requirement needs |
| Locality | Reader must jump through unrelated files to understand simple behavior |
| Clear syntax | Clever syntax hides business behavior, lifecycle constraints, or error handling |
| Scope discipline | Implementation solves future/general cases not required by the task |
| Operational simplicity | Added config, generated code, tooling, or setup increases maintenance without need |

## Output

Return only critical items:

| Decision | Complexity issue | Direction |
|---|---|---|
| accepted / needs revision / rejected | Concrete over-complexity risk | Smallest project-compatible simplification |

Do not flatten necessary architecture, safety checks, or platform handling just to reduce lines.

## Project-Style Examples

| Principle | Signal | Direction |
|---|---|---|
| Minimal abstraction | One-off helper class wraps a single function with no state | Inline or use a small function in the owner file |
| Straight control flow | Nested futures/streams obscure loading/error transitions | Use existing bloc/cubit pattern with explicit states |
| Locality | Simple widget action routes through unrelated service registry | Call existing nearby owner/callback |
| Scope discipline | Feature adds generic plugin system for one variant | Implement current variant with extension point only if needed |
