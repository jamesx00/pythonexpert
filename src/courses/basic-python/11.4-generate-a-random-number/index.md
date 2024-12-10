---
lesson_name: Generate a Random Number
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: game.py
        file_type: python
        id: 49
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: game.py
    id: 1
    name: Python
---

## Random Number Generation

We can generate random numbers in Python by calling functions in the random module.

<div class="alert-info text-sm">
A module is a group of functions, variables, or objects organized together for ease of use. We can import a module using the <b>import</b> command followed by the name of the module.
</div>

We can access each function or variable in the module by using the `.` operator followed by the name of the variable. For example, in the random module, there is a function named `randint()` used to generate random integers. The `randint()` function takes two arguments: the starting number and the ending number that we want to generate. For example, the code below generates a random number between 1 and 100:

```python
import random
print(random.randint(1, 100))
```

In addition to importing the entire module, we can also import specific functions or variables using the `from import` statement. The following code is equivalent to the previous example:

```python
from random import randint
print(randint(1, 100))
```

<div class="alert-info text-sm">
Once we have imported a module, we can use its functions or variables without importing it again.
</div>

In addition to the `randint()` function, the random module also has other functions that can be used. You can read more about the random module at <a href="https://docs.python.org/3/library/random.html" class="text-blue-600">this link</a>.
