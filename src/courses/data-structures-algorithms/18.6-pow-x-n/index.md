---
lesson_name: Pow(x, n)
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 1
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 2
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

### Pow(x, n)

Write a function that computes `x` raised to the integer power `n`, without relying on a built-in power operator or library function. `n` can be negative, in which case the result is `1 / x^|n|`, and `x` can be a float. Your solution should avoid the naive approach of multiplying `x` by itself `n` times, since `n` may be large.

For example, `my_pow(2.0, 10)` is `1024.0`, and `my_pow(2.0, -2)` is `0.25` (that's `1 / 2^2`).

---

### Tests

<ul>
<li id="test-1"><code>my_pow(2.0, 10)</code> should return <code>1024.0</code></li>
<li id="test-2"><code>my_pow(2.0, -2)</code> should return <code>0.25</code></li>
<li id="test-3"><code>my_pow(2.1, 3)</code> should return approximately <code>9.261</code></li>
<li id="test-4"><code>my_pow(5.0, 0)</code> should return <code>1.0</code></li>
<li id="test-5"><code>my_pow(1.0, 1000)</code> should return <code>1.0</code></li>
<li id="test-6"><code>my_pow(-2.0, 3)</code> should return <code>-8.0</code></li>
<li id="test-7"><code>my_pow(0.5, 4)</code> should return <code>0.0625</code></li>
</ul>
