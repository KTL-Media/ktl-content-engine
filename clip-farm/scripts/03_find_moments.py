#!/usr/bin/env python3
"""03_find_moments.py — score candidate clip windows from the transcript.
Usage: find_moments.py --out <workdir> [--min 20] [--max 45] [--top 20]
Produces: <workdir>/moments.json — ranked candidates for the agent to curate.
Scoring is heuristic; the agent (Skooly) makes the final pick.
"""
import argparse, json, os, re

HOOKS = ["stop", "secret", "mistake", "nobody", "everyone", "never", "always",
         "free", "truth", "lie", "warning", "breaking", "why", "how i",
         "the reason", "here's", "listen", "understand", "money", "rich",
         "broke", "system", "they don't", "nobody tells"]
Q_RE = re.compile(r"\?")
NUM_RE = re.compile(r"\d")

def sentences(workdir):
    t = json.load(open(os.path.join(workdir, "transcript.json")))
    sents = []
    for seg in t["segments"]:
        for chunk in re.split(r"(?<=[.!?])\s+", seg["text"]):
            chunk = chunk.strip()
            if len(chunk.split()) >= 4:
                sents.append({"start": seg["start"], "end": seg["end"], "text": chunk})
    return sents

def score(text):
    tl = text.lower()
    s = 0
    for h in HOOKS:
        if h in tl:
            s += 2
    if Q_RE.search(text):
        s += 2
    if NUM_RE.search(text):
        s += 1
    if text.isupper() or sum(1 for c in text if c.isupper()) > len(text) * 0.4:
        s += 1
    s += min(len(text.split()) / 25, 1.5)
    return round(s, 2)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--min", type=int, default=20)
    ap.add_argument("--max", type=int, default=45)
    ap.add_argument("--top", type=int, default=20)
    a = ap.parse_args()
    sents = sentences(a.out)
    cands = []
    for i in range(len(sents)):
        words, start = 0, sents[i]["start"]
        texts = []
        for j in range(i, len(sents)):
            texts.append(sents[j]["text"])
            words += len(sents[j]["text"].split())
            dur = sents[j]["end"] - start
            if dur >= a.min:
                if dur <= a.max:
                    full = " ".join(texts)
                    cands.append({"start": round(start, 1), "end": round(sents[j]["end"], 1),
                                  "dur": round(dur, 1), "score": score(full), "text": full})
                break
    cands.sort(key=lambda c: -c["score"])
    # dedupe overlapping: keep highest-scoring, drop overlaps
    kept = []
    for c in cands:
        if all(c["start"] >= k["end"] or c["end"] <= k["start"] for k in kept):
            kept.append(c)
        if len(kept) >= a.top:
            break
    p = os.path.join(a.out, "moments.json")
    json.dump(kept, open(p, "w"), indent=1)
    print(f"MOMENTS OK: {len(kept)} candidates -> {p}")
    for k in kept[:8]:
        print(f"  [{k['start']}-{k['end']}] score={k['score']} {k['text'][:90]}...")

if __name__ == "__main__":
    main()
