#!/usr/bin/env python3
"""
Caveman memory compression orchestrator.

Usage:
    python3 scripts/compress.py <filepath>
"""

import re
from pathlib import Path

OUTER_FENCE_REGEX = re.compile(
    r"\A\s*(`{3,}|~{3,})[^\n]*\n(.*)\n\1\s*\Z", re.DOTALL
)

SENSITIVE_BASENAME_REGEX = re.compile(
    r"(?ix)^("
    r"\.env(\..+)?"
    r"|\.netrc"
    r"|credentials(\..+)?"
    r"|secrets?(\..+)?"
    r"|passwords?(\..+)?"
    r"|id_(rsa|dsa|ecdsa|ed25519)(\.pub)?"
    r"|authorized_keys"
    r"|known_hosts"
    r"|.*\.(pem|key|p12|pfx|crt|cer|jks|keystore|asc|gpg)"
    r")$"
)

SENSITIVE_PATH_COMPONENTS = frozenset({".ssh", ".aws", ".gnupg", ".kube", ".docker"})

SENSITIVE_NAME_TOKENS = (
    "secret",
    "credential",
    "password",
    "passwd",
    "apikey",
    "accesskey",
    "token",
    "privatekey",
)

PHRASE_REPLACEMENTS = (
    (r"\bin order to\b", "to"),
    (r"\bmake sure to\b", ""),
    (r"\byou should\b", ""),
    (r"\byou must\b", ""),
    (r"\bit is important to\b", ""),
    (r"\bit's important to\b", ""),
    (r"\bit would be good to\b", ""),
    (r"\bit might be worth\b", ""),
    (r"\byou could consider\b", "consider"),
    (r"\bthe reason is because\b", "because"),
    (r"\butilize\b", "use"),
    (r"\bimplement a solution for\b", "fix"),
)

DROP_WORDS = {
    "just",
    "really",
    "basically",
    "actually",
    "simply",
    "essentially",
    "generally",
    "however",
    "furthermore",
    "additionally",
}

from .detect import should_compress
from .validate import validate


def is_sensitive_path(filepath: Path) -> bool:
    """Heuristic denylist for files that must never be compressed."""
    name = filepath.name
    if SENSITIVE_BASENAME_REGEX.match(name):
        return True
    lowered_parts = {p.lower() for p in filepath.parts}
    if lowered_parts & SENSITIVE_PATH_COMPONENTS:
        return True
    lower = re.sub(r"[_\-\s.]", "", name.lower())
    return any(tok in lower for tok in SENSITIVE_NAME_TOKENS)


def strip_llm_wrapper(text: str) -> str:
    """Strip outer markdown fence when it wraps the entire output."""
    match = OUTER_FENCE_REGEX.match(text)
    if match:
        return match.group(2)
    return text


def compress_sentence(text: str) -> str:
    if not text.strip():
        return text

    protected: list[str] = []

    def protect(match: re.Match[str]) -> str:
        protected.append(match.group(0))
        return f"@@CAVEMAN_PROTECTED_{len(protected) - 1}@@"

    result = re.sub(r"`[^`]*`|https?://\S+|\[[^\]]+\]\([^)]+\)", protect, text)
    for pattern, replacement in PHRASE_REPLACEMENTS:
        result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)

    words = []
    for word in result.split():
        stripped = re.sub(r"^[^\w@]+|[^\w@]+$", "", word).lower()
        if stripped in DROP_WORDS:
            continue
        words.append(word)

    result = " ".join(words)
    result = re.sub(r"\s+([,.;:!?])", r"\1", result)
    result = re.sub(r"\s{2,}", " ", result).strip()

    for index, value in enumerate(protected):
        result = result.replace(f"@@CAVEMAN_PROTECTED_{index}@@", value)
    return result


def compress_markdown(original: str) -> str:
    lines = original.splitlines()
    compressed_lines = []
    in_fence = False

    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            compressed_lines.append(line)
            continue

        if in_fence or stripped.startswith("#"):
            compressed_lines.append(line)
            continue

        match = re.match(r"^(\s*(?:[-*+]|\d+[.)])\s+)(.*)$", line)
        if match:
            compressed_lines.append(match.group(1) + compress_sentence(match.group(2)))
            continue

        if "|" in line and line.count("|") >= 2:
            cells = line.split("|")
            compressed_lines.append("|".join(compress_sentence(cell) for cell in cells))
            continue

        compressed_lines.append(compress_sentence(line))

    return "\n".join(compressed_lines) + ("\n" if original.endswith("\n") else "")


def compress_file(filepath: Path) -> bool:
    filepath = filepath.resolve()
    max_file_size = 500_000
    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    if filepath.stat().st_size > max_file_size:
        raise ValueError(f"File too large to compress safely (max 500KB): {filepath}")

    if is_sensitive_path(filepath):
        raise ValueError(
            f"Refusing to compress {filepath}: filename looks sensitive "
            "(credentials, keys, secrets, or known private paths). "
            "Rename the file if this is a false positive."
        )

    print(f"Processing: {filepath}")

    if not should_compress(filepath):
        print("Skipping (not natural language)")
        return False

    original_text = filepath.read_text(errors="ignore")
    backup_path = filepath.with_name(filepath.stem + ".original.md")

    if not original_text.strip():
        print("Refusing to compress: file is empty or whitespace-only.")
        return False

    if backup_path.exists():
        print(f"Backup file already exists: {backup_path}")
        print("The original backup may contain important content.")
        print("Aborting to prevent data loss. Remove or rename the backup file to proceed.")
        return False

    print("Compressing locally...")
    compressed = strip_llm_wrapper(compress_markdown(original_text))

    if not compressed.strip():
        print("Compression aborted: compressor returned empty output.")
        print("Original file untouched; no backup created.")
        return False

    if compressed.strip() == original_text.strip():
        print("Compression aborted: output is identical to input.")
        print("File may already be compact. Original file untouched; no backup created.")
        return False

    backup_path.write_text(original_text)
    backup_readback = backup_path.read_text(errors="ignore")
    if backup_readback != original_text:
        print(f"Backup write verification failed: {backup_path}")
        print("Aborting before touching input file.")
        try:
            backup_path.unlink()
        except OSError:
            pass
        return False

    filepath.write_text(compressed)

    result = validate(backup_path, filepath)
    if result.is_valid:
        print("Validation passed")
        return True

    print("Validation failed:")
    for err in result.errors:
        print(f"   - {err}")
    filepath.write_text(original_text)
    backup_path.unlink(missing_ok=True)
    print("Original restored")
    return False
