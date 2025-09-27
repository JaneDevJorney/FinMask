import json
from pathlib import Path


def load_transactions(file_path: str) -> list[dict]:
    """
    Загружает список транзакций из JSON-файла.
    Если файл не найден, пустой или не список — возвращает [].
    """
    path = Path(file_path)

    if not path.exists():
        return []

    try:
        with path.open(encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
    except (json.JSONDecodeError, OSError):
        return []

    return []
