import pytest

@pytest.fixture
def ops_mixed():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-03-01T10:00:00"},
        {"id": 2, "state": "CANCELED",  "date": "2023-12-31T23:59:59"},
        {"id": 3, "state": "EXECUTED",  "date": "2024-01-01T10:00:00"},
    ]

@pytest.fixture
def ops_equal_dates():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-01T10:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2024-01-01T10:00:00"},
    ]

@pytest.fixture
def ops_bad_not_a_date():
    return [{"id": 1, "state": "EXECUTED", "date": "not_a_date"}]

@pytest.fixture
def ops_bad_empty_date():
    return [{"id": 2, "state": "EXECUTED", "date": ""}]

@pytest.fixture
def ops_bad_missing_date():
    return [{"id": 3, "state": "EXECUTED"}]