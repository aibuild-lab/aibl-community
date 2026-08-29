# AIBL Workflow X-Ray

Turn one fuzzy business workflow into a visible, agent-ready plan.

Workflow X-Ray teaches the public AIBL method through a worked Lenny's Podcast
outreach specimen. The specimen uses verified public sources and sanitized
editorial assets; it is not evidence of a completed live run or sent outreach.
Then the kit helps you map one workflow of your own and, only if you ask,
preview or save the method as a reusable skill.

## Get your first result

1. Open [`prompt.md`](prompt.md) and copy the prompt block.
2. Paste it into Codex, Claude Code, or another agent that can read public
   Markdown.
3. Name one real workflow that currently feels confusing or like a black box.

Your agent will walk you through the lesson before asking about your use case.
It should return:

- a native Mermaid map;
- a handoff table with owners, artifacts, and proof;
- a list of missing decisions or unsafe assumptions; and
- the smallest sensible first build, with a human approval edge.

## The method

Every Workflow X-Ray uses five questions:

**Job -> Roles -> Handoffs -> Proof -> Permission**

- **Job:** What useful result must exist?
- **Roles:** Who decides, coordinates, works, and checks?
- **Handoffs:** What artifact moves between roles?
- **Proof:** What evidence allows the work to continue?
- **Permission:** What needs a person, and when must the system stop?

Read the full [`lesson.md`](lesson.md) or the clearly labeled
[`example.md`](example.md).

## Keep using it

After the first X-Ray, tell your agent: `Save Workflow X-Ray as a skill.` The
agent must offer three choices before it writes anything:

- **Project:** propose a skill scoped to the current project.
- **Personal/global:** propose a reusable skill in the user-level scope
  supported by your tool.
- **Preview only:** show the proposed skill files without installing them.

For Codex or Claude Code, the agent should use the capabilities and documented
skill location of the version actually installed. It must show the proposed
destination and files, then ask immediately before writing. For another tool,
it should produce a portable Markdown skill or explain that the tool does not
support reusable skills. This kit does not hard-code a machine-specific path.

## Safety and IP boundary

The default lesson is public-web and read-only. It does not authorize local
inspection, installation, execution, authentication, deployment, publishing,
or messages. Saving is instruction-only: no scripts, dependencies,
integrations, credentials, or background processes.

The public method teaches how to reason about dependable agent work. It does
not expose AIBL's private prompts, orchestration, provider recipe, thresholds,
security design, customer context, or runtime.

## Files and provenance

- [`lesson.md`](lesson.md): the public lesson.
- [`example.md`](example.md): the representative worked example.
- [`prompt.md`](prompt.md): the copy-and-paste guided experience.
- [`skill/SKILL.md`](skill/SKILL.md): the reusable instruction-only skill.
- [`manifest.json`](manifest.json): version, sources, compatibility, and file
  hashes.

Version `0.2.0`. Published by [AI Build Lab](https://aibuildlab.com) under the
MIT License. The source lesson lives at the
[AIBL live build](https://aibuildlab.com/live-builds/2026-08-28-ai-agent-workforce).
