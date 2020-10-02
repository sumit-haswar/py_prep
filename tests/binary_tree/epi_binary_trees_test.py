import unittest
from binary_tree import util
from binary_tree import TreeNode
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

    def test_is_symmetric(self):
        tree = util.build_symmetric_tree()
        self.assertTrue(is_symmetric(tree))

        tree = util.build_1_to_10_bst()
        self.assertFalse(is_symmetric(tree))

        tree = util.build_epi_binary_tree()
        self.assertFalse(is_symmetric(tree))

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

    def test_get_path_with_sum(self):
        bst = util.build_1_to_10_bst()

        path = get_path_with_sum(bst, 24)
        self.assertEqual("5,9,10", path)

        path = get_path_with_sum(bst, 11)
        self.assertEqual("5,3,2,1", path)

        path = get_path_with_sum(bst, 23)
        self.assertEqual("", path)

        bt = util.build_epi_binary_tree()
        self.assertEqual("314,6,561,3,17", get_path_with_sum(bt, 901))

    def test_traversal(self):
        tree = util.build_1_to_10_bst()
        # self._inorder(tree)
        print('pre-order:')
        self._preorder(tree)
        print('post-order:')
        self._postorder(tree)

    def _inorder(self, node: TreeNode):
        if node is None:
            return
        self._inorder(node.left)
        print(node.data)
        self._inorder(node.right)

    def _preorder(self, node: TreeNode):
        if node is None:
            return
        print(node.data)
        self._preorder(node.left)
        self._preorder(node.right)

    def _postorder(self, node: TreeNode):
        if node is None:
            return
        self._postorder(node.left)
        self._postorder(node.right)
        print(node.data)



if __name__ == '__main__':
    unittest.main()
