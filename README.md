# AIBL Community

Open-source skills and safety tools from [AI Build Lab](https://aibuildlab.com).
Everything here is designed to be inspectable before it is installed or run.

## Start here

### Prove an agent workflow

[`agent-workforce-proof`](skills/agent-workforce-proof/SKILL.md) turns one
requested outcome into an evidence-backed proof pack: a bounded brief, boring
enterprise role assignments, artifact receipts, quality review, evaluation,
and a human-reviewed improvement candidate.

Copy the skill directory into the skills folder supported by your agent, then
ask it to "build a proof pack for this workflow." Read the file before enabling
it; a skill is executable instruction, not harmless documentation.

### Scan a skill before installing it

[`skills-guard`](https://github.com/aibuild-lab/skills-guard) is AIBL's separate
MIT-licensed threat scanner and trust matrix for AI skill files:

```sh
pip install skills-guard
skills-guard --check ./some-skill --json
```

We link to that owning repository instead of copying its source here. That
keeps provenance, security reports, releases, and updates in one place.

## What this repository does not include

- No customer data, meeting transcripts, private knowledge, or credentials.
- No access to AIBL's internal agent organization or production runtime.
- No unattended publishing, email sending, deployment, or self-merging agents.
- No claim that a clean static scan replaces human review or sandboxing.

[`catalog.json`](catalog.json) is the machine-readable inventory. Run the local
validator before proposing a change:

```sh
python3 tools/check_repo.py
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Security issues should follow
[SECURITY.md](SECURITY.md) instead of being posted publicly.

## License

Unless a subdirectory says otherwise, this repository is MIT licensed. See
[LICENSE](LICENSE).
