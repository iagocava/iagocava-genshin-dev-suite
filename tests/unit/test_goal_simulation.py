import pytest

from iagocava_genshin.core.pity import BannerState
from iagocava_genshin.core.probability import simulate_character_goal_probability


def test_completed_goal_has_certain_probability() -> None:
    probability = simulate_character_goal_probability(
        total_pulls=0,
        banner_state=BannerState(0, False),
        copies_needed=0,
        simulations=100,
        seed=42,
    )

    assert probability == 1.0


def test_zero_pulls_cannot_obtain_missing_copy() -> None:
    probability = simulate_character_goal_probability(
        total_pulls=0,
        banner_state=BannerState(0, False),
        copies_needed=1,
        simulations=100,
        seed=42,
    )

    assert probability == 0.0


def test_hard_pity_with_guarantee_is_certain() -> None:
    probability = simulate_character_goal_probability(
        total_pulls=1,
        banner_state=BannerState(89, True),
        copies_needed=1,
        simulations=100,
        seed=42,
    )

    assert probability == 1.0


def test_hard_pity_without_guarantee_is_close_to_half() -> None:
    probability = simulate_character_goal_probability(
        total_pulls=1,
        banner_state=BannerState(89, False),
        copies_needed=1,
        simulations=10_000,
        seed=42,
    )

    assert probability == pytest.approx(0.5, abs=0.02)


def test_negative_total_pulls_raises_value_error() -> None:
    with pytest.raises(ValueError, match="Total pulls cannot be negative"):
        simulate_character_goal_probability(
            total_pulls=-1,
            banner_state=BannerState(0, False),
            copies_needed=1,
        )


def test_negative_copies_needed_raises_value_error() -> None:
    with pytest.raises(ValueError, match="Copies needed cannot be negative"):
        simulate_character_goal_probability(
            total_pulls=10,
            banner_state=BannerState(0, False),
            copies_needed=-1,
        )


def test_invalid_simulation_count_raises_value_error() -> None:
    with pytest.raises(ValueError, match="Simulations must be greater than zero"):
        simulate_character_goal_probability(
            total_pulls=10,
            banner_state=BannerState(0, False),
            copies_needed=1,
            simulations=0,
        )
