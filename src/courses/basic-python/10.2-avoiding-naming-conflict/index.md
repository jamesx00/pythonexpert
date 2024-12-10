---
lesson_name: Avoiding Naming Conflict
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 460
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 458
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: greetings.py
        file_type: python
        id: 459
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: false
        is_main: false
        is_test_file: false
        source: greetings.py
    id: 1
    name: Python
---

### Avoid Naming Conflict

When working with modules in Python, it's important to be mindful of potential name conflicts that can arise when importing values from different modules. Name conflicts occur when two or more imported values have the same name or when an imported value conflicts with an existing name in the current namespace.

For example:

```python
from greetings import greet

def greet():
    print("Hello from greet function")

greet() # Hello from greet function
```

In the example above, we import the function `greet()` from the module `greetings`, and also define the `greet()` function in the current namespace. When we call `greet()` the last defined function will be used. That is why importing all values with `import *` is generally not recommended: it can cause unintended naming conflicts and is difficult to debug.

There are multiple ways to avoid naming conflict from importing in Python

### Import the module instead of specific values

This also helps us identify where the values are coming from.

```python
import greetings

def greet():
    print("Hello from greet function")

greetings.greet("Dillan") # Hello Dillan!
greet() # Hello from greet function
```

### Using `as` keyword

We can alias imported values or the module name using the keyword `as`, for example:

```python
from greetings import greet as gr

def greet():
    print("Hello from greet function")

gr("Dillan") # Hello Dillan!
greet() # Hello from greet function
```

<p class="caption">Aliasing value names</p>

```python
import greetings as g

def greetings():
    print("Hello from greet function")

g.greet("Dillan") # Hello Dillan!
greetings() # Hello from greetings function
```

<p class="caption">Aliasing module names</p>

---

### Exercise

Alias the imported function to avoid naming conflict.

#### Tests

<ul>
<li id="test-1">Alias <code>greet</code> function from <code>greetings</code> module as <code>g</code></li>
<li id="test-2">Call the function <code>g("Cory")</code></li>
</ul>
