---
lesson_name: "Warm-up: Breadth-First Search"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(V + E)
  space: O(V)
hints:
  - "Every node 1 edge away from `start` should come out before any node 2 edges away. Which data structure hands items back in the order you put them in?"
  - "Use *BFS: Go Wide First* from *Graphs Basics*: a `deque` that starts with `start`. Pop from the left, append the node to the result, and enqueue each unvisited neighbour. Mark a node visited **when you enqueue it**, not when you pop it."
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

### Warm-up: Breadth-First Search

Write a function `bfs_order(n, edges, start)` that runs a **breadth-first search** on an undirected graph (nodes `0` to `n - 1`) starting at `start`, and returns the nodes in the order they are visited.

Build the adjacency list with neighbours in edge order, and enqueue neighbours in that order.

For example, with `edges = [[0, 1], [0, 2], [1, 3]]` and `start = 0`, BFS visits everything 1 step away (`1`, `2`) before anything 2 steps away (`3`), so the answer is `[0, 1, 2, 3]`. Compare that with DFS's `[0, 1, 3, 2]` on the same graph.

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

**Brute force:** the same loop with a plain list as the queue and `queue.pop(0)`. The order is right, but each `pop(0)` shifts the whole list, so the worst case is `O(V² + E)`.

**Bottleneck:** removing items from the front of a list.

**Optimal idea:** `collections.deque` pops from the left in `O(1)`. Marking nodes when they're enqueued means each node enters the queue once.

**Why it's correct:** a queue is first in, first out. `start` goes in first, then everything 1 edge away, and those nodes add everything 2 edges away behind them, and so on. So nodes come out in order of distance from `start`, and nodes at the same distance come out in the order they were found.

**Complexity:** `O(V + E)` time. `O(V)` extra space for the queue and `visited`.

**Common mistakes:** marking a node visited when it's popped instead of when it's pushed: two neighbours can both enqueue the same node, so it shows up twice in the result. Popping from the wrong end (`queue.pop()`), which turns the search into a DFS.

</details>
