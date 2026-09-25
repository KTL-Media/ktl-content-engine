#!/usr/bin/env python3
"""02_transcribe.py — faster-whisper with word timestamps.
Usage: transcribe.py --out <workdir> [--model base]
Produces: <workdir>/transcript.json
"""
import argparse, json, os
# httpx (via huggingface_hub) crashes parsing bracketed IPv6 entries in
# no_proxy; strip them before anything imports httpx.
for _k in ("no_proxy", "NO_PROXY"):
    _v = os.environ.get(_k, "")
    if "[" in _v:
        os.environ[_k] = ",".join(p for p in _v.split(",") if "[" not in p)
from faster_whisper import WhisperModel

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--model", default="base")
    a = ap.parse_args()
    wav = os.path.join(a.out, "audio.wav")
    model = WhisperModel(a.model, device="cpu", compute_type="int8")
    segments, _ = model.transcribe(wav, word_timestamps=True,
                                   vad_filter=True,
                                   vad_parameters={"min_silence_duration_ms": 400})
    out = {"segments": []}
    for s in segments:
        words = [{"w": w.word.strip(), "start": round(w.start, 2), "end": round(w.end, 2)}
                 for w in (s.words or []) if w.word.strip()]
        out["segments"].append({
            "start": round(s.start, 2), "end": round(s.end, 2),
            "text": s.text.strip(), "words": words})
    p = os.path.join(a.out, "transcript.json")
    json.dump(out, open(p, "w"))
    nwords = sum(len(s["words"]) for s in out["segments"])
    print(f"TRANSCRIBE OK: {len(out['segments'])} segments, {nwords} words -> {p}")

if __name__ == "__main__":
    main()
