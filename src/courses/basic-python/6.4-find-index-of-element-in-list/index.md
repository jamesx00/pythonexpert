---
lesson_name: Find Index of Element in List
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 286
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 287
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

### Find index of element in list

Write a function that finds the index of a given element in a list. If the value is not found in the given list, return the value `None`.

---

### Tests

<ul>
<li id="test-1"><code>get_index([1, 2, 3], 1)</code> should return <code>0</code></li>
<li id="test-2"><code>get_index([1, 2, 3], 0)</code> should return <code>None</code></li>
<li id="test-3"><code>get_index(["A", "B", "C"], "A")</code> should return <code>0</code></li>
<li id="test-4"><code>get_index(["A", "B", "C"], "C")</code> should return <code>2</code></li>
<li id="test-5"><code>get_index(["A", "B", "C"], "a")</code> should return <code>None</code></li>
<li id="test-6"><code>get_index(["A", "B", "C"], 0)</code> should return <code>None</code></li>
</ul>

### Hints

- Use the function `enumerate` to get both the index and the value to loop through the given list.
