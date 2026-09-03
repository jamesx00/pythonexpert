---
lesson_name: Longest Common Subsequence
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

### Longest Common Subsequence

Given two strings `a` and `b`, write a function `longest_common_subsequence(a, b)` that returns the length of their longest common subsequence — the longest sequence of characters that appears in both strings in the same relative order, though not necessarily contiguously.

For example, with `a = "abcde"` and `b = "ace"`, the subsequence `"ace"` appears in both in order, so `longest_common_subsequence("abcde", "ace")` should return `3`.

---

### Tests

<ul>
<li id="test-1"><code>longest_common_subsequence("abcde", "ace")</code> should return <code>3</code></li>
<li id="test-2"><code>longest_common_subsequence("abc", "abc")</code> should return <code>3</code></li>
<li id="test-3"><code>longest_common_subsequence("abc", "def")</code> should return <code>0</code></li>
<li id="test-4"><code>longest_common_subsequence("", "abc")</code> should return <code>0</code></li>
<li id="test-5"><code>longest_common_subsequence("bsbininm", "jmjkbkjkv")</code> should return <code>1</code></li>
<li id="test-6"><code>longest_common_subsequence("oxcpqrsvwf", "shmtulqrypy")</code> should return <code>2</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def longest_common_subsequence(a, b):
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]
```

</details>
