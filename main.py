from linked_list import linked_list_problems
from binary_tree import binary_tree_problems
from typing import List
from random import randint
import string

x = 0
factor = 47

base64_map = string.ascii_lowercase + string.ascii_lowercase + string.digits + '-_'


def hash(key, mod=None):
    hash = 0
    for ch in key:
        if not mod:
            hash = (hash * factor + ord(ch))
        else:
            hash = (hash * factor + ord(ch)) % mod
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


def base64_hash(url: str) -> str:
    pass


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


def _swap(a, b, seq):
    temp = seq[a]
    seq[a] = seq[b]
    seq[b] = temp


def find_kth_largest(list, k):
    def _get_pivot_idx(left, right, idx):

        # move elem at idx to end
        idx_elem = list[idx]
        list[idx] = list[right]
        list[right] = idx_elem

        pivot_idx = left

        while left < right:
            if list[left] < idx_elem:
                left += 1
            elif list[left] > idx_elem:
                _swap(left, pivot_idx, list)
                left += 1
                pivot_idx += 1

        _swap(right, pivot_idx, list)
        return pivot_idx

    # def _get_pivot_idx(left, right, idx) -> int:
    #     # move idx to right
    #     idx_val = list[idx]
    #     list[idx] = list[right]
    #     list[right] = idx_val
    #
    #     pivot_idx = left
    #     while left < right:
    #         if list[left] < idx_val:
    #             left += 1
    #         elif list[left] > idx_val:
    #             # swap list[left] with list[pivot_idx]
    #             curr = list[left]
    #             list[left] = list[pivot_idx]
    #             list[pivot_idx] = curr
    #
    #             pivot_idx += 1
    #             left += 1
    #     # re-swap with right
    #     list[right] = list[pivot_idx]
    #     list[pivot_idx] = idx_val
    #
    #     return pivot_idx

    def _find_kth_largest(left, right):

        idx = randint(left, right)

        pivot_idx = _get_pivot_idx(left, right, idx)

        if pivot_idx == (k - 1):
            return list[pivot_idx]
        elif pivot_idx > (k - 1):
            # look left
            return _find_kth_largest(left, pivot_idx - 1)
        else:
            return _find_kth_largest(pivot_idx + 1, right)

    return _find_kth_largest(0, len(list) - 1)


class Solution:
    def alienOrder(self, words: List[str]) -> str:

        if not words:
            return ""

        root_nodes = set()
        child_nodes = set()

        # first create graph
        graph = {}
        node_color = {}

        # graph[root] = []
        # node_color[root] = 'white'

        curr_word_idx = 1

        while curr_word_idx < len(words):

            prev_word = words[curr_word_idx - 1]
            curr_word = words[curr_word_idx]

            # move in lock steps
            prev_idx = 0
            curr_idx = 0
            while prev_idx < len(prev_word) and curr_idx < len(curr_word):
                if prev_word[prev_idx] != curr_word[curr_idx]:
                    source = prev_word[prev_idx]
                    sink = curr_word[curr_idx]

                    root_nodes.add(source)
                    if sink in root_nodes:
                        root_nodes.remove(sink)

                    node_color[source] = 'white'
                    node_color[sink] = 'white'

                    if source not in graph:
                        graph[source] = []

                    graph[source].append(sink)
                    break

                prev_idx += 1
                curr_idx += 1

            curr_word_idx += 1

        def _dfs(curr_node):
            if node_color[curr_node] == 'gray':
                raise Exception('cycle detected')
            node_color[curr_node] = 'gray'

            if curr_node in graph:
                for neighbor in graph[curr_node]:
                    if node_color[curr_node] != 'black':
                        _dfs(neighbor)
            top_sort.append(curr_node)
            node_color[curr_node] = 'black'

        top_sort = []
        try:
            # _dfs(root)
            # perform dfs on graph starting with any char from rootset
            for root in root_nodes:
                if node_color[root] == 'white':
                    _dfs(root)
        except Exception as ex:
            return ""

        return ''.join([str(n) for n in reversed(top_sort)])


if __name__ == '__main__':
    # print(hash('www.sumithaswar.com', 1000000))
    # print(hash('www.google.com', 1000000))
    # # print(hash('2a89f374ba8df3e5eefe475bdf61d176', 1000000000))
    #
    # test_url = "https://drive.google.com/file/d/1itbw9WYstpJMFVYqRYdKcVQVADRGVpnQ/view"
    i = 0
    n1, n2 = 0, 1

    seq = []
    while i < 20:
        nth = n1 + n2
        seq.append(nth)

        n1 = n2
        n2 = nth

        ratio = (n1 + n2)/n2
        print(ratio)

        i += 1

    print(seq)
    # print(base64_hash(test_url))

