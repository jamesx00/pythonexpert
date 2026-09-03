import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main


class RefTrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


def build_ref_trie(words):
    root = RefTrieNode()
    for word in words:
        node = root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = RefTrieNode()
            node = node.children[ch]
        node.word = word
    return root


def test_func(board, words):
    if not board or not board[0]:
        return []

    root = build_ref_trie(words)
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


inputs = [
    ([["a", "b", "c"], ["e", "f", "g"], ["i", "j", "k"]],
     ["abc", "abfe", "beg", "aei", "xyz"]),
    ([["a"]], ["a", "b"]),
    ([["a", "a"]], ["aa", "aaa"]),
    ([["x", "y"], ["y", "x"]], ["ab", "cd"]),
    ([["o", "a"], ["e", "t"]], ["oa", "oe", "eat", "ate"]),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = sorted(test_func(*i))
        assert sorted(main.find_words(*i)) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
