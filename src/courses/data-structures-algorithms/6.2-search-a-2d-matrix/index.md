---
lesson_name: Search a 2D Matrix
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
</ul>
