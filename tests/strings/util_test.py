import unittest
from my_strings import find_match


class StringsTestCase(unittest.TestCase):

    def test_find_match(self):
        idx = find_match("not", "to be or not to be")
        self.assertEqual(9, idx)

    def test_find_match_not_found(self):
        idx = find_match("abc", "to be or not to be")
        self.assertEqual(-1, idx)

    def test_find_match_found(self):
        text = "to be or not to be that is the question"
        pattern = "question"
        idx = find_match(pattern, text)
        self.assertEqual(text.index(pattern), idx)


if __name__ == '__main__':
    unittest.main()
