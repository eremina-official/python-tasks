from typing import TypeVar, Sequence, List

# import pandas as pd


T = TypeVar("T")  # must be defined first


# Deduplicate list
# [1, 2, 2, 3] → [1, 2, 3]

duplicates = [1, 2, 2, 3]
print(dict.fromkeys(duplicates))


# 1. using set - fastest
def remove_duplicates1(data: list[T]) -> list[T]:
    return list(set(data))


# 2. using dict.fromkeys() - recommented, clean, order preserved
def remove_duplicates2(data: list[T]) -> list[T]:
    return list(dict.fromkeys(data))


# 3. using for...in loop with set - when custom logic is needed
def remove_duplicates3(data: list[T]) -> list[T]:
    set_data = set()
    list_data = []
    for item in data:
        if item not in set_data:
            set_data.add(item)
            list_data.append(item)
    return list_data


x1 = remove_duplicates1(duplicates)
x2 = remove_duplicates2(duplicates)
x3 = remove_duplicates3(duplicates)
print(x1, x2, x3)


# Deduplicate list of dicts (by key)
# Remove duplicate records by ID.
# [{"id":1},{"id":1},{"id":2}] → [{"id":1},{"id":2}]

duplicates2 = [{"id": 1}, {"id": 1}, {"id": 2}]
print("dict comprehension", {item["id"]: item for item in duplicates2})


# 1. loop and set - classic, preserves order
def duplicates_dict1(data):
    set_data = set()
    list_data = []
    for item in data:
        if item["id"] not in set_data:
            set_data.add(item["id"])
            list_data.append(item)
    return list_data


# 2. dictionary comprehension
def duplicates_dict2(data):
    return list({item["id"]: item for item in data}.values())


# 3. pandas - for large datasets
# df = pd.DataFrame(data)
# df = df.drop_duplicates(subset=["id"])
# result = df.to_dict(orient="records")


a1 = duplicates_dict1(duplicates2)
a2 = duplicates_dict2(duplicates2)
print(a1, a2)
