from linked_list import linked_list_problems
from binary_tree import binary_tree_problems

x = 0
factor = 17


def hash(key, mod):
    hash = 0
    for ch in key:
        hash = (hash * factor + ord(ch))  # % mod

    return hash


def rolling_hash(pattern, limit):
    curr = pattern[:limit]
    curr_hash = hash(curr, 4)

    pow_factor = factor ** (limit - 1)

    print("{}:{}".format(curr, curr_hash))
    for ch in pattern[limit:]:
        leftmost = curr[0]
        curr_right = curr[1:limit]
        curr = curr_right + ch

        curr_hash = curr_hash - (ord(leftmost) * pow_factor)
        curr_hash = curr_hash * factor + ord(curr[-1])

        print("{}:{}".format(curr, curr_hash))





if __name__ == '__main__':
    # linked_list_problems.main()
    # seq = [
    #     'sumit', 'haswar', 'sumit', 'john', 'aaa', 'haswar'
    # ]
    #
    # for key in seq:
    #     print('{}:{}'.format(key, hash(key,100)))

    rolling_hash('abcdefghdefabc', 3)
