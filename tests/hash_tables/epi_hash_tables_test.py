import unittest
from binary_tree import util
from hash_tables import \
    find_anagrams, \
    ContactList, \
    merge_contact_list, \
    is_palindromic_permutation, \
    is_anonymous_letter_possible, \
    LruCache, \
    get_lca


class EpiHashTablesTestCase(unittest.TestCase):
    def test_find_anagrams(self):
        input = ['debitcard', 'elvis', 'silent',
                 'badcredit', 'lives', 'freedom',
                 'listen', 'levis', 'money']
        anagrams = find_anagrams(input)
        expected = [['debitcard', 'badcredit'],
                    ['elvis', 'lives', 'levis'],
                    ['silent', 'listen']]
        self.assertListEqual(expected, anagrams)

    def test_merge_contact_list(self):
        contact_list_1 = ContactList(['sumit haswar', 'jim smith'])
        contact_list_2 = ContactList(['sumit haswar', 'jim smith'])
        contact_list_3 = ContactList(['sumit haswar', 'sumit haswar',
                                      'ema watson'])

        contact_list = merge_contact_list([contact_list_1,
                                           contact_list_2,
                                           contact_list_3])

        self.assertEqual(2, len(contact_list))

    def test_is_palindromic_permutation(self):
        self.assertTrue(is_palindromic_permutation('edified'))
        self.assertFalse(is_palindromic_permutation('edifiedx'))
        self.assertTrue(is_palindromic_permutation('sumitsumit'))

    def test_is_anonymous_letter_possible(self):
        letter = 'data intensive app'
        magazine = 'designing data intensive applications'
        self.assertTrue(is_anonymous_letter_possible(letter, magazine))

        letter = 'to be or not to be that is the question'
        magazine = 'to be or not to be that'
        self.assertFalse(is_anonymous_letter_possible(letter, magazine))

    def test_lru_cache(self):
        cache = LruCache()

        cache.add('jim', 'San Francisco')   # --
        cache.add('ema', 'Los Angeles')     # --
        cache.add('pablo', 'San Diego')
        cache.add('john', 'New York')

        cache.add('sam', 'Chicago') # this should delete jim
        self.assertTrue('jim' not in cache.map)
        cache.add('paul', 'Detroit')    # this should delete ema
        self.assertTrue('ema' not in cache.map)
        self.assertEqual('paul', cache.head.data['key'])

        self.assertEqual('New York', cache.get('john'))
        self.assertEqual('john', cache.head.data['key'])

        cache.add('ram', 'New Delhi') # this should remove pablo
        self.assertTrue('pablo' not in cache.map)

    def test_get_lca(self):
        bt = util.build_1_to_10_bst()

        _10 = bt.right.right
        _8 = bt.right.left.right
        self.assertEqual(9, get_lca(_8, _10).data)

        _9 = bt.right
        _1 = bt.left.left.left
        self.assertEqual(5, get_lca(_9, _1).data)


if __name__ == '__main__':
    unittest.main()
