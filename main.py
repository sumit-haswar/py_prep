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


def _is_letter(ch):
    return True


# a12b3 --> ["a12b3","A12b3","a12B3","A12B3"]
def letter_case_permutation(input: str) -> List:
    def _letter_case_permutation(input: str, curr_idx: int, slate: List, result: List):
        if curr_idx >= len(input):
            # todo add o/p(slate) to result
            return

        curr_char = input[curr_idx]
        if _is_letter(curr_char):
            slate[curr_idx] = curr_char.lower()
            _letter_case_permutation(input, curr_idx + 1, slate, result)
            # todo .upper recursive call
        else:
            slate[curr_idx] = curr_char
            _letter_case_permutation(input, curr_idx + 1, slate, result)

    result = []
    curr_idx = 0
    slate = []
    _letter_case_permutation(input, curr_idx, slate, result)

    return result


def all_subsets(input: str) -> List:
    def _all_subset(input, curr_idx, slate, result):
        if curr_idx >= len(input):
            # print(slate)
            result.append("".join(slate))
            return

        curr_char = input[curr_idx]
        for i in [curr_char, '']:
            slate.append(i)
            # for duplicate entries in input skip over the duplicates, just taking the current one
            # curr_idx + k, where k is the count of total occurrence of
            _all_subset(input, curr_idx + 1, slate, result)
            del slate[-1]

    char_map = set()
    result = []
    curr_idx = 0
    slate = []
    _all_subset(input, curr_idx, slate, result)
    return result


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


def _bracket_violation(left, right):
    return left > right or left < 0 or right < 0


def well_formed_brackets(bracket_count):
    def _well_formed_brackets(slate, left, right):
        if _bracket_violation(left, right):
            return
        if left == 0 and right == 0:
            result.append(slate)
            return

        _well_formed_brackets(slate + "(", left - 1, right)
        _well_formed_brackets(slate + ")", left, right - 1)

    result = []
    _well_formed_brackets("", bracket_count, bracket_count)
    return result


if __name__ == '__main__':
    # linked_list_problems.main()
    # seq = [
    #     'sumit', 'haswar', 'sumit', 'john', 'aaa', 'haswar'
    # ]
    #
    # for key in seq:
    #     print('{}:{}'.format(key, hash(key,100)))
    def pow(n, k):
        if k == 1:
            return n
        return n * pow(n, k - 1)


    def subsets_a(n):
        if n == 0:
            return 1

        if n % 2 == 0:
            return 2 * subsets_a(n / 2)
        else:
            return 2 * subsets_a(n / 2) * subsets_a(n / 2)


    def fibo_iter(n):
        n_minus_1 = 1
        n_minus_2 = 0
        idx = 2
        while idx <= n:
            curr = n_minus_1 + n_minus_2
            n_minus_2 = n_minus_1
            n_minus_1 = curr
            idx += 1

        return n_minus_1


    def fibo_recur(n, n_minus_1, n_minus_2, idx):
        if idx > n:
            return n_minus_1
        return fibo_recur(n, n_minus_1 + n_minus_2, n_minus_1, idx + 1)


    def subsets(n):
        if n == 1:
            return 2
        return subsets(n - 1) + subsets(n - 1)


    print(subset_sum([7, 4, 3, 10, 5], 17))

    # print(fibo_iter(13))
    # print(fibo_recur(13, 1, 0, 2))
