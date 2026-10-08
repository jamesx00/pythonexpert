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


def find_words(board, words):
    if not board or not board[0]:
        return []

    root = build_trie(words)
    rows, cols = len(board), len(board[0])
    found = set()

    def dfs(r, c, node):
        ch = board[r][c]
        if ch not in node.children:
            return
        nxt = node.children[ch]
        if nxt.word is not None:
            found.add(nxt.word)

        board[r][c] = '#'
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                dfs(nr, nc, nxt)
        board[r][c] = ch

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root)

    return list(found)
