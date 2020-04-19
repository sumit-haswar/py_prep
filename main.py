from linked_list import Node
from linked_list import util
from linked_list import linked_list_problems

l = util.get_ordered_linked_list()

util.print_list(l)
l = linked_list_problems.sorted_insert(l, Node(11))
util.print_list(l)
