"""
Daily Task: Implement a Mini CLI Tool Using argparse
Goal:

Practice writing scripts, using command-line arguments, structuring a small project, and good practices—all common in Python jobs.

✅ Task Description

Create a CLI script called todo.py that works as a tiny command-line todo manager.

The script should support:
Commands:

add "task name" → adds a task

list → prints all tasks

remove ID → removes a task by its index

clear → removes all tasks

Example usage:

python todo.py add "Buy milk"
python todo.py list
python todo.py remove 0

Requirements:

Use the argparse module.

Store tasks in a local JSON file (todo.json).

Use a small helper class (e.g., TodoStore) for managing the file.

Handle errors (removing with invalid ID, empty list, unreadable file, etc.).

Add type hints + docstrings.
"""
