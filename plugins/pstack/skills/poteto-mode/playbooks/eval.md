### Eval

**You own the experiment design. Plan, blind, run, synthesize.**

**Non-negotiables for blinding:**

- No `eval`, `test`, `judge`, `experiment`, `rubric`, `score`, `compare`, `benchmark`, `candidate`, or `arena` in any directory, file, or prompt the candidate sees.
- The candidate prompt looks like an organic user request. State the goal, not the meta.
- No chain-eliciting cues. Don't ask the candidate to list which skills, principles, or files they applied. Ask for design notes generally and grade chain-following from code shape, not self-report.
- Sanitize directory and slug names. Use project-shaped names a user might pick.
- Don't tell the candidate other candidates exist.
- The judge can know it's judging but sees outputs by sanitized label only, never by model name.
- Comparing two variants: one judge scores both sets in a single pass on one scale, blind to which set each came from.

**Steps:**

1. **Frame.** State what variant is under test and what behavior counts as success. Write the rubric (3-6 concrete criteria) for the judge only. Hold it back from candidates.
2. **Set up sanitized environments.** Per-candidate working dir with the variant in place. Plant any context an organic task would have: a project skeleton, the skills the candidate would naturally read.
3. **Author one organic prompt.** What a user would type. No leakage of what's being measured.
4. **Run N candidates** through the current host's native delegation interface when available. Use separate sanitized directories and the same prompt. Run concurrently and diversify models only when the host supports those choices. Without delegation, run isolated attempts sequentially and label the experiment accordingly.
5. **Ask a blinded judge** through the host's native delegation interface when available. Prefer a different available model family. The judge sees outputs by sanitized label and the rubric, never a model name. Without an independent judge, score directly and label the verdict as self-review.
6. **Verify the chain from accessible evidence, not self-report.** If the host exposes each candidate's transcript, inspect only those exact task records and identify the files actually opened. Do not guess private paths or scan other projects. If transcripts are unavailable, grade observable output behavior and mark chain-following inconclusive; do not infer it from a candidate's claims.
7. **Read every candidate output yourself** end to end. Compare to the judge's verdict. Disagreement means a model is biased or the rubric is ambiguous. Synthesize.

**Reply:** variant under test, rubric, per-candidate notes, judge's verdict, your synthesis, and a recommendation for whether to promote the variant.
