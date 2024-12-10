---
lesson_name: Update a Dictionary
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 406
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 407
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

### Update a dictionary

Write a function that takes two dictionaries as input and updates the first dictionary with key-value pairs from the second dictionary. If a key already exists in the first dictionary, the value should be updated with the value from the second dictionary. If a key doesn't exist in the first dictionary, it should be added.

### Note

The method `dict.update()` is not allowed for this challenge.

---

### Tests

<ul>
<li id="test-1"><code>update_dictionary({"name": "John", "age": 30}, {"age": 32, "city": "New York"})</code> should return <code>{"name": "John", "age": 32, "city": "New York"}</code></li>
<li id="test-2"><code>update_dictionary({"a": 1, "b": 2, "c": 3}, {"b": 4, "d": 5})</code> should return <code>{"a": 1, "b": 4, "c": 3, "d": 5} </code></li>
<li id="test-3"><code>update_dictionary({"x": 100, "y": 200}, {})</code> should return <code>{"x": 100, "y": 200}</code></li>
<li id="test-4"><code>update_dictionary({}, {"name": "Alice", "age": 25})</code> should return <code>{"name": "Alice", "age": 25}</code></li>
<li id="test-5"><code>update_dictionary({"a": 10, "b": 20, "c": 30}, {"b": 25, "c": 35, "d": 40})</code> should return <code>{"a": 10, "b": 25, "c": 35, "d": 40}</code></li>
<li id="test-6">Must not use <code>dict.update()</code> method</li>
</ul>
