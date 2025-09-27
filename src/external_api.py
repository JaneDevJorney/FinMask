import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")


def convert_to_rub(transaction: dict) -> float:
    """
    Конвертирует сумму транзакции в рубли.
    Поддерживаемые валюты: RUB, USD, EUR.
    """
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    if currency in ("USD", "EUR"):
        response = requests.get(
            f"{BASE_URL}/convert",
            params={
                "to": "RUB",
                "from": currency,
                "amount": amount,
            },
            headers={"apikey": API_KEY},
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
        return float(data["result"])

    raise ValueError(f"Unsupported currency: {currency}")
