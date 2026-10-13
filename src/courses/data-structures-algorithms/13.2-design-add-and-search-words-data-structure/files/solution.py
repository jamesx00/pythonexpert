class WordDictionary:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def add_word(self, word):
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = WordDictionary()
            node = node.children[ch]
        node.is_word = True

    def search(self, pattern):
        def dfs(node, i):
            if i == len(pattern):
                return node.is_word
            ch = pattern[i]
            if ch == '.':
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            if ch not in node.children:
                return False
            return dfs(node.children[ch], i + 1)

        return dfs(self, 0)
