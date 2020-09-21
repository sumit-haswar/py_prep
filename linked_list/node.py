
class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.val = data
        self.next = next

    def __str__(self):
        return "{} -> {}".format(self.data,
                                 self.next.data if self.next else '')
