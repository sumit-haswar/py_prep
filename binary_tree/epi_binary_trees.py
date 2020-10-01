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
    pass


#   9.3 get lca in a binary tree
def get_lca(root: TreeNode,
            node_a: TreeNode,
            node_b: TreeNode) -> TreeNode:
    """
    TODO
    :param root:
    :param node_a:
    :param node_b:
    :return:
    """

    def _get_lca(node: TreeNode, a: TreeNode, b: TreeNode):
        # base case
        if node is None:
            return {'found_a': False,
                    'found_b': False,
                    'lca': None}

        # node found
        if node is a or node is b:
            return {'found_a': node is a,
                    'found_b': node is b,
                    'lca': None}

        # look left
        left = _get_lca(node.left, a, b)

        if left['lca']:
            return left['lca']

        right = _get_lca(node.right, a, b)

        if left['lca'] or right['lca']:
            return left['lca'] if left['lca'] else right['lca']

        if (left['found_a'] or right['found_a']) \
                and (left['found_b'] or right['found_b']):
            return {'found_a': True,
                    'found_b': True,
                    'lca': node}

        return {'found_a': False,
                'found_b': False,
                'lca': None}

    return get_lca(root, node_a, node_b)


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
def get_path_with_sum(root: TreeNode):
    pass


#   9.7 inorder traversal without recursion

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
