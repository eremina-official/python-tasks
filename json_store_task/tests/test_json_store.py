import pytest
from json_store_task.json_store.json_store import JsonStore, KeyNotFoundError


def test_set_and_get(tmp_path):
    test_file = tmp_path / "test_data.json"
    store = JsonStore(test_file)
    store.set("username", "marina")
    assert store.get("username") == "marina"


def test_overwrite_value(tmp_path):
    test_file = tmp_path / "test_data.json"
    store = JsonStore(test_file)
    store.set("username", "marina")
    store.set("username", "alex")
    assert store.get("username") == "alex"


def test_get_nonexistent_key(tmp_path):
    test_file = tmp_path / "test_data.json"
    store = JsonStore(test_file)
    with pytest.raises(KeyNotFoundError):
        store.get("nonexistent")


def test_delete_key(tmp_path):
    test_file = tmp_path / "test_data.json"
    store = JsonStore(test_file)
    store.set("username", "marina")
    store.delete("username")
    with pytest.raises(KeyNotFoundError):
        store.get("username")


def test_delete_nonexistent_key(tmp_path):
    test_file = tmp_path / "test_data.json"
    store = JsonStore(test_file)
    with pytest.raises(KeyNotFoundError):
        store.delete("nonexistent")


def test_keys_method(tmp_path):
    test_file = tmp_path / "test_data.json"
    store = JsonStore(test_file)
    store.set("a", 1)
    store.set("b", 2)
    store.set("c", 3)
    keys = store.keys()
    assert set(keys) == {"a", "b", "c"}


def test_persistence(tmp_path):
    test_file = tmp_path / "test_data.json"
    # Save some data
    store = JsonStore(test_file)
    store.set("username", "marina")
    # Re-load from file
    new_store = JsonStore(test_file)
    assert new_store.get("username") == "marina"


def test_file_creation(tmp_path):
    test_file = tmp_path / "test_data.json"
    store = JsonStore(test_file)
    # File should not exist before first set
    assert not test_file.exists()
    store.set("key", "value")
    # File should exist after set
    assert test_file.exists()
