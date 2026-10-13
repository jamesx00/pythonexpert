---
lesson_name: Number of Islands
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(m * n)
  space: O(m * n)
hints:
  - "When you find a land cell you haven't seen before, you've found a new island. How do you make sure the rest of that island isn't counted again?"
  - "Use the component-counting tip from *Tips & Gotchas* in *Graphs Basics*: loop over every cell, and each time you find unvisited land, count an island and run a DFS or BFS that marks every land cell connected to it. The number of traversals you start is the answer."
  - "Template: `visited = set()`, `count = 0`. For each cell `(r, c)` that is `1` and not in `visited`: add `1` to `count`, then traverse from it with a stack, adding each in-bounds, unvisited land neighbour to `visited` and to the stack. Return `count`."
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

### Number of Islands

Write a function `num_islands(grid)` that takes a 2D grid of `1`s (land) and `0`s (water) and returns the number of islands. An island is a group of `1`s connected horizontally or vertically (not diagonally), surrounded by water or the edge of the grid.

For example, given

```
[[1, 1, 0],
 [1, 0, 0],
 [0, 0, 1]]
```

the top-left `1`s form one connected island, and the lone `1` in the bottom-right corner forms a second, separate island, so the function should return `2`.

---

### Tests

<ul>
<li id="test-1"><code>num_islands([[1, 1, 0], [1, 0, 0], [0, 0, 1]])</code> should return <code>2</code></li>
<li id="test-2"><code>num_islands([[0, 0, 0], [0, 0, 0]])</code> should return <code>0</code></li>
<li id="test-3"><code>num_islands([[1, 1, 1], [1, 1, 1]])</code> should return <code>1</code></li>
<li id="test-4"><code>num_islands([[1, 0, 1, 0, 1]])</code> should return <code>3</code></li>
<li id="test-5"><code>num_islands([[1]])</code> should return <code>1</code></li>
<li id="test-6"><code>num_islands([[0]])</code> should return <code>0</code></li>
<li id="test-7"><code>num_islands([[1, 0], [0, 1], [1, 0]])</code> should return <code>3</code></li>
<li id="test-8"><code>num_islands([[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]])</code> should return <code>1</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def num_islands(grid):
    rows, cols = len(grid), len(grid[0]) if grid else 0
    visited = set()
    count = 0

    def bfs(r, c):
        queue = [(r, c)]
        visited.add((r, c))
        while queue:
            row, col = queue.pop()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, col + dc
                if (0 <= nr < rows and 0 <= nc < cols and
                        grid[nr][nc] == 1 and (nr, nc) not in visited):
                    visited.add((nr, nc))
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                bfs(r, c)
                count += 1
    return count
```

Here `m` and `n` are the number of rows and columns.

**Brute force:** give every land cell its own label, then keep passing over the grid, copying the smaller label from any land neighbour, until nothing changes. Count the different labels at the end. On a winding island a label can need one pass per cell to spread, so that's `O((m * n)²)`.

**Bottleneck:** each pass looks at every cell, though only a few labels change.

**Optimal idea:** an island is a connected component of land cells. Scan the grid, and the first time you meet an unvisited land cell, traverse its whole island and mark every cell. The island's other cells are then already marked when the scan reaches them, so each island is counted once.

**Why it's correct:** a traversal from a land cell marks exactly the land cells connected to it, which is its whole island. A new traversal only starts from an unmarked land cell, which belongs to an island not seen yet, and the scan reaches a cell of every island. So the count goes up exactly once per island.

**Complexity:** `O(m * n)` time: each cell is scanned once and pushed at most once. `O(m * n)` extra space for `visited` and the stack.

**Common mistakes:** counting diagonal neighbours as connected. Looking only at the up and left neighbours, which splits a U-shaped island in two (test 8). Marking cells when they're popped instead of when they're pushed, which can push a cell several times. A recursive DFS works too, but on a large all-land grid it can pass Python's recursion limit of about 1,000; the explicit stack here doesn't have that problem.

</details>
