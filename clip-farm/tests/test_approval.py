import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "05_ship.py"
spec = importlib.util.spec_from_file_location("ship", SCRIPT)
ship = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ship)

class ApprovalTests(unittest.TestCase):
    def test_exact_approval_and_changed_inputs(self):
        with tempfile.TemporaryDirectory() as folder:
            clip = Path(folder) / "clip.mp4"
            clip.write_bytes(b"sample media")
            receipt = Path(folder) / "approval.json"
            data = {"approved": True, "approved_by": "Owner", "clip_sha256": hashlib.sha256(clip.read_bytes()).hexdigest(), "account": "account", "caption": "caption"}
            receipt.write_text(json.dumps(data))
            ship.validate_approval(clip, "account", "caption", receipt)
            for account, caption in [("other", "caption"), ("account", "changed")]:
                with self.assertRaises(ValueError):
                    ship.validate_approval(clip, account, caption, receipt)
            clip.write_bytes(b"changed media")
            with self.assertRaises(ValueError):
                ship.validate_approval(clip, "account", "caption", receipt)

    def test_unapproved_or_unnamed_receipt(self):
        with tempfile.TemporaryDirectory() as folder:
            clip = Path(folder) / "clip.mp4"
            clip.write_bytes(b"media")
            receipt = Path(folder) / "approval.json"
            for data in [{"approved": False}, {"approved": True, "approved_by": ""}]:
                receipt.write_text(json.dumps(data))
                with self.assertRaises(ValueError):
                    ship.validate_approval(clip, "account", "caption", receipt)

if __name__ == "__main__":
    unittest.main()
