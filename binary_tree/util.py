from .tree_node import TreeNode

def build_123():
    one = TreeNode(1)
    three = TreeNode(3)
    return TreeNode(2, one, three)


def build_1_to_10_bst():
    """
                    5
                3        9
               2  4    7   10
              1       6 8
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


def print_bfs(root):
    pass
