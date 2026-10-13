---
lesson_name: "Warm-up: Union-Find"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(log n)
  space: O(n)
hints:
  - "Every item points to a parent, and following parents ends at an item that is its own parent. What do two items in the same group have in common?"
  - "Use *Union-Find* from *Graphs Basics*: `self.parent = list(range(n))`. `find` walks up to the root, pointing each item at its grandparent on the way (`self.parent[x] = self.parent[self.parent[x]]`). `union` finds both roots, returns `False` if they're the same, and otherwise links one root under the other and returns `True`."
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

### Warm-up: Union-Find

Union-find (also called disjoint set union) keeps track of which items belong to the same group, and can merge two groups almost instantly. Each item points to a **parent**. Following parents upward eventually reaches the group's **root**, and two items are in the same group exactly when they have the same root.

Implement a class `UnionFind` with:

- `__init__(self, n)`: items `0` to `n - 1`, each in its own group (its own parent).
- `find(self, x)`: return the root of `x`'s group.
- `union(self, a, b)`: merge the groups of `a` and `b`. Return `True` if they were in different groups, or `False` if they were already connected.
- `connected(self, a, b)`: return `True` if `a` and `b` are in the same group.

Each test creates `UnionFind(n)`, runs a list of `(operation, a, b)` steps, and checks the list of return values.

---

### Tests

<ul>
<li id="test-1"><code>UnionFind(3) then [(&#x27;union&#x27;, 0, 1), (&#x27;connected&#x27;, 0, 1), (&#x27;connected&#x27;, 0, 2)]</code> should return <code>[True, True, False]</code></li>
<li id="test-2"><code>UnionFind(3) then [(&#x27;union&#x27;, 0, 1), (&#x27;union&#x27;, 1, 2), (&#x27;connected&#x27;, 0, 2), (&#x27;union&#x27;, 0, 2)]</code> should return <code>[True, True, True, False]</code></li>
<li id="test-3"><code>UnionFind(2) then [(&#x27;connected&#x27;, 0, 1), (&#x27;union&#x27;, 1, 0), (&#x27;connected&#x27;, 1, 0)]</code> should return <code>[False, True, True]</code></li>
<li id="test-4"><code>UnionFind(6) then [(&#x27;union&#x27;, 0, 1), (&#x27;union&#x27;, 2, 3), (&#x27;union&#x27;, 4, 5), (&#x27;connected&#x27;, 1, 2), (&#x27;union&#x27;, 1, 3), (&#x27;connected&#x27;, 0, 2), (&#x27;connected&#x27;, 0, 4)]</code> should return <code>[True, True, True, False, True, True, False]</code></li>
<li id="test-5"><code>UnionFind(4) then [(&#x27;union&#x27;, 0, 0), (&#x27;union&#x27;, 3, 2), (&#x27;union&#x27;, 2, 3), (&#x27;connected&#x27;, 3, 3)]</code> should return <code>[False, True, False, True]</code></li>
<li id="test-6">Performance: <code>UnionFind(800)</code>, <code>union(i, i + 1)</code> for every <code>i</code> from 0 to 798, then 100,000 <code>connected(0, 799)</code> calls, within 1 second</li>
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

**Brute force:** keep parents but skip path compression. Then `find` walks the whole chain every time, and a group joined as one long chain makes each call `O(n)`. Test 6 builds an 800-item chain and calls `connected` 100,000 times. Storing a group label per item and relabelling a whole group on each `union` is `O(n)` per `union` instead.

**Bottleneck:** long parent chains that get walked again and again.

**Optimal idea:** path compression. While `find` walks up, it points each item at its grandparent, so the next walk from there is about half as long. `union` links one **root** under the other root, never just `a` to `b`, so whole groups merge at once.

**Why it's correct:** each group has exactly one root, the item that is its own parent. Compression only changes which ancestor an item points to, never which root it ends at, so `find` keeps returning the same root for every item in a group. Linking one root under the other merges the two groups and leaves one root.

**Complexity:** amortized `O(log n)` per call with path compression alone. If you also link the smaller group under the larger one (union by size), it's nearly `O(1)`. `O(n)` space.

**Common mistakes:** `self.parent[a] = b` instead of linking the roots, which cuts `a` off from the rest of its old group. Returning `True` from `union` when the two items were already connected (test 5). In a graph, `union` returning `False` means the edge closes a **cycle**: that's the trick behind *Redundant Connection*, *Graph Valid Tree* and Kruskal's minimum spanning tree.

</details>
