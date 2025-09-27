# Проект FinMask

## Описание
**FinMask** — учебное приложение на Python для работы с данными банковских операций.  
В проекте реализованы:
- функции-генераторы для фильтрации транзакций, получения описаний транзакций и генерации номеров карт;
- декоратор `@log` для логирования работы функций.

Тесты обеспечивают 100% покрытие кода.

---

## Установка
1. Клонируйте репозиторий:
   ```bash
   git clone git@github.com:JaneDevJorney/FinMask.git
   ```
2. Перейдите в папку проекта:
    ```bash
    cd FinMask
    ```
3.	Установите зависимости (через Poetry):
    ```bash
    poetry install
    ```
## Использование

### Модуль generators

В проекте реализован модуль `generators`, содержащий функции для работы с транзакциями.


### Функции:

- `filter_by_currency(transactions, currency_code)` — возвращает транзакции с указанным кодом валюты.
- `transaction_descriptions(transactions)` — генератор, возвращающий описание каждой транзакции.
- `card_number_generator(start, end)` — генератор номеров карт в формате `XXXX XXXX XXXX XXXX`.

### Пример 
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

### Модуль decorators

В проекте реализован модуль `decorators`, содержащий декоратор @log.

### Возможности

- Логирование успешного выполнения функций.
- Логирование ошибок с указанием типа исключения и входных аргументов.
- Поддержка вывода логов в консоль или запись в файл.

### Пример использования
```python
from src.decorators import log

@log()
def divide(a, b):
    return a / b

@log(filename="mylog.txt")
def add(a, b):
    return a + b

print(divide(10, 2))   
print(add(3, 7))       
print(divide(10, 0))
```

### Пример содержимого mylog.txt
```
add ok
```

## Тестирование
1. Запуск тестов:
   ```bash
   poetry run pytest -q
   ```
2. Запуск тестов с покрытием:  
   ```bash
   poetry run pytest --cov=src --cov-report=html
   ```
3. HTML-отчет доступен в папке htmlcov/.

## Запуск демо
Для запуска демонстрации работы проекта:
```bash
poetry run python main.py