---
lesson_name: Longest Increasing Path in a Matrix
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: hard
target_complexity:
  time: O(m * n)
  space: O(m * n)
hints:
  - "If you knew the longest increasing path starting from each neighbour of a cell, how long is the longest one starting from the cell itself?"
  - "Let `dfs(r, c)` be the longest increasing path starting at `(r, c)`: `1 + max(dfs(neighbour))` over neighbours with a larger value, or `1` if there are none. Memoize it. Moves must strictly increase, so there are no cycles and no `visited` set is needed (see *Tips & Gotchas* in *2-D Dynamic Programming Basics*)."
  - "Template: an inner `dfs(r, c)` with `@functools.cache`. Set `best = 1`; for each of the four neighbours inside the grid with a larger value: `best = max(best, 1 + dfs(nr, nc))`. Return `best`. The answer is `max(dfs(r, c))` over every cell."
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

### Longest Increasing Path in a Matrix

Given a 2-D grid `matrix` of integers, write a function `longest_increasing_path(matrix)` that returns the length of the longest path you can trace by repeatedly stepping to a horizontally or vertically adjacent cell whose value is strictly greater than the current cell's value. You may start the path at any cell.

For example, in the grid `[[5, 1, 6], [4, 2, 7], [3, 8, 9]]`, one path is `1 -> 2 -> 7 -> 9`, four cells long, and no longer strictly-increasing path exists, so `longest_increasing_path([[5, 1, 6], [4, 2, 7], [3, 8, 9]])` should return `4`.

---

### Tests

<ul>
<li id="test-1"><code>longest_increasing_path([[5, 1, 6], [4, 2, 7], [3, 8, 9]])</code> should return <code>4</code></li>
<li id="test-2"><code>longest_increasing_path([[1]])</code> should return <code>1</code></li>
<li id="test-3"><code>longest_increasing_path([[7, 7, 7], [7, 7, 7]])</code> should return <code>1</code></li>
<li id="test-4"><code>longest_increasing_path([[1, 2, 3], [8, 9, 4], [7, 6, 5]])</code> should return <code>9</code></li>
<li id="test-5"><code>longest_increasing_path([[10, 20], [15, 25]])</code> should return <code>3</code></li>
<li id="test-6">Performance: a 100 x 100 grid where cell <code>(r, c)</code> holds <code>r + c</code>, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
from functools import lru_cache


def longest_increasing_path(matrix):
    if not matrix or not matrix[0]:
        return 0
    rows, cols = len(matrix), len(matrix[0])

    @lru_cache(maxsize=None)
    def dfs(r, c):
        best = 1
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                best = max(best, 1 + dfs(nr, nc))
        return best

    result = max(dfs(r, c) for r in range(rows) for c in range(cols))
    dfs.cache_clear()
    return result
```

**Brute force:** from every cell, run a DFS that follows every strictly increasing path and keeps the longest. It's correct, but it walks each path separately. In a grid where cell `(r, c)` holds `r + c`, every right-or-down path is increasing, and a `100 x 100` grid has about `10^58` of them.

**Bottleneck:** the longest path starting at a cell is always the same, no matter how you got there. The brute force works it out again every time a path passes through.

**Optimal idea:** let `dfs(r, c)` be the length of the longest increasing path starting at `(r, c)`, and memoize it. Each cell is solved once; later visits are a lookup. The answer is the best start over all cells.

**Why it's correct:** a path from `(r, c)` either stops there (length `1`) or steps to a larger neighbour and continues with some path from it, at best `dfs(neighbour)`. Values strictly increase along a path, so a path never comes back to a cell. That means `dfs` never calls itself on a cell that's still being computed, and the memoized answers are final.

**Complexity:** `O(m * n)` time for an `m x n` grid: each cell is computed once and looks at four neighbours. `O(m * n)` space for the memo and, in the worst case, the call stack (a snake-shaped path through every cell). A bottom-up version sorts the cells by value and fills them from the largest down.

**Common mistakes:** adding a `visited` set, which isn't needed and blocks cells another path legitimately goes through. Using `>=` instead of `>`, which allows cycles on equal values and recurses forever. Starting only from the smallest cell, or only from `(0, 0)`. Forgetting the bounds check before reading a neighbour (negative indices wrap around in Python).

</details>
