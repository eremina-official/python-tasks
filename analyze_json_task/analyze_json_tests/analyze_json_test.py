import pytest
from analyze_json_task.analyze_json.analyze_json import compute_revenue, find_top

# Sample data for testing
sample_data = [
    {"product": "Coffee A", "quantity": 10, "price": 25.5, "country": "PL"},
    {"product": "Coffee B", "quantity": 5, "price": 30.0, "country": "PL"},
    {"product": "Coffee A", "quantity": 2, "price": 25.5, "country": "DE"},
]


def test_compute_revenue_product():
    expected = {
        "Coffee A": 10 * 25.5 + 2 * 25.5,  # 255.0 + 51.0 = 306.0
        "Coffee B": 5 * 30.0,  # 150.0
    }
    result = compute_revenue(sample_data, "product")
    assert result == expected


def test_compute_revenue_country():
    expected = {
        "PL": 10 * 25.5 + 5 * 30.0,  # 255.0 + 150.0 = 405.0
        "DE": 2 * 25.5,  # 51.0
    }
    result = compute_revenue(sample_data, "country")
    assert result == expected


def test_find_top_product():
    revenue = compute_revenue(sample_data, "product")
    top, top_value = find_top(revenue)
    assert top == "Coffee A"
    assert top_value == 306.0


def test_find_top_country():
    revenue = compute_revenue(sample_data, "country")
    top, top_value = find_top(revenue)
    assert top == "PL"
    assert top_value == 405.0


def test_find_top_empty_dict():
    with pytest.raises(ValueError):
        find_top({})
