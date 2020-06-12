from .util import *


# Solutions to linked-list problems defined in: http://cslibrary.stanford.edu/105/

# 3. build at head with push()
def build_at_head():
    head = None

    for e in [5, 4, 3, 2, 1]:
        head = push(head, e)

    return head


# 4. build with tail pointer
def build_at_tail():
    head = Node(1)
    curr = head

    for e in [2, 3, 4, 5, 6]:
        this = Node(e)
        curr.next = this
        curr = this

    return head


# questions
# 1. count
# Write a Count() function that counts the number of times a given int occurs in a list. The
# code for this has the classic list traversal structure as demonstrated in Length().
def count_occurrence(head, elem):
    if not head:
        return 0

    curr = head
    count = 0
    while curr:
        if (curr.data == elem):
            count = count + 1
        curr = curr.next

    return count


# 2. get Nth
# // Given a list and an index, return the data
# // in the nth node of the list. The nodes are numbered from 0.
# // Assert fails if the index is invalid (outside 0..length-1).
def get_nth(head, idx):
    assert head
    curr_idx = 0
    curr = head
    while curr:
        if curr_idx == idx:
            return curr.data
        curr = curr.next
        curr_idx = curr_idx + 1

    raise Exception('invalid idx')


# 3. delete list


# 4. pop
# The opposite of Push(). Takes a non-empty list
# and removes the front node, and returns the data
# which was in that node.
def pop(head):
    assert head
    new_head = head.next
    return new_head


# 5. insert Nth
# A more general version of Push().
# Given a list, an index 'n' in the range 0..length,
# and a data element, add a new node to the list so
# that it has the given index.
def insert_nth(head, idx, data):
    # insert at head case
    if idx == 0:
        new_node = Node(data, head)
        return new_node

    curr_idx = 0
    curr = head
    while curr:
        if curr_idx == idx - 1:
            # insert after curr
            new_node = Node(data, curr.next)
            curr.next = new_node
            return head

        curr = curr.next
        curr_idx = curr_idx + 1

    return head


# 6. sorted insert

def sorted_insert(head, new_node):
    """
    Write a SortedInsert() function which given a list that is sorted in increasing order, and a
    single node, inserts the node into the correct sorted position in the list. While Push()
    allocates a new node to add to the list, SortedInsert() takes an existing node, and just
    rearranges pointers to insert it into the list. There are many possible solutions to this
    problem.
    """
    # add at head
    if not head or head.data > new_node.data:
        new_node.next = head
        return new_node

    curr = head
    while curr.next:
        if curr.next.data > new_node.data:
            # add after curr
            new_node.next = curr.next
            curr.next = new_node
            return head
        curr = curr.next

    # add at tail
    curr.next = new_node
    return head


# 7. insert sort
def insert_sort(head):
    """
    Write an InsertSort() function which given a list, rearranges its nodes so they are sorted in
    increasing order. It should use SortedInsert().
    :param head:
    :return:
    """
    pass


# 8. append
# Append 'b' onto the end of 'a', and then set 'b' to NULL.
def append(a_head, b_head):
    if not b_head:
        return a_head
    elif not a_head:
        return b_head

    curr_a = a_head
    while curr_a.next:
        curr_a = curr_a.next

    curr_a.next = b_head
    return a_head


# 9. front back split
# Split the nodes of the given list into front and back halves,
# and return the two lists using the reference parameters.
# If the length is odd, the extra node should go in the front list.


# 10. remove duplicates
# Remove duplicates from a sorted list.
def remove_duplicates(head):
    pass


# 11. move node
# Take the node from the front of the source, and move it to
# the front of the dest.
# It is an error to call this with the source list empty.
def move_node(dest_head, source_head):
    pass


# 12. alternating split
# Given the source list, split its nodes into two shorter lists.
# If we number the elements 0, 1, 2, ... then all the even elements
# should go in the first list, and all the odd elements in the second.
# The elements in the new lists may be in any order.
def alternating_split(source_head):
    pass


# 13. shuffle merge
# Merge the nodes of the two lists into a single list taking a node
# alternately from each list, and return the new list.
# shuffle_merge() with {1, 2, 3} and {7, 13, 1} should yield {1, 7, 2, 13, 3, 1}.
def shuffle_merge(a_head, b_head):
    pass


# 14. sorted merge
# Takes two lists sorted in increasing order, and
# splices their nodes together to make one big
# sorted list which is returned.
def sorted_merge(a_head, b_head):
    pass

# 15. merge sort

# 16. sorted intersect

# 17. reverse

# 18. recursive reverse
