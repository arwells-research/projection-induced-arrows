#!/usr/bin/env python3
"""
Normalize hidden/Unicode hyphenation artifacts in LaTeX sources.

Typical symptom: words like "micro￾scopic" in the rendered PDF text extraction.
Cause: soft hyphen / discretionary hyphen / zero-width characters in .tex.

This script:
- Replaces common Unicode hyphen/dash variants with ASCII '-'
- Removes invisible joiners/ZW spaces that break copy/paste/search
- Optionally converts SOFT HYPHEN (U+00AD) to '-' or removes it

Usage:
  python tools/normalize_hyphens.py --root sections --ext .tex
  python tools/normalize_hyphens.py --root . --ext .tex --dry-run
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path

# Characters to convert to a normal hyphen
TO_ASCII_HYPHEN = {
    "\u2010",  # hyphen
    "\u2011",  # non-breaking hyphen
    "\u2012",  # figure dash
    "\u2013",  # en dash
    "\u2014",  # em dash
    "\u2212",  # minus sign
    "\ufe63",  # small hyphen-minus
    "\uff0d",  # fullwidth hyphen-minus
}

# Characters that should be removed entirely (they create invisible breaks/joining)
REMOVE = {
    "\u200b",  # zero width space
    "\u200c",  # zero width non-joiner
    "\u200d",  # zero width joiner
    "\u2060",  # word joiner
    "\ufeff",  # zero width no-break space (BOM)
}

SOFT_HYPHEN = "\u00ad"  # discretionary / soft hyphen

def normalize_text(s: str, soft_hyphen_mode: str) -> tuple[str, dict[str, int]]:
    """
    soft_hyphen_mode:
      - "hyphen": replace U+00AD with '-'
      - "remove": drop U+00AD entirely
    """
    counts: dict[str, int] = {}

    def bump(ch: str):
        counts[ch] = counts.get(ch, 0) + 1

    out = []
    for ch in s:
        if ch in TO_ASCII_HYPHEN:
            bump(ch)
            out.append("-")
        elif ch in REMOVE:
            bump(ch)
            # drop
        elif ch == SOFT_HYPHEN:
            bump(ch)
            if soft_hyphen_mode == "hyphen":
                out.append("-")
            else:
                # remove
                pass
        else:
            out.append(ch)

    return "".join(out), counts


def iter_files(root: Path, ext: str) -> list[Path]:
    files: list[Path] = []
    for p in root.rglob(f"*{ext}"):
        if p.is_file():
            files.append(p)
    return files


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="Root directory to scan (default: .)")
    ap.add_argument("--ext", default=".tex", help="File extension to process (default: .tex)")
    ap.add_argument("--soft-hyphen", choices=["hyphen", "remove"], default="hyphen",
                    help="How to handle U+00AD soft hyphen (default: hyphen)")
    ap.add_argument("--dry-run", action="store_true", help="Do not modify files; just report")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    files = iter_files(root, args.ext)

    if not files:
        print(f"No *{args.ext} files found under {root}")
        return 0

    total_changed = 0
    total_hits: dict[str, int] = {}

    for f in files:
        data = f.read_text(encoding="utf-8", errors="strict")
        new, counts = normalize_text(data, args.soft_hyphen)

        if new != data:
            total_changed += 1
            print(f"[CHANGED] {f}")
            # merge counts
            for ch, n in counts.items():
                total_hits[ch] = total_hits.get(ch, 0) + n

            if not args.dry_run:
                # write back safely
                tmp = f.with_suffix(f.suffix + ".tmp")
                tmp.write_text(new, encoding="utf-8", errors="strict")
                os.replace(tmp, f)
        else:
            # still count occurrences if desired; here we don't
            pass

    print("\nSummary:")
    print(f"  Files scanned:   {len(files)}")
    print(f"  Files modified:  {total_changed}")
    if total_hits:
        print("  Replacements/removals:")
        for ch, n in sorted(total_hits.items(), key=lambda kv: (-kv[1], kv[0])):
            code = f"U+{ord(ch):04X}"
            # show printable hint
            hint = ch if ch not in REMOVE and ch != SOFT_HYPHEN else ""
            label = "SOFT_HYPHEN" if ch == SOFT_HYPHEN else ("REMOVED" if ch in REMOVE else "DASH/HYPHEN")
            print(f"    {code:<8} {label:<11} count={n}")
    else:
        print("  No normalization needed.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())