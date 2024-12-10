---
lesson_name: Handle Specific Error
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 377
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 376
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

### Handle specific error

Using `except` the way we did in the previous lesson would catch all error types that occurred inside the `try` block, which is generally considered a bad practice. Instead of using a broad `except` statement, it is generally recommended to catch and handle specific exceptions that you expect may occur in your code.

The error type is usually at the bottom of the error message. For example, in the output below, we can see that the error type when we divide by zero is `ZeroDivisionError`.

```bash
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    10 / 0
ZeroDivisionError: division by zero # <-- The error type
```

We can catch a specific type of error with `except` by using the following syntax:

```python
try:
    # code to run
except error_type:
    # code to run of the error occurs.
```

For example, we can catch `ZeroDivisionError` the same way we did in our previous lesson with the code below:

```python
try:
    10 / 0
except ZeroDivisionError: <-- Specify the error type to catch
    print("Error: Cannot divide the number by zero")
print("The program is running")

# Output
Error: Cannot divide the number by zero
The program is running
```

If the error occurred due to another reason, such as dividing a number with a string, the program will stop running and raises another error. In that case, the error raised is the `TypeError` instead of `ZeroDivisionError`:

```python
try:
    10 / "OKAY"
except ZeroDivisionError:
    print("Error: Cannot divide the number by zero")
print("The program is running")

# Output
Traceback (most recent call last):
  File "main.py", line 2, in <module>
    10 / "OKAY"
TypeError: unsupported operand type(s) for /: 'int' and 'str'
```

---

### Exercise

- Update the `divide_the_number` function to handle only `ZeroDivisionError`.

#### Tests

<ul>
<li id="test-1"><code>divide_the_number(4, 2)</code> should return <code>2.0</code></li>
<li id="test-2"><code>divide_the_number(10, 4)</code> should return <code>2.5</code></li>
<li id="test-3"><code>divide_the_number(10, 0)</code> should print the message <code>"You cannot divide by zero!"</code></li>
<li id="test-4"><code>divide_the_number(10, "Hello")</code> should cause an error <code>TypeError</code> and <strong>not</strong> print the message <code>"You cannot divide by zero!"</code></li>
</ul>
