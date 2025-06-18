import csv
from typing import List, Dict, Union


def convert_value(value: str) -> Union[str, int, float]:
    """
    Преобразует строку к int или float, если возможно.
    В противном случае возвращает строку.
    """
    value = value.strip()
    try:
        if "." in value:
            return float(value)
        return int(value)
    except ValueError:
        return value


def load_csv(file_path: str) -> List[Dict[str, Union[str, int, float]]]:
    """
    Загружает CSV-файл и возвращает список словарей,
    автоматически определяя типы значений.
    """
    with open(file_path, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        result = []

        for row in reader:
            converted = {k: convert_value(v) for k, v in row.items()}
            result.append(converted)

        return result
