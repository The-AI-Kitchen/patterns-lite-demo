# Claude vs Cursor: Synthesis Comparison (synthetic corpus, archived)

Comparison of `synthetic/outputs_claude/04-synthesis.md` and `synthetic/outputs_cursor/04-synthesis.md`, both produced from the same 10-transcript synthetic SCU-student corpus (`synthetic/transcripts/`) and the same prompt set (`prompts/01-pain-points.md`, `02-emotional-language.md`, `03-causal-chains.md`, `verification.md`, `synthesis.md`).

Note: this comparison was generated during an earlier development phase when the outputs folders were at the project root. The folders have since moved under `synthetic/`. The relative path references inside this file have been updated to match the current layout; the analysis itself is unchanged.

## Number of quotes

| Metric | Cursor | Claude |
|---|---|---|
| Citations in synthesis | 47 | 25 |
| Word count | 1,236 | 994 |
| Citations the verifier checked | 159 (all VERIFIED) | 287 (233 VERIFIED, 54 UNCITED) |

Cursor cites almost twice as densely. The 54 UNCITED items in the Claude run came from Claude's lens-2 and lens-3 agents writing bare quotes without canonical `[pXX: "..."]` tags in the Hot spots and Tonal contrasts sections. The verifier flagged them; the synthesis routed around them. Cursor's lens agents were stricter about citation format upstream, so the verifier had a cleaner set to draw on.

Both syntheses exceed the prompt's 800-word cap (Cursor by ~55%, Claude by ~24%).

## Participant coverage

Citations per participant in each synthesis:

| Participant | Cursor | Claude |
|---|---|---|
| p01 (CS junior) | 11 | 0 |
| p07 (Psych junior) | 8 | 3 |
| p04 (English junior) | 8 | 4 |
| p03 (Business senior) | 5 | 3 |
| p05 (Math sophomore) | 3 | 4 |
| p06 (MechE senior) | 3 | 4 |
| p10 (Marketing senior) | 3 | 2 |
| p08 (CS senior) | 2 | 2 |
| p09 (Soc transfer) | 2 | 2 |
| p02 (Bio sophomore) | 2 | 1 |

Cursor cites all 10 participants; Claude cites 9. The participant Claude skips is p01, the one with the largest pain-point list in the corpus (10 entries). Cursor leans heavy on p01, p07, and p04 (high-pain participants); Claude distributes more evenly across the middle of the corpus but loses the highest-signal case.

## Style

- Citation format. Cursor uses inline-code styling with file references: `` `[p01: "..."]` (02-emotional-language.md)``. Claude uses bare brackets without file references: `[p01: "..."]`. Cursor's format makes provenance traceable to the lens file; Claude's is leaner.
- Hypothesis layout. Cursor uses numbered paragraphs (`Hypothesis 1: ... Evidence: ... Counter-evidence: ...`). Claude uses bulleted items with bold sub-claims (`H1. ...`). Claude is more scannable; Cursor is more academic.
- Capitalization. Cursor: `P1`, `P4`. Claude: `p01`, `p04`. Cursor reads like a paper; Claude reads like terminal output.
- Sentence rhythm. Cursor's sentences are longer and stitch multiple citations together. Claude's are shorter and more declarative.
- Em-dashes. Cursor used 4, Claude used 2. Both violated the "avoid em-dashes" rule in the user's global instructions.

## Actual content

Where they agree:

- Notion abandonment as a convergence.
- Camino notifications as broken infrastructure.
- Manual translation from chat / email / PDF into personal systems.
- Sticky-wall valence flip in p04.
- p05's near-miss followed by a new check ritual.
- A specific miss installing a new check or buffer.

Where they differ:

- Hypotheses center on different mechanisms. Cursor proposes *activation energy* (the lowest-opens surface wins, even when anxious) and *acute collisions trigger buffers*. Claude proposes *engineered systems defeat their own user* (connecting p07 self-sabotage, p06 two-system double-book, p08 still-missed code review) and *Camino distrust as the load-bearing cause of every workaround stack*. These are genuinely different theoretical framings. Cursor is more behavioral-economic; Claude is more failure-mode-engineering.
- Anchor cases differ. Cursor's lead tension is p01's anxious-but-relied-on Reminders pattern. Claude's lead tension is p05's low-friction-high-undercurrent inversion. The two syntheses picked nearly opposite participants as the central example.
- Equity framing. Both cover p09 (transfer student) and p10 (dyslexia). Cursor frames p10 as "accommodations-dependent workflows split affect: pride coexists with exhaustion." Claude bundles p09 and p10 into a single "compounding translation tax" hypothesis. Cursor's framing keeps the accommodation context visible; Claude's collapses it into a more generic tax metaphor.
- Counter-evidence quality. Cursor offers concrete counter-evidence anchored in the corpus (e.g., p02 chose paper to *reduce* phone stress, which contradicts H1's activation-energy claim). Claude's counter-evidence is largely hypothetical ("a participant who fully trusts Camino...", "a sustained Notion user..."), i.e., what *would* disconfirm rather than what *does* push back from inside the data.
- Handling of p07 in the Notion hypothesis. Claude notices p07 is the one Notion sustainer and explicitly explains it (database-not-pages) as *sharpening* the abandonment hypothesis rather than disconfirming it. Cursor names p07's love-of-Notion but does not reconcile it with the abandonment pattern.

## Headline takeaway

Cursor produced the more thorough, citation-dense synthesis with better corpus coverage and richer in-corpus counter-evidence. Claude produced the more theoretically distinctive synthesis (the "engineered systems defeat their own user" thread) but at the cost of dropping p01 entirely and leaning on hypothetical rather than evidentiary counter-arguments.

The 54 UNCITED entries in Claude's upstream lens-2 output is a process bug worth fixing. Tightening the lens prompts to require canonical `[pXX: "..."]` tags on every direct quote (including those inside Hot spots and Tonal contrasts sections) would close the gap and give the verifier and synthesis pass more verified material to work with.
