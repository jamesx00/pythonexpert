---
lesson_name: Decrease Variables' Values
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 108
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 109
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

## Decrease the value of a variable

Compound subtraction is a shorthand way of subtracting a value from a variable and then assigning the result back to the variable. It is achieved by using the `-=` operator.

For example:

```python
x = 20
x -= 1 # equivalent to x = x - 1
print(x) # output: 19
```

---

### Exercise

<ul>
<li id="test-1">Rewrite the code on line 3 to use <code>-=</code> to increase the value of <code>x</code> by <code>1</code></li>
<li id="test-2">Value of <code>x</code> should be <code>19</code>
</ul>
