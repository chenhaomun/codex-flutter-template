---
name: caveman-compress
description: >
  Compress natural-language memory files to save input tokens. Trigger:
  /caveman:compress FILEPATH or "compress memory file".
---

Run:

```sh
cd <this-skill-dir> && python3 -m scripts <absolute_filepath>
```

Rules:
- Only compress natural-language files: `.md`, `.txt`, `.typ`, `.typst`, `.tex`, extensionless.
- Never compress code/config/env/lock files.
- Preserve exactly: code blocks, inline code, URLs, paths, commands, technical terms, names, dates, numbers, env vars, headings, lists, tables, frontmatter.
- Compress prose only: remove filler/hedging/redundancy, use shorter words, merge duplicate points.
- CLI writes backup as `<file>.original.md`; never compress `.original.md`.
- If validation fails, report failure; do not hand-edit compressed output.
