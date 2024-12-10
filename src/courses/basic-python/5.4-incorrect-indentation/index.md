---
lesson_name: Incorrect Indentation
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 328
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 329
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

### Incorrect indentation

Python uses indentation to define the structure and hierarchy of code blocks. It helps to visually represent nested blocks of code, such as if statements, loops, and function definitions.

Incorrect indentation occurs when the spacing or tabulation used for indentation is inconsistent or does not match the expected structure. Python considers indentation as part of its syntax, so errors in indentation can lead to `IndentationError` or `SyntaxError` messages.

To identify incorrect indentation errors, carefully review the indentation level of your code. Look for inconsistencies such as mixing tabs and spaces, mismatched indentation levels within the same block, or missing or excessive indentation.

For example:

```python
def is_positive_or_negative(num):
    if num > 0:
    print("The number is positive.")
    else:
        print("The number is negative.")
```

In the example above, the indentation after the first `if` is incorrect. Calling the function above will make the program fail to run with the error message below:

```python
  File "main.py", line 3
    print("The number is positive.")
    ^
IndentationError: expected an indented block after 'if' statement on line 2
```

---

### Exercise

- Fix incorrect indentation in the code so that the program runs without any errors.

#### Tests

<ul>
<li id="test-1"><code>is_positive_or_negative(1)</code> should print out the message <code>"The number is positive."</code></li>
<li id="test-2"><code>is_positive_or_negative(-1)</code> should print out the message <code>"The number is negative."</code></li>
</ul>
