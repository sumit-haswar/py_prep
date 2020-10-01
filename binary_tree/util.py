from .tree_node import TreeNode


def print_node(node):
    node_str = '{0}<-- [{1}] -->{2}'.format(node.left.val if node.left else 'null',
                                            node.val,
                                            node.right.val if node.right else 'null')
    print(node_str)


def build_123():
    one = TreeNode(1)
    three = TreeNode(3)
    return TreeNode(2, one, three)


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

    return five


def build_non_balanced_bst():
    pass


def build_balanced_bst():
    pass


def build_random_non_bst():
    """
    height = 4, number of nodes = 9
    :return:
    """
    one = TreeNode(1, None, TreeNode(20))
    ten = TreeNode(10)
    four = TreeNode(4, ten, one)
    forty = TreeNode(40)
    forty_four = TreeNode(44)
    seven = TreeNode(7, forty_four)
    eight = TreeNode(8, four, forty)
    twelve = TreeNode(12, eight, seven)
    return twelve


def build_random_tree():
    """
           5
          / \
         4   8
        /   / \
       11  13  4
       / \\     \
      7   2      1
    """
    _11 = TreeNode(11, TreeNode(7), TreeNode(2))
    _4 = TreeNode(4, None, TreeNode(1))
    _8 = TreeNode(8, TreeNode(13), _4)
    return TreeNode(5, _4, _8)


def build_epi_binary_tree():
    _28 = TreeNode(28)
    _0 = TreeNode(0)
    _17 = TreeNode(17)
    _3 = TreeNode(3, _17, None)
    _271 = TreeNode(271, _28, _0)
    _561 = TreeNode(561, None, _3)
    _6 = TreeNode(6, _271, _561)
    _16 = TreeNode(16)

    root = TreeNode(314, _6, _16)

    return root


def print_bfs(root):
    pass
