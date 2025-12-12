import pytest
from cache_lru_task.cache_lru.cache_lru import LRUCache


# Pytest tests
@pytest.fixture
def cache():
    return LRUCache(capacity=3)


def test_set_and_get(cache):
    cache.set("a", 1)
    cache.set("b", 2)
    assert cache.get("a") == 1
    assert cache.get("b") == 2
    assert cache.get("c") is None


def test_eviction(cache):
    cache.set("a", 1)
    cache.set("b", 2)
    cache.set("c", 3)
    cache.set("d", 4)  # should evict 'a'
    assert cache.get("a") is None
    assert cache.get("b") == 2
    assert cache.get("c") == 3
    assert cache.get("d") == 4


def test_update_existing_key(cache):
    cache.set("a", 1)
    cache.set("b", 2)
    cache.set("a", 10)  # update 'a', move to MRU
    cache.set("c", 3)
    cache.set("d", 4)  # should evict 'b', not 'a'
