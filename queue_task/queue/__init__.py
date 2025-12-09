"""
Implement a Queue class using two stacks.
This is a common interview exercise testing understanding of stack/queue behavior.

Your class should support:

enqueue(item) — add item to the queue

dequeue() — remove and return the first inserted item

peek() — show the next item to be dequeued

is_empty()

size()

Constraints:

You must use two stacks internally (e.g., lists or your Stack class).

All methods should run in amortized O(1) time.

Raise a custom exception if dequeue/peek is performed on an empty queue.
"""

from .queue import Queue, EmptyQueueError

__all__ = ["Queue", "EmptyQueueError"]
