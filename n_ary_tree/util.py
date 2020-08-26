from n_ary_tree import TreeNode


def print_n_ary_dfs(root):
    if root is None:
        return
    print(root.val)
    for child in root.children:
        print_n_ary_dfs(child)


def print_n_ary_bfs(root):
    """"""
    curr_queue = []
    next_queue = []

    curr_queue.append(root)

    while curr_queue:
        # pop front
        curr = curr_queue.pop(0)
        print(curr.val)

        for child in curr.children:
            next_queue.append(child)

        if len(curr_queue) == 0:
            print('--')
            # current level is done
            temp = curr_queue
            curr_queue = next_queue
            next_queue = temp

def build_random_n_ary_tree():
    """
             5
          / \   \
         44   8  12
        /   / \
       11  13  4
       / \     | \
      7 2 9 14     17  1
    """
    _7 = TreeNode(7)
    _2 = TreeNode(2)
    _9 = TreeNode(9)
    _14 = TreeNode(14)
    _17 = TreeNode(17)
    _1 = TreeNode(1)

    _11 = TreeNode(11, [_7, _2, _9, _14])
    _13 = TreeNode(13)
    _4 = TreeNode(4, [_17, _1])

    _44 = TreeNode(44, [_11])
    _8 = TreeNode(8, [_13, _4])
    _12 = TreeNode(12)

    root = TreeNode(5, [_44, _8, _12])

    return root

if __name__ == '__main__':
    root = build_random_n_ary_tree()
    # print_n_ary_bfs(root)
    print_n_ary_dfs(root)
