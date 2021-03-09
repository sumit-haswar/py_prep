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


def equalSubSetSumPartition(s):
    # Write your code here
    def _subset_partition(slate, curr_idx, curr_total, slate_ids):
        if curr_total in dp_lookup:
            return dp_lookup[curr_total]

        # base-case
        if curr_total == 0:
            # found a subset, so generate result and return True
            # slate[] is all the result
            if soln_found[0] is False and slate_ids and sum(slate) == total:
                for i in slate_ids:
                    result[i] = True
                soln_found[0] = True
                return True

        if curr_idx >= len(s):
            return False

        # include curr_idx
        slate.append(s[curr_idx])
        slate_ids.append(curr_idx)
        with_curr = _subset_partition(slate, curr_idx + 1, curr_total - s[curr_idx], slate_ids)
        del slate[-1]
        del slate_ids[-1]

        without_curr = _subset_partition(slate, curr_idx + 1, curr_total, slate_ids)

        dp_lookup[curr_total] = with_curr or without_curr

        return dp_lookup[curr_total]

    total = sum(s)
    if total % 2 == 1:
        return []
    total = total // 2

    soln_found = [False]
    result = [False] * len(s)

    dp_lookup = {}

    _subset_partition([], 0, total, [])
    print(result)
    if soln_found[0]:
        return result
    else:
        return []


if __name__ == '__main__':
    # all_dec(3)
    # all_perm_non_repeating('abcd')

    x = [100,-100,99,-99,22,-22]
    equalSubSetSumPartition(x)

    # print([(l,r) for l in range(0,3) for r in range(0,3)])
    # print('----')
    # for l in range(0,3):
    #     for r in range(0,3):
    #         print((l,r))

