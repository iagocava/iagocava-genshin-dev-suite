from dataclasses import dataclass

MAX_CHARACTER_PITY = 90


@dataclass(frozen=True)
class BannerState:
    current_pity: int
    is_guaranteed: bool

    def __post_init__(self) -> None:
        if self.current_pity < 0:
            raise ValueError("Current pity cannot be negative.")

        if self.current_pity >= MAX_CHARACTER_PITY:
            raise ValueError(f"Current pity must be lower than {MAX_CHARACTER_PITY}.")
