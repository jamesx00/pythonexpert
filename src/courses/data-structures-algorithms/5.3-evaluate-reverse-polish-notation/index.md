---
lesson_name: Evaluate Reverse Polish Notation
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

### Evaluate Reverse Polish Notation

Write a function `evaluate_rpn(tokens)` that evaluates an arithmetic expression written in Reverse Polish Notation (postfix notation) and returns the result as an integer.

`tokens` is a list of strings, where each element is either an integer (possibly negative) or one of the operators `+`, `-`, `*`, `/`. In RPN, operators come after their operands: reading left to right, whenever you hit an operator you apply it to the two most recently seen operands and replace them with the result. Division between integers should truncate toward zero. For example, the tokens `["4", "13", "5", "/", "+"]` mean "4 + (13 / 5)", which is `4 + 2 = 6`.

---

### Tests

<ul>
<li id="test-1"><code>evaluate_rpn(["2", "1", "+", "3", "*"])</code> should return <code>9</code></li>
<li id="test-2"><code>evaluate_rpn(["4", "13", "5", "/", "+"])</code> should return <code>6</code></li>
<li id="test-3"><code>evaluate_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])</code> should return <code>22</code></li>
<li id="test-4"><code>evaluate_rpn(["5"])</code> should return <code>5</code></li>
<li id="test-5"><code>evaluate_rpn(["7", "2", "-"])</code> should return <code>5</code></li>
<li id="test-6"><code>evaluate_rpn(["6", "-3", "/"])</code> should return <code>-2</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def evaluate_rpn(tokens):
    stack = []
    ops = {'+', '-', '*', '/'}
    for tok in tokens:
        if tok in ops:
            b = stack.pop()
            a = stack.pop()
            if tok == '+':
                stack.append(a + b)
            elif tok == '-':
                stack.append(a - b)
            elif tok == '*':
                stack.append(a * b)
            else:
                stack.append(int(a / b))
        else:
            stack.append(int(tok))
    return stack[-1]
```

</details>
