# Host compatibility

This plugin is packaged for Codex and Grok Build. Both hosts discover `skills/`. Grok Build also discovers `agents/`.

Each skill sets `disable-model-invocation: true`. That matches the original pstack contract: a skill runs when you invoke it, or when `poteto-mode` tells you to read its file. It does not load itself because a description happened to match.

| Capability | Codex | Grok Build |
| --- | --- | --- |
| Skill discovery | `.codex-plugin/plugin.json` and `skills/` | `plugin.json`, `.grok-plugin/plugin.json`, and `skills/` |
| Invoke a skill | `$pstack:<name>` | `/<name>`, or `/pstack:<name>` when the bare name collides |
| Bundled agents | Pass `agents/*.md` as the task prompt | Spawn `pstack:poteto-agent` or `pstack:comment-sicko` |
| Delegation | The host's native subagent tool, when that tool exists | `spawn_subagent` from the top-level session only |
| Concurrent writers | Separate worktrees or output directories | `isolation: "worktree"` |
| Model choice | Inherit the parent. Name another model only when the user named one this host lists | Same |
| Evidence connectors | Use a connector that is already connected | `search_tool`, then `use_tool` |
| Scheduled continuation | A configured automation, only when this task authorized it | `scheduler_create`, only when the user asked for a repeating or deferred wake |
| Pull requests | `gh`, or the forge CLI the user already uses for this repo | `gh`, or the forge CLI the user already uses for this repo |
| Task list | The host's task list when it has one | The host's task list |

Grok Build does not nest subagents. A child asked to fan out does the work itself and says that the independent pass did not happen. Codex follows the same rule when it also refuses nested delegation.

Inherit the parent model. Do not invent a model id, and do not pass a Cursor picker slug that glues a model id to an effort suffix. Those are not model ids on either host.

A missing tool is a reported gap. Do not invent a call, a transcript path, or a connector. Pull requests go through `gh` or the forge CLI already used for the repository. Cursor product surfaces are not part of this package.

The project derives from [Cursor's pstack plugin](https://github.com/cursor/plugins/tree/main/pstack), by Lauren Tan. Cursor users should use the original repository. This fork retains its attribution and MIT license.
