from typing import List, Dict, Union

from tabulate import tabulate


def format_table(rows: List[Dict[str, Union[str, int, float]]]) -> str:
    """
    Форматирует список словарей в виде таблицы для отображения в консоли.
    """
    if not rows:
        return "⚠️ Нет данных для отображения."

    headers = rows[0].keys()
    table = [row.values() for row in rows]

    return tabulate(
        table,
        headers=headers,
        tablefmt="grid",
        floatfmt=".3f"
    )
