---
lesson_name: Handle An Error with Try Except
code_editor: True
code_execution: True
adding_file_allowed: False
section: Error Handling
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 374
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 375
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

### Handle an error with try except

In Python, when an error occurs during the execution of a program, it can cause the program to terminate and stop running. However, by using the `try` and `except` block, you can catch and handle these errors instead of having your program stop working.

For example, when the code below is executed, we will get the `ZeroDivisionError` from the first line of code, because you cannot divide any number by zero in Python. And the function `print()` in the second line will not be executed.

```python
10 / 0
print("The program is running")
```

```bash
# Output
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    10 / 0
ZeroDivisionError: division by zero
```

To handle the error above, we can use the `try except` block, like so:

```python
try:
    10 / 0
except:
    print("Error: Cannot divide the number by zero")
print("The program is running")
```

In the example above, we wrap the code that might cause an error within the `try` block. If an error occurs inside the `try` block, the code inside the `except` block will execute.

Here's the output of the example above. We can see that the `print()` inside the `except` block is run, and the program continues to run and execute the last `print()` function:

```bash
# Output
Error: Cannot divide the number by zero
The program is running
```

---

### Exercise

- Update the body of the function `divide_the_numer()` to handle an error.

#### Tests

<ul>
<li id="test-1"><code>divide_the_number(4, 2)</code> should return <code>2.0</code></li>
<li id="test-2"><code>divide_the_number(10, 4)</code> should return <code>2.5</code></li>
<li id="test-3"><code>divide_the_number(10, 0)</code> should print the message <code>"You cannot divide by zero!"</code></li>
<li id="test-4">Must use <code>try</code> and <code>except</code> in the function</li>
</ul>
