import pytest

from iagocava_genshin.core.probability import five_star_probability


def test_probability_before_soft_pity() -> None:
    assert five_star_probability(0) == pytest.approx(0.006)
    assert five_star_probability(72) == pytest.approx(0.006)


def test_probability_at_soft_pity_start() -> None:
    assert five_star_probability(73) == pytest.approx(0.066)


def test_probability_after_soft_pity_start() -> None:
    assert five_star_probability(74) == pytest.approx(0.126)


def test_probability_at_pull_89() -> None:
    assert five_star_probability(88) == pytest.approx(0.966)


def test_probability_at_hard_pity() -> None:
    assert five_star_probability(89) == pytest.approx(1.0)


def test_negative_pity_raises_value_error() -> None:
    with pytest.raises(ValueError, match="Current pity cannot be negative"):
        five_star_probability(-1)


def test_pity_equal_to_hard_pity_raises_value_error() -> None:
    with pytest.raises(ValueError, match="Current pity must be lower than 90"):
        five_star_probability(90)
