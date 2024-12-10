---
lesson_name: String Ends With
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 303
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 302
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

### String Ends With

Write a function that checks whether a given string ends with another specified string. The function takes two arguments, the main string and the substring to check. The function should return a boolean value indicating whether the string ends with the specified substring.

<div class="alert-info text-sm">
We suggest that you avoid using the <code>endswith()</code> method to solve this challenge and try to solve it on your own.
</div>

---

### Tests

<ul>
<li id="test-1"><code>endswith("PythonExpert is amazing!", "amazing!")</code> should return <code>True</code></li>
<li id="test-2"><code>endswith("The quick brown fox jumps over the lazy dog.", "lazy dog.")</code> should return <code>True</code></li>
<li id="test-3"><code>endswith("Hello, World!", "world!")</code> should return <code>False</code></li>
<li id="test-4"><code>endswith("Python programming is awesome!", "awesome")</code> should return <code>False</code></li>
<li id="test-5"><code>endswith("I love coding!", "coding!")</code> should return <code>True</code></li>
</ul>
