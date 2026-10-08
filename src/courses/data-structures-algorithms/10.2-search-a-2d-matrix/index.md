---
lesson_name: Search a 2D Matrix
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(log(m·n))
  space: O(1)
hints:
  - "If you read the grid row by row, left to right, what does the sequence of numbers look like?"
  - "It's one sorted list of `rows * cols` values. Run an ordinary binary search (template 1 in *Binary Search Basics*) over positions `0` to `rows * cols - 1`."
  - "Template: position `mid` lives at row `mid // cols`, column `mid % cols`. Compare that value with `target` exactly as in *Binary Search*."
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

### Search a 2D Matrix

You're given a grid of integers, `matrix`, with the following layout: each row is sorted left to right in ascending order, and the first number in every row is larger than the last number of the row above it. Given a target value, write a function that returns `True` if the target appears anywhere in the grid, and `False` otherwise. An empty grid, or a grid whose rows are empty, should just return `False`.

Because the whole grid can be read as one long sorted sequence stitched row after row, you should be able to solve this in `O(log(rows * cols))` time rather than checking every cell.

For example, given
```
[[1, 3, 5, 7],
 [9, 11, 13, 15],
 [17, 19, 21, 23]]
```
searching for `13` returns `True`, and searching for `6` returns `False`.

---

### Tests

<ul>
<li id="test-1"><code>search_matrix([[1, 3, 5, 7], [9, 11, 13, 15], [17, 19, 21, 23]], 13)</code> should return <code>True</code></li>
<li id="test-2"><code>search_matrix([[1, 3, 5, 7], [9, 11, 13, 15], [17, 19, 21, 23]], 6)</code> should return <code>False</code></li>
<li id="test-3"><code>search_matrix([[1, 3, 5, 7], [9, 11, 13, 15], [17, 19, 21, 23]], 1)</code> should return <code>True</code></li>
<li id="test-4"><code>search_matrix([[1, 3, 5, 7], [9, 11, 13, 15], [17, 19, 21, 23]], 23)</code> should return <code>True</code></li>
<li id="test-5"><code>search_matrix([[1, 3, 5, 7], [9, 11, 13, 15], [17, 19, 21, 23]], 24)</code> should return <code>False</code></li>
<li id="test-6"><code>search_matrix([[5]], 5)</code> should return <code>True</code></li>
<li id="test-7"><code>search_matrix([], 3)</code> should return <code>False</code></li>
<li id="test-8"><code>search_matrix([[]], 3)</code> should return <code>False</code></li>
<li id="test-9">Performance: 20,000 searches in a 500 × 400 grid, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    rows, cols = len(matrix), len(matrix[0])
    lo, hi = 0, rows * cols - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        val = matrix[mid // cols][mid % cols]
        if val == target:
            return True
        elif val < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False
```

Here `m` is the number of rows and `n` the number of columns.

**Brute force:** check every cell, or `target in row` for every row. That's `O(m·n)` per search.

**Bottleneck:** the grid is fully sorted when read row by row, and a linear scan ignores that.

**Optimal idea:** treat the grid as one sorted list of `m·n` values and binary search it, converting each position to a row and column with `divmod`.

**Why it's correct:** each row is sorted, and each row starts above where the previous one ended, so reading row by row gives a sorted sequence. Position `p` in that sequence is `matrix[p // n][p % n]`. Binary search on a sorted sequence finds the target if it's there.

**Complexity:** `O(log(m·n))` time. `O(1)` extra space.

**Common mistakes:** dividing by the number of rows instead of columns when converting a position. Forgetting the empty cases `[]` and `[[]]`, where `matrix[0]` either doesn't exist or has no columns.

</details>
