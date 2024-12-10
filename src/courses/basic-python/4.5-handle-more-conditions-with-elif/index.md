---
lesson_name: Handle More Conditions with Elif
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 238
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 237
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

### Handle more conditions with elif

In Python, `elif` stands for "else if". It is a conditional statement that comes after an `if` statement and before an optional `else` statement. `elif` allows you to check multiple conditions and execute different code blocks depending on the condition that is `True`.

We can add `elif` keyword after `if` keyword, like so:

```python
if condition1:
    # do something
elif condition2:
    # do something else
else:
    # do something if none of the conditions above are true
```

For example:

```python
x = 10

if x > 10:
    print("x is greater than 10")
elif x < 10:
    print("x is less than 10")
else:
    print("x is equal to 10")
```

In this example, we're checking the value of `x` using an `if` statement. If `x` is greater than 10, we print a message saying so. If it's less than `10`, we print a different message. If neither of these conditions are `True`, we move on to the else block and print a message saying that `x` is equal to 10.

Note that both `elif` and `else` are optional in an `if` statement, meaning that we can write an `if` statement without any of those keywords.

---

### Exercise

Write your code inside the `get_discount` so that:

- If the value of `total` is at least 1000, return the number `30`.
- If the value of `total` is at least 500, return the number `20`.
- For other value of `total`, return the number `10`.

#### Tests

<ul>
<li id="test-1"><code>get_discount(300)</code> should return <code>10</code></li>
<li id="test-2"><code>get_discount(500)</code> should return <code>20</code></li>
<li id="test-3"><code>get_discount(1000)</code> should return <code>30</code></li>
<li id="test-4"><code>get_discount(1500)</code> should return <code>30</code></li>
</ul>
