---
name: solid-oop-review
description: Review code for SOLID and OOP quality. Use for refactors, class design, service boundaries, dependency direction, responsibility splits, abstractions, coupling, and maintainability risks.
---

# SOLID OOP Review

Use project architecture first. Do not force textbook patterns where local style is simpler.

## Check

| Principle | Reject when |
|---|---|
| Single responsibility | One class/widget/service mixes orchestration, mapping, IO, policy, UI, and state |
| Open/closed | New variant requires editing many switch/if blocks across unrelated layers |
| Liskov | Subtype/implementation weakens expected behavior or throws unsupported surprises |
| Interface segregation | Callers depend on methods/data they do not need |
| Dependency inversion | High-level policy depends directly on low-level IO/framework details |
| Encapsulation | Mutable state, construction rules, or invariants leak outside owner |

## Output

Return only critical items:

| Decision | Design issue | Direction |
|---|---|---|
| accepted / needs revision / rejected | Concrete smell | Smallest project-compatible fix |

Do not recommend new packages, state managers, or architectures unless required.

## Project-Style Examples

| Principle | Signal | Direction |
|---|---|---|
| SRP | Cubit builds HTTP request, parses DTO, controls player, and renders policy | Split source factory/policy/service from state owner |
| OCP | New media type requires switches in UI, data, scheduler, and cache | Add project-compatible strategy/mapper at the boundary |
| LSP | Repository implementation returns partial model or throws for supported base contract method | Preserve contract or narrow the interface |
| ISP | Widget/service depends on a large manager only to call one method | Depend on smaller existing interface/callback |
| DIP | Domain/use case imports Flutter plugin, API client, or storage implementation | Depend on project abstraction and inject implementation |
| Encapsulation | Widget exposes mutable model and callers patch fields | Encapsulate mutation behind owner method or immutable state |
