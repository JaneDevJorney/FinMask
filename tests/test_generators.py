import pytest
from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator,
)


def test_filter_by_currency_usd(sample_transactions):
    usd_iter = filter_by_currency(sample_transactions, "USD")
    result = list(usd_iter)

    assert len(result) == 2
    assert all(
        tx["operationAmount"]["currency"]["code"] == "USD"
        for tx in result
    )


def test_filter_by_currency_eur(sample_transactions):
    eur_iter = filter_by_currency(sample_transactions, "EUR")
    result = list(eur_iter)

    assert len(result) == 1
    assert result[0]["operationAmount"]["currency"]["code"] == "EUR"


def test_filter_by_currency_empty(sample_transactions):
    gbp_iter = filter_by_currency(sample_transactions, "GBP")
    result = list(gbp_iter)

    assert result == []


def test_filter_by_currency_empty_list():
    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_transaction_descriptions_all(sample_transactions):
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
    ]


def test_transaction_descriptions_empty():
    empty_transactions = [{}]
    descriptions = list(transaction_descriptions(empty_transactions))
    assert descriptions == []


def test_card_number_generator_basic():
    result = list(card_number_generator(1, 3))
    assert result == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
    ]


def test_card_number_generator_formatting():
    result = list(card_number_generator(1234567890123456, 1234567890123456))
    assert result == ["1234 5678 9012 3456"]


@pytest.mark.parametrize(
    "start,end,expected_exception,match",
    [
        (0, 5, ValueError, "вне допустимого диапазона"),
        (1, 10**18, ValueError, "вне допустимого диапазона"),
        (10, 5, ValueError, "start должен быть <= end"),
        ("a", 5, ValueError, "start и end должны быть целыми числами"),
    ],
)
def test_card_number_generator_invalid(start, end, expected_exception, match):
    with pytest.raises(expected_exception, match=match):
        list(card_number_generator(start, end))