from typing import Optional

from _3.trees.tree_node import TreeNode
from _3.trees.util import build_1_to_10_bst


# lookup
def lookup(node: TreeNode, val: int) -> Optional[TreeNode]:
    if node is None:
        return None
    if node.val == val:
        return node

    left = lookup(node.left, val)
    if left:
        return left
    return lookup(node.right, val)


# insert
def insert(node: TreeNode, val: int) -> TreeNode:
    pass


# size

# max-depth
def size(node: TreeNode) -> int:
    if node is None:
        return 0

    return size(node.left) + 1 + size(node.right)

def get_max_depth(node: TreeNode) -> int:
    if node is None:
        return 0

    return max(node.left, node.right) + 1


# min-val
def get_min_val(node: TreeNode) -> int:
    pass


# print-tree

# print post-order

# has path sum
def has_path_sum(node: TreeNode, curr_val: int, val: int) -> bool:
    if node is None and curr_val == 0:
        return True
    elif node is None:
        return False

    return has_path_sum(node.left, curr_val - node.val, val) or \
           has_path_sum(node.right, curr_val - node.val, val)


# print paths

# mirror

# double tree

# same tree

# count trees

# is-bst


def _create_bt() -> TreeNode:
    pass


if __name__ == "__main__":
    root = build_1_to_10_bst()
    node = size(root)
    print(node)
