"""

Implement a LRU (Least Recently Used) Cache

An LRU cache is a fixed-size cache that evicts the least recently used item when it’s full.

Requirements
Fixed capacity: The cache can only hold N items.
Eviction policy: Remove the least recently used item when inserting a new item and the cache is full.

Operations:
get(key) → return value if key exists, otherwise None
set(key, value) → insert/update key; may evict an old key if capacity is reached

Performance goal:
get and set should ideally be O(1)


Internal Structure Ideas

1️⃣ Using OrderedDict (Python 3.7+)
Maintains insertion order
Move a key to the end on access
Pop the first item if capacity exceeded

2️⃣ Using Dictionary + Doubly Linked List
Dictionary for O(1) access by key
Doubly linked list to maintain usage order
Move node to head on access, remove tail on eviction
Pros: true O(1) for get and set without relying on OrderedDict
Cons: more code, more complex

Edge Cases to Handle
Updating an existing key → should move it to most recently used
get for a missing key → return None (or raise KeyError)
Capacity = 0 → should handle gracefully
All operations should maintain cache order correctly

Why LRU Cache is Useful
Memory-limited caches (e.g., API responses, image thumbnails)
CPU/memory optimization (avoid recomputation)
Classic interview question — shows understanding of hash maps + linked lists / data structures

"""
