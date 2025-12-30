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

"""--------------- sum even numbers ----------------"""


# complexity O(n)
def sum_even(lst: list) -> int:
    result = 0
    for n in lst:
        if n % 2 == 0:
            result += n
    return result


def is_even(n):
    return n % 2 == 0


sum_even_data = [1, 2, 3, 4, 6, 7]

# modarate good solutions with for loop:
print("sum_even", sum_even(sum_even_data))

# best and most pythonic solution:
print(sum(x for x in sum_even_data if x % 2 == 0))

# solutions with bad redability:
print("sum_even_filter", sum(filter(is_even, sum_even_data)))
print("sum_even_filter", sum(filter(lambda x: x % 2 == 0, sum_even_data)))


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
