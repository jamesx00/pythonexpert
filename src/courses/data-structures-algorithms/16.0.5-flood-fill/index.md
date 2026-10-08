---
lesson_name: "Warm-up: Flood Fill (Grid DFS)"
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

**Hint:** remember `original = grid[r][c]`. If it already equals `color`, return right away; otherwise recolouring never makes progress and the DFS loops forever. Then write `fill(r, c)` that returns immediately if `(r, c)` is out of bounds or isn't `original`, else recolours the cell and calls itself on the 4 neighbours.

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

Recolouring a cell also marks it as visited, because it no longer equals `original`, so no separate visited set is needed. The bounds check comes first, which keeps every neighbour call safe. *Number of Islands*, *Max Area of Island* and *Surrounded Regions* all use this "check, mark, recurse into 4 neighbours" shape. The cost is `O(rows × cols)`.

</details>
