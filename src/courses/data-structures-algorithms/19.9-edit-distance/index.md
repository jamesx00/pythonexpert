---
lesson_name: Edit Distance
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

### Edit Distance

Given two strings `a` and `b`, write a function `edit_distance(a, b)` that returns the minimum number of single-character insertions, deletions, or substitutions needed to turn `a` into `b`.

For example, turning `"plane"` into `"plant"` only needs one substitution — swap the final `e` for a `t` — so `edit_distance("plane", "plant")` should return `1`.

---

### Tests

<ul>
<li id="test-1"><code>edit_distance("plane", "plant")</code> should return <code>1</code></li>
<li id="test-2"><code>edit_distance("abc", "abc")</code> should return <code>0</code></li>
<li id="test-3"><code>edit_distance("", "abc")</code> should return <code>3</code></li>
<li id="test-4"><code>edit_distance("draft", "crate")</code> should return <code>3</code></li>
<li id="test-5"><code>edit_distance("sunday", "saturday")</code> should return <code>3</code></li>
<li id="test-6"><code>edit_distance("a", "b")</code> should return <code>1</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def edit_distance(a, b):
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[n][m]
```

</details>
