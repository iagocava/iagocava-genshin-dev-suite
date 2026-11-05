from unittest.mock import patch

from iagocava_genshin.apps.pull_calculator.cli import (
    ask_constellation,
    ask_guaranteed,
    ask_integer_in_range,
    ask_non_negative_integer,
)


def test_ask_non_negative_integer_accepts_valid_value() -> None:
    with patch("builtins.input", return_value="100"):
        assert ask_non_negative_integer("Valor: ") == 100


def test_ask_non_negative_integer_retries_negative_value() -> None:
    with patch("builtins.input", side_effect=["-1", "50"]):
        assert ask_non_negative_integer("Valor: ") == 50


def test_ask_non_negative_integer_retries_invalid_text() -> None:
    with patch("builtins.input", side_effect=["abc", "25"]):
        assert ask_non_negative_integer("Valor: ") == 25


def test_ask_constellation_accepts_c6() -> None:
    with patch("builtins.input", return_value="6"):
        assert ask_constellation() == 6


def test_ask_constellation_retries_value_above_c6() -> None:
    with patch("builtins.input", side_effect=["7", "2"]):
        assert ask_constellation() == 2


def test_ask_guaranteed_accepts_yes() -> None:
    with patch("builtins.input", return_value="s"):
        assert ask_guaranteed() is True


def test_ask_guaranteed_accepts_no() -> None:
    with patch("builtins.input", return_value="n"):
        assert ask_guaranteed() is False


def test_ask_guaranteed_retries_invalid_answer() -> None:
    with patch("builtins.input", side_effect=["talvez", "s"]):
        assert ask_guaranteed() is True


def test_range_accepts_minimum() -> None:
    with patch("builtins.input", return_value="0"):
        assert ask_integer_in_range("Pity: ", 0, 89) == 0


def test_range_accepts_maximum() -> None:
    with patch("builtins.input", return_value="89"):
        assert ask_integer_in_range("Pity: ", 0, 89) == 89


def test_range_rejects_negative() -> None:
    with patch("builtins.input", side_effect=["-1", "50"]):
        assert ask_integer_in_range("Pity: ", 0, 89) == 50


def test_range_rejects_above_maximum() -> None:
    with patch("builtins.input", side_effect=["90", "75"]):
        assert ask_integer_in_range("Pity: ", 0, 89) == 75


def test_range_rejects_invalid_text() -> None:
    with patch("builtins.input", side_effect=["abc", "25"]):
        assert ask_integer_in_range("Pity: ", 0, 89) == 25


def test_copies_range() -> None:
    with patch("builtins.input", side_effect=["8", "7"]):
        assert ask_integer_in_range("Cópias: ", 0, 7) == 7
