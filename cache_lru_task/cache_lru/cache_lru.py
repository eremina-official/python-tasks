from collections import OrderedDict


# ordered dict solution
class LRUCache:
    def __init__(self, capacity) -> None:
        print("capacity", capacity)
        self._capacity = capacity
        self._cache = OrderedDict()

    def get(self, key):
        if key not in self._cache:
            return None

        # move to the end of ordered dict
        self._cache.move_to_end(key)
        return self._cache[key]

    def set(self, key, value):
        if key in self._cache:
            # move to end
            self._cache.move_to_end(key)
        print("cache", self._cache)
        # set value
        self._cache[key] = value

        # remove first item (least used one)
        if len(self._cache) > self._capacity:
            self._cache.popitem(last=False)


x = LRUCache(capacity=3)
x.set("key", "value")
print(x.get("key"))


# Dictionary + Doubly Linked List solution
class Node:
    """Doubly linked list node"""

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class Cache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node

        # Dummy head and tail nodes for easy linking
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # Remove a node from linked list
    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    # Add node right before tail (most recently used)
    def _add(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    # Move node to most recently used
    def _move_to_end(self, node):
        self._remove(node)
        self._add(node)

    def get(self, key):
        if key not in self.cache:
            return None
        node = self.cache[key]
        self._move_to_end(node)
        return node.value

    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_end(node)
        else:
            if len(self.cache) >= self.capacity:
                # Remove least recently used node
                lru = self.head.next
                self._remove(lru)
                del self.cache[lru.key]
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add(new_node)

    def __repr__(self):
        # For debugging: show keys in LRU -> MRU order
        nodes = []
        current = self.head.next
        while current != self.tail:
            nodes.append(current.key)
            current = current.next
        return "LRUCache(" + " -> ".join(map(str, nodes)) + ")"
