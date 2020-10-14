import unittest
from util import generate_random_list, \
    generate_distinct_random_list
from searching.epi_searching import \
    find_first_occurrence, \
    search_entry_equal_to_its_index, \
    search_smallest, \
    get_square_root, \
    matrix_search, \
    find_min_max_stream, \
    find_kth_largest, \
    find_duplicate_missing


class EpiSearchingTestCase(unittest.TestCase):
    def test_find_first_occurrence(self):
        list = [-14, -10, 2, 108, 108, 243, 286, 299, 300]
        self.assertEqual(3, find_first_occurrence(list, 108))

        list = [2, 2, 2, 2, 108, 108, 243, 286, 299, 300]
        self.assertEqual(0, find_first_occurrence(list, 2))

        list = [108, 108, 243, 286, 299, 300, 300]
        self.assertEqual(5, find_first_occurrence(list, 300))

    def test_search_entry_equal_to_its_index(self):
        self.assertEqual(11,
                         search_entry_equal_to_its_index([-5, -3, -2, -1, 1,
                                                          2, 3, 4, 6, 8, 9, 11]))

        self.assertEqual(20,
                         search_entry_equal_to_its_index([-12, -11, -10, -7, -6,
                                                          -3, -2, 1, 3, 4, 6, 7,
                                                          8, 9, 10, 12, 13, 15,
                                                          16, 18, 20, 21, 22]))

    def test_search_smallest(self):
        self.assertEqual(3,
                         search_smallest([100, 101, 102, 2, 5]))

        self.assertEqual(2,
                         search_smallest([10, 11, -7, -5, -4, 0,
                                          1, 4, 5, 6, 7, 8]))

        self.assertEqual(26,
                         search_smallest([-23, -21, -18, -17, -13,
                                          -12, -9, -2, -1, 0, 2,
                                          7, 8, 10, 13, 14, 15,
                                          16, 17, 19, 20, 22, 23,
                                          25, 26, 27, -25, -24]))
        self.assertEqual(23,
                         search_smallest([-20, -15, -14, -10, -8,
                                          -7, -6, -5, -4, -3, 0,
                                          2, 4, 5, 7, 11, 14, 15,
                                          16, 18, 21, 23, 24, -27,
                                          -26, -25, -23]))

    def test_get_square_root(self):
        self.assertEqual(12, get_square_root(150))
        self.assertEqual(13, get_square_root(170))
        self.assertEqual(44, get_square_root(44 * 44))
        self.assertEqual(103, get_square_root(10762))
        self.assertEqual(40472, get_square_root(1638036869))
        self.assertEqual(381, get_square_root(145691))
        self.assertEqual(818, get_square_root(670634))
        self.assertEqual(602, get_square_root(363371))
        self.assertEqual(29446, get_square_root(867079849))

    def test_matrix_search(self):
        matrix = [[-1, 2, 4, 4, 6],
                  [1, 5, 5, 9, 21],
                  [3, 6, 6, 9, 22],
                  [3, 6, 8, 10, 24],
                  [6, 8, 9, 12, 25],
                  [7, 10, 12, 12, 25]]

        row, col = matrix_search(matrix, 7)
        self.assertEqual(5, row)
        self.assertEqual(0, col)

        row, col = matrix_search(matrix, 13)
        self.assertEqual(-1, row)
        self.assertEqual(-1, col)

        row, col = matrix_search(matrix, 24)
        self.assertEqual(3, row)
        self.assertEqual(4, col)

    def test_find_min_max_stream(self):
        list = generate_distinct_random_list(5)
        list_min, list_max = find_min_max_stream(list)
        self.assertEqual(min(list), list_min)
        self.assertEqual(max(list), list_max)

    def test_find_kth_largest(self):
        list = generate_distinct_random_list(10)
        sorted_list = sorted(list)
        k = 4
        self.assertEqual(sorted_list[-4], find_kth_largest(list, k))

        list = generate_distinct_random_list(20)
        sorted_list = sorted(list)
        k = 9
        self.assertEqual(sorted_list[-k], find_kth_largest(list, k))

    def test_find_duplicate_missing(self):
        list = [5, 3, 0, 3, 1, 2]
        missing, duplicate = find_duplicate_missing(list)
        self.assertEqual(4, missing)
        self.assertEqual(3, duplicate)

        list = [1, 0, 2, 3, 8, 5, 6, 7, 4, 8]
        missing, duplicate = find_duplicate_missing(list)
        self.assertEqual(9, missing)
        self.assertEqual(8, duplicate)


if __name__ == '__main__':
    unittest.main()
