import unittest
from binary_tree import util
from binary_tree.epi_binary_trees import \
    is_symmetric, \
    is_balanced, \
    get_lca, \
    get_parent_pointer_lca, \
    get_path_sum, \
    get_path_with_sum


class EpiBinaryTreesTestCase(unittest.TestCase):
    def test_is_balanced(self):
        self.assertEqual(False, is_balanced(util.build_random_non_bst()))
        self.assertEqual(True, is_balanced(util.build_1_to_10_bst()))
        self.assertEqual(False, is_balanced(util.build_epi_binary_tree()))

    @unittest.skip
    def test_is_symmetric(self):
        self.assertEqual(True, False)

    @unittest.skip
    def test_get_lca(self):
        bst = util.build_1_to_10_bst()

        one = bst.left.left.left
        four = bst.left.right
        three = bst.left

        lca = get_lca(bst, one, four)
        self.assertEqual(lca, three)

    def test_get_parent_pointer_lca(self):
        bst = util.build_1_to_10_bst()

        one = bst.left.left.left
        four = bst.left.right
        three = bst.left

        lca = get_parent_pointer_lca(one, four)

        self.assertEqual(lca, three)

        lca = get_parent_pointer_lca(three, one)
        self.assertEqual(lca, three)

    @unittest.skip
    def test_get_path_sum(self):
        self.assertEqual(True, False)

    @unittest.skip
    def test_get_path_with_sum(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
