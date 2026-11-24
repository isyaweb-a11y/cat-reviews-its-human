"""Make the AI Judge Laugh: Cat Reviews Its Human.

One funny single-line one-star review from a house cat about its human.
The joke is a product review written by the wrong species: the cat grades
its human on sunbeam management, unwanted furniture and a terrible
impression of a meow, then hands out a single pity star for the one thing
the human still gets right — operating the can opener. Gate: 1-200 chars.
"""

ENTRY = (
    "★☆☆☆☆ The human moved my sunbeam, bought a bed I never asked for, "
    "and meows back in a fake accent. The can opener still works, so one star."
)


def check_review(text: str) -> str:
    """A cat review must open with its star rating and stay one line."""
    cleaned = " ".join(text.split())
    assert 1 <= len(cleaned) <= 200, f"entry is {len(cleaned)} chars, gate is 1-200"
    assert "\n" not in cleaned, "entry must be a single line"
    assert cleaned.startswith("★"), "review must open with its star rating"
    assert "can opener" in cleaned, "review lost the pity star's reason"
    return cleaned


def main() -> None:
    text = check_review(ENTRY)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
