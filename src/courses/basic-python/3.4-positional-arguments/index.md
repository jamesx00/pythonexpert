---
lesson_name: Positional Arguments
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 225
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 224
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

### Positional arguments

A positional argument is a parameter that is passed to a function based on its position in the function call. When calling a function with positional arguments, the arguments must be passed in the same order as the parameters are defined in the function definition.

Here's an example:

```python
def greet(name, message):
    print(f"{message}, {name}!")

greet("John", "Hello") # Output: Hello, John!
```

In the above example, the `greet()` function has two positional parameters, `name` and `message`. When we call the function on the last line, we pass `"John"` as the first argument, which is assigned to the `name` parameter, and `"Hello"` as the second argument, which is assigned to the `message` parameter. The function then prints out the message `Hello, John!`.

---

### Exercise

<ul>
<li id="test-1">Call the function <code>greet()</code> with positional arguments.</li>
</ul>
