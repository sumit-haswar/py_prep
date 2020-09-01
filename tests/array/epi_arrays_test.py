import unittest
import copy

from random import randint

from arrays import \
    my_reverse, \
    even_odd_partition, \
    dutch_national_flag, \
    increment_number


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

    def _get_random_list(self, count):
        return [randint(0, 1000) for _ in range(count)]

if __name__ == '__main__':
    unittest.main()
