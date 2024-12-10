---
lesson_name: Accessing the Error Object
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 382
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 383
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

### Accessing the error object

When handling exceptions using `try-except` blocks in Python, it's often useful to access and work with the error object itself. The error object provides valuable information about the exception that occurred, allowing you to customize error handling, log the error, or extract specific details.

We can access the error object by using the keyword `as` after the error types in the `except` clause, like so:

```python
try:
    10 / 0
except (TypeError, ZeroDivisionError) as e:
    print(type(e)) # <class 'ZeroDivisionError'>
    print(e) # division by zero

    if type(e) == ZeroDivisionError:
        print("This error is caused by zero division")
    else:
        print("This error is caused by something else")
```

In the example above, we get the error object and assign it to the variable `e` with the code `as e`. We can choose any other name that we prefer. We can call the function `type()` to check the type of the error, which we can see that it is simply a class named `ZeroDivisionError`. We could even use `if else` statement to handle the error as well.

---

### Exercise

- Update the function `divide_the_numer` to handle multiple types of error.

#### Tests

<ul>
<li id="test-1"><code>divide_the_number(4, 2)</code> should return <code>2.0</code></li>
<li id="test-2"><code>divide_the_number(10, 4)</code> should return <code>2.5</code></li>
<li id="test-3"><code>divide_the_number(10, 0)</code> should print the message <code>"You cannot divide by zero!"</code></li>
<li id="test-4"><code>divide_the_number(10, "Hello")</code> should print the message <code>"You cannot divide a number with a string!"</code></li>
<li id="test-5">Must use only one <code>except</code> in the function</li>
</ul>
