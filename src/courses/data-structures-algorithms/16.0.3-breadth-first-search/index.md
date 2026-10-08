---
lesson_name: "Warm-up: Breadth-First Search"
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

### Warm-up: Breadth-First Search

Write a function `bfs_order(n, edges, start)` that runs a **breadth-first search** on an undirected graph (nodes `0` to `n - 1`) starting at `start`, and returns the nodes in the order they are visited.

Build the adjacency list with neighbours in edge order, and enqueue neighbours in that order.

For example, with `edges = [[0, 1], [0, 2], [1, 3]]` and `start = 0`, BFS visits everything 1 step away (`1`, `2`) before anything 2 steps away (`3`), so the answer is `[0, 1, 2, 3]`. Compare that with DFS's `[0, 1, 3, 2]` on the same graph.

**Hint:** use a `deque` as a queue. Mark a node visited **when you add it to the queue**, not when you pop it. Otherwise a node can be added several times by different neighbours.

---

### Tests

<ul>
<li id="test-1"><code>bfs_order(4, [[0, 1], [0, 2], [1, 3]], 0)</code> should return <code>[0, 1, 2, 3]</code></li>
<li id="test-2"><code>bfs_order(1, [], 0)</code> should return <code>[0]</code></li>
<li id="test-3"><code>bfs_order(5, [[0, 1], [1, 2], [2, 0], [3, 4]], 0)</code> should return <code>[0, 1, 2]</code></li>
<li id="test-4"><code>bfs_order(6, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5]], 0)</code> should return <code>[0, 1, 2, 3, 4, 5]</code></li>
<li id="test-5"><code>bfs_order(6, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5]], 3)</code> should return <code>[3, 1, 0, 4, 2, 5]</code></li>
<li id="test-6"><code>bfs_order(5, [[0, 4], [0, 1], [1, 2], [2, 3], [3, 4]], 0)</code> should return <code>[0, 4, 1, 3, 2]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
from collections import deque

def bfs_order(n, edges, start):
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order
```

A queue is first-in, first-out, so nodes come out in the order they were discovered, which is in order of distance from `start`. That's why BFS is the go-to for shortest paths in unweighted graphs. Using `deque.popleft()` keeps each dequeue `O(1)`; `list.pop(0)` would be `O(n)`. Total cost: `O(V + E)`.

</details>
