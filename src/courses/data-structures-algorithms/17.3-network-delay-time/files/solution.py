import heapq
from collections import defaultdict


def network_delay_time(times, n, start):
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    dist = {}
    min_heap = [(0, start)]

    while min_heap:
        d, node = heapq.heappop(min_heap)
        if node in dist:
            continue
        dist[node] = d
        for nei, w in graph[node]:
            if nei not in dist:
                heapq.heappush(min_heap, (d + w, nei))

    if len(dist) != n:
        return -1
    return max(dist.values())
