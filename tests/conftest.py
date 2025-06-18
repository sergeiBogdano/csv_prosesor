import pytest


@pytest.fixture
def sample_data():
    return [
        {"name": "iphone 15 pro", "brand": "apple", "price": 999, "rating": 4.9},
        {"name": "redmi note 12", "brand": "xiaomi", "price": 199, "rating": 4.6},
        {"name": "galaxy a54", "brand": "samsung", "price": 349, "rating": 4.2},
        {"name": "iphone se", "brand": "apple", "price": 429, "rating": 4.1},
    ]
