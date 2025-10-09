  # FinMask

Проект для работы с финансовыми данными и маскирования номеров карт и счетов.

## Новая функциональность

Добавлены функции для чтения финансовых операций из файлов **CSV** и **Excel**:

- `read_transactions_csv(path: str) -> list[dict]` — считывает транзакции из CSV-файла.  
- `read_transactions_excel(path: str) -> list[dict]` — считывает транзакции из Excel-файла.

Каждая функция возвращает список словарей с данными о транзакциях.

### Пример использования

```python
from src.csv_excel_reader import read_transactions_csv, read_transactions_excel

csv_data = read_transactions_csv("transactions.csv")
excel_data = read_transactions_excel("transactions_excel.xlsx")

print(len(csv_data), "строк из CSV")
print(len(excel_data), "строк из Excel")
```

### Тестирование
Запуск тестов:
```bash
pytest -v
```

### Проверка кода
Линтер:
```bash
poetry run flake8
```
Сортировка импортов:
```bash
poetry run isort .
```