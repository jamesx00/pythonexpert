---
lesson_name: Truthy & Falsy
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 33
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 245
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

### Truthy & Falsy

After we have understood boolean values and how to use `if` statements, let's try to copy the code below and run it to see the output:

```python
num = 10
if num:
    print(num)
```

We will see that the `print(a)` function is executed even though the value of a is not `True`. However, if we try to run the code below, we will see that the code under the condition is not executed:

```python
num = 0
if num:
    print("Hello World")
```

In Python, every value that is not a boolean value has this property. The values that are evaluated as `True` are called **truthy**, and the values that are evaluated as `False` are called **falsy**. **In Python, almost every value is evaluated as True except for the following values**:

- `None`
- `False`

or numeric values equal to 0, such as:

- 0
- 0.0

or data structures with no values, such as:

- `[]` - list with no data
- `{}` - dictionary with no data
- `()` - tuple with no data
- `set()` - set with no data
- `""`, `''` - empty strings

We can check the truthiness or falsiness of a value by calling the `bool` function with the value you want to check:

```python
print(bool(1)) # True
print(bool("")) # False
print(bool(None)) # False
print(bool([])) # False
print(bool(0)) # False
```

We can use this property to write `if` statements to control the flow of the program as we need. For example, we can write an `if` statement to do something based on whether the variable `name` is an empty string or not:

```python
name = ""
if name:
    print(f"Hello {name}")
else:
    print("There is no name")
```

---

### Exercise

Write code for the function `is_empty_string()` to check if a string is empty.

#### Tests

<ul>
<li id="test-1"><code>is_empty_string("")</code> should return <code>True</code></li>
<li id="test-2"><code>is_empty_string("Not Empty")</code> should return <code>False</code></li>
</ul>
