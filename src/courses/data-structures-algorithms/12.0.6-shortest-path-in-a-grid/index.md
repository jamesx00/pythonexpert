---
lesson_name: "Warm-up: Shortest Path in a Grid (Grid BFS)"
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

### Warm-up: Shortest Path in a Grid (Grid BFS)

Write a function `grid_shortest_path(grid)` where `grid` is a list of lists containing `0` (open) and `1` (wall). Return the minimum number of **moves** to get from the top-left cell to the bottom-right cell, moving up, down, left or right through open cells only. Return `-1` if it's impossible (including when the start or end is a wall). A `1×1` open grid needs `0` moves.

For example:

```python
grid_shortest_path([[0, 0, 0],
                    [1, 1, 0],
                    [0, 0, 0]])   # -> 4
```

**Hint:** this is BFS from the previous exercise on an implicit graph. Put `(0, 0)` in the queue with distance `0`, and generate neighbours with a directions list:

```python
for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    nr, nc = r + dr, c + dc
```

---

### Tests

<ul>
<li id="test-1"><code>grid_shortest_path([[0, 0, 0], [1, 1, 0], [0, 0, 0]])</code> should return <code>4</code></li>
<li id="test-2"><code>grid_shortest_path([[0]])</code> should return <code>0</code></li>
<li id="test-3"><code>grid_shortest_path([[0, 1], [1, 0]])</code> should return <code>-1</code></li>
<li id="test-4"><code>grid_shortest_path([[1, 0], [0, 0]])</code> should return <code>-1</code></li>
<li id="test-5"><code>grid_shortest_path([[0, 0, 0, 0], [1, 1, 1, 0], [0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0]])</code> should return <code>13</code></li>
<li id="test-6"><code>grid_shortest_path([[0, 0], [0, 0]])</code> should return <code>2</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
from collections import deque

def grid_shortest_path(grid):
    rows, cols = len(grid), len(grid[0])
    if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
        return -1
    dist = {(0, 0): 0}
    queue = deque([(0, 0)])
    while queue:
        r, c = queue.popleft()
        if (r, c) == (rows - 1, cols - 1):
            return dist[(r, c)]
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols
                    and grid[nr][nc] == 0 and (nr, nc) not in dist):
                dist[(nr, nc)] = dist[(r, c)] + 1
                queue.append((nr, nc))
    return -1
```

The only differences from graph BFS are that nodes are `(row, col)` tuples and neighbours are computed rather than looked up. Tuples are hashable, so they work as dictionary keys. For problems that start from many cells at once, like *Rotting Oranges* or *Walls and Gates*, put **all** starting cells in the queue before the loop (multi-source BFS).

</details>
