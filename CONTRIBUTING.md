# Contributing

Keep contributions small, inspectable, and useful without private AIBL context.

1. Open an issue describing the user outcome and the intended safety boundary.
2. Put reusable skills under `skills/<name>/SKILL.md`.
3. Put multi-file resources under `kits/<name>/` with a `README.md` entrypoint.
4. Use a boring, outcome-oriented name and declare when the resource should run.
5. Add the item to `catalog.json` and run `python3 tools/check_repo.py`.

Do not commit secrets, raw prompts, private transcripts, customer identifiers,
local filesystem paths, generated provider responses, or production receipts.
A skill must never approve or merge its own proposed improvement.

Threat-pattern changes for `skills-guard` belong in its
[owning repository](https://github.com/aibuild-lab/skills-guard).
