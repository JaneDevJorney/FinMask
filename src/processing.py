from datetime import datetime
from typing import Dict, List


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа "state".

    :param data: список словарей с операциями
    :param state: значение для фильтрации (по умолчанию "EXECUTED")
    :return: новый список словарей, у которых ключ "state" равен заданному значению
    """
    result = []
    for item in data:
        if isinstance(item, dict) and item.get("state") == state:
            result.append(item)
    return result


def sort_by_date(data: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по значению ключа "date".

    :param data: список словарей с операциями
    :param descending: порядок сортировки (по умолчанию True — по убыванию)
    :return: новый список словарей, отсортированный по дате
    """
    data_copy = data.copy()
    for i in range(len(data_copy)):
        for j in range(i + 1, len(data_copy)):
            date_i = datetime.fromisoformat(data_copy[i]["date"])
            date_j = datetime.fromisoformat(data_copy[j]["date"])
            if descending and date_i < date_j:
                data_copy[i], data_copy[j] = data_copy[j], data_copy[i]
            if not descending and date_i > date_j:
                data_copy[i], data_copy[j] = data_copy[j], data_copy[i]
    return data_copy


if __name__ == "__main__":
    sample = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    ]

    print("EXECUTED:", filter_by_state(sample))
    print("CANCELED:", filter_by_state(sample, "CANCELED"))

    print("\nПо убыванию (новые → старые):")
    print(sort_by_date(sample))

    print("\nПо возрастанию (старые → новые):")
    print(sort_by_date(sample, descending=False))
