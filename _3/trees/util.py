from _3.trees.tree_node import TreeNode


def build_1_to_10_bst():
    """
                     5
                 3        9
               2  4     7   10
              1        6 8
    :return:
    """
    one = TreeNode(1)
    two = TreeNode(2, one, None)

    four = TreeNode(4)
    three = TreeNode(3, two, four)

    six = TreeNode(6)
    eight = TreeNode(8)
    seven = TreeNode(7, six, eight)
    ten = TreeNode(10)
    nine = TreeNode(9, seven, ten)

    five = TreeNode(5, three, nine)

    # set parents
    one.parent = two
    two.parent = three
    four.parent = three
    three.parent = five

    six.parent = seven
    eight.parent = seven
    ten.parent = nine
    seven.parent = nine
    nine.parent = five

    # set count
    two.count = 2
    three.count = 4
    seven.count = 3
    nine.count = 5
    five.count = 10

    return five

def build_right_bst():
    """
          5
            \
              9
            7   10
           6 8
    :return:
    """
    six = TreeNode(6)
    eight = TreeNode(8)
    seven = TreeNode(7, six, eight)
    ten = TreeNode(10)
    nine = TreeNode(9, seven, ten)

    five = TreeNode(5, None, nine)

    # set parents

    six.parent = seven
    eight.parent = seven
    ten.parent = nine
    seven.parent = nine
    nine.parent = five

    # set count
    seven.count = 3
    nine.count = 5
    five.count = 10

    return five

def build_left_bst():
    """
                     5
                    /
                   3
                 2  4
               1
    :return:
    """
    one = TreeNode(1)
    two = TreeNode(2, one, None)

    four = TreeNode(4)
    three = TreeNode(3, two, four)

    five = TreeNode(5, three, None)

    # set parents
    one.parent = two
    two.parent = three
    four.parent = three
    three.parent = five

    # set count
    two.count = 2
    three.count = 4
    five.count = 10

    return five

def build_random_non_bst():
    """
    height = 4, number of nodes = 9
    :return:
    """
    one = TreeNode(0, None, TreeNode(20))
    ten = TreeNode(10)
    four = TreeNode(4, ten, one)
    forty = TreeNode(40)
    forty_four = TreeNode(44)
    seven = TreeNode(7, forty_four)
    eight = TreeNode(8, four, forty)
    twelve = TreeNode(12, eight, seven)
    return twelve