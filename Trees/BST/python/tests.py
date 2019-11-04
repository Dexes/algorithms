from unittest import TestCase

import BST


class TreeTest(TestCase):
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
