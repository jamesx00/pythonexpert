---
lesson_name: Advanced Graphs Basics
code_editor: False
code_execution: False
adding_file_allowed: False
section: Advanced Graphs
---

## Why This Pattern Matters &#x1F4A1;

Plain BFS finds the fewest *edges*. Once edges have **weights** (distances, costs, times), the path with the fewest edges isn't necessarily the cheapest. This section adds the standard tools for weighted graphs: **Dijkstra** for shortest paths, **Prim/Kruskal** for minimum spanning trees, **union-find** (from the Graphs section) inside Kruskal, and **Bellman-Ford** when you need to limit how many edges a path uses.

## Spotting It &#x1F50D;

- "Minimum **cost / time / effort** to reach ___" with weighted edges → **Dijkstra**.
- "Connect all points with **minimum total cost**" → **minimum spanning tree** (Prim or Kruskal).
- "**At most k stops**" → Bellman-Ford limited to `k + 1` rounds (or BFS by level).
- "Use **every edge exactly once**" → Eulerian path (Hierholzer's algorithm, *Reconstruct Itinerary*).
- Ordering rules derived from comparisons → build a graph, then **topological sort** (*Alien Dictionary*).

## Dijkstra &#x1F6E3;&#xFE0F;

Dijkstra is BFS with a **min-heap** instead of a queue: always expand the cheapest known node next.

```python
import heapq

def dijkstra(n, edges, start):      # edge: (u, v, weight)
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
    dist = [float("inf")] * n
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue                 # stale entry, already found better
        for nxt, w in graph[node]:
            if d + w < dist[nxt]:
                dist[nxt] = d + w
                heapq.heappush(heap, (dist[nxt], nxt))
    return dist
```

Time is `O(E log V)`. Dijkstra **requires non-negative weights**.

## Union-Find Recap &#x1F517;

You built union-find in the Graphs section. It comes back here inside Kruskal's algorithm: `union(a, b)` returning `False` means the edge would form a cycle, so you skip it.

## Minimum Spanning Tree &#x1F333;

- **Kruskal:** sort edges by weight, and `union` each edge unless it would form a cycle. Stop after `n - 1` edges.
- **Prim:** run Dijkstra-like expansion from any node, but the heap key is the **edge weight alone**, not the total distance.

## Tips & Gotchas &#x1F4CC;

- **Skip stale heap entries** (`if d > dist[node]: continue`). `heapq` has no decrease-key, so outdated entries stay in the heap.
- **Dijkstra's answer** for "time for everything to be reached" is `max(dist)`. If any value is still `inf`, some node is unreachable.
- **Grid with costs** (*Swim in Rising Water*): Dijkstra where the "distance" is the max cell value along the path instead of a sum. The heap pattern doesn't change.
- **Bellman-Ford with k stops:** copy `dist` each round (`temp = dist[:]`) so one round can't chain several edges.
- **Union-find with rank/size** keeps trees shallow. Path compression alone is usually enough in Python.
- **Lexicographic Eulerian paths:** sort neighbours, pop them in order, and add nodes to the result *after* exploring (post-order), then reverse.
