# Host compatibility

The plugin package uses the shared Agent Skills layout. Codex and Grok Build can discover the same `skills/<name>/SKILL.md` workflows, but a shared file format does not make every host action interchangeable.

## Supported package surfaces

| Surface | Package entry | Skill invocation |
|---|---|---|
| OpenAI Codex | `.agents/plugins/marketplace.json` → `plugins/pstack/.codex-plugin/plugin.json` | `$pstack:<skill-name>` |
| Grok Build | `.grok-plugin/marketplace.json` → `plugins/pstack/.grok-plugin/plugin.json` | `/<skill-name>` |

The plugin includes Agent Skills and agent prompt references. It does not install MCP servers, hooks, or host-specific subagent registrations.

## Known host-specific workflows

Some upstream workflows name Cursor tools, settings paths, transcript locations, or built-in commands. Treat those steps as Cursor-only unless the skill itself documents a Codex or Grok equivalent.

| Workflow or content | Host dependency |
|---|---|
| `setup-pstack` | Writes Cursor model rules and detects Cursor `Task` model identifiers. |
| `automate-me` | Reads Cursor transcript paths and calls Cursor's built-in `create-skill`; it now stops on other hosts. |
| `create-verification-skill`, `maintain-verification-skill` | Read or write `.cursor/skills/`; they now stop before modifying files on other hosts. |
| `recall`, `show-me-your-work` | Read Cursor-local transcript or run-log locations; they stop rather than guessing paths when those are unavailable. |
| `make-bot-ui` | Uses Cursor automation routines and `api2.cursor.sh`; it now stops on other hosts. |
| `/loop`, Cursor worktrees, Cursor skill-authoring flow | Referenced by long-running, cleanup, and skill-authoring playbooks. Use the host’s own equivalent when available; do not assume the literal Cursor command exists. |
| `Task`, `subagent_type`, Cursor model slugs | Use the host's own delegation API and available models. `poteto-mode` now requires translation and forbids claiming unsupported parallel or wake behavior. |
| `agents/*.md`, `/swarm`, `/arena`, `/interrogate`, `/no-comments` | Grok Build can discover bundled agent files. Codex exposes the skills, while these Markdown agent prompts remain reference material rather than Codex agent registrations. The workflows must use the host's own delegation API; installation does not create Cursor `subagent_type` registrations. |
| `automations/benny/` | Separate Cursor automation source pack. It is not included in the pstack plugin or registered for Codex/Grok. |

These limitations are explicit so an unsupported host command does not look like a working integration. The common engineering guidance and playbooks remain available as skills; adapt any host-specific step before relying on it.

## Upstream project

The source project is [Cursor’s pstack plugin](https://github.com/cursor/plugins/tree/main/pstack). This fork retains the source author and license attribution while adapting package structure and documentation for Codex and Grok Build.
