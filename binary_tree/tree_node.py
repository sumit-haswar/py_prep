
class TreeNode:

    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.val = data
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return '{} <-- {} --> {}'.format(self.left.data if self.left else 'None',
                                        self.data,
                                        self.right.data if self.right else 'None')
