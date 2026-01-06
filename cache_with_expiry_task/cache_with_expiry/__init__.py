"""

Mini In-Memory Cache with Expiry

Goal:
Implement a tiny in-memory key–value cache that supports storing values with a TTL (time to live). When the TTL expires, the key should no longer be returned.

✅ Requirements

Create a class:

class Cache:
    def set(self, key, value, ttl_seconds):
        ...
    def get(self, key):
        ...


Behavior:

set(key, value, ttl_seconds)
Saves the value.
Stores the expiration time = now + ttl_seconds.
get(key)
Returns the value if:
key exists AND
expiration time > current time
If expired → remove the key from cache and return None.
Internally store data however you want (dict recommended).
Use only built-in Python modules (time, etc.).

"""
