# Проект "FinMask"

## Описание
**FinMask** — учебное приложение на Python для работы с данными банковских операций.  
В проекте реализованы функции-генераторы для фильтрации, получения описаний транзакций и генерации номеров карт.  
Тесты обеспечивают 100% покрытие кода.

## Установка
1. Клонируйте репозиторий:
   ```bash
   git clone git@github.com:JaneDevJorney/FinMask.git
   ```
2. Перейдите в папку проекта:
   ```bash
   cd FinMask
   ```
3. Установите зависимости (через Poetry):
   ```bash
   poetry install
   ```
   
## Использование

Примеры работы функций находятся в модуле src/generators.py.

### Функции:
- `filter_by_currency(transactions, currency_code)` — возвращает транзакции с указанным кодом валюты.
- `transaction_descriptions(transactions)` — генератор, возвращающий описание каждой транзакции.
- `card_number_generator(start, end)` — генератор номеров карт в формате XXXX XXXX XXXX XXXX.

### Пример:
```python
from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator,
)

transactions = [
    {"id": 1, "operationAmount": {"amount": "100", "currency": {"code": "USD"}}, "description": "Перевод"},
    {"id": 2, "operationAmount": {"amount": "200", "currency": {"code": "EUR"}}, "description": "Перевод со счета"},
]

# Фильтрация по валюте
usd = list(filter_by_currency(transactions, "USD"))
print(usd)

# Описание транзакций
desc = list(transaction_descriptions(transactions))
print(desc)

# Генерация номеров карт
for number in card_number_generator(1, 3):
    print(number)
```

## Тестирование

Для запуска тестов с проверкой покрытия:
  ```bash
  poetry run pytest --cov=src --cov-report=term-missing -v 
  ```
Покрытие тестами: 100%