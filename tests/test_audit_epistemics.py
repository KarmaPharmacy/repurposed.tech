import os
import sys
import unittest

WORKSPACE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if WORKSPACE not in sys.path:
    sys.path.insert(0, WORKSPACE)

try:
    from scripts.audit_bible_epistemics import audit_entire_bible
except ImportError:
    audit_entire_bible = None

class TestAuditEpistemics(unittest.TestCase):
    def test_audit_epistemic_reporting(self):
        self.assertIsNotNone(audit_entire_bible, "audit_entire_bible module could not be imported")
        report = audit_entire_bible()
        self.assertIn("chapters", report)
        self.assertIn("blueprints", report)
        self.assertIn("donors", report)
        self.assertEqual(len(report["chapters"]), 36, f"Expected 36 chapters, got {len(report['chapters'])}")
        self.assertEqual(len(report["blueprints"]), 50, f"Expected 50 blueprints, got {len(report['blueprints'])}")
        self.assertEqual(len(report["donors"]), 100, f"Expected 100 donors, got {len(report['donors'])}")

if __name__ == "__main__":
    unittest.main()

