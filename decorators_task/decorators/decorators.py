import time
from functools import wraps
import logging

# Decorators in Python are functions that modify other functions (or classes) without changing their code.
# They work by wrapping a function and running extra logic before and/or after it.
# JS analogue - higher order function (HOF)

# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper


@decorator
def say_hi():
    print("Hi")


# say_hi()
# monotonic clock:
# print("monotonic", time.monotonic())
# high precision monotonic clock:
# print("perf counter", time.perf_counter())
# monotonic clock to meature just CPU time used by fn, ignores I/O and wait time+
# print("process time", time.process_time())


def timeit(fn):
    """Measures how long function takes to execute"""

    @wraps(fn)
    def wrapper(*args, **kwargs):
        fn_return_value = None
        start = time.perf_counter()
        fn_return_value = fn(*args, **kwargs)
        stop = time.perf_counter()

        logger.info(
            f"function name is {fn.__name__}, "
            f"description: {fn.__doc__ if fn.__doc__ else 'No description'}, "
            f"time to execute: {stop - start:.8f}s"
        )
        return fn_return_value

    return wrapper


@timeit
def use_decorator(testKey):
    """test description"""
    print(f"use decorator, arg is {testKey}")
    return testKey


x = use_decorator(testKey="testArgs")
print("return value is", x)
