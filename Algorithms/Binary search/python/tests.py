from random import randrange
from unittest import TestCase

import BS


class BSTest(TestCase):
    def make_list(self, size):
        left = 0
        result = []

        for i in range(size):
            num = randrange(start=left, stop=left + 50)
            left = num + 1
            result.append(num)

        return result

    def test_static(self):
        data = [1, 2, 4, 8, 16, 32, 64]

        self.assertEqual(BS.binary_search(data, 1), 0)
        self.assertEqual(BS.binary_search(data, 2), 1)
        self.assertEqual(BS.binary_search(data, 4), 2)
        self.assertEqual(BS.binary_search(data, 8), 3)
        self.assertEqual(BS.binary_search(data, 16), 4)
        self.assertEqual(BS.binary_search(data, 32), 5)
        self.assertEqual(BS.binary_search(data, 64), 6)

    def test_dynamic(self):
        data = self.make_list(100000)
        for index, number in enumerate(data):
            self.assertEqual(BS.binary_search(data, number), index)
