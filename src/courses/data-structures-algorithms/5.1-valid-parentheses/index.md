---
lesson_name: Valid Parentheses
code_editor: True
code_execution: True
adding_file_allowed: False
section: Stack
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

### Valid Parentheses

Write a function `is_valid(s)` that takes a string made up only of the characters `(`, `)`, `{`, `}`, `[`, and `]`, and returns `True` if every opening bracket is closed by the matching type of bracket in the correct order, and `False` otherwise.

A string is balanced when each closing bracket matches the most recently opened bracket that hasn't been closed yet, and every bracket is eventually closed. For example, `"{[()]}"` is balanced, but `"{[(])}"` is not, because the `]` closes before the `(` that came after it.

---

### Tests

<ul>
<li id="test-1"><code>is_valid("()")</code> should return <code>True</code></li>
<li id="test-2"><code>is_valid("()[]{}")</code> should return <code>True</code></li>
<li id="test-3"><code>is_valid("(]")</code> should return <code>False</code></li>
<li id="test-4"><code>is_valid("([)]")</code> should return <code>False</code></li>
<li id="test-5"><code>is_valid("{[]}")</code> should return <code>True</code></li>
<li id="test-6"><code>is_valid("(")</code> should return <code>False</code></li>
<li id="test-7"><code>is_valid("")</code> should return <code>True</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def is_valid(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)
    return not stack
```

</details>
