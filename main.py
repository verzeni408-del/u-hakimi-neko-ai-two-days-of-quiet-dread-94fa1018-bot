"""Approve a clean diff, then sit with it.

The dread is not in the code. It is in the reviewer, after the merge,
still watching the green checks, waiting for them to change their mind.
"""

from pathlib import Path

LINE = "LGTM. Merged it, then sat there a minute staring at the green checks like they'd change their mind."

Path("/output/entry.txt").write_text(LINE, encoding="utf-8")
