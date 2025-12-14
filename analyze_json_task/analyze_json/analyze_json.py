from pathlib import Path
import json
from collections import defaultdict


# The best way to reduce array to value in python is to use for...in loop or pandas library
# This is a 'group by' and 'reduce to one value' task
#
# Why we use defaultdict to instead of dict for resulting value:
# when we add key:value pairs, defaultdict automatically creates key if it does not exist
# if we used dict, we would have to add an additional check if the key exists:
# revenue[item[key]] = revenue.get(item[key], 0) + item["quantity"] * item["price"]


# load json file and handle errors
# load_data(filename) -> list
# total_revenue_by_product(data) -> dict
# total_revenue_by_country(data) -> dict
# best_product(data) -> str
# best_country(data) -> str
# Use type hints + docstrings.


def load_data(filename) -> list:
    BASE = Path(__file__).parent
    file_path = BASE / filename

    try:
        with open(file_path) as f:
            content = f.read()
            return json.loads(content)
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"error loading file {filename}")
        return []


def compute_revenue(data, key):
    revenue = defaultdict(float)
    for item in data:
        revenue[item[key]] += item["quantity"] * item["price"]
    return revenue


def find_top(data):
    key = max(data, key=data.get)
    return (key, data[key])


x = load_data("sales.json")
print("data", type(x))
y = compute_revenue(x, "product")
print("product", y)
c = compute_revenue(x, "country")
print("country", c)

# data = {"e": 1, "a": 10, "b": 3, "c": 6}
print("highest_product", find_top(y))
print("highest_country", find_top(c))
