---
lesson_name: Setting Default Values for Parameters
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 229
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 228
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

### Setting default values for parameters

You can create a function with default value(s) for its parameter(s) by simply assigning the default value(s) to the parameter(s) in the function definition.

Here's an example:

```python
def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet("John") # Output: Hello, John!
greet("Alice", "Hi") # Output: Hi, Alice!
```

In this example, the `greet()` function takes two parameters: `name` and `message`. The `message` parameter has a default value of `"Hello"`. If the caller doesn't provide a value for `message`, the default value will be used.

In the first call to `greet()`, we only pass the `name` parameter, so the default value of `"Hello"` is used for the `message` parameter. In the second call, we provide both `name` and `message` parameters, so the provided value for the message is used.

<div class="alert-info text-sm">
When defining a function with default arguments, optional argument values must be specified after all the regular arguments. For example, when we define a function like the one below, the program will display an error message: <span class="text-red-500">SyntaxError: non-default argument follows default argument.</span>

```python
def print_height(unit = "cm", height):
    print(f"You are {height} {unit} tall.")
```

</div>

---

### Exercise

Create a function with default parameter

#### Tests

<ul>
<li id="test-1">Create a function <code>print_height</code></li> 
<li id="test-6">Function <code>print_height</code> should take 2 parameters:<ul>
<li id="test-2"><code>height</code> as a number</li>
<li id="test-3"><code>unit</code> with the default value <code>"cm"</code></li>
</ul>
</li>
<li id="test-4"><code>print_height(170)</code> should print <code>"You are 170 cm tall."</code></li>
<li id="test-5"><code>print_height(6, "ft")</code> should print <code>"You are 6 ft tall."</code></li>
</ul>
