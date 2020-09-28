import unittest
from binary_tree import util
from binary_tree.epi_binary_trees import \
    is_symmetric, \
    is_balanced, \
    get_lca, \
    get_parent_pointer_lca, \
    get_path_sum, \
    get_path_with_sum

@unittest.skip
class EpiBinaryTreesTestCase(unittest.TestCase):
    def test_is_balanced(self):
        self.assertEqual(False, is_balanced(util.build_random_non_bst()))
        self.assertEqual(True, is_balanced(util.build_1_to_10_bst()))

    def test_is_symmetric(self):
        self.assertEqual(True, False)

    def test_get_lca(self):
        self.assertEqual(True, False)

    def test_get_parent_pointer_lca(self):
        self.assertEqual(True, False)

    def test_get_path_sum(self):
        self.assertEqual(True, False)

    def test_get_path_with_sum(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
