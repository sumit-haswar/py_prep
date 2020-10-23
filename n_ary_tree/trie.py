from typing import Optional, List


class TrieNode():

    def __init__(self, word=None):
        self.is_word = False
        self.word = word
        self.children = {}


class Trie():

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        curr = self.root
        prefix_till_now = []

        for idx, ch in enumerate(word):
            if ch in curr.children:
                curr = curr.children[ch]
                prefix_till_now.append(ch)
            else:
                for ch in word[idx:]:
                    prefix_till_now.append(ch)
                    new_node = TrieNode(''.join(prefix_till_now))
                    curr.children[ch] = new_node
                    curr = new_node
                break

        # curr.word = word
        curr.is_word = True

    def prefix_search(self, prefix: str):
        prefix_node = self._get_trie_node(prefix)
        if prefix_node:
            word_list = []
            self._traverse_all(prefix_node, word_list)
            return word_list
        else:
            return []

    def _get_trie_node(self, word: str) -> Optional[TrieNode]:
        curr = self.root

        for idx, ch in enumerate(word):
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                return None

        return curr

    def _traverse_all(self, subtree_node: TrieNode, word_list: List[str]):
        if not subtree_node:
            return
        if not subtree_node.children:
            word_list.append(subtree_node.word)
            return
        for child in subtree_node.children.values():
            self._traverse_all(child, word_list)

    # todo
    # def delete(self, word)
