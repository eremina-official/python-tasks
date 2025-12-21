from collections import defaultdict

# Compute aggregates for iterables
# Calculate sum / avg / min / max

data = [1, 2, 3, 5]


def get_avg(data):
    return sum(data) / len(data)


print("sum", sum(data))
print("avg", get_avg(data))
print("min", min(data))
print("max", max(data))

"""--------------- complex data structres ----------------"""

# Tasks:
# Total revenue (sum of price * quantity)
# Revenue per user ({"alice": 25, "bob": 31})
# Most sold product by quantity
# Optional: list users who spent more than a threshold

orders = [
    {
        "user": "alice",
        "items": [
            {"product": "coffee", "price": 10, "quantity": 2},
            {"product": "tea", "price": 5, "quantity": 1},
        ],
    },
    {"user": "alice", "items": [{"product": "tea", "price": 5, "quantity": 2}]},
    {
        "user": "bob",
        "items": [
            {"product": "coffee", "price": 10, "quantity": 1},
            {"product": "cake", "price": 7, "quantity": 3},
        ],
    },
]


def revenue_total(orders):
    result = 0

    for order in orders:
        for item in order["items"]:
            result += item["price"] * item["quantity"]
    return result


def revenue_user(orders):
    result = defaultdict(int)

    for order in orders:
        result[order["user"]] += sum(
            [item["price"] * item["quantity"] for item in order["items"]]
        )
    return result


print("revenue_total", revenue_total(orders))
print("revenue_user", revenue_user(orders))
