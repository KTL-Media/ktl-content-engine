#!/usr/bin/env python3
"""04_render.py — render a vertical clip: face-tracked 9:16 crop + word-highlight captions.
Usage: render.py --out <workdir> --start 12.5 --end 48.0 --name clip01
Produces: <workdir>/clips/<name>.mp4  (1080x1920, 30fps)
"""
import argparse, json, os, subprocess, sys
import cv2
import numpy as np

W, H = 1080, 1920

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-2000:]); sys.exit(r.returncode)

def face_cx(src, start, end):
    """Median face x-center (in source pixels) across the clip, or None."""
    model = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                         "models", "face_yunet.onnx")
    cap = cv2.VideoCapture(src)
    sw = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    sh = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    det = None
    if os.path.exists(model):
        det = cv2.FaceDetectorYN_create(model, "", (320, 320), score_threshold=0.6)
        det.setInputSize((sw, sh))
    cxs = []
    t = start
    while t < end:
        cap.set(cv2.CAP_PROP_POS_MSEC, t * 1000)
        ok, frame = cap.read()
        if not ok:
            break
        if det is not None:
            _, faces = det.detect(frame)
            if faces is not None and len(faces):
                x, y, w, h = max(faces, key=lambda f: f[2] * f[3])[:4]
                cxs.append(x + w / 2)
        t += 0.75
    cap.release()
    return (float(np.median(cxs)), sw) if cxs else (None, sw)

def to_ass_time(s):
    h, rem = divmod(s, 3600); m, sec = divmod(rem, 60)
    return f"{int(h)}:{int(m):02d}:{sec:05.2f}"

def build_ass(words, start, path):
    """Word-highlight karaoke captions, ~4 words per line."""
    lines, cur, cur_w = [], [], 0
    for w in words:
        cur.append(w); cur_w += len(w["w"]) + 1
        if cur_w >= 22 or len(cur) >= 5:
            lines.append(cur); cur, cur_w = [], 0
    if cur:
        lines.append(cur)
    body = []
    for ln in lines:
        t0 = ln[0]["start"] - start; t1 = ln[-1]["end"] - start
        txt = "".join("{\\kf%d}%s " % (max(1, int((w["end"] - w["start"]) * 100)), w["w"]) for w in ln)
        body.append(f"Dialogue: 0,{to_ass_time(t0)},{to_ass_time(t1)},Cap,,0,0,0,,{txt.strip()}")
    ass = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, BorderStyle, Outline, Shadow, Alignment, MarginV
Style: Cap,Noto Sans,72,&H0000C8FF,&H00FFFFFF,&H80000000,&H80000000,-1,0,1,4,1,2,260
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""" + "\n".join(body) + "\n"
    open(path, "w").write(ass)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--start", type=float, required=True)
    ap.add_argument("--end", type=float, required=True)
    ap.add_argument("--name", required=True)
    a = ap.parse_args()
    src = os.path.join(a.out, "source.mp4")
    t = json.load(open(os.path.join(a.out, "transcript.json")))
    words = [w for s in t["segments"] for w in s["words"]
             if w["end"] > a.start and w["start"] < a.end]
    if not words:
        sys.exit("no words in range")

    cx, sw = face_cx(src, a.start, a.end)
    # after scale=1080:1920:force_original_aspect_ratio=increase, compute crop x
    # do the math in ffmpeg instead: crop x from face fraction
    frac = 0.5 if cx is None else min(max(cx / sw, 0), 1)

    adir = os.path.join(a.out, "ass"); os.makedirs(adir, exist_ok=True)
    ass = os.path.join(adir, f"{a.name}.ass")
    build_ass(words, a.start, ass)

    cdir = os.path.join(a.out, "clips"); os.makedirs(cdir, exist_ok=True)
    out = os.path.join(cdir, f"{a.name}.mp4")
    # scale to cover 1080x1920, then crop window centered on face fraction
    vf = (f"scale=1080:1920:force_original_aspect_ratio=increase,"
          f"crop=1080:1920:x='(in_w-1080)*{frac:.4f}':y='(in_h-1920)/2',"
          f"subtitles='{ass}',format=yuv420p")
    run(["ffmpeg", "-y", "-v", "error", "-ss", str(a.start), "-to", str(a.end),
         "-i", src, "-vf", vf, "-r", "30", "-c:v", "libx264", "-preset", "medium",
         "-crf", "20", "-c:a", "aac", "-b:a", "128k",
         "-movflags", "+faststart", out])
    print("RENDER OK:", out, f"words={len(words)} face={'yes' if cx else 'no'}")

if __name__ == "__main__":
    main()
