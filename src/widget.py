from datetime import datetime
from typing import Any

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(value: str) -> str:
    """
    Принимает строку с типом и номером карты/счёта и возвращает строку с маской.
    Для счёта ожидается формат: 'Счет <digits>'.
    Для карты: '<name> <digits>'.
    Некорректный ввод приводит к ValueError.
    """
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Некорректный ввод")

    text = value.strip()

    if text.startswith("Счет"):
        parts = text.split()
        if len(parts) != 2 or not parts[1].isdigit():
            raise ValueError("Некорректный ввод")
        return f"Счет {get_mask_account(parts[1])}"

    if " " not in text:
        raise ValueError("Некорректный ввод")

    name, number = text.rsplit(" ", 1)
    if not name.strip() or not number.isdigit():
        raise ValueError("Некорректный ввод")

    return f"{name} {get_mask_card_number(number)}"


def get_date(value: str) -> str:
    """
    Преобразует ISO-дату ('YYYY-MM-DD' или 'YYYY-MM-DDTHH:MM:SS') в формат 'ДД.ММ.ГГГГ'.
    Некорректный ввод приводит к ValueError.
    """
    if not isinstance(value, str) or not value:
        raise ValueError("Некорректная дата")
    try:
        dt = datetime.fromisoformat(value)
    except Exception as exc:  # noqa: BLE001
        raise ValueError("Некорректная дата") from exc
    return dt.strftime("%d.%m.%Y")
