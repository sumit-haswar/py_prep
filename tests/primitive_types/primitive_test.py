import unittest
import uuid

from primitive_types import power, \
    clear_lowest, \
    set_lowest, \
    bit_count, \
    get_parity_use_lowest_set, \
    get_parity_caching, \
    get_parity_xor, \
    swap_bits, \
    reverse_bits, \
    reverse_digits, \
    reverse_bits_cached


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

    def test_get_parity_caching(self):
        num = uuid.uuid1().int >> 64
        expected_parity = 1 if (bin(num).count("1") % 2 == 1) else 0
        self.assertEqual(expected_parity, get_parity_caching(num))

    def test_get_parity_xor(self):
        nums = [uuid.uuid1().int >> 64, uuid.uuid1().int >> 64]
        for num in nums:
            expected_parity = 1 if (bin(num).count("1") % 2 == 1) else 0
            self.assertEqual(expected_parity, get_parity_xor(num))

    def test_swap_bits(self):
        self.assertEqual(52, swap_bits(37, 0, 4))
        self.assertEqual(53, swap_bits(53, 0, 4))
        self.assertEqual(60, swap_bits(53, 0, 3))

    def test_reverse_bits(self):
        self.assertEqual(0, reverse_bits(0))
        self.assertEqual(9223372036854775808, reverse_bits(1))
        self.assertEqual(13835058055282163712, reverse_bits(3))
        self.assertEqual(3800330000012410880, reverse_bits(4111660))
        # self.assertEqual(1675910589716422256, reverse_bits(1043492552740717288))
        # self.assertEqual(29146305768, reverse_bits(1669290181376606208))
        # self.assertEqual(51008, reverse_bits(208010007789174784))

    @unittest.skip
    def test_reverse_bits_cached(self):
        self.assertEqual(0, reverse_bits_cached(0))
        self.assertEqual(2596148429267413814265248164610048, reverse_bits_cached(1))
        self.assertEqual(3894222643901120721397872246915072, reverse_bits_cached(3))
        # todo debug following test-cases:
        # self.assertEqual(3800330000012410880, reverse_bits_cached(4111660))
        # self.assertEqual(1675910589716422256, reverse_bits_cached(1043492552740717288))
        # self.assertEqual(29146305768, reverse_bits_cached(1669290181376606208))
        # self.assertEqual(51008, reverse_bits_cached(208010007789174784))

    def test_reverse_digits(self):
        self.assertEqual(2311, reverse_digits(1132))
        self.assertEqual(8, reverse_digits(8))
        self.assertEqual(-6798, reverse_digits(-8976))

    def test_xor(self):
        result = 0
        for _ in range(0, 5):
            result = result ^ 1
            print(result)


if __name__ == '__main__':
    unittest.main()
