def word_search(board, word):
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
