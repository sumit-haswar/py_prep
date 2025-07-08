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

def build_123_bt():
    return TreeNode(2, TreeNode(1), TreeNode(3))

def build_prime_bst():
    _2 = TreeNode(2)
    _5 = TreeNode(5)
    _13 = TreeNode(13)
    _31 = TreeNode(31)
    _41 = TreeNode(41)
    _53 = TreeNode(53)

    _29 = TreeNode(29, None, _31)

    _17 = TreeNode(17, _13, None)
    _37 = TreeNode(37, _29, _41)

    _3 = TreeNode(3, _2, _5)
    _11 = TreeNode(11, None, _17)
    _23 = TreeNode(23, None, _37)
    _47 = TreeNode(47, None, _53)

    _7 = TreeNode(7, _3, _11)

    _43 = TreeNode(43, _23, _47)

    return TreeNode(19, _7, _43)

