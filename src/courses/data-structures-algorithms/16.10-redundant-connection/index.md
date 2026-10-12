---
lesson_name: Redundant Connection
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n log n)
  space: O(n)
hints:
  - "Add the edges one at a time. How can you tell that a new edge joins two nodes that were already connected?"
  - "Use *Union-Find* from *Graphs Basics*: `union` the two ends of each edge in order. The first edge whose ends already share a root closes the cycle. The other cycle edges all came before it, so it's also the one that appears last."
  - "Template: `parent = {}` with every node as its own parent. `find(x)` walks up to the root. For each `[a, b]`: if `find(a) == find(b)`, return `[a, b]`; otherwise set `parent[find(a)] = find(b)`."
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

### Redundant Connection

A tree with `n` nodes labeled `1` to `n` should have exactly `n - 1` edges. You are given a list of `n` edges `[a, b]` describing a graph that started as a valid tree and then had one extra edge added, creating exactly one cycle. Write a function `find_redundant_connection(edges)` that returns the one edge that can be removed to turn the graph back into a tree. If several edges could be removed to break the cycle, return the one that appears last in the input list.

For example, given `[[1, 2], [1, 3], [2, 3]]`, the edges `[1, 2]` and `[1, 3]` already connect all three nodes into a tree, so the extra edge `[2, 3]` is the one that creates the cycle, and the function should return `[2, 3]`.

---

### Tests

<ul>
<li id="test-1"><code>find_redundant_connection([[1, 2], [1, 3], [2, 3]])</code> should return <code>[2, 3]</code></li>
<li id="test-2"><code>find_redundant_connection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]])</code> should return <code>[1, 4]</code></li>
<li id="test-3"><code>find_redundant_connection([[1, 2], [1, 3], [1, 4], [3, 4]])</code> should return <code>[3, 4]</code></li>
<li id="test-4"><code>find_redundant_connection([[1, 4], [3, 4], [1, 3], [1, 2]])</code> should return <code>[1, 3]</code></li>
<li id="test-5"><code>find_redundant_connection([[1, 2], [2, 3], [1, 3]])</code> should return <code>[1, 3]</code></li>
<li id="test-6"><code>find_redundant_connection([[3, 4], [1, 2], [2, 4], [3, 5], [2, 5]])</code> should return <code>[2, 5]</code></li>
<li id="test-7">Performance: 8,000 edges, a star around node 1 with one extra edge in the middle, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def find_redundant_connection(edges):
    parent = {}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in edges:
        parent.setdefault(a, a)
        parent.setdefault(b, b)

    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra == rb:
            return [a, b]
        parent[ra] = rb
    return []
```

Here `n` is the number of edges, which is also the number of nodes.

**Brute force:** before adding each edge, search the graph built so far (DFS or BFS) for a path between its two ends. If there is one, this edge closes the cycle. That's `O(n)` per edge and `O(n²)` in total, and test 7 has 8,000 edges. Removing one edge at a time from the end and checking whether the rest is a tree is `O(n²)` as well.

**Bottleneck:** each search walks over the same connected part of the graph again.

**Optimal idea:** union-find keeps track of which nodes are connected without walking any paths. An edge whose two ends already share a root closes a cycle.

**Why it's correct:** the graph has exactly one cycle. Going through the edges in order, every edge joins two different groups until the cycle is completed. The first edge whose ends are already connected is the one that completes it. All the other edges of the cycle come before it in the list, so it's the cycle edge that appears last, which is the one the problem asks for.

**Complexity:** `O(n log n)` time, amortized, with path compression. `O(n)` space.

**Common mistakes:** returning the first edge of the cycle instead of the last. Linking `a` to `b` directly instead of linking their roots. The labels start at `1`, so a list-based `parent` needs `n + 1` slots.

</details>
