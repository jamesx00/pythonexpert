from collections import deque

def shortest_path(n, edges, start, end):
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    dist = {start: 0}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node == end:
            return dist[node]
        for neighbor in graph[node]:
            if neighbor not in dist:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    return -1
