import unittest
import copy

from random import randint

from arrays import \
    my_reverse, \
    even_odd_partition, \
    dutch_national_flag, \
    increment_number, \
    delete_duplicates, \
    max_profit_buy_sell, \
    delete_duplicates_o_n, \
    multiply_two_numbers, \
    random_sampling, \
    get_primes, \
    get_next_permutation, \
    get_random_subset, \
    is_valid_sudoku


class ArraysTestCase(unittest.TestCase):
    def test_reverse(self):
        list = self._get_random_list(11)
        actual = copy.deepcopy(list)
        my_reverse(actual)
        list.reverse()
        self.assertListEqual(list, actual)

    def test_even_odd_partition(self):
        list = [3, 5, 10, 7, 2, 4, 8]
        even_odd_partition(list)
        print(list)

    def test_dutch_national_flag(self):
        list = [0, 1, 4, 2, 3, 1, 2, 0]
        dutch_national_flag(list, 3)
        expected = [0, 1, 0, 1, 2, 2, 3, 4]
        self.assertListEqual(list, expected)

        list = [0, 1, 4, 2, 3, 1, 2, 0, 1, 1, 4, 7]
        dutch_national_flag(list, 1)
        expected = [0, 0, 1, 1, 1, 1, 2, 7, 4, 2, 3, 4]
        self.assertListEqual(list, expected)

    def test_increment_number(self):
        self.assertListEqual([1, 3, 0], increment_number([1, 2, 9]))
        self.assertListEqual([1, 0, 0, 0], increment_number([9, 9, 9]))
        self.assertListEqual([2, 0, 0, 0], increment_number([1, 9, 9, 9]))
        self.assertListEqual([1, 8, 0, 0], increment_number([1, 7, 9, 9]))

    def test_delete_duplicates_o_n(self):
        list = [2, 4, 6, 6, 6, 8, 8, 10]
        expected = [2, 4, 6, 8, 10]
        self.assertListEqual(expected, delete_duplicates_o_n(list))

        list = [1, 1, 2, 2, 2, 4, 6, 8, 8, 10, 10, 10, 10, 10, 11, 11]
        expected = [1, 2, 4, 6, 8, 10, 11]
        self.assertListEqual(expected, delete_duplicates_o_n(list))

    def test_delete_duplicates(self):
        list = [2, 4, 6, 6, 6, 8, 8, 10]
        expected = [2, 4, 6, 8, 10]
        end_idx = delete_duplicates(list)
        self.assertListEqual(expected, list[:end_idx])

        list = [1, 1, 2, 2, 2, 4, 6, 8, 8, 10, 10, 10, 10, 10, 11, 11]
        expected = [1, 2, 4, 6, 8, 10, 11]
        end_idx = delete_duplicates(list)
        self.assertListEqual(expected, list[:end_idx])

    def test_multiply_two_numbers(self):
        self.assertListEqual([8, 4, 4],
                             multiply_two_numbers([4, 2, 2], [2]))

        self.assertListEqual([3, 4, 5, 6],
                             multiply_two_numbers([4, 3, 2], [8]))

        self.assertListEqual([7, 7, 7, 6],
                             multiply_two_numbers([4, 3, 2], [1, 8]))

        self.assertListEqual([1, 6, 4, 1, 6],
                             multiply_two_numbers([4, 3, 2], [3, 8]))

        self.assertListEqual([9, 9, 8, 0, 0, 1],
                             multiply_two_numbers([9, 9, 9], [9, 9, 9]))

        self.assertListEqual([-3, 8, 6, 0, 0, 2, 8, 4],
                             multiply_two_numbers([-8, 4, 5, 2], [4, 5, 6, 7]))

    def test_get_primes(self):
        result = get_primes(10)
        self.assertListEqual([2, 3, 5, 7], result)

        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                    37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
                    79, 83, 89, 97, 101, 103, 107, 109, 113,
                    127, 131, 137, 139, 149, 151, 157, 163,
                    167, 173, 179, 181, 191, 193, 197, 199]

        self.assertListEqual(expected, get_primes(200))

    def test_random_sampling(self):
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = random_sampling(list, 5)
        self.assertEqual(5, len(result))

    def test_max_profit_buy_sell(self):
        list = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
        actual = max_profit_buy_sell(list)

        self.assertEqual(30, actual)
        self.assertEqual(0, max_profit_buy_sell([200, 150, 75, 50, 20]))
        self.assertEqual(35, max_profit_buy_sell([200, 150, 75, 50, 20, 55, 50]))

    def test_is_valid_sudoku(self):
        grid = [[4, 3, 0, 0],
                [1, 2, 3, 0],
                [0, 0, 2, 0],
                [2, 1, 0, 0]]
        self.assertTrue(is_valid_sudoku(grid))

        grid = [[0, 0, 8, 3, 1, 9, 4, 0, 2],
                [0, 0, 1, 4, 5, 2, 3, 0, 0],
                [2, 3, 4, 6, 0, 0, 5, 0, 1],
                [6, 1, 9, 0, 0, 4, 0, 2, 0],
                [0, 2, 5, 0, 9, 0, 0, 0, 0],
                [4, 0, 0, 2, 0, 0, 9, 1, 5],
                [1, 4, 3, 0, 0, 7, 0, 5, 9],
                [0, 0, 6, 9, 0, 3, 1, 0, 0],
                [9, 7, 2, 1, 0, 5, 8, 0, 0]]
        self.assertTrue(is_valid_sudoku(grid))

        invalid_grid = [[0, 0, 8, 3, 1, 9, 4, 0, 2],
                        [0, 8, 1, 4, 5, 2, 3, 0, 0],
                        [2, 3, 4, 6, 0, 0, 5, 0, 1],
                        [6, 1, 9, 0, 0, 4, 0, 2, 0],
                        [0, 2, 5, 0, 9, 0, 0, 0, 0],
                        [4, 0, 0, 2, 0, 0, 9, 1, 5],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertFalse(is_valid_sudoku(invalid_grid))

    @unittest.skip
    def test_random_subset(self):
        actual = get_random_subset(100, 4)
        self.assertEqual(len(set(actual)), len(actual))

    def test_get_next_permutation(self):
        actual = get_next_permutation([8, 6, 15, 18, 17, 10, 17,
                                       13, 16, 1, 6, 1, 18, 11, 1,
                                       12, 15, 6])
        expected = [8, 6, 15, 18, 17, 10, 17, 13, 16,
                    1, 6, 1, 18, 11, 1, 15, 6, 12]
        self.assertListEqual(expected, actual)

        actual = get_next_permutation([6, 2, 1, 5, 4, 3, 0])
        expected = [6, 2, 3, 0, 1, 4, 5]
        self.assertListEqual(expected, actual)

        actual = get_next_permutation([4, 2, 4, 3])
        expected = [4, 3, 2, 4]
        self.assertListEqual(expected, actual)

    def _get_random_list(self, count):
        return [randint(0, 1000) for _ in range(count)]


if __name__ == '__main__':
    unittest.main()
