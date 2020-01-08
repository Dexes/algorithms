from unittest import TestCase

import BIT


class BITTest(TestCase):
    @property
    def cases(self):
        return [
            {
                'updates': [[1, 2, 2], [1, 3, 1], [2, 3, 1], [0, 1, 1], [0, 0, 1]],
                'result': [2, 4, 4, 2],
            },
            {
                'updates': [[0, 6, 1], [1, 2, 4], [2, 4, 3], [0, 1, 1], [4, 6, 4], [1, 3, 10], [2, 3, 2], [0, 5, 3]],
                'result': [5, 19, 23, 19, 11, 8, 5],
            },
        ]

    def test_range_sum_query(self):
        for case in self.cases:
            tree = BIT.BIT(len(case['result']))
            for update in case['updates']:
                tree.update_range(update[0], update[1], update[2])

            self.assertEqual(case['result'], tree.calculate_data())
            for index, item in enumerate(case['result']):
                self.assertEqual(tree.get_element(index), item)
