import unittest
from searching.epi_searching import \
    find_first_occurrence, \
    search_entry_equal_to_its_index, \
    search_smallest, \
    get_square_root


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


if __name__ == '__main__':
    unittest.main()
