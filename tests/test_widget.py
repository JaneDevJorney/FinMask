import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "raw, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ],
)
def test_mask_account_card_card(raw, expected):
    assert mask_account_card(raw) == expected


@pytest.mark.parametrize(
    "raw, expected",
    [
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card_account(raw, expected):
    assert mask_account_card(raw) == expected


@pytest.mark.parametrize(
    "bad_input",
    [
        "",
        "Visa Platinum",
        "Счет ABCD",
        "Просто текст",
    ],
)
def test_mask_account_card_invalid_inputs(bad_input):
    with pytest.raises(ValueError):
        mask_account_card(bad_input)


def test_mask_account_card_no_space_raises():
    """Если строка без пробела — должна упасть с ValueError"""
    with pytest.raises(ValueError):
        mask_account_card("Visa")


def test_get_date_iso():
    assert get_date("2024-03-11T12:00:00") == "11.03.2024"


@pytest.mark.parametrize(
    "value, expected",
    [
        ("2024-03-11", "11.03.2024"),
        ("2024-03-11T00:00:00", "11.03.2024"),
    ],
)
def test_get_date_various_formats(value, expected):
    assert get_date(value) == expected


@pytest.mark.parametrize(
    "bad_value",
    [
        "",
        "abc",
        "32.13.2024",
        "2024/03/11",
        "11.03.2024",
    ],
)
def test_get_date_invalid_inputs(bad_value):
    with pytest.raises(ValueError):
        get_date(bad_value)

