# Run prompts for Patterns Lite

The materials (transcripts, lens prompts, synthesis prompt) are tool-agnostic. Only the kickoff prompt syntax differs between Claude Code and Cursor. Both should produce comparable subagent runs and output files.

---

## Claude Code (CLI, desktop Code tab, or web Code feature)

Sign in with your Pro or Max account. Open this folder. Paste the prompt below.

```
Use the Task tool to spawn three subagents in parallel. Each subagent should read all three transcripts in @transcripts/ and apply exactly one lens prompt:

- Subagent 1: apply @prompts/01-pain-points.md. Write output to @outputs/01-pain-points.md.
- Subagent 2: apply @prompts/02-emotional-language.md. Write output to @outputs/02-emotional-language.md.
- Subagent 3: apply @prompts/03-causal-chains.md. Write output to @outputs/03-causal-chains.md.

After all three subagents finish, read all three output files and apply @prompts/synthesis.md. Write the synthesis to @outputs/04-synthesis.md.

Each lens has a specific job. Keep direct quotes with the transcript filename whenever an output references something a participant said. Do not summarize the transcripts.
```

---

## Cursor Pro

Open this folder in Cursor. Open the Agent panel (Cmd+I). Make sure you are on a model that supports subagents (Composer 2 or Sonnet). Paste the prompt below.

```
/multitask

Spawn three parallel subagents. Each one should read all three transcripts in @transcripts/ and apply exactly one lens prompt:

- Subagent 1: apply @prompts/01-pain-points.md. Write output to @outputs/01-pain-points.md.
- Subagent 2: apply @prompts/02-emotional-language.md. Write output to @outputs/02-emotional-language.md.
- Subagent 3: apply @prompts/03-causal-chains.md. Write output to @outputs/03-causal-chains.md.

After all three subagents finish, read all three output files and apply @prompts/synthesis.md. Write the synthesis to @outputs/04-synthesis.md.

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

