import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_card_mask_standard_16_str():
    """Стандартный 16-значный номер карты (строка)."""
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"


def test_card_mask_standard_16_int():
    """Стандартный 16-значный номер карты (int)."""
    assert get_mask_card_number(1234567890123456) == "1234 56** **** 3456"


@pytest.mark.parametrize(
    "num, expected",
    [
        ("123456789012", "1234 56** 9012"),
        ("9876543210", "9876 5432 10"),
    ],
)
def test_card_various_lengths(num, expected):
    """Нестандартные длины номера карты."""
    assert get_mask_card_number(num) == expected


def test_card_mask_too_short_9_digits():
    """Карта из 9 цифр."""
    assert get_mask_card_number("123456789") == "1234 5667 89"


def test_card_mask_empty_string():
    """Пустая строка для карты."""
    assert get_mask_card_number("") == ""


def test_account_mask_standard_20_str():
    """Стандартный счёт (строка)."""
    assert get_mask_account("73654108430135874305") == "**4305"


def test_account_mask_standard_20_int():
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
    """Разные длины номеров счёта."""
    assert get_mask_account(acc) == expected


def test_account_empty_string():
    """Пустая строка для счёта."""
    assert get_mask_account("") == "**"