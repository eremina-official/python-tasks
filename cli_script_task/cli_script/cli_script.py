import argparse
import json


"""
Arguments types:

| Example                 | Type                       |
| ----------------------- | -------------------------- |
| `--repeat 3`            | optional argument (flag)   |  python file.py --repeat 3, created with parser
| `word`                  | positional argument        |  python file.py 7 or python file.py 'some text', created with parser
| `add`, `remove`, `list` | **positional subcommands** |  python file.py add (like git add, git clone etc), created with subparser

"""


class TodoStore:
    def __init__(self):
        self._todo_list = []
        self._json_file_name = "todo_json.json"

        # load tasks from json
        try:
            with open(self._json_file_name) as f:
                content = f.read()
                self._todo_list = json.loads(content)
        except (FileNotFoundError, json.JSONDecodeError):
            self._todo_list = []

    # save dict to json
    def _save(self):
        with open(self._json_file_name, "w") as f:
            json.dump(self._todo_list, f)

    # helper to generate id for next todo
    def _get_id(self):
        if not self._todo_list:
            return 1
        else:
            return max(item["id"] for item in self._todo_list) + 1

    # methods attached to subcommands
    def add_task(self, args: argparse.Namespace) -> None:
        """Add a new task to the todo list."""
        print(f"Adding task: {args.text}")
        self._todo_list.append({"id": self._get_id(), "text": args.text, "done": False})
        self._save()

    def list_tasks(self, args):
        if not self._todo_list:
            print("No tasks found")
            return
        for todo in self._todo_list:
            status = "✔" if todo["done"] else "✖"
            print(f'{todo["id"]}: {todo["text"]} [{status}]')

    def delete_task(self, args):
        print("Deleting task", args)
        # Create a new list excluding the todo with the given id
        todos = [todo for todo in self._todo_list if todo["id"] != int(args.id)]
        self._todo_list = todos
        self._save()


# init store
store = TodoStore()


# declare parser
parser = argparse.ArgumentParser()

# declare subparsers
subparsers = parser.add_subparsers(
    title="subcommands",
    description="Use these subcommands to edit todo list:",
    help="additional help",
)

# --- add subcommand ---
add_parser = subparsers.add_parser("add", help="Add a new task")
add_parser.add_argument("text")
add_parser.set_defaults(func=store.add_task)

# --- list subcommand ---
list_parser = subparsers.add_parser("list", help="List tasks")
list_parser.set_defaults(func=store.list_tasks)

# --- delete subcommand ---
delete_parser = subparsers.add_parser("delete", help="Delete task by index")
delete_parser.add_argument("id")
delete_parser.set_defaults(func=store.delete_task)

args = parser.parse_args()

# Call the function assigned to the subcommand
args.func(args)


# parser.add_argument("square", type=int, help="display a square of a given number")
# parser.add_argument("-v", "--verbosity", help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbosity:
#     print(f"the square of {args.square} equals {answer}", args)
# else:
#     print(answer, args)
