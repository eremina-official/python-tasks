import pytest
from stack_task.src.stack import Stack, EmptyStackError


# Fixture for a fresh stack
@pytest.fixture
def empty_stack():
    """Return a new empty stack."""
    return Stack()


# Fixture for a pre-filled stack
@pytest.fixture
def stack_with_values():
    """Return a stack with some initial values pushed."""
    s = Stack()
    s.push("a")
    s.push("b")
    s.push("c")
    return s


def test_push_and_peek(empty_stack):
    empty_stack.push(1)
    assert empty_stack.peek() == 1
    assert empty_stack.pop() == 1


def test_pop_lifo_order(stack_with_values):
    assert stack_with_values.pop() == "c"
    assert stack_with_values.pop() == "b"
    assert stack_with_values.pop() == "a"


def test_peek_does_not_remove(empty_stack):
    empty_stack.push(10)
    first_peek = empty_stack.peek()
    second_peek = empty_stack.peek()
    assert first_peek == 10
    assert second_peek == 10
    assert empty_stack.pop() == 10


def test_pop_on_empty_raises_indexerror(empty_stack):
    with pytest.raises(EmptyStackError):
        empty_stack.pop()


def test_peek_on_empty_raises_indexerror(empty_stack):
    with pytest.raises(IndexError):
        empty_stack.peek()
