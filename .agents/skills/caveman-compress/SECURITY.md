# Security

This project-local copy is Codex-only and local-only.

- No external model API usage.
- No external agent CLI fallback.
- No network calls.
- Refuses filenames and paths that look like secrets, credentials, keys, or private config.
- Backs up the original as `FILE.original.md` before overwriting.
- Restores the original and removes the backup if validation fails.

Only run this on natural-language instruction files such as `AGENTS.md`, `.agents/*.md`, todos, and preferences.
