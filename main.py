"""A code review comment that approves the pull request while
quietly admitting the reviewer has run out of fear to feel."""

from pathlib import Path

APPROVAL_LINE = "LGTM. Nothing in this diff scares me anymore, which is exactly what scares me."

DESTINATION = Path("/output/entry.txt")


def main() -> None:
    DESTINATION.write_text(APPROVAL_LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
