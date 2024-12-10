---
lesson_name: Find The Total From Range
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 399
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 398
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
    id: 1
    name: Python
---

### Find the total from a range

Write a function that takes a range given as a list of two numbers and calculates the sum of all the numbers within that range, including the start and the end of the range.

### Example

`calculate_range_sum([1, 5])` returns the number `15`. The range `[1, 5]` includes the numbers 1, 2, 3, 4, and 5. The sum of these numbers is `15`.

### Tests

<ul>
<li id="test-1"><code>calculate_range_sum([1, 5])</code> should return <code>15</code></li>
<li id="test-2"><code>calculate_range_sum([10, 0])</code> should return <code>55</code></li>
<li id="test-3"><code>calculate_range_sum([-5, -1])</code> should return <code>-15</code></li>
<li id="test-4"><code>calculate_range_sum([0, -10])</code> should return <code>-55</code></li>
<li id="test-5"><code>calculate_range_sum([105, 100])</code> should return <code>615</code></li>
</ul>
