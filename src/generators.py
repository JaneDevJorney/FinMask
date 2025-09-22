from typing import Dict, Iterator, List


def filter_by_currency(
    transactions: List[Dict],
    currency_code: str,
) -> Iterator[Dict]:
    """
    Генератор, который поочередно возвращает транзакции,
    у которых код валюты совпадает с заданным.
    """
    for transaction in transactions:
        if (
            "operationAmount" in transaction
            and "currency" in transaction["operationAmount"]
            and transaction["operationAmount"]["currency"].get("code")
            == currency_code
        ):
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Генератор, который поочередно возвращает описание каждой транзакции.
    """
    for transaction in transactions:
        description = transaction.get("description")
        if description:
            yield description


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генератор номеров карт в формате 'XXXX XXXX XXXX XXXX'.

    Порождает номера от `start` до `end` включительно.
    """
    min_val = 1
    max_val = 9_999_999_999_999_999

    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("start и end должны быть целыми числами")
    if start < min_val or end < min_val or start > max_val or end > max_val:
        raise ValueError("start/end вне допустимого диапазона")
    if start > end:
        raise ValueError("start должен быть <= end")

    for n in range(start, end + 1):
        s = f"{n:016d}"  # 16 цифр с лидирующими нулями
        grouped = " ".join(s[i:i + 4] for i in range(0, 16, 4))
        yield grouped
