---
lesson_name: Check a List for Value
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 285
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 284
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

### Check a list for value

Write a function that checks if a given value exists in a list. The function takes a list as the first argument and the value to find in the second argument.

We recommend that you do not use the `in` operator for this challenge and try to solve the problem on your own.

---

### Tests

<ul>
<li id="test-1"><code>does_list_contain([1, 2, 3], 1)</code> should return <code>True</code></li>
<li id="test-2"><code>does_list_contain([1, 2, 3], 0)</code> should return <code>False</code></li>
<li id="test-3"><code>does_list_contain(["A", "B", "C"], "A")</code> should return <code>True</code></li>
<li id="test-4"><code>does_list_contain(["A", "B", "C"], "a")</code> should return <code>False</code></li>
<li id="test-5"><code>does_list_contain(["A", "B", "C"], 0)</code> should return <code>False</code></li>
</ul>
