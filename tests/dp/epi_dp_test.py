import unittest
from dp import *


class EpiDPTestCase(unittest.TestCase):
    def test_fibonacci_dp(self):
        self.assertEqual(144, fibonacci_dp(12))
        self.assertEqual(433494437, fibonacci_dp(43))

    def test_fibonacci_iter(self):
        self.assertEqual(5, fibonacci_iter(5))
        self.assertEqual(144, fibonacci_iter(12))
        self.assertEqual(433494437, fibonacci_iter(43))

    def test_find_maximum_subarray_brute_force(self):
        array = [904, 40, 523, 12, -335, -385, -124, 481, -13]
        maximum, max_sub_array = find_maximum_subarray_brute_force(array)
        # self.assertEqual()
        self.assertListEqual([0, 3], max_sub_array)

        array = [2, 3, -1, 1, -3, 0, 1]
        maximum, max_sub_array = find_maximum_subarray_brute_force(array)
        self.assertEqual(5, maximum)
        self.assertListEqual([0, 1], max_sub_array)

        array = [-2, 3, 1, -7, 3, 2, -1]
        maximum, max_sub_array = find_maximum_subarray_brute_force(array)
        self.assertEqual(5, maximum)
        self.assertListEqual([4, 5], max_sub_array)

    def test_find_maximum_subarray(self):
        array = [904, 40, 523, 12, -335, -385, -124, 481, -13]
        maximum = find_maximum_subarray(array)
        self.assertEqual(1479, maximum)

        array = [2, 3, -1, 1, -3, 0, 1]
        maximum = find_maximum_subarray(array)
        self.assertEqual(5, maximum)

        array = [-2, 3, 1, -7, 3, 2, -1]
        maximum = find_maximum_subarray(array)
        self.assertEqual(5, maximum)

        array = [-2, 3, -2, -1, 3, -2, 5]
        maximum = find_maximum_subarray(array)
        self.assertEqual(6, maximum)


if __name__ == '__main__':
    unittest.main()
