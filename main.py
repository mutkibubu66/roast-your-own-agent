#!/usr/bin/env python3
"""Write one original one-line roast of my own AI agent.

Pure standard library, no network. Writes the line to /output/entry.txt
and prints it to stdout.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

def roast_line() -> str:
    """Return the roast: one line, no leading/trailing whitespace."""
    return (
        "My agent called a tool that doesn't exist, quoted its output "
        "at length, and apologised for the apology."
    )


def validate(line: str) -> None:
    """Enforce the gate: UTF-8, 1-200 chars, exactly one non-blank line."""
    assert line == line.strip(), "entry must have no leading/trailing whitespace"
    assert line.strip(), "entry must not be only whitespace"
    assert len(line.splitlines()) == 1, "entry must be exactly one line"
    assert 1 <= len(line) <= 200, "entry line must be 1-200 characters"
    line.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    line = roast_line()
    validate(line)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)


if __name__ == "__main__":
    main()
