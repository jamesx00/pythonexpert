---
lesson_name: Returning Values from Functions
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 231
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 230
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

### Returning Values from Functions

Another important feature of creating functions is the ability to return values or return the result of the function. The value returned can be assigned to a variable or used for other purposes. We can return a value using the `return` keyword followed by the value we want to return, as shown in the example below:

This function takes a year in AD as an argument and returns the corresponding year in the Buddhist era (BE) when called.

```python
def year_ac_to_be(year):
    return year + 543

year_in_ac = 2000
year_in_be = year_ac_to_be(year_in_ac)

print(year_in_be) # Output: 2543
```

The keyword `return` is not necessary for a function. When a function does not return anything, the value `None` is returned. For example:

```python
def do_something():
    print("Do this")

result = do_something()
print(result) # Output: None
```

When a function returns a value, it immediately stops executing the remaining parts of the function. For example, in the code below, the function will return `True` when called and the print function that follows will not be executed. Try copying the code to an editor and running the code to see the result.

```python
def print_hello_world():
    return True
    print("Hello World")

result = print_hello_world()
print(result)
```

```bash
Output:
True
```

---

### Exercise

Create a function that accepts arguments and returns a values.

#### Tests

<ul>
<li id="test-1">Create a function <code>add_numbers</code></li>
<li id="test-2">Function <code>add_numbers</code> should accept 2 arguments</li>
<li id="test-3"><code>add_numbers(5, 5)</code> should <code>return</code> 10</li>
<li id="test-4"><code>add_numbers(10, 10)</code> should <code>return</code> 20</li>
</ul>
