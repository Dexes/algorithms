from unittest import TestCase

import BST


class BSTTest(TestCase):
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
        tree.insert(50)
        tree.insert(25)
        tree.insert(12)
        tree.insert(37)
        tree.insert(75)
        tree.insert(62)
        tree.insert(87)
        tree.insert(70)

        self.assertEqual(tree.root.value, 50)
        self.assertEqual(tree.root.left.value, 25)
        self.assertEqual(tree.root.left.left.value, 12)
        self.assertEqual(tree.root.left.right.value, 37)
        self.assertEqual(tree.root.right.value, 75)
        self.assertEqual(tree.root.right.left.value, 62)
        self.assertEqual(tree.root.right.right.value, 87)
        self.assertEqual(tree.root.right.left.right.value, 70)

    def test_remove_root(self):
        tree = BST.Tree()
        tree.insert(50)
        tree.insert(25)
        tree.insert(75)

        self.assertTrue(tree.remove(50))
        self.assertIsNone(tree.root)

    def test_remove_node(self):
        tree = BST.Tree()
        tree.insert(50)
        tree.insert(25)

        self.assertEqual(tree.root.left.value, 25)
        self.assertTrue(tree.remove(25))
        self.assertIsNone(tree.root.left)

    def test_remove_nonexistent(self):
        tree = BST.Tree()
        tree.insert(50)
        tree.insert(25)

        self.assertFalse(tree.remove(75))

    def test_find(self):
        tree = BST.Tree()
        tree.insert(50)
        tree.insert(25)
        tree.insert(12)
        tree.insert(37)
        tree.insert(75)
        tree.insert(62)
        tree.insert(87)

        self.assertEqual(tree.root, tree.find(50))
        self.assertEqual(tree.root.left, tree.find(25))
        self.assertEqual(tree.root.left.left, tree.find(12))
        self.assertEqual(tree.root.left.right, tree.find(37))
        self.assertEqual(tree.root.right, tree.find(75))
        self.assertEqual(tree.root.right.left, tree.find(62))
        self.assertEqual(tree.root.right.right, tree.find(87))
