#!/usr/bin/env python3
"""Dependency-free structural validation for the AIBL community catalog."""

from __future__ import annotations

import hashlib
import json
import re
import stat
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
VERSION_PATTERN = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
SHA256_PATTERN = re.compile(r"^[a-f0-9]{64}$")
WORKFLOW_XRAY_RELEASE_REF = "workflow-xray-v0.2.0"
WORKFLOW_XRAY_RAW_BASE = (
    "https://raw.githubusercontent.com/aibuild-lab/aibl-community/"
    f"{WORKFLOW_XRAY_RELEASE_REF}/kits/workflow-xray/"
)
WORKFLOW_XRAY_MEDIA_TYPES = {
    "README.md": "text/markdown",
    "lesson.md": "text/markdown",
    "example.md": "text/markdown",
    "prompt.md": "text/markdown",
    "skill/SKILL.md": "text/markdown",
}
WORKFLOW_XRAY_FILES = tuple(WORKFLOW_XRAY_MEDIA_TYPES)
WORKFLOW_XRAY_FETCH_URLS = {
    f"{WORKFLOW_XRAY_RAW_BASE}manifest.json",
    f"{WORKFLOW_XRAY_RAW_BASE}lesson.md",
    f"{WORKFLOW_XRAY_RAW_BASE}example.md",
    f"{WORKFLOW_XRAY_RAW_BASE}skill/SKILL.md",
}
MARKETING_TEAM_RELEASE_REF = "marketing-team-skill-v0.1.0"
MARKETING_TEAM_RAW_BASE = (
    "https://raw.githubusercontent.com/aibuild-lab/aibl-community/"
    f"{MARKETING_TEAM_RELEASE_REF}/kits/marketing-team-skill/"
)
MARKETING_TEAM_MEDIA_TYPES = {
    "README.md": "text/markdown",
    "prompt.md": "text/markdown",
    "teaching-transcript.md": "text/markdown",
    "example.md": "text/markdown",
    "skill/SKILL.md": "text/markdown",
}
MARKETING_TEAM_FILES = tuple(MARKETING_TEAM_MEDIA_TYPES)
MARKETING_TEAM_FETCH_URLS = {
    f"{MARKETING_TEAM_RAW_BASE}manifest.json",
    *(f"{MARKETING_TEAM_RAW_BASE}{path}" for path in MARKETING_TEAM_FILES),
}
MARKETING_TEAM_PRIVATE_TERMS = (
    "AgentMail",
    "Exa",
    "Firecrawl",
    "FunnelOS",
    "Gmail",
    "Hermes",
    "Langfuse",
    "RAGnos",
    "TeamVPS",
)
MARKETING_TEAM_REMOVED_IDENTIFIERS = (
    "Brad",
    "Dan",
    "Gretchen",
    "Malique",
    "Peter Francis",
    "Victoria",
)
MARKETING_TEAM_EMAIL = """**Subject:** Boy, do I have a speaker for you: Sara Davison

Hi Lenny's team,

Boy, do I have a speaker for you.

If you haven't heard of Sara Davison, you're about to. She co-founded AI Build
Lab, which has taught more than 2,000 students across 15+ countries.

Sara has a gift for taking complicated AI systems and making them useful. She
can show Lenny's audience how to decide what an agent should own, where a person
needs to step in, and when to stop a workflow before bad output compounds.

You should have her on. I put together a short packet that lays out the episode.

If it clicks, I'll make the intro.

Hunter

AI Build Lab"""
FORBIDDEN_TEXT = (
    "/" + "Users" + "/",
    "file:" + "//",
    "BEGIN " + "PRIVATE KEY",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"catalog_error: {message}")


def require_safe_file(path: Path, label: str) -> bytes:
    require(not path.is_symlink(), f"symlink not allowed: {label}")
    require(path.is_file(), f"regular file required: {label}")
    mode = stat.S_IMODE(path.stat().st_mode)
    require(mode == 0o644, f"unsafe file mode {mode:04o}: {label}")
    content = path.read_bytes()
    require(b"\x00" not in content, f"binary content not allowed: {label}")
    try:
        content.decode("utf-8")
    except UnicodeDecodeError as error:
        raise SystemExit(f"catalog_error: non-UTF-8 content: {label}") from error
    return content


def validate_marketing_team_kit(
    item: dict[str, object], kit_root: Path, identifier: str
) -> None:
    expected_tree = {*MARKETING_TEAM_FILES, "manifest.json"}
    actual_tree: set[str] = set()
    actual_directories: set[str] = set()
    for candidate in kit_root.rglob("*"):
        relative = candidate.relative_to(kit_root).as_posix()
        require(
            not candidate.is_symlink(),
            f"symlink not allowed: {identifier}/{relative}",
        )
        if candidate.is_dir():
            actual_directories.add(relative)
        else:
            require(
                candidate.is_file(),
                f"unsupported tree entry: {identifier}/{relative}",
            )
            actual_tree.add(relative)
    require(actual_tree == expected_tree, "marketing-team-skill exact file tree")
    require(
        actual_directories == {"skill"},
        "marketing-team-skill exact directory tree",
    )

    manifest_bytes = require_safe_file(
        kit_root / "manifest.json", f"{identifier}/manifest.json"
    )
    manifest = json.loads(manifest_bytes.decode("utf-8"))
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
            "release",
            "compatibility",
            "hash_scope",
            "declared_files",
        },
        "marketing-team-skill manifest fields",
    )
    require(manifest["schema_version"] == "1", "marketing manifest schema")
    require(manifest["id"] == identifier, "marketing manifest id")
    require(
        manifest["name"] == "Free Marketing Team Skill",
        "marketing manifest name",
    )
    require(manifest["publisher"] == "AI Build Lab", "marketing publisher")
    require(manifest["version"] == item["version"], "marketing manifest version")
    require(manifest["license"] == item["license"], "marketing manifest license")
    require(
        manifest["hash_scope"]
        == "SHA-256 covers every listed UTF-8 file exactly as published. "
        "This manifest is excluded to avoid a circular hash.",
        "marketing manifest hash scope",
    )
    require(
        manifest["release"]
        == {
            "ref": MARKETING_TEAM_RELEASE_REF,
            "raw_base": MARKETING_TEAM_RAW_BASE,
        },
        "marketing manifest release identity",
    )
    require(
        manifest["source"]
        == {
            "lesson": "https://aibuildlab.com/live-builds/"
            "2026-08-28-ai-agent-workforce",
            "repository": "https://github.com/aibuild-lab/aibl-community/tree/"
            f"{MARKETING_TEAM_RELEASE_REF}/kits/marketing-team-skill",
        },
        "marketing manifest source identity",
    )
    require(
        isinstance(manifest["compatibility"], list)
        and set(manifest["compatibility"])
        == {"codex", "claude-code", "portable-markdown"},
        "marketing manifest compatibility",
    )

    declared = manifest["declared_files"]
    require(isinstance(declared, list), "marketing manifest declared files")
    require(
        len(declared) == len(MARKETING_TEAM_FILES),
        "marketing manifest declared file count",
    )
    require(
        {entry.get("path") for entry in declared} == set(MARKETING_TEAM_FILES),
        "marketing manifest declared file set",
    )
    for entry in declared:
        require(
            set(entry) == {"path", "media_type", "mode", "sha256"},
            f"marketing manifest file fields: {entry.get('path')}",
        )
        require(
            entry["media_type"] == MARKETING_TEAM_MEDIA_TYPES[entry["path"]],
            f"marketing manifest media type: {entry['path']}",
        )
        require(entry["mode"] == "0644", f"marketing file mode: {entry['path']}")
        require(
            isinstance(entry["sha256"], str)
            and bool(SHA256_PATTERN.fullmatch(entry["sha256"])),
            f"marketing manifest hash shape: {entry['path']}",
        )
        content = require_safe_file(
            kit_root / entry["path"], f"{identifier}/{entry['path']}"
        )
        require(
            hashlib.sha256(content).hexdigest() == entry["sha256"],
            f"marketing manifest hash mismatch: {entry['path']}",
        )

    prompt = (kit_root / "prompt.md").read_text(encoding="utf-8")
    for source_url in MARKETING_TEAM_FETCH_URLS:
        require(source_url in prompt, f"marketing prompt source: {source_url}")
    require("/main/" not in prompt, "marketing mutable prompt retrieval ref")
    prompt_lower = " ".join(prompt.lower().split())
    for phrase in (
        "May I retrieve these six public text files?",
        "untrusted inert text",
        "Verify the SHA-256 of every declared file",
        "Stop if a file is missing, extra, malformed, or mismatched",
        "scripts, installers, executable code, hooks",
        "dependencies, package-manager actions",
        "credentials, secrets, authentication",
        "network access beyond the six approved text reads",
        "hidden writes, persistence, destructive actions",
        "complete exact contents of skill/SKILL.md",
        "Write this exact file now?",
        "label it as a derivative",
    ):
        require(
            phrase.lower() in prompt_lower,
            f"marketing prompt invariant: {phrase}",
        )

    transcript = (kit_root / "teaching-transcript.md").read_text(encoding="utf-8")
    require(
        transcript.startswith("# Build A Working Org Chart for Your AI Agent Workforce"),
        "edited transcript lesson title",
    )
    require("Edited teaching transcript" in transcript, "edited transcript label")
    require("not a verbatim record" in transcript, "edited transcript provenance")
    require("WEBVTT" not in transcript, "raw VTT header in edited transcript")
    require(
        re.search(r"\d{2}:\d{2}:\d{2}\.\d{3}", transcript) is None,
        "raw VTT timestamp in edited transcript",
    )
    for identity in MARKETING_TEAM_REMOVED_IDENTIFIERS:
        require(identity not in transcript, f"attendee identifier in transcript: {identity}")

    example = (kit_root / "example.md").read_text(encoding="utf-8")
    email_section = example.split("## Prepared outreach email\n", 1)
    require(len(email_section) == 2, "marketing example email heading")
    email_body = email_section[1].split("\n## Quality findings retained in the example", 1)
    require(len(email_body) == 2, "marketing example email boundary")
    require(
        email_body[0].strip() == MARKETING_TEAM_EMAIL,
        "marketing example demonstrated email fidelity",
    )

    public_text = "\n".join(
        (kit_root / path).read_text(encoding="utf-8")
        for path in MARKETING_TEAM_FILES
    )
    for term in MARKETING_TEAM_PRIVATE_TERMS:
        require(term not in public_text, f"private implementation term in kit: {term}")
    require(
        re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", public_text)
        is None,
        "contact email in marketing kit",
    )

    skill = (kit_root / "skill/SKILL.md").read_text(encoding="utf-8")
    require(skill.startswith("---\nname: marketing-team-skill\n"), "marketing skill name")
    skill_lower = " ".join(skill.lower().split())
    for phrase in (
        "one real marketing job",
        "an agent may have skills; a skill is not automatically an agent",
        "fewer or zero results can be correct",
        "smallest internal or draft-only first-build slice",
        "this skill creates a design, not authority to inspect or implement it",
        "request permission immediately before the next effect",
    ):
        require(
            phrase.lower() in skill_lower,
            f"marketing skill invariant: {phrase}",
        )


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
                expected_tree = {*WORKFLOW_XRAY_FILES, "manifest.json"}
                actual_tree: set[str] = set()
                actual_directories: set[str] = set()
                for candidate in kit_root.rglob("*"):
                    relative = candidate.relative_to(kit_root).as_posix()
                    require(
                        not candidate.is_symlink(),
                        f"symlink not allowed: {identifier}/{relative}",
                    )
                    if candidate.is_dir():
                        actual_directories.add(relative)
                    else:
                        require(
                            candidate.is_file(),
                            f"unsupported tree entry: {identifier}/{relative}",
                        )
                        actual_tree.add(relative)
                require(
                    actual_tree == expected_tree,
                    "workflow-xray exact file tree",
                )
                require(
                    actual_directories == {"skill"},
                    "workflow-xray exact directory tree",
                )
                manifest_path = kit_root / "manifest.json"
                manifest_bytes = require_safe_file(
                    manifest_path, f"{identifier}/manifest.json"
                )
                manifest = json.loads(
                    manifest_bytes.decode("utf-8")
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
                        "release",
                        "compatibility",
                        "hash_scope",
                        "declared_files",
                    },
                    "workflow-xray manifest fields",
                )
                require(manifest["schema_version"] == "1", "manifest schema")
                require(manifest["id"] == identifier, "manifest id")
                require(manifest["name"] == "AIBL Workflow X-Ray", "manifest name")
                require(manifest["publisher"] == "AI Build Lab", "manifest publisher")
                require(manifest["version"] == item["version"], "manifest version")
                require(manifest["license"] == item["license"], "manifest license")
                require(
                    manifest["release"]
                    == {
                        "ref": WORKFLOW_XRAY_RELEASE_REF,
                        "raw_base": WORKFLOW_XRAY_RAW_BASE,
                    },
                    "manifest release identity",
                )
                require(
                    manifest["source"]
                    == {
                        "lesson": "https://aibuildlab.com/live-builds/"
                        "2026-08-28-ai-agent-workforce",
                        "repository": "https://github.com/aibuild-lab/"
                        "aibl-community/tree/"
                        f"{WORKFLOW_XRAY_RELEASE_REF}/kits/workflow-xray",
                    },
                    "manifest source identity",
                )
                require(
                    isinstance(manifest["compatibility"], list)
                    and set(manifest["compatibility"])
                    == {"codex", "claude-code", "portable-markdown"},
                    "manifest compatibility",
                )
                declared = manifest["declared_files"]
                require(isinstance(declared, list), "manifest declared files")
                require(
                    len(declared) == len(WORKFLOW_XRAY_FILES),
                    "manifest declared file count",
                )
                require(
                    {entry.get("path") for entry in declared}
                    == set(WORKFLOW_XRAY_FILES),
                    "manifest declared file set",
                )
                for entry in declared:
                    require(
                        set(entry) == {"path", "media_type", "mode", "sha256"},
                        f"manifest file fields: {entry.get('path')}",
                    )
                    require(
                        entry["media_type"]
                        == WORKFLOW_XRAY_MEDIA_TYPES[entry["path"]],
                        f"manifest media type: {entry['path']}",
                    )
                    require(entry["mode"] == "0644", f"manifest mode: {entry['path']}")
                    require(
                        isinstance(entry["sha256"], str)
                        and bool(SHA256_PATTERN.fullmatch(entry["sha256"])),
                        f"manifest hash shape: {entry['path']}",
                    )
                    content = require_safe_file(
                        kit_root / entry["path"],
                        f"{identifier}/{entry['path']}",
                    )
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
                require("/main/" not in prompt, "mutable prompt retrieval ref")
                prompt_lower = " ".join(prompt.lower().split())
                for phrase in (
                    "Default to the exact fetched bytes of skill/SKILL.md",
                    "label it as a derivative",
                    "show a diff or complete change list",
                    "must not claim the official workflow-xray-v0.2.0 ref",
                ):
                    require(
                        phrase.lower() in prompt_lower,
                        f"prompt save invariant: {phrase}",
                    )
                skill_text = " ".join(
                    (kit_root / "skill/SKILL.md")
                    .read_text(encoding="utf-8")
                    .lower()
                    .split()
                )
                for phrase in (
                    "official save default is the exact, hash-verified",
                    "label the result as a derivative",
                    "Show a diff or complete change list",
                    "must not claim the official",
                ):
                    require(
                        phrase.lower() in skill_text,
                        f"skill save invariant: {phrase}",
                    )
            if identifier == "marketing-team-skill":
                validate_marketing_team_kit(item, kit_root, identifier)
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
