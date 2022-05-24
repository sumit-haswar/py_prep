
class TreeNode:

    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.left.val if self.left else None} <-- {self.val} --> {self.right.val if self.right else None}"

    def is_leaf(self):
        if self.left is None and self.right is None:
            return True

        return False
