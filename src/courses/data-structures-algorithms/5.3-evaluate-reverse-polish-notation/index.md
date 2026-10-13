---
lesson_name: Evaluate Reverse Polish Notation
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n)
  space: O(n)
hints:
  - "When you reach an operator, which two numbers does it apply to?"
  - "It applies to the two most recent numbers that haven't been used yet, which is exactly the top two of a stack (see *Stack Basics*). The result goes back on the stack as a new number."
  - "Template: push numbers as `int`. For an operator, pop `b` then `a`, push `a op b`, and use `int(a / b)` for division. Return the last value on the stack."
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

**Brute force:** repeatedly find the first operator in the list, replace it and its two operands with the result, and start again. Each replacement rebuilds the list, so this is `O(n²)`.

**Bottleneck:** after every operation the scan starts again from the beginning, although the operands an operator needs are always the most recent unused values.

**Optimal idea:** scan once with a stack. Numbers are pushed, and an operator pops its two operands and pushes the result.

**Why it's correct:** in postfix notation, each operator's operands are the two values produced immediately before it, which are the top two of the stack. Pushing the result makes it the operand for the next operator that needs it. A valid expression leaves exactly one value at the end.

**Complexity:** `O(n)` time for one pass. `O(n)` space for the stack.

**Common mistakes:** popping the operands in the wrong order. The first pop is the *right* operand, so `["7", "2", "-"]` is `7 - 2`, not `2 - 7`. Using `a // b`, which rounds toward negative infinity: `6 // -3` is fine, but `-7 // 2` is `-4` where truncation gives `-3`.

</details>
