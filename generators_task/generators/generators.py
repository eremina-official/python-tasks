from typing import Iterator

# Generators are preferred over lists when working with large or infinite
# sequences because they produce values lazily, one at a time.

# A list stores all values in memory at once (O(n) memory),
# while a generator keeps only the current value in memory (O(1) memory),
# making generators more memory-efficient and scalable.


# EvenRange inherits from Iterator[int], it is optional but good practice
# it shows to readers and tools that this class is an iterator
class EvenRangeIterator(Iterator[int]):
    def __init__(self, start: int, stop: int) -> None:
        self._current = start if start % 2 == 0 else start + 1
        self._stop = stop

    def __iter__(self) -> "EvenRange":
        return self

    def __next__(self) -> int:
        if self._current > self._stop:
            raise StopIteration

        value = self._current
        self._current += 2
        return value


def even_range_generator(start: int, stop: int):
    current = start if start % 2 == 0 else start + 1

    while current <= stop:
        yield current
        current += 2


itr = EvenRangeIterator(3, 8)
print("interator result", list(itr))
