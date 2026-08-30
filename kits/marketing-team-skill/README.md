# Free Marketing Team Skill

Build a visible, human-governed Agent Native Marketing Team around one real
marketing job.

This kit turns AIBL's **Build A Working Org Chart for Your AI Agent Workforce**
lesson into an agent-ready experience. Your agent first inspects the exact
versioned package, walks you through the completed podcast-outreach example,
and then helps you design a marketing workflow you can actually test.

## Start here

1. Open [`prompt.md`](prompt.md).
2. Copy the single prompt block into Codex, Claude Code, or another agent that
   can retrieve public Markdown.
3. Approve the six listed text-only reads only if you want the agent to inspect
   this release.
4. Choose one marketing job to map, such as podcast outreach, partnerships,
   customer stories, events, or newsletter production.

The agent will produce:

- a Mermaid map of the roles, work, evidence gates, repair paths, and human
  decision;
- a handoff table naming each input, output, owner, and proof requirement;
- a risk and black-box report separating facts, assumptions, and missing
  evidence; and
- the smallest internal or draft-only build slice worth testing first.

Afterward, it can offer to save the exact instruction-only skill. It must show
the destination, complete file, release ref, and verified hash before asking
for permission to write.

## What is inside

- [`prompt.md`](prompt.md): the one-paste guided experience and safety check.
- [`teaching-transcript.md`](teaching-transcript.md): an edited, chaptered
  teaching transcript with setup chatter and participant details removed.
- [`example.md`](example.md): the completed public podcast-outreach example.
- [`skill/SKILL.md`](skill/SKILL.md): the reusable instruction-only skill.
- [`manifest.json`](manifest.json): the immutable release identity and SHA-256
  hashes for every declared file.

## Boundary

Reading this kit grants no authority to inspect private resources, install or
run software, edit files, send outreach, publish, deploy, authenticate, or
activate a workflow. The package teaches a public operating method, not AIBL's
private prompts, providers, orchestration, security design, or runtime.

Version `0.1.0`, published by [AI Build Lab](https://aibuildlab.com) under the
MIT License. Immutable release identity: `marketing-team-skill-v0.1.0`.
Source lesson: [Build A Working Org Chart for Your AI Agent Workforce](https://aibuildlab.com/live-builds/2026-08-28-ai-agent-workforce).
