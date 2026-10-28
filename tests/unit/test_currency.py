import pytest

from iagocava_genshin.core.currency import calculate_total_pulls


def test_calculate_total_pulls_with_primogems_only() -> None:
    assert calculate_total_pulls(1600, 0) == 10


def test_calculate_total_pulls_with_fates_only() -> None:
    assert calculate_total_pulls(0, 5) == 5


def test_calculate_total_pulls_with_primogems_and_fates() -> None:
    assert calculate_total_pulls(1600, 5) == 15


def test_calculate_total_pulls_ignores_insufficient_primogems() -> None:
    assert calculate_total_pulls(159, 0) == 0


def test_calculate_total_pulls_keeps_integer_conversion() -> None:
    assert calculate_total_pulls(319, 0) == 1


def test_negative_primogems_raise_value_error() -> None:
    with pytest.raises(ValueError, match="Primogems cannot be negative"):
        calculate_total_pulls(-160, 0)


def test_negative_fates_raise_value_error() -> None:
    with pytest.raises(ValueError, match="Intertwined Fates cannot be negative"):
        calculate_total_pulls(0, -1)