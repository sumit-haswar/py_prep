import unittest
from binary_tree import util
from hash_tables import \
    find_anagrams, \
    ContactList, \
    merge_contact_list, \
    is_palindromic_permutation, \
    is_anonymous_letter_possible, \
    LruCache, \
    get_lca, \
    get_nearest_repeated_entries, \
    get_smallest_subarray_cover, \
    get_longest_subarray_with_distinct_values, \
    get_longest_contained_interval


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

        cache.add('jim', 'San Francisco')  # --
        cache.add('ema', 'Los Angeles')  # --
        cache.add('pablo', 'San Diego')
        cache.add('john', 'New York')

        cache.add('sam', 'Chicago')  # this should delete jim
        self.assertTrue('jim' not in cache.map)
        cache.add('paul', 'Detroit')  # this should delete ema
        self.assertTrue('ema' not in cache.map)
        self.assertEqual('paul', cache.head.data['key'])

        self.assertEqual('New York', cache.get('john'))
        self.assertEqual('john', cache.head.data['key'])

        cache.add('ram', 'New Delhi')  # this should remove pablo
        self.assertTrue('pablo' not in cache.map)

    def test_get_lca(self):
        bt = util.build_1_to_10_bst()

        _10 = bt.right.right
        _8 = bt.right.left.right
        self.assertEqual(9, get_lca(_8, _10).data)

        _9 = bt.right
        _1 = bt.left.left.left
        self.assertEqual(5, get_lca(_9, _1).data)

    def test_get_nearest_repeated_entries(self):
        result = get_nearest_repeated_entries('all work and no play makes '
                                              'for no work no fun and no results')

        self.assertDictEqual({'start': 7, 'end': 9}, result)

        result = get_nearest_repeated_entries('work work and no play makes '
                                              'for no work no fun and no results')

        self.assertDictEqual({'start': 0, 'end': 1}, result)

        result = get_nearest_repeated_entries('all work and no play')

        self.assertDictEqual({'start': -1, 'end': -1}, result)

    def test_get_smallest_subarray_cover(self):
        text = "to be save the union and to not save which is the union"
        keywords = {'save', 'union'}

        start, end = get_smallest_subarray_cover(text, keywords)
        self.assertEqual(2, start)
        self.assertEqual(4, end)

        text = "The sooner the national authority of the union can be restored " \
               "the nearer the union will be the union as it was " \
               "If there be those who would not save the union " \
               "unless they could at the same time save slavery " \
               "I do not agree with them"

        start, end = get_smallest_subarray_cover(text, keywords)
        self.assertEqual(29, start)
        self.assertEqual(31, end)

    def test_get_longest_subarray_with_distinct_values(self):
        self.assertEqual(3,
                         get_longest_subarray_with_distinct_values([1, 2, 1, 3, 1, 2, 1]))

        self.assertEqual(3,
                         get_longest_subarray_with_distinct_values([26, 73, 77, 26, 73, 77, 73, 73]))

        self.assertEqual(7,
                         get_longest_subarray_with_distinct_values([6, 59, 49, 35, 77, 17, 86]))

        self.assertEqual(12,
                         get_longest_subarray_with_distinct_values([18, 26, 72, 5, 16, 90,
                                                                    84, 5, 33, 41, 33, 66,
                                                                    46, 72, 85, 59, 97, 87,
                                                                    97, 2, 16, 84, 85, 2, 73,
                                                                    18, 23, 90, 59, 41, 64, 39]))

    def test_get_longest_contained_interval(self):
        self.assertEqual(6,
                         get_longest_contained_interval([3, -2, 7, 9, 8, 1, 2, 0, -1, 5, 8]))

        self.assertEqual(5,
                         get_longest_contained_interval([34, -4, -20, -25, 25, -34, -15,
                                                         -17, -11, -16, 23, 4, 10, 20, -6,
                                                         28, -14, -33, 11, -10, -23, 19, -27,
                                                         1, -12, 33, -18, 24, -9, -7, -26, -5,
                                                         18, 14, -31]))


if __name__ == '__main__':
    unittest.main()
