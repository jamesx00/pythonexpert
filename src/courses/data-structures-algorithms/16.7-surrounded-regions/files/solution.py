def surrounded_regions(board):
    rows, cols = len(board), len(board[0]) if board else 0
    safe = set()

    def dfs(r, c):
        if (r, c) in safe or r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O':
            return
        safe.add((r, c))
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dfs(r + dr, c + dc)

    for r in range(rows):
        dfs(r, 0)
        dfs(r, cols - 1)
    for c in range(cols):
        dfs(0, c)
        dfs(rows - 1, c)

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O' and (r, c) not in safe:
                board[r][c] = 'X'
    return board
