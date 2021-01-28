import unittest
from dp import binomial_coefficients, fibonacci, fibonacci_memoized, fibonacci_iter


class AdmDPTestCase(unittest.TestCase):

    def test_binomial_coefficients(self):
        n_choose_k = binomial_coefficients(12, 7)
        self.assertEqual(n_choose_k, 792)
        n_choose_k = binomial_coefficients(12, 9)
        self.assertEqual(n_choose_k, 220)

    def test_fibonacci(self):
        self.assertEqual(1597, fibonacci(17))
        self.assertEqual(44945570212853, fibonacci_memoized(67))
        self.assertEqual(308061521170129, fibonacci_iter(71))


if __name__ == '__main__':
    unittest.main()
