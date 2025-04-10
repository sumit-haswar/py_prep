import functools
from typing import Dict, List, Optional
from _3.trees.tree_node import TreeNode
from _3.linked_list import Node
from _3.searching.util import find_least_greater_than
import collections

# a hash function has one hard requirement: equal keys should have equal hash-codes!
# keys should be spread evenly
# should be fast and rolling

def string_hash(val: str, mod: int) -> int:
    mult = 997
    hash = 0
    for c in val:
        hash = (hash * mult + ord(c)) % mod

    return hash

def str_hash(val: str, mod: int) -> int:
    mult = 997
    return functools.reduce(lambda h, c: ( h * mult + ord(c) ) % mod, val, 0)


def find_anagrams(input: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)
    res : List[List[str]] = []
    for word in input:
        # find signature of this word
        signature = ''.join(sorted(word))
        anagrams[signature].append(word)

    for k,v in anagrams.items():
        if len(v) > 1:
            res.append(v)

    return res

# 12.2 is an anonymous letter constructible
def is_anonymous_letter_possible(letter_text: str, magazine_text: str) -> bool:
    # generate a counter dict from letter_text
    look_up = {}
    for c in letter_text:
        if c not in look_up:
            look_up[c] = 0

        look_up[c] = look_up[c] + 1

    # now iterate over magazine_text
    for c in magazine_text:
        if len(look_up) == 0:
            return True

        if c in look_up:
            look_up[c] = look_up[c] - 1
            if look_up[c] == 0:
                del look_up[c]

    return True if len(look_up) == 0 else False

# 12.3 implement an ISBN cache(LRU)
class MyLruCache:
    # must implement: lookup, insert and erase

    # insert should update that isbn should be most recent used entry

    # if not present return -1 or NULL
    def __init__(self, capacity: int):
        self._cache : dict[str, Node] = {}
        self._capacity : int = capacity

        self._head  = None
        self._tail = None

    def print_cache(self):
        print(self._cache)
        if self._head:
            print(self._head.print_till_tail())

    def insert(self, isbn: str, price: int):
        if isbn in self._cache:     # entry already in cache
            node = self._cache[isbn]
            self._move_to_front(node)
            return
        elif len(self._cache) == self._capacity:
            tail_isbn = self._remove_from_back()
            del self._cache[tail_isbn]

        node = Node((isbn, price))
        self._cache[isbn] = node
        self._move_to_front(node)

    def lookup(self, isbn: str):
        if isbn not in self._cache:
            raise Exception("key not found")

        node = self._cache[isbn]
        entry = node.val
        # move isbn entry to "front" and return price
        self._move_to_front(node)
        return entry

    def delete(self, isbn: str):
        if isbn not in self._cache:
            raise Exception("key not found")

        node = self._cache[isbn]

        if node is self._tail:
            self._remove_from_back()
        elif node is self._head:
            new_head = self._head.next
            self._head.next = None
            if new_head:
                new_head.prev = None
            self._head = new_head
        else: # node is somewhere in between
            next_node = node.next
            prev_node = node.prev
            prev_node.next = next_node
            next_node.prev = prev_node
            node.next = None
            node.prev = None

        del self._cache[isbn]

    def _remove_from_back(self):
        isbn = self._tail.val[0]
        new_tail = self._tail.prev
        self._tail.prev = None
        new_tail.next = None
        self._tail = new_tail

        return isbn

    def _move_to_front(self, node:Node):
        if self._head is None: # this is the first entry in the cache
            self._head = node
            self._tail = node

            self._head.next = None
            self._head.prev = None

            self._tail.next = None
            self._tail.prev = None
            return

        if self._head is node:  # node is already head, nothing to do
            return

        if self._tail is node:  # node is tail, so we need to also update self._tail
            # update self._tail
            new_tail = self._tail.prev

            new_tail.next = None
            self._tail = new_tail

            node.prev = None

            curr_head = self._head
            curr_head.prev = node
            node.next = curr_head
            self._head = node
            return

        # node is somewhere in between
        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        curr_head = self._head
        curr_head.prev = node
        node.next = curr_head
        self._head = node


class LruCache:

    def __init__(self):
        self._cache : collections.OrderedDict[str, float] = collections.OrderedDict()
        self._capacity : int = 10

    def insert(self, isbn: str, price: float):
        if isbn in self._cache: # item already in cache, no change in size
            price = self._cache.pop(isbn)
        elif len(self._cache) == self._capacity:    # cache is now AT capacity so remove least recently used
            self._cache.popitem(last=False)         # pop and discard last item

        self._cache[isbn] = price   # put item back at the top

    def lookup(self, isbn: str) -> Optional[float]:
        if isbn not in self._cache:
            return None

        price = self._cache.pop(isbn) # remove item from dictionary
        self._cache[isbn] = price     # put item back at the TOP
        return price

    def delete(self, isbn: str):
        return self._cache.pop(isbn, None) is not None


# 12.5 find the nearest repeated entries in an array
def find_nearest_repeated_entries(input_text : List[str]):
    nearest = None
    res = None
    lookup = {}
    for idx, word in enumerate(input_text):
        if word in lookup:  # found duplicate word
            diff = abs(idx - lookup[word])
            if not nearest or diff < nearest:
                res = (lookup[word], idx)
                nearest = diff

        lookup[word] = idx

    return nearest, res, input_text[res[0]]


# 12.1 test for palindromic permutations
def is_palindromic_permutation(input: str):
    lookup = {}
    for c in input:
        if c not in lookup:
            lookup[c] = 0
        lookup[c] = lookup[c] + 1

    odd_found = False

    for val in lookup.values():
        if val % 2 == 0:    # is even
            continue
        elif val % 2 == 1 and not odd_found:
            odd_found = True
        else:
            return False

    return True


# 12.4 compute the LCA optimizing for close ancestors
def get_lca(node_a: TreeNode, node_b: TreeNode) -> Optional[TreeNode]:
    lookup : Dict[int, TreeNode] = {}
    if not node_a or not node_b:
        return None
    curr_a, curr_b = node_a, node_b
    while curr_a or curr_b:
        # traverse up the tree in lock-steps
        if curr_a:
            if curr_a.val in lookup:
                return curr_a
            lookup[curr_a.val] = curr_a
            curr_a = curr_a.parent

        if curr_b:
            if curr_b.val in lookup:
                return curr_b
            lookup[curr_b.val] = curr_b
            curr_b = curr_b.parent

    return None


# 12.6 find the smallest sub-array covering all values
def find_smallest_covering_sub_array(text: List[str], keywords: set):
    left, right = 0, 0
    start, end = None, None

    keywords_remaining = len(keywords)
    keyword_counter = collections.Counter(keywords)

    while right < len(text):
        # shift right
        curr_right = text[right]
        if curr_right in keywords:
            # keyword found
            keyword_counter[curr_right] -= 1
            if keyword_counter[curr_right] >= 0:
                keywords_remaining -= 1

        while keywords_remaining == 0:
            # keep shifting left
            if (start == end is None) or (abs(left - right) < abs(start - end)):
                start = left
                end = right

            curr_left = text[left]
            if curr_left in keywords:
                keyword_counter[curr_left] += 1
                if keyword_counter[curr_left] > 0:
                    keywords_remaining += 1

            left += 1

        right += 1

    return start, end



# 12.9 find the length of the longest contained interval
def get_longest_contained_interval(arr: List[int]) -> int:
    lookup = set(arr)
    longest_interval_len = 0

    for num in arr:

        if num not in lookup:
            continue

        curr_internal_len = 1
        # iter left of num
        curr = num
        while True:
            curr = curr - 1
            if curr in lookup:
                curr_internal_len += 1
                lookup.remove(curr)
            else:
                break

        # iter right of num
        curr = num
        while True:
            curr = curr + 1
            if curr in lookup:
                curr_internal_len += 1
                lookup.remove(curr)
            else:
                break

        if curr_internal_len > longest_interval_len:
            longest_interval_len = curr_internal_len

    return longest_interval_len

# 12.7 O(n) find smallest subarray sequentially covering all values
class KeywordEntry:
    def __init__(self, idx, last_occurrence, shortest_subarray_len):
        self.idx = idx
        self.last_occurrence = last_occurrence
        self.shortest_subarray_len = shortest_subarray_len


def find_smallest_seq_covering_subset(text: List[str], keywords: List[str]):

    keyword_map : Dict[str, KeywordEntry] = {}
    shortest_dist = float('inf')
    result = (None, None)
    for idx, keyword in enumerate(keywords):
        entry = KeywordEntry(idx, -1, float('inf'))
        keyword_map[keyword] = entry

    for idx, word in enumerate(text):
        if word not in keyword_map:
            continue

        # we found a keyword
        if keyword_map[word].idx == 0:  # this is the first keyword
            keyword_map[word].shortest_subarray_len = 1
        else:                           # any following keyword
            prev_keyword = keywords[keyword_map[word].idx - 1]
            if keyword_map[prev_keyword] != float('inf'):  # prev keyword hasn't been found yet
                distance_to_prev_keyword = idx - keyword_map[prev_keyword].last_occurrence
                shortest_subarray_len = distance_to_prev_keyword + keyword_map[prev_keyword].shortest_subarray_len
                keyword_map[word].shortest_subarray_len = shortest_subarray_len

        keyword_map[word].last_occurrence = idx

        #
        if word == keywords[-1] and keyword_map[word].shortest_subarray_len < shortest_dist:
            shortest_dist = keyword_map[word].shortest_subarray_len
            result = (keyword_map[keywords[0]].last_occurrence, keyword_map[word].last_occurrence)


    return result

# 12.7 O(n.log n) find smallest subarray sequentially covering all values
def find_smallest_seq_covering_subset_opt(text: List[str], keywords: List[str]):
    ht : Dict[str, List[int]] = {}

    for idx, word in enumerate(text):
        if word not in keywords:
            continue
        if word not in ht:
            ht[word] = []
        ht[word].append(idx)

    res = []

    first_term_indices = ht[keywords[0]]

    smallest_seq_len = float('inf')

    for idx in first_term_indices:
        curr_keyword_idx = 1

        left = idx
        curr_res = [left]
        prev_idx = left
        is_covered = True
        while curr_keyword_idx <= (len(keywords) - 1):
            curr_keyword_indices = ht[keywords[curr_keyword_idx]]
            idx = find_least_greater_than(curr_keyword_indices, prev_idx)
            if idx is None:
                is_covered = False
                break

            curr_res.append(idx)
            prev_idx = idx

            curr_keyword_idx += 1

        if is_covered and abs(curr_res[0] - curr_res[-1]) < smallest_seq_len:
            # new smallest found
            smallest_seq_len = abs(curr_res[0] - curr_res[-1])
            res = curr_res

    return res


# 12.8 find the longest subarray with distinct entries
# todo revise and fix failing edge case
def get_longest_subarray_with_distinct_values(input: List[int]) -> (int, int):
    ht = {}
    longest_subarray_len = None
    longest_start_idx = 0
    res = (None, None)
    for idx, elem in enumerate(input):
        if elem in ht:
            elem_last_idx = ht[elem]
            # we found a duplicate, so check if curr_seq length > longest_subarray_len
            if elem_last_idx >= longest_start_idx:
                if longest_subarray_len is None or (idx - longest_start_idx > longest_subarray_len):
                    res = longest_start_idx, idx - 1
                    longest_subarray_len = idx - longest_start_idx
                longest_start_idx = elem_last_idx + 1

        ht[elem] = idx

    if longest_subarray_len is None:
        return 0, len(input) - 1

    return res


if __name__ == "__main__":

    my_cache = MyLruCache(4)
    my_cache.insert("a", 50)
    my_cache.insert("b", 60)
    my_cache.insert("c", 70)
    my_cache.insert("d", 80)
    my_cache.insert("e", 90)
    my_cache.print_cache()

    my_cache.delete("e")
    my_cache.print_cache()

    # print(res)
