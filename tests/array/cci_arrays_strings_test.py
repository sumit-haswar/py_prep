import unittest
from arrays.cci_arrays_strings import *


class CciArraysStringsTestCase(unittest.TestCase):
    def test_is_unique_bit_map(self):
        self.assertTrue(is_unique_bit_map('abcd'))
        self.assertTrue(is_unique_bit_map('haruki'))
        self.assertFalse(is_unique_bit_map('adidas'))

    def test_is_unique(self):
        self.assertTrue(is_unique('abcd'))
        self.assertTrue(is_unique('haruki'))
        self.assertFalse(is_unique('adidas'))

    def test_is_unique_sort(self):
        self.assertTrue(is_unique_sort('abcd'))
        self.assertTrue(is_unique_sort('haruki'))
        self.assertFalse(is_unique_sort('adidas'))

    def test_is_permutation(self):
        self.assertTrue(is_permutation('qwerty', 'ytrewq'))
        self.assertTrue(is_permutation('dormitory', 'dirtyroom'))
        self.assertTrue(is_permutation('schoolmaster', 'theclassroom'))
        self.assertFalse(is_permutation('schoolmaster', 'theclassromm'))

    def test_is_permutation_sort(self):
        self.assertTrue(is_permutation_sort('qwerty', 'ytrewq'))
        self.assertTrue(is_permutation_sort('dormitory', 'dirtyroom'))
        self.assertTrue(is_permutation_sort('schoolmaster', 'theclassroom'))

    def test_get_url(self):
        self.assertEqual('mr%20john%20smith', get_url('mr john smith'))
        self.assertEqual('mr%20john%20smith%20', get_url('mr john smith '))

    def test_is_palindromic(self):
        self.assertTrue(is_palindromic('madam'))
        self.assertTrue(is_palindromic('carrace'))
        self.assertTrue(is_palindromic('nolemonnomelon'))
        self.assertFalse(is_palindromic('carracxy'))

if __name__ == '__main__':
    unittest.main()
