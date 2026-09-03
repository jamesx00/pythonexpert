---
lesson_name: Word Break
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

### Word Break

Write a function `word_break(s, word_dict)` that takes a string `s` and a list of dictionary words `word_dict`, and returns `True` if `s` can be split into a sequence of one or more dictionary words placed back to back with nothing left over, or `False` otherwise. Each dictionary word may be reused as many times as needed.

For example, given `s = "pineapplepen"` and `word_dict = ["pine", "apple", "pen"]`, the string can be split as `"pine" + "apple" + "pen"`, so the function should return `True`.

---

### Tests

<ul>
<li id="test-1"><code>word_break("pineapplepen", ["pine", "apple", "pen"])</code> should return <code>True</code></li>
<li id="test-2"><code>word_break("catsandog", ["cats", "dog", "sand", "and", "cat"])</code> should return <code>False</code></li>
<li id="test-3"><code>word_break("leetcode", ["leet", "code"])</code> should return <code>True</code></li>
<li id="test-4"><code>word_break("applepenapple", ["apple", "pen"])</code> should return <code>True</code></li>
<li id="test-5"><code>word_break("aaaaaaa", ["aaaa", "aaa"])</code> should return <code>True</code></li>
<li id="test-6"><code>word_break("aaaaaaab", ["aaaa", "aaa"])</code> should return <code>False</code></li>
<li id="test-7"><code>word_break("", ["a"])</code> should return <code>True</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def word_break(s, word_dict):
    words = set(word_dict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[n]
```

</details>
