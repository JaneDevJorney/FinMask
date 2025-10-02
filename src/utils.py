from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any

LOGS_DIR = Path(__file__).resolve().parent.parent / "logs"
LOGS_DIR.mkdir(exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.propagate = False

_utils_log_file = LOGS_DIR / "utils.log"
_utils_handler = logging.FileHandler(
    _utils_log_file, mode="w", encoding="utf-8"
)
_utils_handler.setLevel(logging.DEBUG)

_utils_formatter = logging.Formatter(
    "%(asctime)s [%(name)s] %(levelname)s: %(message)s"
)
_utils_handler.setFormatter(_utils_formatter)

if not logger.handlers:
    logger.addHandler(_utils_handler)


def load_transactions(path: str) -> list[dict[str, Any]]:
    """Читает JSON-файл с транзакциями.

    Возвращает список словарей. Если файл пустой, содержит не-список,
    повреждён или не найден — возвращает [].
    """
    logger.debug("load_transactions: path=%s", path)

    json_path = Path(path)
    if not json_path.exists():
        logger.error("File not found: %s", path)
        return []

    try:
        content = json_path.read_text(encoding="utf-8").strip()
        if not content:
            logger.info("Empty JSON file: %s", path)
            return []

        data = json.loads(content)
        if isinstance(data, list):
            logger.info("Loaded %d transactions from %s", len(data), path)
            return data

        logger.error("JSON root is not a list: %s", type(data).__name__)
        return []
    except json.JSONDecodeError as exc:
        logger.error("Invalid JSON in %s: %s", path, exc)
        return []
    except OSError as exc:
        logger.error("I/O error while reading %s: %s", path, exc)
        return []
