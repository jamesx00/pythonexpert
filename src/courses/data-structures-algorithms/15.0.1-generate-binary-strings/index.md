---
lesson_name: "Warm-up: Generate Binary Strings"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(2ⁿ · n)
  space: O(n)
hints:
  - "At each of the `n` positions you pick `\"0\"` or `\"1\"`. How do you try one, explore everything after it, and then try the other?"
  - "Use *The Template* from *Backtracking Basics*: keep a `path` list, and when `len(path) == n` record `\"\".join(path)`. Otherwise loop over `\"01\"`: append, recurse, pop. Trying `\"0\"` before `\"1\"` gives ascending order for free."
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

### Warm-up: Generate Binary Strings

Write a function `binary_strings(n)` that returns **every** string of length `n` made of the characters `"0"` and `"1"`, in ascending order. For `n = 0`, return `[""]` (one empty string).

For example, `binary_strings(2)` returns `["00", "01", "10", "11"]`.

This is the smallest possible backtracking problem: at each position you have two choices. Practise the **choose → explore → un-choose** rhythm:

```python
path.append("0")   # choose
backtrack()        # explore
path.pop()         # un-choose
```

---

### Tests

<ul>
<li id="test-1"><code>binary_strings(2)</code> should return <code>[&#x27;00&#x27;, &#x27;01&#x27;, &#x27;10&#x27;, &#x27;11&#x27;]</code></li>
<li id="test-2"><code>binary_strings(1)</code> should return <code>[&#x27;0&#x27;, &#x27;1&#x27;]</code></li>
<li id="test-3"><code>binary_strings(0)</code> should return <code>[&#x27;&#x27;]</code></li>
<li id="test-4"><code>binary_strings(3)</code> should return <code>[&#x27;000&#x27;, &#x27;001&#x27;, &#x27;010&#x27;, &#x27;011&#x27;, &#x27;100&#x27;, &#x27;101&#x27;, &#x27;110&#x27;, &#x27;111&#x27;]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def binary_strings(n):
    result = []
    path = []

    def backtrack():
        if len(path) == n:
            result.append("".join(path))
            return
        for ch in "01":
            path.append(ch)
            backtrack()
            path.pop()

    backtrack()
    return result
```

**Brute force:** count from `0` to `2ⁿ - 1` and format each number as an `n`-digit binary string with `format(i, f"0{n}b")`. That's also `O(2ⁿ · n)`, and it's a fine answer, but it skips the backtracking rhythm this warm-up is for.

**Bottleneck:** there isn't a faster way. The output itself has `2ⁿ` strings of length `n`, so any solution takes at least `O(2ⁿ · n)`.

**Optimal idea:** build the string one position at a time. At each position, choose `"0"`, explore every string that starts that way, un-choose it, then do the same with `"1"`.

**Why it's correct:** every string is one sequence of `n` choices, and the recursion tries every choice at every position, so each string is recorded exactly once. Because `"0"` is tried before `"1"` at every position, the strings come out in ascending order.

**Complexity:** `O(2ⁿ · n)` time: `2ⁿ` results, each joined in `O(n)`. `O(n)` extra space for `path` and the recursion, not counting the output.

**Common mistakes:** forgetting `path.pop()`, so the path keeps growing. Returning `[]` instead of `[""]` for `n = 0`: there's exactly one string of length 0.

</details>
