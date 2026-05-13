# Three-way synthesis comparison: Claude Code, Cursor (Opus 4.7), Cursor (Auto)

All three runs were against the same real Enriquez gig-worker corpus in `real_gig_work_transcripts/` (10 Amazon Flex worker interviews, A1 through A11, A8 dropped from the original dataset). The harness and model settings differ across the three:

| Run | Folder | Harness | Model | Plan | Context | Effort |
|---|---|---|---|---|---|---|
| Claude | `outputs_claude/` | Claude Code (desktop) | Opus 4.7 | Max | 1M | Max |
| Cursor Opus 4.7 | `outputs_cursor_opus47/` | Cursor | Opus 4.7 | Pro | 300k | Extra high |
| Cursor Auto | `outputs_cursor_auto/` | Cursor | Auto (Cursor chooses) | Pro | n/a | n/a |

This is not strictly apples to apples. The Claude / Cursor Opus 4.7 pair is the closest to a same-model, different-harness comparison. The Cursor Opus 4.7 / Cursor Auto pair is the closest to a same-harness, different-model comparison. As discussed in the Caveat section below, the second pair is also confounded by a workspace-contamination effect, so it is not a clean test.

## Number of quotes

| Metric | Claude | Cursor Opus 4.7 | Cursor Auto |
|---|---|---|---|
| Synthesis citations | 20 | 30 | 31 |
| Synthesis word count | 990 | 797 | 794 |
| Verifier total | 245 | 259 | 306 |
| Verifier VERIFIED | 241 | 258 | 306 |
| Verifier FUZZY_MATCH | 4 | 0 | 0 |
| Verifier NOT_FOUND | 0 | 0 | 0 |
| Verifier MISATTRIBUTED | 0 | 0 | 0 |
| Verifier UNCITED | 0 | 1 | 5 |

Observations:

- The two Cursor syntheses cite at almost identical density (~30) and word count (~795). Claude cites less densely (20) in a longer document (990 words), so it spends more prose between citations.
- Total lens citations: Cursor Auto produced the most (306 properly-tagged plus 5 bare); Claude the fewest (245 properly-tagged, 0 bare). More lens citations means more upstream material the synthesis could pull from.
- Zero NOT_FOUND or MISATTRIBUTED across all three runs. No hallucinated quotes anywhere.
- Claude had 4 FUZZY_MATCH (minor word slips like "they have been" instead of "there have been"); both Cursor runs had 0.
- Cursor Auto had 5 UNCITED, all in lens-2 Hot spots parentheticals. Cursor Opus 4.7 had 1 UNCITED. Claude had 0. Bare-quote discipline degraded slightly under Auto, although the synthesis routed around all 5.

## Participant coverage

Citations per participant in each synthesis:

| Participant | Claude | Cursor Opus 4.7 | Cursor Auto |
|---|---|---|---|
| A1 | 5 | 5 | 4 |
| A2 | 0 | 1 | 1 |
| A3 | 1 | 3 | 4 |
| A4 | 2 | 4 | 3 |
| A5 | 1 | 2 | 3 |
| A6 | 1 | 3 | 3 |
| A7 | 2 | 3 | 3 |
| A10 | 2 | 7 | 7 |
| A11 | 6 | 2 | 3 |

Both Cursor runs cite all nine participants. Claude skips A2 entirely. Claude is heaviest on A11 (six citations) and leads its tension section with the A11 love-and-leave split. Both Cursor runs are heaviest on A10 (seven citations each) and lead with A10's warmth-with-precarity pattern. Cursor Opus 4.7 and Cursor Auto have nearly identical coverage profiles per participant.

## Style

- Citation format. All three runs use the same bare-bracket `[A<N>: "..."]` format.
- Em-dashes. Claude: 0 (consistent with Kai's CLAUDE.md preference). Cursor Opus 4.7: 5. Cursor Auto: 7. This is environmental rather than harness or model: Claude Code in the desktop app reads CLAUDE.md formatting rules; Cursor does not unless told to.
- Hypothesis layout. Claude uses bulleted items with bold sub-claims (`- **H1. ...**`). Both Cursor runs use numbered paragraphs (`1. **...**`). Same split as on the synthetic corpus.
- Bolding. Both Cursor runs use bold mid-paragraph to highlight a pattern name (`**heavy pain + intense emotion + sticky behavior**`). Claude bolds the participant ID at the start of each tension paragraph (`**A1**`, `**A11**`).
- Sentence rhythm. Claude has longer sentences with more clauses around each quote. Both Cursor runs are tighter and more enumerable.
- The two Cursor runs are nearly identical at the section level. They share the same three tensions (A1 sticky pain, A10 warmth-with-precarity, A6 inverts), the same three convergences (physical decline, support vacuum, identity), and the same four hypotheses, with hypothesis titles nearly verbatim. My first read of this was that Cursor's harness imposes structure independent of the model. A closer diff shows the convergence is too tight for two independent agents (see the Caveat section). The synthesis-level similarity is most likely a workspace-contamination artifact, not a clean harness signal.

## Actual content

Where all three converge:

- A1's max-friction, max-affect, sticky-behavior pattern. All three syntheses anchor this as a lead tension.
- A6 as the corpus's positive-affect outlier.
- Physical decline as exit trigger (A4, A5, A11). Claude calls it "bodies as the exit trigger"; Cursor Opus 4.7 calls it "physical decline → abandonment"; Cursor Auto calls it "physical decline → abandonment of delivery work". Same participants, same evidence.
- Support / management vacuum drives self-built workarounds. Claude calls it "algorithmic management as broken infrastructure"; both Cursor runs frame it as a "manager / support vacuum → personal workaround layer." Same lens-level evidence.

Where they differ:

- A11's love-and-leave split. Claude leads its tension section with this. Both Cursor runs include A11 but place A10 in the lead tension role instead, treating warmth-with-precarity as the headline pattern.
- Identity convergence (employee vs freelancer). Both Cursor runs name this as a third convergence. Claude does not raise it.
- Hypothesis framings. Claude's H1: "Dependence on the income predicts negative affect more than working conditions do." Cursor's H1 (same in both runs): "The platform substitutes algorithmic feedback for coaching, and workers withdraw reliance rather than improve." Different framings of overlapping evidence: Claude's is psychological-economic; Cursor's is structural-platform.
- A2 coverage. Both Cursor runs cite A2. Claude skips A2 entirely in the synthesis.
- Photo or hide as defensive ritual. Claude names this convergence; neither Cursor run does, though both reference the underlying pain points.

Cursor Opus 4.7 vs Cursor Auto, before the contamination caveat: surface differences are almost cosmetic. Same three tensions, same three convergences with slightly reworded labels, same four hypotheses, same lead with A10. Slightly different quote selections for the same idea (Cursor Opus 4.7 quotes [A11: "Alas, I cannot, my body cannot keep up..."]; Cursor Auto quotes [A11: "I do miss it though. I loved every bit of"] for the same body-toll-with-regret beat). Cursor Auto's third convergence is named "the employee vs freelancer identity tension"; Cursor Opus 4.7's is named "word-of-mouth onboarding."

## Caveat: synthesis-step contamination in the Auto run

After writing the initial comparison, a closer diff of the two Cursor syntheses showed the convergence is too tight to be independent. Specific evidence:

- Hypothesis 1 reproduces verbatim across both runs: a ~40-word sentence including the same claim, the same A2 evidence quote, the same A10 evidence quote (truncated slightly differently but the same anchor), and the same counter-evidence wording. Hypotheses 2, 3, and 4 reproduce with near-identical titles and the same evidence anchors.
- The line "Behavior converges; threat assessment splits." appears verbatim at the end of tension #2 in both runs.
- The line "A6 is the absence-of-tension case, worth flagging because it doesn't match the rest of the corpus." appears verbatim in tension #3 of both runs.

However, the lens-level outputs are not identical:

| Lens file | Cursor Opus 4.7 | Cursor Auto |
|---|---|---|
| 01-pain-points.md | 89 citations, 3,887 words | 109 citations, 4,759 words |
| 02-emotional-language.md | 113 citations, 4,117 words | 137 citations, 4,207 words |
| 03-causal-chains.md | 57 citations, 3,782 words | 60 citations, 3,904 words |

Auto produced about 20% more citations in the first two lenses. The lens subagents did independent work on the corpus.

The most plausible explanation: Cursor's Auto-mode agent does workspace-aware context loading by default, and nothing in the kickoff prompt told it to ignore the prior `outputs_cursor_opus47/04-synthesis.md` already in the workspace. The synthesis pass of the Auto run almost certainly read that earlier synthesis and used it as a template, then varied wording and quote selection at the margins.

Implications:

- The earlier "harness imposes most of the structure" reading is not supported by this comparison. We cannot separate the harness signal from the contamination signal at the synthesis level.
- A clean controlled comparison would require moving the prior tool's outputs out of the workspace (or explicitly excluding them from the agent's context) before kicking off the second run.
- Lens-level discipline is unaffected by this issue. The Auto run's lens subagents did read the source transcripts and produce their own citations, with citation counts and chosen quotes that differ from Cursor Opus 4.7.

## Headline takeaway

Same model, different harness (Claude Opus 4.7 vs Cursor Opus 4.7): substantial structural differences. Claude is longer-form with fewer, more elaborated citations and skips one participant. Cursor is tighter, more enumerable, and covers everyone. Both arrive at most of the same convergences.

Same harness, different model (Cursor Opus 4.7 vs Cursor Auto): the synthesis-level output is near-identical, but the Caveat section above explains why that should not be read as a clean harness-versus-model signal. The Auto run's synthesis agent very likely had the Opus 4.7 synthesis in its context. A clean re-run, with the prior synthesis moved out of the workspace, would be needed to isolate the effect.

Citation discipline ranks Claude > Cursor Opus 4.7 > Cursor Auto for the UNCITED metric (0 vs 1 vs 5). The five UNCITED items in Cursor Auto are in the same Hot spots / Tonal contrasts section that produced the 54 UNCITED in the earlier synthetic-corpus Claude run. The explicit "every quote needs a canonical tag" instruction in the kickoff helps but does not fully close the gap under Auto.

Em-dash usage is environmental, not a quality signal: Claude Code reads Kai's CLAUDE.md and avoids em-dashes; Cursor does not have that preference loaded by default.

No hallucinations in any of the three runs. Zero NOT_FOUND or MISATTRIBUTED across all three verifier reports.

## For Zach

- The grounding step does its job consistently across all three combinations of harness and model tried here. Hallucination is zero in all three.
- We cannot isolate harness-versus-model from this comparison. The Cursor Auto synthesis was almost certainly contaminated by the prior Cursor Opus 4.7 synthesis already in the workspace. The methodological lesson, for both student exercises and production use, is that prior agent outputs in the workspace can leak into later agent runs unless the kickoff explicitly excludes them or they are moved aside.
- For a student exercise, the most pedagogically useful pair is probably Claude Code vs Cursor on the same model, with each tool's prior outputs removed from the workspace before each run. Students can see two different agent harnesses produce comparable-but-stylistically-different syntheses on the same input, and the contamination point itself is a teachable moment about why isolation matters.
- The auto-mode run is still informative for lens-level citation behavior: Auto produced ~20% more upstream citations than controlled Opus 4.7, and slightly worse bare-quote discipline (5 UNCITED vs 1). Its synthesis-level similarity to Opus 4.7 is contaminated and should not be interpreted as a clean signal.
