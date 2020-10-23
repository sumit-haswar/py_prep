import unittest
from n_ary_tree import Trie

class TrieTestCase(unittest.TestCase):
    def test_trie(self):
        trie = Trie()

        trie.insert('sumit')
        trie.insert('summit')
        trie.insert('summation')

        expected = ['sumit','summit','summation']
        self.assertListEqual(expected,
                             trie.prefix_search('sum'))

        trie.insert('summary')

        expected = ['summit', 'summation', 'summary']
        self.assertListEqual(expected,
                             trie.prefix_search('summ'))

        self.assertListEqual([],
                             trie.prefix_search('xyz'))


if __name__ == '__main__':
    unittest.main()
