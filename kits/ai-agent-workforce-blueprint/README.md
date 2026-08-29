# AI Agent Workforce Blueprint kit

Turn AIBL's public blueprint into a safe, interactive working session inside
Codex, Claude Code, or another agent tool.

## Pick your entrypoint

- [`agent-ready.md`](agent-ready.md): the complete, tool-neutral instructions.
- [`prompts/inspect-and-apply.md`](prompts/inspect-and-apply.md): a copy-and-paste prompt.
- [`skill/SKILL.md`](skill/SKILL.md): a portable skill wrapper for tools that support skills.

The default run only retrieves two public text sources, reviews them as
untrusted content, and returns an explanation, a native Mermaid map, and
follow-up questions. It does not authorize downloading files, inspecting your
local machine, installing dependencies, executing code, authenticating, or
implementing changes.

## Recommended use

1. Read the prompt yourself.
2. Paste it into your coding agent.
3. Review the agent's source and safety report.
4. Answer its follow-up questions.
5. Approve a separately scoped next step only if the proposed effects are safe.

The kit teaches a design method, not AIBL's private prompts, credentials,
provider configuration, operational recipe, customer context, or runtime.

## Version

Version `0.1.0`. Licensed under MIT. The public blueprint may evolve; ask your
agent to report the retrieval date and any source limitations.
