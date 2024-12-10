---
lesson_name: What is Python Module
code_editor: True
code_execution: True
adding_file_allowed: True
section: Python Modules
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 447
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 448
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

### What is Python module

In Python, a module is a file that contains Python definitions and statements. The file name is the module name with the suffix **.py**. A module can define functions, classes, and variables, and can also include runnable code. By using modules, we can organize code and make it more reusable.

### Exercise

#### Creating a module

Since modules are simply files containing Python definitions and statements that can be imported and used in other Python code, creating a module is very simple.

In this lesson, we have already created one file: **main.py**. This is our main file, which is the entrypoint to the program.

Create a new Python file with a **.py** extension in the same directory as your main Python file. Click on the `+` on top of the editor to add a new file. Let's name this file `greetings.py`.

Here's what our directory looks like after a new file is created. You can see that both files are in the same level.

```bash
.
├── greetings.py
└── main.py
```

Now, go ahead and copy the function below to the **greetings.py** file:

```python
def greet(name):
    print(f"Hello {name}!")
```

### Tests

<ul>
<li id="test-1">Create a new file named <code>greetings.py</code></li>
<li id="test-2">Create a new function named <code>greet</code> in the file <code>greetings.py</code></li>
</ul>
