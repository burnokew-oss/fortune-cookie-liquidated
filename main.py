"""Fortune Cookie for the Liquidated Trader.

Writes a single fortune-cookie line for a crypto trader who has just
been liquidated, to /output/entry.txt. Pure stdlib, fully deterministic:
the same line every run.
"""

import os

FORTUNE = (
    "You will meet a tall, dark stranger: Margin Call. "
    "He emptied your wallet, but left your sense of humour."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
