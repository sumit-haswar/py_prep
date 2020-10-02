import typing
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
    pass


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


#   9.7 inorder traversal without recursion

#   9.8 kth node in an inorder traversal

#   9.9 compute the successor

#   9.10 inorder traversal with constant space

#   9.11 reconstruct a binary tree with traversal data

#   9.12 reconstruct a binary tree from preorder traversal with markers

#   (9.15) compute the right sibling tree


def _get_height(node: TreeNode):
    height = -1
    curr = node
    while (curr):
        height += 1
        curr = curr.parent
    return height
