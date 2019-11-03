from unittest import TestCase

import AVL


class TreeTest(TestCase):
    def check_node(self, node: AVL.Node):
        if node.left is not None:
            self.assertLess(node.left.value, node.value)
            self.check_node(node.left)

        if node.right is not None:
            self.assertGreaterEqual(node.right.value, node.value)
            self.check_node(node.right)

    def test_insert(self):
        tree = AVL.Tree()
        for i in range(7):
            tree.insert(i)

        self.assertEqual(tree.root.value, 3)
        self.assertEqual(tree.root.left.value, 1)
        self.assertEqual(tree.root.left.left.value, 0)
        self.assertEqual(tree.root.left.right.value, 2)
        self.assertEqual(tree.root.right.value, 5)
        self.assertEqual(tree.root.right.left.value, 4)
        self.assertEqual(tree.root.right.right.value, 6)
        self.check_node(tree.root)

    def test_find_with_empty_root(self):
        tree = AVL.Tree()
        self.assertIsNone(tree.find(50))

    def test_find(self):
        tree = AVL.Tree()
        nodes = [
            tree.insert(50), tree.insert(25), tree.insert(12),
            tree.insert(37), tree.insert(75), tree.insert(62),
            tree.insert(87), tree.insert(70), tree.insert(38),
        ]

        for node in nodes:
            self.assertEqual(tree.find(node.value), node)

    def test_find_nonexistent(self):
        tree = AVL.Tree()
        root = tree.insert(50)
        left = tree.insert(25)
        right = tree.insert(75)

        for i in range(left.value + 1, right.value, 1):
            if i == root.value:
                continue

            self.assertIsNone(tree.find(i))

    def test_remove_root(self):
        tree = AVL.Tree()
        root = tree.insert(50)

        self.assertTrue(tree.remove(root.value))
        self.assertIsNone(tree.root)

    def test_remove(self):
        tree = AVL.Tree()
        for i in range(8):
            tree.insert(i)

        self.assertTrue(tree.remove(5))
        self.assertEqual(tree.root.value, 3)
        self.assertEqual(tree.root.height, 3)
        self.assertEqual(tree.root.left.value, 1)
        self.assertEqual(tree.root.left.height, 2)
        self.assertEqual(tree.root.left.left.value, 0)
        self.assertEqual(tree.root.left.left.height, 1)
        self.assertEqual(tree.root.left.right.value, 2)
        self.assertEqual(tree.root.left.right.height, 1)
        self.assertEqual(tree.root.right.value, 6)
        self.assertEqual(tree.root.right.height, 2)
        self.assertEqual(tree.root.right.left.value, 4)
        self.assertEqual(tree.root.right.left.height, 1)
        self.assertEqual(tree.root.right.right.value, 7)
        self.assertEqual(tree.root.right.right.height, 1)
        self.check_node(tree.root)
