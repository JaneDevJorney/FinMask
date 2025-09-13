from datetime import datetime
from typing import Any, Dict, Iterable, List


def filter_by_state(items: Iterable[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Возвращает новый список словарей, отфильтрованный по значению ключа 'state'.
    """
    return [item for item in items if item.get("state") == state]


def sort_by_date(items: Iterable[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по ключу 'date' в ISO-формате.
    При отсутствии или некорректности даты выбрасывает ValueError.
    """
    items_list: List[Dict[str, Any]] = list(items)

    parsed_items = []
    for item in items_list:
        if "date" not in item or not item["date"]:
            raise ValueError("Отсутствует корректная дата")

        try:
            parsed_date = datetime.fromisoformat(item["date"])
        except Exception as exc:
            raise ValueError("Некорректный ISO-формат даты") from exc

        parsed_items.append((parsed_date, item))

    parsed_items.sort(key=lambda x: x[0], reverse=descending)
    return [it for _, it in parsed_items]
