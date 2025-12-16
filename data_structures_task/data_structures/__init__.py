"""

Write a Reusable Timing Decorator

Goal
Practice:
decorators (@)
higher-order functions
*args / **kwargs
writing reusable, testable utilities

✅ Task Description

Implement a decorator called @timeit that measures how long a function takes to execute.

Expected behavior
@timeit
def slow_function():
    time.sleep(1)

slow_function()
# Output (example):
# slow_function took 1.0023 seconds

Requirements
The decorator must:
work with any function signature
preserve the wrapped function’s name and docstring
print execution time in seconds
Use only standard library modules:
time
functools
Return the original function’s return value.

"""
