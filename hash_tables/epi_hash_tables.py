import typing
from typing import List, Set, Dict
import collections
from binary_tree import TreeNode
from linked_list import Node


def find_anagrams(list: List[str]) -> List[List[str]]:
    anagram_map = {}
    for word in list:
        signature = ''.join(sorted(word))
        if signature in anagram_map:
            anagram_map[signature].append(word)
        else:
            anagram_map[signature] = [word]

    return [word_list for word_list in
            anagram_map.values()
            if len(word_list) > 1]


class ContactList:
    def __init__(self, names):
        self.names = names

    def __hash__(self):
        return hash(frozenset(self.names))

    def __eq__(self, other):
        return set(self.names) == set(other.names)


def merge_contact_list(contacts: List[ContactList]):
    s = set(contacts)
    return list(s)


#   12.1 test for palindromic permutations
def is_palindromic_permutation(input: str) -> bool:
    counter_map = collections.Counter(input)
    return sum([val % 2 for val in counter_map.values()]) <= 1


#   12.2 is an anonymous letter constructable?
def is_anonymous_letter_possible(letter_text: str, magazine_text: str) -> bool:
    letter_counter_map = collections.Counter(letter_text)

    for char in magazine_text:
        if char in letter_counter_map:
            letter_counter_map[char] -= 1
            if letter_counter_map[char] == 0:
                del letter_counter_map[char]
                if not letter_counter_map:
                    return True

    return not letter_counter_map


#   12.3 implement an ISBN cache
class LruCache():
    def __init__(self):
        self.map = {}
        self.head = None
        self.tail = None
        self.count = 0
        self.threshold = 4

    def get(self, key: str):
        if key not in self.map:
            return None
        val = self.map[key]

        if val is not self.head:
            # move val from curr location to head
            curr_head = self.head

            # link val prev and next
            if val.prev:
                val.prev.next = val.next
            if val.next:
                val.next.prev = val.prev

            curr_head.prev = val
            val.next = curr_head
            self.head = val

        return val.data['val']

    def add(self, key: str, val):
        node = Node({'key': key, 'val': val})
        self.map[key] = node

        if self.count == self.threshold:  # remove from tail

            lru_key = self.tail.data['key']
            del self.map[lru_key]

            new_lru = self.tail.prev
            new_lru.next = None
            self.tail = new_lru
            self.count -= 1

        # this is the first entry
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
        else:
            curr_head = self.head
            if not self.tail.prev:
                self.tail.prev = curr_head
            curr_head.prev = node
            node.next = curr_head

            self.head = node
        self.count += 1

    def delete(self, key: str):
        pass


#   12.4 compute the LCA, optimizing for close ancestors
def get_lca(node_a: TreeNode, node_b: TreeNode) -> TreeNode:
    lookup = set()
    curr_a = node_a
    curr_b = node_b

    while curr_a or curr_b:
        if curr_a:
            if curr_a.data in lookup:
                return curr_a
            lookup.add(curr_a.data)
            curr_a = curr_a.parent

        if curr_b:
            if curr_b.data in lookup:
                return curr_b
            lookup.add(curr_b.data)
            curr_b = curr_b.parent

    return None


#   12.5 find the nearest repeated entries in an array
def get_nearest_repeated_entries(text: str):
    result = {"start": -1, "end": -1}
    diff = float('inf')
    word_last_idx_map = {}
    for idx, word in enumerate(text.split(" ")):
        if word in word_last_idx_map:
            last_idx = word_last_idx_map[word]
            curr_diff = abs(last_idx - idx)
            if curr_diff < diff:
                diff = curr_diff
                result['start'] = last_idx
                result['end'] = idx

        word_last_idx_map[word] = idx

    return result


#   12.6 find the smallest subarray covering all values
def get_smallest_subarray_cover(input: str, keywords: Set[str]):
    text = input.split(' ')

    keyword_set = collections.Counter(keywords)
    remaining_keywords = len(keyword_set)
    left = 0

    start = -1
    end = -1

    for right, curr in enumerate(text):
        if curr in keyword_set:
            keyword_set[curr] -= 1
            if keyword_set[curr] >= 0:
                remaining_keywords -= 1

        while remaining_keywords == 0:
            if (start == end == -1) or (abs(left - right) < abs(start - end)):
                start = left
                end = right
            candidate = text[left]
            if candidate in keyword_set:
                keyword_set[candidate] += 1
                if keyword_set[candidate] > 0:
                    remaining_keywords += 1
            left += 1

    return (start, end)


#   (12.8) find the longest subarray with distinct entries
def get_longest_subarray_with_distinct_values(A: List[int]):
    lookup: Dict[int, int] = {}
    result = 0
    longest_distinct_subarray_start_idx = 0
    result_idx = (-1, -1)
    for idx, elem in enumerate(A):
        if elem in lookup:
            elem_last_idx = lookup[elem]
            # find if curr element's last-idx is within longest_start_index and curr idx
            if elem_last_idx >= longest_distinct_subarray_start_idx:
                curr_result = idx - longest_distinct_subarray_start_idx
                if result is None or curr_result > result:
                    result = curr_result
                    result_idx = (longest_distinct_subarray_start_idx, idx - 1)
                longest_distinct_subarray_start_idx = elem_last_idx + 1

        lookup[elem] = idx

    # we again perform max wherein longest_distinct_subarray_start_idx till the last idx was unique
    return max(result, len(A) - longest_distinct_subarray_start_idx)

#   12.9 find the length of a longest contained interval
def get_longest_contained_interval(array: List[int]):
    lookup = set(array)
    result = 0
    for elem in array:
        if elem in lookup:

            lower_bound = elem - 1
            while lower_bound in lookup:
                lookup.remove(lower_bound)
                lower_bound -= 1

            upper_bound = elem + 1
            while upper_bound in lookup:
                lookup.remove(upper_bound)
                upper_bound += 1

            result = max(result, upper_bound - lower_bound - 1)

    return result

# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# todo
#   (12.7) find smallest subarray sequentially covering all values
#   (12.10) compute all string decompositions
#   (12.11) test the collatz conjecture
