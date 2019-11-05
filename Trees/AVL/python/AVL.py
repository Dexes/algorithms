from __future__ import annotations

from typing import Any, Optional


class Node:
    left: Optional[Node]
    right: Optional[Node]
    value: Any
    height: int

    def __init__(self, value: Any):
        self.left = None
        self.right = None
        self.value = value
        self.height = 1

    def find_minimum(self):
        if self.left is not None:
            return self.left.find_minimum()

        return self

    def remove_minimum(self):
        if self.left is None:
            return self.right

        self.left = self.left.remove_minimum()
        self.balance()

    @property
    def balance_factor(self) -> int:
        left = self.left.height if self.left is not None else 0
        right = self.right.height if self.right is not None else 0
        return right - left

    def refresh_height(self):
        left = self.left.height if self.left is not None else 0
        right = self.right.height if self.right is not None else 0
        self.height = (left if left > right else right) + 1

    def rotate_left(self) -> Node:
        parent = self.right
        self.right = parent.left
        parent.left = self

        self.refresh_height()
        parent.refresh_height()

        return parent

    def rotate_right(self) -> Node:
        parent = self.left
        self.left = parent.right
        parent.right = self

        self.refresh_height()
        parent.refresh_height()

        return parent

    def balance(self, recursive: bool = False) -> Node:
        if recursive:
            if self.left:
                self.left.balance(True)

            if self.right:
                self.right.balance(True)

        self.refresh_height()
        balance_factor = self.balance_factor

        if balance_factor == 2:
            if self.right.balance_factor < 0:
                self.right = self.right.rotate_right()

            return self.rotate_left()

        if balance_factor == -2:
            if self.left.balance_factor > 0:
                self.left = self.left.rotate_left()

            return self.rotate_right()

        return self

    def insert(self, node: Any) -> Node:
        if node.value < self.value:
            if self.left is None:
                self.left = node
            else:
                self.left = self.left.insert(node)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right = self.right.insert(node)

        return self.balance()

    def remove(self, value: Any) -> Optional[Node]:
        if value < self.value:
            if self.left is None:
                raise self.NotFoundException()

            self.left = self.left.remove(value)
        elif value > self.value:
            if self.right is None:
                raise self.NotFoundException()

            self.right = self.right.remove(value)
        else:
            if self.left is None or self.right is None:
                return self.left if self.right is None else self.right

            minimum = self.right.find_minimum()
            minimum.right = self.right.remove_minimum()
            minimum.left = self.left

            return minimum.balance()

        return self.balance()

    def find(self, value: Any) -> Optional[Node]:
        if value < self.value:
            if self.left is None:
                return None

            return self.left.find(value)

        if value > self.value:
            if self.right is None:
                return None

            return self.right.find(value)

        return self

    class NotFoundException(Exception):
        pass


class Tree:
    root: Optional[Node]

    def __init__(self):
        self.root = None

    def insert(self, value: Any) -> Node:
        node = Node(value)

        if self.root is None:
            self.root = node
        else:
            self.root = self.root.insert(node)

        return node

    def remove(self, value: Any) -> bool:
        if self.root is None:
            return False

        try:
            self.root = self.root.remove(value)
        except Node.NotFoundException:
            return False

        return True

    def find(self, value: Any) -> Optional[Node]:
        if self.root is None:
            return None

        return self.root.find(value)
