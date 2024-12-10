---
lesson_name: Chain Booleans with And
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 214
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 213
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

### Chain booleans with the `and` keyword

In Python, `and` and `or` are logical operators used to chain together multiple conditions in an expression.

`and` returns `True` if **all conditions in the expression evaluate to** `True`. If any condition is `False`, the entire expression evaluates to `False`. For example:

```python
x = 5
y = 10
z = 15

result = x < y and y < z
print(result) # Output: True

result_2 = x < y and y == z
print(result_2) # Output: False
```

In the above example, the variable `result` is `True`, since both conditions were `True`: `x < y` and `y < z`. However, the variable `result_2` is `False` because one of the conditions is `False` (`y == z`)

---

### Exercise

Use `and` to set the variables' values.

#### Tests

<ul>
<li id="test-1">Variable <code>true_and_true</code> should be <code>True</code></li>
<li id="test-2">Variable <code>false</code> should be <code>False</code></li>
<li id="test-3">Use <code>and</code> keyword to set the value of variable <code>true_and_true</code></li>
<li id="test-4">Use <code>and</code> keyword to set the value of variable <code>false</code></li>
</ul>
