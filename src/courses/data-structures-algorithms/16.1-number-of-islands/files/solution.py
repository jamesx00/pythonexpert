def num_islands(grid):
    rows, cols = len(grid), len(grid[0]) if grid else 0
    visited = set()
    count = 0

    def bfs(r, c):
        queue = [(r, c)]
        visited.add((r, c))
        while queue:
            row, col = queue.pop()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, col + dc
                if (0 <= nr < rows and 0 <= nc < cols and
                        grid[nr][nc] == 1 and (nr, nc) not in visited):
                    visited.add((nr, nc))
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                bfs(r, c)
                count += 1
    return count
