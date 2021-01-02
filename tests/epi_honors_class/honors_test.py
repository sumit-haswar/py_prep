import unittest
from epi_honors_class import *
from linked_list.util import create_list, get_list_from_linked_list

class MyTestCase(unittest.TestCase):

    @unittest.skip
    def test_gcd(self):
        self.assertEqual(5, gcd(5,0))
        self.assertEqual(12, gcd(456, 900))

    def test_gcd_mod(self):
        self.assertEqual(5, gcd_mod(0,5))
        self.assertEqual(12, gcd_mod(456, 900))
        self.assertEqual(45, gcd_mod(945, 900))

    @unittest.skip
    def test_justify_text(self):
        actual = justify_text('the quick brown fox jumped over the lazy dog')
        expected = [

        ]
        self.assertListEqual(expected, actual)

    @unittest.skip
    def test_zipping_linked_list(self):
        ll = create_list([])
        zipped_ll = zipping_linked_list(ll)
        zipped_ll_list = get_list_from_linked_list(zipped_ll)
        expected = []
        self.assertListEqual(expected, zipped_ll_list)

if __name__ == '__main__':
    unittest.main()
