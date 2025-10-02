import logging
import os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(
    "logs/masks.log", mode="w", encoding="utf-8"
)
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int | str) -> str:
    """
    Маскирует номер банковской карты.

    Оставляет первые 6 и последние 4 цифры,
    остальные заменяет на звездочки.
    Результат делится пробелами по блокам по 4 символа.
    """
    try:
        card_number_str = str(card_number)
        first_six_digits = card_number_str[:6]
        last_four_digits = card_number_str[-4:]
        middle_hidden_digits = "*" * (len(card_number_str) - 10)

        masked_number = (
            first_six_digits
            + middle_hidden_digits
            + last_four_digits
        )

        result = " ".join(
            masked_number[i:i + 4] for i in range(0, len(masked_number), 4)
        )
        logger.debug("Замаскирован номер карты: %s", result)
        return result
    except Exception as e:
        logger.error("Ошибка при маскировании карты: %s", e)
        raise


def get_mask_account(account_number: int | str) -> str:
    """
    Маскирует номер банковского счета.

    Оставляет только последние 4 цифры,
    перед ними добавляет две звездочки.
    """
    try:
        account_number_str = str(account_number)
        last_four_digits = account_number_str[-4:]
        result = f"**{last_four_digits}"
        logger.debug("Замаскирован номер счёта: %s", result)
        return result
    except Exception as e:
        logger.error("Ошибка при маскировании счёта: %s", e)
        raise
