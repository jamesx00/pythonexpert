---
lesson_name: "Warm-up: Minimum Path Sum"
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

### Warm-up: Minimum Path Sum

Write a function `min_path_sum(grid)` that takes a grid of non-negative numbers and returns the smallest possible sum of a path from the top-left cell to the bottom-right cell, moving only **right** or **down**. The sum includes both the start and end cells.

For example:

```python
min_path_sum([[1, 3, 1],
              [1, 5, 1],
              [4, 2, 1]])   # -> 7  (1 -> 3 -> 1 -> 1 -> 1)
```

**Hint:** let `dp[r][c]` be the cheapest cost to reach cell `(r, c)`. The only ways in are from above or from the left, so `dp[r][c] = grid[r][c] + min(dp[r - 1][c], dp[r][c - 1])`. The first row and first column have only one way in, so fill them first.

---

### Tests

<ul>
<li id="test-1"><code>min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])</code> should return <code>7</code></li>
<li id="test-2"><code>min_path_sum([[5]])</code> should return <code>5</code></li>
<li id="test-3"><code>min_path_sum([[1, 2, 3]])</code> should return <code>6</code></li>
<li id="test-4"><code>min_path_sum([[1], [2], [3]])</code> should return <code>6</code></li>
<li id="test-5"><code>min_path_sum([[1, 2, 3], [4, 5, 6]])</code> should return <code>12</code></li>
<li id="test-6"><code>min_path_sum([[0, 9, 9, 9], [0, 0, 9, 9], [9, 0, 0, 0], [9, 9, 9, 0]])</code> should return <code>0</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def min_path_sum(grid):
    rows, cols = len(grid), len(grid[0])
    dp = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if r == 0 and c == 0:
                dp[r][c] = grid[r][c]
            elif r == 0:
                dp[r][c] = dp[r][c - 1] + grid[r][c]
            elif c == 0:
                dp[r][c] = dp[r - 1][c] + grid[r][c]
            else:
                dp[r][c] = grid[r][c] + min(dp[r - 1][c], dp[r][c - 1])
    return dp[-1][-1]
```

Looping row by row, left to right, guarantees the cells above and to the left are filled before they're needed. The table is created with a list comprehension, because `[[0] * cols] * rows` would make every row the same list. Each row only reads the previous row, so you could shrink the space to one row of size `cols`.

</details>
