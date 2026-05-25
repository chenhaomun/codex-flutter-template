# Skill Maintenance

Keep project-local skills current like vendored dependencies. Refresh them separately from app changes, review diffs, then commit the skill update on its own.

## Refresh Cadence

- Monthly.
- Before major Flutter or Dart upgrades.
- When a skill bug, stale recommendation, or missing workflow is suspected.

## Official Flutter and Dart Skills

```powershell
npx.cmd skills add flutter/skills --skill '*' --agent universal
npx.cmd skills add dart-lang/skills --skill '*' --agent universal
```

## Caveman Skills

```powershell
npx.cmd skills add JuliusBrussee/caveman --skill caveman --agent universal
npx.cmd skills add JuliusBrussee/caveman --skill caveman-compress --agent universal
```

`caveman-compress` is project-adapted for Codex-only/local-only use. After upstream refresh, re-check it has no external model API, external agent CLI, or network path before committing.

If the CLI refuses because a skill already exists, reinstall only that skill after backing up or reviewing local changes.

## Review

```powershell
git diff -- .agents/skills skills-lock.json
```

Review every changed `SKILL.md` before relying on updated behavior. Pay extra attention to skills that can change dependencies, package choices, architecture, test generation, command execution, or bundled scripts.

Restart Codex after skill changes so new skill metadata is loaded.
