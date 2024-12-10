---
lesson_name: Raising an Exception
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 384
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 385
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

### Raising an exception

You can raise errors explicitly to signal exceptional situations or enforce specific conditions in your code. Raising errors is sometimes called throwing an error.

To raise an error or raise an exception in Python, use the keyword `raise`, followed by the error object. For example:

```python
raise TypeError("The value is unacceptable")
```

Here's the output when we run the code above:

```bash
### Output
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    raise TypeError("The value is unacceptable")
TypeError: The value is unacceptable
```

By raising an error instead of simply printing the error message, we can use `try-except` block to handle the errors when they occur.

---

### Exercise

- Update the function `divide_the_number` to throw errors with custom messages.

#### Tests

<ul>
<li id="test-1"><code>divide_the_number(4, 2)</code> should return <code>2.0</code></li>
<li id="test-2"><code>divide_the_number(10, 4)</code> should return <code>2.5</code></li>
<li id="test-3"><code>divide_the_number(10, 0)</code> should raise a <code>ZeroDivisionError</code> with the message <code>"You cannot divide by zero!"</code></li>
<li id="test-4"><code>divide_the_number(10, "Hello")</code> should raise a <code>TypeError</code> with the message <code>"You cannot divide a number with a string!"</code></li>
</ul>
