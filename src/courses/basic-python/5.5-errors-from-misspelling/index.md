---
lesson_name: Errors from Misspelling
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 332
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 333
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

### Errors from misspelling

One of the most common issues while programming is misspelling your variable names, function names, etc. However, they are easy to spot and debug. If you misspelled something in Python, the program will raise an error `NameError` with the message `name 'something' is not defined`.

For example, when you run the code below:

```python
name = "OKAY"
print(names)
```

You will see below error message:

```bash
Traceback (most recent call last):
  File "main.py", line 2, in <module>
    print(names)
NameError: name 'names' is not defined. Did you mean: 'name'?
```

---

### Exercise

- Fix any misspelling in the given code.

#### Tests

<ul>
<li id="test-1">Variable <code>area</code> should equal to <code>50</code></li>
<li id="test-2">The program should print the message <code>The area of the square is 50</code></li>
</ul>
