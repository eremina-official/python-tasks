class EmptyStackError(Exception):
    """Raised when stack operations are performed on an empty stack."""

    pass


class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if not self._data:
            raise EmptyStackError("Stack is empty")
        return self._data.pop()

    def peek(self):
        """
        Return the last item without removing it
        """
        return self._data[-1]

    def is_empty(self):
        if not self._data:
            return True
        else:
            return False

    def size(self):
        return len(self._data)


test = Stack()
print("stack before", test.size())

test.push("7")
print("stack", test.peek())
