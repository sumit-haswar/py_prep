import unittest
from combinatorial import Subsets, Permutation


class BacktrackTestCase(unittest.TestCase):
    def test_subset(self):
        subset = Subsets()
        n = 3
        k = 0
        a = [False] * (n + 1)

        subset.backtrack(a, k, n)

        expected = ['1,2,3', '1,2', '1,3', '1', '2,3', '2', '3', '']
        self.assertListEqual(sorted(expected), sorted(subset.result))

    def test_permutation(self):
        permutation = Permutation()
        n = 3
        k = 0
        a = [0] * (n + 1)

        permutation.backtrack(a, k, n)

        expected = ['1,2,3', '1,3,2', '2,3,1', '2,1,3', '3,2,1', '3,1,2']
        self.assertListEqual(sorted(expected), sorted(permutation.result))


if __name__ == '__main__':
    unittest.main()
