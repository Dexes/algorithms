from unittest import TestCase

import BIT


class BITTest(TestCase):
    def make_tree(self) -> BIT.BIT:
        tree = BIT.BIT(4)
        tree.update(0, 1)
        tree.update(1, 10)
        tree.update(2, 100)
        tree.update(3, 1000)

        return tree

    def test_range_sum_query(self):
        tree = self.make_tree()
        self.assertEqual(tree.get_range_sum(0, 0), 1)
        self.assertEqual(tree.get_range_sum(0, 1), 11)
        self.assertEqual(tree.get_range_sum(2, 3), 1100)
        self.assertEqual(tree.get_range_sum(3, 3), 1000)
