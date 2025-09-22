## Модуль decorators

В проекте реализован модуль `decorators`, содержащий декоратор `@log`.

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

print(divide(10, 2))   # Вывод в консоль: "divide ok"
print(add(3, 7))       # Запись в файл mylog.txt: "add ok"
print(divide(10, 0))   # Вывод в консоль: "divide error: ZeroDivisionError. Inputs: (10, 0), {}"
```
### Пример содержимого mylog.txt
add ok

### Тестирование
1.	Запуск тестов:
   ```bash
   poetry run pytest -q
   ``` 
2. Запуск тестов с покрытием:
   ```bash
   poetry run pytest --cov=src --cov-report=html
   ```
3.	HTML-отчет доступен в папке htmlcov/.
 