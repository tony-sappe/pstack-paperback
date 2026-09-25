# pstack

pstack is a collection of reusable engineering skills and workflows. This repository packages the skills as a plugin for **OpenAI Codex** and **Grok Build**.

The skills originated in [Cursor’s pstack plugin](https://github.com/cursor/plugins/tree/main/pstack), authored by [Lauren Tan](https://github.com/poteto). Cursor users should use that original repository. This repository is a derivative fork maintained at [tony-sappe/pstack-paperback](https://github.com/tony-sappe/pstack-paperback). The original project remains the source of the pstack name, principles, and much of the workflow content; see [LICENSE](./LICENSE) for the MIT terms.

The dual-host package and marketplace layout follows the project structure in [deep-thought](https://github.com/tony-sappe/deep-thought).

## Install

### Codex

Add this repository as a plugin marketplace:

```bash
codex plugin marketplace add tony-sappe/pstack-paperback
```

Then install **pstack** from the marketplace in the Codex app’s Plugins directory. To use a local checkout while developing, run `codex plugin marketplace add .` from the repository root.

From the CLI, install the same catalog entry with `codex plugin add pstack@pstack-paperback`. Start a new task or reload after installation so the skills are discovered.

### Grok Build

Add the repository marketplace and install the plugin:

```bash
grok plugin marketplace add tony-sappe/pstack-paperback
grok plugin install pstack --trust
grok plugin enable pstack
```

Plugins run with your permissions. Review the skills and grant trust only if you trust this source. For a local checkout, use `grok plugin marketplace add .` from the repository root.

Run `grok plugin details pstack` and `grok inspect` after installation to inspect the loaded components. Grok Build discovers the bundled agent definitions as well as the skills.

## Get started

Start with **poteto-mode**, the router for the bundled engineering playbooks:

- Codex: invoke `$pstack:poteto-mode` from the plugin skill list.
- Grok Build: invoke `/poteto-mode`.

For example, ask it to reproduce a bug, fix the cause, and report the exact verification evidence. The [pstack guide](./docs/guide/README.md) walks through the workflows.

The rest of the skills are available individually when you need them. See [the skill catalog](./plugins/pstack/skills/) and [host compatibility notes](./plugins/pstack/HOST-COMPATIBILITY.md) for host-specific behavior.

## Repository layout

```text
.
├── .agents/plugins/marketplace.json   # Codex repo marketplace
├── .grok-plugin/marketplace.json      # Grok Build marketplace
├── docs/                              # Human-facing pstack guide
├── plugins/pstack/                    # Installable plugin package
│   ├── .codex-plugin/plugin.json      # Codex plugin metadata
│   ├── .grok-plugin/plugin.json       # Grok Build plugin metadata
│   ├── plugin.json                    # Portable plugin metadata
│   ├── agents/                        # Grok agents; Codex prompt references
│   └── skills/                        # Agent Skills workflows
```

The marketplace files point to the same `plugins/pstack` package. The skills use the shared `SKILL.md` format; where an individual workflow depends on host APIs, consult the [compatibility notes](./plugins/pstack/HOST-COMPATIBILITY.md).

## Validate a checkout

```bash
python3 scripts/validate.py
grok plugin validate ./plugins/pstack
```

The first command checks the package, marketplace entries, skill frontmatter, and local guide links. Codex's bundled `plugin-creator` validator can provide an additional host check. The second command requires Grok Build.

## Upstream and license

This project keeps the upstream attribution and MIT license from [cursor/plugins/pstack](https://github.com/cursor/plugins/tree/main/pstack). The current repository is independently maintained and may change the structure and host integrations while retaining that attribution.

The package layout follows the [deep-thought plugin](https://github.com/tony-sappe/deep-thought) and the current [OpenAI plugin packaging guide](https://developers.openai.com/plugins/build/plugins) and [SpaceXAI plugin guide](https://docs.x.ai/build/features/skills-plugins-marketplaces).
