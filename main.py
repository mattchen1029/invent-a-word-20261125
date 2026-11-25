"""Invent a Word We Need — make.fun entry.

Coins one new English word and defines it in a single clear line.
The program writes the word and its definition to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt), exactly as the competition's
sealed scorer expects: UTF-8 text of 1 to 140 characters, not blank.
"""

import os

WORD = "Pocketbuzz"
DEFINITION = (
    "the false feeling that your phone just vibrated "
    "in your pocket when it did not."
)
ENTRY = f"{WORD} \u2014 {DEFINITION}"

MIN_CHARS = 1
MAX_CHARS = 140
OUTPUT_NAME = "entry.txt"


def validate_entry(text):
    """Check the entry against the competition gate."""
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if "\n" in text:
        raise ValueError("entry must be a single line")
    return text


def write_entry(out_dir):
    """Validate the coinage and write it to entry.txt."""
    text = validate_entry(ENTRY)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = write_entry(out_dir)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
