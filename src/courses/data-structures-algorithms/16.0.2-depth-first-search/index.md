---
lesson_name: "Warm-up: Depth-First Search"
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

### Warm-up: Depth-First Search

Write a function `dfs_order(n, edges, start)` that runs a **depth-first search** on an undirected graph (nodes `0` to `n - 1`) starting at `start`, and returns the nodes in the order they are **first visited**.

To make the order predictable, build the adjacency list with neighbours in edge order (like the previous exercise), and always explore neighbours in that order.

For example, with `edges = [[0, 1], [0, 2], [1, 3]]` and `start = 0`, DFS goes `0 -> 1 -> 3`, backs up to `0`, then visits `2`, so the answer is `[0, 1, 3, 2]`. Nodes that can't be reached from `start` are not included.

**Hint:** use a recursive helper `visit(node)` that marks `node` as visited, appends it to the result, and then calls `visit` on each **unvisited** neighbour. The visited set is what stops you from going back and forth between two connected nodes forever.

---

### Tests

<ul>
<li id="test-1"><code>dfs_order(4, [[0, 1], [0, 2], [1, 3]], 0)</code> should return <code>[0, 1, 3, 2]</code></li>
<li id="test-2"><code>dfs_order(1, [], 0)</code> should return <code>[0]</code></li>
<li id="test-3"><code>dfs_order(5, [[0, 1], [1, 2], [2, 0], [3, 4]], 0)</code> should return <code>[0, 1, 2]</code></li>
<li id="test-4"><code>dfs_order(5, [[0, 1], [1, 2], [2, 0], [3, 4]], 4)</code> should return <code>[4, 3]</code></li>
<li id="test-5"><code>dfs_order(6, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5]], 0)</code> should return <code>[0, 1, 3, 4, 2, 5]</code></li>
<li id="test-6"><code>dfs_order(6, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5]], 3)</code> should return <code>[3, 1, 0, 2, 5, 4]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def dfs_order(n, edges, start):
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = set()
    order = []

    def visit(node):
        visited.add(node)
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visit(neighbor)

    visit(start)
    return order
```

Each call goes as deep as it can before returning, and returning **is** the backtracking step: the call stack remembers where to continue. Every node is visited once and every edge is checked twice (once from each end), so the cost is `O(V + E)`.

You can also write DFS iteratively with your own stack (`stack.pop()` instead of recursion). That avoids Python's recursion limit on very large graphs, but the visiting order can differ slightly unless you push neighbours in reverse.

</details>
