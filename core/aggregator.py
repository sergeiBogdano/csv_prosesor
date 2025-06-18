from typing import List, Dict, Union, Callable, Tuple

Row = Dict[str, Union[str, int, float]]
AggregatorFunction = Callable[[List[Union[int, float]]], float]


def parse_aggregate_condition(condition: str) -> Tuple[str, str]:
    """
    Разбирает условие агрегации в формате: column=operation.
    """
    if "=" not in condition:
        raise ValueError(
            "Условие агрегации должно быть в формате: column=operation"
        )
    column, operation = condition.split("=", 1)
    return column.strip(), operation.strip().lower()


def aggregate_data(
    rows: List[Row],
    column: str,
    operation: str
) -> float:
    """
    Выполняет агрегацию по колонке: avg, min, max.
    """
    if not rows:
        raise ValueError("Нет данных для агрегации")

    values = [
        row[column]
        for row in rows
        if isinstance(row.get(column), (int, float))
    ]

    if not values:
        raise ValueError(
            f"Колонка '{column}' не содержит числовых значений"
        )

    aggregators: Dict[str, AggregatorFunction] = {
        "avg": lambda nums: sum(nums) / len(nums),
        "min": min,
        "max": max,
    }

    if operation not in aggregators:
        raise ValueError(f"Неподдерживаемая операция: {operation}")

    return round(aggregators[operation](values), 3)
