from dataclasses import dataclass

MIN_CONSTELLATION = 0
MAX_CONSTELLATION = 6
MAX_CHARACTER_COPIES = MAX_CONSTELLATION + 1


@dataclass(frozen=True)
class CharacterGoal:
    target_constellation: int
    copies_owned: int = 0

    def __post_init__(self) -> None:
        if not MIN_CONSTELLATION <= self.target_constellation <= MAX_CONSTELLATION:
            raise ValueError(
                f"Target constellation must be between {MIN_CONSTELLATION} and {MAX_CONSTELLATION}."
            )

        if self.copies_owned < 0:
            raise ValueError("Copies owned cannot be negative.")

        if self.copies_owned > MAX_CHARACTER_COPIES:
            raise ValueError(f"Copies owned cannot be greater than {MAX_CHARACTER_COPIES}.")

    @property
    def total_copies_required(self) -> int:
        return self.target_constellation + 1

    @property
    def copies_needed(self) -> int:
        return max(
            self.total_copies_required - self.copies_owned,
            0,
        )
