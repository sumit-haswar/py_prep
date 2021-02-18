from linked_list import linked_list_problems
from binary_tree import binary_tree_problems
from typing import List

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


def all_permutations(input: str):
    def _all_perm(slate, num_placed, result):
        if num_placed >= len(slate):
            result.append(''.join(slate))
            return

        for curr_idx in range(num_placed, len(slate)):
            # swap
            # recur
            # swap back
            pass

    result = []
    _all_perm()
    return result


def subset_sum(input, target):
    def _subset_sum(input, curr_idx, slate, curr_sum):
        if curr_sum > target:
            return

        if curr_idx >= len(input):
            if curr_sum == target:
                result.append(",".join([str(x) for x in slate if x > 0]))
            return
        curr_num = input[curr_idx]
        for i in [curr_num, 0]:
            slate.append(i)
            _subset_sum(input, curr_idx + 1, slate, curr_sum + i)
            del slate[-1]

    result = []
    _subset_sum(input, 0, [], 0)
    return result


def all_dec_0(n):
    def _all_dec(n, slate, curr_idx):
        if curr_idx >= n:
            print("".join(slate))
            return

        for i in range(10):
            slate.append(str(i))
            _all_dec(n, slate, curr_idx + 1)
            del slate[-1]

    result = []
    slate = []
    _all_dec(n, slate, 0)
    return result


def all_perm_non_repeating(n):
    def _all_dec(slate, seq):
        if len(seq) == 0:
            print("".join(slate))
            return

        for i in range(len(seq)):
            slate.append(str(seq[i]))
            _all_dec(slate, seq[:i] + seq[i + 1:])
            del slate[-1]

    result = []
    slate = []
    _all_dec(slate, n)
    return result


if __name__ == '__main__':
    # all_dec(3)
    # all_perm_non_repeating('abcd')

    print([(l,r) for l in range(0,3) for r in range(0,3)])
    print('----')
    for l in range(0,3):
        for r in range(0,3):
            print((l,r))

