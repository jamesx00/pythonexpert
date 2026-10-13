---
lesson_name: Clone Graph
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(V + E)
  space: O(V + E)
hints:
  - "Copying a node means making a new list of its neighbours. If you follow the neighbours and copy every node you reach, what goes wrong on a graph with a cycle?"
  - "Use DFS with a visited record, from *DFS: Go Deep First* in *Graphs Basics*. Here the record is a dictionary `clones` from each node to its new list: create the clone before visiting the neighbours, and skip nodes that already have one. Start from every node, since the graph may not be connected."
  - "Template: `clones = {}`. `dfs(node)`: if `node in clones`, return; set `clones[node] = []`; for each neighbour, append it to `clones[node]` and call `dfs(neighbor)`. Call `dfs` on every node, then return `[clones[i] for i in range(len(adj_list))]`."
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
<li id="test-7"><code>clone_graph([[1], [0], [3], [2]])</code> should return <code>[[1], [0], [3], [2]]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def clone_graph(adj_list):
    clones = {}

    def dfs(node):
        if node in clones:
            return
        clones[node] = []
        for neighbor in adj_list[node]:
            clones[node].append(neighbor)
            dfs(neighbor)

    for node in range(len(adj_list)):
        dfs(node)
    return [clones[node] for node in range(len(adj_list))]
```

Here `V` is the number of nodes and `E` the number of edges.

**Brute force:** a DFS that makes a copy every time it reaches a node, without remembering which nodes it has already copied. On any cycle, like the triangle in test 1, it never stops: `0` leads to `1`, `1` leads back to `0`, and so on.

**Bottleneck:** the traversal can't tell a new node from one it has already copied.

**Optimal idea:** keep a `clones` dictionary from each node to its new list. Create the clone before visiting the neighbours, and return straight away for a node that's already in `clones`. Start a DFS from every node, so parts of the graph that aren't connected to node `0` get copied too.

**Why it's correct:** each node gets exactly one new list, created the first time the DFS reaches it, with the same neighbours in the same order. The entry goes into `clones` before the neighbours are visited, so a cycle that leads back to the node stops right there. The loop over all nodes means no node is missed.

**Complexity:** `O(V + E)` time and space.

**Common mistakes:** `adj_list[:]` or `list(adj_list)`: a new outer list that holds the *same* inner lists, so changing the copy changes the original. Starting only from node `0`, which misses the other parts of a graph that isn't connected (test 7). Since nodes here are just numbers, `[list(neighbors) for neighbors in adj_list]` is also correct. The `clones` dictionary matters in the classic version of this problem, where each node is an object that points at other node objects.

</details>
