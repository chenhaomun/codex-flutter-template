---
name: performance-review
description: Review code for performance risks. Use for Flutter UI rebuilds, scrolling, async work, parsing, caching, memory, startup, network calls, expensive loops, rendering, and responsiveness.
---

# Performance Review

Focus on user-visible slowness, jank, unnecessary work, and scaling risks.

## Check

| Area | Reject when |
|---|---|
| Flutter rebuilds | Expensive work happens in `build()`, broad listeners rebuild large subtrees, or const/lazy widgets are missed |
| Lists/rendering | Large collections use eager widgets, unstable keys, image misuse, or layout work that can overflow/jank |
| Async/IO | Network, disk, parsing, or heavy compute blocks UI or lacks timeout/cancel/error path |
| State churn | State updates are too broad, repeated, leaked, or triggered during lifecycle incorrectly |
| Memory | Controllers, streams, subscriptions, caches, images, or isolates can leak or grow unbounded |
| Data processing | Repeated mapping/filtering/sorting/parsing should be cached, paged, streamed, or offloaded |
| Startup | Feature adds synchronous startup work or blocks first usable screen |

## Output

| Severity | Performance risk | Required action |
|---|---|---|
| P1/P2/P3 | Concrete slow path | Smallest measurable fix or verification |

Do not optimize prematurely; reject only plausible production risks.

## Examples

| Signal | Required action |
|---|---|
| Sorting/filtering large list in `build()` | Precompute, memoize, move to state layer, or lazy page |
| Network call starts on every rebuild | Start once in lifecycle/state owner |
| Stream/controller not disposed | Dispose or bind lifecycle to existing owner |
