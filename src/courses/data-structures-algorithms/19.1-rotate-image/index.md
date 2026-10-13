---
lesson_name: Rotate Image
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n²)
  space: O(1)
hints:
  - "Where does the cell at row `r`, column `c` end up after a clockwise turn? Can you get there in two simpler moves that each only swap values?"
  - "A clockwise turn is a transpose (swap `matrix[r][c]` with `matrix[c][r]`) followed by reversing each row. See *Rotate 90° clockwise = transpose + reverse each row* in *Math & Geometry Basics*."
  - "Template: for each `r`, for each `c` in `range(r + 1, n)`, swap `matrix[r][c]` and `matrix[c][r]`. Then call `row.reverse()` on every row and return `matrix`."
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

### Rotate Image

You're given a square grid of integers, `matrix`, representing an image. Write a function that rotates the image 90 degrees clockwise and returns the rotated grid. The rotation must be done in place, overwriting `matrix` itself rather than building a brand new grid, and your function should return that same mutated `matrix` object.

For example, given
```
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
```
the top row `1, 2, 3` becomes the rightmost column read top to bottom, producing
```
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

---

### Tests

<ul>
<li id="test-1"><code>rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])</code> should return <code>[[7, 4, 1], [8, 5, 2], [9, 6, 3]]</code></li>
<li id="test-2"><code>rotate([[1, 2], [3, 4]])</code> should return <code>[[3, 1], [4, 2]]</code></li>
<li id="test-3"><code>rotate([[5]])</code> should return <code>[[5]]</code></li>
<li id="test-4"><code>rotate([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])</code> should return <code>[[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]</code></li>
<li id="test-5"><code>rotate([[1, -2], [-3, 4]])</code> should return <code>[[-3, 1], [4, -2]]</code></li>
<li id="test-6">after <code>m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]</code> and <code>rotate(m)</code>, <code>m</code> itself should be <code>[[7, 4, 1], [8, 5, 2], [9, 6, 3]]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix
```

Here `n` is the side length of the grid.

**Brute force:** build a new grid with `new[c][n - 1 - r] = matrix[r][c]`, then copy it back into `matrix`. That's `O(n²)` time too, but it needs `O(n²)` extra space, which the in-place rule is meant to avoid.

**Bottleneck:** writing a value straight to its new cell overwrites a value you haven't moved yet.

**Optimal idea:** split the turn into two moves that are each made of swaps. First transpose: swap `matrix[r][c]` with `matrix[c][r]` above the diagonal. Then reverse each row.

**Why it's correct:** the transpose sends `(r, c)` to `(c, r)`. Reversing a row sends column `j` to column `n - 1 - j`, so `(c, r)` goes to `(c, n - 1 - r)`. That's exactly where a clockwise turn sends `(r, c)`: the top row becomes the right column. Swaps never lose a value, so nothing needs a temporary grid.

**Complexity:** `O(n²)` time, each cell is swapped a constant number of times. `O(1)` extra space.

**Common mistakes:** looping `c` over the whole row in the transpose, which swaps every pair twice and undoes the work. Reversing the row order (`matrix.reverse()`) instead of each row, which turns the grid counterclockwise. Returning a new grid like `[list(row) for row in zip(*matrix[::-1])]`: it has the right values, but `matrix` itself is unchanged (test 6).

</details>
