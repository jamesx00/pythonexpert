---
lesson_name: Divide a Number with Compound Division
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 112
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 113
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

## Compound division

Compound division is a shorthand way of dividing a variable by a given value and then assigning the result to the same variable. It uses the `/=` operator.

For example:

```python
x = 5
x /= 2 # equivalent to x = x / 2
print(x)  # Output: 2.5
```

---

### Exercise

<ul>
<li id="test-1">Rewrite the code on line 3 to use <code>/=</code> to divide the value of <code>x</code> and assign it back to the variable <code>x</code></li>
<li id="test-2">The value of <code>x</code> should be <code>50</code></li>
</ul>
