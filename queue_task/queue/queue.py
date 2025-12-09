"""
When to use while and for...in loops:

for...in loop:
    is used to iterate iterate over a fixed sequence
    meaning that we know exact size of sequence and do not change is when we iterate

while loop:
    use it when the number of iterations is unknown in advance
    meaning that loop runs until condition is changing or if the size of array changes when we loop

Mutating list while iterating with for...in is invalid, if list is mutated with pop(), use while loop
Iterating with for..in loop with mutatin the list with pop() leads to conflicts or IndexError,
because index is moving while list is shrinking.
"""


class EmptyQueueError(Exception):
    """Raised when stack operations are performed on an empty stack."""

    pass


msg = "Queue is empty."


class Queue:
    def __init__(self):
        self._stack_in = []
        self._stack_out = []

    def _transfer(self):
        while self._stack_in:
            self._stack_out.append(self._stack_in.pop())

    def enqueue(self, item):
        self._stack_in.append(item)

    def dequeue(self):
        if not self._stack_in and not self._stack_out:
            raise EmptyQueueError(msg)

        if not self._stack_out:
            self._transfer()

        return self._stack_out.pop()

    def peek(self):
        """
        Return the next item to be dequeued without removing it
        """
        if self._stack_out:
            return self._stack_out[-1]
        elif self._stack_in:
            return self._stack_in[0]
        else:
            raise EmptyQueueError(msg)

    def is_empty(self):
        if self._stack_in or self._stack_out:
            return False
        else:
            return True

    def size(self):
        return len(self._stack_in) + len(self._stack_out)


test = Queue()
