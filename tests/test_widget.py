from datetime import datetime
from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(item: str) -> str:
    """
    Принимает строку с номером карты или счёта и возвращает замаскированный номер.

    Форматы:
    - "<Название карты> <номер_карты>"
    - "Счет <номер_счёта>"

    На некорректный ввод выбрасывает ValueError.
    """
    item = item.strip()
    if not item:
        raise ValueError("Ожидается формат: '<Имя> <Номер>'")

    if item.lower().startswith(("счет", "счёт")):
        parts = item.split(maxsplit=1)
        if len(parts) != 2:
            raise ValueError("Ожидается формат: 'Счет <номер>'")
        number = parts[1].replace(" ", "")
        if not number.isdigit():
            raise ValueError("Номер счета должен содержать только цифры")
        return f"Счет {get_mask_account(number)}"

    try:
        name, number = item.rsplit(maxsplit=1)
    except ValueError as exc:
        raise ValueError("Ожидается формат: '<Имя> <Номер>'") from exc

    number = number.replace(" ", "")
    if not number.isdigit():
        raise ValueError("Номер карты должен содержать только цифры")

    return f"{name} {get_mask_card_number(number)}"


def get_date(item: str) -> str:
    """
    Принимает дату в ISO-формате и возвращает строку в формате ДД.ММ.ГГГГ.

    Допустимые входы: "YYYY-MM-DD", "YYYY-MM-DDTHH:MM:SS[.ffffff][±HH:MM]".
    На некорректный ввод выбрасывает ValueError.
    """
    item = item.strip()
    try:
        dt = datetime.fromisoformat(item)
    except Exception as exc:
        raise ValueError("Некорректный ISO-формат даты") from exc
    return dt.strftime("%d.%m.%Y")
