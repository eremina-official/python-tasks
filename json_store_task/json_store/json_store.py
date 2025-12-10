from pathlib import Path
import json


class KeyNotFoundError(Exception):
    def __init__(self, key):
        super().__init__(f"Key '{key}' not found")
        self.key = key


class JsonStore:
    def __init__(self, file_name: str) -> None:
        self._json_dict_data = {}

        BASE = Path(__file__).parent
        self.file_path = BASE / file_name

        try:
            with open(self.file_path) as f:
                content = f.read()
                self._json_dict_data = json.loads(content)
        except (FileNotFoundError, json.JSONDecodeError):
            self._json_dict_data = {}

    def _open_and_write_json(self):
        with open(self.file_path, "w") as f:
            json.dump(self._json_dict_data, f)

    def set(self, key, value):
        self._json_dict_data[key] = value
        self._open_and_write_json()

    def get(self, key):
        if key not in self._json_dict_data:
            raise KeyNotFoundError(key)
        return self._json_dict_data[key]

    def delete(self, key):
        if key not in self._json_dict_data:
            raise KeyNotFoundError(key)
        self._json_dict_data.pop(key)
        self._open_and_write_json()

    def keys(self) -> list[str]:
        return list(self._json_dict_data.keys())

    def save(self):
        self._open_and_write_json()

    # def get(self, key):
    #     value = self._json_dict_data.get(key, self._get_error_msg(key))
    #     return(f"Value for {key} is", value)
    # def delete(self, key):
    #     try:
    #         self._data.pop(key)
    #     except KeyError:
    #         raise KeyNotFoundError(key)


x = JsonStore("file.txt")
x.set("testKey", "testValue")
# x.get("test")
x.keys()

y = JsonStore("file.txt")
y.get("testKey")
