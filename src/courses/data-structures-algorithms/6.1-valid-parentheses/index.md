---
lesson_name: Valid Parentheses
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(n)
  space: O(n)
hints:
  - "When you see a closing bracket, which opening bracket must it match?"
  - "It must match the most recent opening bracket that isn't closed yet, and a stack keeps exactly that on top. This is the *Matching brackets* block in *Stack Basics*."
  - "Template: push each opening bracket. For a closing bracket, return `False` if the stack is empty or its top isn't the matching opener, otherwise pop. At the end, the string is valid only if the stack is empty."
rich_test_results: true
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
<li id="test-8">Performance: 100,000 brackets, within 1 second</li>
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

**Brute force:** repeatedly delete adjacent pairs `"()"`, `"[]"` and `"{}"` until none are left, then check whether the string is empty. Each pass copies the string, and deeply nested input needs about `n / 2` passes, so this is `O(n²)`.

**Bottleneck:** each pass rescans the whole string to remove a single pair.

**Optimal idea:** scan once with a stack of unclosed opening brackets. Each closing bracket must match the top of the stack.

**Why it's correct:** in a valid string, every closing bracket closes the most recently opened bracket that's still open, which is the top of the stack. A mismatch, a closing bracket with nothing open, or anything left open at the end makes the string invalid, and those are the only three ways it can be invalid.

**Complexity:** `O(n)` time for one pass. `O(n)` space for the stack.

**Common mistakes:** returning `True` at the end without checking that the stack is empty, which accepts `"("`. Popping from an empty stack on a leading `)`, which raises `IndexError`.

</details>
