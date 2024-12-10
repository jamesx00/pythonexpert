---
lesson_name: Nested If Statements
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 244
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 243
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

### Nested if statements

In Python, it's possible to have an `if` statement inside another `if` statement. This is known as a nested `if` statement.

A nested if statement can be useful when you want to check multiple conditions before deciding what code to run. For example, you may want to check if a number is greater than 5 and less than 10. You could do this with a single if statement, but some developers prefer to use a nested if statement:

```python
x = 7
if x > 5:
    if x < 10:
        print("x is between 5 and 10")
```

In this example, the outer `if` statement checks if `x` is greater than 5. If it is, the inner `if` statement checks if `x` is less than 10. If both conditions are true, the string `"x is between 5 and 10"` is printed.

It's important to remember that each `if` statement needs to be indented properly. In the example above, the inner `if` statement is indented further, because it's inside the outer `if` statement.

---

### Exercise

Rewrite the `if` statement inside the function `get_discount()` so that the function does the following:

- If `employee` is `True` and `years` is more than 5, returns 20.
- If `employee` is `True` and `years` is less than or equal to 5, returns 10.
- if `employee` is `False`, returns 5.

### Tests

- `get_discount(employee=True, years=10)` should return `20`
  {: #test-1 }
- `get_discount(employee=True, years=5)` should return `10`
  {: #test-2 }
- `get_discount(employee=True, years=1)` should return `10`
  {: #test-3 }
- `get_discount(employee=False)` should return `10`
  {: #test-4 }
- Use nested `if` instead of using `and` keyword
  {: #test-5 }
