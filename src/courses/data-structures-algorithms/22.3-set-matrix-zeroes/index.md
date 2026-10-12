---
lesson_name: Set Matrix Zeroes
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(m * n)
  space: O(m + n)
hints:
  - "If you zero cells as soon as you find a `0`, the new zeros look just like the original ones. How can you tell them apart?"
  - "Find all the zeros first, then write. Only the row and column numbers matter, so two sets are enough. *In-place markers* in *Math & Geometry Basics* shows how to shrink even those to `O(1)` space."
  - "Template: one pass over the grid adds `r` to `zero_rows` and `c` to `zero_cols` for every `0`. A second pass sets `matrix[r][c] = 0` when `r in zero_rows or c in zero_cols`. Return `matrix`."
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

### Set Matrix Zeroes

You're given a grid of integers, `matrix`. Write a function that finds every cell containing `0`, and for each one zeroes out its entire row and entire column. The change must be made in place on `matrix`, and your function should return that same mutated `matrix`.

For example, given
```
[[1, 2, 3],
 [4, 0, 6],
 [7, 8, 9]]
```
the `0` sits at row 1, column 1, so row 1 and column 1 both get zeroed out, producing
```
[[1, 0, 3],
 [0, 0, 0],
 [7, 0, 9]]
```

---

### Tests

<ul>
<li id="test-1"><code>set_zeroes([[1, 2, 3], [4, 0, 6], [7, 8, 9]])</code> should return <code>[[1, 0, 3], [0, 0, 0], [7, 0, 9]]</code></li>
<li id="test-2"><code>set_zeroes([[0, 1], [1, 1]])</code> should return <code>[[0, 0], [0, 1]]</code></li>
<li id="test-3"><code>set_zeroes([[1, 2], [3, 4]])</code> should return <code>[[1, 2], [3, 4]]</code></li>
<li id="test-4"><code>set_zeroes([[1, 0, 3], [4, 5, 6], [0, 8, 9]])</code> should return <code>[[0, 0, 0], [0, 0, 6], [0, 0, 0]]</code></li>
<li id="test-5"><code>set_zeroes([[5]])</code> should return <code>[[5]]</code></li>
<li id="test-6"><code>set_zeroes([[0]])</code> should return <code>[[0]]</code></li>
<li id="test-7"><code>set_zeroes([[1, 2, 3, 4], [5, 0, 7, 0], [9, 10, 11, 12]])</code> should return <code>[[1, 0, 3, 0], [0, 0, 0, 0], [9, 0, 11, 0]]</code></li>
<li id="test-8">after <code>m = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]</code> and <code>set_zeroes(m)</code>, <code>m</code> itself should be <code>[[1, 0, 3], [0, 0, 0], [7, 0, 9]]</code></li>
<li id="test-9">Performance: a 600x600 grid with 40,000 zeros, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def set_zeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    zero_rows, zero_cols = set(), set()
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                zero_rows.add(r)
                zero_cols.add(c)
    for r in range(rows):
        for c in range(cols):
            if r in zero_rows or c in zero_cols:
                matrix[r][c] = 0
    return matrix
```

Here `m` and `n` are the number of rows and columns.

**Brute force:** copy the grid, then for every `0` in the copy, zero its whole row and column in `matrix`. Each `0` costs `O(m + n)`, so a grid full of zeros takes `O((m * n) * (m + n))`. Test 9 has 40,000 zeros in a 600x600 grid, about 48 million writes.

**Bottleneck:** many zeros share a row or a column, and each one zeros it again.

**Optimal idea:** a row ends up all `0` exactly when it holds at least one `0`, and the same goes for columns. So one pass records which rows and columns have a `0`, and a second pass zeros each cell whose row or column was recorded.

**Why it's correct:** the first pass only reads, so it sees the original zeros and nothing else. A cell must become `0` exactly when its row or its column had an original `0`, and that's what the second pass checks.

**Complexity:** `O(m * n)` time, two passes over the grid. `O(m + n)` extra space for the two sets. You can get to `O(1)` by storing the flags in the first row and first column themselves, plus one variable for whether the first row had a `0` (see *In-place markers* in *Math & Geometry Basics*).

**Common mistakes:** zeroing rows and columns during the first scan, so the new zeros spread and the whole grid ends up `0`. Building and returning a new grid, which leaves `matrix` unchanged (test 8).

</details>
