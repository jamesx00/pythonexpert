---
lesson_name: "Warm-up: Flood Fill (Grid DFS)"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(m * n)
  space: O(m * n)
hints:
  - "Which cells should change colour? Once a cell has the new colour, how can you tell you've already been there?"
  - "Use a grid DFS from *Representing a Graph* and *DFS: Go Deep First* in *Graphs Basics*: save `original = grid[r][c]` and return right away if it equals `color`. Then `fill(r, c)` returns if `(r, c)` is off the grid or isn't `original`, and otherwise recolours the cell and calls itself on the 4 neighbours."
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

### Warm-up: Flood Fill (Grid DFS)

A 2-D grid is a graph in disguise: each cell is a node, and its neighbours are the cells directly **up, down, left and right**.

Write a function `flood_fill(grid, r, c, color)` that works like a paint-bucket tool. Starting at cell `(r, c)`, change that cell and every cell connected to it (4-directionally) that has the **same original value** to `color`. Return the modified grid.

For example:

```python
flood_fill([[1, 1, 0],
            [1, 0, 0],
            [1, 1, 1]], 0, 0, 2)
# -> [[2, 2, 0],
#     [2, 0, 0],
#     [2, 2, 2]]
```

---

### Tests

<ul>
<li id="test-1"><code>flood_fill([[1, 1, 0], [1, 0, 0], [1, 1, 1]], 0, 0, 2)</code> should return <code>[[2, 2, 0], [2, 0, 0], [2, 2, 2]]</code></li>
<li id="test-2"><code>flood_fill([[0, 0], [0, 0]], 1, 1, 0)</code> should return <code>[[0, 0], [0, 0]]</code></li>
<li id="test-3"><code>flood_fill([[5]], 0, 0, 3)</code> should return <code>[[3]]</code></li>
<li id="test-4"><code>flood_fill([[1, 0, 1], [0, 1, 0], [1, 0, 1]], 1, 1, 7)</code> should return <code>[[1, 0, 1], [0, 7, 0], [1, 0, 1]]</code></li>
<li id="test-5"><code>flood_fill([[3, 3, 3, 4], [4, 3, 4, 4], [3, 3, 3, 3]], 2, 3, 9)</code> should return <code>[[9, 9, 9, 4], [4, 9, 4, 4], [9, 9, 9, 9]]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def flood_fill(grid, r, c, color):
    original = grid[r][c]
    if original == color:
        return grid
    rows, cols = len(grid), len(grid[0])

    def fill(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] != original:
            return
        grid[r][c] = color
        fill(r + 1, c)
        fill(r - 1, c)
        fill(r, c + 1)
        fill(r, c - 1)

    fill(r, c)
    return grid
```

Here `m` and `n` are the number of rows and columns.

**Brute force:** pass over the whole grid again and again, recolouring any `original` cell next to a recoloured one, until a pass changes nothing. Along a winding region that can take one pass per cell: `O((m * n)²)`.

**Bottleneck:** each pass rescans cells that can't change.

**Optimal idea:** DFS from `(r, c)`: recolour a cell, then visit its 4 neighbours. Recolouring also marks the cell as visited, because it no longer equals `original`, so no separate visited set is needed.

**Why it's correct:** the DFS reaches exactly the cells connected to `(r, c)` through cells equal to `original`, and it recolours each of them once. If `original == color`, recoloured cells would still look unvisited and the DFS would never stop, which is why that case returns early.

**Complexity:** `O(m * n)` time. `O(m * n)` extra space for the call stack in the worst case.

**Common mistakes:** forgetting the `original == color` check. Reading `grid[r][c]` before the bounds check, which raises `IndexError`, or wraps around with negative indexes. *Number of Islands*, *Max Area of Island* and *Surrounded Regions* all use this "check, mark, visit the 4 neighbours" shape.

</details>
