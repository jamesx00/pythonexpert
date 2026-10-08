from functools import lru_cache


def longest_increasing_path(matrix):
    if not matrix or not matrix[0]:
        return 0
    rows, cols = len(matrix), len(matrix[0])

    @lru_cache(maxsize=None)
    def dfs(r, c):
        best = 1
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                best = max(best, 1 + dfs(nr, nc))
        return best

    result = max(dfs(r, c) for r in range(rows) for c in range(cols))
    dfs.cache_clear()
    return result
