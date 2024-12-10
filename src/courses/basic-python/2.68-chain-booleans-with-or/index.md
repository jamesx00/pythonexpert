---
lesson_name: Chain Booleans with Or
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 215
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 216
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

### Chain booleans with the `or` keyword

The `or` keyword is different from the `and` that `or` returns `True` if **any** conditions in the expression evaluate to `True`. For the expression to be `False`, all conditions must be `False`.

For example:

```python
x = 5
y = 10
z = 15

result = x < y or y < z # True or True
print(result) # Output: True

result_2 = x < y or y == z # True or False
print(result_2) # Output: True

result_3 = x == y or y == z # False or False
print(result_3) # Output: False
```

In the above example, the variable `result` and `result_2` are both `True`, since at least one of the conditions are `True`. However, the variable `result_3` is `False` because all of the conditions are `False`.

---

### Exercise

Use the keyword `or` to set the variables' values

#### Tests

<ul>
<li id="test-1">Variable <code>true</code> should be <code>True</code></li>
<li id="test-2">Variable <code>false</code> should be <code>False</code></li>
<li id="test-3">Use the keyword <code>or</code> to set the variable <code>true</code></li>
<li id="test-4">Use the keyword <code>or</code> to set the variable <code>false</code></li>
</ul>
