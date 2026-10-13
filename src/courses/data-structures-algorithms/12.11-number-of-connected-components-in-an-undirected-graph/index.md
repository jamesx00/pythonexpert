---
lesson_name: Number of Connected Components in an Undirected Graph
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(V + E log V)
  space: O(V)
hints:
  - "Each separate group of connected nodes is one component. What should happen to the number of groups each time an edge joins two of them?"
  - "Use *Union-Find* from *Graphs Basics*: start with `n` groups and `union` the two ends of every edge. The number of different roots at the end is the answer. (A DFS from every unvisited node, counting how many you start, as in *Tips & Gotchas*, works just as well.)"
  - "Template: `parent = list(range(n))` and a `find` that walks up to the root. For each `[a, b]`, if `find(a) != find(b)`, set `parent[find(a)] = find(b)`. Return `len({find(x) for x in range(n)})`."
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

### Number of Connected Components in an Undirected Graph

You are given `n` nodes labeled `0` to `n - 1` and a list of undirected edges `[a, b]` connecting pairs of them. Write a function `count_components(n, edges)` that returns how many separate connected components the graph has. A node with no edges at all still counts as its own component.

For example, with `n = 5` and `edges = [[0, 1], [1, 2], [3, 4]]`, nodes `0`, `1`, and `2` are linked into one component, and nodes `3` and `4` form a second component, so the function should return `2`.

---

### Tests

<ul>
<li id="test-1"><code>count_components(5, [[0, 1], [1, 2], [3, 4]])</code> should return <code>2</code></li>
<li id="test-2"><code>count_components(5, [])</code> should return <code>5</code></li>
<li id="test-3"><code>count_components(4, [[0, 1], [1, 2], [2, 3]])</code> should return <code>1</code></li>
<li id="test-4"><code>count_components(1, [])</code> should return <code>1</code></li>
<li id="test-5"><code>count_components(6, [[0, 1], [2, 3], [4, 5]])</code> should return <code>3</code></li>
<li id="test-6"><code>count_components(3, [[0, 1], [0, 2], [1, 2]])</code> should return <code>1</code></li>
<li id="test-7"><code>count_components(6, [[5, 0], [3, 4], [0, 4]])</code> should return <code>3</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def count_components(n, edges):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    return len({find(x) for x in range(n)})
```

Here `V` is `n`, the number of nodes, and `E` is the number of edges.

**Brute force:** run a BFS from every node to collect its component, and count the different components found. Each component is explored once per node in it: `O(V * (V + E))`.

**Bottleneck:** the same component is explored again from each of its nodes.

**Optimal idea:** union-find. Every node starts as its own group, and each edge merges two groups. The number of groups left at the end is the number of components.

**Why it's correct:** two nodes end up with the same root exactly when a chain of edges connects them, because each edge merges the groups of its two ends and nothing else merges groups. So there's one root per component, and a node with no edges keeps its own root.

**Complexity:** `O(V + E log V)` time, amortized, with path compression. `O(V)` space.

**Common mistakes:** counting only the nodes that appear in edges, which misses nodes with no edges (test 2). Counting `len(set(parent))` without calling `find`: an entry in `parent` can point at a node that isn't a root any more.

</details>
