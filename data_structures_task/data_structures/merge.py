from collections import defaultdict

# Merge two dicts
# Combine dictionaries (handle overlaps).
# {"a":1},{"b":2} → {"a":1,"b":2}

dct1 = {"a": 1}
dct2 = {"b": 2}

# 1. union operator |
# Creates a new dictionary
# Original dicts (dct1, dct2) are not modified
# If keys overlap, right-hand dict overwrites the left-hand
merged_dict1 = dct1 | dct2
print(merged_dict1)

# 2. dict.update() - modifies the dictionary in place
dct3 = {"a": 1}
dct3.update(dct2)
print(dct3)

# 3. dictionary unpacking - identical to union operator |, but more readable
a = {"x": 1}
b = {"y": 2}
merged = {**a, **b}


"""--------------- merge datasets -----------------"""

# Merge datasets (join-like)
# Join records by common key, the key appears one in each set.
# users=[{"id":1,"name":"A"}]
# orders=[{"id":1,"item":"X"}]
# → [{"id":1,"name":"A","item":"X"}]

users = [{"id": 1, "name": "A"}, {"id": 2, "name": "John"}]
orders = [{"id": 1, "item": "X"}, {"id": 2, "item": "X"}]

# Methods with linear complexity O(m + n) linear, much faster than nested loops O(n*m):

# 1. Using dictionary lookup (hash join)

# build dict for lookup by key (group by key)
lookup_orders1 = {o["id"]: o for o in orders}

# merge
result = [{**u, **lookup_orders1[u["id"]]} for u in users]
print(result)


# Merge datasets (join-like)
# Join records by common key, the key appears more than once.
# output1: [
#     {"id": 1, "name": "A", "item": "X"},
#     {"id": 1, "name": "A", "item": "B"},
#     {"id": 2, "name": "John", "item": "X"}
# ]
# output2: [
#     {"id": 1, "name": "A", "orders": [{"item": "X"}, {"item": "B"}]},
#     {"id": 2, "name": "John", "orders": [{"item": "X"}]}
# ]
# output3: {
#     1: {"name": "A", "orders": [{"item": "X"}, {"item": "B"}]},
#     2: {"name": "John", "orders": [{"item": "X"}]}
# }


users1 = [{"id": 1, "name": "A"}, {"id": 2, "name": "John"}]
orders1 = [{"id": 1, "item": "X"}, {"id": 1, "item": "B"}, {"id": 2, "item": "X"}]


# build dict for lookup by key (group by key)
lookup_users = {u["id"]: u for u in users1}
# merge
result1 = [{**o, **lookup_users[o["id"]]} for o in orders1]
print("result1", result1)

# build lookup
lookup_orders2 = defaultdict(list)
for o in orders1:
    lookup_orders2[o["id"]].append(o)
# merge
result2 = [{**u, "orders": lookup_orders2[u["id"]]} for u in users]
print("result2", result2)
