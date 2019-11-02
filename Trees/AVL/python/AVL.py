from __future__ import annotations

from typing import Any, Optional


class Node:
    parent: Optional[Node]
    left: Optional[Node]
    right: Optional[Node]
    value: Any
    height: int

    def __init__(self, value: Any):
        self.parent = None
        self.left = None
        self.right = None
        self.value = value
        self.height = 1


class Tree:
    root: Optional[Node]

    def __init__(self):
        self.root = None

    # ...

    def find(self, value: Any) -> Optional[Node]:
        if self.root is None or self.root.value == value:
            return self.root

        current = self.root
        while True:
            if value < current.value:
                if current.left is None or current.left.value == value:
                    return current.left

                current = current.left
            else:
                if current.right is None or current.right.value == value:
                    return current.right

                current = current.right
