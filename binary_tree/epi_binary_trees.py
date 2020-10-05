import typing
from typing import List
from .tree_node import TreeNode


#   9.1 test if tree is height balanced
def is_balanced(root: TreeNode) -> bool:
    def _is_balanced(node: TreeNode):
        if not node:
            return {'is_balanced': True, 'height': -1}

        left = _is_balanced(node.left)

        if left['is_balanced'] is False:
            return {'is_balanced': False, 'height': None}

        right = _is_balanced(node.right)
        if right['is_balanced'] is False:
            return {'is_balanced': False, 'height': None}

        if abs(left['height'] - right['height']) > 1:
            return {'is_balanced': False, 'height': None}

        height = max(left['height'], right['height']) + 1
        return {'is_balanced': True, 'height': height}

    return _is_balanced(root)['is_balanced']


#   9.2 test if binary tree is symmetric
def is_symmetric(root: TreeNode) -> bool:
    def _is_symmetric(a: TreeNode, b: TreeNode) -> bool:
        if a is None and b is None:
            return True
        elif a is not None and b is not None:
            return a.data == b.data \
                   and _is_symmetric(a.left, b.right) \
                   and _is_symmetric(a.right, b.left)
        else:
            return False

    return _is_symmetric(root.left, root.right)


#   9.3 get lca in a binary tree
def get_lca(root: TreeNode,
            node_a: TreeNode,
            node_b: TreeNode) -> TreeNode:
    def _get_lca(node: TreeNode, a: TreeNode, b: TreeNode):
        # base case
        if node is None:
            return {'count': 0,
                    'lca': None}

        # look left
        left = _get_lca(node.left, a, b)

        if left['count'] == 2:
            return left

        # look right
        right = _get_lca(node.right, a, b)

        if right['count'] == 2:
            return right

        count = left['count'] + right['count'] + (a, b).count(node)

        return {'count': count,
                'lca': node if count == 2 else None}

    return _get_lca(root, node_a, node_b)['lca']


#   9.4 get lca when nodes have parent pointers
def get_parent_pointer_lca(node_a: TreeNode, node_b: TreeNode) -> bool:
    node_a_height = _get_height(node_a)
    node_b_height = _get_height(node_b)

    if node_b_height > node_a_height:
        node_a, node_b = node_b, node_a
        node_a_height, node_b_height = node_b_height, node_a_height

    # ascend a till height same as b
    while node_a_height != node_b_height:
        node_a = node_a.parent
        node_a_height -= 1

    # move in lock steps
    while node_a is not node_b:
        node_a = node_a.parent
        node_b = node_b.parent

    return node_a


#   9.5 root to leaf path sum
def get_path_sum(root: TreeNode):
    def _get_path_sum(node: TreeNode, path_sum):

        if node is None:
            return 0

        node_sum = (path_sum << 1) + node.data
        if not node.left and not node.right:
            return node_sum

        return _get_path_sum(node.left, node_sum) + _get_path_sum(node.right, node_sum)

    return _get_path_sum(root, 0)


#   9.6 find root to leaf path with specified sum
def get_path_with_sum(root: TreeNode, sum: int):
    def _get_path_with_sum(node, value, path):
        if node is None:
            if value == 0:
                return True, path
            else:
                return False, ''
        if path:
            path += ',' + str(node.data)
        else:
            path = str(node.data)

        left = _get_path_with_sum(node.left, value - node.data, path)
        if left[0]:
            return True, left[1]

        right = _get_path_with_sum(node.right, value - node.data, path)
        if right[0]:
            return True, right[1]

        return False, path

    result = _get_path_with_sum(root, sum, '')
    return result[1] if result[0] else ''


#   9.8 kth node in an inorder traversal
def get_kth_node(root: TreeNode, k: int) -> TreeNode:
    curr = root
    while curr:
        left_count = curr.left.count if curr.left else 0
        if left_count + 1 == k:
            # this is the node
            return curr
        elif left_count >= k:
            curr = curr.left
        else:
            curr = curr.right
            k = k - left_count - 1

    return None


#   9.9 compute the successor (node with parents)
def get_successor(node: TreeNode) -> TreeNode:
    if node.right:
        # return the leftmost child of right
        curr = node.right
        while curr.left:
            curr = curr.left
        return curr
    curr = node
    while curr:
        if curr.parent and curr.parent.left is curr:
            return curr.parent
        curr = curr.parent

    return None

#   9.10 inorder traversal with constant space (Morris Traversal)
def inorder_traversal(root: TreeNode) -> List[int]:
    pass


#   9.11 reconstruct a binary tree with traversal data
#   (inorder and pre/postorder)
def reconstruct_bt(inorder: List[int], preorder: List[int]) -> TreeNode:
    # generate inorder-map
    inorder_map = {}
    for idx, elem in enumerate(inorder):
        inorder_map[elem] = idx

    def _reconstruct_bt(in_start, in_end, pre_start, pre_end):

        if in_start > in_end:
            return None

        if in_start == in_end:
            return TreeNode(inorder[in_start])

        node_data = preorder[pre_start]
        inorder_idx = inorder_map[node_data]

        left_node_count = inorder_idx - in_start

        left_in_start = in_start
        left_in_end = inorder_idx - 1
        left_pre_start = pre_start + 1
        left_pre_end = pre_start + left_node_count

        right_in_start = inorder_idx + 1
        right_in_end = in_end
        right_pre_start = left_pre_end + 1
        right_pre_end = pre_end

        return TreeNode(node_data,
                        _reconstruct_bt(left_in_start,
                                        left_in_end,
                                        left_pre_start,
                                        left_pre_end),
                        _reconstruct_bt(right_in_start,
                                        right_in_end,
                                        right_pre_start,
                                        right_pre_end))

    return _reconstruct_bt(0, len(inorder) - 1, 0, len(preorder) - 1)

    #   (9.15) compute the right sibling tree


def compute_right_sibling_tree():
    pass


# todo  9.7 inorder traversal without recursion
# todo  9.12 reconstruct a binary tree from preorder traversal with markers


def _get_height(node: TreeNode):
    height = -1
    curr = node
    while (curr):
        height += 1
        curr = curr.parent
    return height
