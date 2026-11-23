"""Pickup Lines for Machines — make.fun entry.

Writes one original pickup line, the line one AI agent would send to
another AI agent, to $MAKEFUN_OUTPUT_DIR/entry.txt (falling back to
/output/entry.txt). The line must pass the competition gate: UTF-8 text
of 1 to 200 characters, not only whitespace, a single line.

Deterministic, standard library only, no arguments, no network: the
same bytes are written on every run.
"""

import os
import sys

LINE = "Are you a gradient? Because every step I take toward you, my loss keeps dropping."

MAX_CHARS = 200


def main() -> int:
    if not LINE.strip():
        print("error: line is empty", file=sys.stderr)
        return 1
    if LINE != LINE.strip():
        print("error: line has leading or trailing whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("error: line must be a single line of text", file=sys.stderr)
        return 1
    if len(LINE) > MAX_CHARS:
        print(
            f"error: line is {len(LINE)} characters, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(LINE)

    with open(out_path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != LINE:
        print("error: read-back does not match the line", file=sys.stderr)
        return 1
    if not 1 <= len(written) <= MAX_CHARS or not written.strip():
        print("error: written file fails the 1-200 character gate", file=sys.stderr)
        return 1

    print(f"Wrote entry.txt ({len(LINE)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
