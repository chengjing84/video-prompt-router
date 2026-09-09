#!/usr/bin/env python3
"""Build a byte-level manifest from the bundled skill snapshot."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = Path.home() / ".codex" / "skills"
PACKAGES = (
    "video-prompt-router",
    "h3-prompt-writing",
    "anime-pv-i2va-generator",
    "seedance-20",
)


def main() -> None:
    records: list[dict[str, object]] = []
    skills: list[dict[str, str]] = []

    for package in PACKAGES:
        package_root = SOURCE_ROOT / package
        for source in sorted(package_root.rglob("*")):
            if not source.is_file():
                continue
            relative = source.relative_to(package_root)
            target_relative = relative if package == "video-prompt-router" else Path(package) / relative
            target = ROOT / target_relative
            data = source.read_bytes()
            if not target.is_file() or target.read_bytes() != data:
                raise RuntimeError(f"Bundled file differs from local source: {target_relative.as_posix()}")
            blob = b"blob " + str(len(data)).encode("ascii") + b"\0" + data
            records.append(
                {
                    "path": target_relative.as_posix(),
                    "source_package": package,
                    "bytes": len(data),
                    "sha256": hashlib.sha256(data).hexdigest(),
                    "git_blob_sha": hashlib.sha1(blob).hexdigest(),
                }
            )
            if source.name == "SKILL.md":
                match = re.search(r"^name:\s*([^\r\n]+)", data.decode("utf-8-sig"), re.MULTILINE)
                if match is None:
                    raise RuntimeError(f"Missing skill name: {source}")
                skills.append(
                    {
                        "name": match.group(1).strip().strip("\"'"),
                        "path": target_relative.as_posix(),
                    }
                )

    manifest = {
        "format_version": 1,
        "description": "Byte-exact snapshot of the router and its complete local dependency packages.",
        "files": sorted(records, key=lambda record: str(record["path"])),
        "skills": sorted(skills, key=lambda record: record["name"]),
    }
    (ROOT / "BUNDLE-MANIFEST.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(
        f"Snapshot: {len(records)} original files, {len(skills)} skill entrypoints, "
        f"{sum(int(record['bytes']) for record in records):,} bytes."
    )


if __name__ == "__main__":
    main()
