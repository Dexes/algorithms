from __future__ import annotations

from typing import List


class BIT:
    """
    Point update & range query
    """
    _size: int
    _data: List[int]

    def __init__(self, size: int):
        self._size = size
        self._data = [0] * (size + 1)

    @property
    def size(self) -> int:
        return self._size

    def update(self, index: int, delta: int):
        index += 1
        while index <= self._size:
            self._data[index] += delta
            index += index & -index

    def accumulate(self, index: int) -> int:
        index += 1
        result = 0
        while index > 0:
            result += self._data[index]
            index -= index & -index

        return result

    def get_range_sum(self, left: int, right: int) -> int:
        return self.accumulate(right) - self.accumulate(left - 1)
