from typing import Iterator, Dict, List


def filter_by_currency(transactions: List[Dict], currency_code: str) -> Iterator[Dict]:
    """
    Генератор, который поочередно возвращает транзакции,
    у которых код валюты совпадает с заданным.

    :param transactions: список транзакций (словарей)
    :param currency_code: код валюты (например, "USD")
    :return: итератор по транзакциям
    """
    for transaction in transactions:
        if (
            "operationAmount" in transaction
            and "currency" in transaction["operationAmount"]
            and transaction["operationAmount"]["currency"].get("code") == currency_code
        ):
            yield transaction