from datetime import datetime
from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(item: str) -> str:
    """
    Функция принимает строку с номером карты или счета
    и возвращает замаскированный номер
    """
    item = item.strip()

    if item.lower().startswith(("счет", "счёт")):
        parts = item.split(maxsplit=1)
        if len(parts) != 2:
            raise ValueError("Ожидается формат: 'Счет <номер>'")
        number = parts[1].replace(" ", "")
        masked = get_mask_account(number)
        return f"Счет {masked}"
    else:
        try:
            name, number = item.rsplit(maxsplit=1)
        except ValueError as exc:
            raise ValueError("Ожидается формат: '<Имя> <Номер>'") from exc
        number = number.replace(" ", "")
        masked = get_mask_card_number(number)
        return f"{name} {masked}"


def get_date(item: str) -> str:
    """
    Функция принимает дату в ISO-формате
    и возвращает строку в формате ДД.ММ.ГГГГ.
    """
    item = item.strip()
    try:
        dt = datetime.fromisoformat(item)
    except Exception as exc:
        raise ValueError("Некорректный ISO-формат даты") from exc
    return dt.strftime("%d.%m.%Y")


if __name__ == "__main__":
    print(get_date("2024-03-11T02:26:18.671407"))
