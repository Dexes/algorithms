from __future__ import annotations

from typing import Any, Optional


class Node:
    left: Node
    right: Node

    def __init__(self, value: Any):
        self.left = None
        self.right = None
        self.value = value


class Tree:
    root: Optional[Node]

    def __init__(self):
        self.root = None

    def insert(self, value: Any):
        node = Node(value)

        if self.root is None:
            self.root = node
            return

        current = self.root
        while True:
            if node.value < current.value:
                if current.left is None:
                    current.left = node
                    break

                current = current.left
            else:
                if current.right is None:
                    current.right = node
                    break

                current = current.right

    def remove(self, value: Any) -> bool:
        if self.root is None:
            return False

        if self.root.value == value:
            self.root = None
            return True

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    return False

                if current.left.value == value:
                    current.left = None
                    return True

                current = current.left
            else:
                if current.right is None:
                    return False

                if current.right.value == value:
                    current.right = None
                    return True

                current = current.right

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
