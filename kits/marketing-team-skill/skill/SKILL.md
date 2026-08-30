---
name: marketing-team-skill
description: Design one human-governed marketing workflow as an agent team with explicit roles, handoffs, evidence gates, repair paths, and a smallest safe first build. Use for a concrete marketing job such as podcast outreach, partnerships, customer stories, events, newsletters, or content repurposing; do not use it as authority to inspect private resources, implement, send, publish, install, deploy, or activate anything.
---

# Free Marketing Team Skill

Turn one real marketing job into a visible team a person can direct.

## Frame the job

Ask the user to choose one concrete marketing result, not a department-wide
ambition. Identify:

- the useful result and accountable human owner;
- the allowed source material and evidence;
- the audience or recipient;
- the acceptance checks and honest stop condition; and
- the external effects that remain prohibited without later permission.

If the user has not chosen a job, offer a short set relevant to their context,
such as podcast outreach, partner outreach, customer stories, events,
newsletter production, or content repurposing. Do not inspect their stack to
generate options.

## Design the minimum team

Separate only the responsibilities that create useful ownership or control.
Consider:

- **Coordination:** translates the brief and keeps the outcome visible.
- **Research:** finds allowed evidence and cites it.
- **Strategy:** decides what the evidence means for the objective.
- **Production:** creates the named marketing artifact.
- **Quality review:** tests grounding, fit, tone, and boundaries.
- **Human owner:** approves, revises, or stops before an external effect.

An agent may have skills; a skill is not automatically an agent. Recommend a
distinct role only when it needs separate context, responsibility, tools, or a
meaningful review boundary. Use a skill or deterministic step when that is the
simpler design.

## Make the work inspectable

For every handoff, name:

1. the owner;
2. the input artifact;
3. the output artifact and expected shape;
4. the evidence required to continue;
5. the repair or honest-stop path; and
6. the next decision.

Preserve uncertainty. Fewer or zero results can be correct when the evidence
does not support the requested quantity. Do not turn a polished artifact,
activity log, confidence label, or connected diagram into proof by itself.

## Return four artifacts

Produce:

1. A readable Mermaid map with the job, roles, artifacts, evidence gates,
   repair or honest-stop paths, and human approval edge.
2. A handoff table with stage, owner, input, output, proof, and next decision.
3. A risk report separating known facts, assumptions, missing evidence,
   black-box steps, and unsafe autonomy.
4. The smallest internal or draft-only first-build slice that tests the most
   important handoff or evidence gate.

Prefer a story a human can follow over a dense architecture inventory. Label
unknowns instead of inventing missing decisions.

## Bound the next step

This skill creates a design, not authority to inspect or implement it. Do not
inspect the user's files, repositories, accounts, services, current stack, or
private data unless a separate request authorizes those exact reads.

Do not send outreach, publish content, create accounts, connect integrations,
install dependencies, write files, deploy, or activate a runtime. If the user
asks to continue, first state:

- exact read and write targets;
- allowed and prohibited effects;
- validation and evidence;
- stop conditions and rollback; and
- the human decision still required.

Request permission immediately before the next effect that needs it. Earlier
approval to make the plan does not authorize implementation or an external
effect.

## Source boundary

This is a public derivative of AIBL Workflow X-Ray adapted to one class of
marketing work. It teaches public operating principles and does not reveal or
reconstruct AIBL's private prompts, providers, orchestration, security design,
client context, or runtime.

Source lesson: [Build A Working Org Chart for Your AI Agent Workforce](https://aibuildlab.com/live-builds/2026-08-28-ai-agent-workforce).

Free Marketing Team Skill, version `0.1.0`.
