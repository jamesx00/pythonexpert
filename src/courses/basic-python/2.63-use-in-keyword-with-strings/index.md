---
lesson_name: Use in Keyword with Strings
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 205
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 206
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

### Use in keyword with strings

The `in` keyword in Python is used to check if a value exists in a sequence, such as a string, list, or dictionary. The general syntax for using `in` is:

```python
value in sequence
```

Here, **value** is the value that you want to check if it exists in the **sequence**. If the value exists in the sequence, the in operator will return `True`, otherwise, it will return `False`

The `in` keyword is used to check if a substring or character exists within a string. It returns `True` if the substring or character is found in the string, and `False` if it is not found.

For example:

```python
string = "Hello, World!"
print('H' in string) # Output: True
print('h' in string) # Output: False
print('World' in string) # Output: True
print('world' in string) # Output: False
```

---

### Exercise

- Use the `in` keyword to check if the word `"Python"` is in the variable `sentence` and set it to the variable `has_python`.
- Use the `in` keyword to check if the word `"hard"` is in the variable `sentence` and set it to the variable `has_hard`.

#### Tests

<ul>
<li id="test-1">Variable <code>has_python</code> should be <code>True</code></li>
<li id="test-2">Variable <code>has_hard</code> should be <code>False</code></li>
</ul>
