---
lesson_name: Generate Parentheses
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

### Generate Parentheses

Write a function `generate_parentheses(n)` that returns every possible string of `n` pairs of parentheses that is well-formed, as a list of strings. The order of the strings in the returned list does not matter.

A string of parentheses is well-formed when every `(` has a matching `)` later in the string, and at no point while scanning left to right does the count of `)` exceed the count of `(`. For `n = 2` there are exactly two well-formed arrangements: `"(())"` and `"()()"`.

---

### Tests

<ul>
<li id="test-1"><code>generate_parentheses(1)</code> should return <code>["()"]</code></li>
<li id="test-2"><code>generate_parentheses(2)</code> should return <code>["(())", "()()"]</code> (any order)</li>
<li id="test-3"><code>generate_parentheses(3)</code> should return <code>["((()))", "(()())", "(())()", "()(())", "()()()"]</code> (any order)</li>
<li id="test-4"><code>generate_parentheses(4)</code> should return all 14 well-formed arrangements for 4 pairs (any order)</li>
<li id="test-5"><code>generate_parentheses(0)</code> should return <code>[""]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def generate_parentheses(n):
    result = []

    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)

    backtrack('', 0, 0)
    return result
```

</details>
