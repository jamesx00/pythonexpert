---
lesson_name: Longest Increasing Path in a Matrix
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

</details>
