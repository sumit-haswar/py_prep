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
    get_primes


class ArraysTestCase(unittest.TestCase):
    def test_reverse(self):
        list = self._get_random_list(11)
        actual = copy.deepcopy(list)
        my_reverse(actual)
        list.reverse()
        self.assertListEqual(list, actual)

    def test_even_odd_partition(self):
        list = [3,5,10,7,2,4,8]
        even_odd_partition(list)
        print(list)

    def test_dutch_national_flag(self):
        list = [0,1,4,2,3,1,2,0]
        dutch_national_flag(list, 3)
        expected = [0,1,0,1,2,2,3,4]
        self.assertListEqual(list, expected)

        list = [0, 1, 4, 2, 3, 1, 2, 0, 1, 1, 4, 7]
        dutch_national_flag(list, 1)
        expected = [0, 0, 1, 1, 1, 1, 2, 7, 4, 2, 3, 4]
        self.assertListEqual(list, expected)

    def test_increment_number(self):
        self.assertListEqual([1, 3, 0] , increment_number([1,2,9]))
        self.assertListEqual([1, 0, 0, 0], increment_number([9, 9, 9]))
        self.assertListEqual([2, 0, 0, 0], increment_number([1, 9, 9, 9]))
        self.assertListEqual([1, 8, 0, 0], increment_number([1, 7, 9, 9]))

    def test_delete_duplicates_o_n(self):
        list = [2,4,6,6,6,8,8,10]
        expected = [2,4,6,8,10]
        self.assertListEqual(expected, delete_duplicates_o_n(list))

        list = [1, 1, 2, 2, 2, 4, 6, 8, 8, 10, 10, 10, 10, 10, 11, 11]
        expected = [1, 2, 4, 6, 8, 10, 11]
        self.assertListEqual(expected, delete_duplicates_o_n(list))

    def test_delete_duplicates(self):
        list = [2,4,6,6,6,8,8,10]
        expected = [2,4,6,8,10]
        end_idx = delete_duplicates(list)
        self.assertListEqual(expected, list[:end_idx])

        list = [1, 1, 2, 2, 2, 4, 6, 8, 8, 10, 10, 10, 10, 10, 11, 11]
        expected = [1, 2, 4, 6, 8, 10, 11]
        end_idx = delete_duplicates(list)
        self.assertListEqual(expected, list[:end_idx])

    # def test_multiply_two_numbers(self):
    #     self.assertListEqual([4,4,8,9,6],
    #                          multiply_two_numbers([4,8,8], [9,2]))
    #
    #     self.assertListEqual([3, 9, 0, 1, 4, 4, 3, 7, 8, 2, 8],
    #                          multiply_two_numbers([8,5,4,2,6,8,4], [4,5,6,7]))
    #
    #     self.assertListEqual([-3,8,6,0,0,2,8,4],
    #                          multiply_two_numbers([-8,4,5,2], [4,5,6,7]))

    def test_get_primes(self):
        pass
        # result = get_primes(10)
        # self.assertListEqual()

    def test_random_sampling(selfs):
        pass

    def test_max_profit_buy_sell(self):
        list = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
        actual = max_profit_buy_sell(list)

        self.assertEqual(30, actual)
        self.assertEqual(0, max_profit_buy_sell([200, 150, 75, 50, 20]))
        self.assertEqual(35, max_profit_buy_sell([200, 150, 75, 50, 20, 55, 50]))

    def _get_random_list(self, count):
        return [randint(0, 1000) for _ in range(count)]

if __name__ == '__main__':
    unittest.main()
