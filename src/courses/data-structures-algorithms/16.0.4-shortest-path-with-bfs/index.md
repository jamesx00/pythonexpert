---
lesson_name: "Warm-up: Shortest Path with BFS"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(V + E)
  space: O(V)
hints:
  - "BFS reaches nodes in order of their distance from `start`. What extra number do you need to keep for each node to answer the question?"
  - "Use `bfs_distances` from *BFS: Go Wide First* in *Graphs Basics*: keep `dist = {start: 0}`, and when you discover a neighbour, set `dist[neighbor] = dist[node] + 1`. Return `dist[end]` when you pop `end`, or `-1` if the queue runs out."
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

### Warm-up: Shortest Path with BFS

Write a function `shortest_path(n, edges, start, end)` that returns the **fewest number of edges** needed to travel from `start` to `end` in an undirected graph with nodes `0` to `n - 1`. Return `0` if `start == end`, and `-1` if `end` can't be reached.

For example, with `edges = [[0, 1], [1, 2], [2, 3], [0, 3]]`, `shortest_path(4, edges, 0, 2)` returns `2` (either `0 -> 1 -> 2` or `0 -> 3 -> 2`).

---

### Tests

<ul>
<li id="test-1"><code>shortest_path(4, [[0, 1], [1, 2], [2, 3], [0, 3]], 0, 2)</code> should return <code>2</code></li>
<li id="test-2"><code>shortest_path(3, [[0, 1]], 0, 2)</code> should return <code>-1</code></li>
<li id="test-3"><code>shortest_path(1, [], 0, 0)</code> should return <code>0</code></li>
<li id="test-4"><code>shortest_path(6, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [0, 5]], 0, 4)</code> should return <code>2</code></li>
<li id="test-5"><code>shortest_path(5, [[0, 1], [1, 2], [2, 3], [3, 4]], 4, 0)</code> should return <code>4</code></li>
<li id="test-6"><code>shortest_path(6, [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4], [4, 5]], 0, 5)</code> should return <code>4</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
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
```

**Brute force:** use DFS to walk every path from `start` to `end` that doesn't repeat a node, and keep the shortest. The number of such paths can grow exponentially with the size of the graph.

**Bottleneck:** DFS finds *a* path, not the shortest one, so it has to try them all.

**Optimal idea:** BFS. It reaches every node 1 edge away before any node 2 edges away, so the first time it reaches `end` is along a shortest path. `dist` works as both the visited set and the answer table.

**Why it's correct:** by induction on the distance. While the nodes at distance `d` are popped, they discover exactly the new nodes at distance `d + 1`. A node gets its `dist` the first time it's discovered, from a node one step closer to `start`, so the value is its true distance.

**Complexity:** `O(V + E)` time, `O(V)` extra space.

**Common mistakes:** returning `-1` or `1` when `start == end`: the answer is `0`, which the code gets by checking `end` when it's popped. Using DFS, which can return a longer path. This exact loop shows up in *Word Ladder*, *Rotting Oranges* and every "minimum number of moves" problem. Only the definition of "neighbour" changes.

</details>
