import os
import sys
import pytest

# Добавляем src в PYTHONPATH, чтобы тесты видели проектные модули
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@pytest.fixture
def sample_transactions():
    """Пример набора транзакций для тестов"""
    return [
        {
            "id": 1,
            "operationAmount": {"amount": "100", "currency": {"code": "USD"}},
            "description": "Перевод организации",
        },
        {
            "id": 2,
            "operationAmount": {"amount": "200", "currency": {"code": "EUR"}},
            "description": "Перевод со счета на счет",
        },
        {
            "id": 3,
            "operationAmount": {"amount": "300", "currency": {"code": "USD"}},
            "description": "Перевод с карты на карту",
        },
    ]