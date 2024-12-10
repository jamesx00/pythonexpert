---
lesson_name: Missing Parentheses
code_editor: True
code_execution: True
adding_file_allowed: False
section: Basic Debugging in Python
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 325
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 324
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

### Missing parentheses

In Python, parentheses are used to enclose arguments in function calls, define tuples, and group expressions. Forgetting to include or properly close parentheses can lead to syntax errors in your code. It's important to understand where parentheses are required and ensure they are used correctly to avoid such errors.

For example, if we run this code below in our editor:

```python
print("Hello World"
```

The output of the program will be an error type `SyntaxError`, which tells us that there is something wrong with the syntax.

```bash
# Output:
File "main.py", line 1
    print("Hello World"
         ^
SyntaxError: '(' was never closed
```

<div class="alert-info text-sm">
The error message helps pinpoint the exact location of the error by indicating the file name and line number where the error was raised. This allows you to navigate to the specific part of your code that needs attention. In the example above, you can see that the error happened on line <b>1</b> in the file <b>main.py</b>
</div>

---

### Exercise

- Fix the code by adding the necessary parentheses to resolve the syntax error.

#### Tests

<ul>
<li id="test-1">The program should run without an error</li>
<li id="test-2">The program should print the message <code>"Hello World!"</code></li>
</ul>
