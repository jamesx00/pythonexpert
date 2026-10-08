---
lesson_name: Valid Parenthesis String
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

### Valid Parenthesis String

You're given a string `s` made up only of the characters `(`, `)`, and `*`, where each `*` can be treated as either `(`, `)`, or an empty string. Write a function `check_valid_string(s)` that returns `True` if there's some way to interpret every `*` so the resulting string of parentheses is balanced (every opening bracket has a matching closing bracket, in the correct order), and `False` otherwise.

For example, `s = "(*))"` is valid because treating the `*` as `(` turns it into the balanced `(())`. But `s = "(((*"` is not valid: even treating the `*` as `(` still leaves three opening brackets with nothing to close them.

---

### Tests

<ul>
<li id="test-1"><code>check_valid_string("()")</code> should return <code>True</code></li>
<li id="test-2"><code>check_valid_string("(*)")</code> should return <code>True</code></li>
<li id="test-3"><code>check_valid_string("(*))")</code> should return <code>True</code></li>
<li id="test-4"><code>check_valid_string("(((*")</code> should return <code>False</code></li>
<li id="test-5"><code>check_valid_string("())")</code> should return <code>False</code></li>
<li id="test-6"><code>check_valid_string(")(")</code> should return <code>False</code></li>
<li id="test-7"><code>check_valid_string("*")</code> should return <code>True</code></li>
<li id="test-8"><code>check_valid_string("((*)")</code> should return <code>True</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def check_valid_string(s):
    lo = hi = 0
    for c in s:
        if c == '(':
            lo += 1
            hi += 1
        elif c == ')':
            lo -= 1
            hi -= 1
        else:
            lo -= 1
            hi += 1
        if hi < 0:
            return False
        lo = max(lo, 0)
    return lo == 0
```

</details>
