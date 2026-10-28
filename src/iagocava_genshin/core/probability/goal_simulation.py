import random

from iagocava_genshin.core.pity import BannerState

from .character_banner import five_star_probability

DEFAULT_SIMULATIONS = 100_000


def simulate_character_goal_probability(
    total_pulls: int,
    banner_state: BannerState,
    copies_needed: int,
    simulations: int = DEFAULT_SIMULATIONS,
    seed: int | None = None,
) -> float:
    """Estimate the probability of obtaining the required featured copies."""

    if total_pulls < 0:
        raise ValueError("Total pulls cannot be negative.")

    if copies_needed < 0:
        raise ValueError("Copies needed cannot be negative.")

    if simulations <= 0:
        raise ValueError("Simulations must be greater than zero.")

    if copies_needed == 0:
        return 1.0

    if total_pulls == 0:
        return 0.0

    random_generator = random.Random(seed)
    successful_simulations = 0

    for _ in range(simulations):
        if _simulate_goal_attempt(
            total_pulls=total_pulls,
            initial_state=banner_state,
            copies_needed=copies_needed,
            random_generator=random_generator,
        ):
            successful_simulations += 1

    return successful_simulations / simulations


def _simulate_goal_attempt(
    total_pulls: int,
    initial_state: BannerState,
    copies_needed: int,
    random_generator: random.Random,
) -> bool:
    current_pity = initial_state.current_pity
    is_guaranteed = initial_state.is_guaranteed
    featured_copies = 0

    for _ in range(total_pulls):
        probability = five_star_probability(current_pity)

        if random_generator.random() < probability:
            current_pity = 0

            if is_guaranteed:
                featured_copies += 1
                is_guaranteed = False
            elif random_generator.random() < 0.5:
                featured_copies += 1
            else:
                is_guaranteed = True

            if featured_copies >= copies_needed:
                return True
        else:
            current_pity += 1

    return False
