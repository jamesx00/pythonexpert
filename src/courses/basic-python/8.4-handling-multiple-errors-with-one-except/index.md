---
lesson_name: Handling Multiple Errors with One Except
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 380
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 381
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

### Handling multiple errors with a single except

Sometimes, we might prefer to handle multiple error types in a single `except` statement. We can do so by providing multiple error types in parentheses, separated by comma `,` after `except`.

For example:

```python
try:
    # Code to run
except (ZeroDivisionError, TypeError):
    # Code to run when ZeroDivisionError or TypeError was raised
```

---

### Exercise

- Update the function `divide_the_number` to handle multiple error types

#### Tests

<ul>
<li id="test-1"><code>divide_the_number(4, 2)</code> should return <code>2.0</code></li>
<li id="test-2"><code>divide_the_number(10, 4)</code> should return <code>2.5</code></li>
<li id="test-3"><code>divide_the_number(10, 0)</code> should print the message <code>"Something is wrong!"</code></li>
<li id="test-4"><code>divide_the_number(10, "Hello")</code> should print the message <code>"Something is wrong!"</code></li>
<li id="test-5">Must use only one <code>except</code> inside the function
</ul>
