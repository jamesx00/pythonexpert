---
lesson_name: "Warm-up: Build an Adjacency List"
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

### Warm-up: Build an Adjacency List

Graph problems usually give you an **edge list** like `[[0, 1], [1, 2]]`. Before you can traverse anything, you need an **adjacency list**: for each node, the list of nodes it connects to.

Write a function `build_graph(n, edges)` for an **undirected** graph with nodes `0` to `n - 1`. Return a list of `n` lists where `graph[i]` contains every neighbour of node `i`, **in the order the edges appear** in `edges`.

For example, `build_graph(3, [[0, 1], [1, 2]])` returns `[[1], [0, 2], [1]]`.

**Hint:** start with `[[] for _ in range(n)]` (not `[[]] * n`, which makes every slot the same list). For each edge `[a, b]`, undirected means you add it **both ways**.

---

### Tests

<ul>
<li id="test-1"><code>build_graph(3, [[0, 1], [1, 2]])</code> should return <code>[[1], [0, 2], [1]]</code></li>
<li id="test-2"><code>build_graph(1, [])</code> should return <code>[[]]</code></li>
<li id="test-3"><code>build_graph(4, [[0, 1], [0, 2], [0, 3]])</code> should return <code>[[1, 2, 3], [0], [0], [0]]</code></li>
<li id="test-4"><code>build_graph(4, [[2, 3], [0, 3], [1, 2]])</code> should return <code>[[3], [2], [3, 1], [2, 0]]</code></li>
<li id="test-5"><code>build_graph(5, [[0, 1], [3, 4]])</code> should return <code>[[1], [0], [], [4], [3]]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def build_graph(n, edges):
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    return graph
```

The adjacency list costs `O(V + E)` space and makes "who are my neighbours?" an instant lookup, which is what DFS and BFS need. For a **directed** graph you'd drop the second `append`. When node labels aren't `0..n-1` (strings, for example), use `defaultdict(list)` instead of a list of lists.

</details>
