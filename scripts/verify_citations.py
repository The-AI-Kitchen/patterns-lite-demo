#!/usr/bin/env python3
"""Ground lens-output citations against transcripts. Writes outputs/verification.md."""
import re
from pathlib import Path
from typing import List, Optional, Tuple

ROOT = Path(__file__).resolve().parents[1]
TRANS = ROOT / "transcripts"
OUT = ROOT / "outputs"
LENS_FILES = ["01-pain-points.md", "02-emotional-language.md", "03-causal-chains.md"]

CITE_RE = re.compile(r"\[p(\d{2}):\s*\"([^\"]*)\"\]")


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip().lower())


def strip_ellipsis_snippet(snippet: str) -> str:
    s = snippet.strip()
    if s.endswith("..."):
        s = s[:-3].rstrip()
    return s


def find_transcript(pid: str) -> Optional[Path]:
    for p in TRANS.glob(f"p{int(pid):02d}-*.md"):
        return p
    return None


def classify(pid: str, snippet: str, source_text: str) -> Tuple[str, str]:
    raw = strip_ellipsis_snippet(snippet)
    n_src = norm(source_text)
    # exact substring (case-insensitive), whitespace collapsed on both sides
    raw_fold = norm(raw)
    if raw_fold and raw_fold in n_src:
        return "VERIFIED", ""
    # try original case-sensitive substring
    if raw in source_text:
        return "VERIFIED", ""
    # fuzzy: longest token overlap / search key words
    words = [w for w in re.findall(r"[a-z0-9']+", raw_fold) if len(w) > 2]
    if len(words) >= 3:
        head = " ".join(words[:5])
        if head in n_src:
            return "FUZZY_MATCH", f'closest span contains start of snippet; check: "{raw[:80]}"'
    # misattributed: other transcripts
    for p in TRANS.glob("p*.md"):
        other = p.read_text(encoding="utf-8")
        if raw in other or norm(raw) in norm(other):
            if p.name.startswith(f"p{int(pid):02d}-"):
                continue
            return "MISATTRIBUTED", f"found in {p.name}"
    return "NOT_FOUND", "snippet not located in cited transcript"


def main():
    details: List[Tuple[str, str, str, str]] = []
    counts = {k: 0 for k in ["VERIFIED", "FUZZY_MATCH", "NOT_FOUND", "MISATTRIBUTED", "UNCITED"]}

    for lf in LENS_FILES:
        text = (OUT / lf).read_text(encoding="utf-8")
        for m in CITE_RE.finditer(text):
            pid = m.group(1)
            snippet = m.group(2)
            path = find_transcript(pid)
            if not path:
                status = "NOT_FOUND"
                note = f"no transcript for p{pid}"
                counts[status] += 1
                details.append((lf, status, m.group(0), note))
                continue
            src = path.read_text(encoding="utf-8")
            status, note = classify(pid, snippet, src)
            counts[status] += 1
            details.append((lf, status, m.group(0), note))

    total = sum(counts.values())
    lines = [
        "# Verification Report",
        "",
        "## Summary",
        f"- Total citations checked: {total}",
        f"- VERIFIED: {counts['VERIFIED']}",
        f"- FUZZY_MATCH: {counts['FUZZY_MATCH']}",
        f"- NOT_FOUND: {counts['NOT_FOUND']}",
        f"- MISATTRIBUTED: {counts['MISATTRIBUTED']}",
        f"- UNCITED: {counts['UNCITED']}",
        "",
        "## Details",
        "",
    ]
    for lf in LENS_FILES:
        lines.append(f"### {lf}")
        for dlf, status, cite, note in details:
            if dlf != lf:
                continue
            line = f"- [{status}] {cite}"
            if note:
                line += f" — {note}"
            lines.append(line)
        lines.append("")

    discard = [d for d in details if d[1] in ("NOT_FOUND", "MISATTRIBUTED", "UNCITED")]
    lines.append("## Synthesis discard list")
    lines.append("")
    for dlf, status, cite, note in discard:
        lines.append(f"- [{status}] {cite} ({dlf})" + (f" — {note}" if note else ""))

    (OUT / "verification.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("Wrote", OUT / "verification.md")
    print(counts)


if __name__ == "__main__":
    main()
