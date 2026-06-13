---
name: skill-maintenance
description: >
  Refresh and review project-local Codex skills. Use when the user asks to update,
  refresh, install, or keep Flutter/Dart/Caveman skills current, or asks to run
  skill maintenance for this template.
---

# Skill Maintenance

Keep skills current like vendored dependencies. Run only when the user invokes this skill.

## Refresh

Invocation is the command. Run the refresh batch immediately when this skill is loaded or mentioned. Do not reply "loaded", "awaiting command", or ask conversational confirmation first. Rely only on system approval prompts for network/install commands.

macOS/Linux:

```sh
npx skills add flutter/skills --skill '*' --agent universal
npx skills add dart-lang/skills --skill '*' --agent universal
npx skills add JuliusBrussee/caveman --skill caveman --agent universal
npx skills add JuliusBrussee/caveman --skill caveman-compress --agent universal
```

Windows PowerShell:

```powershell
npx.cmd skills add flutter/skills --skill '*' --agent universal
npx.cmd skills add dart-lang/skills --skill '*' --agent universal
npx.cmd skills add JuliusBrussee/caveman --skill caveman --agent universal
npx.cmd skills add JuliusBrussee/caveman --skill caveman-compress --agent universal
```

## Review

- Review `git diff -- .agents/skills skills-lock.json`.
- Review every changed `SKILL.md`.
- Investigate installer high-risk flags before use.
- Check unexpected lock-hash-only churn against actual skill diffs.
- Re-check `caveman-compress` stays local-only: no external model API, external agent CLI, or network path.
- Review Flutter AI rules: https://docs.flutter.dev/ai/ai-rules. Merge only portable guardrails into `AGENTS.md`; do not override project architecture/packages/routing/state.
- Do not commit automatically.
- Tell user to restart Codex after skill changes if metadata does not refresh.
