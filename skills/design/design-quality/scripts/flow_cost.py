"""Estimate how long the main tasks in an interface take, with the Keystroke-Level Model (KLM).

The Keystroke-Level Model (Card, Moran and Newell, 1980) gives a fixed time to each small user
action. Adding them up predicts how long a skilled user needs for a task. It is a good way to
compare two designs of the same flow before anyone tests them with people.

Usage (from any folder):

    python flow_cost.py flows.txt
    python flow_cost.py before.txt after.txt      # compare two versions, task by task
    python flow_cost.py flows.txt --K 0.20        # change one operator time

File format: one task per block.

    task: Change the spindle speed | budget=6
    M click M click type:4 K

Lines that start with "#" are comments. "budget=" is optional and in seconds.
The exit code is 1 when a task is over its budget, so the script can run in a test suite.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass, field

# Operator times in seconds, from Card, Moran and Newell (1980).
# K uses the value for an average non-secretary typist (about 40 words per minute).
DEFAULT_TIMES = {
    "K": 0.28,  # press one key
    "P": 1.10,  # point at a target with a mouse
    "B": 0.10,  # press or release a mouse button
    "H": 0.40,  # move the hand between keyboard and mouse
    "M": 1.35,  # think: decide, find, or remember something
}

SHORTHANDS = {
    "click": ["P", "B", "B"],
    "think": ["M"],
    "home": ["H"],
}


@dataclass
class Task:
    name: str
    budget: float | None = None
    ops: list[str] = field(default_factory=list)
    waits: float = 0.0

    def seconds(self, times: dict[str, float]) -> float:
        return sum(times[o] for o in self.ops) + self.waits

    def count(self, op: str) -> int:
        return self.ops.count(op)


def expand(token: str, line_no: int) -> tuple[list[str], float]:
    """Turn one token into basic operators and an optional system wait in seconds."""
    t = token.strip()
    if t.lower() in SHORTHANDS:
        return SHORTHANDS[t.lower()], 0.0
    if t.lower().startswith("type:"):
        return ["K"] * int(t.split(":", 1)[1]), 0.0
    if t.upper().startswith("W:") or t.upper().startswith("R:"):
        return [], float(t.split(":", 1)[1])
    if t.upper() in DEFAULT_TIMES:
        return [t.upper()], 0.0
    raise ValueError(f"line {line_no}: unknown step '{token}'")


def parse(path: str) -> list[Task]:
    tasks: list[Task] = []
    with open(path, encoding="utf-8") as fh:
        for line_no, raw in enumerate(fh, start=1):
            line = raw.split("#", 1)[0].strip()
            if not line:
                continue
            if line.lower().startswith("task:"):
                head = line[5:]
                name, _, opts = head.partition("|")
                task = Task(name=name.strip())
                for opt in opts.split():
                    if opt.startswith("budget="):
                        task.budget = float(opt.split("=", 1)[1].rstrip("s"))
                tasks.append(task)
                continue
            if not tasks:
                raise ValueError(f"line {line_no}: steps found before the first 'task:' line")
            for token in line.split():
                ops, wait = expand(token, line_no)
                tasks[-1].ops.extend(ops)
                tasks[-1].waits += wait
    return tasks


def report(path: str, tasks: list[Task], times: dict[str, float]) -> bool:
    print(f"\n{path}")
    print(f"{'task':40} {'time s':>7} {'clicks':>6} {'keys':>5} {'decide':>6} {'budget':>7}  result")
    ok = True
    for t in tasks:
        sec = t.seconds(times)
        clicks = t.count("B") // 2
        over = t.budget is not None and sec > t.budget
        ok &= not over
        budget = f"{t.budget:.1f}" if t.budget is not None else "-"
        result = "OVER" if over else ("ok" if t.budget is not None else "")
        print(f"{t.name[:40]:40} {sec:7.1f} {clicks:6d} {t.count('K'):5d} {t.count('M'):6d} {budget:>7}  {result}")
    return ok


def compare(a: list[Task], b: list[Task], times: dict[str, float]) -> None:
    after = {t.name: t for t in b}
    print("\nChange per task (second file minus first file)")
    for t in a:
        if t.name in after:
            d = after[t.name].seconds(times) - t.seconds(times)
            pct = 100 * d / t.seconds(times) if t.seconds(times) else 0.0
            print(f"{t.name[:40]:40} {d:+7.1f} s  ({pct:+.0f} %)")
        else:
            print(f"{t.name[:40]:40} missing in second file")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+", help="one flow file, or two to compare")
    for op, sec in DEFAULT_TIMES.items():
        ap.add_argument(f"--{op}", type=float, default=sec, help=f"seconds for operator {op} (default {sec})")
    args = ap.parse_args(argv)
    times = {op: getattr(args, op) for op in DEFAULT_TIMES}

    try:
        parsed = [parse(f) for f in args.files[:2]]
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    results = [report(f, tasks, times) for f, tasks in zip(args.files, parsed)]
    ok = all(results)
    if len(parsed) == 2:
        compare(parsed[0], parsed[1], times)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
