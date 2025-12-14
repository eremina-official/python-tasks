"""

Analyze JSON Data

Goal:
Practice reading JSON files, parsing data, aggregating information, and writing clean functions.

Task Description
You have a JSON file called sales.json with this structure:

[
  {"product": "Coffee A", "quantity": 10, "price": 25.5, "country": "PL"},
  {"product": "Coffee B", "quantity": 5, "price": 30.0, "country": "PL"},
  {"product": "Coffee A", "quantity": 2, "price": 25.5, "country": "DE"},
  {"product": "Coffee A", "quantity": 10, "price": 25.5, "country": "EN"},
  {"product": "Coffee B", "quantity": 5, "price": 30.0, "country": "PL"},
  {"product": "Coffee A", "quantity": 2, "price": 25.5, "country": "EN"}
]


Implement a Python script that:
Loads the JSON file.

Computes:
Total revenue (quantity * price) per product.
Total revenue per country.
Finds the product with the highest total sales.
Finds the country with the highest revenue.

Requirements
Use functions for each task:
load_data(filename) -> list
total_revenue_by_product(data) -> dict
total_revenue_by_country(data) -> dict
best_product(data) -> str
best_country(data) -> str
Use type hints + docstrings.
Handle file errors gracefully.

"""
