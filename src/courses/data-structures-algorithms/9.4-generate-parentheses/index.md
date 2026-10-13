---
lesson_name: Generate Parentheses
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(4ⁿ / √n)
  space: O(n)
hints:
  - "Build the string one character at a time. When is it allowed to add `(`, and when is it allowed to add `)`?"
  - "You can add `(` while fewer than `n` have been used, and `)` only while there are more `(` than `)` so far. Any string built by following those two rules is well-formed."
  - "Template: a recursive `backtrack(current, open_count, close_count)` that saves `current` when its length is `2 * n`, and otherwise tries adding `(` and `)` when the rules allow."
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

**Brute force:** generate all `2^(2n)` strings of `(` and `)` and keep the well-formed ones, checking each in `O(n)`. That's `O(2^(2n)·n)`.

**Bottleneck:** most of those strings break the rules early, for example by starting with `)`, but the brute force still builds them to full length.

**Optimal idea:** build strings one character at a time and only add a character when the result can still become well-formed. That way only valid prefixes are ever extended.

**Why it's correct:** a prefix can be completed to a well-formed string exactly when it uses at most `n` opens and never has more closes than opens. The two rules keep both conditions true, so every finished string is well-formed. Every well-formed string is reached, because each of its prefixes satisfies the rules.

**Complexity:** the number of results is the `n`-th Catalan number, about `4ⁿ / n^1.5`, and each takes `O(n)` to build, so `O(4ⁿ / √n)` time. `O(n)` space for the recursion, not counting the output.

**Common mistakes:** allowing `)` whenever `close_count < n`, which produces strings such as `")("`. Forgetting the `n = 0` case, which should return `[""]`, a list holding one empty string.

</details>
