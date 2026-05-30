# Skill Maintenance

Keep project-local skills current like vendored dependencies. Refresh them separately from app changes, review diffs, then commit the skill update on its own.

## Refresh Cadence

- Monthly.
- Before major Flutter or Dart upgrades.
- When a skill bug, stale recommendation, or missing workflow is suspected.

## Official Flutter and Dart Skills

macOS/Linux:

```sh
npx skills add flutter/skills --skill '*' --agent universal
npx skills add dart-lang/skills --skill '*' --agent universal
```

Windows PowerShell:

```powershell
npx.cmd skills add flutter/skills --skill '*' --agent universal
npx.cmd skills add dart-lang/skills --skill '*' --agent universal
```

## Official Flutter AI Rules

Review [Flutter AI rules](https://docs.flutter.dev/ai/ai-rules) during refreshes. Selectively merge portable guardrails into `AGENTS.md`; do not copy defaults that conflict with existing project architecture, packages, routing, or state management.

## Caveman Skills

macOS/Linux:

```sh
npx skills add JuliusBrussee/caveman --skill caveman --agent universal
npx skills add JuliusBrussee/caveman --skill caveman-compress --agent universal
```

Windows PowerShell:

```powershell
npx.cmd skills add JuliusBrussee/caveman --skill caveman --agent universal
npx.cmd skills add JuliusBrussee/caveman --skill caveman-compress --agent universal
```

`caveman-compress` is project-adapted for Codex-only/local-only use. After upstream refresh, re-check it has no external model API, external agent CLI, or network path before committing.

If the CLI refuses because a skill already exists, reinstall only that skill after backing up or reviewing local changes.

## Review

```sh
git diff -- .agents/skills skills-lock.json
```

Review every changed `SKILL.md` before relying on updated behavior. Pay extra attention to skills that can change dependencies, package choices, architecture, test generation, command execution, or bundled scripts.

Review installer security-risk flags and investigate any high-risk skill before use. Check unexpected lock-hash-only churn against the actual skill diff.

Restart Codex after skill changes so new skill metadata is loaded.
