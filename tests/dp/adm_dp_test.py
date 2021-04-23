import unittest
from dp import binomial_coefficients, binomial_coefficients_recur, fibonacci, fibonacci_memoized, fibonacci_iter, \
    partition, longest_increasing_subsequence


class AdmDPTestCase(unittest.TestCase):

    def test_binomial_coefficients(self):
        n_choose_k = binomial_coefficients(12, 7)
        self.assertEqual(n_choose_k, 792)
        n_choose_k = binomial_coefficients(12, 9)
        self.assertEqual(n_choose_k, 220)

    def test_binomial_coefficients_recur(self):
        n_choose_k = binomial_coefficients_recur(5, 3)
        self.assertEqual(n_choose_k, 10)
        n_choose_k = binomial_coefficients_recur(9, 3)
        self.assertEqual(n_choose_k, 84)

    def test_fibonacci(self):
        self.assertEqual(1597, fibonacci(17))
        self.assertEqual(44945570212853, fibonacci_memoized(67))
        self.assertEqual(308061521170129, fibonacci_iter(71))

    def test_partition(self):
        books = [100, 200, 300, 400, 500, 600, 700, 800, 900]
        min_diff, partitioned_books = partition(books, 3)
        self.assertEqual(min_diff, 400)
        expected_partition = ['100,200,300,400,500', '600,700', '800,900']
        self.assertListEqual(expected_partition, partitioned_books)


if __name__ == '__main__':
    unittest.main()
