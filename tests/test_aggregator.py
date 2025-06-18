from core.aggregator import (
    parse_aggregate_condition,
    aggregate_data,
)


def test_parse_aggregate_condition():
    assert parse_aggregate_condition("price=avg") == ("price", "avg")
    assert parse_aggregate_condition("rating=min") == ("rating", "min")


def test_aggregate_avg(sample_data):
    expected = (999 + 199 + 349 + 429) / 4
    result = aggregate_data(sample_data, "price", "avg")
    assert round(result, 2) == round(expected, 2)


def test_aggregate_min(sample_data):
    assert aggregate_data(sample_data, "rating", "min") == 4.1


def test_aggregate_max(sample_data):
    assert aggregate_data(sample_data, "rating", "max") == 4.9
