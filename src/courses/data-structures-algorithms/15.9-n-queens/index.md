---
lesson_name: N-Queens
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

### N-Queens

Write a function `n_queens(n)` that takes a board size `n` and returns **the number of distinct ways** to place `n` queens on an `n x n` chessboard so that no two queens attack each other — meaning no two queens may share a row, a column, or a diagonal. Rather than returning the actual board layouts, just return how many valid arrangements exist, as an integer.

For example, on a `4 x 4` board there are exactly 2 ways to place 4 non-attacking queens, so `n_queens(4)` should return `2`. On a `1 x 1` board a single queen trivially doesn't attack itself, so `n_queens(1)` should return `1`, while a `2 x 2` or `3 x 3` board has no valid arrangement at all.

---

### Tests

<ul>
<li id="test-1"><code>n_queens(4)</code> should return <code>2</code></li>
<li id="test-2"><code>n_queens(1)</code> should return <code>1</code></li>
<li id="test-3"><code>n_queens(2)</code> should return <code>0</code></li>
<li id="test-4"><code>n_queens(3)</code> should return <code>0</code></li>
<li id="test-5"><code>n_queens(5)</code> should return <code>10</code></li>
<li id="test-6"><code>n_queens(6)</code> should return <code>4</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def n_queens(n):
    count = 0
    cols = set()
    diag1 = set()
    diag2 = set()

    def backtrack(row):
        nonlocal count
        if row == n:
            count += 1
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            backtrack(row + 1)
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    return count
```

</details>
