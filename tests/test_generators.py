from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)

transactions = [
    {
        "id": 1,
        "operationAmount": {"amount": "100", "currency": {"code": "USD"}},
        "description": "Перевод организации",
    },
    {
        "id": 2,
        "operationAmount": {"amount": "200", "currency": {"code": "EUR"}},
        "description": "Перевод со счета на счет",
    },
    {
        "id": 3,
        "operationAmount": {"amount": "300", "currency": {"code": "USD"}},
        "description": "Перевод с карты на карту",
    },
]


def test_filter_by_currency_usd():
    usd_iter = filter_by_currency(transactions, "USD")
    result = list(usd_iter)

    assert len(result) == 2
    assert all(
        tx["operationAmount"]["currency"]["code"] == "USD"
        for tx in result
    )


def test_filter_by_currency_eur():
    eur_iter = filter_by_currency(transactions, "EUR")
    result = list(eur_iter)

    assert len(result) == 1
    assert result[0]["operationAmount"]["currency"]["code"] == "EUR"


def test_filter_by_currency_empty():
    gbp_iter = filter_by_currency(transactions, "GBP")
    result = list(gbp_iter)
    assert result == []


def test_transaction_descriptions_all():
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
    ]


def test_transaction_descriptions_empty():
    empty_transactions = [{}]
    descriptions = list(transaction_descriptions(empty_transactions))
    assert descriptions == []


def test_card_number_generator_small_range():
    gen = card_number_generator(1, 5)
    result = list(gen)
    assert result == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]


def test_card_number_generator_formatting():
    gen = card_number_generator(123456789012345, 123456789012345)
    got = next(gen)
    # 123456789012345 -> '0123456789012345'
    assert got == "0123 4567 8901 2345"


def test_card_number_generator_bounds_and_errors():
    # start > end
    try:
        list(card_number_generator(5, 1))
        assert False, "ожидали ValueError"
    except ValueError:
        pass

    # ниже минимума
    try:
        list(card_number_generator(0, 2))
        assert False, "ожидали ValueError"
    except ValueError:
        pass

    # выше максимума
    try:
        list(card_number_generator(1, 10_000_000_000_000_000))
        assert False, "ожидали ValueError"
    except ValueError:
        pass
