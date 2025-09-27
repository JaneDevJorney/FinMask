                         # Проект FinMask

## Описание
**FinMask** — Учебный проект для работы с банковскими транзакциями: чтение из JSON, маскирование данных и конвертация валют через внешний API.

---

## Установка и запуск
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
4. Активируйте виртуальное окружение:
    ```bash
    poetry shell
    ```

## Использование

### Загрузка транзакций из JSON

### Функция load_transactions(path) (модуль src/utils.py):
- Читает JSON-файл и возвращает `list[dict]`.
- Если файл пустой, содержит не-список или не существует — возвращает пустой список.

### Пример 
```python
from src.utils import load_transactions

transactions = load_transactions("data/operations.json")
print(transactions)
```
## Конвертация валюты в рубли

### Функция:
`convert_to_rub(transaction) (модуль src/external_api.py):`

- Если валюта RUB → возвращает сумму без запроса.
- Если USD или EUR → обращается к Exchange Rates Data API и возвращает сумму в рублях.
- Если валюта не поддерживается → выбрасывает ValueError.

### Пример 
```python
from src.external_api import convert_to_rub

tx = {"operationAmount": {"amount": "10", "currency": {"code": "USD"}}}
print(convert_to_rub(tx))  
```

## Конфигурация

Для работы с API требуется файл .env (в корне проекта).
### Пример в .env.example:
```EXCHANGE_API_KEY=your_api_key_here
EXCHANGE_API_URL=https://api.apilayer.com/exchangerates_data/convert
```

## Тестирование
1. Запуск тестов с покрытием:
    ```bash
    poetry run pytest --cov=src --cov-report=term-missing -v
    ```
2. Проверка стиля кода:   
   ```bash
   poetry run flake8 .
   ```
3. Проверка импортов:
   ```bash
   poetry run isort . --check-only
   ```
4. Статический анализ:
    ```bash
   poetry run mypy src
   ```
## Что сделано
- Добавлен модуль src/utils.py: load_transactions(path)
- Читает JSON, возвращает list[dict].
- Для пустого/не-списка/ошибки/отсутствия файла — возвращает [].
- Добавлен модуль src/external_api.py: convert_to_rub(transaction)
- Конвертация USD/EUR → RUB через Exchange Rates Data API.
- Для RUB — сумма без запроса.
- Добавлен .env.example (переменные: EXCHANGE_API_KEY, EXCHANGE_API_URL).
- Тесты tests/test_utils_api.py:
- load_transactions: валидный файл / пустой / не-JSON / не-список / файл не найден.
- convert_to_rub: кейсы RUB / USD / EUR / невалидная валюта (mock requests).
- Обновлён .gitignore (игнор .env, coverage, IDE, виртуалки).
- Покрытие тестами: 100% по src.   