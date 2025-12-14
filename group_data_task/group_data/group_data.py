from collections import defaultdict

orders_list = [
    {"user": "alice", "product": "coffee", "price": 25, "quantity": 2},
    {"user": "bob", "product": "tea", "price": 10, "quantity": 1},
    {"user": "alice", "product": "coffee", "price": 25, "quantity": 1},
    {"user": "alice", "product": "tea", "price": 10, "quantity": 3},
]


def total_spent_per_user(orders: list[dict]) -> dict[str, float]:
    total_per_user = defaultdict(float)
    for order in orders:
        total_per_user[order["user"]] += order["price"] * order["quantity"]
    return total_per_user


def total_quantity_per_product(orders: list[dict]) -> dict[str, int]:
    total_per_product = defaultdict(int)
    for order in orders:
        total_per_product[order["product"]] += order["quantity"]
    return total_per_product


def top_user(users: dict[str, float]) -> str | None:
    if not users:
        return None
    return max(users, key=lambda k: users[k])


x = total_spent_per_user(orders_list)
print("total per user", x)

y = total_quantity_per_product(orders_list)
print("total product", y)

u = top_user(x)
print("top user", u)
