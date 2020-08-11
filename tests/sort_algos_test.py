from sort_algos import bubble_sort, selection_sort, heap_sort
from random import randint

import unittest


class SortAlgosTest(unittest.TestCase):

    def test_bubble_sort(self):
        pass

    def test_insertion_sort(self):
        pass

    def test_selection_sort(self):
        input, expected = self._get_input_expected_list()
        selection_sort(input)
        self.assertListEqual(input, expected)

    def test_quick_sort(self):
        pass

    def test_merge_sort(self):
        pass

    def test_heap_sort(self):
        input, expected = self._get_input_expected_list()
        input = heap_sort(input)
        self.assertListEqual(input, expected)

    def _get_input_expected_list(self):
        random_list = self._get_random_list(count=15)
        expected = random_list.copy()
        expected.sort()

        return random_list, expected

    def _get_random_list(self, count):
        return [randint(0, 1000) for _ in range(count)]
