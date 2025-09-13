from datetime import datetime
from typing import Any, Dict, Iterable, List


def filter_by_state(items: Iterable[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Возвращает новый список словарей, отфильтрованный по значению ключа 'state'.

    По умолчанию фильтрует по 'EXECUTED'.
    """
    return [item for item in items if item.get("state") == state]


def sort_by_date(items: Iterable[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по ключу 'date' в ISO-формате.

    Аргументы:
        items: коллекция словарей с ключом 'date' (ISO-строка).
        descending: порядок сортировки; True — по убыванию, False — по возрастанию.

    При отсутствии корректной даты выбрасывает ValueError.
    """
    def parse(item: Dict[str, Any]) -> datetime:
        value = item.get("date")
        if not value:
            raise ValueError("Отсутствует корректная дата")
        try:
            return datetime.fromisoformat(value)
        except Exception as exc:
            raise ValueError("Некорректный ISO-формат даты") from exc

    return sorted(items, key=parse, reverse=descending)