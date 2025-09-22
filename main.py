from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator,
)
from src.decorators import log


def main():
    # Демонстрация генераторов
    transactions = [
        {"id": 1, "operationAmount": {"amount": "100", "currency": {"code": "USD"}}, "description": "Перевод"},
        {"id": 2, "operationAmount": {"amount": "200", "currency": {"code": "EUR"}}, "description": "Снятие"},
    ]

    print("Фильтрация по валюте:")
    print(list(filter_by_currency(transactions, "USD")))

    print("\nОписание транзакций:")
    print(list(transaction_descriptions(transactions)))

    print("\nГенерация номеров карт:")
    for number in card_number_generator(1, 3):
        print(number)

    # Демонстрация декоратора
    @log()
    def divide(a: int, b: int) -> float:
        return a / b

    print("\nДемонстрация декоратора:")
    try:
        print(divide(10, 2))
        print(divide(10, 0))
    except ZeroDivisionError:
        print("Ошибка деления на ноль корректно зафиксирована логгером")


if __name__ == "__main__":
    main()