from _3.trees.tree_node import TreeNode
from _3.trees.util import *
from collections import deque
from typing import Optional, List


def get_height(node: TreeNode) -> int:
    if node is None:
        return -1

    return max(get_height(node.left), get_height(node.right)) + 1


#   14.1    test if a binary tree satisfies a bst property
def is_bst(root: TreeNode) -> bool:
    def _is_bst_internal(node: TreeNode, minimum: float, maximum: float) -> bool:
        if not node:
            return True

        # check if this node DOES NOT violate bst rule
        if node.val < minimum or node.val > maximum:
            return False

        return _is_bst_internal(node.left, minimum, node.val) and _is_bst_internal(node.right, node.val, maximum)

    return _is_bst_internal(root, float("-inf"), float("inf"))


def is_bst_bfs(root: TreeNode) -> bool:
    queue = deque()
    queue.append((root, (float("-inf"), float("inf"))))

    while queue:
        entry = queue.popleft()
        node = entry[0]
        minimum = entry[1][0]
        maximum = entry[1][1]
        # check bst rule violation
        if node.val < minimum or node.val > maximum:
            return False

        if node.left:
            queue.append((node.left, (minimum, node.val)))

        if node.right:
            queue.append((node.right, (node.val, maximum)))

    return True


def get_right_most(node: TreeNode) -> Optional[TreeNode]:
    if node.right:
        return get_right_most(node.right)
    return node


#   14.2    find the first key greater than a given value in a bst(successor)
def find_successor(root: TreeNode, val: int):
    candidate = None
    curr_node = root
    while curr_node:
        if val < curr_node.val:
            candidate = curr_node
            curr_node = curr_node.left
        elif val >= curr_node.val:
            curr_node = curr_node.right

    return candidate


#   14.3    find k largest elements in a bst
def find_k_largest(root: TreeNode, k: int):
    res = []

    def _find_k_largest(node: TreeNode, k: int):
        if not node:
            return

        # go right
        _find_k_largest(node.right, k)
        # process this node
        if len(res) < k:
            res.append(node.val)
            _find_k_largest(node.left, k)

    _find_k_largest(root, k)
    return res


#   14.4    compute the LCA in a bst
def find_lca(root: TreeNode, node_a: TreeNode, node_b: TreeNode):
    if node_a.val > node_b.val:
        node_a, node_b = node_b, node_a

    def _find_lca(curr_node: TreeNode) -> Optional[TreeNode]:
        if not curr_node:
            return None

        if node_a.val == curr_node.val or node_b.val == curr_node.val:
            return curr_node
        elif node_a.val < curr_node.val < node_b.val:
            return curr_node
        else:
            return _find_lca(curr_node.left) if (
                    node_a.val < curr_node.val and node_b.val < curr_node.val) else _find_lca(curr_node.right)

    return _find_lca(root)


#   14.5    generate a bst from traversal data
def generate_bst() -> TreeNode:
    pass


#   14.6    find the closest entries in three sorted arrays
def find_closest_trio(a: List[int], b: List[int], c: List[int]):
    pass


#   14.8    build a min height BST from a sorted array
def build_min_height_bst(arr: List[int]):

    def _build_bst(arr, left: int, right: int):
        if left > right:
            return None
        # base case: arr of just 1 length
        if left == right:
            return TreeNode(arr[left])

        mid_idx = left + (right - left)//2
        curr_node = TreeNode(arr[mid_idx])
        curr_node.left = _build_bst(arr, left, mid_idx - 1)
        curr_node.right = _build_bst(arr, mid_idx + 1, right)

        return curr_node

    return _build_bst(arr, 0, len(arr) - 1)

#   14.10   the range lookup problem
#   14.11   add credits

#   todo
#       14.7
#       14.9

if __name__ == "__main__":
    # root = build_prime_bst()
    root = build_min_height_bst([2,3,5,7,11])
    print(root)
