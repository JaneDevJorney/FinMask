def get_mask_card_number(card_number: int | str) -> str:
    """
    Маскирует номер банковской карты.

    Оставляет первые 6 и последние 4 цифры,
    остальные заменяет на звездочки.
    Результат делится пробелами по блокам по 4 символа.
    """
    card_number_str = str(card_number)
    first_six_digits = card_number_str[:6]
    last_four_digits = card_number_str[-4:]
    middle_hidden_digits = "*" * (len(card_number_str) - 10)
    masked_number = first_six_digits + middle_hidden_digits + last_four_digits
    return " ".join(masked_number[i:i+4] for i in range(0, len(masked_number), 4))


def get_mask_account(account_number: int | str) -> str:
    """
    Маскирует номер банковского счета.

    Оставляет только последние 4 цифры,
    перед ними добавляет две звездочки.
    """
    account_number_str = str(account_number)
    last_four_digits = account_number_str[-4:]
    return f"**{last_four_digits}"
