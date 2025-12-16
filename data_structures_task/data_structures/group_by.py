from collections import defaultdict

# Count frequencies
# ["a", "b", "a"] → {"a": 2, "b": 1}

group_by_data = ["a", "b", "a", "a", "c", "c"]

# Count items using for..in loop with dict or defauldict


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


# Group by key
# Group values by category
# [("a",1),("b",2),("a",3)] → {"a":[1,3],"b":[2]}

group_by_key_data = [("a", 1), ("b", 2), ("a", 3)]


# initial solution
def group_by_key(data: list[tuple[str, int]]) -> dict[str, list[int]]:
    result = {}
    for item in data:
        if item[0] in result:
            result[item[0]].append(item[1])
        else:
            result[item[0]] = [item[1]]
    return result


b = group_by_key(group_by_key_data)
print(b)


# solution with tuple unpacking and defaultdict
def group_by_key2(data):
    result = defaultdict(list)
    for key, value in data:
        result[key].append(value)
    return dict(result)  # convert defaultdict to dict


c = group_by_key2(group_by_key_data)
print(c)
