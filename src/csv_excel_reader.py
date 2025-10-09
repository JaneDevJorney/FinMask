from typing import List, Dict
import pandas as pd


def read_transactions_csv(path: str) -> List[Dict]:
    """Считывает финансовые операции из CSV-файла и возвращает список словарей."""
    df = pd.read_csv(path)
    return df.to_dict(orient="records")


def read_transactions_excel(path: str) -> List[Dict]:
    """Считывает финансовые операции из Excel-файла (.xlsx) и возвращает список словарей."""
    df = pd.read_excel(path)  # engine=openpyxl ставится автоматически, если пакет установлен
    return df.to_dict(orient="records")
