---
lesson_name: Min Stack
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

### Min Stack

Design a stack class named `MinStack` that supports the usual stack operations, but can also report its smallest element at any time in constant time.

Implement these methods:
- `push(val)` — pushes `val` onto the stack.
- `pop()` — removes the element on top of the stack.
- `top()` — returns the element on top of the stack without removing it.
- `get_min()` — returns the smallest element currently in the stack.

For example, after pushing `5`, `3`, `7` in that order, `get_min()` should return `3`. If you then `pop()` (removing `7`) and `pop()` again (removing `3`), `get_min()` should return `5`, since `5` is the only value left.

---

### Tests

<ul>
<li id="test-1">push 5, push 3, push 7 &mdash; <code>get_min()</code> should return <code>3</code></li>
<li id="test-2">push 5, push 3, push 7, pop &mdash; <code>get_min()</code> should return <code>3</code></li>
<li id="test-3">push 5, push 3, push 7, pop, pop &mdash; <code>get_min()</code> should return <code>5</code></li>
<li id="test-4">push -2, push 0, push -3 &mdash; <code>get_min()</code> should return <code>-3</code>, then after pop, <code>top()</code> should return <code>0</code> and <code>get_min()</code> should return <code>-2</code></li>
<li id="test-5">push 1, push 1, push 1 &mdash; <code>get_min()</code> should return <code>1</code> after each pop</li>
<li id="test-6">push 4 &mdash; <code>top()</code> and <code>get_min()</code> should both return <code>4</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]
```

</details>
