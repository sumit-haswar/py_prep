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
