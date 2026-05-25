---
name: caveman-compress
description: >
  Compress natural language Codex memory/instruction files (AGENTS.md, .agents/*.md,
  todos, preferences) into caveman format to save input tokens. Preserves technical
  substance, code, URLs, and structure. Compressed version overwrites the original file.
  Human-readable backup saved as FILE.original.md. Trigger: /caveman-compress FILEPATH
  or "compress memory file"
---

# Caveman Compress

## Purpose

Compress natural language Codex memory/instruction files (`AGENTS.md`, `.agents/*.md`, todos, preferences) into caveman-speak to reduce input tokens. Compressed version overwrites original. Human-readable backup saved as `<filename>.original.md`.

## Trigger

`/caveman-compress <filepath>` or when user asks to compress a memory file.

## Process

1. The compression scripts live in `scripts/` next to this `SKILL.md`.

2. From this skill directory, run:

```bash
python -m scripts <absolute_filepath>
```

3. The local CLI will:
- detect file type
- compress prose with deterministic local rules
- preserve code blocks, inline code, URLs, headings, paths, commands, and structure
- validate output
- restore the original and remove the backup if validation fails

4. Return result to user.

## Compression Rules

### Remove
- Articles when safe: a, an, the
- Filler: just, really, basically, actually, simply, essentially, generally
- Pleasantries: "sure", "certainly", "of course", "happy to", "I'd recommend"
- Hedging: "it might be worth", "you could consider", "it would be good to"
- Redundant phrasing: "in order to" -> "to", "make sure to" -> "ensure", "the reason is because" -> "because"
- Connective fluff: "however", "furthermore", "additionally", "in addition"

### Preserve Exactly
- Code blocks
- Inline code
- URLs and markdown links
- File paths
- Commands
- Technical terms
- Proper nouns
- Dates, versions, numeric values
- Environment variables

### Preserve Structure
- Markdown headings
- Bullet hierarchy
- Numbered lists
- Tables
- Frontmatter/YAML headers in markdown files

### Compress
- Use short synonyms: "big" not "extensive", "fix" not "implement a solution for", "use" not "utilize"
- Fragments OK: "Run tests before commit" not "You should always run tests before committing"
- Drop "you should", "make sure to", "remember to"; state action directly
- Merge redundant bullets when manually compressing
- Keep one example where multiple examples show the same pattern

## Boundaries

- Only compress natural language files (`.md`, `.txt`, `.typ`, `.typst`, `.tex`, extensionless)
- Never modify code/config/source files
- If file has mixed prose and code, compress only prose sections
- If unsure whether something is code or prose, leave it unchanged
- Original file is backed up as `FILE.original.md` before overwriting
- Never compress `FILE.original.md`
- This project-local copy is Codex-only and local-only: no external model API, no external agent CLI, no network
