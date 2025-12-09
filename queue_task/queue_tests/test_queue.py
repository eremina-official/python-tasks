import pytest
from queue_task.queue.queue import Queue, EmptyQueueError


def test_enqueue_and_dequeue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3


def test_peek():
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)

    assert q.peek() == 10
    q.dequeue()
    assert q.peek() == 20


def test_is_empty_and_size():
    q = Queue()
    assert q.is_empty()
    assert q.size() == 0

    q.enqueue(5)
    q.enqueue(6)

    assert not q.is_empty()
    assert q.size() == 2


def test_dequeue_order_with_many_items():
    q = Queue()
    for i in range(1, 6):
        q.enqueue(i)

    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.dequeue() == 4
    assert q.dequeue() == 5


def test_mixed_operations():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)

    assert q.dequeue() == 1

    q.enqueue(3)
    q.enqueue(4)

    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.dequeue() == 4


def test_peek_empty_error():
    q = Queue()
    with pytest.raises(EmptyQueueError):
        q.peek()


def test_dequeue_empty_error():
    q = Queue()
    with pytest.raises(EmptyQueueError):
        q.dequeue()


def test_size_after_operations():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.dequeue()
    q.enqueue(3)

    assert q.size() == 2
