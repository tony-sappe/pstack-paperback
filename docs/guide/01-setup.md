# Set up pstack

Install the pstack plugin for Codex or Grok Build, then use the host's model and permission settings. The plugin packages reusable skills; it does not set a preferred model or change host configuration.

## Install in Codex

Add this repository as a marketplace:

```bash
codex plugin marketplace add tony-sappe/pstack-paperback
```

Install **pstack** from the Plugins directory in the Codex app. To use a local checkout during development, run `codex plugin marketplace add .` from the repository root.

## Install in Grok Build

Add the marketplace and install the plugin:

```bash
grok plugin marketplace add tony-sappe/pstack-paperback
grok plugin install pstack --trust
```

Grok plugins need trust before their skills load. Review the plugin source before granting it. For a local checkout, run `grok plugin marketplace add .` from the repository root.

## Choose your model

The former `/setup-pstack` workflow writes Cursor-only model rules and is not a Codex or Grok configuration command. Choose models and reasoning settings in your host's own settings. The skill workflows use available host capabilities and may delegate when the host supports it.

## Run your first task

Use pstack's main router with a real, checkable outcome:

```text
/poteto-mode add a --json flag to this command. text output stays byte-identical. verify both.
```

In Codex, invoke the plugin skill as `$pstack:poteto-mode` and give it the same request. The router selects the Feature playbook and uses the other skills when their steps apply.

Next: [Route work through `poteto-mode`](./02-poteto-mode.md).
