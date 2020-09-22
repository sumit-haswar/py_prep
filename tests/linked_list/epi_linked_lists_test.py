import unittest
from linked_list.util import *
from linked_list.epi_linked_lists import \
    merge_sorted_list, \
    reverse_sublist, \
    remove_duplicates, \
    remove_last_kth_node, \
    even_odd_merge, \
    is_palindromic, \
    get_cycle_head, \
    get_overlap_head


class EpiLinkedListsTestCase(unittest.TestCase):

    def test_merge_sorted_list(self):
        list_a = create_list([12, 14, 19, 25, 50, 55])
        list_b = create_list([9, 16, 21, 28])

        actual = merge_sorted_list(list_a, list_b)

        expected = [9, 12, 14, 16, 19, 21, 25, 28, 50, 55]
        self.assertListEqual(get_list_from_linked_list(actual),
                             expected)

    def test_merge_sorted_equal_len_list(self):
        list_a = create_list([12, 14, 19, 25])
        list_b = create_list([9, 16, 21, 28])

        actual = merge_sorted_list(list_a, list_b)

        expected = [9, 12, 14, 16, 19, 21, 25, 28]
        self.assertListEqual(get_list_from_linked_list(actual),
                             expected)

    def test_merge_sorted_list_empty_nonempty(self):
        list_a = create_list([12, 14, 19, 25, 50, 55])

        actual = merge_sorted_list(list_a, None)

        expected = [12, 14, 19, 25, 50, 55]
        self.assertListEqual(get_list_from_linked_list(actual),
                             expected)

    def test_reverse_sublist(self):
        link_list = create_list([11, 7, 4, 6, 5, 3, 2])
        head = reverse_sublist(link_list, 3, 5)
        self.assertListEqual([11, 7, 5, 6, 4, 3, 2],
                             get_list_from_linked_list(head))

        link_list = create_list([11, 7, 4, 6, 5, 3, 22, 9, 2])
        head = reverse_sublist(link_list, 2, 7)
        self.assertListEqual([11, 22, 3, 5, 6, 4, 7, 9, 2],
                             get_list_from_linked_list(head))

    def test_get_cycle_head(self):
        head, tail = create_list_tail([2, 3, 4, 5, 6, 7, 8, 9])

        curr = head
        while True:
            if curr.data == 5:
                break
            curr = curr.next

        tail.next = curr

        cycle_head = get_cycle_head(head)
        self.assertEqual(curr, cycle_head)

        non_cyclic = create_list([4, 5, 6, 8, 12, 3, 2, ])
        self.assertIsNone(get_cycle_head(non_cyclic))

    def test_get_overlap_head(self):
        head_a, tail_a = create_list_tail([0, 2, 4, 6])

        head_b, tail_b = create_list_tail([1, 3, 5, 7, 9, 11, 13])

        curr = head_b
        while True:
            if curr.data == 7:
                break
            curr = curr.next

        tail_a.next = curr

        node = get_overlap_head(head_a, head_b)

        self.assertEqual(curr, node)

    def test_get_no_overlap_head(self):
        head_a, tail_a = create_list_tail([0, 2, 4, 6])

        head_b, tail_b = create_list_tail([1, 3, 5, 7, 9, 11, 13])

        node = get_overlap_head(head_a, head_b)

        self.assertIsNone(node)

    def test_get_overlap_node_cyclic(self):
        pass

    def test_remove_last_kth_node(self):
        head_a = create_list([2, 4, 6, 8, 10, 12, 14])

        remove_last_kth_node(head_a, 3)

        self.assertListEqual([2, 4, 6, 8, 12, 14],
                             get_list_from_linked_list(head_a))

        remove_last_kth_node(head_a, 4)
        self.assertListEqual([2, 4, 8, 12, 14],
                             get_list_from_linked_list(head_a))

    def test_remove_duplicates(self):
        head = create_list([2, 2, 4, 6, 8, 8, 8, 10, 10, 12, 14, 14])

        remove_duplicates(head)

        self.assertListEqual([2, 4, 6, 8, 10, 12, 14],
                             get_list_from_linked_list(head))

    def test_remove_all_duplicates_(self):
        head = create_list([2, 2, 2, 2, 2, 2])

        remove_duplicates(head)

        self.assertListEqual([2],
                             get_list_from_linked_list(head))

    def test_even_odd_merge(self):
        pass

    def test_is_palindromic(self):
        self.assertTrue(
            is_palindromic(
                create_list([2, 4, 5, 5, 4, 2])))
        self.assertTrue(
            is_palindromic(
                create_list([2, 4, 5, 6, 5, 4, 2])))
        self.assertFalse(
            is_palindromic(
                create_list([2, 4, 5, 6, 5, 3, 2])))


if __name__ == '__main__':
    unittest.main()
