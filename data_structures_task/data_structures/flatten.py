from itertools import chain
from functools import reduce


# Flatten list
# Convert nested list into flat list.
# [[1,2],[3,4]] → [1,2,3,4]

lst = [[1, 2], [3, 4]]

# 1. intertools.chain - most common
# itertools is a Python standard-library module that provides fast, memory-efficient iterator building blocks (inspired by functional programming) for looping, combining, and transforming data without creating intermediate lists.
itertls_flat = list(chain.from_iterable(lst))
print(itertls_flat)


# 2. nested list comprehension (equivalent to nested loop)
compr_lst = [x for sub in lst for x in sub]
print(compr_lst)


# 3. funtools
# functools provides higher-order function utilities: tools for wrapping, composing, caching, and adapting functions.
flat = reduce(lambda a, b: a + b, [[1, 2], [3, 4]])
