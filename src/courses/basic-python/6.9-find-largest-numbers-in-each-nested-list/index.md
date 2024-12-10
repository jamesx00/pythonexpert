---
lesson_name: Find Largest Numbers in Each Nested List
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 295
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 294
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

### Find Largest Numbers in Each Nested List

Write a function that takes a nested list as input and returns a list containing the largest number from each sublist. If there is no value in a sublist, returns `None`.

For example:

Input: `[[1, 2, 3], [4, 5, 6], [7, 8, 9], []]`<br />
Output: `[3, 6, 9, None]`

---

### Tests

<ul>
<li id="test-1"><code>find_largest_numbers([[1, 2, 3], [4, 5, 6], [7, 8, 9], []])</code> should return <code>[3, 6, 9, None]</code></li>
<li id="test-2"><code>find_largest_numbers([[15, 25, 35], [45, 55, 65], [], [75, 85, 95], [105, 115, 125]])</code> should return <code>[35, 65, None, 95, 125]</code></li>
<li id="test-3"><code>find_largest_numbers([[100, 200, 300], [400, 500, 600], [700, 800, 900], [1000, 1100, 1200]])</code> should return <code>[300, 600, 900, 1200]</code></li>
<li id="test-4"><code>find_largest_numbers([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9], [-10, -11, -12]])</code> should return <code>[-1, -4, -7, -10]</code></li>
<li id="test-5"><code>find_largest_numbers([[], [], [], []])</code> should return <code>[None, None, None, None]</code></li>
</ul>
