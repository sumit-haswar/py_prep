from linked_list.linked_list_problems import *
from linked_list.util import create_list, \
    get_random_list, \
    get_list_from_linked_list
from random import randint

import unittest


class LinkedListProblemsTests(unittest.TestCase):

    def test_count_occurrence(self):
        list = create_list([5, 6, 11, 9, 3, 11, 11])
        self.assertEqual(count_occurrence(list, 11), 3)

    def test_get_nth(self):
        list = create_list([5, 6, 11, 9, 3, 11, 11])
        self.assertEqual(get_nth(list, 2), 11)

    def test_insert_nth(self):
        list = create_list([5, 6, 11, 9, 3, 11])
        result = insert_nth(list, idx=3, data=15)
        expected = create_list([5, 6, 11, 15, 9, 3, 11])
        self.assertTrue(self._are_equal(result, expected))

    def test_sorted_insert(self):
        list = create_list([2, 4, 12, 15, 17, 32])
        list = sorted_insert(list, Node(22))

        actual = get_list_from_linked_list(list)
        expected = [2, 4, 12, 15, 17, 22, 32]
        self.assertListEqual(expected, actual)

    def test_append(self):
        list_a = create_list([2, 4, 5, 6])
        list_b = create_list([6, 7, 8])
        list_a = append(list_a, list_b)

        actual = get_list_from_linked_list(list_a)
        expected = [2, 4, 5, 6, 6, 7, 8]
        self.assertListEqual(actual, expected)

    def test_front_back_split(self):
        list = create_list([2, 4, 12, 15, 17, 32])
        front, back = front_back_split(list)

        # assert front back
        self.assertListEqual(get_list_from_linked_list(front),
                             [2, 4, 12])
        self.assertListEqual(get_list_from_linked_list(back),
                             [15, 17, 32])

        list = create_list([2, 4, 12, 15, 17, 32, 34])
        front, back = front_back_split(list)

        # assert front back
        self.assertListEqual(get_list_from_linked_list(front),
                             [2, 4, 12, 15])
        self.assertListEqual(get_list_from_linked_list(back),
                             [17, 32, 34])

    def test_remove_duplicates(self):
        result = remove_duplicates(create_list([2, 3, 4, 4, 4, 5, 6, 7, 7]))
        self.assertListEqual(get_list_from_linked_list(result),
                             [2, 3, 4, 5, 6, 7])

    def test_move_node(self):
        source = create_list([1, 2, 3, 4])
        dest = create_list([5, 6, 7])
        source, dest = move_node(source_head=source, dest_head=dest)

        self.assertListEqual(get_list_from_linked_list(dest),
                             [1, 5, 6, 7])
        self.assertListEqual(get_list_from_linked_list(source),
                             [2, 3, 4])

    def test_alternating_split(self):

        even, odd = alternating_split(create_list([11, 22, 33, 44, 55, 66]))

        self.assertListEqual(get_list_from_linked_list(even),
                             [11, 33, 55])
        self.assertListEqual(get_list_from_linked_list(odd),
                             [22, 44, 66])

    def test_shuffle_merge(self):
        result = shuffle_merge(create_list([1, 2, 3]),
                               create_list([7, 13, 1]))

        self.assertListEqual(get_list_from_linked_list(result),
                             [1, 7, 2, 13, 3, 1])

    def test_sorted_merge(self):
        result = sorted_merge(create_list([11, 13, 17, 34, 90, 123]),
                              create_list([3, 14, 99, 111, 150]))
        self.assertListEqual(get_list_from_linked_list(result),
                             [3, 11, 13, 14, 17, 34, 90, 99, 111, 123, 150])

    def test_merge_sort(self):
        random_list = []
        for _ in range(10):
            random_list.append(randint(0, 500))

        result = merge_sort(create_list(random_list))

        random_list.sort()
        self.assertListEqual(get_list_from_linked_list(result),
                             random_list)

    def test_insert_sort(self):
        pass

    def test_sorted_intersect(self):

        result = sorted_intersect(create_list([2, 3, 5, 5, 8, 9, ]),
                                  create_list([3, 5, 19, 28, 90, ]))

        self.assertListEqual(get_list_from_linked_list(result),
                             [2, 3, 5, 8, 9, 19, 28, 90])

    def test_reverse(self):

        result = reverse(create_list([3, 4, 5, 6, 7, 8]))
        self.assertListEqual(get_list_from_linked_list(result),
                             [8, 7, 6, 5, 4, 3])

    def test_reverse_recursive(self):
        result = recursive_reverse(create_list([8, 22, 6, 12, 234, 56, 20]))
        self.assertListEqual(get_list_from_linked_list(result),
                             [20, 56, 234, 12, 6, 22, 8])

    def _are_equal(self, a, b):
        curr_a = a
        curr_b = b

        while curr_a is not None and curr_b is not None:
            if curr_a.data != curr_b.data:
                return False
            curr_a = curr_a.next
            curr_b = curr_b.next

        return curr_a is None and curr_b is None


if __name__ == '__main__':
    unittest.main()
