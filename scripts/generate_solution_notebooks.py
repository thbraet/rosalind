#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "generated_solution_notebooks"
SKIP_DIRS = {
    "template_problem",
    "jupyter_templates",
    "tests",
    "rosalind",
    ".git",
    "__pycache__",
    "scripts",
    "functions",
}


def should_skip(relative_path: Path) -> bool:
    return any(part in SKIP_DIRS for part in relative_path.parts)


def is_problem_notebook(path: Path) -> bool:
    return path.with_suffix(".md").exists()


def discover_solution_notebooks() -> list[Path]:
    notebooks: list[Path] = []
    for notebook in ROOT.rglob("*.ipynb"):
        relative = notebook.relative_to(ROOT)
        if should_skip(relative):
            continue
        if notebook.parent == OUTPUT_DIR:
            continue
        if not is_problem_notebook(notebook):
            continue
        notebooks.append(notebook)
    return sorted(notebooks)


def build_output_path(source: Path) -> Path:
    relative = source.relative_to(ROOT)
    return OUTPUT_DIR / relative


def main() -> None:
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    notebooks = discover_solution_notebooks()
    generated: list[str] = []

    for source in notebooks:
        destination = build_output_path(source)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        generated.append(destination.relative_to(ROOT).as_posix())

    manifest = {
        "total_notebooks": len(generated),
        "source": "local repository problem notebooks (network access to rosalind.info unavailable in this environment)",
        "notebooks": generated,
    }

    manifest_path = OUTPUT_DIR / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print(f"Generated {len(generated)} notebooks into {OUTPUT_DIR.relative_to(ROOT)}")
    print(f"Manifest written to {manifest_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
