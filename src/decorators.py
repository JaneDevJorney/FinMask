import functools
import sys
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования вызовов функций.

    Логирует:
    - имя функции и результат выполнения (если успешно);
    - имя функции, тип ошибки и входные параметры (если произошла ошибка).

    :param filename: путь к файлу для логирования. Если None — вывод в консоль.
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                _write_log(message, filename)
                return result
            except Exception as e:
                message = (
                    f"{func.__name__} error: {type(e).__name__}. "
                    f"Inputs: {args}, {kwargs}"
                )
                _write_log(message, filename)
                raise
        return wrapper

    return decorator


def _write_log(message: str, filename: Optional[str]) -> None:
    """Вспомогательная функция для записи лога в файл или консоль."""
    if filename:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(message + "\n")
    else:
        print(message, file=sys.stdout)
