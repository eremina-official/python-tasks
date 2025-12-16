"""Python’s main built-in collections: dict, list, set, and tuple

1. dict (Dictionary)
Description: Key-value pairs, unordered (Python 3.7+ maintains insertion order), mutable.
Use: Store and lookup data by unique keys.

2. list
Description: Ordered, mutable collection of items.
Use: Store sequences of elements that may change.

3. set
Description: Unordered collection of unique elements, mutable.
Use: Remove duplicates, perform set operations like union, intersection.

4. tuple
Description: Ordered, immutable collection of items.
Use: Store fixed sequences or use as dictionary keys.

5. collections OrderedDict
Description: The OrderedDict algorithm can handle frequent reordering operations better than dict

"""

"""Dictionaries and Objects in Python

Dictionaries are intended to be simple containers for key-value pairs, not full objects with behavior.
Dictionaries cannot have methods directly attached to them
Properteis in dict are accessed with breaket notion

Python’s separation of concerns encourages using classes for things that have both data and behavior (methods).
Objects are instances of Class, dataclass, built-in classes
Objects properties are accessed with dot notaion

"""

"""
Ways to create dict in Python:

# Literal (recommended), string keys should be in quotes (different from JS)
todo = {"id": 1, "text": "Buy milk", "done": False}

# dict() constructor (shortcut for identifiers)
todo = dict(id=1, text="Buy milk", done=False)

# dict() from pairs (dynamic)
pairs = [("id", 1), ("text", "Buy milk"), ("done", False)]
todo = dict(pairs)

"""

# list of built in functions:

print()
input()
len("test")
int()
max(1, 3, 2)  # creates temp list in memory
# any() - lazy evaluation, does not create new list in memeory, does not modify original list
# next() - lazy evaluation, does not create new list in memeory, does not modify original list
# filter() - creates temp list in memory


# List comprehension (describe a list):
# [item for item in data if condition]

# set comprehension: {x for x in ...}
# dict comprehension: {key: value for item in iterable if condition}, if there are duplicate keys previous are overwritten
# generator expression: (x for x in ...)

# conditional expression (ternary operator):
# value_if_true if condition else value_if_false
# test = item if item > 0 else item + 1
