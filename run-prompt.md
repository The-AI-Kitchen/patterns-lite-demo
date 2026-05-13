# Run prompts for Patterns Lite

The materials (transcripts, lens prompts, verification prompt, synthesis prompt) are tool-agnostic. Only the kickoff prompt syntax differs between Claude Code and Cursor.

Each model writes to its own output folder so runs can be compared side-by-side without overwriting each other:

- Claude Code runs write to `outputs_claude/`.
- Cursor runs write to `outputs_cursor/`.
- If you add a third tool, pick a third folder name (`outputs_<tool>/`) and adapt the kickoff prompt the same way.

The kickoffs below default to the real Amazon Flex gig worker corpus in `real_gig_work_transcripts/`. A synthetic-corpus variant is at the bottom of the file for smoke tests.

---

## Run against the real corpus (default)

### Claude Code

Sign in with a Pro or Max account. Open this folder. Paste the prompt below.

```
Use the Task tool to spawn three subagents in parallel. All outputs from this run go to @outputs_claude/ so they don't collide with runs from other models. Each subagent reads all transcripts in @real_gig_work_transcripts/ (filenames A1.md through A11.md; A8 is dropped from the original dataset) and applies exactly one lens prompt:

- Subagent 1: apply @prompts/01-pain-points.md. Write output to @outputs_claude/01-pain-points.md.
- Subagent 2: apply @prompts/02-emotional-language.md. Write output to @outputs_claude/02-emotional-language.md.
- Subagent 3: apply @prompts/03-causal-chains.md. Write output to @outputs_claude/03-causal-chains.md.

Every direct quote in every lens output, including in Hot spots, Tonal contrasts, and cross-reference sections, must be wrapped in a canonical `[A<N>: "..."]` citation tag, where `<N>` is the participant number from the transcript filename (e.g., `A1.md` → `A1`, `A11.md` → `A11`). Bare quotes without an inline snippet citation will be flagged UNCITED.

After all three subagents finish, spawn a verifier subagent. It applies @prompts/verification.md, reads the three lens files in @outputs_claude/, grounds every citation against the source transcripts in @real_gig_work_transcripts/, and writes the verification report to @outputs_claude/verification.md.

After the verifier finishes, apply @prompts/synthesis.md. Read all four files in @outputs_claude/ (the three lens outputs plus verification.md). Write the synthesis to @outputs_claude/04-synthesis.md.

Each lens has a specific job. Keep direct quotes anchored with the participant ID whenever an output references something a participant said. Do not summarize the transcripts.
```

### Cursor

Open this folder in Cursor. Open the Agent panel. Make sure you are on a model with subagent support. Paste the prompt below.

```
/multitask

Spawn three parallel subagents. All outputs from this run go to @outputs_cursor/ so they don't collide with runs from other models. Each subagent reads all transcripts in @real_gig_work_transcripts/ (filenames A1.md through A11.md; A8 is dropped from the original dataset) and applies exactly one lens prompt:

- Subagent 1: apply @prompts/01-pain-points.md. Write output to @outputs_cursor/01-pain-points.md.
- Subagent 2: apply @prompts/02-emotional-language.md. Write output to @outputs_cursor/02-emotional-language.md.
- Subagent 3: apply @prompts/03-causal-chains.md. Write output to @outputs_cursor/03-causal-chains.md.

Every direct quote in every lens output, including in Hot spots, Tonal contrasts, and cross-reference sections, must be wrapped in a canonical `[A<N>: "..."]` citation tag, where `<N>` is the participant number from the transcript filename (e.g., `A1.md` → `A1`, `A11.md` → `A11`). Bare quotes without an inline snippet citation will be flagged UNCITED.

After all three subagents finish, spawn a verifier subagent. It applies @prompts/verification.md, reads the three lens files in @outputs_cursor/, grounds every citation against the source transcripts in @real_gig_work_transcripts/, and writes the verification report to @outputs_cursor/verification.md.

After the verifier finishes, apply @prompts/synthesis.md. Read all four files in @outputs_cursor/ (the three lens outputs plus verification.md). Write the synthesis to @outputs_cursor/04-synthesis.md.

Each lens has a specific job. Keep direct quotes anchored with the participant ID whenever an output references something a participant said. Do not summarize the transcripts.
```

If `/multitask` is not available on your Cursor build, drop the slash command. Cursor's main agent will still delegate to subagents in parallel based on the explicit task list.

---

## Run against the synthetic corpus (smoke test or alternative)

Same kickoffs as above, with these substitutions:

- `@real_gig_work_transcripts/` becomes `@synthetic/transcripts/`.
- `[A<N>: "..."]` citation format becomes `[p0X: "..."]`. The synthetic transcripts use `p01` through `p10` for participant IDs (filename prefix).
- Choose an output folder that does not overwrite the archived synthetic outputs. The archive lives at `synthetic/outputs_claude/` and `synthetic/outputs_cursor/`. To do a fresh synthetic run, write to a new folder name like `@outputs_claude_synthetic/` or pick another `outputs_<tool>_synthetic/` name.

---

## What to compare across two runs

- Did Claude Code and Cursor produce comparable lens outputs? Same themes surfaced in both?
- Did one tool stay more disciplined inside the lens (no scope creep into the other lenses' territory)?
- Did either tool hallucinate quotes? Spot-check three quotes per lens against the source transcripts, then read the verifier report.
- Did either tool's synthesis pass find tensions across lenses, or did it just stitch summaries together?
- Citation density in the synthesis (how often does it anchor a claim in a quote?).
- Participant coverage in the synthesis (does it cite every participant, or skip some?).
- Token usage and wall time.
