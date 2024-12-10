---
lesson_name: Combine For Loops with If Statements
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 252
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 251
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

### Combine for loops with if statements

`for` loops and `if` statements can be combined to perform more complex operations. A common use case is to loop through a list and perform a specific action based on a condition.

Here's an example of how to use a `for` loop with an `if` statement. Note the level of indentation for each code block:

```python
for number in range(10):
    if number > 5:
        print(number)
```

```bash
Output:
6
7
8
9
```

In the example above, we loop through numbers from 0 to 9. However, with each iteration, we check that the variable `number` is greater than 5 to call the `print()` function, which we can see from the output showing the numbers only from 6 to 9.

---

### Exercise

<ul>
<li id="test-1">Add an <code>if</code> statement within the <code>for</code> loop so that <code>my_numbers</code> only contains the numbers from 0 to 10.</li>
</ul>
