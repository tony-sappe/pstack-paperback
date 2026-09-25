# Verify the result and open a PR

"It compiles" is not evidence. The [Prove It Works principle](../../plugins/pstack/skills/principle-prove-it-works/SKILL.md) makes the agent check the real artifact before it reports success, and your job is to make "the real artifact" checkable. This page covers stating a finish condition, generating a verification skill for your app, opening the PR, and driving it to merged.

![A prototype plane flies a real test course while she times it with a stopwatch and robots film and checklist the run; the terminal reads verify: pass, evidence: captured.](./images/verification.jpg)

## State the finish condition up front

Put what done means in the first prompt, in whatever words fit:

```text
/poteto-mode add json output to this command. text output stays byte-identical, the json parses, both run against the sample project. show me the evidence.
```

Now the agent has three checks it can run, not a mood to satisfy. When the reply comes back, it should carry the exact commands and outputs. If a check couldn't run, a good reply says "inconclusive", and you should treat a confident reply without evidence as a red flag.

Match the check to the change:

- A CLI change runs the real command.
- A UI change walks the changed flow in the running app.
- A parser or migration replays a saved input.
- A perf change compares before and after profiles.
- A storage change reads back the written value.

For a small diff you don't fully trust, [`/blast-radius`](../../plugins/pstack/skills/blast-radius/SKILL.md) finds what it could break elsewhere. It picks the one fact the change is safe because of and proves it by running code instead of writing an essay about it.

## Create a project verification skill

The UI bullet above hides a real requirement. The agent needs a scripted way to drive your app. If your project has one, great. If not, run:

```text
/create-verification-skill
```

[`/create-verification-skill`](../../plugins/pstack/skills/create-verification-skill/SKILL.md) interviews the repository, not you. It works out what a user touches, how the app launches locally, what can drive it (an existing harness first, otherwise browser and CDP, a PTY, or plain HTTP), what evidence proves behavior, and whether two instances can run side by side. It asks you only what the code can't answer.

It writes `verify-<app>/` under the host's project skill directory (`.agents/skills/` in Codex, `.grok/skills/` in Grok Build), with Launch, Doctor, Drive, Evidence, and Cleanup sections. A feature map under `features/` indexes what the app does and what result proves each feature works. The skill ships a [worked feature-map example](../../plugins/pstack/skills/create-verification-skill/references/feature-map-example/). Before handing it over, the generator proves the skill once end to end: launch, doctor check, drive one feature, capture evidence, clean up. If that proof fails, don't use the output.

From then on, "verify it in the app" is a step any agent can execute, in this repo, with no setup conversation.

Once the verify skill works, a [`/swarm`](../../plugins/pstack/skills/swarm/SKILL.md) can split a full pass by feature-map entry and aggregate the results.

## Keep the verification skill honest

Apps change and feature maps rot. When yours drifts, run:

```text
/maintain-verification-skill
```

[`/maintain-verification-skill`](../../plugins/pstack/skills/maintain-verification-skill/SKILL.md) audits the generated skill: one read-only source reader per feature in parallel, then one live pass that drives every mapped feature. It ends in exactly one of three outcomes. `clean` means full coverage and nothing to ship. `changed` means one PR of proven corrections, confined to the verification skill's own directory. `blocked` names the blocker. It never edits product code. If the live pass catches a product regression, it reports the regression instead of papering over it in docs.

## Open the PR

```text
/poteto-mode open the pr. small ordered commits, evidence in the description.
```

The [Opening a PR playbook](../../plugins/pstack/skills/poteto-mode/playbooks/opening-a-pr.md) works from a worktree, rebases the work into small ordered commits, cleans the diff, unslops the prose, and returns the PR link. Five narrow PRs beat one fat one, and stacked follow-ups beat a growing branch.

## Drive the PR to merge-ready with Babysit

An open PR starts collecting blockers immediately. Checks fail, reviewers comment, trunk moves. Hand that churn to the [Babysit playbook](../../plugins/pstack/skills/poteto-mode/playbooks/babysit.md):

```text
/poteto-mode babysit this pr. get it green.
```

Babysit checks the PR with an available forge tool and takes blockers in order: conflicts, then review threads, then CI. It can watch during the active session; continuation after the session requires an actual host wake mechanism. Every known fix batches into one push so checks restart once. The comment triage verifies each claim against the code. When all you want is status, ask smaller and Babysit answers without starting a loop:

```text
/poteto-mode check on pr 123. anything outstanding?
```

Babysit stops at merge-ready. It never merges, even with everything green, because merging is a different decision.

## Land a verified stack

Green is not the same as safe. When you're ready to land, say so:

```text
/poteto-mode land the stack.
```

Request a PR review and live verification on the real surface. Use the host's available forge tool to merge after the requested review and approval gates are met.

Next: [Run work while you sleep](./07-overnight.md).
