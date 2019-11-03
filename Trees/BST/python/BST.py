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
        self.parent = parent
        self.value = value

    @property
    def is_root(self) -> bool:
        return self.parent is None

    @property
    def is_leaf(self) -> bool:
        return self.left is None and self.right is None

    def detach(self):
        if self.parent is None:
            return

        if self.parent.left == self:
            self.parent.left = None
        else:
            self.parent.right = None

    @property
    def deepest_leaf_on_left(self) -> Optional[Node]:
        if self.is_leaf:
            return None

        current = self
        while True:
            if current.left is not None:
                current = current.left
            else:
                current = current.right

            if current.is_leaf:
                return current

    def insert(self, node: Any):
        if node.value < self.value:
            if self.left is None:
                self.left = node
                node.parent = self
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                self.right = node
                node.parent = self
            else:
                self.right.insert(node)

    def remove(self) -> Optional[Node]:
        left_is_none = self.left is None
        right_is_none = self.right is None

        if left_is_none and right_is_none:
            self.detach()
            return None

        if left_is_none != right_is_none:
            child = self.left if right_is_none else self.right
            if not self.is_root:
                if self.parent.left == self:
                    self.parent.left = child
                else:
                    self.parent.right = child

            return child

        deepest_leaf = self.right.deepest_leaf_on_left or self.right
        deepest_leaf.detach()
        deepest_leaf.parent = self.parent
        deepest_leaf.left = self.left
        deepest_leaf.right = self.right if self.right is not deepest_leaf else None

        if not self.is_root:
            if self.parent.left == self:
                deepest_leaf.parent.left = deepest_leaf
            else:
                deepest_leaf.parent.right = deepest_leaf

        return deepest_leaf

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

        instead_node = node.remove()
        if node.is_root:
            self.root = instead_node

        return True

    def find(self, value: Any) -> Optional[Node]:
        if self.root is None:
            return None

        return self.root.find(value)
