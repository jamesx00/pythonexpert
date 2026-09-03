---
lesson_name: Search in Rotated Sorted Array
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

### Search in Rotated Sorted Array

You're given a list of distinct integers that was sorted in ascending order and then rotated at some unknown pivot, along with a target value. Write a function that returns the index of the target in the list, or `-1` if it isn't present. As with a plain sorted list, your solution should run in `O(log n)` time.

For example, in `[30, 40, 50, 5, 10, 20]` (the sorted list `[5, 10, 20, 30, 40, 50]` rotated by three), searching for `10` should return `4`, and searching for `100` should return `-1`.

---

### Tests

<ul>
<li id="test-1"><code>search_rotated([30, 40, 50, 5, 10, 20], 10)</code> should return <code>4</code></li>
<li id="test-2"><code>search_rotated([30, 40, 50, 5, 10, 20], 100)</code> should return <code>-1</code></li>
<li id="test-3"><code>search_rotated([4, 5, 6, 7, 0, 1, 2], 0)</code> should return <code>4</code></li>
<li id="test-4"><code>search_rotated([4, 5, 6, 7, 0, 1, 2], 3)</code> should return <code>-1</code></li>
<li id="test-5"><code>search_rotated([1], 1)</code> should return <code>0</code></li>
<li id="test-6"><code>search_rotated([1], 0)</code> should return <code>-1</code></li>
<li id="test-7"><code>search_rotated([5, 1, 3], 5)</code> should return <code>0</code></li>
<li id="test-8"><code>search_rotated([1, 2, 3, 4, 5], 5)</code> should return <code>4</code></li>
</ul>
