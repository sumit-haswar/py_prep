from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = {}
        self.sentences = defaultdict(int)


class TrieContainer:
    def __init__(self):
        self.root = TrieNode()

    def add_to_trie(self, word, count = 1):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
            curr.sentences[word] += count

if __name__ == "__main__":
    trie = TrieContainer()
    trie.add_to_trie("sumit")
    trie.add_to_trie("summit")
    print(trie.root)