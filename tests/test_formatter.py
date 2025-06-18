from core.formatter import format_table


def test_format_table(sample_data):
    result = format_table(sample_data)
    assert isinstance(result, str)
    assert "iphone 15 pro" in result
    assert "redmi note 12" in result
    assert "+----------" in result
