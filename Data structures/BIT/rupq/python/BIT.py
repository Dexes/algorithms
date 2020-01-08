from __future__ import annotations

from typing import List


class BIT:
    """
    Range update & point query
    """
    _size: int
    _data: List[int]

    def __init__(self, size: int):
        self._size = size
        self._data = [0] * size

    @property
    def size(self) -> int:
        return self._size

    def update_range(self, left: int, right: int, delta: int):
        self._data[left] += delta

        right += 1
        if right < self._size:
            self._data[right] -= delta

    def get_element(self, index: int) -> int:
        result = 0
        for i in range(index + 1):
            result += self._data[i]

        return result

    def calculate_data(self) -> List[int]:
        result = [0] * self._size
        result[0] = self._data[0]

        for i in range(1, self._size):
            result[i] += result[i - 1] + self._data[i]

        return result
