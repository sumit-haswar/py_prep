import unittest
from binary_tree import util
from binary_search_trees import *
from binary_tree.epi_binary_trees import is_balanced


class EpiBinarySearchTreesTestCase(unittest.TestCase):

    def test_is_bst(self):
        bst = util.build_1_to_10_bst()
        self.assertTrue(is_bst(bst))

        non_bst = util.build_random_non_bst()
        self.assertFalse(is_bst(non_bst))

    def test_is_bst_bfs(self):
        bst = util.build_1_to_10_bst()
        self.assertTrue(is_bst_bfs(bst))

        non_bst = util.build_random_non_bst()
        self.assertFalse(is_bst_bfs(non_bst))

    def test_find_greater_than_k(self):
        bst = util.build_1_to_10_bst()
        self.assertEqual(5, find_greater_than_k(bst, 4).data)
        self.assertEqual(9, find_greater_than_k(bst, 8).data)
        self.assertEqual(6, find_greater_than_k(bst, 5).data)

    def test_find_kth_largest(self):
        bst = util.build_1_to_10_bst()
        self.assertListEqual([10, 9, 8], find_k_largest(bst, 3))
        self.assertListEqual([10, 9, 8, 7], find_k_largest(bst, 4))

    def test_get_lca(self):
        bst = util.build_1_to_10_bst()
        self.assertEqual(5, get_lca(bst, 4, 7).data)
        self.assertEqual(9, get_lca(bst, 10, 7).data)
        self.assertEqual(3, get_lca(bst, 4, 1).data)

        epi_bst = util.build_epi_bst()
        self.assertEqual(43, get_lca(epi_bst, 53, 29).data)

    def test_get_lca_iter(self):
        bst = util.build_1_to_10_bst()
        self.assertEqual(5, get_lca_iter(bst, 4, 7).data)
        self.assertEqual(9, get_lca_iter(bst, 10, 7).data)
        self.assertEqual(3, get_lca_iter(bst, 4, 1).data)

        epi_bst = util.build_epi_bst()
        self.assertEqual(43, get_lca_iter(epi_bst, 53, 29).data)

    def test_build_bst(self):
        bst = build_bst_from_preorder([43, 23, 37, 29, 31, 41, 47, 53])
        expected = util.build_epi_bst().right
        self.assertTrue(util.tree_equal(bst, expected))

    def test_build_bst_from_preorder_optimal(self):
        bst = build_bst_from_preorder_optimal([43, 23, 37, 29, 31, 41, 47, 53])
        expected = util.build_epi_bst().right
        self.assertTrue(util.tree_equal(bst, expected))

    def test_find_closest_elements_in_sorted_array(self):
        input = [[5, 10, 15],
                 [3, 6, 9, 12, 15],
                 [8, 16, 24]]
        actual = find_closest_elements_in_sorted_array(input)
        self.assertEqual(1, actual)

        input = [[5, 10, 15, 24],
                 [3, 6, 9, 12, 15, 24],
                 [8, 16, 24]]
        actual = find_closest_elements_in_sorted_array(input)
        self.assertEqual(0, actual)

    def test_create_bst(self):
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        bst = create_bst(list)
        self.assertTrue(is_balanced(bst))

    def test_pair_includes_ancestor_and_descendant_of_m(self):
        bst = util.build_epi_bst()

        _43 = bst.right
        _41 = bst.right.left.right.right
        _37 = bst.right.left.right

        self.assertTrue(pair_includes_ancestor_and_descendant_of_m(_41, _43, _37))

        _13 = bst.left.right.right.left
        _11 = bst.left.right
        self.assertTrue(pair_includes_ancestor_and_descendant_of_m(bst, _13, _11))

        _5 = bst.left.left.right
        _11 = bst.left.right
        self.assertFalse(pair_includes_ancestor_and_descendant_of_m(bst, _5, _11))

    def test_get_range_in_bst(self):
        bst = util.build_epi_bst()
        result = get_range_in_bst(bst, 16, 41)
        self.assertListEqual([17, 19, 23, 29, 31, 37, 41], result)

        result = get_range_in_bst(bst, 53, 90)
        self.assertListEqual([53], result)

        result = get_range_in_bst(bst, 0, 1)
        self.assertListEqual([], result)

        self.assertListEqual([7, 11, 13], get_range_in_bst(bst, 7, 15))

    def test_clients_credits_info(self):
        cci = ClientsCreditsInfo()
        data = [
            {'client_id': 'john-pablo', 'credit': 100},
            {'client_id': 'jim-smith', 'credit': 80},
            {'client_id': 'ema-scott', 'credit': 95},
        ]

        for client in data:
            cci.insert(client['client_id'], client['credit'])

        max = cci.get_max()
        self.assertTrue('john-pablo' in max)

        cci.insert('jim-ross', 200)
        self.assertTrue('jim-ross' in cci.get_max())
        cci.remove('jim-ross')
        self.assertTrue('john-pablo' in cci.get_max())

        self.assertDictEqual({'credit': 80, 'client_id': 'jim-smith'}, cci.lookup('jim-smith'))


if __name__ == '__main__':
    unittest.main()
