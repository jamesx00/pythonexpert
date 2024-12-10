---
lesson_name: Find Fibonacci Sequence
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 422
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 423
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

### Find fibonacci sequence

Write a function that takes a positive integer as input and returns a list of Fibonacci numbers that are less than or equal to the given number.

Fibonacci numbers are a sequence of numbers starting with 0 and 1 in which each number is the sum of the two preceding ones, e.g. `0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...`

---

### Tests

<ul>
<li id="test-1"><code>find_fibonacci(1)</code> should return <code>[0, 1, 1]</code></li>
<li id="test-2"><code>find_fibonacci(10)</code> should return <code>[0, 1, 1, 2, 3, 5, 8]</code></li>
<li id="test-3"><code>find_fibonacci(20)</code> should return <code>[0, 1, 1, 2, 3, 5, 8, 13]</code></li>
<li id="test-4"><code>find_fibonacci(100)</code> should return <code>[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]</code></li>
<li id="test-5"><code>find_fibonacci(1000)</code> should return <code>[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]</code></li>
</ul>
