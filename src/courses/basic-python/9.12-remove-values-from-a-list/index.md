---
lesson_name: Remove Values From a List
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 420
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 421
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

### Remove values from a list

Write a function that removes specified values from the given list. The first argument is the list, and the rest of the arguments are the values to be removed.

---

### Tests

<ul>
<li id="test-0">The function <code>remove_values()</code> should accept variable number of arguments</li>
<li id="test-1"><code>remove_values([True, False, None])</code> should return <code>[True, False, None]</code></li>
<li id="test-2"><code>remove_values([1, 2, 3, 3, 4], 3)</code> should return <code>[1, 2, 4]</code></li>
<li id="test-3"><code>remove_values([1, 1, 2, 2, 3, 4, 5, 6], 1, 2)</code> should return <code>[3, 4, 5, 6]</code></li>
<li id="test-4"><code>remove_values(["Apple", "Banana", "Cherry"], "Apple", "Banana", "Cherry")</code>  should return <code>[]</code></li>
<li id="test-5"><code>remove_values(["Hello, 123", "OpenAI GPT-3.5", 42, "Python Programming", 9876, "Data Science 101", 777, "Machine Learning", 1234, "Web Development"], [42, 9876, 777, 1234])</code> should return <code>["Hello, 123", "OpenAI GPT-3.5", "Python Programming", "Data Science 101", "Machine Learning", "Web Development"]</code></li>
</ul>
