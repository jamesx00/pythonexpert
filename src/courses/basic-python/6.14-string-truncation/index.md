---
lesson_name: String Truncation
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 305
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 304
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

### String Truncation

Write a function that truncates a given string to a specified length. Truncation means reducing the length of the string by removing characters from the end and adding an ellipsis `"..."` to indicate that the string has been shortened.

The function takes 2 arguments: the string to be truncated, and the maximum length allowed. If the string is shorter than the allowed length, no truncation is required.

---

### Tests

<ul>
<li id="test-1"><code>truncate("Hello, World!", 8)</code> should return <code>"Hello, W..."</code></li>
<li id="test-2"><code>truncate("The quick brown fox jumps over the lazy dog", 20)</code> should return <code>"The quick brown fox ..."</code></li>
<li id="test-3"><code>truncate("Lorem ipsum dolor sit amet", 25)</code> should return <code>"Lorem ipsum dolor sit ame..."</code></li>
<li id="test-4"><code>truncate("Python programming is fun", 30)</code> should return <code>"Python programming is fun"</code></li>
<li id="test-5"><code>truncate("abcdefghijklmnopqrstuvwxyz", 5)</code> should return <code>"abcde..."</code></li>
</ul>
