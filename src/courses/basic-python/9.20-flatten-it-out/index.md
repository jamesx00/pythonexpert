---
lesson_name: Flatten It Out
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 446
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 445
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

### Flatten it out

Write a function that takes a list as input and returns a new list with all the values flattened. The input list can contain non-list values, lists, or even nested lists. The goal is to create a single-level list containing all the values from the input list.

---

### Tests

<ul>
<li id="test-1"><code>flatten_list([5, 6, 7, 8])</code> should return <code>[5, 6, 7, 8]</code></li>
<li id="test-2"><code>flatten_list([[1], [2], [3], [4]])</code> should return <code>[1, 2, 3, 4]</code></li>
<li id="test-3"><code>flatten_list([1, [2, 3], [4, [5, 6]]])</code> should return <code>[1, 2, 3, 4, 5, 6]</code></li>
<li id="test-4"><code>flatten_list([7, [8, 9, [10]], 11])</code> should return <code>[7, 8, 9, 10, 11]</code></li>
<li id="test-5"><code>flatten_list(['a', ['b', ['c', 'd']]])</code> should return <code>['a', 'b', 'c', 'd']</code></li>
</ul>
