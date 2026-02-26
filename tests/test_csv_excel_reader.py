import pytest
from unittest.mock import patch, MagicMock
from src.csv_excel_reader import read_transactions_csv, read_transactions_excel


@patch("pandas.read_csv")
def test_read_transactions_csv(mock_read_csv):
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"id": 1, "amount": 100}]
    mock_read_csv.return_value = mock_df

    result = read_transactions_csv("fake_path.csv")

    mock_read_csv.assert_called_once_with("fake_path.csv")
    assert result == [{"id": 1, "amount": 100}]


@patch("pandas.read_excel")
def test_read_transactions_excel(mock_read_excel):
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"id": 2, "amount": 200}]
    mock_read_excel.return_value = mock_df

    result = read_transactions_excel("fake_path.xlsx")

    mock_read_excel.assert_called_once_with("fake_path.xlsx")
    assert result == [{"id": 2, "amount": 200}]
