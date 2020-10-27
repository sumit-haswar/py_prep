import unittest
from recursion import get_phone_mnemonic, \
    generate_permutation_iter, \
    generate_permutation


class EpiRecursionTestCase(unittest.TestCase):
    def test_get_phone_mnemonic(self):

        result = get_phone_mnemonic('19')
        self.assertListEqual(["1W", "1X", "1Y", "1Z"], result)

        result = get_phone_mnemonic('2804')
        self.assertListEqual(["AT0G", "AT0H", "AT0I", "AU0G", "AU0H", "AU0I",
                              "AV0G", "AV0H", "AV0I", "BT0G", "BT0H", "BT0I",
                              "BU0G", "BU0H", "BU0I", "BV0G", "BV0H", "BV0I",
                              "CT0G", "CT0H", "CT0I", "CU0G", "CU0H",
                              "CU0I", "CV0G", "CV0H", "CV0I"],
                             result)

    def test_generate_permutation(self):
        result = generate_permutation([0,1,2])
        self.assertListEqual([[0, 1, 2],
                              [0, 2, 1],
                              [1, 0, 2],
                              [1, 2, 0],
                              [2, 1, 0],
                              [2, 0, 1]],
                             result)

    def test_generate_permutation_iter(self):
        result = generate_permutation_iter([0,1,2])
        self.assertListEqual([[0, 1, 2],
                              [0, 2, 1],
                              [1, 0, 2],
                              [1, 2, 0],
                              [2, 0, 1],
                              [2, 1, 0]],
                             result)

if __name__ == '__main__':
    unittest.main()
