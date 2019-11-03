from unittest import TestCase

import BST


class NodeTest(TestCase):
    @property
    def nodes(self):
        value = 1000

        root = BST.Node(value)
        left = BST.Node(value - value / 2)
        right = BST.Node(value + value / 2)

        root.insert(left)
        root.insert(right)

        return root, left, right

    def test_is_root(self):
        root, left, right = self.nodes

        self.assertTrue(root.is_root)
        self.assertFalse(left.is_root)
        self.assertFalse(right.is_root)

    def test_is_leaf(self):
        root, left, right = self.nodes

        self.assertFalse(root.is_leaf)
        self.assertTrue(left.is_leaf)
        self.assertTrue(right.is_leaf)

    def test_is_leaf_with_empty_left(self):
        root, left, right = self.nodes

        root.left = None
        self.assertFalse(root.is_leaf)

    def test_is_leaf_with_empty_right(self):
        root, left, right = self.nodes

        root.right = None
        self.assertFalse(root.is_leaf)

    def test_detach_root(self):
        root, left, right = self.nodes

        root.detach()
        self.assertIsNone(root.parent)

    def test_detach(self):
        root, left, right = self.nodes

        left.detach()
        self.assertIsNone(root.left)
        self.assertEqual(root.right, right)

    def test_deepest_leaf_on_left_is_none(self):
        root, left, right = self.nodes

        self.assertIsNone(left.deepest_leaf_on_left)
        self.assertIsNone(right.deepest_leaf_on_left)

    def test_deepest_leaf_on_left_is_child(self):
        root, left, right = self.nodes

        self.assertEqual(root.deepest_leaf_on_left, left)

    def test_deepest_leaf_on_left_is_left(self):
        root, left, right = self.nodes
        left_left = BST.Node(left.value - 10)
        left_right = BST.Node(left.value + 10)

        left.insert(left_left)
        left.insert(left_right)

        self.assertEqual(root.deepest_leaf_on_left, left_left)

    def test_deepest_leaf_on_left_is_right(self):
        root, left, right = self.nodes
        left_right = BST.Node(left.value + 10)
        left_right_left = BST.Node(left_right.value - 5)
        left_right_left_right = BST.Node(left_right_left.value + 2)

        left.insert(left_right)
        left.insert(left_right_left)
        left.insert(left_right_left_right)

        self.assertEqual(root.deepest_leaf_on_left, left_right_left_right)


class BSTTest(TestCase):
    def check_node(self, node: BST.Node):
        if node.left is not None:
            self.assertLess(node.left.value, node.value)
            self.check_node(node.left)

        if node.right is not None:
            self.assertGreaterEqual(node.right.value, node.value)
            self.check_node(node.right)

    def test_insert_left(self):
        tree = BST.Tree()
        iterator = range(5, 0, -1)

        for i in iterator:
            tree.insert(i)

        current = tree.root
        for i in iterator:
            self.assertEqual(current.value, i)
            self.assertIsNone(current.right)
            current = current.left

        self.assertIsNone(current)

    def test_insert_right(self):
        tree = BST.Tree()
        iterator = range(5)

        for i in iterator:
            tree.insert(i)

        current = tree.root
        for i in iterator:
            self.assertEqual(current.value, i)
            self.assertIsNone(current.left)
            current = current.right

        self.assertIsNone(current)

    def test_insert_mixed(self):
        tree = BST.Tree()
        root = tree.insert(50)
        left = tree.insert(25)
        left_left = tree.insert(12)
        left_right = tree.insert(37)
        right = tree.insert(75)
        right_left = tree.insert(62)
        right_right = tree.insert(87)
        right_left_right = tree.insert(70)

        self.assertEqual(tree.root, root)
        self.assertEqual(tree.root.left, left)
        self.assertEqual(tree.root.left.left, left_left)
        self.assertEqual(tree.root.left.right, left_right)
        self.assertEqual(tree.root.right, right)
        self.assertEqual(tree.root.right.left, right_left)
        self.assertEqual(tree.root.right.right, right_right)
        self.assertEqual(tree.root.right.left.right, right_left_right)

    def test_find_with_empty_root(self):
        tree = BST.Tree()
        self.assertIsNone(tree.find(50))

    def test_find(self):
        tree = BST.Tree()
        nodes = [
            tree.insert(50), tree.insert(25), tree.insert(12),
            tree.insert(37), tree.insert(75), tree.insert(62),
            tree.insert(87), tree.insert(70), tree.insert(38),
        ]

        for node in nodes:
            self.assertEqual(tree.find(node.value), node)

    def test_find_nonexistent(self):
        tree = BST.Tree()
        root = tree.insert(50)
        left = tree.insert(25)
        right = tree.insert(75)

        for i in range(left.value + 1, right.value, 1):
            if i == root.value:
                continue

            self.assertIsNone(tree.find(i))

    def test_remove_with_empty_root(self):
        tree = BST.Tree()

        self.assertFalse(tree.remove(50))

    def test_remove_root(self):
        tree = BST.Tree()
        root = tree.insert(50)
        left = tree.insert(25)
        right = tree.insert(75)

        self.assertTrue(tree.remove(root.value))
        self.assertEqual(tree.root, right)
        self.assertEqual(right.left, left)
        self.assertIsNone(right.right)
        self.assertIsNone(left.left)
        self.assertIsNone(left.right)
        self.check_node(tree.root)

    def test_remove_nonexistent(self):
        tree = BST.Tree()
        root = tree.insert(50)
        left = tree.insert(25)
        right = tree.insert(75)

        for i in range(left.value + 1, right.value, 1):
            if i == root.value:
                continue

            self.assertFalse(tree.find(i))

        self.assertEqual(tree.root, root)
        self.assertEqual(tree.root.left, left)
        self.assertEqual(tree.root.right, right)

    def test_remove_left_leaf(self):
        tree = BST.Tree()
        root = tree.insert(50)
        left = tree.insert(25)
        right = tree.insert(75)

        self.assertTrue(tree.remove(left.value))
        self.assertEqual(tree.root, root)
        self.assertIsNone(tree.root.left)
        self.assertEqual(tree.root.right, right)
        self.check_node(root)

    def test_remove_right_leaf(self):
        tree = BST.Tree()
        root = tree.insert(50)
        left = tree.insert(25)
        right = tree.insert(75)

        self.assertTrue(tree.remove(right.value))
        self.assertEqual(tree.root, root)
        self.assertIsNone(tree.root.right)
        self.assertEqual(tree.root.left, left)
        self.check_node(root)

    def test_remove_node_with_empty_left(self):
        tree = BST.Tree()
        root = tree.insert(100)
        left = tree.insert(20)
        left_right = tree.insert(30)

        self.assertTrue(tree.remove(left.value))
        self.assertEqual(tree.root, root)
        self.assertEqual(tree.root.left, left_right)
        self.check_node(root)

    def test_remove_node_with_empty_right(self):
        tree = BST.Tree()
        root = tree.insert(100)
        left = tree.insert(20)
        left_left = tree.insert(30)

        self.assertTrue(tree.remove(left.value))
        self.assertEqual(tree.root, root)
        self.assertEqual(tree.root.left, left_left)
        self.check_node(root)

    def test_remove_node(self):
        tree = BST.Tree()
        root = tree.insert(50)
        right = tree.insert(75)
        right_left = tree.insert(70)
        right_right = tree.insert(90)
        right_right_left = tree.insert(80)
        right_right_right = tree.insert(100)

        self.assertTrue(tree.remove(right.value))
        self.assertEqual(root.right, right_right_left)
        self.assertEqual(root.right.left, right_left)
        self.assertEqual(root.right.right, right_right)
        self.assertEqual(root.right.right.right, right_right_right)
        self.assertIsNone(root.right.right.left)
        self.check_node(root)
