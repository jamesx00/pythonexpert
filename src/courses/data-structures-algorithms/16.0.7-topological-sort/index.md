---
lesson_name: "Warm-up: Topological Sort"
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

### Warm-up: Topological Sort

A **directed** edge `[a, b]` means "`a` must come before `b`" (for example, course `a` is a prerequisite of course `b`). A **topological order** lists all nodes so that every edge points forward.

Write a function `topo_sort(n, edges)` for nodes `0` to `n - 1` that returns **any** valid topological order as a list. If the graph has a cycle, no order exists, so return `[]`.

For example, `topo_sort(4, [[0, 1], [0, 2], [1, 3], [2, 3]])` could return `[0, 1, 2, 3]` or `[0, 2, 1, 3]`. Both are accepted.

**Hint (Kahn's algorithm):**

1. Count each node's **in-degree**: how many edges point *into* it.
2. Put every node with in-degree `0` (no prerequisites) in a queue.
3. Pop a node, add it to the order, and decrement the in-degree of everything it points to. Any node that hits `0` joins the queue.
4. If the order has fewer than `n` nodes at the end, some nodes were stuck in a cycle.

---

### Tests

<ul>
<li id="test-1"><code>topo_sort(4, [[0, 1], [0, 2], [1, 3], [2, 3]])</code> should return a valid order, e.g. <code>[0, 1, 2, 3]</code></li>
<li id="test-2"><code>topo_sort(2, [[0, 1], [1, 0]])</code> should return <code>[]</code> (the graph has a cycle)</li>
<li id="test-3"><code>topo_sort(1, [])</code> should return a valid order, e.g. <code>[0]</code></li>
<li id="test-4"><code>topo_sort(3, [])</code> should return a valid order, e.g. <code>[0, 1, 2]</code></li>
<li id="test-5"><code>topo_sort(6, [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]])</code> should return a valid order, e.g. <code>[4, 5, 2, 0, 3, 1]</code></li>
<li id="test-6"><code>topo_sort(4, [[0, 1], [1, 2], [2, 3], [3, 1]])</code> should return <code>[]</code> (the graph has a cycle)</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
from collections import deque

def topo_sort(n, edges):
    graph = [[] for _ in range(n)]
    indegree = [0] * n
    for a, b in edges:
        graph[a].append(b)
        indegree[b] += 1

    queue = deque(i for i in range(n) if indegree[i] == 0)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nxt in graph[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    return order if len(order) == n else []
```

A node only enters the queue once all of its prerequisites are already in `order`, so every edge points forward. Nodes on a cycle wait for each other forever, their in-degree never reaches `0`, and they never get added, which is why `len(order) < n` detects a cycle. This is the engine behind *Course Schedule I & II* and *Alien Dictionary*. The DFS alternative is to append each node **after** visiting all its descendants (post-order), then reverse.

</details>
