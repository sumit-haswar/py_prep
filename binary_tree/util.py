from .tree_node import TreeNode
import typing


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

    # set count
    two.count = 2
    three.count = 4
    seven.count = 3
    nine.count = 5
    five.count = 10

    return five


def build_epi_bst():
    _19 = TreeNode(19)
    _7 = TreeNode(7)
    _3 = TreeNode(3)
    _11 = TreeNode(11)
    _2 = TreeNode(2)
    _5 = TreeNode(5)
    _17 = TreeNode(17, TreeNode(13))
    _43 = TreeNode(43)
    _23 = TreeNode(23)
    _47 = TreeNode(47)
    _37 = TreeNode(37)
    _53 = TreeNode(53)
    _29 = TreeNode(29)
    _41 = TreeNode(41)
    _31 = TreeNode(31)

    _19.left = _7
    _19.right = _43
    _7.left = _3
    _7.right = _11
    _3.left = _2
    _3.right = _5
    _11.right = _17

    _43.left = _23
    _43.right = _47
    _23.right = _37
    _47.right = _53
    _37.left = _29
    _37.right = _41
    _29.right = _31

    return _19

def build_non_balanced_bst():
    pass


def build_perfect_bt():
    one = TreeNode(1)
    two = TreeNode(2, one, TreeNode(2.1))

    four = TreeNode(4, TreeNode(4.1), TreeNode(4.2))
    three = TreeNode(3, two, four)

    six = TreeNode(6)
    eight = TreeNode(8)
    seven = TreeNode(7, six, eight)
    ten = TreeNode(10, TreeNode(10.1), TreeNode(10.2))
    nine = TreeNode(9, seven, ten)

    five = TreeNode(5, three, nine)

    return five


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


def build_symmetric_tree():
    _14_1 = TreeNode(14)
    _14_2 = TreeNode(14)
    _32_1 = TreeNode(32, _14_1, _14_2)
    _4_1 = TreeNode(4, _32_1)
    _7_1 = TreeNode(7)
    _9_1 = TreeNode(9, _7_1, _4_1)

    _14_3 = TreeNode(14)
    _14_4 = TreeNode(14)
    _32_2 = TreeNode(32, _14_3, _14_4)
    _4_2 = TreeNode(4, None, _32_2)
    _7_2 = TreeNode(7)
    _9_2 = TreeNode(9, _4_2, _7_2)

    return TreeNode(5, _9_1, _9_2)


def print_bfs(root):
    pass


def build_bit_tree() -> TreeNode:
    m = TreeNode(1)
    n = TreeNode(0)
    p = TreeNode(0)
    l = TreeNode(1, None, m)
    o = TreeNode(0, None, p)
    k = TreeNode(0, l, n)
    j = TreeNode(0, None, k)
    i = TreeNode(1, j, o)

    d = TreeNode(0)
    e = TreeNode(1)
    h = TreeNode(0)
    g = TreeNode(1, left=h, right=None)
    c = TreeNode(0, left=d, right=e)
    f = TreeNode(1, left=None, right=g)
    b = TreeNode(0, left=c, right=f)
    a = TreeNode(1, left=b, right=i)

    return a


def tree_equal(node_a, node_b):
    if not node_a and not node_b:
        return True
    elif node_a and node_b:
        return node_a.data == node_b.data \
               and tree_equal(node_a.left, node_b.left) \
               and tree_equal(node_a.right, node_b.right)
    else:
        return False
