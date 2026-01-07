#!/usr/bin/env python3
"""
Basic structural linter for Kumu blueprint-style JSON files.

Validates essential schema properties:
* Top-level object with `elements` and `connections` arrays.
* Each element has unique `_id`, string label, and attribute dictionary.
* Each connection has unique `_id`, references existing element ids,
  and uses supported direction/delayed/reversed fields.
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Set, Optional
import subprocess

SUPPORTED_DIRECTIONS = {"directed", "undirected", "mutual"}


@dataclass
class LintResult:
    path: Path
    errors: List[str]

    @property
    def ok(self) -> bool:
        return not self.errors


def load_json(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON: {exc}") from exc


def ensure_dict(value: Any, context: str) -> Dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError(f"{context} must be an object, got {type(value).__name__}")
    return value


def get_base_element_ids(path: Path) -> Optional[Set[str]]:
    """Return set of element ids from origin/main for the given file, or None if unavailable."""
    repo_root = Path(__file__).resolve().parents[1]
    try:
        rel = path.resolve().relative_to(repo_root)
    except Exception:
        rel = path
    git_arg = f"origin/main:{rel.as_posix()}"
    try:
        # Ensure subprocess output is decoded as UTF-8 to avoid platform-specific
        # decoding errors when reading git output on Windows (cp1252 default).
        proc = subprocess.run(
            ["git", "show", git_arg],
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        try:
            data = json.loads(proc.stdout)
        except json.JSONDecodeError:
            # If decoding produced replacement characters and JSON fails,
            # fall back to returning None to allow lint to continue.
            return None
        elements = data.get("elements", [])
        return {e.get("_id") for e in elements if isinstance(e, dict) and isinstance(e.get("_id"), str)}
    except Exception:
        return None


def lint_blueprint(path: Path, require_metrics_for_new: bool = False) -> LintResult:
    errors: List[str] = []

    try:
        data = load_json(path)
    except ValueError as exc:
        return LintResult(path, [str(exc)])

    if not isinstance(data, dict):
        return LintResult(path, [f"Top-level JSON must be an object, got {type(data).__name__}"])

    elements = data.get("elements")
    if not isinstance(elements, list):
        errors.append("Missing or invalid `elements` array.")
        elements = []

    connections = data.get("connections")
    if not isinstance(connections, list):
        errors.append("Missing or invalid `connections` array.")
        connections = []

    element_ids: Set[str] = set()
    for index, raw_element in enumerate(elements):
        prefix = f"elements[{index}]"
        if not isinstance(raw_element, dict):
            errors.append(f"{prefix}: must be an object.")
            continue

        elem_id = raw_element.get("_id")
        if not isinstance(elem_id, str) or not elem_id.strip():
            errors.append(f"{prefix}._id must be a non-empty string.")
            continue
        if elem_id in element_ids:
            errors.append(f"{prefix}._id '{elem_id}' is duplicated.")
        element_ids.add(elem_id)

        attributes = raw_element.get("attributes")
        if not isinstance(attributes, dict):
            errors.append(f"{prefix}.attributes must be an object.")
        else:
            label = attributes.get("label")
            if not isinstance(label, str) or not label.strip():
                errors.append(f"{prefix}.attributes.label must be a non-empty string.")

    # If requested, determine base element ids to detect newly added elements
    base_ids: Optional[Set[str]] = None
    if require_metrics_for_new:
        base_ids = get_base_element_ids(path)
        if base_ids is None:
            errors.append("Warning: could not fetch origin/main version to determine new elements; skipping new-element metric checks.")
    # If base_ids is available, check newly added elements for required metrics
    if base_ids is not None:
        for index, raw_element in enumerate(elements):
            if not isinstance(raw_element, dict):
                continue
            elem_id = raw_element.get("_id")
            if not isinstance(elem_id, str):
                continue
            if elem_id in base_ids:
                continue
            attributes = raw_element.get("attributes")
            if not isinstance(attributes, dict):
                continue
            meas = attributes.get("measurability")
            infl = attributes.get("influenceability")
            missing = []
            if meas is None:
                missing.append("measurability")
            if infl is None:
                missing.append("influenceability")
            if missing:
                errors.append(
                    f"New element '{elem_id}' missing fields: {', '.join(missing)}. "
                    + "Add values (0/0.5/1) or include 'MISSING_METRICS: measurability=<value_or_NULL>, influenceability=<value_or_NULL>' in the PR description."
                )

    connection_ids: Set[str] = set()
    for index, raw_connection in enumerate(connections):
        prefix = f"connections[{index}]"
        if not isinstance(raw_connection, dict):
            errors.append(f"{prefix}: must be an object.")
            continue

        conn_id = raw_connection.get("_id")
        if not isinstance(conn_id, str) or not conn_id.strip():
            errors.append(f"{prefix}._id must be a non-empty string.")
            continue
        if conn_id in connection_ids:
            errors.append(f"{prefix}._id '{conn_id}' is duplicated.")
        connection_ids.add(conn_id)

        for field in ("from", "to"):
            value = raw_connection.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{prefix}.{field} must be a non-empty string.")
            elif value not in element_ids:
                errors.append(f"{prefix}.{field} references unknown element id '{value}'.")

        direction = raw_connection.get("direction")
        if direction is not None:
            if direction not in SUPPORTED_DIRECTIONS:
                errors.append(
                    f"{prefix}.direction must be one of {sorted(SUPPORTED_DIRECTIONS)}, got '{direction}'."
                )

        for flag in ("delayed", "reversed"):
            value = raw_connection.get(flag)
            if value is not None and not isinstance(value, bool):
                errors.append(f"{prefix}.{flag} must be boolean if provided.")

        attributes = raw_connection.get("attributes")
        if attributes is not None and not isinstance(attributes, dict):
            errors.append(f"{prefix}.attributes must be an object when present.")

    return LintResult(path, errors)


def collect_blueprint_files(paths: Sequence[str]) -> List[Path]:
    if paths:
        targets = [Path(p) for p in paths]
    else:
        # Default to repo-relative models directory.
        repo_root = Path(__file__).resolve().parents[1]
        default_dir = repo_root / "models"
        targets = [default_dir]

    files: List[Path] = []
    missing: List[Path] = []

    for target in targets:
        if target.is_dir():
            files.extend(sorted(p for p in target.rglob("*.json") if p.is_file()))
        elif target.is_file():
            files.append(target)
        else:
            missing.append(target)

    if missing:
        missing_paths = ", ".join(str(p) for p in missing)
        raise ValueError(f"Targets not found: {missing_paths}")

    if not files:
        root_list = ", ".join(str(t) for t in targets)
        raise ValueError(f"No blueprint JSON files found under: {root_list}")

    return files


def parse_args(argv: Iterable[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate basic syntax and structure of Kumu blueprint JSON files."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="Blueprint JSON files or directories to lint (defaults to ./models).",
    )
    parser.add_argument(
        "--require-metrics-for-new",
        action="store_true",
        help="When set, check newly added elements (vs origin/main) have measurability/influenceability defined.",
    )
    return parser.parse_args(argv)


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    try:
        blueprint_files = collect_blueprint_files(args.paths)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2

    results = [lint_blueprint(path, require_metrics_for_new=args.require_metrics_for_new) for path in blueprint_files]

    had_error = False
    for result in results:
        if result.ok:
            print(f"OK   {result.path}")
        else:
            had_error = True
            print(f"FAIL {result.path}")
            for msg in result.errors:
                print(f"  - {msg}")

    return 1 if had_error else 0


if __name__ == "__main__":
    sys.exit(main())
