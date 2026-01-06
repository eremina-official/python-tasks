import time
from dataclasses import dataclass, field

"""
TTL cache using monotonic clocks (clock that is based on the pc hardware clock mechanism that os is providing to python)

Works perfectly while the program is running, independent from the system time changes
(if user changes system time or system corrects time according to web data)
Cannot persist expiry across reboots
Ideal for in-memory caches but not for persistent caches

For persistent cache use wall-clock timestamps
expires_at = time.time() + ttl_seconds  # wall-clock timestamp

Wall-clock timestamps — when to use
If you need persistence across program restarts
If you need real-world absolute expiration (e.g., “expires at 2025-12-15 12:00 UTC”)
Downside: subject to system clock changes, may make TTL unreliable in short-term timers.
"""

# print(time.time())
# print(time.sleep(5))
# ts = time.time()
# t = time.localtime(ts)  # local timezone
# utc_t = time.gmtime(ts)  # UTC
# print("after", ts, "local", t, "utc", utc_t)
# s = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# print(s, "local", time.localtime())
# print(time.strptime("2025-01-01", "%Y-%m-%d"))
# print(time.ctime())  # 'Mon Dec 12 12:34:56 2025'


# decorator for simple data containers with minimal boilerplate, automaticaly provides __init__
@dataclass
class CacheItem:
    value: any
    ttl_seconds: float
    expires_at: float = field(
        init=False
    )  # float means that expires_at is initialised after __init__

    def __post_init__(self):
        # Initialize expires_at after __init__
        self.expires_at = time.monotonic() + self.ttl_seconds


class Cache:
    def __init__(self) -> None:
        self._cache = {}

    def set(self, key, value, ttl_seconds):
        if key and value and ttl_seconds:
            self._cache[key] = CacheItem(value, ttl_seconds)
        else:
            print("Please provide key, value and ttl_seconds")

    def get(self, key):
        item = self._cache[key]

        if not item:
            return None

        if time.monotonic() >= item.expires_at:
            self._cache.pop(key)
            return None

        return item.value


x = Cache()
x.set("testKey", "testValue", 2)
print(x.get("testKey"))
