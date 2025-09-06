# Проект "FinMask"

## Описание:

Проект **"FinMask"** — это учебное приложение на Python для работы с данными банковских операций.  
В рамках проекта реализованы функции фильтрации и сортировки операций.

## Установка:

1. Клонируйте репозиторий:
```
git clone git@github.com:JaneDevJorney/FinMask.git
```
2. Перейдите в папку проекта:
```
cd FinMask
```

3. Установите зависимости (через Poetry или pip):
```
poetry install 
```

## Использование:

Примеры работы функций находятся в модуле `processing.py`.

### filter_by_state

Фильтрует список словарей по значению ключа `state`.

**Пример:**
```python
from src.processing import filter_by_state

data = [
    {"id": 1, "state": "EXECUTED"},
    {"id": 2, "state": "CANCELED"},
]

print(filter_by_state(data))
# [{'id': 1, 'state': 'EXECUTED'}]

print(filter_by_state(data, "CANCELED"))
# [{'id': 2, 'state': 'CANCELED'}]
```
### sort_by_date

Сортирует список словарей по значению ключа date.

**Пример:**
```python
from src.processing import sort_by_date

data = [
    {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]

print(sort_by_date(data))
# [{'id': 1, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#  {'id': 2, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

print(sort_by_date(data, descending=False))
# [{'id': 2, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#  {'id': 1, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
```

## Документация:

Подробное описание функций и примеры можно найти в модуле src/processing.py.

## Лицензия:

Проект распространяется под лицензией MIT.

## Линтеры

В проекте настроены проверки качества кода с помощью **flake8** и **mypy**.
Результаты последних прогонов сохранены в файлах:
- flake8_report.txt
- mypy_report.txt

Запуск проверок:  
```bash
poetry run flake8 .
poetry run mypy src