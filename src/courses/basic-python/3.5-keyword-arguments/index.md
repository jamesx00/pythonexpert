---
lesson_name: Keyword Arguments
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 227
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 226
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

### Keyword arguments

Another way to call a function in Python is by using **keyword arguments**. Keyword arguments are passed to a function by specifying the parameter name followed by the value, separated by an equal sign `=`. This allows the arguments to be passed in any order, regardless of the order they were defined in the function signature.

Here is an example of using keyword arguments:

```python
def greet(name, message):
    print(f"{message}, {name}!")

greet("John", "Hello") # Output: Hello, John!
greet(message="Hello", name="John") # Output: Hello, John!
```

<p class="caption">Calling greet with positional and keyword arguments</p>

In this example, the `greet()` function takes two parameters, `name` and `message`. When calling the function with the last line of code, we pass the arguments in a different order than they were defined in the function signature, but this is okay because we use keyword arguments to specify which value corresponds to which parameter.

By using keyword arguments, we can make our code more readable and less error-prone, especially when working with functions that take a large number of arguments.

---

### Exercise

<ul>
<li id="test-1">Call the function <code>greet()</code> with keyword arguments.</li>
</ul>
