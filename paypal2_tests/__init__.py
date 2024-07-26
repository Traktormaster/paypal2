"""
Safeguard against importing when not testing.
"""
import os

if os.environ.get("ALLOW_TESTS_IMPORT", "").lower() not in ("1", "true", "yes", "on"):
    raise Exception("Testing must be explicitly enabled by setting ALLOW_TESTS_IMPORT")
