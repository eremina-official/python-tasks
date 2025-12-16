from collections import defaultdict

# Count frequencies
# ["a", "b", "a"] → {"a": 2, "b": 1}

group_by_data = ["a", "b", "a", "a", "c", "c"]


def group_by(data: list) -> dict[str, int]:
    result = {}
    for item in data:
        result[item] = result.get(item, 0) + 1
    return result


x = group_by(group_by_data)
print("group_by", x)


def group_by_defaultdict(data: list) -> dict[str, int]:
    result = defaultdict(int)
    for item in data:
        result[item] += 1
    return result


y = group_by_defaultdict(group_by_data)
print("group_by_defaultdict", y)
print(y.items())
print(list(y))
