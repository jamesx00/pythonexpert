---
lesson_name: Find the Union of Two Lists
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 317
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 316
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

### Find the union of two lists

Write a function `find_union(list1, list2)` that takes two lists as input and returns a new list containing the union of the two input lists. The union is defined as the set of all distinct elements that appear in either of the lists.

---

### Tests

<ul>
<li id="test-1"><code>find_union([1, 2, 3, 4, 5, 6, 7], [4, 5, 6, 7, 8])</code> should return <code>[1, 2, 3, 4, 5, 6, 7, 8]</code>
<li id="test-2"><code>find_union([5, 6, 7, 8], [6, 7, 8, 9, 10, 11])</code> should return <code>[5, 6, 7, 8, 9, 10, 11]</code>
<li id="test-3"><code>find_union([1, 2, 3], [4, 5, 6])</code> should return <code>[1, 2, 3, 4, 5, 6]</code>
</ul>
