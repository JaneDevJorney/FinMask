from src.widget import mask_account_card, get_date


def test_widget_visa():
    """Маскирование строки c картой Visa."""
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"


def test_widget_maestro():
    """Маскирование строки c картой Maestro."""
    assert mask_account_card("Maestro 7000792289606361") == "Maestro 7000 79** **** 6361"


def test_widget_account():
    """Маскирование строки со счётом."""
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"


def test_get_date_iso_to_ru():
    """ISO → ДД.ММ.ГГГГ."""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_get_date_already_ru():
    """Если уже ДД.ММ.ГГГГ — вернуть как есть."""
    assert get_date("11.03.2024") == "11.03.2024"
