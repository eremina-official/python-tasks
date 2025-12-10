"""
Daily Task: Implement a File-Based Key–Value Store
Goal:

Practice file I/O, classes, exceptions, serialization, and basic project structure — all useful for Python job interviews.

✅ Task Description

Implement a small persistent key–value store class:

store = KeyValueStore("data.json")
store.set("username", "marina")
store.get("username")  # "marina"
store.delete("username")

Requirements
Class: KeyValueStore

Takes a file path in the constructor.

On initialization:

loads existing data from JSON file if it exists

otherwise starts with an empty dict

Methods:

set(key, value)

get(key) → returns value or raises custom KeyNotFoundError

delete(key) → removes key or raises custom error

keys() → returns list of all keys

save() → writes current data to file in JSON format

Automatically saves changes after every write operation (set, delete).

Technical requirements

Use the built-in json module.

Use type hints + docstrings.

Add a custom exception class KeyNotFoundError.

Handle file read/write errors gracefully (e.g., wrap in try/except).

⭐ Bonus (if you finish early)

Add a backup() method that writes a timestamped backup file.

Add context-manager support:

with KeyValueStore("data.json") as store:
    store.set("a", 5)


Write pytest tests for:

setting/getting

missing keys

delete

persistence across two instances
"""
