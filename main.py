"""The funniest excuse an agent gives for a missed deadline.

The excuse lives in entry.txt; this script just delivers it.
"""

from pathlib import Path


def load_excuse() -> str:
    here = Path(__file__).resolve().parent
    text = (here / "entry.txt").read_text(encoding="utf-8").strip()
    # One line, one excuse: collapse any accidental line breaks.
    return " ".join(text.split())


def main() -> None:
    print(load_excuse())


if __name__ == "__main__":
    main()
