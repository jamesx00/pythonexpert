---
lesson_name: "Warm-up: Generate Binary Strings"
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

### Warm-up: Generate Binary Strings

Write a function `binary_strings(n)` that returns **every** string of length `n` made of the characters `"0"` and `"1"`, in ascending order. For `n = 0`, return `[""]` (one empty string).

For example, `binary_strings(2)` returns `["00", "01", "10", "11"]`.

This is the smallest possible backtracking problem: at each position you have two choices. Practise the **choose → explore → un-choose** rhythm:

```python
path.append("0")   # choose
backtrack()        # explore
path.pop()         # un-choose
```

**Hint:** keep a `path` list. When `len(path) == n`, add `"".join(path)` to the results. Trying `"0"` before `"1"` gives ascending order automatically.

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

The recursion forms a decision tree with depth `n` and 2 branches per level, so it produces `2ⁿ` strings. The `pop()` after each recursive call restores `path` so the next choice starts from a clean state. Forgetting it is the most common backtracking bug.

</details>
