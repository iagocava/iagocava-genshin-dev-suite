BASE_FIVE_STAR_RATE = 0.006
SOFT_PITY_START = 74
SOFT_PITY_INCREMENT = 0.06
HARD_PITY = 90


def five_star_probability(current_pity: int) -> float:
    """Return the estimated probability of obtaining a 5-star on the next pull."""

    if current_pity < 0:
        raise ValueError("Current pity cannot be negative.")

    if current_pity >= HARD_PITY:
        raise ValueError(f"Current pity must be lower than {HARD_PITY}.")

    next_pull = current_pity + 1

    if next_pull >= HARD_PITY:
        return 1.0

    if next_pull >= SOFT_PITY_START:
        soft_pity_pulls = next_pull - SOFT_PITY_START + 1

        return min(
            BASE_FIVE_STAR_RATE + soft_pity_pulls * SOFT_PITY_INCREMENT,
            1.0,
        )

    return BASE_FIVE_STAR_RATE
