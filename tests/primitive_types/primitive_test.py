import unittest
from primitive_types import power


class PrimitiveTestCase(unittest.TestCase):

    def test_power(self):
        self.assertEqual(pow(5, 4), power(5, 4))
        self.assertEqual(pow(9, 9), power(9, 9))


if __name__ == '__main__':
    unittest.main()
