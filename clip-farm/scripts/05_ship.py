#!/usr/bin/env python3
"""05_ship.py — post a rendered clip as an IG reel (approval-gated by Skooly).
Usage: ship.py --clip <workdir>/clips/clip01.mp4 --account <fbid|username> --caption "..."
Extracts a cover frame, then publishes via instagram-cli post-feed.
"""
import argparse, hashlib, json, os, subprocess, sys, tempfile

def validate_approval(clip, account, caption, approval_path):
    """Bind human approval to exact media bytes, account, and caption."""
    with open(approval_path, encoding="utf-8") as source:
        approval = json.load(source)
    with open(clip, "rb") as source:
        digest = hashlib.sha256(source.read()).hexdigest()
    expected = {"clip_sha256": digest, "account": account, "caption": caption}
    if approval.get("approved") is not True or not str(approval.get("approved_by", "")).strip():
        raise ValueError("Named human approval is required.")
    if any(approval.get(key) != value for key, value in expected.items()):
        raise ValueError("Approval does not match the exact clip, account, and caption.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--clip", required=True)
    ap.add_argument("--account", required=True)
    ap.add_argument("--caption", default="")
    ap.add_argument("--approval", required=True, help="Human-reviewed JSON receipt bound to this clip, account, and caption")
    a = ap.parse_args()
    try:
        validate_approval(a.clip, a.account, a.caption, a.approval)
    except (OSError, ValueError) as exc:
        sys.exit(f"Publishing blocked: {exc}")
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
