---
lesson_name: "Warm-up: Minimum Path Sum"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(m * n)
  space: O(m * n)
hints:
  - "A path can only enter cell `(r, c)` from above or from the left. If you knew the cheapest cost to reach both of those cells, what would the cheapest cost to reach `(r, c)` be?"
  - "Let `dp[r][c]` be the cheapest cost to reach `(r, c)`. Then `dp[r][c] = grid[r][c] + min(dp[r - 1][c], dp[r][c - 1])`. The first row and first column have only one way in, so fill them first. It's the same table as *Grid paths* in *2-D Dynamic Programming Basics*, with `min` and `+` instead of a count."
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

### Warm-up: Minimum Path Sum

Write a function `min_path_sum(grid)` that takes a grid of non-negative numbers and returns the smallest possible sum of a path from the top-left cell to the bottom-right cell, moving only **right** or **down**. The sum includes both the start and end cells.

For example:

```python
min_path_sum([[1, 3, 1],
              [1, 5, 1],
              [4, 2, 1]])   # -> 7  (1 -> 3 -> 1 -> 1 -> 1)
```

---

### Tests

<ul>
<li id="test-1"><code>min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])</code> should return <code>7</code></li>
<li id="test-2"><code>min_path_sum([[5]])</code> should return <code>5</code></li>
<li id="test-3"><code>min_path_sum([[1, 2, 3]])</code> should return <code>6</code></li>
<li id="test-4"><code>min_path_sum([[1], [2], [3]])</code> should return <code>6</code></li>
<li id="test-5"><code>min_path_sum([[1, 2, 3], [4, 5, 6]])</code> should return <code>12</code></li>
<li id="test-6"><code>min_path_sum([[0, 9, 9, 9], [0, 0, 9, 9], [9, 0, 0, 0], [9, 9, 9, 0]])</code> should return <code>0</code></li>
<li id="test-7">Performance: a 100 x 100 grid, within 1 second</li>
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

**Brute force:** recurse from the start: the cost from `(r, c)` is `grid[r][c]` plus the cheaper of going right or going down. With no memo, this follows every path separately. A `100 x 100` grid has about `10^58` paths, so it never finishes.

**Bottleneck:** many paths pass through the same cell, and the cheapest way on from that cell is the same every time. The brute force works it out again for each path.

**Optimal idea:** there are only `m * n` different questions, one per cell. Let `dp[r][c]` be the cheapest cost to reach `(r, c)` from the top-left. Fill the table row by row, so the cell above and the cell to the left are always done first.

**Why it's correct:** the last step into `(r, c)` comes from above or from the left. The path up to that cell must itself be the cheapest way there, or swapping in a cheaper one would lower the total. So taking the cheaper of the two neighbours and adding `grid[r][c]` gives the best cost. The first row can only be reached from the left, and the first column only from above.

**Complexity:** `O(m * n)` time for an `m x n` grid: each cell is filled once with constant work. `O(m * n)` space for the table. You can keep only one row, or write the costs into `grid` itself, to get `O(n)` or `O(1)` extra space.

**Common mistakes:** treating the first row and column like the rest, so they read `dp[-1][c]` (the last row in Python) or start from `0`. Forgetting to add the starting cell. Going greedy (always step to the cheaper neighbour), which can walk into an expensive area later.

</details>
