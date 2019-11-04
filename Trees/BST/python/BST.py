from __future__ import annotations

from typing import Any, Optional


class Node:
    left: Optional[Node]
    right: Optional[Node]
    parent: Optional[Node]
    value: Any

    def __init__(self, value: Any, parent: Optional[Node] = None):
        self.left = None
        self.right = None
        self.value = value

    def find_leaf(self, parent=None):
        if self.left is not None:
            return self.left.find_leaf(self)

        if self.right is not None:
            return self.right.find_leaf(self)

        return self, parent

    def remove_minimum(self):
        if self.left is None:
            return self.right

        self.left = self.left.remove_minimum()

    def insert(self, node: Any):
        if node.value < self.value:
            if self.left is None:
                self.left = node
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(node)

    def remove(self, value: Any) -> Optional[Node]:
        if value < self.value:
            self.left = self.left.remove(value)
        elif value > self.value:
            self.right = self.right.remove(value)
        else:
            if self.left is None or self.right is None:
                return self.left if self.right is None else self.right

            leaf, leaf_parent = self.right.find_leaf()
            leaf.right = self.right if self.right != leaf else None
            leaf.left = self.left

            if leaf_parent is not None:
                if leaf_parent.left == leaf:
                    leaf_parent.left = None
                else:
                    leaf_parent.right = None

            return leaf

        return self

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


class Tree:
    root: Optional[Node]

    def __init__(self):
        self.root = None

    def insert(self, value: Any) -> Node:
        node = Node(value)

        if self.root is None:
            self.root = node
        else:
            self.root.insert(node)

        return node

    def remove(self, value: Any) -> bool:
        node = self.find(value)
        if node is None:
            return False

        self.root = self.root.remove(value)

        return True

    def find(self, value: Any) -> Optional[Node]:
        if self.root is None:
            return None

        return self.root.find(value)
