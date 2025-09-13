import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_card_mask_standard_str():
    """Стандартный номер карты (строка)."""
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_card_mask_standard_int():
    """Стандартный номер карты (int)."""
    assert get_mask_card_number(7000792289606361) == "7000 79** **** 6361"


@pytest.mark.parametrize(
    "num, expected",
    [
        ("123456789012", "1234 56** 9012"),
        ("9876543210", "9876 5432 10"),
        ("123456789", "1234 5667 89"),
    ],
)
def test_card_various_lengths(num, expected):
    """Нестандартные длины номера карты."""
    assert get_mask_card_number(num) == expected


def test_card_empty_string():
    """Пустая строка для карты."""
    assert get_mask_card_number("") == ""


def test_account_mask_standard_str():
    """Стандартный счёт (строка)."""
    assert get_mask_account("73654108430135874305") == "**4305"


def test_account_mask_standard_int():
    """Стандартный счёт (int)."""
    assert get_mask_account(73654108430135874305) == "**4305"


@pytest.mark.parametrize(
    "acc, expected",
    [
        ("1234567890", "**7890"),
        ("1234", "**1234"),
        ("123", "**123"),
    ],
)
def test_account_various_lengths(acc, expected):
    """Разные длины счёта."""
    assert get_mask_account(acc) == expected


def test_account_empty_string():
    """Пустая строка для счёта."""
    assert get_mask_account("") == "**"
