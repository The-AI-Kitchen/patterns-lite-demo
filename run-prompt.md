# Run prompts for Patterns Lite

The materials (transcripts, lens prompts, verification prompt, synthesis prompt) are tool-agnostic. Only the kickoff prompt syntax differs between Claude Code and Cursor.

**Each model writes to its own output folder so runs can be compared side-by-side without overwriting each other:**

- Claude Code runs write to `outputs_claude/`.
- Cursor runs write to `outputs_cursor/`.
- If you add a third tool, pick a third folder name (`outputs_<tool>/`) and adapt the kickoff prompt the same way.

---

## Claude Code (CLI, desktop Code tab, or web Code feature)

Sign in with your Pro or Max account. Open this folder. Paste the prompt below.

```
Use the Task tool to spawn three subagents in parallel. All outputs from this run go to @outputs_claude/ so they don't collide with runs from other models. Each subagent reads all transcripts in @transcripts/ and applies exactly one lens prompt:

- Subagent 1: apply @prompts/01-pain-points.md. Write output to @outputs_claude/01-pain-points.md.
- Subagent 2: apply @prompts/02-emotional-language.md. Write output to @outputs_claude/02-emotional-language.md.
- Subagent 3: apply @prompts/03-causal-chains.md. Write output to @outputs_claude/03-causal-chains.md.

After all three subagents finish, spawn a verifier subagent. It applies @prompts/verification.md, reads the three lens files in @outputs_claude/, grounds every citation against the source transcripts, and writes the verification report to @outputs_claude/verification.md.

After the verifier finishes, apply @prompts/synthesis.md. Read all four files in @outputs_claude/ (the three lens outputs plus verification.md). Write the synthesis to @outputs_claude/04-synthesis.md.

Each lens has a specific job. Keep direct quotes with the transcript filename whenever an output references something a participant said. Do not summarize the transcripts.
```

---

## Cursor Pro

Open this folder in Cursor. Open the Agent panel (Cmd+I). Make sure you are on a model that supports subagents (Composer 2 or Sonnet). Paste the prompt below.

```
/multitask

Spawn three parallel subagents. All outputs from this run go to @outputs_cursor/ so they don't collide with runs from other models. Each subagent reads all transcripts in @transcripts/ and applies exactly one lens prompt:

- Subagent 1: apply @prompts/01-pain-points.md. Write output to @outputs_cursor/01-pain-points.md.
- Subagent 2: apply @prompts/02-emotional-language.md. Write output to @outputs_cursor/02-emotional-language.md.
- Subagent 3: apply @prompts/03-causal-chains.md. Write output to @outputs_cursor/03-causal-chains.md.

After all three subagents finish, spawn a verifier subagent. It applies @prompts/verification.md, reads the three lens files in @outputs_cursor/, grounds every citation against the source transcripts, and writes the verification report to @outputs_cursor/verification.md.

After the verifier finishes, apply @prompts/synthesis.md. Read all four files in @outputs_cursor/ (the three lens outputs plus verification.md). Write the synthesis to @outputs_cursor/04-synthesis.md.

Each lens has a specific job. Keep direct quotes with the transcript filename whenever an output references something a participant said. Do not summarize the transcripts.
```

If /multitask is not available on your Cursor build, drop the slash command and Cursor's main agent will still delegate to subagents in parallel based on the explicit task list.

---

## What to compare across the two runs

- Did Claude Code and Cursor produce comparable lens outputs? Same themes surfaced in both?
- Did one tool stay more disciplined inside the lens (no scope creep into the other lenses' territory)?
- Did either tool hallucinate quotes? Spot-check three quotes per lens against the source transcripts.
- Did either tool's synthesis pass find tensions across lenses, or did it just stitch summaries together?
- Token usage and wall time. Useful for deciding which path students should run on May 22.

