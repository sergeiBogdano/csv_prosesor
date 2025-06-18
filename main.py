import argparse
import sys

from core.loader import load_csv
from core.filter import parse_filter_condition, filter_data
from core.aggregator import (
    parse_aggregate_condition,
    aggregate_data,
)
from core.formatter import format_table


def main():
    parser = argparse.ArgumentParser(
        description="CSV Processor CLI Tool"
    )

    parser.add_argument(
        "--file",
        required=True,
        help="Путь к CSV-файлу"
    )
    parser.add_argument(
        "--filter",
        help=(
            "Фильтрация в формате: "
            "column=value, column>value, column<value"
        )
    )
    parser.add_argument(
        "--aggregate",
        help=(
            "Агрегация в формате: column=operation "
            "(operation: avg, min, max)"
        )
    )

    args = parser.parse_args()

    try:
        data = load_csv(args.file)
        if not data:
            print("❌ CSV-файл пустой или не содержит данных.")
            sys.exit(1)
    except Exception as e:
        print(f"❌ Ошибка при чтении файла: {e}")
        sys.exit(1)

    if args.filter:
        try:
            column, operator, value = parse_filter_condition(args.filter)
            data = filter_data(data, column, operator, value)
        except Exception as e:
            print(f"❌ Ошибка в фильтрации: {e}")
            sys.exit(1)

    if args.aggregate:
        try:
            column, operation = parse_aggregate_condition(args.aggregate)
            result = aggregate_data(data, column, operation)
            print(
                f"\n📊 Результат агрегации: "
                f"{operation.upper()} по '{column}' = {result}"
            )
        except Exception as e:
            print(f"❌ Ошибка агрегации: {e}")
            sys.exit(1)
    else:
        if data:
            print(format_table(data))
        else:
            print("⚠️ Нет данных для отображения.")


if __name__ == "__main__":
    main()
