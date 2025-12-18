# Filter data
# Keep elements matching condition.

data = [1, 2, 3, 4, 5, 6, 8]


# 1. list comprehension, complexity O(n), pythonic, readable, eager (creates list)
def filter_even_numbers(data: list[int]) -> list[int]:
    return [item for item in data if item % 2 == 0]


print(filter_even_numbers(data))

# 2. filter(), lazy (iterator until converted), for streaming of large data


def is_even(n):
    return n % 2 == 0


result = list(filter(is_even, data))
print("result", result)
