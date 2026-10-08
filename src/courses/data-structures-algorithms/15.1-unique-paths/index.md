---
lesson_name: Unique Paths
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

</details>
