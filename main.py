"""One-sentence pitch for an absurd invention, for make.fun's One-Sentence Absurd Invention Pitch."""
import os

OUTPUT_PATH = "/output/entry.txt"

PITCH = (
    "Meet the Sock Summons: a washing machine that serves your missing sock a formal "
    "court summons, and if it skips the hearing, the dryer seizes its partner as collateral."
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
