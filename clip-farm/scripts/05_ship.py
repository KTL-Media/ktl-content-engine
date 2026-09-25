#!/usr/bin/env python3
"""05_ship.py — post a rendered clip as an IG reel (approval-gated by Skooly).
Usage: ship.py --clip <workdir>/clips/clip01.mp4 --account <fbid|username> --caption "..."
Extracts a cover frame, then publishes via instagram-cli post-feed.
"""
import argparse, os, subprocess, sys, tempfile

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--clip", required=True)
    ap.add_argument("--account", required=True)
    ap.add_argument("--caption", default="")
    a = ap.parse_args()
    cover = os.path.join(tempfile.gettempdir(), "clip-cover.jpg")
    r = subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", "1",
                        "-i", a.clip, "-frames:v", "1", cover])
    if r.returncode != 0:
        sys.exit("cover extract failed")
    acct = a.account
    # resolve username -> fbid if needed
    if not acct.isdigit():
        out = subprocess.run(["instagram-cli", "accounts"], capture_output=True, text=True)
        import json
        for acc in json.loads(out.stdout)["accounts"]:
            if acc["username"].lower() == acct.lower().lstrip("@"):
                acct = acc["user_fbid"]; break
    cmd = ["instagram-cli", "post-feed", "--account-id", acct,
           "--file", a.clip, "--cover", cover]
    if a.caption:
        cmd += ["--caption", a.caption]
    print("+", " ".join(cmd[:6]), "...")
    r = subprocess.run(cmd)
    sys.exit(r.returncode)

if __name__ == "__main__":
    main()
