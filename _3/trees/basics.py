from typing import Optional, List

from _3.trees.tree_node import TreeNode
from _3.trees.util import build_1_to_10_bst, build_random_non_bst, build_right_bst, build_left_bst


# lookup: find if a node exists in a binary-tree(non-bst)
def lookup(node: TreeNode, val: int) -> Optional[TreeNode]:
    if node is None:
        return None

    if node.val == val:
        return node

    left = lookup(node.left, val)
    if left:
        return left

    right = lookup(node.right, val)

    return right


# lookup: find if a node exists in a bst
def lookup_bst(node: TreeNode, val: int) -> Optional[TreeNode]:
    if node is None:
        return None

    if node.val == val:
        return node
    elif node.val < val:
        return lookup_bst(node.right, val)
    else:
        return lookup_bst(node.left, val)


# insert
def insert(node: TreeNode, val: int) -> TreeNode:
    pass


# size
def size(node: TreeNode) -> int:
    if node is None:
        return 0

    if node.is_leaf():
        return 1

    return size(node.left) + size(node.right) + 1


# max-depth aka height
def get_max_depth(node: TreeNode) -> int:
    if node is None:
        return -1

    return max(get_max_depth(node.left) + 1, get_max_depth(node.right) + 1)


# min-val of a generic: non-bst
def get_min_val(node: TreeNode) -> int:
    def get_min_val_internal(node: TreeNode, curr_min: List[TreeNode]):
        if node is None:
            return

        if curr_min[0].val is None or node.val < curr_min[0].val:
            curr_min[0] = node

        get_min_val_internal(node.left, curr_min)
        get_min_val_internal(node.right, curr_min)

        return curr_min

    curr_min = get_min_val_internal(node, [TreeNode(None)])
    return curr_min[0].val


# min-val of a bst
def get_min_val_bst(node: TreeNode) -> TreeNode:
    if node is None:
        return node

    if node.left:
        return get_min_val_bst(node.left)

    return node


def get_min_val_bst_iter(node: TreeNode) -> TreeNode:
    if node is None or node.left is None:
        return node

    curr = node
    while curr.left is not None:
        curr = curr.left

    return curr


def get_max_val_bst_iter(node: TreeNode):
    if node is None or node.right is None:
        return node

    curr = node
    while curr.right is not None:
        curr = curr.right

    return curr


# print-tree(inorder traversal)
def inorder_traversal(root: TreeNode) -> List[int]:
    def _inorder_traversal(node: TreeNode, tl: List[int]):
        if node is None:
            return

        _inorder_traversal(node.left, tl)
        tl.append(node.val)
        _inorder_traversal(node.right, tl)

    traversal_list: List[int] = []
    _inorder_traversal(root, traversal_list)
    return traversal_list


# print post-order
def postorder_traversal(node: TreeNode) -> List[int]:
    def _postorder_traversal(node: TreeNode, tl: List[int]):
        if node is None:
            return

        _postorder_traversal(node.left, tl)
        _postorder_traversal(node.right, tl)
        tl.append(node.val)

    tl: List[int] = []
    _postorder_traversal(node, tl)
    return tl


# has path sum
def has_path_sum(node: TreeNode, val: int) -> bool:
    def _has_path_sum(node: TreeNode, acc_val: int, val: int) -> bool:
        if node.is_leaf() and (acc_val + node.val == val):
            return True

        if node.left:
            has_sum = _has_path_sum(node.left, acc_val + node.val, val)
            if has_sum:
                return True

        if node.right:
            has_sum = _has_path_sum(node.right, acc_val + node.val, val)
            if has_sum:
                return True

        return False

    return _has_path_sum(node, 0, val)


# print all paths
def print_all_paths(node: TreeNode):
    def _print_all_paths(node: TreeNode, path_prefix: str):
        if node.is_leaf():
            print(path_prefix + "," + str(node.val))

        if node.left:
            _print_all_paths(node.left, path_prefix + "," + str(node.val))

        if node.right:
            _print_all_paths(node.right, path_prefix + "," + str(node.val))

    _print_all_paths(node, "")


# mirror

# double tree

# same tree (aka tree_equal)
def tree_equal(root_a: TreeNode, root_b: TreeNode) -> bool:
    # two empty trees are equal
    if root_a is None and root_b is None:
        return True

    if root_a is None or root_b is None:
        return False

    return (tree_equal(root_a.left, root_b.left) and
            tree_equal(root_a.right, root_b.right) and
            root_a.val == root_b.val)


# count trees
def count_trees(n: int) -> int:
    pass


# is-bst version 1
def is_bst(node: TreeNode) -> bool:
    if node is None:
        return True

    # check if this node satisfies BST axiom
    if node.left and node.val < get_min_val_bst_iter(node.left).val:
        return False

    if node.right and node.val >= get_max_val_bst_iter(node.right).val:
        return False

    if is_bst(node.left) == False or is_bst(node.right) == False:
        return False

    return True


def is_bst_v2(node: TreeNode) -> bool:
    def _is_bst_v2(node: TreeNode, min_val: int, max_val: int) -> bool:
        if node is None:
            return True

        # check this node
        if node.val < min_val or node.val >= max_val:
            return False

        return _is_bst_v2(node.left, min_val, node.val) and _is_bst_v2(node.right, node.val, max_val)

    # check this Node
    return _is_bst_v2(node, -(2 << 31), (2 << 31))


if __name__ == "__main__":
    bst = build_right_bst()

    node = is_bst_v2(bst)
    print(node)
