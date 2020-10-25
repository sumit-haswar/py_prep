import unittest
from heap import k_longest_strings, \
    merge_sorted_streams, \
    sort_inc_dec_array, \
    sort_k_sorted_array, \
    get_k_closest_stars, \
    compute_stream_median, \
    Star, \
    get_k_largest_in_heap


class EpiHeapsTestCase(unittest.TestCase):

    def test_k_longest_strings(self):
        list = [
            'green tea',
            'jenga',
            'adidas',
            'dark souls',
            'this is a long string',
            'this is a very long string',
            'xbox'
        ]
        result = k_longest_strings(4, iter(list))
        self.assertSetEqual({'green tea',
                             'dark souls',
                             'this is a long string',
                             'this is a very long string'},
                            set(result))

    def test_merge_sorted_streams(self):
        iterators = [
            iter([4, 5, 6, 7]),
            iter([1, 2, 6, 10]),
            iter([8, 99, 200]),
        ]
        list = merge_sorted_streams(iterators)
        self.assertListEqual([1, 2, 4, 5, 6, 6, 7, 8, 10, 99, 200], list)

    def test_sort_inc_dec_array(self):
        arr = [2147483647, 8, 4, 2, 1, 0, -1, -2147483648]
        result = sort_inc_dec_array(arr)
        expected = sorted([2147483647, 8, 4, 2, 1, 0, -1, -2147483648])
        self.assertListEqual(expected, result)

        arr = [1, 2, 3, 2, 1, 4, 5, 10, 9, 4, 4, 1, -1]
        result = sort_inc_dec_array(arr)
        expected = sorted([1, 2, 3, 2, 1, 4, 5, 10, 9, 4, 4, 1, -1])
        self.assertListEqual(expected, result)

    def test_sort_k_sorted_array(self):
        arr = [3, -1, 2, 6, 4, 5, 8]
        result = sort_k_sorted_array(iter(arr), 2)
        expected = sorted(arr)
        self.assertListEqual(expected, result)

        arr = [-45, -35, -29, 0, 1, 17, 30, 53]
        result = sort_k_sorted_array(iter(arr), 3)
        expected = sorted(arr)
        self.assertListEqual(expected, result)

    def test_get_k_closest_stars(self):
        stars = iter(
            [
                Star(10),
                Star(5),
                Star(9),
                Star(15),
                Star(90),
                Star(2),
                Star(1),
                Star(30),
            ]
        )

        k_closest = get_k_closest_stars(stars, 5)
        self.assertListEqual([1, 2, 5, 9, 10], k_closest)

    def test_online_median(self):
        stream = iter([-5, 7, -5, -2, -2, 0, -5, 3, -7, -9, 10])
        medians = compute_stream_median(stream)
        self.assertListEqual([-5, 1.0, -5, -3.5, -2, -2.0, -2, -2.0, -2, -3.5, -2], medians)

        stream = iter([-9, 8, 11, 10, 12, 9, -2, 9, 12, 7, 2, 4])
        medians = compute_stream_median(stream)
        self.assertListEqual([-9, -0.5, 8, 9.0, 10, 9.5, 9, 9.0, 9, 9.0, 9, 8.5], medians)

    def test_get_k_largest_in_heap(self):
        heap = [10, 2, 9, 2, 2, 8, 8, 2, 2, 2, 2, 7, 7, 7, 7]
        k_largest = get_k_largest_in_heap(heap, 3)
        self.assertListEqual([10, 9, 8], k_largest)

        k_largest = get_k_largest_in_heap(heap, 5)
        self.assertListEqual([10, 9, 8, 8, 7], k_largest)

        heap = [76, 75, 75, 71, 61, 74, 73, 63, 61, 51, 51, 59, 69, 56, 56, 58, 54, 43, 39, 48, 43, 45, 48, 59, 56,
                45, 33, 40, 51, 48, 54, 41, 37, 54, 30, 17, 40, 26, 37, 11, 3, 24, 21, 37, 0, 12, 30, 28, 42,
                10, 0, 1, 27, 22, 6, 38, 6, 37, 39, 7, 16, 0, 0, 0, 39, 7, 4, 36, 39, 30, 6, 10, 2, 9, 3, 15, 25, 19]

        k_largest = get_k_largest_in_heap(heap, 30)
        self.assertListEqual([76, 75, 75, 74, 73, 71, 69, 63, 61, 61, 59, 59, 58, 56, 56, 56, 54, 54, 54, 51,
                              51, 51, 48, 48, 48, 45, 45, 43, 43, 42],
                             k_largest)

if __name__ == '__main__':
    unittest.main()
