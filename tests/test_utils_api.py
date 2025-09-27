import json
import pytest
from unittest.mock import patch, MagicMock
from src.utils import load_transactions
from src.external_api import convert_to_rub


def test_load_transactions_valid_file(tmp_path):
    data = [{"id": 1, "amount": "100"}]
    file_path = tmp_path / "operations.json"
    file_path.write_text(json.dumps(data), encoding="utf-8")

    result = load_transactions(str(file_path))
    assert result == data


def test_load_transactions_empty_file(tmp_path):
    file_path = tmp_path / "empty.json"
    file_path.write_text("", encoding="utf-8")

    result = load_transactions(str(file_path))
    assert result == []


def test_load_transactions_invalid_json(tmp_path):
    file_path = tmp_path / "invalid.json"
    file_path.write_text("{not valid}", encoding="utf-8")

    result = load_transactions(str(file_path))
    assert result == []


def test_load_transactions_not_list(tmp_path):
    file_path = tmp_path / "not_list.json"
    file_path.write_text(json.dumps({"id": 1}), encoding="utf-8")

    result = load_transactions(str(file_path))
    assert result == []


def test_convert_to_rub_rub():
    transaction = {
        "operationAmount": {"amount": "150", "currency": {"code": "RUB"}}
    }
    result = convert_to_rub(transaction)
    assert result == 150.0


@patch("src.external_api.requests.get")
def test_convert_to_rub_usd(mock_get):
    transaction = {
        "operationAmount": {"amount": "10", "currency": {"code": "USD"}}
    }

    mock_response = MagicMock()
    mock_response.json.return_value = {"result": 950.0}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = convert_to_rub(transaction)
    assert result == 950.0
    mock_get.assert_called_once()


@patch("src.external_api.requests.get")
def test_convert_to_rub_eur(mock_get):
    transaction = {
        "operationAmount": {"amount": "20", "currency": {"code": "EUR"}}
    }

    mock_response = MagicMock()
    mock_response.json.return_value = {"result": 2100.0}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = convert_to_rub(transaction)
    assert result == 2100.0


def test_convert_to_rub_invalid_currency():
    transaction = {
        "operationAmount": {"amount": "50", "currency": {"code": "GBP"}}
    }

    with pytest.raises(ValueError, match="Unsupported currency"):
        convert_to_rub(transaction)

def test_load_transactions_file_not_found():
    from src.utils import load_transactions
    data = load_transactions("data/__no_such_file__.json")
    assert data == []
