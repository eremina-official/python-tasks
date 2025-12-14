"""

Implement a Custom Iterator & Generator

Goal
Practice:

__iter__ / __next__

generators (yield)
clean, Pythonic iteration
explaining why generators are useful (important in interviews)

✅ Task Description

Part 1 — Custom Iterator (class-based)
Implement an iterator that generates numbers from start to end (inclusive), but only even numbers.
it = EvenRange(2, 10)
list(it)
# [2, 4, 6, 8, 10]


Requirements:
Class name: EvenRange
Implement __iter__ and __next__
Raise StopIteration correctly
Add type hints and docstrings

Part 2 — Generator function
Write a generator function that yields the same sequence:
def even_range(start: int, end: int):
    ...

Part 3 — Comparison (short explanation)
Write a short comment or docstring explaining:
when you would prefer a generator over a list
memory implications

"""
