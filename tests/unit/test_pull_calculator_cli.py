from unittest.mock import patch

from iagocava_genshin.apps.pull_calculator.cli import (
    ask_constellation,
    ask_guaranteed,
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
