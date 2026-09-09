#!/usr/bin/env python3
"""Verify the complete video-prompt skill snapshot without modifying files."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[1]
PACKAGES = ("h3-prompt-writing", "anime-pv-i2va-generator", "seedance-20")


def main() -> int:
    manifest = json.loads((ROOT / "BUNDLE-MANIFEST.json").read_text(encoding="utf-8"))
    errors: list[str] = []
    expected: set[str] = set()
    for record in manifest["files"]:
        relative = record["path"]
        normalized = PurePosixPath(relative)
        if normalized.is_absolute() or ".." in normalized.parts or "\\" in relative:
            errors.append(f"Invalid manifest path: {relative}")
            continue
        if relative in expected:
            errors.append(f"Duplicate manifest path: {relative}")
        expected.add(relative)
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"Missing file: {relative}")
            continue
        data = path.read_bytes()
        blob = b"blob " + str(len(data)).encode("ascii") + b"\0" + data
        if (
            len(data) != record["bytes"]
            or hashlib.sha256(data).hexdigest() != record["sha256"]
            or hashlib.sha1(blob).hexdigest() != record["git_blob_sha"]
        ):
            errors.append(f"Changed file: {relative}")

    actual = {"SKILL.md"} if (ROOT / "SKILL.md").is_file() else set()
    for package in PACKAGES:
        actual.update(
            path.relative_to(ROOT).as_posix()
            for path in (ROOT / package).rglob("*")
            if path.is_file()
            and "__pycache__" not in path.parts
            and ".pytest_cache" not in path.parts
            and path.suffix not in {".pyc", ".pyo"}
        )
    for relative in sorted(actual - expected):
        errors.append(f"Unlisted file: {relative}")

    skill_names: set[str] = set()
    for entry in manifest["skills"]:
        path = ROOT / entry["path"]
        if not path.is_file():
            errors.append(f"Missing skill: {entry['name']}")
            continue
        text = path.read_text(encoding="utf-8-sig")
        match = re.search(r"^name:\s*([^\r\n]+)", text, re.MULTILINE)
        if match is None or match.group(1).strip().strip("\"'") != entry["name"]:
            errors.append(f"Skill name mismatch: {entry['path']}")
        skill_names.add(entry["name"])

    router = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    routes = set(re.findall(r"\|\s*`([^`]+)`\s*\|", router))
    for name in sorted(routes - skill_names):
        errors.append(f"Missing router dependency: {name}")
    if len(routes) != 12:
        errors.append(f"Expected 12 direct router dependencies, found {len(routes)}")
    discovered_skills = {relative for relative in expected if relative.endswith("SKILL.md")}
    if discovered_skills != {entry["path"] for entry in manifest["skills"]}:
        errors.append("Skill inventory does not match the snapshot")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(
        f"PASS: {len(expected)} original files match; "
        f"{len(skill_names)} skill entrypoints and {len(routes)} router dependencies exist."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
