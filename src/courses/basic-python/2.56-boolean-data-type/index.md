---
lesson_name: Boolean Data Type
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 192
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 191
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

### Boolean data type

The boolean data type is a logic or a truth value that is important in programming in all languages, especially for controlling the program's execution. There are two types of Boolean data, `True` and `False`.

In Python, we can define a Boolean value using the words `True` or `False` (the first letter must be capitalized) because the words true or false would be considered variable names.

For example:

```python
x = True
print(x) # True
print(type(true)) # NameError: name 'true' is not defined.
```

From the example above, when we call the function `print()` with the word `true`, we get the <span class="text-red-500">NameError: name 'true' is not defined.</span>, because we did not spell `True` correctly.

---

### Exercise

<ul>
<li id="test-1">Create a new variable <code>true</code> to be <code>True</code>.</li>
<li id="test-2">Create a new variable <code>false</code> to be <code>False</code>.</li>
</ul>
