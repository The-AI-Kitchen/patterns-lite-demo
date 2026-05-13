# Patterns Lite

A small, teachable demonstration of the multi-agent user research workflow described in DoorDash's [Researchers Are Rewriting the Playbook with AI](https://medium.com/design-doordash/researchers-are-rewriting-the-playbook-with-ai-f07fb89df049) and [How Cursor & Claude Code Are Changing Research At DoorDash and Deliveroo](https://medium.com/design-doordash/how-cursor-claude-code-are-changing-research-at-doordash-and-deliveroo-c2b534018af5).

This is a stripped-down, classroom-scale version of the pattern, not a replacement for production tooling. DoorDash's internal Patterns implementation is far more sophisticated, hardened, and product-aware. This repo exists so students can see the *concept* working end to end on a manageable corpus, including the grounding step that prevents the synthesis pass from citing quotes that were never said.

Put together by Kai Lukoff (Santa Clara University, Computer Science and Engineering) as input for a conversation with the design research team at DoorDash about whether something like this could anchor a student session on AI-assisted research.

## What this demonstrates

- Three lens prompts run in parallel against the same single-domain corpus.
- A verifier subagent grounds every quote against the source transcript before synthesis runs.
- A synthesis pass reads the verification report first and discards any quote the verifier flagged.

Pedagogical takeaway for students: multi-agent extraction is powerful and also lossy. Grounding catches what the lenses get wrong. Without the grounding gate, the synthesis will confidently cite quotes that were not in the source.

## The data

The real corpus in `real_gig_work_transcripts/` is from:

- Enriquez, Diana. "Delivery Gig Worker Interviews on Automation at Work." Princeton University, September 2019. DOI: [10.34770/4324-yn77](https://doi.org/10.34770/4324-yn77).
- License: Creative Commons Attribution 4.0.
- The original dataset contains 39 structured interviews with Amazon Flex, Lyft, Uber, and UberEats drivers. The 10 transcripts included here (A1, A2, A3, A4, A5, A6, A7, A9, A10, A11; A8 was dropped by the original research team) are the Amazon Flex / Amazon delivery subset.
- Interviews are about 20 minutes long, anonymized by the original research team (location and identifying details redacted as `[city]`, `[county]`, `[inaudible]`, etc.).
- Original PDFs and Enriquez's dataset README are included in the folder. The `.md` versions used by the pipeline were extracted with light formatting cleanup (page headers and footers stripped, dialogue verbatim, bracketed redactions preserved).

### Why this corpus is a plausible fit for a DoorDash teaching session

- Delivery gig workers, the same labor model as DoorDash dashers.
- Recurring themes (app friction, surveillance and tracking, schedule unpredictability, pay precarity, attitude toward future automation) overlap with topics that DoorDash research has historically focused on.
- Not a direct competitor (Amazon package delivery rather than restaurant food delivery), so analyzing it is a less loaded exercise for students than examining DoorDash's own competitors.
- Real qualitative data (not synthetic, not AI-generated), which lets the verifier do real work.
- Public and CC-licensed, so re-use in a classroom setting is straightforward.

### Important caveat: 2019 data

These interviews were conducted July through September 2019. They predate:

- The COVID-19 pandemic, which reshaped both gig demand and worker expectations.
- Several waves of platform UX, pay-algorithm, and surveillance updates across the major gig platforms.
- Most major changes in worker classification (California Proposition 22, ongoing classification battles in other states).
- Most public discussion of generative AI in the workplace.

Durable themes like "I don't trust the app" and "support is broken" likely still hold. Specific platform behaviors, pay structures, and worker expectations have shifted, sometimes significantly. Treat the corpus as a teaching dataset that captures a particular moment, not as current-state research input.

## Folder structure

```
patterns-lite-demo/
├── README.md                       (this file)
├── run-prompt.md                   (paste-ready kickoff prompts for Claude Code and Cursor)
├── prompts/
│   ├── 01-pain-points.md           (lens 1)
│   ├── 02-emotional-language.md    (lens 2)
│   ├── 03-causal-chains.md         (lens 3)
│   ├── verification.md             (grounding pass)
│   └── synthesis.md                (cross-lens synthesis, gated by verifier)
├── real_gig_work_transcripts/      (10 Amazon Flex interviews as .md + original PDFs + Enriquez README)
├── outputs_claude/                 (latest Claude Code run on the real corpus)
├── scripts/
│   └── verify_citations.py         (fallback Python verifier; the canonical verifier is a subagent)
└── synthetic/                      (archived earlier run on synthetic SCU student data)
    ├── transcripts/                (10 synthetic transcripts: SCU students tracking academic deadlines)
    ├── outputs_claude/             (lens + verification + synthesis outputs)
    ├── outputs_cursor/             (same, from a Cursor run)
    └── comparisons/                (Claude-vs-Cursor synthesis comparison)
```

The default pipeline target is `real_gig_work_transcripts/`. The synthetic corpus is kept under `synthetic/` because the earlier development of this repo used it before the Enriquez data was added; it stays available as a comparison artifact and as a smaller starter set if students want to read short transcripts before tackling the longer real ones.

## Grounding mechanism

This is the part that matters most.

DoorDash's production Patterns uses Anthropic's Citations API plus an adversarial LLM-as-judge for hard guarantees on quote provenance. The exercise here cannot enforce citations at the model layer, so we enforce them at the prompt and file level instead.

1. Every lens prompt requires a strict citation format: `[A<N>: "first 8 to 12 words of the verbatim quote..."]` for the real corpus, or `[p0X: "..."]` for the synthetic corpus. A lens entry that lacks a properly formatted citation is invalid and must be skipped.
2. A dedicated verifier subagent runs after the three lenses. It parses every citation, opens the cited source transcript, and substring-searches for the snippet. Each citation is classified as VERIFIED, FUZZY_MATCH, NOT_FOUND, MISATTRIBUTED, or UNCITED.
3. The synthesis prompt reads the verification report first. Any quote the verifier flagged as NOT_FOUND, MISATTRIBUTED, or UNCITED is discarded. FUZZY_MATCH quotes may be used only if the snippet is corrected to the actual source text and the correction is noted.

This is the smallest mechanism that demonstrates the principle. It is intentionally easy to read end to end.

## Pipeline

```
3 lens subagents (parallel)
        ↓
1 verifier subagent (after lenses finish)
        ↓
1 synthesis pass (after verifier finishes)
```

Each lens has one job. Lens 1 catalogs pain points. Lens 2 catalogs emotional language. Lens 3 traces explicit causal chains. The lenses do not see each other's outputs.

## How to run

See `run-prompt.md` for paste-ready kickoff prompts targeting the real corpus by default. Each tool writes to a model-specific folder.

- Claude Code writes to `outputs_claude/`.
- Cursor writes to `outputs_cursor/` (create the folder before pasting the prompt, or let the kickoff create it).
- If you add a third tool, pick a third folder name and adapt the kickoff prompt.

### Claude Code

Three surfaces, all work:

- Desktop app: claude.com/download, sign in with a Pro or Max account, Code tab.
- CLI: install with `curl -fsSL https://claude.ai/install.sh | bash`, then `claude` inside this folder.
- Web: claude.ai with Pro or higher.

### Cursor

Open the folder in Cursor. Open the Agent panel. Make sure you are on a model with subagent support. Paste the Cursor prompt from `run-prompt.md`.

## Expected runtime

Five to fifteen minutes end to end on Claude Code with ten transcripts. Cursor timings vary by model. The verifier pass adds about a minute over an ungrounded flow but catches what would otherwise propagate into the synthesis.

## What to look for when evaluating a run

- Lens discipline. Did each subagent stay in its lens? Pain points should not include emotional language, and vice versa.
- Citation discipline. Did each lens output use the strict format? Look at the UNCITED count in the verifier report. A high UNCITED count usually means the lens agent wrote bare quotes in its cross-reference or hot-spot sections without canonical tags.
- Verifier accuracy. Spot-check three VERIFIED citations and any NOT_FOUND citations against the source files.
- Synthesis fidelity. Did the synthesis cite any quotes the verifier flagged? Did it route around them when the verifier discarded them?
- Cross-cutting themes. With ten participants, do real patterns emerge (algorithmic management as broken infrastructure, body wear-down as exit trigger, photo-or-hide defensive rituals), or does the synthesis just list things?

## Side-by-side: Claude Code vs Cursor

Run both paths. Each writes to its own folder so runs do not overwrite each other and can be diffed directly when both finish. Order does not matter. Useful axes of comparison:

- Hallucination rate (NOT_FOUND and UNCITED counts in each `verification.md`).
- Theme overlap in the synthesis after discarding unverified quotes.
- Citation density in the synthesis (how heavily the writer leans on lens evidence rather than abstracting away from it).
- Participant coverage in the synthesis (does it cite every participant, or skip some?).
- Token and time spend.
- Cold-start ease for a first-time user.

An example comparison performed against the synthetic corpus lives in `synthetic/comparisons/synthesis-comparison.md`. It is not a head-to-head verdict (the two runs were generated under slightly different prompt discipline) but it shows the shape of the comparison.

## Synthetic corpus (archived)

`synthetic/transcripts/` contains ten short interviews with fictional Santa Clara University students about how they track academic deadlines. It was useful during development because the topic is single-domain, the cross-cutting themes are obvious, and the transcripts are short enough to spot-check the verifier by hand. It remains in the repo as an alternative input and a smoke-test corpus.

To run the pipeline against the synthetic corpus, swap the transcript path in the kickoff prompt (see the "Run against the synthetic corpus" block in `run-prompt.md`).

## Known limitations and gaps

- Word-count cap. The synthesis prompt asks for under 800 words. Runs to date have come in over. Either tighten the prompt or accept the overage, but do not silently trim citations to fit.
- Domain prompts. The lens prompts were originally written for the synthetic SCU corpus. The lens *definitions* are domain-agnostic, but the example citations inside the prompt files use the synthetic IDs. The kickoff brief in `run-prompt.md` explicitly remaps participant IDs for the real corpus.
- No LLM-as-judge layer. The verifier checks quote provenance only. A judge layer that scores synthesis claims for support (does each claim actually follow from the quotes that anchor it?) would close the remaining gap and is the natural next iteration.
- Single language. Transcripts are English-only.
- One tool per output folder. There is no automatic merge across tools, only side-by-side comparison.

## Acknowledgments

- Data: Diana Enriquez (Princeton Sociology) collected and anonymized the gig worker interviews. The dataset README is in `real_gig_work_transcripts/Enriquez_GigWorkersAutomationAtWork_README.txt`.
- Methodological inspiration: the DoorDash design research team's writeups on Patterns and on the Claude Code / Cursor workflow.

## License

This repository's prompts, scripts, and README are released under MIT. The included real transcripts retain their original Creative Commons Attribution 4.0 license from Enriquez and should be cited per the dataset DOI when reused.
