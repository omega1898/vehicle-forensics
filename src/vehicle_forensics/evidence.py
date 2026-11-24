"""Parse a recorded capture and seal it as evidence.

Capture line format (slice 1): "<timestamp_seconds> <can_id_hex> <data_hex>".
Input is untrusted: malformed lines are counted and skipped, never executed.
"""
import hashlib


def hash_bytes(raw_bytes):
    """Return the SHA-256 hex digest of the raw capture."""
    return hashlib.sha256(raw_bytes).hexdigest()


def parse_capture(capture_text):
    """Turn capture lines into records; return (records, skipped_line_count)."""
    records = []
    skipped_line_count = 0
    for line in capture_text.splitlines():
        parts = line.split()
        if len(parts) != 3:
            skipped_line_count += 1
            continue
        timestamp_text, can_id_text, data_text = parts
        try:
            records.append({
                "timestamp_seconds": float(timestamp_text),
                "can_id": int(can_id_text, 16),
                "data": bytes.fromhex(data_text).hex(),
            })
        except ValueError:
            skipped_line_count += 1
    return records, skipped_line_count


def build_evidence_package(raw_bytes, examiner_label):
    """Hash the raw capture first, then parse, and return the package."""
    raw_sha256 = hash_bytes(raw_bytes)
    records, skipped_line_count = parse_capture(raw_bytes.decode("utf-8", errors="replace"))
    return {
        "raw_sha256": raw_sha256,
        "record_count": len(records),
        "skipped_line_count": skipped_line_count,
        "records": records,
        "custody": [{"action": "sealed", "by": examiner_label, "raw_sha256": raw_sha256}],
    }
