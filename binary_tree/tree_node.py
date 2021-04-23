class TreeNode:

    def __init__(self,
                 data=None,
                 left=None,
                 right=None,
                 parent=None):
        self.data = data
        self.val = data
        self.left = left
        self.right = right
        self.parent = parent
        self.count = 1
        self.next = None

    def __str__(self):
        return '{} <-- {} --> {}'.format(self.left.data if self.left else 'None',
                                         self.data,
                                         self.right.data if self.right else 'None')

    def is_leaf(self):
        if self.left is None and self.right is None:
            return True

        return False


class BinaryTreeIterator:

    def _stack_nodes(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def __init__(self, root):
        self.stack = []
        self._stack_nodes(root)

    def next(self):
        curr_node = self.stack.pop()
        self._stack_nodes(curr_node.right)
        return curr_node.val

    def has_next(self):
        if self.stack:
            return True
        else:
            return False
