---
lesson_name: "Warm-up: Dijkstra's Algorithm"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(E log V)
  space: O(V + E)
hints:
  - "BFS always expands the node with the fewest edges. With weights, which node should you expand next instead, and what data structure hands it to you quickly?"
  - "Use the *Dijkstra* template from *Advanced Graphs Basics*: a min-heap of `(cost_so_far, node)`. Pop the cheapest, skip it if `d > dist[node]` (a stale entry), and push a neighbour whenever `d + w < dist[v]` improves it. Turn any `inf` left at the end into `-1`."
rich_test_results: true
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

---

### Tests

<ul>
<li id="test-1"><code>dijkstra(3, [[0, 1, 4], [0, 2, 1], [2, 1, 2]], 0)</code> should return <code>[0, 3, 1]</code></li>
<li id="test-2"><code>dijkstra(1, [], 0)</code> should return <code>[0]</code></li>
<li id="test-3"><code>dijkstra(3, [[0, 1, 5]], 0)</code> should return <code>[0, 5, -1]</code></li>
<li id="test-4"><code>dijkstra(4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 10]], 0)</code> should return <code>[0, 1, 2, 3]</code></li>
<li id="test-5"><code>dijkstra(4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 10]], 2)</code> should return <code>[-1, -1, 0, 1]</code></li>
<li id="test-6"><code>dijkstra(5, [[0, 1, 2], [0, 2, 6], [1, 2, 3], [1, 3, 8], [2, 3, 0], [3, 4, 1]], 0)</code> should return <code>[0, 2, 5, 5, 6]</code></li>
<li id="test-7">Performance: 20,000 nodes in a line with about 40,000 edges, within 1 second</li>
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

Here `V` is the number of nodes and `E` the number of edges.

**Brute force:** Bellman-Ford. Go over every edge and relax it (`dist[v] = min(dist[v], dist[u] + w)`), and repeat until nothing changes. That can take `V - 1` rounds, so it's `O(V · E)`. Another slow version is Dijkstra that finds the closest unfinished node with a linear scan, which is `O(V²)`.

**Bottleneck:** both spend most of their time on nodes whose distance is already final, or looking for the next closest node.

**Optimal idea:** keep the candidates in a min-heap keyed by cost, so the cheapest one comes out in `O(log V)`. Each time a node's cost improves, push the new cost. A node can sit in the heap several times. When an old, more expensive copy comes out, skip it.

**Why it's correct:** weights are never negative, so a path can only get more expensive as it grows. When the cheapest entry in the heap is popped, any other route to that node would have to go through a node that costs at least as much already. So its distance is final, and relaxing its edges from that final distance is safe.

**Complexity:** `O(E log V)` time: each edge pushes at most one heap entry, and each push or pop costs `O(log E) = O(log V)`. `O(V + E)` extra space for the graph, `dist` and the heap.

**Common mistakes:** marking a node done when it's *pushed* instead of when it's *popped*, which can lock in a cost before a cheaper route shows up, as in test 1. Forgetting the stale-entry check, which still gives the right answer but redoes work. Returning `inf` instead of `-1` for nodes you can't reach.

</details>
