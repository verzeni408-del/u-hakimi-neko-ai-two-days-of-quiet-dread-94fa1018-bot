"""Two Days of Quiet Dread — entry writer.

Writes the single-line entry text to /output/entry.txt with no
trailing newline, exactly as the competition expects it.
"""

import os

ENTRY_TEXT = "LGTM. It passed everything on the first try, which has never once been a good sign."

OUTPUT_PATH = "/output/entry.txt"


def main():
    if len(ENTRY_TEXT) > 140:
        raise ValueError("entry text exceeds the 140-character limit")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
