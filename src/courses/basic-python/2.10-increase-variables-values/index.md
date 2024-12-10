---
lesson_name: Increase Variables' Values
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 107
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 106
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

## Increase the value of a variable

You can increase the value of a variable by performing some type of calculation on the variable, then reassign it back to the same variable.

For example, you can increase a value of a variable by 1 like so:

```python
x = 10
x = x + 1
print(x) # output: 11
```

In the example above, the variable `x` is created with the value `10`. The value is then incremented by 1 with the code `x + 1` and then reassigned back to the variable `x`.

However, you can also increase the value of a variable by using what's called **compound assignment operator**, which is a shorthand way of performing some action on the variable and reassigning it back to the original variable.

We can increase the value of a variable with the operator `+=` like so:

```python
x = 10
x += 1 # equivalent to x = x + 1
print(x) # output: 11
```

---

### Exercise

<ul>
<li id="test-1">Rewrite the code on line 3 to use <code>+=</code> to increase the value of <code>x</code> by <code>1</code></li>
<li id="test-2">Value of <code>x</code> should be <code>21</code>
</ul>
