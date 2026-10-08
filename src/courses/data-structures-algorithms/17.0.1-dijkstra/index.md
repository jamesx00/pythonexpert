---
lesson_name: "Warm-up: Dijkstra's Algorithm"
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 1
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 2
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
    id: 1
    name: Python
---

### Warm-up: Dijkstra's Algorithm

Write a function `dijkstra(n, edges, start)` for a **directed, weighted** graph with nodes `0` to `n - 1`. Each edge is `[u, v, w]`: a one-way road from `u` to `v` with cost `w` (always `>= 0`). Return a list where position `i` is the cheapest total cost to get from `start` to node `i`, or `-1` if node `i` can't be reached.

For example:

```python
dijkstra(3, [[0, 1, 4], [0, 2, 1], [2, 1, 2]], 0)   # -> [0, 3, 1]
```

The direct edge `0 -> 1` costs `4`, but `0 -> 2 -> 1` costs only `1 + 2 = 3`. Plain BFS can't see this because it counts edges, not costs.

**Hint:** it's BFS with a min-heap. Store `(cost_so_far, node)` in the heap and always pop the cheapest. When you pop a node whose cost is worse than the best already recorded in `dist`, it's a stale entry, so skip it. Otherwise, try to improve each neighbour: if `d + w < dist[v]`, update it and push it.

---

### Tests

<ul>
<li id="test-1"><code>dijkstra(3, [[0, 1, 4], [0, 2, 1], [2, 1, 2]], 0)</code> should return <code>[0, 3, 1]</code></li>
<li id="test-2"><code>dijkstra(1, [], 0)</code> should return <code>[0]</code></li>
<li id="test-3"><code>dijkstra(3, [[0, 1, 5]], 0)</code> should return <code>[0, 5, -1]</code></li>
<li id="test-4"><code>dijkstra(4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 10]], 0)</code> should return <code>[0, 1, 2, 3]</code></li>
<li id="test-5"><code>dijkstra(4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 10]], 2)</code> should return <code>[-1, -1, 0, 1]</code></li>
<li id="test-6"><code>dijkstra(5, [[0, 1, 2], [0, 2, 6], [1, 2, 3], [1, 3, 8], [2, 3, 0], [3, 4, 1]], 0)</code> should return <code>[0, 2, 5, 5, 6]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
import heapq

def dijkstra(n, edges, start):
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))

    dist = [float("inf")] * n
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        for nxt, w in graph[node]:
            if d + w < dist[nxt]:
                dist[nxt] = d + w
                heapq.heappush(heap, (dist[nxt], nxt))
    return [x if x != float("inf") else -1 for x in dist]
```

Because weights are non-negative, the cheapest node in the heap can never be improved later, so its distance is final when it's popped. A node can be pushed several times as better routes are found. The `d > dist[node]` check throws away the outdated copies. Runtime is `O(E log V)`. *Network Delay Time* is this function plus `max(dist)`.

</details>
