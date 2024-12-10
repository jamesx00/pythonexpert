---
lesson_name: Reverse a String
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 280
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 281
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

### Reverse a string

Write a Python function that takes a string as input and returns the reverse of that string.

---

### Tests

<ul>
<li id="test-1"><code>reverse_a_string("Hello")</code> should return <code>"olleH"</code></li>
<li id="test-2"><code>reverse_a_string("Python is so easy!")</code> should return <code>"!ysae os si nohtyP"</code></li>
<li id="test-3"><code>reverse_a_string("12345")</code> should return <code>"54321"</code></li>
<li id="test-4"><code>reverse_a_string("123!@#")</code> should return <code>"#@!321"</code></li>
<li id="test-5"><code>reverse_a_string("Hello World!")</code> should return <code>"!dlroW olleH"</code></li>
</ul>

### Hints

- Try looping each character in the given string and then build the result from each character.
