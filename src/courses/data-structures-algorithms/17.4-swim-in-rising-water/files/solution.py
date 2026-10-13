import heapq


def swim_in_water(grid):
    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    min_heap = [(grid[0][0], 0, 0)]
    visited[0][0] = True
    result = 0

    while min_heap:
        t, r, c = heapq.heappop(min_heap)
        result = max(result, t)
        if r == n - 1 and c == n - 1:
            return result
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                visited[nr][nc] = True
                heapq.heappush(min_heap, (grid[nr][nc], nr, nc))

    return result
