from core.loader import convert_value


def test_convert_value():
    assert convert_value("42") == 42
    assert convert_value("3.14") == 3.14
    assert convert_value(" hello ") == "hello"
    assert convert_value("5.0") == 5.0
    assert isinstance(convert_value("5.0"), float)
