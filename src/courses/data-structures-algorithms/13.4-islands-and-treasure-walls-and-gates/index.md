---
lesson_name: Islands and Treasure (Walls and Gates)
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(m * n)
  space: O(m * n)
hints:
  - "A BFS from each chest would work, but it walks over the same cells again and again. What if every chest started spreading at the same moment?"
  - "Use multi-source BFS from *BFS: Go Wide First* in *Graphs Basics*: put every chest in the queue before the loop. Each cell is then reached first from its nearest chest, so the first distance you write into a cell is final."
  - "Template: queue every `(r, c)` where `grid[r][c] == 0`. While the queue isn't empty, pop `(r, c)`, and for each neighbour that's in bounds and still `2147483647`, set it to `grid[r][c] + 1` and queue it. Return `grid`."
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

### Islands and Treasure (Walls and Gates)

You are given a 2D grid representing an island where each cell is one of three things: `0` marks a chest of treasure, `-1` marks an impassable rock, and `2147483647` (a stand-in for infinity) marks open ground with no treasure yet. Write a function `islands_and_treasure(grid)` that replaces every open-ground cell with the number of steps to the nearest treasure chest, moving only up/down/left/right through open ground. Cells that can never reach a chest keep the infinity value. Return the mutated grid.

For example, given

```
[[2147483647, -1, 0],
 [2147483647, 2147483647, 2147483647],
 [0, -1, 2147483647]]
```

the cell at row 0, col 0 is 2 steps from the nearest chest, so after processing it becomes `2`, and every reachable open cell is similarly replaced with its shortest distance to a chest.

---

### Tests

<ul>
<li id="test-1"><code>islands_and_treasure([[2147483647, -1, 0], [2147483647, 2147483647, 2147483647], [0, -1, 2147483647]])</code> should return <code>[[2, -1, 0], [1, 2, 1], [0, -1, 2]]</code></li>
<li id="test-2"><code>islands_and_treasure([[0]])</code> should return <code>[[0]]</code></li>
<li id="test-3"><code>islands_and_treasure([[-1]])</code> should return <code>[[-1]]</code></li>
<li id="test-4"><code>islands_and_treasure([[2147483647]])</code> should return <code>[[2147483647]]</code></li>
<li id="test-5"><code>islands_and_treasure([[0, 2147483647, 2147483647]])</code> should return <code>[[0, 1, 2]]</code></li>
<li id="test-6"><code>islands_and_treasure([[0, -1, 2147483647]])</code> should return <code>[[0, -1, 2147483647]]</code></li>
<li id="test-7"><code>islands_and_treasure([[0, 2147483647, 2147483647, 2147483647, 0]])</code> should return <code>[[0, 1, 2, 1, 0]]</code></li>
<li id="test-8">Performance: a 200x200 grid with a chest on every cell of the top row, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
from collections import deque

def islands_and_treasure(grid):
    INF = 2147483647
    rows, cols = len(grid), len(grid[0]) if grid else 0
    queue = deque((r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 0)
    while queue:
        r, c = queue.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF:
                grid[nr][nc] = grid[r][c] + 1
                queue.append((nr, nc))
    return grid
```

Here `m` and `n` are the number of rows and columns.

**Brute force:** run a separate BFS from each chest and keep the smallest distance each cell gets. With `k` chests that's `O(k * m * n)`. Test 8 has 200 chests on a 200x200 grid: about 8 million cell visits.

**Bottleneck:** every BFS walks over the same open cells again.

**Optimal idea:** one BFS that starts from all chests at once (multi-source BFS). Cells come out in order of their distance to the *nearest* chest, so the first distance a cell gets is its answer. Writing the distance into the grid also marks the cell as visited, because only cells that are still `2147483647` get updated.

**Why it's correct:** imagine one extra node joined to every chest. A BFS from that node puts all the chests at the same distance, and from there it is exactly this loop. So each open cell is first reached along a shortest path from some chest, which is a shortest path to the nearest chest. Rocks are never queued, and cells no chest can reach keep `2147483647`.

**Complexity:** `O(m * n)` time: each cell is queued at most once. `O(m * n)` extra space for the queue.

**Common mistakes:** a DFS from each chest that updates a cell whenever it finds a shorter distance: it's correct, but it can revisit the same cells many times. Overwriting chests or rocks: only update cells that are still `2147483647`. Using `list.pop(0)` as the queue, which costs `O(m * n)` per pop.

</details>
