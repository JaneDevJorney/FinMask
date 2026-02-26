from datetime import datetime
import re

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(item: str) -> str:
    """
    Функция принимает строку с типом и номером карты или счета,
    маскирует номер в зависимости от типа.
    """
    item = item.strip()

    if item.lower().startswith("счет"):
        parts = item.split()
        if len(parts) != 2:
            raise ValueError("Некорректный формат строки со счётом")
        name, number = parts
        return f"{name} {get_mask_account(number)}"

    parts = item.rsplit(" ", 1)
    if len(parts) != 2:
        raise ValueError("Некорректный формат строки с картой")

    name, number = parts
    return f"{name} {get_mask_card_number(number)}"


def get_date(item: str) -> str:
    """
    Принимает дату (ISO-формата или ДД.ММ.ГГГГ)
    и возвращает её в формате ДД.ММ.ГГГГ.
    """
    s = item.strip()

    # Если уже в формате ДД.ММ.ГГГГ
    if re.fullmatch(r"\d{2}\.\d{2}\.\d{4}", s):
        return s

    # Пробуем ISO-формат
    try:
        dt = datetime.fromisoformat(s)
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        pass

    # Пробуем просто YYYY-MM-DD
    try:
        dt = datetime.strptime(s, "%Y-%m-%d")
        return dt.strftime("%d.%m.%Y")
    except ValueError as exc:
        raise ValueError("Некорректный формат даты") from exc

