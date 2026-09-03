---
lesson_name: Non-overlapping Intervals
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

### Non-overlapping Intervals

Write a function `erase_overlap_intervals(intervals)` that takes a list of `[start, end]` intervals and returns the minimum number of intervals you must remove so that none of the remaining intervals overlap each other. Intervals that only touch at an endpoint (like `[1, 2]` and `[2, 3]`) are not considered overlapping.

For example, given `intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]`, removing `[1, 3]` leaves `[1, 2], [2, 3], [3, 4]`, which don't overlap, so the answer is `1`.

---

### Tests

<ul>
<li id="test-1"><code>erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]])</code> should return <code>1</code></li>
<li id="test-2"><code>erase_overlap_intervals([[1, 2], [1, 2], [1, 2]])</code> should return <code>2</code></li>
<li id="test-3"><code>erase_overlap_intervals([[1, 2], [2, 3]])</code> should return <code>0</code></li>
<li id="test-4"><code>erase_overlap_intervals([])</code> should return <code>0</code></li>
<li id="test-5"><code>erase_overlap_intervals([[1, 100], [11, 22], [1, 11], [2, 12]])</code> should return <code>2</code></li>
<li id="test-6"><code>erase_overlap_intervals([[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]])</code> should return <code>2</code></li>
<li id="test-7"><code>erase_overlap_intervals([[-5, -2], [-3, 1], [2, 5]])</code> should return <code>1</code></li>
</ul>
