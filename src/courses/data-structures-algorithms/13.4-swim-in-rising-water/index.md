---
lesson_name: Swim in Rising Water
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

### Swim in Rising Water

Write a function `swim_in_water(grid)` that takes a square grid of distinct elevations (a list of lists of integers), where you start at the top-left cell `(0, 0)` and want to reach the bottom-right cell. At time `t`, the water level is `t`, and you may move up, down, left, or right into any adjacent cell whose elevation is at most `t`, without ever stepping onto a cell above the current water level. Return the minimum time `t` at which a path exists from the top-left to the bottom-right cell.

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

</details>
