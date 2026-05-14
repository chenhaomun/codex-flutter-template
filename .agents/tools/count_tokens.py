#!/usr/bin/env python3
"""Approximate guidance/report token pressure with word and character counts."""

from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path.cwd()
REPORT = ROOT / ".agents" / "guidance-token-report.md"


def word_count(text: str) -> int:
    return len(text.split())


def size_for(paths: list[Path]) -> tuple[int, int]:
    words = 0
    chars = 0
    for path in paths:
        if not path.exists() or not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        words += word_count(text)
        chars += len(text)
    return words, chars


def guidance_paths() -> list[Path]:
    paths = [ROOT / "AGENTS.md", ROOT / ".agents" / "project-map.md"]
    subagents_dir = ROOT / ".agents" / "subagents"
    paths += sorted(subagents_dir.glob("*.md")) if subagents_dir.exists() else []
    paths += sorted((ROOT / ".agents" / "skills").glob("*/SKILL.md"))
    return paths


def report_paths() -> list[Path]:
    reports = ROOT / "reports"
    return sorted(reports.rglob("*.md")) if reports.exists() else []


def risk(words: int) -> str:
    if words >= 3000:
        return "High"
    if words >= 1000:
        return "Medium"
    return "Low"


def live_row(task: str, source: str, words: int, chars: int) -> str:
    return f"| {task} | {source} | {words} words / {chars} chars | {risk(words)} | Review if growing. |"


def append_live_row(task: str, source: str, words: int, chars: int) -> bool:
    row = live_row(task, source, words, chars)
    if not REPORT.exists():
        REPORT.parent.mkdir(parents=True, exist_ok=True)
        REPORT.write_text("# Guidance Token Report\n\n## Live Run Log\n\n| Task | Source | Approx size | Risk | Action |\n|---|---|---:|---|---|\n", encoding="utf-8")

    text = REPORT.read_text(encoding="utf-8", errors="ignore")
    marker = "## Live Run Log"
    if marker not in text:
        text += "\n## Live Run Log\n\n| Task | Source | Approx size | Risk | Action |\n|---|---|---:|---|---|\n"
    text += row + "\n"
    try:
        REPORT.write_text(text, encoding="utf-8")
        return True
    except OSError:
        print("update blocked; append this row manually:")
        print(row)
        return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Approximate token pressure.")
    parser.add_argument("--update", action="store_true", help="Append a live row to .agents/guidance-token-report.md.")
    parser.add_argument("--task", default="manual", help="Task label for --update.")
    args = parser.parse_args()

    guidance_words, guidance_chars = size_for(guidance_paths())
    reports_words, reports_chars = size_for(report_paths())
    total_words = guidance_words + reports_words
    total_chars = guidance_chars + reports_chars

    print(f"guidance: {guidance_words} words / {guidance_chars} chars / {risk(guidance_words)}")
    print(f"reports: {reports_words} words / {reports_chars} chars / {risk(reports_words)}")
    print(f"total: {total_words} words / {total_chars} chars / {risk(total_words)}")

    if args.update:
        if append_live_row(args.task, "guidance+reports", total_words, total_chars):
            print("updated: .agents/guidance-token-report.md")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
