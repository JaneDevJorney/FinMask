from src.generators import filter_by_currency, transaction_descriptions

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


# --------- ТЕСТЫ ДЛЯ filter_by_currency ---------
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


# --------- ТЕСТЫ ДЛЯ transaction_descriptions ---------
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