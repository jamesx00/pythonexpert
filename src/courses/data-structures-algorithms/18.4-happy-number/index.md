---
lesson_name: Happy Number
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

### Happy Number

Take a positive integer `n` and repeatedly replace it with the sum of the squares of its digits. Keep repeating this process. Write a function that returns `True` if this chain of replacements eventually reaches `1`, and `False` if it instead falls into a repeating cycle that never includes `1`.

For example, starting from `19`: `1^2 + 9^2 = 82`, then `8^2 + 2^2 = 68`, then `6^2 + 8^2 = 100`, then `1^2 + 0^2 + 0^2 = 1`. Since the chain reached `1`, `19` is happy. Starting from `2`, the chain cycles through `4, 16, 37, 58, 89, 145, 42, 20, 4, ...` forever without ever hitting `1`, so `2` is not happy.

---

### Tests

<ul>
<li id="test-1"><code>is_happy(19)</code> should return <code>True</code></li>
<li id="test-2"><code>is_happy(2)</code> should return <code>False</code></li>
<li id="test-3"><code>is_happy(1)</code> should return <code>True</code></li>
<li id="test-4"><code>is_happy(7)</code> should return <code>True</code></li>
<li id="test-5"><code>is_happy(4)</code> should return <code>False</code></li>
<li id="test-6"><code>is_happy(100)</code> should return <code>True</code></li>
<li id="test-7"><code>is_happy(89)</code> should return <code>False</code></li>
</ul>
