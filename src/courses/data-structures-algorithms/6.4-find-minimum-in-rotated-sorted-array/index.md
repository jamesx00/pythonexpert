---
lesson_name: Find Minimum in Rotated Sorted Array
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

### Find Minimum in Rotated Sorted Array

You're given a list of distinct integers that was originally sorted in ascending order, then rotated some unknown number of positions (possibly zero) — meaning a prefix of the sorted list was moved to the end. Write a function that returns the smallest value in the list. Solve it in `O(log n)` time rather than scanning every element.

For example, `[11, 15, 19, 2, 5, 8]` is `[2, 5, 8, 11, 15, 19]` rotated by three positions, so the minimum is `2`. A list that hasn't been rotated at all, like `[1, 2, 3, 4]`, should just return its first element, `1`.

---

### Tests

<ul>
<li id="test-1"><code>find_min([11, 15, 19, 2, 5, 8])</code> should return <code>2</code></li>
<li id="test-2"><code>find_min([1, 2, 3, 4])</code> should return <code>1</code></li>
<li id="test-3"><code>find_min([4, 1, 2, 3])</code> should return <code>1</code></li>
<li id="test-4"><code>find_min([3, 4, 1, 2])</code> should return <code>1</code></li>
<li id="test-5"><code>find_min([2, 3, 4, 1])</code> should return <code>1</code></li>
<li id="test-6"><code>find_min([9])</code> should return <code>9</code></li>
<li id="test-7"><code>find_min([2, 1])</code> should return <code>1</code></li>
</ul>
