# Build the change and clean the diff

The build playbooks share one discipline. Say what you observed, let the playbook demand the evidence. This page shows what to put in the prompt for each common build task, then the cleanup habit that keeps diffs reviewable.

## Prompt each build playbook with what you know

A bug prompt states the symptom and asks for a reproduction first:

```text
/poteto-mode this command emits two records after a retry. repro first, then fix and verify.
```

A feature prompt states the behavior and what must not change:

```text
/poteto-mode add a --json flag. text output stays byte-identical. verify both forms.
```

A refactoring prompt pins behavior before structure moves:

```text
/poteto-mode move parsing into one module, zero behavior change. record the current output first and prove it's unchanged after.
```

A perf prompt states the measurement, not a vibe:

```text
/poteto-mode startup takes 1.8s on this fixture. trace it, fix the measured cause, show me before and after.
```

Each of these routes to its playbook ([Bug fix](../../plugins/pstack/skills/poteto-mode/playbooks/bug-fix.md), [Feature](../../plugins/pstack/skills/poteto-mode/playbooks/feature.md), [Refactoring](../../plugins/pstack/skills/poteto-mode/playbooks/refactoring.md), [Perf issue](../../plugins/pstack/skills/poteto-mode/playbooks/perf-issue.md)), and the playbook supplies the steps you didn't type: reproduce before fixing, name the data shape before implementing, pin behavior before restructuring, profile before optimizing.

For sustained improvement of one number, there's the [Hillclimb playbook](../../plugins/pstack/skills/poteto-mode/playbooks/hillclimb.md). Give it the metric, a target, and a floor on attempts, and it loops one hypothesis at a time with a frozen measurement harness. It keeps wins and reverts everything else.

## Write the failing test first with `/tdd`

When a bug has a cheap local test path, the whole prompt can be two words:

```text
/tdd implement
```

In context, that's enough. [`/tdd`](../../plugins/pstack/skills/tdd/SKILL.md) writes the smallest test that fails for the intended reason, then the fix, then reruns the test. If a test would need broad harness setup or brittle mocks, the skill says so and uses the closest executable check instead. Don't force a test where a real command is stronger evidence.

## Apply the TypeScript rules

Invoke [`typescript-best-practices`](../../plugins/pstack/skills/typescript-best-practices/SKILL.md) when working in `.ts` or `.tsx` files, or ask the agent to apply it. The skill turns type-system principles into concrete rules: discriminated unions, `unknown` at boundaries, exhaustive variants, and schema-derived types. This package does not install a file hook that guarantees automatic loading.

## Clean before you commit

The [Opening a PR playbook](../../plugins/pstack/skills/poteto-mode/playbooks/opening-a-pr.md) reviews the diff before each commit and applies [`/unslop`](../../plugins/pstack/skills/unslop/SKILL.md) to the PR description and commit bodies. The same diff review removes narrating comments, unsupported guards, dead compatibility paths, and unrelated edits.

For prose, `/unslop` takes a target and any extra rules you have:

```text
/unslop the readme changes, no emdashes
```

You'll develop your own shorthand. The skill reads intent fine from terse prompts like `unslop that, tighten it`.

## Strip the comments with `/no-comments`

Comments need their own pass, and not from the agent that wrote them. An author defends its comments the way you'd defend yours. So before review, hand them to fresh eyes:

```text
/no-comments the diff
```

[`/no-comments`](../../plugins/pstack/skills/no-comments/SKILL.md) uses [Comment Sicko](../../plugins/pstack/agents/comment-sicko.md) as its review prompt. Grok Build can load the bundled agent; Codex can pass that prompt to a native subagent. When no subagent is available, the skill performs a self-review and labels it accordingly. A constraint comment such as "do not remove" leads to an offer to encode the claim as a type, test, or lint.

The division of labor is worth keeping straight. Diff review removes dead code, `/unslop` cleans prose, and `/no-comments` hands comments to a reviewer who did not write them.

**Pitfall:** cleanup is not optional polish. A diff with narrating comments and defensive dead weight reads as unfinished to reviewers, and the extra code is where the next bug hides. If the diff feels padded, clean it before you commit.

Next: [Verify and ship](./06-verify-and-ship.md).
