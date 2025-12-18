import heapq


# Find missing numbers
# Detect gaps in sequence.
# [1,2,4,5] → [3]

# 1. Solution with for...in and while loops, O(n + g), n - number of items, g - number of gaps:
lst = [1, 2, 5, 6]
gaps = []

for index, number in enumerate(lst):
    if index + 1 < len(lst):
        current_item = number
        while current_item + 1 < lst[index + 1]:
            current_item = current_item + 1
            gaps.append(current_item)

print("gaps", gaps)

# 2. Cleaner version with zip() and range() for gaps, time complexity O(n + g):

lst1 = [1, 2, 5, 6]
gaps1 = []

for a, b in zip(lst1, lst1[1:]):
    for gap in range(a + 1, b):
        gaps1.append(gap)

print("gaps1", gaps1)

for a, b in zip(lst1, lst1[1:]):
    print("zip", "a", a, "b", b)
for item in range(2, 5):
    print("range", item)

"""--------------- find top values ---------------"""

# Find top-N values
# Get largest N elements.

data = [5, 1, 3, 2]


# 1. sorting, O(n) complexity, ok for small lists
def find_top(data: list[int], N: int) -> list[int]:
    return sorted(data, reverse=True)[:N]


print("top with sort", find_top(data, 2))

# 2. using heapq, optimal for large datasets
# heapq - binary min-heap implementation in Python
result = heapq.nlargest(2, data)
print("top with heapq", result)
