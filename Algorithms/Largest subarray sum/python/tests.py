from unittest import TestCase

import largest_subarray_sum


class LargestSubarraySumTest(TestCase):
    @property
    def cases(self):
        return [
            [[-1, 2, 3, -9], 5],
            [[-1, 2, 3, -9, 11], 11],
            [[2, -1, 2, 3, -9], 6],
            [[-2, -1, 1, 2], 3],
            [[100, -9, 2, -3, 5], 100],
            [[1, 2, 3], 6],
            [[-1, -1, -1], 0],
        ]

    def test_largest_subarray_sum(self):
        for case in self.cases:
            data = case[0]
            expected = case[1]

            self.assertEqual(largest_subarray_sum.find(data), expected)
