---
lesson_name: Create a Function that Accepts Arguments
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 222
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 223
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

### Create a function that accepts arguments

**Arguments** are values that we specify when calling a function as its inputs. For example, we can call `print("Hello World!")`, and the message `"Hello World!"` is printed out in the output box. We can create functions that accept values by adding **parameters** in the function definition.

For example, we can create a function that takes 2 arguments, like so:

```python
def my_function(param1, param2):
    print(param1 + param2)
```

When we call the function `my_function(10, 20)`, we pass 2 number arguments. Inside the function, variable `param1` will be `10`, and variable `param2` will be `20`, then the `print()` function will be called with those 2 numbers added together.

```python
my_function(1, 1) # Output: 2
my_function(5, 5) # Output: 10
```

---

### Exercise

Create a new function called `add_them_up` that takes 2 numbers and prints the total of those 2 numbers by calling `print()`.

#### Tests

<ul>
<li id="test-1">Create a new function named <code>add_them_up</code></li>
<li id="test-2">Function <code>add_them_up</code> should accept 2 arguments</li>
<li id="test-3">Calling the function <code>add_them_up(1, 2)</code> should call <code>print(3)</code></li>
<li id="test-4">Calling the function <code>add_them_up(10, 10)</code> should call <code>print(20)</code></li>
</ul>
