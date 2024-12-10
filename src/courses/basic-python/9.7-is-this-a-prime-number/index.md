---
lesson_name: Is This a Prime Number
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 396
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 397
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

### Is this a prime number

Write a function that takes a number as input and determines whether it is a prime number. A prime number is a whole number greater than 1 whose only factors are 1 and itself.

Examples:

- 2 is a prime number because 2 is divisible only by 1 and 2.
- 3 is also a prime number because it is divisible only by 1 and 3.
- 4 is **not** a prime number because it is divisible by 1, 2, and 4.
- 25 is **not** a prime number because it is divisible by 1, 5, and 25.
- 100 is **not** a prime number because it is divisible by 1, 2, 4, 5, 10, 20, and 50.
- 997 is a prime number because it is divisible only by 1 and 997.

### Tests

<ul>
<li id="test-1"><code>is_prime(2)</code> should return <code>True</code></li>
<li id="test-2"><code>is_prime(17)</code> should return <code>True</code></li>
<li id="test-3"><code>is_prime(97)</code> should return <code>True</code></li>
<li id="test-4"><code>is_prime(121)</code> should return <code>False</code></li>
<li id="test-5"><code>is_prime(999)</code> should return <code>False</code></li>
<li id="test-6"><code>is_prime(10007)</code> should return <code>True</code></li>
<li id="test-7"><code>is_prime(99991)</code> should return <code>True</code></li>
<li id="test-8"><code>is_prime(100003)</code> should return <code>True</code></li>
<li id="test-9"><code>is_prime(1000000)</code> should return <code>False</code></li>
</ul>
