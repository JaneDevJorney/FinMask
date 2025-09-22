# tests/conftest.py
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
# Добавим в путь и корень проекта, и папку src
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))