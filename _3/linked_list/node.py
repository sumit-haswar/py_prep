class Node:

    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return f"{self.val} -> {self.next.val if self.next else ''}"

    def print_till_tail(self):
        curr = self
        values = []
        while curr:
            values.append(str(curr.val))
            curr = curr.next

        print(",".join(values))
