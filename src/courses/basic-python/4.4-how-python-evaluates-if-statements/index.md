---
lesson_name: How Python Evaluates If Statements
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 239
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 240
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

### How Python evaluates if statements

In Python, if-elif-else statements are evaluated in order from top to bottom. This means that the first condition that evaluates to `True` will be executed, and subsequent conditions will be ignored.

It's important to order the conditions correctly to ensure that the correct block of code is executed. If two or more conditions could be `True` for a given input, only the first matching condition will be executed.

Here's an example of incorrect ordering in Python if-elif statements:

```python
x = 5
if x < 10:
    print("x is less than 10")
elif x < 7:
    print("x is less than 7")
else:
    print("x is greater than or equal to 10")
```

In this example, the ordering of the elif statements is incorrect. The elif condition `x < 7` will never be reached, because any value of `x` that satisfies that condition will have already been caught by the previous elif condition `x < 10`. As a result, the output of this code for x = 5 will be "x is less than 10", even though `x` is less than 7.

To correct the ordering, the elif conditions should be reordered so that the most specific condition comes first:

```python
x = 5
if x < 7:
    print("x is less than 7")
elif x < 10:
    print("x is less than 10")
else:
    print("x is greater than or equal to 10")
```

---

### Exercise

- Fix the order of the if statement in the function `get_spicy_message` so that it returns the correct value.

#### Tests

<ul>
<li id="test-1"><code>get_spicy_message(3)</code> should return <code>"Not spicy"</code>.</li>
<li id="test-2"><code>get_spicy_message(4)</code> should return <code>"Little spicy"</code>.</li>
<li id="test-3"><code>get_spicy_message(5)</code> should return <code>"Very spicy"</code>.</li>
<li id="test-4"><code>get_spicy_message(6)</code> should return <code>"Very spicy"</code>.</li>
</ul>
