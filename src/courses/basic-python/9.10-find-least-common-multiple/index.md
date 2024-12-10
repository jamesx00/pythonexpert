---
lesson_name: Find Least Common Multiple
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 404
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 405
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

### Find least common multiple

Write a function that takes two integers as input and calculates the least common multiple (LCM) of all the numbers between those two integers, inclusive. The LCM is the smallest positive integer that is divisible by all the numbers in the given range.

For example, if the input is the numbers 1 and 5, the least common multiple of all numbers 1, 2, 3, 4, and 5 is 60.

---

### Tests

<ul>
<li id="test-1"><code>find_lcm([1, 5])</code> should return <code>60</code></li>
<li id="test-2"><code>find_lcm([5, 1])</code> should return <code>60</code></li>
<li id="test-3"><code>find_lcm([3, 10])</code> should return <code>2520</code></li>
<li id="test-4"><code>find_lcm([1, 1])</code> should return <code>1</code></li>
<li id="test-5"><code>find_lcm([2, 7])</code> should return <code>420</code></li>
</ul>
