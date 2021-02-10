import unittest
from recursion import all_subsets, letter_case_permutation


class MyTestCase(unittest.TestCase):
    def test_all_subsets(self):
        expected = ['123', '12', '13', '1', '23', '2', '3', '']
        subsets = all_subsets('123')
        self.assertListEqual(subsets, expected)

    def test_letter_case_permutation(self):
        expected = ["a12b3","a12B3","A12b3","A12B3"]
        subsets = letter_case_permutation('a12b3')
        self.assertListEqual(subsets, expected)

if __name__ == '__main__':
    unittest.main()
