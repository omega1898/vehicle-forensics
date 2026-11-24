import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from vehicle_forensics.evidence import build_evidence_package, hash_bytes

SAMPLE_CAPTURE = b"0.001 7E8 0441050A\n0.002 7E8 not_hex\ngarbage\n"


class EvidencePackageTest(unittest.TestCase):
    def test_package_hashes_raw_and_skips_bad_lines(self):
        package = build_evidence_package(SAMPLE_CAPTURE, examiner_label="examiner_1")
        self.assertEqual(package["raw_sha256"], hash_bytes(SAMPLE_CAPTURE))
        self.assertEqual(package["record_count"], 1)
        self.assertEqual(package["skipped_line_count"], 2)
        self.assertEqual(package["records"][0]["can_id"], 0x7E8)


if __name__ == "__main__":
    unittest.main()
