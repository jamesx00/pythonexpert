---
lesson_name: Creating Custom Error Classes
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 386
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 387
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

### Creating custom error classes

Sometimes in your program, the build-in error classes in Python, such as `TypeError` or `ZeroDivisionError`, may not be suitable for our needs. In such cases, you can create custom error classes to represent specific types of exceptions that occur in your code. By defining custom error classes, you can provide more descriptive and meaningful error messages.

All we need to do to create our own error is create a class that inherits from the built-in `Exception` class.

```python
class MyOwnError(Exception):
    pass
```

Now that we have our own error class, we can raise the error just like any other errors.

```python
raise MyOwnError("My custom error message")

### Output
Traceback (most recent call last):
  File "main.py", line 4, in <module>
    raise MyOwnError("My custom error message")
__main__.MyOwnError: My custom error message
```

---

### Exercise

- Create your own error class named `BadFunctionCallError`.

#### Tests

<ul>
<li id="test-1"><code>BadFunctionCallError</code> should inherit from <code>Exception</code></li>
</ul>
