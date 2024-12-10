---
lesson_name: Assign a Variable to another Variable
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 85
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 84
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

## Assigning a Variable with another Variable

In Python, we can assign the value of one variable to another variable using the assignment operator `=`. The value on the right side of the operator is assigned to the variable on the left side. For example, if we have a variable `x` with the value 10, we can assign it to another variable `y` like this:

```python
x = 10
y = x
```

Now the value of `y` is also 10. We can also reassign the value of `x` later, and it will not affect the value of `y` since it was only assigned the value of `x` at the time of assignment.

---

### Exercise

<ul>
<li id="test-1">Create a new variable <code>x</code> and assign the number <code>10</code> to it.</li>
<li id="test-2">Create another variable <code>y</code> and assign the variable <code>x</code> to it.</li>
</ul>
