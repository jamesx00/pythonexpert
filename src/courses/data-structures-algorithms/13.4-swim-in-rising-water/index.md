---
lesson_name: Swim in Rising Water
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: hard
target_complexity:
  time: O(n² log n)
  space: O(n²)
hints:
  - "A path is usable at time `t` when every cell on it is at most `t`. So what does a path \"cost\", and which path do you want?"
  - "From *Tips & Gotchas* in *Advanced Graphs Basics*: this is Dijkstra on a grid where a path's cost is the *highest* cell on it, not the sum. Always expand the lowest cell you can reach from what you've visited, and keep track of the highest cell you've popped so far."
  - "Template: `heap = [(grid[0][0], 0, 0)]`, mark `(0, 0)` visited, `result = 0`. Pop `(h, r, c)`, set `result = max(result, h)`. If `(r, c)` is the bottom-right cell, return `result`. Otherwise push each unvisited neighbour as `(grid[nr][nc], nr, nc)` and mark it visited."
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

### Swim in Rising Water

Write a function `swim_in_water(grid)` that takes a square grid of elevations (a list of lists of integers), where you start at the top-left cell `(0, 0)` and want to reach the bottom-right cell. At time `t`, the water level is `t`, and you may move up, down, left, or right into any adjacent cell whose elevation is at most `t`, without ever stepping onto a cell above the current water level. Return the minimum time `t` at which a path exists from the top-left to the bottom-right cell.

For example, given the grid `[[0, 1], [2, 3]]`, at time `0` you can only stand on the cell with elevation `0`; by time `3` the water has risen enough that every cell, including the elevation-`3` bottom-right cell, is reachable, and no smaller time works, so `swim_in_water(grid)` should return `3`.

---

### Tests

<ul>
<li id="test-1"><code>swim_in_water([[0, 1], [2, 3]])</code> should return <code>3</code></li>
<li id="test-2"><code>swim_in_water([[0, 2], [1, 3]])</code> should return <code>3</code></li>
<li id="test-3"><code>swim_in_water([[0]])</code> should return <code>0</code></li>
<li id="test-4"><code>swim_in_water([[3, 2], [0, 1]])</code> should return <code>3</code></li>
<li id="test-5"><code>swim_in_water([[0, 1, 2], [1, 2, 3], [2, 3, 4]])</code> should return <code>4</code></li>
<li id="test-6"><code>swim_in_water([[0, 4, 2], [1, 3, 5], [6, 7, 8]])</code> should return <code>8</code></li>
<li id="test-7"><code>swim_in_water([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]])</code> should return <code>16</code></li>
<li id="test-8">Performance: a 100x100 grid holding 0 to 9,999 in a scrambled order, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
import heapq


def swim_in_water(grid):
    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    min_heap = [(grid[0][0], 0, 0)]
    visited[0][0] = True
    result = 0

    while min_heap:
        t, r, c = heapq.heappop(min_heap)
        result = max(result, t)
        if r == n - 1 and c == n - 1:
            return result
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                visited[nr][nc] = True
                heapq.heappush(min_heap, (grid[nr][nc], nr, nc))

    return result
```

Here the grid is `n` by `n`, so it has `n²` cells.

**Brute force:** try `t = grid[0][0]`, then `t + 1`, and so on, and each time BFS from the top-left over cells at most `t`. Stop at the first `t` where the BFS reaches the bottom-right. That's up to `n²` values of `t`, each with an `O(n²)` BFS, so `O(n⁴)`.

**Bottleneck:** each BFS starts over from scratch, though raising `t` by one only opens up the cells of height `t + 1`.

**Optimal idea:** grow the reachable area one cell at a time, always taking the *lowest* cell on its edge. A min-heap gives you that cell. The answer is the highest cell you had to take before the bottom-right cell came out of the heap. Binary search on `t` with a BFS each time also works, in `O(n² log n)`.

**Why it's correct:** this is Dijkstra where a path costs its highest cell. Taking a higher cell never makes a path cheaper, so the same argument holds: when a cell comes out of the heap, no route to it has a lower highest cell. `result` is the highest cell popped so far, and every cell popped before the target was needed, because at that moment it was the lowest way to grow the area.

**Complexity:** `O(n² log n)` time: each cell is pushed and popped once, and the heap holds at most `n²` entries. `O(n²)` extra space for `visited` and the heap.

**Common mistakes:** returning the height of the last cell popped instead of the highest one so far. Adding up the heights as in normal Dijkstra. Forgetting the start cell's own height: you can't leave it before `t = grid[0][0]`, as in test 4.

</details>
