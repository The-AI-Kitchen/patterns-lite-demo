# Patterns Lite — Demo Project

A stripped-down version of the multi-agent extraction pipeline described in DoorDash's [Researchers Are Rewriting the Playbook with AI](https://medium.com/design-doordash/researchers-are-rewriting-the-playbook-with-ai-f07fb89df049) and [How Cursor & Claude Code Are Changing Research At DoorDash and Deliveroo](https://medium.com/design-doordash/how-cursor-claude-code-are-changing-research-at-doordash-and-deliveroo-c2b534018af5).

Use this to test the AI Kitchen exercise end to end in Claude Code and Cursor Pro before sharing with Zach.

## What this demonstrates

- Three lens prompts run in parallel against the same single-topic transcript corpus.
- A verifier subagent grounds every quote against the source transcript before synthesis runs.
- A synthesis pass reads the verification report first and discards any unverified quote.

Pedagogical takeaway for students: multi-agent extraction is powerful and also lossy. Grounding catches what the lenses get wrong.

## Single-topic corpus

All ten transcripts are about a single topic: how students at SCU track academic deadlines (Camino, group projects, personal systems).

This matters. With a single topic, the lens analysis can find real patterns across participants rather than tautological topic-level differences. The synthesis becomes meaningful.

## Folder structure

```
patterns-lite-demo/
├── README.md                  (this file)
├── run-prompt.md              (kickoff prompts for Claude Code and Cursor)
├── transcripts/
│   ├── p01-cs-junior.md
│   ├── p02-bio-sophomore.md
│   ├── p03-business-senior.md
│   ├── p04-english-junior.md
│   ├── p05-math-sophomore.md
│   ├── p06-mech-eng-senior.md
│   ├── p07-psych-junior.md
│   ├── p08-cs-senior.md
│   ├── p09-soc-transfer.md
│   └── p10-marketing-senior.md
├── prompts/
│   ├── 01-pain-points.md      (lens 1, with strict citation requirement)
│   ├── 02-emotional-language.md  (lens 2)
│   ├── 03-causal-chains.md    (lens 3)
│   ├── verification.md        (grounding pass)
│   └── synthesis.md           (cross-lens synthesis, gated by verifier)
└── outputs/                   (subagent outputs land here)
```

## Data note

All ten transcripts are synthetic, written for this demo. Each is labeled as EXAMPLE DATA at the top. Do not treat as real participant data. Plan to either replace with HCI Lab data (with consent) or keep synthetic and label clearly when sharing with Zach.

## Grounding mechanism (the most important part)

Inspired by DoorDash's use of Anthropic's Citations API and their LLM-as-judge evaluation pass.

We cannot enforce citations at the model API layer here, so we enforce them at the prompt and file level:

1. Every lens prompt requires a strict citation format: `[p0X: "first 8 to 12 words of the verbatim quote..."]`.
2. A dedicated verifier subagent runs after the three lenses. It parses every citation, opens the cited source transcript, and substring-searches for the snippet. Each citation gets classified as VERIFIED, FUZZY_MATCH, NOT_FOUND, MISATTRIBUTED, or UNCITED.
3. The synthesis prompt reads the verification report first. Any quote the verifier flagged as NOT_FOUND, MISATTRIBUTED, or UNCITED is discarded. FUZZY_MATCH quotes are allowed only if the snippet is corrected to the actual source text.

This is the smallest mechanism that demonstrates the principle. Real Patterns uses the Citations API for hard guarantees plus an adversarial LLM-as-judge for claim-level checking. This demo emulates both at a teachable scale.

## Pipeline

```
3 lens subagents (parallel)
        ↓
1 verifier subagent (after lenses finish)
        ↓
1 synthesis subagent (after verifier finishes)
```

## How to run

The run has three top-level steps. The agent must perform all three, in order. Verification is its own step, not a side effect of synthesis.

1. **Lens pass.** Spawn three parallel subagents, one per lens prompt: `prompts/01-pain-points.md`, `prompts/02-emotional-language.md`, `prompts/03-causal-chains.md`. Each writes to the matching file in `outputs/`.
2. **Verification pass.** After all three lens outputs exist, run `prompts/verification.md` as its own subagent. It grounds every citation against the source transcripts and writes `outputs/verification.md`. Required, runs before synthesis, not optional.
3. **Synthesis pass.** Apply `prompts/synthesis.md`. The synthesis reads `outputs/verification.md` first and discards any quote the verifier flagged. Output goes to `outputs/04-synthesis.md`.

See `run-prompt.md` for ready-to-paste kickoff prompts for Claude Code and Cursor Pro.

### Claude Code

Three surfaces, all work:

- Desktop app: claude.com/download, sign in with Pro or Max, Code tab.
- CLI: install with `curl -fsSL https://claude.ai/install.sh | bash`, then `claude` inside this folder.
- Web: claude.ai with Pro or higher.

### Cursor Pro

Open the folder in Cursor. Open the Agent panel (Cmd+I). Paste the Cursor prompt from `run-prompt.md`.

## Expected runtime

Five to ten minutes end to end with ten transcripts. The verifier pass adds a minute over the ungrounded flow but catches what would otherwise propagate into the synthesis.

## What to look for when testing

- Lens discipline: did each subagent stay in its lens? Pain points should not include emotional language, and vice versa.
- Citation discipline: did each lens output use the strict format? Look at the UNCITED count in the verifier report.
- Verifier accuracy: spot-check three VERIFIED citations and three NOT_FOUND citations against the source files. Did the verifier classify correctly?
- Synthesis fidelity: did the synthesis ignore the flagged quotes, or did it sneak them in anyway?
- Scale signal: with ten participants, do real cross-cutting themes emerge (Camino calendar unreliability, Notion abandonment, group-chat deadline burial) or does the synthesis just list them?

## Side-by-side: Claude Code vs Cursor

Run the Claude Code path first. Save the outputs by renaming `outputs/` to `outputs-claude/`. Then run the Cursor path into a fresh `outputs/`. Compare:

- Hallucination rate: NOT_FOUND counts in `verification.md` for each tool.
- Theme overlap in the synthesis after discarding unverified quotes.
- Time and token spend.
- Cold-start ease for a first-time user.

The hallucination rate is the comparison most relevant for the AI Kitchen exercise. Whichever tool produces fewer NOT_FOUND citations gives students a more honest feel for the technique.

## What to adjust before the AI Kitchen session

- Swap synthetic transcripts for HCI Lab data with consent, or keep them synthetic and label clearly.
- Pre-record an expected output (lens outputs, verification report, synthesis) so students have a comparison baseline.
- Decide whether to surface the LLM-as-judge layer as a bonus stretch (`prompts/judge.md` not yet built).

