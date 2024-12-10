---
lesson_name: Inheritance and Except Clause
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 388
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 389
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

### Inheritance and except clause

Now we know that an error is just an object created by an error class that inherits from Python's built-in class `Exception`. When using inheritance in the `except` clause, catching a base class can also catch its subclasses, for example:

```python
class FirstError(Exception):
    pass

try:
    raise FirstError("An error message")
except Exception as e:
    print("The error is caught")
```

```bash
# Output
The error is caught
```

In the example above, the `try-except` block catches the error `FirstError`, even though it is not specified after `except`.

<div class="alert-info text-sm">
The class <code>Exception</code> also inherits from <code>BaseException</code>, but we rarely use it after <code>except</code> clause. This is because some actions, such as exiting the program or using the keyboard to stop the program causes an errors that inherits from <code>BaseException</code> class. If we were to use <code>BaseException</code> class after <code>except</code> clause, we won't be able to stop or exit the program from those actions.
</div>

---

### Exercise

- Update the function `divide_the_number` to handle multiple errors without specifying those errors explicitly.

#### Tests

<ul>
<li id="test-1"><code>divide_the_number(4, 2)</code> should return <code>2.0</code></li>
<li id="test-2"><code>divide_the_number(10, 4)</code> should return <code>2.5</code></li>
<li id="test-3"><code>divide_the_number(10, 0)</code> should print the message <code>"You cannot divide by zero!"</code></li>
<li id="test-4"><code>divide_the_number(10, "Hello")</code> should print the message <code>"You cannot divide a number with a string!"</code></li>
<li id="test-5">Must use only one <code>except</code> inside the function
<li id="test-6">Must <b>not</b> use <code>ZeroDivisionError</code> and <code>TypeError</code> directly after <code>except</code> clause
</ul>
