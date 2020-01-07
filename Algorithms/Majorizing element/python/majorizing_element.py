from typing import List, Any


def find(data: List[Any]) -> Any:
    count = 0
    candidate = None

    for current in data:
        if count == 0:
            candidate = current
            count = 1
        elif candidate == current:
            count += 1
        else:
            count -= 1

    return candidate
