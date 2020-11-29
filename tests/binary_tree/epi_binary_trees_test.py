import unittest
from binary_tree import util
from binary_tree import TreeNode
from binary_tree.epi_binary_trees import \
    is_symmetric, \
    is_balanced, \
    get_lca, \
    get_parent_pointer_lca, \
    get_path_sum, \
    get_path_with_sum, \
    get_kth_node, \
    get_successor, \
    inorder_traversal, \
    reconstruct_bt, \
    compute_right_sibling_tree, \
    create_list_of_leaves, \
    compute_right_sibling_tree_recur, \
    exterior_binary_tree


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

    def test_get_path_sum(self):
        bt = util.build_bit_tree()
        sum = get_path_sum(bt)
        self.assertEqual(126, sum)

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

    def test_get_kth_node(self):
        bt = util.build_1_to_10_bst()

        for k in range(1, 11):
            node = get_kth_node(bt, k)
            self.assertEqual(k, node.data)

    def test_get_successor(self):
        root = util.build_1_to_10_bst()
        _4 = root.left.right
        succ = get_successor(_4)
        self.assertEqual(5, succ.data)

        succ = get_successor(root)
        self.assertEqual(6, succ.data)

        _8 = root.right.left.right
        succ = get_successor(_8)
        self.assertEqual(9, succ.data)

        _10 = root.right.right
        succ = get_successor(_10)
        self.assertIsNone(succ)

    def test_inorder_traversal(self):
        bst = util.build_1_to_10_bst()
        result = inorder_traversal(bst)
        self.assertListEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], result)

    def test_reconstruct_bt(self):
        inorder_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        preorder_list = [5, 3, 2, 1, 4, 9, 7, 6, 8, 10]

        bt = reconstruct_bt(inorder_list, preorder_list)

        expected = util.build_1_to_10_bst()

        self.assertTrue(util.tree_equal(expected, bt))

    def test_create_list_of_leaves(self):
        tree = util.build_1_to_10_bst()
        list = create_list_of_leaves(tree)
        self.assertListEqual([1, 4, 6, 8, 10], list)

    def test_exterior_binary_tree(self):
        tree = util.build_1_to_10_bst()
        list = exterior_binary_tree(tree)
        self.assertListEqual([5,3,2,1,4,6,8,10,9], list)

    # todo complete unit-test
    def test_compute_right_sibling_tree(self):
        perfect_bt = util.build_perfect_bt()
        compute_right_sibling_tree(perfect_bt)
        self.assertIsNotNone(perfect_bt)

    # todo complete unit-test
    def test_compute_right_sibling_tree_recur(self):
        perfect_bt = util.build_perfect_bt()
        perfect_bt = compute_right_sibling_tree_recur(perfect_bt)
        self.assertIsNotNone(perfect_bt)

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
