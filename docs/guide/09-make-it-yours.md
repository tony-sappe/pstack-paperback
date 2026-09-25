# Make it yours

poteto-mode is one person's style. You can adapt its playbooks and write project skills for your own workflow. This page covers Codex and Grok Build workflows.

## Build your own mode

```text
Write a project skill that captures my recurring engineering preferences from the examples I provide. Show the proposed rules and the evidence for each before editing files.
```

Give the agent concrete examples or task history the host exposes. Write the result under `.agents/skills/` for Codex or `.grok/skills/` for Grok Build, following the host's skill-authoring guidance. Review each proposed rule against evidence before adopting it.

When your habits change, ask for a focused update:

```text
Update my mode skill using the new examples in this task. Keep rules that still have evidence and show me the diff.
```

Do not infer preferences from private history the host has not exposed.

## Capture a session's lessons with `/reflect`

Right after a task that taught you something, run:

```text
/reflect that took way too long. capture what we learned so the next run doesn't repeat it.
```

[`/reflect`](../../plugins/pstack/skills/reflect/SKILL.md) uses the current task or accessible task history, then reviews proposed lessons. It should label evidence it cannot access and avoid turning one unusual session into a permanent rule.

## Author a focused skill

When you already know the workflow you want to capture:

```text
/poteto-mode write a skill for verifying database migrations in this repo
```

Writing a skill matches the [Authoring or modifying a skill playbook](../../plugins/pstack/skills/poteto-mode/playbooks/authoring-a-skill.md). Use the current host's skill-authoring guidance, validate frontmatter and links, and test behavior when the change is structural. Agent-facing prose has a higher bar than human prose because an unhelpful sentence becomes an instruction some future agent follows.

One special case has its own generator. A skill that must drive your app and prove behavior is a verification skill, so use [`/create-verification-skill`](../../plugins/pstack/skills/create-verification-skill/SKILL.md) and [`/maintain-verification-skill`](../../plugins/pstack/skills/maintain-verification-skill/SKILL.md) instead. [Verify and ship](./06-verify-and-ship.md#create-a-project-verification-skill) covers both.

## Write docs to a standard with `/technical-writing`

Skills aren't the only prose you ship. For docs, RFCs, readmes, PR descriptions, and commit messages:

```text
/technical-writing review the readme changes
```

[`/technical-writing`](../../plugins/pstack/skills/technical-writing/SKILL.md) applies a layered standard with one goal, prose a tired engineer understands on the first read. It picks the document's mode first (tutorial, how-to, reference, or explanation), then works sentence by sentence: who does what, one thought per sentence, nothing readable two ways. Use it to review what you or an agent just wrote, or name it up front when you ask for a doc.

## Test a skill change blind

A skill edit affects every future session, so test it like the experiment it is:

```text
/poteto-mode run the eval playbook on this skill change. same task for both variants, candidates stay blind.
```

The [Eval playbook](../../plugins/pstack/skills/poteto-mode/playbooks/eval.md) gives candidates an organic task in separate sanitized directories and scores the results under neutral labels. Native delegation and model diversity depend on the host. Chain-following is graded from transcripts only when the host exposes those candidate records; otherwise the report marks that criterion inconclusive and judges observable behavior.

Read every output yourself before accepting the verdict. If you disagree with the judge, suspect the rubric before you suspect your judgment.

**Pitfall:** don't edit a skill mid-task because it's misbehaving. Fix it in its own PR and keep the task moving. A skill edit that ships tangled into feature work is invisible to review and impossible to evaluate.

Next: [Recipes and pitfalls](./10-recipes-and-pitfalls.md).
