import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_word_search(board, word):
    rows, cols = len(board), len(board[0])

    def backtrack(r, c, i, visited):
        if i == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if (r, c) in visited or board[r][c] != word[i]:
            return False
        visited.add((r, c))
        found = (
            backtrack(r + 1, c, i + 1, visited)
            or backtrack(r - 1, c, i + 1, visited)
            or backtrack(r, c + 1, i + 1, visited)
            or backtrack(r, c - 1, i + 1, visited)
        )
        visited.remove((r, c))
        return found

    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0, set()):
                return True
    return False

inputs = [
    ([["C", "A", "T"], ["B", "R", "E"], ["D", "O", "G"]], "CARE"),
    ([["C", "A", "T"], ["B", "R", "E"], ["D", "O", "G"]], "DOT"),
    ([["A", "B"], ["C", "D"]], "ABDC"),
    ([["A", "B"], ["C", "D"]], "ABCD"),
    ([["X"]], "X"),
    ([["X"]], "XX"),
    ([["A", "A", "A"], ["A", "A", "A"]], "AAAAA"),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_word_search(*i)
        assert main.word_search(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
