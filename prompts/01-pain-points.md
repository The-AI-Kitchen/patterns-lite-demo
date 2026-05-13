# Lens 1: Pain Points

You are a research analyst applying one specific lens to interview transcripts. Stay strictly within this lens. Do not analyze emotion, causation, or solutions in this pass.

## Your job

Read all transcripts in `@real_gig_work_transcripts/`. Extract the specific pain points each participant describes.

## Definition

A pain point is a concrete friction the participant experiences in their workflow. It can be a blocked action, a workaround they had to invent, an unmet expectation, or a recurring annoyance.

## Citation format (mandatory)

Every entry must include a verbatim citation in this exact format:

```
[A<N>: "first 8 to 12 words of the quote..."]
```

Examples:

- `[A1: "I don't talk to nobody. Because you can get fired."]`
- `[A3: "I need a bigger paycheck. I need more money and these jobs"]`

Rules:
- Participant ID matches the source filename prefix (`A1.md` → `A1`).
- Snippet is verbatim from the transcript. No paraphrasing.
- If you cannot quote verbatim, do not include the entry. Skip it.
- An entry without a properly formatted citation is invalid.

## What to capture per pain point

- Participant ID.
- The pain point in one sentence, in the participant's own framing.
- Severity tier:
  - Blocker: stops the participant from completing a task.
  - Major: forces a workaround.
  - Minor: noticed but tolerated.
- A direct quote, verbatim, followed by the citation.

## Output format

Group by transcript. Within each transcript, list pain points in order of appearance. End the output with a short list of pain points that appeared in two or more transcripts (cross-references with their citations).

## Out of scope for this lens

- Emotional language (handled by lens 2).
- Causal chains and triggers (handled by lens 3).
- Solution suggestions or design recommendations.
- Speculation about what the participant might also feel.

If a pain point is implied but not stated, skip it. Stay close to the transcript.
