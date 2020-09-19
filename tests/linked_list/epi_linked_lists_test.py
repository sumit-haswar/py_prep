import unittest
from linked_list.util import *
from linked_list.epi_linked_lists import \
    merge_sorted_list


class MyTestCase(unittest.TestCase):

    @unittest.skip
    def test_merge_sorted_list(self):
        list_a = create_list([12, 14, 19, 25, 50, 55])
        list_b = create_list([9, 16, 21, 28])

        actual = merge_sorted_list(list_a, list_b)

        expected = [9, 12, 14, 16, 19, 21, 25, 28, 50, 55]
        self.assertListEqual(get_list_from_linked_list(actual),
                             expected)

    def test_reverse_sublist(self):
        pass

    def test_is_cyclic(self):
        pass

if __name__ == '__main__':
    unittest.main()
