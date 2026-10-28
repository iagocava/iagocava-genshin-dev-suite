import pytest

from iagocava_genshin.core.pity import BannerState


def test_banner_state_accepts_valid_pity() -> None:
    state = BannerState(
        current_pity=43,
        is_guaranteed=False,
    )

    assert state.current_pity == 43
    assert state.is_guaranteed is False


def test_banner_state_accepts_guaranteed_state() -> None:
    state = BannerState(
        current_pity=70,
        is_guaranteed=True,
    )

    assert state.current_pity == 70
    assert state.is_guaranteed is True


def test_banner_state_accepts_zero_pity() -> None:
    state = BannerState(
        current_pity=0,
        is_guaranteed=False,
    )

    assert state.current_pity == 0


def test_negative_pity_raises_value_error() -> None:
    with pytest.raises(ValueError, match="Current pity cannot be negative"):
        BannerState(
            current_pity=-1,
            is_guaranteed=False,
        )


def test_pity_equal_to_hard_pity_raises_value_error() -> None:
    with pytest.raises(ValueError, match="Current pity must be lower than 90"):
        BannerState(
            current_pity=90,
            is_guaranteed=False,
        )


def test_pity_above_hard_pity_raises_value_error() -> None:
    with pytest.raises(ValueError, match="Current pity must be lower than 90"):
        BannerState(
            current_pity=100,
            is_guaranteed=True,
        )
