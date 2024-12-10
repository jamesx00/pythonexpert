---
lesson_name: Skip a Loop with Continue
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 274
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 275
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

### Skip a loop with continue

The `continue` statement skips the current item and moves on to the next item in the loop. **Unlike break, the loop will continue until all items have been processed.**

In the example below, we see that only odd numbers are printed since the print statement is skipped when the number is even.

```python
numbers = [1, 2, 3, 4, 5, 6, 7 ,8 ,9, 10]

for number in numbers:
    if number % 2 == 0:
        continue
    print(number)

print("This is called after the loop")
```

Here's the output of the example code above:

```bash
1
3
5
7
9
This is called after the loop
```

---

### Exercise

<ul>
<li id="test-1">Use <code>continue</code> inside <code>for</code> loop so that <strong>only even numbers</strong> are printed to the output.</li>
</ul>
