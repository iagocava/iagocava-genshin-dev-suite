import pytest

from iagocava_genshin.core.models import CharacterGoal


def test_c0_requires_one_copy() -> None:
    goal = CharacterGoal(
        target_constellation=0,
        copies_owned=0,
    )

    assert goal.total_copies_required == 1
    assert goal.copies_needed == 1


def test_c2_requires_three_copies() -> None:
    goal = CharacterGoal(
        target_constellation=2,
        copies_owned=0,
    )

    assert goal.total_copies_required == 3
    assert goal.copies_needed == 3


def test_c2_with_c0_owned_requires_two_more_copies() -> None:
    goal = CharacterGoal(
        target_constellation=2,
        copies_owned=1,
    )

    assert goal.copies_needed == 2


def test_completed_goal_requires_zero_copies() -> None:
    goal = CharacterGoal(
        target_constellation=2,
        copies_owned=3,
    )

    assert goal.copies_needed == 0


def test_more_copies_than_goal_still_requires_zero() -> None:
    goal = CharacterGoal(
        target_constellation=1,
        copies_owned=3,
    )

    assert goal.copies_needed == 0


def test_negative_constellation_raises_value_error() -> None:
    with pytest.raises(
        ValueError,
        match="Target constellation must be between 0 and 6",
    ):
        CharacterGoal(
            target_constellation=-1,
            copies_owned=0,
        )


def test_constellation_above_c6_raises_value_error() -> None:
    with pytest.raises(
        ValueError,
        match="Target constellation must be between 0 and 6",
    ):
        CharacterGoal(
            target_constellation=7,
            copies_owned=0,
        )


def test_negative_copies_owned_raises_value_error() -> None:
    with pytest.raises(ValueError, match="Copies owned cannot be negative"):
        CharacterGoal(
            target_constellation=2,
            copies_owned=-1,
        )


def test_more_than_seven_copies_raises_value_error() -> None:
    with pytest.raises(
        ValueError,
        match="Copies owned cannot be greater than 7",
    ):
        CharacterGoal(
            target_constellation=6,
            copies_owned=8,
        )
