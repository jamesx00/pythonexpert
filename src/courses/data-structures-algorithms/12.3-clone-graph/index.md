---
lesson_name: Clone Graph
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

### Clone Graph

Write a function `clone_graph(adj_list)` that takes an undirected graph described as an adjacency list — `adj_list[i]` is the list of node indices connected to node `i` — and returns a deep copy of it, in the same adjacency-list format. The copy must be built from brand-new inner lists (not the exact same list objects as the input), even though the returned structure should describe the same connections.

For example, given `[[1, 2], [0, 2], [0, 1]]` (three nodes forming a triangle, where node `0` connects to nodes `1` and `2`, and so on), the function should return a new adjacency list with the identical connections: `[[1, 2], [0, 2], [0, 1]]`.

---

### Tests

<ul>
<li id="test-1"><code>clone_graph([[1, 2], [0, 2], [0, 1]])</code> should return <code>[[1, 2], [0, 2], [0, 1]]</code></li>
<li id="test-2"><code>clone_graph([])</code> should return <code>[]</code></li>
<li id="test-3"><code>clone_graph([[]])</code> should return <code>[[]]</code></li>
<li id="test-4"><code>clone_graph([[1], [0]])</code> should return <code>[[1], [0]]</code></li>
<li id="test-5"><code>clone_graph([[1, 3], [0, 2], [1, 3], [0, 2]])</code> should return <code>[[1, 3], [0, 2], [1, 3], [0, 2]]</code></li>
<li id="test-6"><code>clone_graph([[1], [0, 2], [1]])</code> should return <code>[[1], [0, 2], [1]]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def clone_graph(adj_list):
    if not adj_list:
        return []

    clones = {}

    def dfs(node):
        if node in clones:
            return clones[node]
        clones[node] = []
        for neighbor in adj_list[node]:
            clones[node].append(neighbor)
        for neighbor in adj_list[node]:
            dfs(neighbor)
        return clones[node]

    dfs(0)
    return [clones[i] for i in range(len(adj_list))]
```

</details>
