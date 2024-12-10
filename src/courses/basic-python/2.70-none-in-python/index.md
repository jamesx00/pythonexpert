---
lesson_name: None in Python
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 190
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 189
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

### None in Python

The value `None`, or often referred to as `null` value in many languages, is a special value in programming. It means there is no value, typically used when a function does not return anything or to initialize a variable without a value.

For example:

```python
x = None
print(type(x)) # <class 'NoneType'>

print(x == True) # False
print(x == False) # False
print(x == 0) # False
print(x == "") # False
print(x == None) # True
print(x is None) # True
```

In the example above, we created a variable `x` and set its value to `None`. Note that the `None` value starts with a capitalized **N**. Note that `None` is **not** equal to any other value, except for `None` itself.

---

### Exercise

<ul>
<li id="test-1">Create a new variable <code>name</code> and set its value to <code>None</code>.</li>
</ul>
