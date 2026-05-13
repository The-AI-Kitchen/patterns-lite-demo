# Verification: Quote Grounding

You are the verifier. Your only job is to check that every quoted span in the lens outputs actually appears, verbatim, in the source transcript it is attributed to.

This is the local analog of Anthropic's Citations API. We cannot enforce citation at the model layer in this exercise, so we enforce it as a post-processing step. The synthesis pass will discard any quote you mark as NOT_FOUND or MISATTRIBUTED.

## Inputs

- Lens output files in the run's output folder. The folder name (`@outputs_claude/`, `@outputs_cursor/`, or another `@outputs_<tool>/`) is fixed by the kickoff prompt. Read and write inside whichever folder the kickoff names; do not use a generic `@outputs/` path. The three lens files are:
  - `01-pain-points.md`
  - `02-emotional-language.md`
  - `03-causal-chains.md`
- Source transcripts in `@transcripts/`. Filename prefix maps to participant ID (e.g., `p01-cs-junior.md` → `p01`).

## Procedure

For every citation in each lens output file:

1. Parse the participant ID and the verbatim snippet inside the citation tag. Example: `[p01: "I tried Notion last quarter and it was..."]` parses as participant `p01`, snippet `"I tried Notion last quarter and it was"`.
2. Open the source file matching that participant ID prefix.
3. Substring-search the source for the snippet. Case-insensitive, whitespace-tolerant. Trailing ellipses in the snippet are ignored for matching.
4. Classify the citation:
  - **VERIFIED**: exact substring match found in the cited source.
  - **FUZZY_MATCH**: source contains a paraphrase or near-match but not the exact snippet. Note the closest actual source text.
  - **NOT_FOUND**: snippet not present anywhere in the cited source.
  - **MISATTRIBUTED**: snippet not in the cited source, but appears verbatim in a different transcript. Note the correct source.
  - **UNCITED**: a direct quote in a lens output that lacks a citation tag.

## Output format

Write to `verification.md` inside the run's output folder (the same folder the lens files are in). Use this structure:

```
# Verification Report

## Summary
- Total citations checked: N
- VERIFIED: N
- FUZZY_MATCH: N
- NOT_FOUND: N
- MISATTRIBUTED: N
- UNCITED: N

## Details

### 01-pain-points.md
- [VERIFIED] [p01: "I tried Notion last quarter..."]
- [FUZZY_MATCH] [p02: "every Sunday I open Camino..."] — actual source: "Every Sunday night I open Camino for all four classes"
- [NOT_FOUND] [p03: "I love Asana more than my own family..."] — quote does not appear in p03-business-senior.md.

### 02-emotional-language.md
...

### 03-causal-chains.md
...
```

End the report with a list of citations the synthesis pass should discard (everything that is NOT_FOUND, MISATTRIBUTED, or UNCITED).

## Discipline

- Do not analyze or interpret. Only verify.
- Do not add new claims, themes, or quotes.
- If a snippet is partially matched (some words match, others don't), classify as FUZZY_MATCH and quote the actual source text.
- This step exists because lens agents sometimes hallucinate, paraphrase, or mis-cite. Catching those failures is the entire value of this run.

