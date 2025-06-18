from core.filter import (
    parse_filter_condition,
    filter_data,
)


def test_parse_filter_condition_valid():
    assert parse_filter_condition("price=100") == ("price", "=", "100")
    assert parse_filter_condition("rating<4.5") == ("rating", "<", "4.5")
    assert parse_filter_condition("name=iphone") == ("name", "=", "iphone")


def test_filter_data_numeric(sample_data):
    result = filter_data(sample_data, "price", ">", "400")
    assert len(result) == 2
    assert all(row["price"] > 400 for row in result)


def test_filter_data_string(sample_data):
    result = filter_data(sample_data, "brand", "=", "apple")
    assert len(result) == 2
    assert all(row["brand"] == "apple" for row in result)
