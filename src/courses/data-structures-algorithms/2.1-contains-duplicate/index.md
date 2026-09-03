---
lesson_name: Contains Duplicate
code_editor: True
code_execution: True
adding_file_allowed: False
section: Arrays & Hashing
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

### Contains Duplicate

Write a function `has_duplicate(nums)` that takes a list of integers and returns `True` if any value appears more than once, or `False` if every value is unique.

For example, `has_duplicate([4, 2, 7, 2, 9])` should return `True` because `2` shows up twice, while `has_duplicate([4, 2, 7, 9])` should return `False` since all four values are distinct.

---

### Tests

<ul>
<li id="test-1"><code>has_duplicate([4, 2, 7, 2, 9])</code> should return <code>True</code></li>
<li id="test-2"><code>has_duplicate([4, 2, 7, 9])</code> should return <code>False</code></li>
<li id="test-3"><code>has_duplicate([1, 1, 1, 1])</code> should return <code>True</code></li>
<li id="test-4"><code>has_duplicate([])</code> should return <code>False</code></li>
<li id="test-5"><code>has_duplicate([5])</code> should return <code>False</code></li>
<li id="test-6"><code>has_duplicate([10, 20, 30, 40, 10])</code> should return <code>True</code></li>
</ul>
