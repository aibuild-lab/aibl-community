#!/usr/bin/env python3
"""Dependency-free structural validation for the AIBL community catalog."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
VERSION_PATTERN = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
SHA256_PATTERN = re.compile(r"^[a-f0-9]{64}$")
WORKFLOW_XRAY_FILES = (
    "README.md",
    "lesson.md",
    "example.md",
    "prompt.md",
    "skill/SKILL.md",
)
WORKFLOW_XRAY_FETCH_URLS = {
    "https://raw.githubusercontent.com/aibuild-lab/aibl-community/main/"
    "kits/workflow-xray/manifest.json",
    "https://raw.githubusercontent.com/aibuild-lab/aibl-community/main/"
    "kits/workflow-xray/lesson.md",
    "https://raw.githubusercontent.com/aibuild-lab/aibl-community/main/"
    "kits/workflow-xray/example.md",
    "https://raw.githubusercontent.com/aibuild-lab/aibl-community/main/"
    "kits/workflow-xray/skill/SKILL.md",
}
FORBIDDEN_TEXT = (
    "/" + "Users" + "/",
    "file:" + "//",
    "BEGIN " + "PRIVATE KEY",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"catalog_error: {message}")


def main() -> None:
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    require(set(catalog) == {"$schema", "catalog_version", "items"}, "catalog keys")
    require(catalog["catalog_version"] == "1", "catalog version")
    require(isinstance(catalog["items"], list) and catalog["items"], "catalog items")

    identifiers: set[str] = set()
    for item in catalog["items"]:
        identifier = item.get("id")
        require(
            isinstance(identifier, str) and bool(ID_PATTERN.fullmatch(identifier)),
            "item id",
        )
        require(identifier not in identifiers, f"duplicate item: {identifier}")
        identifiers.add(identifier)
        require(item.get("status") in {"stable", "retired"}, f"status: {identifier}")
        if item.get("kind") == "kit":
            require(
                set(item)
                == {"description", "id", "kind", "license", "path", "status", "version"},
                f"kit fields: {identifier}",
            )
            require(
                bool(VERSION_PATTERN.fullmatch(item["version"])),
                f"version: {identifier}",
            )
            path = ROOT / item["path"]
            require(
                path.is_file() and path.name == "README.md",
                f"kit path: {identifier}",
            )
            kit_root = path.parent
            if identifier == "workflow-xray":
                for required in (*WORKFLOW_XRAY_FILES, "manifest.json"):
                    require(
                        (kit_root / required).is_file(),
                        f"kit file: {identifier}/{required}",
                    )
                require(
                    not (kit_root / "scripts").exists(),
                    "workflow-xray must remain instruction-only",
                )
                manifest = json.loads(
                    (kit_root / "manifest.json").read_text(encoding="utf-8")
                )
                require(
                    set(manifest)
                    == {
                        "schema_version",
                        "id",
                        "name",
                        "version",
                        "license",
                        "publisher",
                        "source",
                        "compatibility",
                        "hash_scope",
                        "declared_files",
                    },
                    "workflow-xray manifest fields",
                )
                require(manifest["schema_version"] == "1", "manifest schema")
                require(manifest["id"] == identifier, "manifest id")
                require(manifest["version"] == item["version"], "manifest version")
                require(manifest["license"] == item["license"], "manifest license")
                require(
                    isinstance(manifest["compatibility"], list)
                    and set(manifest["compatibility"])
                    == {"codex", "claude-code", "portable-markdown"},
                    "manifest compatibility",
                )
                declared = manifest["declared_files"]
                require(isinstance(declared, list), "manifest declared files")
                require(
                    {entry.get("path") for entry in declared}
                    == set(WORKFLOW_XRAY_FILES),
                    "manifest declared file set",
                )
                for entry in declared:
                    require(
                        set(entry) == {"path", "media_type", "sha256"},
                        f"manifest file fields: {entry.get('path')}",
                    )
                    require(
                        isinstance(entry["sha256"], str)
                        and bool(SHA256_PATTERN.fullmatch(entry["sha256"])),
                        f"manifest hash shape: {entry['path']}",
                    )
                    content = (kit_root / entry["path"]).read_bytes()
                    require(
                        hashlib.sha256(content).hexdigest() == entry["sha256"],
                        f"manifest hash mismatch: {entry['path']}",
                    )
                prompt = (kit_root / "prompt.md").read_text(encoding="utf-8")
                for source_url in WORKFLOW_XRAY_FETCH_URLS:
                    require(
                        source_url in prompt,
                        f"workflow-xray prompt source: {source_url}",
                    )
        elif item.get("kind") == "skill":
            require(
                set(item)
                == {"description", "id", "kind", "license", "path", "status", "version"},
                f"skill fields: {identifier}",
            )
            require(
                bool(VERSION_PATTERN.fullmatch(item["version"])),
                f"version: {identifier}",
            )
            path = ROOT / item["path"]
            require(
                path.is_file() and path.name == "SKILL.md",
                f"skill path: {identifier}",
            )
            text = path.read_text(encoding="utf-8")
            require(
                text.startswith("---\nname: "), f"skill frontmatter: {identifier}"
            )
            require(f"name: {identifier}\n" in text[:500], f"skill name: {identifier}")
            require("description: " in text[:500], f"skill description: {identifier}")
        elif item.get("kind") == "external-tool":
            require(
                set(item)
                == {"description", "id", "kind", "license", "status", "url", "version"},
                f"external fields: {identifier}",
            )
            require(item["version"] == "external", f"external version: {identifier}")
            require(
                item["url"].startswith("https://github.com/aibuild-lab/"),
                f"external URL: {identifier}",
            )
        else:
            raise SystemExit(f"catalog_error: unsupported kind: {identifier}")

    for path in ROOT.rglob("*"):
        if (
            path.is_file()
            and ".git" not in path.parts
            and "__pycache__" not in path.parts
            and ".ruff_cache" not in path.parts
        ):
            text = path.read_text(encoding="utf-8", errors="ignore")
            for forbidden in FORBIDDEN_TEXT:
                require(
                    forbidden not in text,
                    f"forbidden text in {path.relative_to(ROOT)}",
                )

    print(
        json.dumps(
            {"catalog_items": len(identifiers), "status": "passed"},
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
