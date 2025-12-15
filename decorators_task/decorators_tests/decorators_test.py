import pytest
from io import StringIO
import sys
import time
import logging
from decorators_task.decorators.decorators import timeit


@timeit
def add(a, b):
    """Add two numbers"""
    time.sleep(0.05)
    return a + b


@timeit
def no_doc_func():
    time.sleep(0.01)
    return "done"


# -------- Tests --------
def test_return_value():
    assert add(2, 3) == 5


def test_printed_output_with_doc(caplog):
    with caplog.at_level(logging.INFO):
        add(1, 1)

    # Get captured log messages
    logs = [record.message for record in caplog.records]

    # Check that our expected strings are in the logs
    assert any("function name is add" in msg for msg in logs)
    assert any("description: Add two numbers" in msg for msg in logs)
    assert any("time to execute:" in msg for msg in logs)


def test_logged_output_no_doc(caplog):
    with caplog.at_level(logging.INFO):
        no_doc_func()

    # Get captured log messages
    logs = [record.message for record in caplog.records]

    # Check that our expected strings are in the logs
    assert any("function name is no_doc_func" in msg for msg in logs)
    assert any("description: No description" in msg for msg in logs)
    assert any("time to execute" in msg for msg in logs)
