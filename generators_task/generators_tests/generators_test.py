import pytest
from generators_task.generators.generators import (
    EvenRangeIterator,
    even_range_generator as even_range,
)


def test_even_range_basic():
    assert list(EvenRangeIterator(2, 10)) == [2, 4, 6, 8, 10]


def test_even_range_start_odd():
    assert list(EvenRangeIterator(3, 10)) == [4, 6, 8, 10]


def test_even_range_end_odd():
    assert list(EvenRangeIterator(2, 9)) == [2, 4, 6, 8]


def test_even_range_single_value_even():
    assert list(EvenRangeIterator(4, 4)) == [4]


def test_even_range_single_value_odd():
    assert list(EvenRangeIterator(5, 5)) == []


def test_even_range_empty_when_start_greater_than_end():
    assert list(EvenRangeIterator(10, 2)) == []


def test_even_range_is_iterator():
    it = EvenRangeIterator(2, 6)
    assert iter(it) is it


def test_generator_basic():
    assert list(even_range(2, 10)) == [2, 4, 6, 8, 10]


def test_generator_start_odd():
    assert list(even_range(3, 10)) == [4, 6, 8, 10]


def test_generator_end_odd():
    assert list(even_range(2, 9)) == [2, 4, 6, 8]


def test_generator_single_value_even():
    assert list(even_range(4, 4)) == [4]


def test_generator_single_value_odd():
    assert list(even_range(5, 5)) == []


def test_generator_empty_when_start_greater_than_end():
    assert list(even_range(10, 2)) == []
