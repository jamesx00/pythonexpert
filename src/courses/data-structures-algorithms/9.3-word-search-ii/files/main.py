class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


def build_trie(words):
    root = TrieNode()
    for word in words:
        node = root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word = word
    return root


def find_words(board, words):
    return []
