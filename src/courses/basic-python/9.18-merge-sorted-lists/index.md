---
lesson_name: Merge Sorted Lists
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 439
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 440
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

### Merge sorted lists

Write a function that takes two sorted lists as input and merges them into a single sorted list. The function should return the merged list.

---

### Tests

<ul>
<li id="test-1"><code>merge_list([], [])</code> should return <code>[]</code></li>
<li id="test-2"><code>merge_list([1, 3, 5, 7], [2, 4, 6, 8])</code> should return <code>[1, 2, 3, 4, 5, 6, 7, 8]</code></li>
<li id="test-3"><code>merge_list([1, 2, 3], [2, 4, 4, 5])</code> should return <code>[1, 2, 2, 3, 4, 4, 5]</code></li>
<li id="test-4"><code>merge_list([2, 4, 6, 8], [1, 3, 5])</code> should return <code>[1, 2, 3, 4, 5, 6, 8]</code></li>
<li id="test-5"><code>merge_list([-2, 0, 3, 9], [-5, 1, 4, 7])</code> should return <code>[-5, -2, 0, 1, 3, 4, 7, 9]</code></li>
</ul>
