from sort_algos import bubble_sort
from random import randint

import unittest


class SortAlgosTest(unittest.TestCase):

    def test_bubble_sort(self):
        random_list = self._get_random_list(count=15)
        actual = bubble_sort(random_list)

    def _get_random_list(self, count):
        return [randint(0, 1000) for _ in range(count)]
