# Sort by key
# Sort records by one or more fields.
# [{"a":2},{"a":1}] → [{"a":1},{"a":2}]


# sort simple and small list with built in methods list.sort() and sorted()

# 1. In place sort - modifies original list, time complexity: O(n log n)
lst1 = [3, 2, 0, 1]
sorted_lst1 = lst1.sort()
print(lst1, sorted_lst1)  # [0, 1, 2, 3]

# 2. Return a new sorted list - also O(n log n)
lst2 = [3, 2, 0, 1, 8, 6]
sorted_lst2 = sorted(lst2)
print(lst2, sorted_lst2)


lst3 = [{"a": 2}, {"a": 1}, {"a": 3}, {"a": 0}]
lst4 = [{"a": 2}, {"a": 1}, {"a": 3}, {"a": 0}]

sorted_lst3 = lst3.sort(key=lambda k: k["a"])
sorted_lst4 = sorted(lst4, key=lambda k: k["a"])
print(lst3, sorted_lst3)
print(lst4, sorted_lst4)
