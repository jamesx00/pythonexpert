---
lesson_name: Unique Paths
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(m * n)
  space: O(m * n)
hints:
  - "The robot's last move into the bottom-right cell came from either the cell above or the cell to the left. How do the path counts for those two cells relate to the answer?"
  - "Let `dp[r][c]` be the number of paths to `(r, c)`. Every cell in the first row or first column has exactly one path, and every other cell has `dp[r][c] = dp[r - 1][c] + dp[r][c - 1]`. That's *Grid paths* in *2-D Dynamic Programming Basics*."
  - "Template: `dp = [[1] * cols for _ in range(rows)]`. For `r` from `1` to `rows - 1`, for `c` from `1` to `cols - 1`: `dp[r][c] = dp[r - 1][c] + dp[r][c - 1]`. Return `dp[rows - 1][cols - 1]`."
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

### Unique Paths

A robot sits in the top-left cell of a grid with `rows` rows and `cols` columns. It can only move one step right or one step down at a time, and it wants to reach the bottom-right cell. Write a function `count_paths(rows, cols)` that returns how many distinct paths the robot can take to get there.

For example, on a grid with 2 rows and 3 columns the robot can go right-right-down or right-down-right or down-right-right, so `count_paths(2, 3)` should return `3`.

---

### Tests

<ul>
<li id="test-1"><code>count_paths(2, 3)</code> should return <code>3</code></li>
<li id="test-2"><code>count_paths(3, 2)</code> should return <code>3</code></li>
<li id="test-3"><code>count_paths(1, 1)</code> should return <code>1</code></li>
<li id="test-4"><code>count_paths(3, 3)</code> should return <code>6</code></li>
<li id="test-5"><code>count_paths(1, 5)</code> should return <code>1</code></li>
<li id="test-6"><code>count_paths(4, 4)</code> should return <code>20</code></li>
<li id="test-7"><code>count_paths(5, 6)</code> should return <code>126</code></li>
<li id="test-8">Performance: <code>count_paths(30, 30)</code>, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def count_paths(rows, cols):
    dp = [[1] * cols for _ in range(rows)]
    for r in range(1, rows):
        for c in range(1, cols):
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
    return dp[rows - 1][cols - 1]
```

**Brute force:** count recursively: `count_paths(r, c) = count_paths(r - 1, c) + count_paths(r, c - 1)`, with `1` when either side is `1`. It's correct, but every call makes two more and nothing is saved. The number of calls is at least the answer itself, and `count_paths(30, 30)` is about `3 * 10^16`.

**Bottleneck:** the same smaller grids are counted over and over. `count_paths(r - 1, c - 1)` is reached from both of its bigger neighbours, and the repeats multiply further down.

**Optimal idea:** there are only `rows * cols` different questions. Let `dp[r][c]` be the number of paths from the start to `(r, c)`. The first row and first column are all `1`, since the robot can only go straight along them. Every other cell adds the cell above and the cell to the left.

**Why it's correct:** each path into `(r, c)` makes its last move either down from `(r - 1, c)` or right from `(r, c - 1)`. Those two groups don't overlap and together cover every path, so the count is their sum. Filling row by row makes sure both neighbours are final before they're read.

**Complexity:** `O(m * n)` time and `O(m * n)` space for `m` rows and `n` columns. One row is enough, which brings space down to `O(n)`. There's also a formula: the robot makes `rows - 1` down moves among `rows + cols - 2` moves in total, so the answer is `math.comb(rows + cols - 2, rows - 1)`.

**Common mistakes:** building the table with `[[1] * cols] * rows`, so every row is the same list. Starting the loops at `0`, which reads `dp[-1]` (the last row). Mixing up `rows` and `cols` in the loops, which goes unnoticed on square grids.

</details>
