# Host compatibility

This plugin is packaged for Codex and Grok Build. Both hosts can discover the bundled `skills/` directory. Grok Build also discovers the bundled `agents/` directory. Codex users can pass an agent prompt to native subagents when that interface is available.

| Capability | Codex | Grok Build |
| --- | --- | --- |
| Skill discovery | `.codex-plugin/plugin.json` and `skills/` | `plugin.json`, `.grok-plugin/plugin.json`, and `skills/` |
| Bundled agents | Use the Markdown prompts as task context | Discover `agents/` |
| Delegation and model choice | Use available native tools and models | Use available native tools and models |
| Scheduled continuation | Use a configured Codex automation when authorized | Use a configured host mechanism when available |
| PR operations | Use the connected forge or CLI | Use the connected forge or CLI |

A skill may ask for delegation, scheduling, or a forge action. It can use only capabilities actually available and authorized in the current host. Report an unavailable step and its impact.

The project derives from [Cursor's pstack plugin](https://github.com/cursor/plugins/tree/main/pstack), by Lauren Tan. Cursor users should use the original repository. This fork retains its attribution and MIT license.
