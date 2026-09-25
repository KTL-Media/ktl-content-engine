#!/usr/bin/env python3
"""01_ingest.py — fetch long-form source into the clip farm.
Usage:
  ingest.py --url <youtube-url> --out <workdir> [--sections "00:10:00-00:13:00"]
  ingest.py --file <local.mp4> --out <workdir>
Produces: <workdir>/source.mp4 and <workdir>/audio.wav (16k mono)
"""
import argparse, os, subprocess, sys, shutil

def run(cmd):
    print("+", " ".join(cmd))
    r = subprocess.run(cmd)
    if r.returncode != 0:
        sys.exit(r.returncode)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url")
    ap.add_argument("--file")
    ap.add_argument("--out", required=True)
    ap.add_argument("--sections", default=None, help='"START-END" slice, e.g. 00:10:00-00:13:00')
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    src = os.path.join(a.out, "source.mp4")

    if a.file:
        shutil.copy(a.file, src)
    elif a.url:
        cmd = ["yt-dlp", "-f", "bv*[height<=1080]+ba/b[height<=1080]/b",
               "--merge-output-format", "mp4", "-o", src]
        if a.sections:
            cmd += ["--download-sections", f"*{a.sections}"]
        cmd.append(a.url)
        run(cmd)
    else:
        sys.exit("need --url or --file")

    wav = os.path.join(a.out, "audio.wav")
    run(["ffmpeg", "-y", "-v", "error", "-i", src,
         "-ac", "1", "-ar", "16000", wav])
    print("INGEST OK:", src)

if __name__ == "__main__":
    main()
