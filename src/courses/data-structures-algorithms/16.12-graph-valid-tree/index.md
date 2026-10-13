---
lesson_name: Graph Valid Tree
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n log n)
  space: O(n)
hints:
  - "A tree with `n` nodes always has the same number of edges. Once the edge count is right, what else must be true?"
  - "Use *Union-Find* from *Graphs Basics*: a valid tree has exactly `n - 1` edges and no cycle. Check the count first, then `union` every edge. If an edge's ends already share a root, it closes a cycle."
  - "Template: if `len(edges) != n - 1`, return `False`. `parent = list(range(n))`. For each `[a, b]`: if `find(a) == find(b)`, return `False`; otherwise link the roots. At the end, return whether every node has the same root."
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

### Graph Valid Tree

You are given `n` nodes labeled `0` to `n - 1` and a list of undirected edges `[a, b]`. Write a function `valid_tree(n, edges)` that returns `True` if these edges form a valid tree — meaning the graph is fully connected and contains no cycles — and `False` otherwise.

For example, with `n = 4` and `edges = [[0, 1], [1, 2], [2, 3]]`, every node is reachable and there is exactly one path between any pair of nodes, so the function should return `True`. But with `n = 4` and `edges = [[0, 1], [1, 2], [2, 3], [1, 3]]`, the extra edge creates a cycle, so the function should return `False`.

---

### Tests

<ul>
<li id="test-1"><code>valid_tree(4, [[0, 1], [1, 2], [2, 3]])</code> should return <code>True</code></li>
<li id="test-2"><code>valid_tree(4, [[0, 1], [1, 2], [2, 3], [1, 3]])</code> should return <code>False</code></li>
<li id="test-3"><code>valid_tree(5, [[0, 1], [2, 3]])</code> should return <code>False</code></li>
<li id="test-4"><code>valid_tree(1, [])</code> should return <code>True</code></li>
<li id="test-5"><code>valid_tree(3, [[0, 1], [1, 2], [0, 2]])</code> should return <code>False</code></li>
<li id="test-6"><code>valid_tree(2, [[0, 1]])</code> should return <code>True</code></li>
<li id="test-7"><code>valid_tree(2, [])</code> should return <code>False</code></li>
<li id="test-8"><code>valid_tree(4, [[0, 1], [1, 2], [2, 0]])</code> should return <code>False</code></li>
<li id="test-9"><code>valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])</code> should return <code>True</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def valid_tree(n, edges):
    if len(edges) != n - 1:
        return False
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[ra] = rb

    return len({find(x) for x in range(n)}) == 1
```

Here `n` (also called `V`) is the number of nodes and `E` the number of edges.

**Brute force:** for each edge, remove it and check with a DFS whether its two ends are still connected, which would mean a cycle. Then run one more DFS to check that every node is reachable. That's `O(E * (V + E))`.

**Bottleneck:** each check walks over the whole graph again.

**Optimal idea:** a graph with `n` nodes is a tree exactly when it has `n - 1` edges and no cycle. The count costs nothing, and union-find spots a cycle as the edges are added.

**Why it's correct:** with no cycle, each edge merges two different groups, so `n - 1` edges merge the `n` starting groups into one. The graph is then connected with no cycle, which is a tree. If an edge joins two nodes already in the same group, it closes a cycle, and the graph isn't a tree. A graph with any other number of edges can't be a tree either.

**Complexity:** `O(n log n)` time, amortized, with path compression. `O(n)` space.

**Common mistakes:** checking only for cycles: `valid_tree(5, [[0, 1], [2, 3]])` has none but isn't connected. Checking only the edge count: test 8 has `n - 1` edges, but they form a cycle and leave node `3` alone. Forgetting that a single node with no edges is a valid tree.

</details>
