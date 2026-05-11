# Project Map

Use this map before broad searches. If user mentions a known area, start with its folders and nearby tests.

Codex maintains this file. When this file is empty, stale, or missing a requested area, inspect the repo and update the map.

## Areas

No areas mapped yet.

Expected format:

```text
- area-name
  - folders: lib/features/example, test/features/example
  - terms: example, sample, alias
  - notes: state/routing/API ownership if useful
```

## Rules

- Keep area names stable and lowercase.
- Store folders, not exact file paths, unless one file is the whole area.
- Prefer the nearest stable parent folder that helps locate code quickly.
- Include test folders beside source folders when known.
- Generate real project folders from repo inspection after copying this template.
- Update this file when modules move, new major areas appear, or user terms do not map cleanly.
- If a folder is missing or stale, fall back to `rg` and update the map.
