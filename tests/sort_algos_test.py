from sort_algos import bubble_sort, \
    selection_sort, \
    heap_sort, \
    insertion_sort, \
    quick_sort, \
    merge_sort
from random import randint

import unittest


class SortAlgosTest(unittest.TestCase):

    def test_insertion_sort(self):
        input, expected = self._get_input_expected_list()
        insertion_sort(input)
        self.assertListEqual(expected, input)

    def test_selection_sort(self):
        for count in range(1, 10):
            input, expected = self._get_input_expected_list(count)
            selection_sort(input)
            self.assertListEqual(expected, input)

    def test_quick_sort(self):
        for count in range(1,25):
            input, expected = self._get_input_expected_list(count)
            quick_sort(input, 0, len(input) - 1)
            self.assertListEqual(expected, input)

    def test_merge_sort(self):
        input, expected = self._get_input_expected_list(16)
        merge_sort(input, 0, len(input) - 1)
        self.assertListEqual(expected, input)

    def test_heap_sort(self):
        input, expected = self._get_input_expected_list()
        input = heap_sort(input)
        self.assertListEqual(input, expected)

    def _get_input_expected_list(self, count=10):
        random_list = self._get_random_list(count=count)
        expected = random_list.copy()
        expected.sort()

        return random_list, expected

    def _get_random_list(self, count):
        return [randint(0, 1000) for _ in range(count)]
