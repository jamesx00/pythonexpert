---
lesson_name: Write Comments
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 53
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 81
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: true
        source: tests.py
    id: 1
    name: Python
---

## Comments in Python

In Python, comments are used to add explanatory notes or remarks to the code, without affecting the actual execution of the program. The interpreter ignores comments while executing the program. Comments are a useful tool for documenting code, providing context, and making it easier for others to understand your code.

Python has two ways to create comments:

### Single-line comments

Single-line comments start with a hash symbol `#` and continue until the end of the line. Anything after the hash symbol on that line is ignored by the interpreter.
Example:

```python
# This is a single-line comment in Python
print("Hello World!")  # This line will print "Hello World!"
```

### Multi-line comments

Multi-line comments are created by enclosing a block of text in triple quotes `"""`, also known as `docstrings`. These can be used for documenting classes, functions, and modules.
Example:

```python
"""
This is a multi-line comment or docstring in Python.
It can span across multiple lines and can be used to
document classes, functions, and modules.
"""

def greet(name):
    """
    This function greets the person passed in as a parameter.
    """
    print("Hello, " + name + ". How are you?")
```

---

### Exercise

Write comments in Python

#### Tests

<ul>
<li id="test-1">Write a single-line comment with at least 5 characters.</li>
<li id="test-2">Write a multi-line comment with at least 5 characters.</li>
</ul>
