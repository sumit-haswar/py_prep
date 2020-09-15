import unittest
from my_strings import \
    string_to_int, \
    int_to_string, \
    convert_base, \
    is_palindromic, \
    is_palindrome, \
    replace_and_remove, \
    reverse_words


class StringsTestCase(unittest.TestCase):

    def test_is_palindromic(self):
        self.assertTrue(is_palindromic('qwertyytrewq'))
        self.assertTrue(is_palindromic('qwertytrewq'))
        self.assertFalse(is_palindromic('qwertyuxytrewq'))

    def test_int_to_string(self):
        actual = int_to_string(7867)
        self.assertEqual("7867", actual)

        actual = int_to_string(-984388)
        self.assertEqual("-984388", actual)

    def test_string_to_int(self):
        actual = string_to_int("98524")
        self.assertEqual(98524, actual)

        actual = string_to_int("-67576576")
        self.assertEqual(-67576576, actual)

        actual = string_to_int("-9")
        self.assertEqual(-9, actual)

    def test_convert_base(self):
        actual = convert_base("615", 7, 13)
        self.assertEqual("1A7", actual)

        actual = convert_base("-7541", 8, 16)
        self.assertEqual("-F61", actual)

    def test_replace_remove(self):
        input = list('abxyzdab')
        final_size = replace_and_remove(input, 8)
        self.assertListEqual(list('ddxyzddd'), input[:final_size])

        input = list('bbxayzdab')
        final_size = replace_and_remove(input, 9)
        self.assertListEqual(list('xddyzddd'), input[:final_size])

    def test_is_palindrome(self):
        actual = is_palindrome('A man, a plan, a canal, Panama.')
        self.assertTrue(actual)

        actual = is_palindrome("Murder? for a jar of red rum!")
        self.assertTrue(actual)

        actual = is_palindrome('Ray a ray')
        self.assertFalse(actual)

    def test_reverse_words(self):
        self.assertEqual("Francisco San", reverse_words(list("San Francisco")))
        self.assertEqual("Clockwork", reverse_words(list("Clockwork")))
        self.assertEqual("John loves Alice", reverse_words(list("Alice loves John")))
        self.assertEqual("be to not or be to", reverse_words(list("to be or not to be")))


if __name__ == '__main__':
    unittest.main()
