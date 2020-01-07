from typing import List


def find(data: List[int]) -> int:
    result = 0
    partial_sum = 0

    for current in data:
        partial_sum += current
        result = max(result, partial_sum)

        if partial_sum < 0:
            partial_sum = 0

    return result
