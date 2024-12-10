---
lesson_name: Accept a Variable Number of Arguments with Kwargs
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 37
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 271
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

### Accept a variable number of arguments with kwargs

In the previous lesson, besides using args to receive an unlimited number of **positional arguments**, we can also receive an unlimited number of **keyword arguments** by using the `**` symbol in the same way. The values that are specified when calling the function will be stored as a dictionary.

```python
def do_something(**kwargs):
    print("keyword arguments: ", kwargs)

do_something(a="5", b="10", c="15")
```

```bash
Output:
keyword arguments:  {'a': '5', 'b': '10', 'c': '15'}
```

Furthermore, we can use args and kwargs together in the same function.

```python
def do_something(*args, **kwargs):
    print("positional arguments:", args)
    print("keywr=ord arguments:", kwargs)

do_something(1, 2, 3, a="5", b="10", c="15")
```

```bash
Output:
positional arguments: (1, 2, 3)
keyword arguments: {'a': '5', 'b': '10', 'c': '15'}
```

<div class="alert-info text-sm">
We can use variable names other than <b>args</b> and <b>kwargs</b>, and the program will work the same way. However, using args and kwargs as variable names is common practice to represent positional and named arguments, respectively, that can accept an arbitrary number of values.
</div>

---

### Exercise

Create a function named `accept_any_keyword_arguments` that can take any number of keyword arguments.

#### Tests

<ul>
<li id="test-1">Create a function named <code>accept_any_keyword_arguments</code></li>
<li id="test-2">Function <code>accept_any_keyword_arguments</code> should accept any number of keyword arguments</li>
</ul>
