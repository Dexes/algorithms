from unittest import TestCase

import majorizing_element


class MajorizingElementTest(TestCase):
    @property
    def cases(self):
        return [
            [[4, 1, 1, 2, 1, 1, 3], 1],
            [[1, 2, 2], 2],
            [[
                1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 0, 0, 0, 0, 4, 0, 0,
                0, 0, 5, 0, 0, 0, 0, 6, 0, 0, 0, 0, 7, 0, 0, 0, 0, 8, 0, 0, 0, 0, 9
            ], 0],
        ]

    def test_majorizing_element(self):
        for case in self.cases:
            data = case[0]
            expected = case[1]

            self.assertEqual(majorizing_element.find(data), expected)
