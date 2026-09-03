---
lesson_name: Insert Interval
section: Intervals
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

### Insert Interval

Write a function `insert_interval(intervals, new_interval)` that takes a list of non-overlapping `[start, end]` intervals already sorted by start time, plus one extra `new_interval`, and returns a new list with `new_interval` merged in. Any intervals that overlap the newly inserted one should be combined into a single interval so the result stays sorted and non-overlapping.

For example, given `intervals = [[1, 3], [6, 9]]` and `new_interval = [2, 5]`, the interval `[2, 5]` overlaps `[1, 3]` but not `[6, 9]`, so the result is `[[1, 5], [6, 9]]`.

---

### Tests

<ul>
<li id="test-1"><code>insert_interval([[1, 3], [6, 9]], [2, 5])</code> should return <code>[[1, 5], [6, 9]]</code></li>
<li id="test-2"><code>insert_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])</code> should return <code>[[1, 2], [3, 10], [12, 16]]</code></li>
<li id="test-3"><code>insert_interval([], [5, 7])</code> should return <code>[[5, 7]]</code></li>
<li id="test-4"><code>insert_interval([[1, 5]], [6, 8])</code> should return <code>[[1, 5], [6, 8]]</code></li>
<li id="test-5"><code>insert_interval([[1, 5]], [2, 3])</code> should return <code>[[1, 5]]</code></li>
<li id="test-6"><code>insert_interval([[3, 5]], [0, 1])</code> should return <code>[[0, 1], [3, 5]]</code></li>
<li id="test-7"><code>insert_interval([[1, 3], [4, 6], [8, 10]], [0, 12])</code> should return <code>[[0, 12]]</code></li>
</ul>
