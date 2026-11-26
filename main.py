"""The Robot Vacuum's Funniest Excuse - make.fun entry.

Prints one line (at most 120 characters): the excuse a robot
vacuum gives for missing a spot. Also writes it to
/output/entry.txt, the artifact the grader reads.
"""

import os

EXCUSE = "I didn't miss that spot \u2014 the dust and I are in a situationship now, and I'm not ready to commit."


def main():
    line = EXCUSE.strip()
    assert 1 <= len(line) <= 120, "excuse must be 1-120 characters"
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(line)
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = os.path.join("output", "entry.txt")
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(line)
    print(line)


if __name__ == "__main__":
    main()
