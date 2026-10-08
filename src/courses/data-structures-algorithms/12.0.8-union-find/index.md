---
lesson_name: "Warm-up: Union-Find"
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

### Warm-up: Union-Find

Union-find (also called disjoint set union) keeps track of which items belong to the same group, and can merge two groups almost instantly. Each item points to a **parent**. Following parents upward eventually reaches the group's **root**, and two items are in the same group exactly when they have the same root.

Implement a class `UnionFind` with:

- `__init__(self, n)`: items `0` to `n - 1`, each in its own group (its own parent).
- `find(self, x)`: return the root of `x`'s group.
- `union(self, a, b)`: merge the groups of `a` and `b`. Return `True` if they were in different groups, or `False` if they were already connected.
- `connected(self, a, b)`: return `True` if `a` and `b` are in the same group.

Each test creates `UnionFind(n)`, runs a list of `(operation, a, b)` steps, and checks the list of return values.

**Hint:** in `find`, while `x` isn't its own parent, move up. For speed, add **path compression**: point `x` at its grandparent as you go (`self.parent[x] = self.parent[self.parent[x]]`).

---

### Tests

<ul>
<li id="test-1"><code>UnionFind(3) then [(&#x27;union&#x27;, 0, 1), (&#x27;connected&#x27;, 0, 1), (&#x27;connected&#x27;, 0, 2)]</code> should return <code>[True, True, False]</code></li>
<li id="test-2"><code>UnionFind(3) then [(&#x27;union&#x27;, 0, 1), (&#x27;union&#x27;, 1, 2), (&#x27;connected&#x27;, 0, 2), (&#x27;union&#x27;, 0, 2)]</code> should return <code>[True, True, True, False]</code></li>
<li id="test-3"><code>UnionFind(2) then [(&#x27;connected&#x27;, 0, 1), (&#x27;union&#x27;, 1, 0), (&#x27;connected&#x27;, 1, 0)]</code> should return <code>[False, True, True]</code></li>
<li id="test-4"><code>UnionFind(6) then [(&#x27;union&#x27;, 0, 1), (&#x27;union&#x27;, 2, 3), (&#x27;union&#x27;, 4, 5), (&#x27;connected&#x27;, 1, 2), (&#x27;union&#x27;, 1, 3), (&#x27;connected&#x27;, 0, 2), (&#x27;connected&#x27;, 0, 4)]</code> should return <code>[True, True, True, False, True, True, False]</code></li>
<li id="test-5"><code>UnionFind(4) then [(&#x27;union&#x27;, 0, 0), (&#x27;union&#x27;, 3, 2), (&#x27;union&#x27;, 2, 3), (&#x27;connected&#x27;, 3, 3)]</code> should return <code>[False, True, False, True]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        self.parent[ra] = rb
        return True

    def connected(self, a, b):
        return self.find(a) == self.find(b)
```

`union` links one **root** to the other root, never just `a` to `b`, so whole groups merge at once. `union` returning `False` means the edge connects two items that were already connected: in a graph, that edge closes a **cycle**. That's the whole trick behind *Redundant Connection*, *Graph Valid Tree* and Kruskal's minimum spanning tree. With path compression, each operation is nearly `O(1)`.

</details>
