---
lesson_name: Importing a Module
code_editor: True
code_execution: True
adding_file_allowed: True
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 449
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: greetings.py
        file_type: python
        id: 450
        is_closable: false
        is_edit_focus: false
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: greetings.py
      - file_name: tests.py
        file_type: python
        id: 451
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

### Importing a module

Now that we have a module (the file named `greetings.py`), we can start importing the module use whatever is inside.

To import a module, we use the `import` statement followed by the name of the module:

```python
import module_name
```

For example, to import the `greetings` module, we can use:

```python
import greetings
```

Once we have imported a module, we can access variables, functions, classes, objects, etc., in that module by using the dot notation `.` followed by the name of the thing you need. Here's an example of using the `greet()` function inside the `greetings` module:

```python
import greetings

greetings.greet("James") # Hello James!
```

---

### Exercise

Import the module `greetings` and call the `greet()` function with your name.

#### Tests

<ul>
<li id="test-1">Import the module <code>greetings</code> </li>
<li id="test-2">Call the <code>greet()</code> function with your name</li>
</ul>
