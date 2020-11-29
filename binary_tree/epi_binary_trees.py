import typing
from typing import List, Iterable
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

        # preorder processing
        node_sum = (path_sum << 1) + node.data

        # if leaf return
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
            # this is the kth node
            return curr
        elif left_count >= k:
            # k is to the left of current
            curr = curr.left
        else:
            # kth is to the right of current
            # - 1 is for current node
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


#   (9.10) inorder traversal with constant space
def inorder_traversal(tree: TreeNode) -> List[int]:
    result = []
    curr = tree
    prev = None
    while curr:
        # we are coming downhill from curr to left
        if prev is curr.parent:
            if curr.left:
                next = curr.left
            else:
                result.append(curr.data)
                if curr.right:
                    next = curr.right
                else:
                    next = curr.parent
        # we came up from prev to curr(which is prev's parent)
        elif curr.left is prev:
            result.append(curr.data)
            if curr.right:
                next = curr.right
            else:
                next = curr.parent
        else:  # done with left, root and right, so go up
            next = curr.parent

        prev, curr = curr, next

    return result


#   9.12 reconstruct a binary tree from preorder traversal with markers
def reconstruct_bt_preorder(preorder: List[int]) -> TreeNode:
    """
                     5
                 3        9
               2  4     7   10
              1        6 8
    preorder: 5, 3, 2, 1, None, None, None, 4, None, None \
        9, 7, 6, None, None, 8, None, None, 10 None, None
    """

    def _reconstruct_bt_preorder(seq: Iterable[int]) -> TreeNode:
        curr = next(seq, None)
        if curr is None:
            return None
        left = _reconstruct_bt_preorder(seq)
        right = _reconstruct_bt_preorder(seq)
        return TreeNode(curr, left, right)

    return _reconstruct_bt_preorder(iter(preorder))


#   9.11 reconstruct a bt with traversal data (inorder and pre/postorder)
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


#   9.13 form a linked-list from the leaves of a binary tree
def create_list_of_leaves(root: TreeNode) -> List[TreeNode]:
    def _get_leaf_list(node: TreeNode, seq: List[int]):
        if node.left is None and node.right is None:
            seq.append(node.data)
            return

        if node.left:
            _get_leaf_list(node.left, seq)

        if node.right:
            _get_leaf_list(node.right, seq)

    list = []
    _get_leaf_list(root, list)
    return list


#   (9.15) compute right sibling tree for a perfect bt
def compute_right_sibling_tree(node: TreeNode):
    def _compute_right_sibling_tree(curr: TreeNode):
        while curr and curr.left:
            # set curr.left to curr.right
            curr.left.next = curr.right

            # set curr.right to curr's next's left
            curr.right.next = curr.next.left if curr.next else None

            # move to next
            curr = curr.next

    while node:
        _compute_right_sibling_tree(node)
        node = node.left


def compute_right_sibling_tree_recur(root: TreeNode):
    def _compute_right_sibling_tree_recur(node: TreeNode):
        if node is None:
            return
        if node.left:
            node.left.next = node.right

        if node.right:
            node.right.next = node.next.left if node.next else None

        _compute_right_sibling_tree_recur(node.left)
        _compute_right_sibling_tree_recur(node.right)

    _compute_right_sibling_tree_recur(root)
    return root


def _get_height(node: TreeNode):
    height = -1
    curr = node
    while (curr):
        height += 1
        curr = curr.parent
    return height


# 9.14 compute the exterior of a binary tree
def exterior_binary_tree(root: TreeNode) -> List[int]:
    def _traverse_left(node: TreeNode):
        if node is None or (node.left is None and node.right is None):
            return
        # pre-order processing
        exterior.append(node.data)

        if node.left:
            _traverse_left(node.left)
        else:
            _traverse_left(node.right)

    def _traverse_right(node: TreeNode):
        if node is None or (node.left is None and node.right is None):
            return
        if node.right:
            _traverse_right(node.right)
        else:
            _traverse_right(node.left)
        # post-order processing
        exterior.append(node.data)

    def _traverse_leaves(node: TreeNode):
        if node.left is None and node.right is None:
            exterior.append(node.data)
            return

        if node.left:
            _traverse_leaves(node.left)

        if node.right:
            _traverse_leaves(node.right)

    exterior = [root.data]

    # traverse left branch
    _traverse_left(root.left)
    # traverse leaves of root.left
    _traverse_leaves(root.left)
    # traverse leaves of root.right
    _traverse_leaves(root.right)
    # traverse right branch
    _traverse_right(root.right)

    return exterior

# todo  9.7 inorder traversal without recursion
