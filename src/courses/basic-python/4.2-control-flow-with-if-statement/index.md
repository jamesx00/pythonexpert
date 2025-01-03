---
lesson_name: Control Flow with If Statement
section: Statements in Python
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 234
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 233
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

### If Statement

The if statement or **control flow statement** is used to control the program's operation when it meets the specified conditions. The conditions can be any expression that evaluates to a boolean value (`True` or `False`). If the condition is `True`, the code block following the if statement will be executed. If the condition is `False`, the code block will be skipped. For example, if today is Monday, set the alarm clock to ring at 6 a.m.

For example, in the following code, when we run it, the system will display `This is run`. However, if we change the value from `True` to `False`, we will see that the system does not display anything.

```python
if True:
    print("This is run")
```

Here's how to write an if statement:

```python
if condition:
    # code block to be executed when the condition is true
```

For example:

```python
def more_than_50(number):
    if number > 50:
        return True
    return False

print(more_than_50(100)) # True
print(more_than_50(10)) # False
```

This code defines a function called `more_than_50` that takes a single parameter `number`. The function first checks if the value of `number` is greater than 50 using an if statement. If `number` is greater than 50, the function returns `True`. If `number` is not greater than 50, the function returns `False`.

---

### Exercise

We have created a function `is_even` that takes a number as an argument. Write the function body so that the function returns `True` if the number is even, and returns `False` if the number is not even.

#### Tests

<ul>
<li id="test-1"><code>is_even(0)</code> should return <code>True</code></li>
<li id="test-2"><code>is_even(15)</code> should return <code>False</code></li>
<li id="test-3"><code>is_even(50)</code> should return <code>True</code></li>
</ul>

---

#### Hint

You can check if a number is even by using the `%` operator. For example, `20 % 2 == 0` will be `True`, and `21 % 2 == 0` will be `False`.
