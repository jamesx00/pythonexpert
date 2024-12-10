---
lesson_name: Find Largest Number in Nested Lists
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 292
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 293
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

### Find the Largest Number in Nested Lists

Write a function that takes a nested list as input and returns the largest number from the nested list.

---

### Tests

<ul>
<li id="test-1"><code>find_largest_number([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])</code> should return <code>12</code></li>
<li id="test-2"><code>find_largest_number([[15, 25, 35], [45, 55, 65], [75, 85, 95], [105, 115, 125]])</code> should return <code>125</code></li>
<li id="test-3"><code>find_largest_number([[100, 200, 300], [400, 500, 600], [700, 800, 900], [1000, 1100, 1200]])</code> should return <code>1200</code></li>
<li id="test-4"><code>find_largest_number([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9], [-10, -11, -12]])</code> should return <code>-1</code></li>
<li id="test-5"><code>find_largest_number([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]])</code> should return <code>0</code></li>
</ul>
