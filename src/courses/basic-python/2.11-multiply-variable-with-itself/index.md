---
lesson_name: Multiply Variable with Itself
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 111
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 110
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

## Compound multiplication

Compound multiplication is a shorthand way of multiplying a variable by a given value and then assigning the result to the same variable. It uses the `*=` operator.

For example:

```python
x = 5
x *= 2 # equivalent to x = x * 2
print(x)  # Output: 10
```

---

### Exercise

<ul>
<li id="test-1">Rewrite the code on line 3 to use <code>*=</code> to multiply the value of <code>x</code> and assign it back to the variable <code>x</code></li>
<li id="test-2">Value of <code>x</code> should be <code>100</code></li>
</ul>
