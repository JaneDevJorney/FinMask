from typing import List, Dict


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа "state".

    :param data: список словарей, описывающих операции
    :param state: значение для фильтрации (по умолчанию "EXECUTED")
    :return: новый список словарей, где значение по ключу "state" совпадает с параметром state
    """
    result = []

    for item in data:
        if isinstance(item, dict) and item.get("state") == state:
            result.append(item)

    return result


if __name__ == "__main__":
    sample = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    ]

    print("EXECUTED:", filter_by_state(sample))
    print("CANCELED:", filter_by_state(sample, "CANCELED"))
