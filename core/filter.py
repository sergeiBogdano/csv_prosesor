from typing import List, Dict, Union, Callable, Tuple

Row = Dict[str, Union[str, int, float]]
OperatorFunction = Callable[[Union[str, int, float], Union[str, int, float]], bool]


def parse_filter_condition(condition: str) -> Tuple[str, str, str]:
    """
    Разбирает строку фильтрации в формате:
    column=value / column>value / column<value / column>=value / column<=value.
    """
    for op in [">=", "<=", ">", "<", "="]:
        if op in condition:
            column, value = condition.split(op, 1)
            return column.strip(), op, value.strip()
    raise ValueError(
        "Условие фильтрации должно содержать один из операторов: "
        "=, <, >, >=, <="
    )


def compare(operator: str) -> OperatorFunction:
    """
    Возвращает функцию сравнения по оператору.
    """
    ops: Dict[str, OperatorFunction] = {
        "=": lambda a, b: a == b,
        ">": lambda a, b: a > b,
        "<": lambda a, b: a < b,
        ">=": lambda a, b: a >= b,
        "<=": lambda a, b: a <= b,
    }
    if operator not in ops:
        raise ValueError(f"Неподдерживаемый оператор: {operator}")
    return ops[operator]


def filter_data(
    rows: List[Row],
    column: str,
    operator: str,
    raw_value: str
) -> List[Row]:
    """
    Фильтрует строки по значению в колонке, используя оператор.
    """
    if not rows:
        return []

    sample_value = rows[0].get(column)
    if sample_value is None:
        raise ValueError(f"Колонка '{column}' не найдена в данных")

    try:
        if isinstance(sample_value, int):
            value = int(raw_value)
        elif isinstance(sample_value, float):
            value = float(raw_value)
        else:
            value = raw_value
    except Exception:
        value = raw_value

    op_func = compare(operator)
    return [row for row in rows if op_func(row[column], value)]
