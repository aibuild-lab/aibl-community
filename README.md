# AIBL Community

Open-source skills and safety tools from [AI Build Lab](https://aibuildlab.com).
Everything here is designed to be inspectable before it is installed or run.

This is our public freebie shelf: small, versioned kits that help people move
from an AI idea to a useful, human-governed build. Learn with us in the
[AI Agent Workforce program](https://maven.com/aibuildlab/scale-with-ai-agent-workforce).

## Start here

### Explore the AI Agent Workforce Blueprint

[`ai-agent-workforce-blueprint`](kits/ai-agent-workforce-blueprint/README.md)
is an agent-ready companion to AIBL's public blueprint. Give its bounded prompt
to Codex, Claude Code, or another coding agent to inspect the public materials,
draw a native Mermaid map, and help you identify one safe application to your
own stack. The prompt instructs the agent to ask before downloading, installing,
executing, or changing anything.

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

## The AIBL team

<table>
  <tr>
    <td align="center"><img src="assets/team/tyler-fisk.jpg" width="150" alt="Tyler Fisk"><br><a href="https://www.linkedin.com/in/tyfisk"><strong>Tyler Fisk</strong></a><br>Co-Founder and Lead Instructor</td>
    <td align="center"><img src="assets/team/sara-davison.jpg" width="150" alt="Sara Davison"><br><a href="https://www.linkedin.com/in/sara-davison-21b41131"><strong>Sara Davison</strong></a><br>Co-Founder and Strategy Lead</td>
  </tr>
</table>

- [**Hunter Lee Canning**](https://www.linkedin.com/in/hunter-canning) builds
  agent-native platform systems and turns live operating work into
  evidence-backed proofs.
- [**J. Michael Schmidt**](https://www.linkedin.com/in/jmichael-schmidt)
  contributes technical teaching, repository enablement, and data work.
- [**Wade Murley**](https://www.linkedin.com/in/wademurley) supports LMS
  production, learner operations, and program delivery.

## Roadmap

We are keeping the first release deliberately small. The direction is:

1. Publish useful, installation-neutral kits with clear safety boundaries.
2. Add versioned manifests and compatibility notes for major agent tools.
3. Expand automated structural, provenance, and threat-pattern checks.
4. Accept focused community contributions with human review and release notes.
5. Keep each resource useful on the web, as Markdown, and inside an agent tool.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Security issues should follow
[SECURITY.md](SECURITY.md) instead of being posted publicly.

## License

Unless a subdirectory says otherwise, this repository is MIT licensed. See
[LICENSE](LICENSE). Team photography is excluded; see
[assets/team/README.md](assets/team/README.md).
