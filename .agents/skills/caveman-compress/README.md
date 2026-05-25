# caveman-compress

Shrink Codex instruction files. Save context every session.

This project-local copy is Codex-only. It compresses natural-language memory files such as `AGENTS.md`, `.agents/*.md`, todos, and preferences into caveman format.

## What It Does

```text
/caveman-compress AGENTS.md
```

```text
AGENTS.md          <- compressed
AGENTS.original.md <- human-readable backup
```

Original content is backed up before overwrite. If validation fails, the original is restored and the backup is removed.

## Security

This copy is local-only:

- No external model API.
- No external agent CLI.
- No network calls.
- Refuses secret-looking filenames and private config paths.

See [SECURITY.md](./SECURITY.md).

## Usage

```text
/caveman-compress <filepath>
```

Examples:

```text
/caveman-compress AGENTS.md
/caveman-compress .agents/flutter-ai.md
/caveman-compress todos.md
```

## Files

| Type | Compress? |
|------|-----------|
| `.md`, `.txt`, `.rst`, `.typ`, `.typst`, `.tex` | Yes |
| Extensionless natural language | Yes |
| `.py`, `.js`, `.ts`, `.json`, `.yaml` | Skip |
| `*.original.md` | Skip |

## Flow

```text
detect file type
compress prose locally
validate headings, code blocks, URLs, file paths, bullets
write compressed file
write original backup
```

## Preserved

- Code blocks
- Inline code
- URLs and links
- File paths
- Commands
- Technical terms, library names, API names
- Headings
- Table structure
- Dates, versions, numeric values

## Notes

`caveman` controls response style. `caveman-compress` shrinks instruction files. Use both only where brevity helps; clarity wins when compression would hide meaning.
