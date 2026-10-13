---
lesson_name: Min Cost to Connect All Points
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n²)
  space: O(n)
hints:
  - "Every point can connect to every other point. Which edge should you add next if you grow one connected group, starting from a single point?"
  - "This is a minimum spanning tree, from *Minimum Spanning Tree* in *Advanced Graphs Basics*. Use Prim: start from point `0`, and keep adding the outside point that's cheapest to connect to the group. Since every pair is an edge, keep `best[v]`, the cheapest edge from the group to `v`, in a plain list."
  - "Template: `best = [inf] * n`, `best[0] = 0`. Repeat `n` times: pick the point `u` not in the tree with the smallest `best[u]`, add it and add `best[u]` to the total, then for every `v` not in the tree, set `best[v] = min(best[v], dist(u, v))`."
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

### Min Cost to Connect All Points

Write a function `min_cost_connect_points(points)` that takes a list of `[x, y]` integer coordinates and returns the minimum total cost required to connect every point to every other point through some path, directly or indirectly. The cost of connecting two points is the Manhattan distance between them: `abs(x1 - x2) + abs(y1 - y2)`. You may connect any pair of points directly; the answer is the cost of the cheapest set of connections that leaves all points in one connected network.

For example, given points `[[0, 0], [2, 2], [3, 10]]`, connecting `[0, 0]` to `[2, 2]` costs `4`, and connecting `[2, 2]` to `[3, 10]` costs `9`, for a total of `13`, which is cheaper than any other way of linking all three points, so `min_cost_connect_points(points)` should return `13`.

---

### Tests

<ul>
<li id="test-1"><code>min_cost_connect_points([[0, 0], [2, 2], [3, 10]])</code> should return <code>13</code></li>
<li id="test-2"><code>min_cost_connect_points([[0, 0], [2, 2]])</code> should return <code>4</code></li>
<li id="test-3"><code>min_cost_connect_points([[0, 0]])</code> should return <code>0</code></li>
<li id="test-4"><code>min_cost_connect_points([[0, 0], [1, 1], [1, 0], [-1, 1]])</code> should return <code>4</code></li>
<li id="test-5"><code>min_cost_connect_points([[3, 12], [-2, 5], [-4, 1]])</code> should return <code>18</code></li>
<li id="test-6"><code>min_cost_connect_points([[0, 0], [5, 0], [10, 0], [15, 0]])</code> should return <code>15</code></li>
<li id="test-7">Performance: 500 points, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def min_cost_connect_points(points):
    n = len(points)
    in_tree = [False] * n
    # best[v]: cheapest edge from the tree to point v found so far
    best = [float("inf")] * n
    best[0] = 0
    total = 0

    for _ in range(n):
        u = -1
        for v in range(n):
            if not in_tree[v] and (u == -1 or best[v] < best[u]):
                u = v
        in_tree[u] = True
        total += best[u]
        ux, uy = points[u]
        for v in range(n):
            if not in_tree[v]:
                d = abs(ux - points[v][0]) + abs(uy - points[v][1])
                if d < best[v]:
                    best[v] = d

    return total
```

Here `n` is the number of points. Every pair of points is a possible edge, so there are about `n² / 2` edges.

**Brute force:** grow the tree one point at a time, and each time check every pair (point in the tree, point outside it) for the cheapest edge. That's `O(n²)` work per point, so `O(n³)` in total.

**Bottleneck:** after a point joins the tree, the next step checks all the same pairs again, though only the edges from the new point are new.

**Optimal idea:** remember `best[v]`, the cheapest edge from the tree to each outside point `v`. When a point `u` joins, only its own edges can improve `best`, so update it in one pass over the points. Picking the next point is another pass over `best`. A heap of edges works too, but with every pair being an edge, two passes over a list are simpler and just as fast.

**Why it's correct:** at any time, the cheapest edge leaving the tree is part of some minimum spanning tree (if a cheaper network skipped it, swapping it in for another edge that crosses the same gap would cost no more). Prim adds exactly that edge each step: `best[u]` is the cheapest edge from the tree to `u`, and `u` has the smallest `best`. After `n` steps every point is connected.

**Complexity:** `O(n²)` time: `n` steps, each with two passes over the points. `O(n)` extra space for `in_tree` and `best`. Prim with a heap is `O(n² log n)`, and Kruskal over all pairs needs `O(n²)` space for the edge list. Both also pass the performance test.

**Common mistakes:** adding up the distance from each new point to its *nearest* point, without checking that the result is connected. Updating `best` for points already in the tree. Using Euclidean distance instead of `abs(x1 - x2) + abs(y1 - y2)`.

</details>
