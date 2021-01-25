# This class structure and code is derived from Erik Demaine's `AVL trees, AVL sort` lecture
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-notes/

class BSTNode():

    def __init__(self, key, parent, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

    def find(self, key):
        if self.key == key:
            return self
        elif self.key < key:
            # look right
            return self.right.find(key) if self.right else None
        else:
            # look left
            return self.left.find(key) if self.left else None

    def find_min(self):
        if self.left is None:
            return self
        else:
            return self.left.find_min()

    def next_larger(self) -> 'BSTNode':
        """Returns the node with the next larger key (the successor) in the BST."""
        # if right node exists, find left-most of sub-tree at right
        if self.right is not None:
            return self.right.find_min()
        # keep going up, till you find a node which is NOT the left node of its parent
        current = self
        while current.parent is not None and current is current.parent.right:
            current = current.parent
        return current.parent

    def insert(self, node):
        """Inserts a node into the subtree rooted at this node."""
        if node.key < self.key:
            # insert as left-child or insert at left-child
            if self.left:
                self.left.insert(node)
            else:
                self.left = node
                node.parent = self
        else:
            if self.right:
                self.right.insert(node)
            else:
                self.right = node
                node.parent = self

    def delete(self):
        if not self.left or not self.right: # node either has no left OR no right child
            if self is self.parent.left:    # if this node is left child of its parent
                self.parent.left = self.left or self.right
                if self.parent.left:
                    self.parent.left.parent = self.parent
            else:
                self.parent.right = self.left or self.right
                if self.parent.right:
                    self.parent.right.parent = self.parent
        else:  # node has both left and right child
            # get next larger of node
            next_node = self.next_larger()
            # swap current and next_larger values
            next_node.key, self.key = self.key, next_node.key
            return next_node.delete()


class BST():

    def __init__(self, root: BSTNode=None):
        self.root = root

    def find(self, key:int):
        return self.root.find(key)

    def find_min(self):
        return self.root.find_min()

    def next_larger(self, key: int):
        node = self.find(key)
        if node:
            return node.next_larger()
        else:
            return None

    def delete(self, key: int):
        node = self.root.find(key)
        if not node:
            return None
        else:
            if node is self.root:
                pass
            else:
                return node.delete()

    def insert(self, key: int):
        new_node = BSTNode(key, None)
        if self.root is None:
            self.root = new_node
        else:
            self.root.insert(new_node)
        return new_node
