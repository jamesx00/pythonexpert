---
lesson_name: Plus One
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

### Plus One

A large non-negative integer is given to you as a list of its digits, `digits`, most significant digit first, with no leading zeros (other than the number `0` itself). Write a function that adds one to the number and returns the result in the same list-of-digits format, carrying as needed.

For example, `[1, 2, 9]` represents the number `129`, so adding one gives `130`, returned as `[1, 3, 0]`. If every digit is a `9`, such as `[9, 9]`, the carry pushes a new leading digit, giving `[1, 0, 0]`.

---

### Tests

<ul>
<li id="test-1"><code>plus_one([1, 2, 9])</code> should return <code>[1, 3, 0]</code></li>
<li id="test-2"><code>plus_one([9, 9])</code> should return <code>[1, 0, 0]</code></li>
<li id="test-3"><code>plus_one([1, 2, 3])</code> should return <code>[1, 2, 4]</code></li>
<li id="test-4"><code>plus_one([0])</code> should return <code>[1]</code></li>
<li id="test-5"><code>plus_one([4, 3, 2, 9])</code> should return <code>[4, 3, 3, 0]</code></li>
<li id="test-6"><code>plus_one([9])</code> should return <code>[1, 0]</code></li>
</ul>
