---
lesson_name: Escaping Special Characters
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 134
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 135
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

### String Escaping with Special Characters

The backslash also `\` tells Python that the following character should be interpreted as a special character instead of a regular character. For example, if you want to include a newline character in a string (from pressing `Enter`), you can use the escape sequence `\n`. Or if you want to include a tab character (from pressing `Tab`), you can use the escape sequence `\t`.

For example, we can print multiple lines of text with the special character `\n`, like so:

```python
print("Hello\nworld!")
# Hello
# world!
```

And because the backslash is a special character, to use a baskslash in a string also requires escaping as well:

```python
print("C:\\Users\\John\\Documents")
# Output: C:\Users\John\Documents
```

---

### Exercise

<ul>
<li id="test-1">Fix the value of <code>file_path</code> to be <code>C:\Users\John\Documents</code></li>
</ul>
