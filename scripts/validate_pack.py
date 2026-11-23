#!/usr/bin/env python3
"""Basic no-dependency validation for a generated documentary pack."""
from pathlib import Path
import sys

path = Path(sys.argv[1] if len(sys.argv) > 1 else "episode-pack.md")
if not path.is_file():
    raise SystemExit(f"Missing output file: {path}")

content = path.read_text(encoding="utf-8")
required = [
    "Episode premise", "Title options", "Cold open", "Timed structure",
    "Full narration script", "Research ledger", "Uncertainty register",
    "Visual storyboard", "Thumbnail brief", "YouTube metadata", "Quality check",
]
missing = [heading for heading in required if heading.lower() not in content.lower()]
if missing:
    raise SystemExit("Pack is incomplete; missing: " + ", ".join(missing))

words = len(content.split())
if words < 1200:
    raise SystemExit(f"Pack looks too short ({words} words); review generation.")
print(f"Structure passed ({words} words). Human fact-check and editorial review remain required.")
