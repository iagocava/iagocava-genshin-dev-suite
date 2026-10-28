import pytest

from iagocava_genshin.core.calculator import calculate_pull_summary
from iagocava_genshin.core.models import CharacterGoal
from iagocava_genshin.core.pity import BannerState


def test_calculate_pull_summary() -> None:
    state = BannerState(
        current_pity=73,
        is_guaranteed=False,
    )

    goal = CharacterGoal(
        target_constellation=2,
        copies_owned=0,
    )

    summary = calculate_pull_summary(
        primogems=38400,
        intertwined_fates=27,
        banner_state=state,
        character_goal=goal,
    )

    assert summary.total_pulls == 267
    assert summary.current_pity == 73
    assert summary.is_guaranteed is False
    assert summary.pulls_until_hard_pity == 17
    assert summary.next_five_star_probability == pytest.approx(0.066)

    assert summary.target_constellation == 2
    assert summary.total_copies_required == 3
    assert summary.copies_owned == 0
    assert summary.copies_needed == 3


def test_calculate_pull_summary_with_guarantee() -> None:
    state = BannerState(
        current_pity=43,
        is_guaranteed=True,
    )

    goal = CharacterGoal(
        target_constellation=2,
        copies_owned=1,
    )

    summary = calculate_pull_summary(
        primogems=1600,
        intertwined_fates=5,
        banner_state=state,
        character_goal=goal,
    )

    assert summary.total_pulls == 15
    assert summary.current_pity == 43
    assert summary.is_guaranteed is True
    assert summary.pulls_until_hard_pity == 47
    assert summary.next_five_star_probability == pytest.approx(0.006)

    assert summary.target_constellation == 2
    assert summary.total_copies_required == 3
    assert summary.copies_owned == 1
    assert summary.copies_needed == 2
