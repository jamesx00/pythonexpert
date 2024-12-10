---
lesson_name: Find The Mode From a List
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 432
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 431
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

### Find the mode from a list

Write a function that takes a list and returns the mode, which is the value that appears most frequently in the list. If there are multiple modes, return a list of all the modes.

---

### Tests

<ul>
<li id="test-1"><code>find_the_mode([1, "apple", "apple", "banana", 1, None, "apple"])</code> should return <code>["apple"]</code></li>
<li id="test-2"><code>find_the_mode([1, 2, 3, "apple", "banana", 2, "banana", None])</code> should return <code>[2, 'banana']
</code></li>
<li id="test-3"><code>find_the_mode(["apple", "orange", "apple", "banana", None, None, "banana", "orange", "apple"])</code> should return <code>["apple"]</code></li>
<li id="test-4"><code>find_the_mode([None, None, None, None, None])</code> should return <code>[None]</code></li>
<li id="test-5"><code>find_the_mode([1, "1", 2, "2", 3, "3"])</code> should return <code>[1, '1', 2, '2', 3, '3']</code></li>
</ul>
