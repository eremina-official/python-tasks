"""

Group & Aggregate Data (Without Pandas)

Goal
Practice:
working with lists & dictionaries
writing pure functions
handling edge cases
thinking like an interviewer (data transformation)

✅ Task Description
You are given a list of dictionaries:

orders = [
    {"user": "alice", "product": "coffee", "price": 25, "quantity": 2},
    {"user": "bob", "product": "tea", "price": 10, "quantity": 1},
    {"user": "alice", "product": "coffee", "price": 25, "quantity": 1},
    {"user": "alice", "product": "tea", "price": 10, "quantity": 3},
]

Implement the following functions

total_spent_per_user(orders) -> dict

{
  "alice": 105,
  "bob": 10
}


total_quantity_per_product(orders) -> dict

{
  "coffee": 3,
  "tea": 4
}


top_user(orders) -> str

Returns the user who spent the most money

🔒 Constraints
Do not use pandas or collections.Counter
Use plain Python only
Functions must not mutate the input list
Add type hints and docstrings

"""
