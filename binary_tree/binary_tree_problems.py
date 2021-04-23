"""
this module contains solutions to problems listed in
http://cslibrary.stanford.edu/110/
Most of the solutions are inspired from the pdf document on this page.
For details regarding problem and solutions pls refer the original document:
    http://cslibrary.stanford.edu/110/BinaryTrees.pdf

"""

from .util import *


# 2.
def get_size(root):
    if root is None:
        return 0
    return get_size(root.left) + get_size(root.right) + 1


# 3. max depth
# same as get height
def get_max_depth(root):
    if root is None:
        return -1
    left = get_max_depth(root.left) + 1
    right = get_max_depth(root.right) + 1

    if left > right:
        return left
    else:
        return right


# 4. min value
def get_min_val(root):
    # base case
    if root is None or root.left is None:
        return root

    return get_min_val(root.left)


# 4.1 max value
def get_max_val(root):
    if root is None or root.right is None:
        return root

    return get_max_val(root.right)


# 5. print tree in-order
def print_inorder(root):
    # base-case
    if root is None:
        return
    print_inorder(root.left)
    print(root.val)
    print_inorder(root.right)


# 6. print post-order
def print_postorder(root):
    if root is None:
        return
    print_postorder(root.left)
    print_postorder(root.right)
    print(root.val)


# 7. tree has path sum = some value
def has_path_sum(root, sum):
    if root.left is None and root.right is None:
        return (sum - root.val) == 0

    if root.left is not None:
        left = has_path_sum(root.left, sum - root.val)
        if left:
            return True

    if root.right is not None:
        right = has_path_sum(root.right, sum - root.val)
        if right:
            return True

    return False


def has_path_sum_2(root, sum):
    if root is None and sum == 0:
        return True
    elif root is None:
        return False

    return has_path_sum(root.left, sum - root.val) \
           or has_path_sum(root.right, sum - root.val)


# 8.Given a binary tree, print out all of its root-to-leaf paths.
def print_all_paths(root, path_so_far):
    # base-case
    if root is None:
        return

    if root.left is None and root.right is None:
        path = "{0} -> {1}".format(path_so_far, root.val)
        print(path)
        return

    if path_so_far:
        path_so_far = path_so_far + ' -> ' + str(root.val)
    else:
        path_so_far = str(root.val)
    print_all_paths(root.left, path_so_far)
    print_all_paths(root.right, path_so_far)


# 9. Change a tree so that the roles of the left and right pointers are swapped at every node.
def mirror(root):
    if root is None:
        return
    # swap left and right for this node
    left = root.left
    root.left = root.right
    root.right = left

    # continue downstream
    mirror(root.left)
    mirror(root.right)


# 10. double tree
# For each node in a binary search tree, create a new duplicate node, and insert the
# duplicate as the left child of the original node.
# The resulting tree should still be a binary search tree.
def double_tree(root):
    if root is None:
        return

    # duplicate this node
    duplicate = TreeNode(root.val, root.left, None)
    original_left = root.left
    root.left = duplicate

    double_tree(original_left)
    double_tree(root.right)


# 11.
def same_tree(tree_a, tree_b):
    if tree_a is None and tree_b is None:
        return True
    elif tree_a is not None and tree_b is not None:
        if tree_a.val == tree_b.val:
            return same_tree(tree_a.left, tree_b.left) \
                   and same_tree(tree_a.right, tree_b.right)
        else:
            return False
    else:
        return False


# 12. count trees
# given the number of distinct values, computes the number of structurally unique binary
# search trees that store those values.
def count_trees(num_keys):
    pass


# is bst
# version - 1
def is_bst_inefficient(root):
    if root is None:
        return True

    if root.left is not None:
        if get_min_val(root.left).val > root.left.val:
            return False

    if root.right is not None:
        if get_max_val(root.right).val < root.right.val:
            return False

    # recursive calls
    if is_bst_inefficient(root.right) is False \
            or is_bst_inefficient(root.left) is False:
        return False

    return True


def is_bst(root, min, max):
    if root is None:
        return True

    # check this node
    if root.val < min:
        return False

    if root.val > max:
        return False

    return is_bst(root.left, min, root.val) \
           and is_bst(root.right, root.val, max)


def is_bst_bfs(root):
    if root is None:
        return True

    queue = [{'node': root, 'min': 0, 'max': 99999}]

    while (queue):
        curr = queue.pop()
        curr_node = curr['node']

        # check if this node does to break the bst constraint
        if curr_node.val < curr['min'] or curr_node.val > curr['max']:
            return False

        # add left and right to the queue
        if curr_node.left:
            queue.append({'node': curr_node.left,
                          'min': curr['min'],
                          'max': curr_node.val})

        if curr_node.right:
            queue.append({'node': curr_node.right,
                          'min': curr_node.val,
                          'max': curr['max']})

    return True


# todo tree-list recursion problem !!

class NodeInfo:
    def __init__(self, min_val, max_val, is_bst=False, size=0, max_size=0):
        self.min_val = min_val
        self.max_val = max_val
        self.is_bst = is_bst
        self.size = size
        self.max_size = max_size


def find_largest_bst_count(root):
    def _is_leaf(node):
        return node.left_ptr is None and node.right_ptr is None

    def _is_bst(node):

        # base-cases
        if node is None:
            return True, 0

        if _is_leaf(node):
            return NodeInfo(node.val, node.val, True, 1, 1)

        # no left child
        if node.left_ptr is None:
            right_info = _is_bst(node.right_ptr)
            if right_info.is_bst and root.val <= right_info.min_val:
                curr_size = 1 + right_info.size
                max_size = max(curr_size, right_info.max_size)
                return NodeInfo(node.val, right_info.max_val, True, curr_size, max_size)
            else:
                return NodeInfo(None, None, False, 1, right_info.max_size)

        # no right child
        if node.right_ptr is None:
            left_info = _is_bst(node.left_ptr)
            if left_info.is_bst and root.val >= left_info.max_val:
                curr_size = left_info.size + 1
                max_size = max(curr_size, left_info.max_size)
                return NodeInfo(left_info.min_val, node.val, True, curr_size, max_size)
            else:
                return NodeInfo(None, None, False, 1, left_info.max_size)

        left_info = _is_bst(node.left_ptr)
        right_info = _is_bst(node.right_ptr)

        # check if this node is-bst valid
        if left_info.is_bst and right_info.is_bst and left_info.max_val <= node.val <= right_info.min_val:
            curr_size = 1 + left_info.size + right_info.size
            max_size = max(curr_size, max(left_info.size, right_info.size))
            return NodeInfo(left_info.min_val, right_info.max_val, True, curr_size, max_size)
        else:
            return NodeInfo(None, None, False, 1, max(left_info.max_size, right_info.max_size))

    if root is None:
        return 0

    root_info = _is_bst(root)

    return root_info.max_size

def main():
    # todo create binary trees util build methods
    #   for example: root = build_1_to_10_bst()
    #   invoke required methods to be tested

    print('is-bst bfs')
    assert is_bst_bfs(build_123())
    assert is_bst_bfs(build_random_non_bst()) is False
    assert is_bst_bfs((build_1_to_10_bst()))
    assert is_bst_bfs((build_balanced_bst()))
    assert is_bst_bfs((build_random_tree())) is False
