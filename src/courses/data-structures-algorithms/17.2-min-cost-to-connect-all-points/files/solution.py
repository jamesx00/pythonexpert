import heapq


def min_cost_connect_points(points):
    n = len(points)
    if n <= 1:
        return 0

    visited = [False] * n
    min_heap = [(0, 0)]
    total = 0
    connected = 0

    while min_heap and connected < n:
        cost, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total += cost
        connected += 1
        for v in range(n):
            if not visited[v]:
                dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                heapq.heappush(min_heap, (dist, v))

    return total
