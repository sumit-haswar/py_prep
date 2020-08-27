import unittest
from primitive_types import power, \
    clear_lowest, \
    set_lowest, \
    bit_count, \
    get_parity_use_lowest_set


class PrimitiveTestCase(unittest.TestCase):

    def test_power(self):
        self.assertEqual(pow(5, 4), power(5, 4))
        self.assertEqual(pow(9, 9), power(9, 9))

    def test_clear_lowest(self):
        self.assertEqual(8, clear_lowest(10))
        self.assertEqual(12, clear_lowest(13))
        self.assertEqual(0, clear_lowest(8))

    def test_set_lowest(self):
        self.assertEqual(15, set_lowest(11))
        self.assertEqual(7, set_lowest(6))
        self.assertEqual(7, set_lowest(5))
        self.assertEqual(11, set_lowest(10))

    def test_bit_count(self):
        nums = [14, 6, 127, 512, 899]
        for num in nums:
            self.assertEqual(bin(num).count("1"), bit_count(num))
            expected_parity = 1 if bin(num).count("1") % 2 == 1 else 0
            self.assertEqual(expected_parity, get_parity_use_lowest_set(num))

    def test_get_parity_use_lowest_set(self):
        nums = [14, 6, 127, 512, 899]
        for num in nums:
            expected_parity = 1 if (bin(num).count("1") % 2 == 1) else 0
            self.assertEqual(expected_parity, get_parity_use_lowest_set(num))

    def test_xor(self):
        result = 0
        for _ in range(0, 5):
            result = result ^ 1
            print(result)

if __name__ == '__main__':
    unittest.main()
